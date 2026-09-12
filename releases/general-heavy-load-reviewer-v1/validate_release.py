#!/usr/bin/env python3
"""Clean replay, exact search reproduction, recovery and navigation checks."""
from pathlib import Path
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-heavy-load-family-v1'


def main():
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().strip('\0').split('\0')
    commands=['check_local.py','probe_frontiers.py','probe_profiles.py','verify_applications.py']
    runs=[]
    with tempfile.TemporaryDirectory(prefix='murty-heavy-family-') as directory:
        clean=Path(directory)
        for name in paths:
            source=ROOT/name
            if source.is_file():
                target=clean/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        catalog=json.loads((clean/RESEARCH/'EVIDENCE_STORAGE.json').read_text())
        for script in commands:
            if script=='verify_applications.py':
                # Reproduced raw bytes match every original hash, then the
                # application check runs using the archived streams alone.
                for name,meta in catalog['files'].items():
                    raw=(clean/RESEARCH/name).read_bytes()
                    assert len(raw)==meta['original_bytes'] and hashlib.sha256(raw).hexdigest()==meta['original_sha256'],name
                    (clean/RESEARCH/name).unlink()
            command=[sys.executable,RESEARCH+'/'+script]
            result=subprocess.run(command,cwd=clean,env=env,capture_output=True,text=True)
            assert result.returncode==0,(script,result.stdout,result.stderr)
            runs.append(dict(command='python '+RESEARCH+'/'+script,returncode=0,
                             stdout_sha256=hashlib.sha256(result.stdout.encode()).hexdigest()))
            print('PASS',script,flush=True)
        reproduced=['local_verification.json','frontier_summary.json','profile_summary.json','application_verification.json']
        for name in reproduced:
            assert (clean/RESEARCH/name).read_bytes()==(ROOT/RESEARCH/name).read_bytes(),name
    changed=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
    markdown=[ROOT/p for p in changed if p.endswith('.md')];links=0
    for file in markdown:
        for m in re.finditer(r'\[[^\]]*\]\(([^)\s]+)\)',file.read_text()):
            target=m.group(1).split('#')[0]
            if not target or re.match(r'^[a-z]+:',target):continue
            assert (file.parent/target).exists(),(str(file),target)
            links+=1
    for name in ['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md']:
        body=(ROOT/name).read_text()
        assert 'general-heavy-load-reviewer-v1/README.md' in body
        assert 'n34-reviewer-v2/README.md' in body and 'n35-reviewer-v1/README.md' in body
    report=dict(status='PASS',date='2026-09-12',python=platform.python_version(),replay=runs,
        reproduced_summary_files=reproduced,all_three_raw_study_streams_reproduced_exactly=True,
        verification_from_encoded_evidence_without_raw_streams=True,
        navigation=dict(changed_markdown_files=len(markdown),local_links_checked=links,status='PASS'),
        scope='New general family and application study; existing fixed-order proofs and ledgers are unchanged.',external_review='OPEN')
    (HERE/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
