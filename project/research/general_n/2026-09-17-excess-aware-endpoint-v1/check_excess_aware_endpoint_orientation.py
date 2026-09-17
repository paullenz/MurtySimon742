#!/usr/bin/env python3
"""Replay the strict excess-aware common-margin example.
No third-party modules. This is a bridge-level arithmetic/degree audit, not a graph census.
"""
from __future__ import annotations
import json

a,b,t,Q=20,23,2,80
rho=[5]*7+[4]*8+[2]+[1]*7
R=[5]+[4]*14+[3]*5
s=[4]*20
x=[4]*20
e=[xx-ss for xx,ss in zip(x,s)]
C=[rr+xx for rr,xx in zip(R,x)]


def p0(r): return min(b-1,r+b-a-1)

def qmax(r,p):
    best=0
    for ss,ee,cc in zip(s,e,C):
        if 0<ss<=r and ee>=max(0,p-r+1):
            best=max(best,min(b-1-p,cc-p))
    return max(0,best)

def erdos_gallai(seq):
    d=sorted(seq,reverse=True)
    if sum(d)%2: return False
    return all(sum(d[:k])<=k*(k-1)+sum(min(v,k) for v in d[k:]) for k in range(1,len(d)+1))

def gale_ryser(rows,cols):
    r=sorted(rows,reverse=True); c=sorted(cols,reverse=True)
    return sum(r)==sum(c) and all(sum(r[:k])<=sum(min(v,k) for v in c) for k in range(1,len(r)+1))

# preceding basic cut
basic=0
for r in rho:
    compat=[cc for ss,cc in zip(s,C) if ss<=r]
    basic+=max([p0(r)]+compat)

# weighted (alpha,beta)=(2,3)
weighted=0
curves={}
for r in sorted(set(rho),reverse=True):
    vals=[]
    for p in range(p0(r)+1):
        q=qmax(r,p)
        vals.append((p,q))
    curves[r]=vals
for r in rho:
    weighted+=max(2*q+3*p for p,q in curves[r])

# exact DP: maximum total q at total p=Q
dp={0:0}
for r in rho:
    nd={}
    for ps,qs in dp.items():
        for p,q in curves[r]:
            if ps+p<=Q:
                nd[ps+p]=max(nd.get(ps+p,-10**9),qs+q)
    dp=nd
exact_q=dp.get(Q,-1)

Fdeg=[rr+ss for rr,ss in zip(R,s)]
summary={
    'status':'PASS_EXCESS_AWARE_STRICTNESS',
    'a':a,'b':b,'t':t,'Q':Q,
    'sum_rho':sum(rho),'sum_R':sum(R),'sum_s':sum(s),
    'basic_lhs_2Q':2*Q,'basic_rhs_sum_B':basic,
    'weighted_lhs_5Q':5*Q,'weighted_rhs_sum_H':weighted,
    'exact_max_outgoing_at_incoming_Q':exact_q,
    'source_curves':{str(k):v for k,v in curves.items()},
    'F_degree_sequence':sorted(Fdeg,reverse=True),
    'F_graphical':erdos_gallai(Fdeg),
    'residual_bipartite_graphical':gale_ryser(rho,R),
    'interpretation':'abstract canonical-bridge profile only; no original-graph realization claimed'
}
assert sum(rho)==sum(R)==76
assert sum(rho)+2*t==sum(s)==80
assert basic==160
assert weighted==397
assert exact_q==78
assert summary['F_graphical'] and summary['residual_bipartite_graphical']
print(json.dumps(summary,indent=2,sort_keys=True))
