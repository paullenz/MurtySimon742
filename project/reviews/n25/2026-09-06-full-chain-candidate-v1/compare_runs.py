#!/usr/bin/env python3
"""Compare independently generated summaries and every stored primary column.

Reads the complete compressed rejection ledger, avoiding the redundant large
pretty-printed column JSON. The canonical column hash is defined by the second
implementation. This comparison does not execute either arithmetic scanner.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def main(primary, independent, output):
    first=json.loads((primary/'primary_summary.json').read_text())
    second=json.loads((independent/'independent_summary.json').read_text())
    for name in ('scope','state_count','state_key_sha256','rows','survivors','column_vectors'):
        if first[name]!=second[name]:
            raise ValueError('Comparison failed: '+name)
    canonical=[]
    with gzip.open(primary/'primary_ledger.jsonl.gz','rt',encoding='ascii') as stream:
        for line in stream:
            row=json.loads(line)
            if row['kind'] in ('all_columns','survives'):
                for col in row['witness']['columns']:
                    canonical.append(json.dumps([row['key'],col['columns'],col['required'],
                                                  col['caps'],col['refined_caps']],
                                                 separators=(',',':')))
    if len(canonical)!=second['column_vectors']:
        raise ValueError('Wrong column count')
    digest=hashlib.sha256()
    for line in sorted(canonical):
        digest.update(line.encode('ascii')+b'\n')
    if not canonical:
        digest.update(b'\n')
    if digest.hexdigest()!=second['column_comparison_sha256']:
        raise ValueError('Column fingerprint mismatch')
    result=dict(status='ALL_STATE_KEYS_COUNTS_DISPOSITIONS_AND_COLUMN_CAPS_MATCH',
                state_count=first['state_count'],column_vectors=len(canonical),
                column_sha256=digest.hexdigest(),external_mathematical_review=False)
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('primary',type=Path)
    parser.add_argument('independent',type=Path)
    parser.add_argument('output',type=Path)
    a=parser.parse_args()
    main(a.primary,a.independent,a.output)
