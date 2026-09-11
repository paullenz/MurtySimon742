#!/usr/bin/env python3
"""Exploratory scalar excess/Hall duals. Float discovery is NOT acceptance."""
from pathlib import Path
import sys, json
from collections import Counter
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'2026-09-11-threshold-tail-v1'
sys.path.insert(0,str(OLD))
from verify_m225_tail_slack_reduction import parse_profiles,score,weak_comps,hist_from_tails

def tight_rows():
    for s,Q in parse_profiles(OLD/'N30_M225_QGE18_PROFILES.txt'):
        _,gs=score(s); gs[13]=0
        for inc in weak_comps(Q-18,12):
            z={h:gs[h]+inc[h-2] for h in range(2,14)}
            if any(z[h]<z[h+1] for h in range(2,13)) or z[2]>16:continue
            rho=hist_from_tails(z)
            assert sum(s)==sum(rho)+2
            yield s,rho

def h(k,r,q,p):return q*(q>=k+1)-p*(r+q>=k)

def types(s,r):
    for q in range(min(13-r,sum(x<=r for x in s))+1):
        for p in range(min(r+2,15-q)+1):yield q,p

def search(s,rho):
    rs=sorted(set(rho)); c=max(s)+3; n=Counter(rho)
    # z_1,...,z_12 >=0; nu free; L_r free.
    obj=[0]*13+[-n[r] for r in rs]; A=[];b=[]
    for j,r in enumerate(rs):
        for q,p in types(s,r):
            row=[-h(k,r,q,p) for k in range(1,13)]+[-(q-p)]+[int(i==j) for i in range(len(rs))]
            A.append(row);b.append(q*(max(0,p-r+1)-c))
    sol=linprog(obj,A_ub=A,b_ub=b,bounds=[(0,None)]*12+[(None,None)]*(1+len(rs)),method='highs')
    out={'s':s,'rho':rho,'status':int(sol.status)}
    if sol.success:
        out['float_gap']=float(c*sum(s)-sol.fun)
        # Rationalise only weights, then recompute true minima with Fraction.
        ws=[Fraction(float(x)).limit_denominator(10000) for x in sol.x[:13]]
        mins={r:min(Fraction(q*(max(0,p-r+1)-c))+sum(ws[k-1]*h(k,r,q,p) for k in range(1,13))+ws[12]*(q-p) for q,p in types(s,r)) for r in rs}
        gap=c*sum(s)+sum(n[r]*mins[r] for r in rs)
        out.update(weights=list(map(str,ws)),minima={r:str(v) for r,v in mins.items()},exact_gap=str(gap),exact_positive=gap>0)
    return out

if __name__=='__main__':
    out=[]
    for i,(s,rho) in enumerate(tight_rows()):
        out.append(search(s,rho))
        if (i+1)%50==0:print(i+1,sum(r.get('exact_positive',False) for r in out),flush=True)
    result={'purpose':'exploration; exact source minima checked, full bridge remains a written obligation','rows':out}
    (HERE/'SCALAR_EXCESS_DISCOVERY.json').write_text(json.dumps(result,indent=2)+'\n')
    print('rows',len(out),'positive',sum(r.get('exact_positive',False) for r in out),'statuses',dict(Counter(r['status'] for r in out)))
