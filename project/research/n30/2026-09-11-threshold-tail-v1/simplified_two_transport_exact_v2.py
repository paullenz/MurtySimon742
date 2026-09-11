#!/usr/bin/env python3
"""Exact-certificate layer for simplified_two_transport.py.

The model builder is unchanged.  This file replaces crude decimal scaling of a
floating Farkas proposal by bounded-denominator rational reconstruction, then
verifies the resulting integer ray coefficient-by-coefficient.
"""
from __future__ import annotations
from fractions import Fraction
from functools import reduce
from math import gcd,lcm
from collections import Counter
import argparse,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import hstack,vstack,csr_matrix

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from simplified_two_transport import ROWS,build,verify,eqkind


def reconstruct(m):
    _,_,E,f=m.arrays();N=len(m.names);ne=len(m.eq)
    D=hstack([-E.T,E.T],format='csr')
    D=vstack([D,csr_matrix(np.r_[f,-f].reshape(1,-1))],format='csr')
    rhs=np.r_[np.zeros(N),-1.0]
    res=linprog(np.ones(2*ne),A_ub=D,b_ub=rhs,bounds=(0,None),method='highs')
    if not res.success:return None
    raw=[float(x-y) for x,y in zip(res.x[:ne],res.x[ne:])]
    for maxden in (20,50,100,250,1000,5000,20000,100000,1000000):
        mu=[Fraction(x).limit_denominator(maxden) for x in raw]
        coef=[Fraction(0) for _ in range(N)];rv=Fraction(0)
        for (row,b),w in zip(m.eq,mu):
            if not w:continue
            rv += w*b
            for j,a in row.items():coef[j] += w*a
        if min(coef)>=0 and rv<0:
            den=1
            for x in mu:den=lcm(den,x.denominator)
            ints=[int(x*den) for x in mu]
            factor=reduce(gcd,[abs(x) for x in ints if x] or [1]) or 1
            ints=[x//factor for x in ints]
            c={'eq':[(i,w) for i,w in enumerate(ints) if w],
               'variables':N,'equalities':ne}
            # Compute exact RHS after primitive reduction.
            rr=0
            for i,w in c['eq']:rr+=w*m.eq[i][1]
            c['rhs']=rr
            verify(m,c)
            return c
    return None


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');z=ap.parse_args()
    out={'schema':'n30-m226-simplified-two-transport-exact-v2','rows':[]}
    for tag,s,rho in ROWS:
        m=build(s,rho);sol=m.solve()
        row={'tag':tag,'status':int(sol.status),'variables':len(m.names),'equalities':len(m.eq)}
        assert sol.status==2,(tag,sol.status)
        c=reconstruct(m);assert c is not None,('no_exact_certificate',tag)
        kinds=Counter(eqkind(m,i) for i,w in c['eq'])
        row['certificate']={'rhs':c['rhs'],'terms':len(c['eq']),'support_counts':dict(kinds),
                            'multipliers':c['eq']}
        out['rows'].append(row)
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if z.output:Path(z.output).write_text(text)
    print(text,end='')

if __name__=='__main__':main()
