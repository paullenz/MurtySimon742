#!/usr/bin/env python3
"""Clean-copy exact replay and publication navigation checks.

Run after staging the intended new files. Reports are regenerated before
final manifest construction; manifests intentionally exclude themselves.
"""
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
AUDIT='project/reviews/n34/2026-09-12-heavy-independent-v1'
N35='project/research/n35/2026-09-12-candidate-v1'


def main():
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().strip('\0').split('\0')
    commands=[
        ['python','project/research/n34/2026-09-12-frontier-v1/verify_upper_layers.py'],
        ['python','project/research/n34/2026-09-12-m290-v1/verify.py'],
        ['python',AUDIT+'/verify_hand.py'],['python',AUDIT+'/verify_v2.py'],
        ['python',AUDIT+'/compare_models.py'],['python',AUDIT+'/verify_count_certificate.py'],
        ['python',N35+'/verify.py'],['python',N35+'/audit_frontier.py']]
    runs=[]
    with tempfile.TemporaryDirectory(prefix='murty-n35-clean-') as directory:
        clean=Path(directory)
        for name in paths:
            source=ROOT/name
            if not source.is_file():continue
            target=clean/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        for command in commands:
            result=subprocess.run([sys.executable,*command[1:]],cwd=clean,env=env,capture_output=True,text=True)
            assert result.returncode==0,(command,result.stdout,result.stderr)
            runs.append(dict(command=' '.join(command),returncode=result.returncode,
                             stdout_sha256=hashlib.sha256(result.stdout.encode()).hexdigest()))
            print('PASS',' '.join(command),flush=True)
        # Confirm regenerated exact reports equal the newly preserved reports.
        reproduced=[]
        for name in [AUDIT+'/hand_verification.json',AUDIT+'/v2_verification.json',
                     AUDIT+'/comparison.json',AUDIT+'/count_certificate.json',
                     N35+'/verification.json',N35+'/frontier_audit.json']:
            assert (clean/name).read_bytes()==(ROOT/name).read_bytes(),name
            reproduced.append(name)
        source='project/research/n34/2026-09-12-frontier-v1/enumerate_frontier.cpp'
        build=subprocess.run(['g++','-O2','-std=c++17',source,'-o','enumerate'],cwd=clean,capture_output=True,text=True)
        assert build.returncode==0,build.stderr
        result=subprocess.run([str(clean/'enumerate'),'fresh.csv'],cwd=clean,capture_output=True,text=True)
        assert result.returncode==0,result.stderr
        original=clean/'project/research/n34/2026-09-12-frontier-v1/FRONTIER.csv'
        assert (clean/'fresh.csv').read_bytes()==original.read_bytes()
        enumeration=dict(status='PASS_EXACT_BYTE_MATCH',profiles_enumerated=77558760,
            stdout=result.stdout,csv_sha256=hashlib.sha256(original.read_bytes()).hexdigest())
        print('PASS complete 77,558,760-profile enumeration; exact CSV byte match',flush=True)
    changed=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
    markdown=[ROOT/name for name in changed if name.endswith('.md')]
    links=0
    for file in markdown:
        body=file.read_text()
        for match in re.finditer(r'\[[^\]]*\]\(([^)\s]+)\)',body):
            target=match.group(1).split('#')[0]
            if not target or re.match(r'^[a-z]+:',target):continue
            assert (file.parent/target).exists(),(str(file.relative_to(ROOT)),target)
            links+=1
    for name in ['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md']:
        body=(ROOT/name).read_text()
        assert 'n34-reviewer-v2/README.md' in body and 'n35-reviewer-v1/README.md' in body
        assert not re.search(r'above\s+`?n=33',body)
        assert 'n34-reviewer-v1/README.md' not in body
    report=dict(status='PASS',schema='n34-v2-n35-v1-clean-validation',python=platform.python_version(),
        exact_replay=runs,reproduced_artifacts=reproduced,demand_enumeration=enumeration,
        navigation=dict(markdown_files=len(markdown),local_links=links,status='PASS'),
        clean_copy='staged/tracked files only; no original raw N34 JSONL or working caches required',
        external_review='OPEN')
    for package in ['n34-reviewer-v2','n35-reviewer-v1']:
        (ROOT/'releases'/package/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
