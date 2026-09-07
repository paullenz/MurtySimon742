#!/usr/bin/env python3
"""Cross-language check of six saved outer states: fully labelled enumeration,
augmenting-path matching and exhaustive subsets. Checks the C++ orbit reduction.
The full production replay uses columns.cpp check with threshold matching.
"""
import gzip,hashlib,importlib.util,json,math
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('second',ROOT/'general_independent.py')
second=importlib.util.module_from_spec(spec);spec.loader.exec_module(second)
second.A=11;second.B=15

def stable(x):return json.dumps(x,separators=(',',':'))

def main():
    rows=[json.loads(s) for s in gzip.open(ROOT/'validation_frontier.jsonl.gz','rt')]
    cuts=iter(json.loads(s) for s in gzip.open(ROOT/'validation_cuts.jsonl.gz','rt'))
    reference=[json.loads(s) for s in (ROOT/'validation_columns.jsonl').read_text().splitlines()]
    total_labelled=total_orbits=0
    for state,(k,r,ds,rs,lo) in enumerate(rows):
        domains=Counter()
        for excess in second.weak_compositions(r-sum(lo),len(ds)):
            R=tuple(l+x for l,x in zip(lo,excess))
            if max(R)>len(rs):continue
            canonical=[]
            for d in sorted(set(ds)):
                canonical.extend(sorted(R[i] for i,di in enumerate(ds) if di==d))
            domains[tuple(canonical)]+=1
        digest=hashlib.sha256();counts=Counter()
        for R in sorted(domains):
            caps=second.neighbours_bound(tuple(ds),tuple(rs),R)
            required=sum(max(0,d-x) for d,x in zip(ds,R))
            if sum(caps)>=required:
                while True:
                    newer=[]
                    for b,cap in enumerate(caps):
                        newer.append(max(q for q in range(cap+1) if sum(w!=b and rs[w]+caps[w]>=q-1 for w in range(len(rs)))>=q))
                    if newer==caps:break
                    caps=newer
            kind=0;mask=0
            if sum(caps)>=required:
                record=next(cuts);assert record[:3]==[state,list(R),caps];mask=record[3]
                failing=[]
                for subset in range(1,1<<len(ds)):
                    S=[i for i in range(len(ds)) if subset>>i&1]
                    demand=sum(max(0,ds[i]-R[i]) for i in S)
                    available=sum(min(cap,sum(ds[i]<rb+cap and ds[i]<=rb+R[i] for i in S)) for rb,cap in zip(rs,caps))
                    if demand>available:failing.append(subset)
                assert bool(mask)==bool(failing)
                if mask:assert mask in failing
                kind=1 if mask else 2
            counts[kind]+=1
            digest.update((stable(R)+stable(caps)+str(kind)+':'+str(mask)+'\n').encode())
        actual={'state':state,'canonical':len(domains),'labelled':sum(domains.values()),'total_reject':counts[0],'cut_reject':counts[1],'survives':counts[2],'sha256':digest.hexdigest()}
        assert actual==reference[state]
        total_labelled+=sum(domains.values());total_orbits+=len(domains)
    assert next(cuts,None) is None
    result={'status':'PASS','states':len(rows),'fully_labelled_columns':total_labelled,'canonical_columns':total_orbits,
            'matching':'augmenting paths','subsets':'exhaustive','scope':'selected six-state cross-language validation; full replay separate'}
    (ROOT/'COLUMN_SAMPLE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

if __name__=='__main__':main()
