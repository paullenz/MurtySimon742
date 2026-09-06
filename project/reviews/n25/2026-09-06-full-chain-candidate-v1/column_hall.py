#!/usr/bin/env python3
"""Exact subset-capacity cuts on explicitly preserved surviving column states.

For S subset A, required=sum(max(0,d[a]-R[a])) over a in S.
At source b, at most min(c[b], number of eligible a in S) can be selected.
Eligibility: d[a] <= rho[b]+c[b]-1 and d[a] <= rho[b]+R[a].
Every c[b] is the already certified previous-stage upper bound on q[b].
No max-flow/SAT solver or graph-realizability inference is used.
"""
import argparse
from collections import Counter
import hashlib
import gzip
import json
from pathlib import Path


def cut(ds, rs, cols, caps):
    for mask in range(1, 1 << len(ds)):
        subset = [a for a in range(len(ds)) if mask & (1 << a)]
        required = sum(max(0, ds[a]-cols[a]) for a in subset)
        by_source = [min(c, sum(ds[a] <= rb+c-1 and ds[a] <= rb+cols[a]
                               for a in subset)) for rb, c in zip(rs, caps)]
        if required > sum(by_source):
            return dict(subset=subset, required=required,
                        by_source=by_source, available=sum(by_source))
    return None


def run(path, output):
    if path.name.endswith('.jsonl.gz'):
        stream = gzip.open(path, 'rt', encoding='ascii')
        records = (json.loads(line) for line in stream)
    else:
        records = json.loads(path.read_text())
    certificates, survivors = [], []
    for record in records:
        if record['kind'] != 'survives':
            continue
        k, r, ds, rs = json.loads(record['key'])
        for col in record['witness']['survivors']:
            witness = cut(ds, rs, col['columns'], col['refined_caps'])
            result = dict(key=record['key'], columns=col['columns'],
                          caps=col['refined_caps'], witness=witness)
            (certificates if witness else survivors).append(result)
    result = dict(input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  checked=len(certificates)+len(survivors),
                  eliminated=len(certificates), surviving_columns=len(survivors),
                  surviving_outer_states=len({s['key'] for s in survivors}),
                  certificates=certificates, survivors=survivors,
                  mathematical_status='CANDIDATE_NECESSARY_CONDITION')
    output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    if path.name.endswith('.jsonl.gz'):
        stream.close()
    print(json.dumps({k:v for k,v in result.items()
                      if k not in ('certificates', 'survivors')}, sort_keys=True))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args=parser.parse_args()
    run(args.input, args.output)
