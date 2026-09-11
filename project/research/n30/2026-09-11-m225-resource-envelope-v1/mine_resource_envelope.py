#!/usr/bin/env python3
"""Explore a simple residual-plus-excess resource inequality; exactify positives."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json
import numpy as np
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'2026-09-11-m225-hall-continuation-v1'
KS=tuple(range(1,14))

def types(s,rho):
    qmax=min(13-rho,sum(si<=rho for si in s))
    return [(q,p) for q in range(qmax+1) for p in range(rho+3)]

def coeffs(s,rho,q,p):
    smax=max(s)
    alpha=max(0,p-rho+1)
    cost=[q*(alpha-smax-3)]
    cost += [q*(min(max(0,q+p-rho),K)-smax-K) for K in KS]
    cost += [q*(q>=j+1)-p*(rho+q>=j) for j in range(1,13)]
    cost += [q-p]
    return cost

def constant(s):
    return [(max(s)+3)*sum(s)]+[2*(max(s)+K) for K in KS]+[0]*13

def gap(s,rhos,w):
    mins={rho:min(sum(x*y for x,y in zip(w,coeffs(s,rho,q,p))) for q,p in types(s,rho)) for rho in set(rhos)}
    return sum(x*y for x,y in zip(w,constant(s)))+sum(n*mins[r] for r,n in Counter(rhos).items()),mins

def search(pf):
    s=pf['s'];rhos=pf['rho'];rs=sorted(set(rhos));num=27
    assert sum(s)==sum(rhos)+2
    obj=[-v for v in constant(s)]+[-rhos.count(r) for r in rs]
    A=[]
    for i,r in enumerate(rs):
        for q,p in types(s,r):A.append([-v for v in coeffs(s,r,q,p)]+[int(i==j) for j in range(len(rs))])
    norm=[1]*14+[0]*(13+len(rs))
    sol=linprog(obj,A_ub=A,b_ub=np.zeros(len(A)),A_eq=[norm],b_eq=[1],bounds=[(0,None)]*26+[(None,None)]*(1+len(rs)),method='highs')
    out={'s':s,'rho':rhos,'status':int(sol.status)}
    if sol.success:
        out['float_gap']=-float(sol.fun)
        w=[F(float(x)).limit_denominator(100000) for x in sol.x[:num]]
        exact,mins=gap(s,rhos,w)
        out.update(weights=list(map(str,w)),exact_gap=str(exact),exact_positive=exact>0,minima={r:str(v) for r,v in mins.items()})
    return out

if __name__=='__main__':
    rows=json.loads((OLD/'REMAINING_150_POSITIVE_ROWS.json').read_text());out=[]
    for i,pf in enumerate(rows):
        out.append(search(pf))
        if (i+1)%25==0:print(i+1,sum(r.get('exact_positive',False) for r in out),flush=True)
    (HERE/'SIMPLE_RESOURCE_DISCOVERY.json').write_text(json.dumps({'schema':'n30-simple-resource-discovery-v1','K':KS,'rows':out},indent=2)+'\n')
    print('positive',sum(r.get('exact_positive',False) for r in out),'of',len(out))
