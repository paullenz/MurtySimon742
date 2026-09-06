#!/usr/bin/env python3
"""Verify the frozen reviewer package and replay the complete numerical route.

The original candidate ZIP is unchanged. This wrapper adds extraction,
integrity checks and the otherwise separately nested Delta14/e157 replay.
It does not certify mathematical lemmas or independent external review.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile

ARCHIVE='N25_Full_Chain_Candidate_Evidence_2026-09-06_v1.zip'
ARCHIVE_SHA='0588c85900762184040dfb313c89d36349f2a8183db5cbc91a1ee50915cb4e95'
SCOPES=['d15_157','d15_156','d14_156','d14_156_k1']


def sha(path):
    digest=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):
            digest.update(block)
    return digest.hexdigest()


def verify_manifest(root,name):
    manifest=json.loads((root/name).read_text())
    for row in manifest['files']:
        relative=Path(row['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Invalid manifest path')
        path=root/relative
        if path.stat().st_size!=row['bytes'] or sha(path)!=row['sha256']:
            raise ValueError('Manifest mismatch: '+str(relative))
    return len(manifest['files'])


def extract(archive,target):
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            relative=Path(info.filename)
            if relative.is_absolute() or '..' in relative.parts or stat.S_ISLNK(info.external_attr>>16):
                raise ValueError('Invalid archive member')
        bad=z.testzip()
        if bad is not None:
            raise ValueError('Archive CRC failed: '+bad)
        z.extractall(target)


def run(command,log,cwd):
    with log.open('w') as stream:
        subprocess.run(command,cwd=cwd,stdout=stream,stderr=subprocess.STDOUT,check=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--verify-only',action='store_true')
    mode.add_argument('--replay',action='store_true')
    parser.add_argument('--output',type=Path)
    parser.add_argument('--scopes',nargs='+',choices=SCOPES,default=SCOPES)
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    count=verify_manifest(root,'MANIFEST.json')
    if sha(root/ARCHIVE)!=ARCHIVE_SHA:
        raise ValueError('Wrong frozen candidate ZIP')
    if args.replay and args.output is None:
        parser.error('--replay requires a new --output directory')
    temporary=None
    if args.replay:
        work=args.output.resolve()
        work.mkdir(parents=True,exist_ok=False)
    else:
        temporary=tempfile.TemporaryDirectory(prefix='n25-review-')
        work=Path(temporary.name)
    extract(root/ARCHIVE,work/'unpacked')
    evidence=work/'unpacked/N25_Full_Chain_Candidate_2026-09-06_v1'
    new_count=verify_manifest(evidence,'MANIFEST.json')
    original_zip=evidence/'historical/N25_Delta14_Document_Review_Evidence_2026-09-06.zip'
    extract(original_zip,work/'original')
    original=work/'original/N25_Delta14_Document_Review'
    old_count=verify_manifest(original,'REVIEW_MANIFEST.json')
    prefix=[sys.executable,'-I','-B']
    run(prefix+[str(evidence/'reproduce.py'),'--verify-only'],work/'integrity_and_equality.log',evidence)
    report=dict(status='ALL_MANIFESTS_AND_EQUALITY_CERTIFICATES_CHECKED',
                top_level_files=count,candidate_files=new_count,original_review_files=old_count,
                frozen_candidate_sha256=ARCHIVE_SHA,external_mathematical_review=False,
                independent_machine_reproduction=False)
    print(json.dumps(report,sort_keys=True),flush=True)
    if args.replay:
        original_results=work/'original_replay'
        run(prefix+[str(original/'verify_primary.py'),'--output',str(original_results)],
            work/'original_primary.log',original)
        run(prefix+[str(original/'verify_independent.py'),'--output',str(original_results),
                    '--reference',str(original_results)],work/'original_independent.log',original)
        for name in ('primary_summary.json','primary_ledger.jsonl.gz','primary_column_cases.json','independent_summary.json'):
            if sha(original_results/name)!=sha(original/'results'/name):
                raise ValueError('Original Delta14 output mismatch: '+name)
        run(prefix+[str(original/'test_verifiers.py')],work/'original_tests.log',original)
        print(json.dumps(dict(scope='original_delta14_157',status='EXACT_REPLAY_AND_TESTS_MATCH')),flush=True)
        run(prefix+[str(evidence/'reproduce.py'),'--replay','--output',str(work/'new_replay'),
                    '--scopes']+args.scopes,work/'new_scopes.log',evidence)
        report.update(status=('FULL_NUMERICAL_ROUTE_REPRODUCED' if set(args.scopes)==set(SCOPES)
                              else 'PARTIAL_NUMERICAL_ROUTE_REPRODUCED'),
                      original_delta14_replayed=True,new_scopes=args.scopes)
        (work/'REPLAY_REPORT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
        print(json.dumps(report,sort_keys=True))
    if temporary:
        temporary.cleanup()


if __name__=='__main__':
    main()
