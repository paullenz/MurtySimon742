#!/usr/bin/env python3
"""Pure integer local domains and count-conditioned routing envelope."""
from collections import Counter


def context(rec,h,T):
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho']
    groups=[]
    for rv,n in sorted(Counter(v for v in rho if v>=h).items()):
        c=min(a-rv,sum(h<=sv<=rv for sv in s));P=rv+b-a-1
        opts=[(H,p,h*H+H*max(0,T-max(h,H+p)))
              for H in range(c+1) for p in range(min(P,b-1-H)+1)]
        groups.append(dict(rho=rv,n=n,c=c,P=P,options=opts))
    caps=[g['c'] for g in groups for _ in range(g['n'])]
    high=sorted((c for c in caps if c>h),reverse=True)
    z=len(caps);W=sum(v for v in s if v>=h);G=sum(max(T,v) for v in s if v>=h)
    L=sum(min(h,c) for c in caps)
    jbounds=[L-j*h+min(sum(high[:j]),j*z-j*(j+1)//2) for j in range(len(high)+1)]
    return dict(h=h,T=T,z=z,W=W,G=G,r=sum(rho),groups=groups,jbounds=jbounds)


def evaluate(ctx,j,lam,mu,eta,den=1,mode='joint'):
    h=ctx['h'];low=[];diff=[]
    for g in ctx['groups']:
        values=[[],[]]
        for H,p,B in g['options']:
            high=int(H>h);D=H*high
            incoming=p if mode=='aggregate' else min(p,j-high)
            val=den*B-(lam+mu)*D+lam*incoming+eta*H
            values[high].append(val)
        lo=max(values[0]);low.extend([lo]*g['n'])
        if values[1]:diff.extend([max(values[1])-lo]*g['n'])
    assert j<=len(diff)
    pair=j*ctx['z']-j*(j+1)//2
    rhs=den*h*ctx['r']+sum(low)+sum(sorted(diff,reverse=True)[:j])+mu*pair-eta*ctx['W']
    lhs=den*h*ctx['G']
    return dict(j=j,denominator=den,lam=lam,mu=mu,eta=eta,lhs=lhs,rhs=rhs,gap=lhs-rhs,mode=mode)
