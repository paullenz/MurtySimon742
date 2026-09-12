#!/usr/bin/env python3
"""Clean staged-tree reproduction, archive-only exact replay and link checks."""
from pathlib import Path
import hashlib,json,os,platform,re,shutil,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-joint-routing-pilot-v1'


def main():
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().strip('\0').split('\0')
    runs=[]
    with tempfile.TemporaryDirectory(prefix='murty-joint-routing-') as directory:
        clean=Path(directory)
        for name in paths:
            source=ROOT/name
            if source.is_file():
                target=clean/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        catalog=json.loads((clean/RESEARCH/'EVIDENCE_STORAGE.json').read_text())
        for script in ['select_pilot.py','probe.py','catalog.py','replay_frontier.py','check_routing.py','verify.py']:
            if script=='verify.py':
                for name,meta in catalog['files'].items():
                    path=clean/RESEARCH/name;raw=path.read_bytes()
                    assert len(raw)==meta['original_bytes'] and hashlib.sha256(raw).hexdigest()==meta['original_sha256'],name
                    path.unlink()
            result=subprocess.run([sys.executable,RESEARCH+'/'+script],cwd=clean,env=env,capture_output=True,text=True)
            assert result.returncode==0,(script,result.stdout,result.stderr)
            runs.append(dict(command='python '+RESEARCH+'/'+script,returncode=0,stdout_sha256=hashlib.sha256(result.stdout.encode()).hexdigest()))
            print('PASS',script,flush=True)
        reproduced=['pilot_inputs.json','multiplier_catalog.json','frontier_summary.json','routing_verification.json','verification.json','environment.json']
        for name in reproduced:assert (clean/RESEARCH/name).read_bytes()==(ROOT/RESEARCH/name).read_bytes(),name
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
        for package in ['general-joint-routing-reviewer-v1','general-heavy-load-reviewer-v1','n34-reviewer-v2','n35-reviewer-v1']:
            assert package+'/README.md' in body,(name,package)
    report=dict(status='PASS',date='2026-09-12',python=platform.python_version(),replay=runs,
        reproduced_summary_files=reproduced,both_original_streams_reproduced_byte_for_byte=True,
        exact_verification_from_archives_without_raw_streams=True,
        navigation=dict(changed_markdown_files=len(markdown),local_links_checked=links,status='PASS'),
        scope='New general joint-routing lemma and finite applications; canonical fixed-order proof ledgers unchanged.',external_review='OPEN')
    (HERE/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
