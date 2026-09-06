#!/usr/bin/env python3
"""Separate verifier for coverage and the integer subset inequalities.

Imports neither the subset search nor either arithmetic scan.
Uses their saved, mutually compared column caps as its explicit input premise.
"""
import argparse
import hashlib
import gzip
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main(source, evidence):
    raw=source.read_bytes()
    if source.name.endswith('.jsonl.gz'):
        stream=gzip.open(source,'rt',encoding='ascii')
        original=(json.loads(line) for line in stream)
    else:
        original=json.loads(raw)
    certificate=json.loads(evidence.read_text())
    require(certificate['input_sha256']==hashlib.sha256(raw).hexdigest(), 'Wrong input')
    expected={}
    for row in original:
        if row['kind']=='survives':
            for col in row['witness']['survivors']:
                key=(row['key'], tuple(col['columns']))
                require(key not in expected, 'Duplicate input')
                expected[key]=col['refined_caps']
    observed=set()
    for row in certificate['certificates']:
        key=(row['key'],tuple(row['columns']))
        require(key in expected and key not in observed, 'Unexpected or duplicate certificate')
        require(row['caps']==expected[key], 'Unjustified source cap')
        observed.add(key)
        _, _, degrees, residuals=json.loads(row['key'])
        indices=row['witness']['subset']
        require(len(set(indices))==len(indices), 'Repeated label')
        require(indices and all(0<=a<len(degrees) for a in indices), 'Invalid subset')
        demand=0
        for a in indices:
            if degrees[a]>row['columns'][a]:
                demand+=degrees[a]-row['columns'][a]
        bound=[]
        for b in range(len(residuals)):
            eligible=set()
            for a in indices:
                if (degrees[a]-row['columns'][a]<=residuals[b]
                    and degrees[a]-residuals[b]<row['caps'][b]):
                    eligible.add(a)
            bound.append(min(len(eligible), row['caps'][b]))
        require(demand==row['witness']['required'], 'Wrong demand')
        require(bound==row['witness']['by_source'], 'Wrong source bounds')
        require(sum(bound)==row['witness']['available'], 'Wrong total')
        require(demand>sum(bound), 'No strict contradiction')
    for row in certificate['survivors']:
        key=(row['key'],tuple(row['columns']))
        require(key in expected and key not in observed, 'Unexpected survivor')
        observed.add(key)
    require(observed==set(expected), 'Incomplete coverage')
    require(len(expected)==certificate['checked'], 'Wrong check count')
    require(len(certificate['certificates'])==certificate['eliminated'], 'Wrong rejection count')
    require(len(certificate['survivors'])==certificate['surviving_columns'], 'Wrong survivor count')
    if source.name.endswith('.jsonl.gz'):
        stream.close()
    print(json.dumps(dict(status='ALL_CERTIFICATES_AND_COVERAGE_CHECKED',
                          columns=len(expected), rejected=len(certificate['certificates']),
                          remaining=len(certificate['survivors']),
                          external_mathematical_review=False), sort_keys=True))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('certificates', type=Path)
    args=parser.parse_args()
    main(args.source,args.certificates)
