#!/usr/bin/env python3
"""Exhaustive small domains and deterministic larger challenges for the closed formula."""
from pathlib import Path
from itertools import product
from random import Random
import json
from closed import maxima
HERE=Path(__file__).resolve().parent

def enumerate_maxima(a,b,h,k,j,rho,hi,lo):
    best=[None,None];options=0
    for H,q,p in product(range(a+1),range(a+1),range(b)):
        if H>hi or H>q or q-H>lo or q+rho>a or q+p>=b or p>rho+b-a-1:continue
        e=int(H>=h+1)
        if e>j:continue
        # Independent direct semantic summation, with the ramp as indicators.
        ramp=sum(q+p<=cut for cut in range(h,4*h))
        receiving=min(p,j-e) if rho>=h else 0
        value=H*(h+ramp)+H-2*(e*H-receiving)-4*((q if q>=k+1 else 0)-(p if rho+q>=k else 0))
        options+=1
        if best[e] is None or value>best[e]:best[e]=value
    return tuple(best),options

def main():
    count=options=0;maxpieces=maxcandidates=0
    def check(case):
        nonlocal count,options,maxpieces,maxcandidates
        reference,n=enumerate_maxima(*case);closed=maxima(*case);count+=1;options+=n
        found=tuple(x['value'] for x in closed)
        if found!=reference:
            (HERE/'LOCAL_FAILURE.json').write_text(json.dumps(dict(case=case,reference=reference,closed=closed),indent=2)+'\n')
        assert found==reference,case
        maxpieces=max(maxpieces,*(x['pieces'] for x in closed));maxcandidates=max(maxcandidates,*(x['candidates'] for x in closed))
    for a in range(2,6):
        for b in (a,a+1):
            for rho in range(1,a+1):
                for h in range(2,a+2):
                    for hi in range(a+1) if rho>=h else (0,):
                        for lo in range(a-hi+1):
                            for k in range(a+2):
                                for j in range(b+1):check((a,b,h,k,j,rho,hi,lo))
        print('EXHAUSTED a',a,'cases',count,flush=True)
    small=count;rng=Random(74220260912);larger=[]
    for _ in range(512):
        a=rng.randint(6,32);b=a+rng.randint(0,6);rho=rng.randint(1,a);h=rng.randint(2,a+1)
        hi=rng.randint(0,a) if rho>=h else 0;lo=rng.randint(0,a-hi);k=rng.randint(0,a+1);j=rng.randint(0,b)
        case=(a,b,h,k,j,rho,hi,lo);larger.append(case);check(case)
    (HERE/'larger_local_cases.json').write_text(json.dumps(larger,separators=(',',':'))+'\n')
    report=dict(status='PASS',exhaustive_cases=small,larger_cases=len(larger),total_cases=count,reference_source_options=options,
        small_domain='a=2..5, b=a or a+1, rho=1..a, h=2..a+1, k=0..a+1, j=0..b; all hi+lo<=a with hi=0 if rho<h',
        larger_domain='512 deterministic cases, seed 74220260912, a=6..32, b=a..a+6; full tuples preserved',
        largest_observed_pieces=maxpieces,largest_observed_candidate_count=maxcandidates,
        proved_candidate_bound_per_sender_class=59,external_review='OPEN')
    (HERE/'local_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
