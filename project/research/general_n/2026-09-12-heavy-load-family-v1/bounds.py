#!/usr/bin/env python3
"""Integer formulas for the general heavy-load/routing family.

All statements are candidate graph consequences; no numerical optimizer.
"""
from functools import lru_cache


def ramp(h,T,L):
    assert 1<=h<=T
    return max(0,T-max(h,L))


def source_cost(h,T,H,p):
    return h*H+h*p+H*ramp(h,T,H+p)-(h*H if H>h else 0)


def quadratic(B,lo,hi):
    """Maximum integer x(B-x) on a nonempty closed interval."""
    assert lo<=hi
    x=min(hi,max(lo,B//2))
    return x*(B-x)


@lru_cache(None)
def uniform_cap(h,T,P):
    assert 1<=h<=T and P>=0
    return max(h*T,h*(h+P),T*T//4)


@lru_cache(None)
def capped(h,T,P,c):
    """Exact source-cost maximum, evaluated using at most five pieces."""
    assert 1<=h<=T and P>=0 and c>=0
    m=min(h,c);values=[]
    # For H<=h the cost is nondecreasing in p; set p=P.
    end=min(m,h-P)
    if end>=0:values.append(end*T+h*P)
    lo=max(0,h-P);hi=min(m,T-P)
    if lo<=hi:values.append(h*P+quadratic(h+T-P,lo,hi))
    if m>=max(0,T-P):values.append(h*(m+P))
    # For H>h the cost is convex in p; only p=0,P can maximize it.
    if c>h:
        for p in (0,P):
            hi=min(c,T-p)
            peak=quadratic(T-p,h+1,hi) if h+1<=hi else 0
            values.append(h*p+max(0,peak))
    assert values
    return max(values)


def profile_gap(a,b,s,rho,h,T,mode='capped'):
    """Positive integer gap excludes a canonical profile; no surplus assumed here."""
    assert len(s)==a and len(rho)==b and 1<=h<=T
    W=sum(max(T,v) for v in s if v>=h)
    terms=[]
    for rv in rho:
        if rv<h:continue
        P=rv+b-a-1
        c=min(a-rv,sum(h<=v<=rv for v in s))
        assert P>=0 and c>=0
        C=capped(h,T,P,c) if mode=='capped' else uniform_cap(h,T,P)
        terms.append((rv,P,c,C))
    rhs=h*sum(rho)+sum(row[3] for row in terms)
    return dict(h=h,T=T,mode=mode,lhs=h*W,rhs=rhs,gap=h*W-rhs,source_terms=terms)
