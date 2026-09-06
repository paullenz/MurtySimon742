#!/usr/bin/env python3
"""Losslessly reconstruct the redundant pretty-printed column JSON from a ledger.

With --original, check byte identity by SHA256 without writing the reconstruction.
The ledger contains each full column-state record, including all capacities.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def file_hash(path):
    result=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            result.update(block)
    return result.hexdigest()


def main(ledger,original,output):
    digest=hashlib.sha256()
    sink=output.open('wb') if output else None
    length=0
    def emit(data):
        nonlocal length
        length+=len(data)
        digest.update(data)
        if sink:
            sink.write(data)
    count=0
    with gzip.open(ledger,'rt',encoding='ascii') as f:
        for line in f:
            row=json.loads(line)
            if row['kind'] not in ('all_columns','survives'):
                continue
            emit(b'[\n' if count==0 else b',\n')
            body=json.dumps(row,indent=2,sort_keys=True)
            emit(('\n'.join('  '+line for line in body.split('\n'))).encode('ascii'))
            count+=1
    emit(b'\n]\n' if count else b'[]\n')
    if sink:
        sink.close()
    if original and digest.hexdigest()!=file_hash(original):
        raise ValueError('Reconstruction differs from original column JSON')
    print(json.dumps(dict(bytes=length,sha256=digest.hexdigest(),column_states=count,
                          original_bytes_match=bool(original)),sort_keys=True))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ledger',type=Path)
    parser.add_argument('--original',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    main(args.ledger,args.original,args.output)
