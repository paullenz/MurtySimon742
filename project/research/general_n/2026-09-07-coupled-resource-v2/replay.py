#!/usr/bin/env python3
"""Check preserved evidence and exact certificates; --full repeats all tests.
The default and full replay require only Python's standard library.
"""
from __future__ import annotations
import argparse
import base64
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from coupled import arithmetic_tests, scalar_rows, check_certificate
from verify_certificate import verify


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    report=json.loads((root/'REPORT.json').read_text())
    packed=base64.b64decode((root/'EVIDENCE.json.gz.b64').read_bytes())
    require(hashlib.sha256(packed).hexdigest()==report['evidence']['gzip_sha256'],'evidence archive hash mismatch')
    data=json.loads(gzip.decompress(packed))
    require(set(data)==set(report['evidence']['files']),'evidence coverage mismatch')
    for name,text in data.items():
        entry=report['evidence']['files'][name];raw=text.encode()
        require(len(raw)==entry['bytes'] and hashlib.sha256(raw).hexdigest()==entry['sha256'],f'evidence mismatch: {name}')
    manifest_path=root/'MANIFEST.json'
    if manifest_path.exists():
        for name,entry in json.loads(manifest_path.read_text())['files'].items():
            raw=(root/name).read_bytes()
            require(hashlib.sha256(raw).hexdigest()==entry['sha256'] and len(raw)==entry['bytes'],f'file mismatch: {name}')
    expected=json.loads(data['RESULTS.json'])
    require(arithmetic_tests()==expected['arithmetic_tests'],'arithmetic regression mismatch')
    require(scalar_rows()==expected['scalar_rows'],'scalar results mismatch')
    profile=expected['n27_profile'];certificate=expected['n27_discovery']['certificate']
    primary=check_certificate(profile,certificate)
    require(primary==expected['n27_discovery']['check'],'primary certificate output mismatch')
    separate=verify(profile,certificate)
    require(separate==report['separate_checker_tests']['n27_separate_check'],'separate certificate output mismatch')
    result={'status':'PASS','evidence_files':len(data),'scalar_orders':len(expected['scalar_rows']),
            'primary_certificate':primary,'separate_certificate':separate,
            'full_test_replay':'NOT_REQUESTED',
            'scope':'Exact replay and software checks; universal mathematical review remains OPEN.'}
    if args.full:
        with tempfile.TemporaryDirectory(prefix='murty_coupled_replay_') as td:
            folder=Path(td)
            for name in ['coupled.py','verify_certificate.py','test_coupled.py']:
                shutil.copyfile(root/name,folder/name)
            env=dict(os.environ);env.pop('PYTHONOPTIMIZE',None)
            subprocess.run([sys.executable,'-B',str(folder/'test_coupled.py')],cwd=folder,
                           env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            got=(folder/'TEST_RESULTS.json').read_text()
            require(got==data['TEST_RESULTS.json'],'full test replay byte mismatch')
            result['full_test_replay']='BYTE_FOR_BYTE_PASS'
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
