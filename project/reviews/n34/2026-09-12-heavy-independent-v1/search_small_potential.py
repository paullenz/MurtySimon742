#!/usr/bin/env python3
"""Preserved integer search used after compact class-potential discovery."""
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
accepted=[]
for w6,w7,w9,v1,v0 in product(range(2),repeat=5):
    def f(L,k):
        return sum(L<=j for j in (2,3,4,5))+w6*(L<=6)+w7*(L<=7)+w9*(L<=9)+v1*(k>=-1)+v0*(k>=0)
    for lam,c,nu in product(range(1,5),range(1,6),range(1,6)):
        ell=min(lam*R+c*x+x*f(R+x,2-x) for R in range(12) for x in range(2,min(8,18-R)+1))
        sig=min(-c*H+nu*((H if H>2 else 0)-p)-H*f(H+p,1-p) for H in range(14) for p in range(5))
        gap=26*lam-13*ell-8*sig
        if gap<0:
            accepted.append(dict(lambda_=lam,c=c,nu=nu,ell=ell,sig=sig,gap=gap,extra_weights=[w6,w7,w9,v1,v0]))
report=dict(trials=3200,accepted=accepted,
            chosen=dict(lambda_=2,c=2,nu=2,ell=12,sig=-12,gap=-8,extra_weights=[0]*5))
assert report['chosen'] in accepted
(HERE/'small_potential_search.json').write_text(json.dumps(report,separators=(',',':'))+'\n')
print('PASS',len(accepted),'accepted; four-step hand potential gap -8')
