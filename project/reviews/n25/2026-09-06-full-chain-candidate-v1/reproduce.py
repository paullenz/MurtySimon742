#!/usr/bin/env python3
"""Integrity verification and isolated exact replay of the N=25 candidate.

This runner never labels arithmetic reproduction as mathematical verification.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

SCOPES={
    'd15_157':(9,157,[3,2]),
    'd15_156':(9,156,[3,2]),
    'd14_156':(10,156,[5,4,3,2]),
    'd14_156_k1':(10,156,[1]),
}


def sha(path):
    digest=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):
            digest.update(block)
    return digest.hexdigest()


def run(command,log=None):
    if log is None:
        subprocess.run(command,check=True)
    else:
        with log.open('w') as stream:
            subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,check=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    modes=parser.add_mutually_exclusive_group(required=True)
    modes.add_argument('--verify-only',action='store_true')
    modes.add_argument('--replay',action='store_true')
    parser.add_argument('--output',type=Path)
    parser.add_argument('--scopes',nargs='+',choices=list(SCOPES),default=list(SCOPES))
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    manifest=json.loads((root/'MANIFEST.json').read_text())
    for item in manifest['files']:
        path=root/item['path']
        if not path.is_relative_to(root) or '..' in Path(item['path']).parts:
            raise ValueError('Invalid manifest path')
        if path.stat().st_size!=item['bytes'] or sha(path)!=item['sha256']:
            raise ValueError('Integrity mismatch: '+item['path'])
    print(json.dumps(dict(status='MANIFEST_MATCH',files=len(manifest['files'])),sort_keys=True),flush=True)
    prefix=[sys.executable,'-I','-B']
    if args.verify_only:
        for name in ('d14_156','d14_156_k1'):
            run(prefix+[str(root/'check_column_certificates.py'),
                        str(root/name/'primary_ledger.jsonl.gz'),
                        str(root/name/'hall_certificates.json')])
        print(json.dumps(dict(status='PRESERVED_BYTES_AND_EQUALITY_CERTIFICATES_CHECKED',
                              mathematical_proof_verified=False),sort_keys=True))
        return
    if args.output is None:
        parser.error('--replay requires a new --output directory')
    output=args.output.resolve()
    output.mkdir(parents=True,exist_ok=False)
    for name in args.scopes:
        a,edges,ks=SCOPES[name]
        folder=output/name
        params=['--a',str(a),'--edges',str(edges),'--ks']+list(map(str,ks))
        for implementation in ('primary','independent'):
            run(prefix+[str(root/f'general_{implementation}.py')]+params+
                ['--output',str(folder)],output/f'{name}_{implementation}.log')
        for filename in ('primary_summary.json','primary_ledger.jsonl.gz'):
            if sha(folder/filename)!=sha(root/name/filename):
                raise ValueError('Fresh output mismatch: '+name+'/'+filename)
        run(prefix+[str(root/'compare_runs.py'),str(folder),str(folder),
                    str(folder/'comparison.json')],output/f'{name}_comparison.log')
        if name.startswith('d14'):
            run(prefix+[str(root/'column_hall.py'),str(folder/'primary_ledger.jsonl.gz'),
                        str(folder/'hall_certificates.json')],output/f'{name}_hall.log')
            if sha(folder/'hall_certificates.json')!=sha(root/name/'hall_certificates.json'):
                raise ValueError('Fresh subset-certificate mismatch: '+name)
            run(prefix+[str(root/'check_column_certificates.py'),str(folder/'primary_ledger.jsonl.gz'),
                        str(folder/'hall_certificates.json')],output/f'{name}_hall_check.log')
        print(json.dumps(dict(scope=name,status='FRESH_EXACT_REPLAY_MATCH'),sort_keys=True),flush=True)
    print(json.dumps(dict(status='REQUESTED_NEW_SCOPES_REPRODUCED',scopes=args.scopes,
                          mathematical_proof_verified=False),sort_keys=True))


if __name__=='__main__':
    main()
