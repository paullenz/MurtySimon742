#!/usr/bin/env python3
"""Replay this audit using the frozen reviewer ZIP supplied with edition 1."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import stat
import subprocess
import sys
import zipfile

REVIEWER_SHA='ff5a88f4202fb1e201f52e7e6ec0b50f88248cd43493eee78f120a3c1de15c3d'
CANDIDATE_SHA='0588c85900762184040dfb313c89d36349f2a8183db5cbc91a1ee50915cb4e95'


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()


def unpack(path,target):
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            p=Path(info.filename)
            if p.is_absolute() or '..' in p.parts or stat.S_ISLNK(info.external_attr>>16):raise ValueError('Unsafe ZIP member')
        if z.testzip() is not None:raise ValueError('ZIP CRC failure')
        z.extractall(target)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reviewer-zip',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--prepare-only',action='store_true',help='Check/extract inputs without running the audit')
    args=parser.parse_args();here=Path(__file__).resolve().parent
    for row in json.loads((here/'MANIFEST.json').read_text())['files']:
        path=here/row['path']
        if path.stat().st_size!=row['bytes'] or sha(path)!=row['sha256']:raise ValueError('Audit payload mismatch: '+row['path'])
    archive=args.reviewer_zip.resolve()
    if sha(archive)!=REVIEWER_SHA:raise ValueError('Wrong reviewer archive')
    work=args.output.resolve();work.mkdir(parents=True,exist_ok=False)
    unpack(archive,work/'reviewer')
    candidate=work/'reviewer/N25_Reviewer_Package_v1/N25_Full_Chain_Candidate_Evidence_2026-09-06_v1.zip'
    if sha(candidate)!=CANDIDATE_SHA:raise ValueError('Wrong candidate archive')
    unpack(candidate,work)
    evidence=work/'N25_Full_Chain_Candidate_2026-09-06_v1'
    unpack(evidence/'historical/N25_Delta14_Document_Review_Evidence_2026-09-06.zip',work/'original')
    shutil.copytree(work/'original/N25_Delta14_Document_Review',work/'review_evidence')
    run_dir=work/'redteam_v1';run_dir.mkdir()
    for name in ['structural_attack.py','arithmetic_attack.py','helper_boundary_attack.py']:
        shutil.copy2(here/name,run_dir/name)
    for row in json.loads((here/'AUDIT_INPUTS.json').read_text())['files']:
        path=work/row['path']
        if sha(path)!=row['sha256']:raise ValueError('Audit input mismatch: '+row['path'])
    if args.prepare_only:
        print(json.dumps(dict(status='INPUTS_PREPARED_ONLY_AUDIT_NOT_RUN',output=str(work))));return
    for name in ['structural_attack','arithmetic_attack','helper_boundary_attack']:
        with (run_dir/(name+'.log')).open('w') as log:
            subprocess.run([sys.executable,'-I','-B',str(run_dir/(name+'.py'))],stdout=log,stderr=subprocess.STDOUT,check=True)
        print(json.dumps(dict(completed=name)),flush=True)
    for name in ['structural','arithmetic']:
        if json.loads((run_dir/(name+'_results.json')).read_text())['status']!='PASS':raise ValueError('Audit failed')
    print(json.dumps(dict(status='RED_TEAM_CHECKS_REPRODUCED',external_mathematical_review=False,output=str(work))))


if __name__=='__main__':main()
