import baseline as old
from collections import Counter
from pathlib import Path
import json

def spill(s,q,rho,P):
    E=sum(q)-sum(s); out=list(P); trace=[]
    # All changes of the eligible label block: no rho breakpoint needed.
    for eta in sorted({0,*s}):
        low=[i for i,d in enumerate(s) if d<=eta]; SL=sum(s[i] for i in low)
        forced=[max(0,qq-sum(eta<d<=r for d in s)) for qq,r in zip(q,rho)]
        M=sum(forced)
        if M>SL+E:raise ValueError('spill infeasible')
        for w,(qq,r) in enumerate(zip(q,rho)):
            if qq==0:continue
            eligible=sum(d<=min(eta,r) for d in s)
            C=E+SL-M+forced[w]
            k=min(qq,eligible,C)
            if qq>k:
                cap=r-1+(C-k)//(qq-k)
                if cap<out[w]:trace.append((w,eta,cap,C,forced[w],M,SL));out[w]=cap
    return out,trace

# Exact separable upper envelope with necessary column eligibility and prefix bounds.
# Each candidate e vector may still fail the incidence matching: an upper bound only.
def envelope(s,q,rho,delta=None):
    E=sum(q)-sum(s)
    cols=sorted(s)
    h=[sum(qq>0 and r>=d for qq,r in zip(q,rho))-d for d in cols]
    if min(h)<0:return None
    dp={0:0}; lower={}
    for d in set(cols):
        upto=sum(x<=d for x in cols)
        spilltot=sum(max(0,qq-sum(d<x<=r for x in cols)) for qq,r in zip(q,rho))
        lower[upto]=max(0,spilltot-sum(x for x in cols if x<=d))
    for i,(d,hi) in enumerate(zip(cols,h),1):
        nxt={}
        for total,cost in dp.items():
            for e in range(min(hi,E-total)+1):
                v=cost+((min(e,delta) if delta is not None else e)*(d+e) if d>0 else 0); ee=total+e
                if ee>=lower.get(i,0) and v>nxt.get(ee,-1):nxt[ee]=v
        dp=nxt
    return dp.get(E)

def priced(q,rho,s,P,env=None):
    E=sum(q)-sum(s);z=s.count(0);c=[qq+r for qq,r in zip(q,rho)];v=[max(0,qq-z) for qq in q]
    if env is None:env=E*(E+max(s))
    best=(-10**9,None)
    for tau in range(1,max(q)+1):
        A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(len(q)))) for w in range(len(q))]
        demand=sum(qq for qq in q if qq>=tau)
        f=[min(a,r-1) for a,r in zip(A,rho)];g=[a-b for a,b in zip(A,f)]
        for theta in {0,*v,env+max(v)+1}:
            score=theta*(demand-sum(f))-sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))-env
            if score>best[0]:best=(score,(tau,theta,demand,sum(A)))
    return best

example=dict(a=24,b=27,t=2,D0=0,Esel=34,z=2,q=[7,2,2,2,2,2,2,6,3,4,5,2,3,8,6,2,2,6,2,3,6,4,6,2,4,1,2],rho=[3,1,1,1,1,1,1,4,4,3,3,1,4,3,4,1,1,2,1,2,3,3,3,1,3,2,1],s=[0,0,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
