#!/usr/bin/env python3
"""Independent finite audit for CANONICAL_HALL_SLACK_EXPANSION.md."""
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path
import json, random

SEED=742091404
OUT=Path(__file__).resolve().parent/'CANONICAL_HALL_SLACK_EXPANSION_VERIFICATION.json'

def compat(x,y):
    return x[0]<=y[1]+1 and y[0]<=x[1]

def grouped(profile):
    c=Counter(profile); types=tuple(sorted(c)); return types,tuple(c[t] for t in types)

def ycounts(types,n,mask):
    out=[]
    for s,sig in enumerate(types):
        y=sum(n[t] for t,tau in enumerate(types) if (mask>>t)&1 and compat(tau,sig))
        if (mask>>s)&1:y-=1
        assert y>=0
        out.append(y)
    return out

def H(types,n,mask):
    y=ycounts(types,n,mask)
    return sum(n[s]*min(types[s][2],y[s]) for s in range(len(types)))

def D(types,n,mask):
    return sum(n[t]*types[t][0] for t in range(len(types)) if (mask>>t)&1)

def F(types,n,mask):return H(types,n,mask)-D(types,n,mask)

def extrema(types,n):
    vals=[F(types,n,m) for m in range(1<<len(types))]; z=min(vals)
    mins=[m for m,v in enumerate(vals) if v==z]
    mp=0; mm=(1<<len(types))-1
    for m in mins: mp|=m; mm&=m
    assert F(types,n,mp)==z and F(types,n,mm)==z
    return z,mp,mm

def audit(profile,st):
    types,n=grouped(profile); k=len(types); best,mp,mm=extrema(types,n)
    y=ycounts(types,n,mp); slack=[max(0,types[s][2]-y[s]) for s in range(k)]
    outside=((1<<k)-1)^mp
    T=outside
    # Enumerate every nonempty subset of the exterior.
    sub=T
    while sub:
        gain_formula=0
        for s,sig in enumerate(types):
            K=sum(n[t] for t,tau in enumerate(types) if (sub>>t)&1 and compat(tau,sig))-int((sub>>s)&1)
            assert K>=0
            gain_formula+=n[s]*min(slack[s],K)
        direct=H(types,n,mp|sub)-H(types,n,mp)
        assert gain_formula==direct
        dem=D(types,n,sub)
        gap=F(types,n,mp|sub)-best
        assert gap>=1 and gain_formula>=dem+1
        st['exterior_subsets']+=1
        st['min_exterior_gap']=min(st['min_exterior_gap'],gap)
        sub=(sub-1)&T
    if outside:
        total_slack=sum(n[s]*slack[s] for s in range(k))
        assert total_slack>=D(types,n,outside)+1
        st['whole_exterior_checks']+=1

    # Every nonempty subset of M- has strict removal gap; every subset M+ has weak loss bound.
    sub=mp
    while sub:
        loss=H(types,n,mp)-H(types,n,mp^sub)
        assert loss<=D(types,n,sub)
        st['interior_subsets']+=1
        sub=(sub-1)&mp
    sub=mm
    while sub:
        loss=H(types,n,mp)-H(types,n,mp^sub)
        gap=F(types,n,mp^sub)-best
        assert gap>=1 and loss<=D(types,n,sub)-1
        st['mminus_subsets']+=1
        sub=(sub-1)&mm
    st['profiles']+=1; st['infeasible']+=int(best<0); st['max_types']=max(st['max_types'],k)

def main():
    U=[(0,0,0),(0,1,1),(1,1,0),(1,2,1),(1,3,2),(2,2,1),(2,3,2),(2,4,3)]
    st={'profiles':0,'infeasible':0,'exterior_subsets':0,'whole_exterior_checks':0,'interior_subsets':0,'mminus_subsets':0,'min_exterior_gap':10**9,'max_types':0}
    ex=0
    for size in range(1,6):
        for p in combinations_with_replacement(U,size):audit(p,st);ex+=1
    rng=random.Random(SEED); rand=800
    for _ in range(rand):
        size=rng.randint(1,7);p=[]
        for __ in range(size):
            q=rng.randint(0,4);rho=rng.randint(0,4);P=rng.randint(0,5);p.append((q,q+rho,P))
        audit(tuple(p),st)
    if st['min_exterior_gap']==10**9:st['min_exterior_gap']=None
    rep={'schema':'canonical-hall-slack-expansion-verification-v1','result':'PASS','seed':SEED,'exhaustive_profiles':ex,'random_profiles':rand,**st,'external_review':'OPEN'}
    OUT.write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n');print(json.dumps(rep,indent=2,sort_keys=True))
if __name__=='__main__':main()
