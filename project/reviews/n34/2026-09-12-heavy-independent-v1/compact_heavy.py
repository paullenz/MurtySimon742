#!/usr/bin/env python3
"""Seek a short class-specific potential proof of the low N34 state."""
from pathlib import Path
from fractions import Fraction
from math import lcm
import json
import sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'project/research/n34/2026-09-12-frontier-v1'))
from certify_upper_layers import integer_certificate


def feature(kind,k,H,d,load):
    return (d>=k and load<=H) if kind=='BC' else d-load>=k


def build(simple=False):
    names=[];bounds=[];rows=[];rhs=[];kinds=[]
    def var(name,bound=(None,None)):
        names.append(name);bounds.append(bound);return len(names)-1
    lam=var('lambda');c={s:var(('c',s)) for s in [1,2]};mu=var('mu')
    nu=var('nu',(0,None));tau={j:var(('tau',j),(0,None)) for j in range(1,16)}
    ell={s:var(('ell',s)) for s in [1,2]};sig={r:var(('sig',r)) for r in [1,2]}
    terms=[('BC',d,h) for d in range(1,14) for h in range(19)]+[('DIAG',k,0) for k in range(-18,15)]
    weight={(s,*term):var(('weight',s,*term),(0,None)) for s in [1,2] for term in terms}
    if simple:
        for j,n in enumerate(names):
            if (n=='mu' or n in [('c',1),('ell',1),('sig',1)]
                or (isinstance(n,tuple) and n[0]=='tau' and n[1]!=4)
                or (isinstance(n,tuple) and n[0]=='weight' and
                    (n[1]==1 or (n[2]=='BC' and n[3]!=1) or (n[2]=='DIAG' and n[3] not in [-2,-1,0])))):
                bounds[j]=(0,0)
    def le(co,b,kind):rows.append(co);rhs.append(b);kinds.append(kind)
    for s in [1,2]:
        for R in range(14-s):
            for x in range(s,min(18-R,18 if s==1 else 8)+1):
                co={ell[s]:1,lam:-R,c[s]:-x}
                for term in terms:
                    if feature(*term,R+s,R+x):co[weight[s,*term]]=-x
                le(co,0,('local',ell[s]))
    for r in [1,2]:
        for q in range((2 if r==1 else 13)+1):
            for p in range(min(r+2,17-q)+1):
                for H in range(max(0,q-2),min(q,0 if r==1 else 13)+1):
                    co={sig[r]:1,mu:-(q-p),c[1]:q-H,c[2]:H,
                        nu:-(H if H>2 else 0)+(p if r>=2 else 0)}
                    for j in tau:
                        v=(q if q>=j+1 else 0)-(p if r+q>=j else 0)
                        if v:co[tau[j]]=-v
                    for s,kount in [(1,q-H),(2,H)]:
                        if kount:
                            for term in terms:
                                if feature(*term,r+q-1,q+p):co[weight[s,*term]]=kount
                    le(co,0,('local',sig[r]))
    le({lam:26,ell[1]:-2,ell[2]:-13,sig[1]:-10,sig[2]:-8},-1,('gap',None))
    mat=lil_matrix((len(rows),len(names)))
    for i,row in enumerate(rows):
        for j,v in row.items():mat[i,j]=v
    objective=np.array([1 if isinstance(n,tuple) and n[0]=='weight' else 0 for n in names],float)
    res=linprog(objective,A_ub=mat.tocsr(),b_ub=rhs,bounds=bounds,method='highs')
    return names,bounds,rows,rhs,kinds,res


def main():
    simple='--simple' in sys.argv
    model=build(simple);cert=integer_certificate(model)
    out=dict(solver_status=int(model[-1].status),certificate=cert)
    if cert:
        pairs=[(n,x) for n,x in zip(cert['names'],cert['numerators']) if x]
        out['nonzero_coefficients']=pairs
        print('EXACT',cert['gap'],'support',len(pairs),flush=True)
        print(pairs,flush=True)
    (HERE/('compact_simple.json' if simple else 'compact_heavy.json')).write_text(json.dumps(out,separators=(',',':'))+'\n')


if __name__=='__main__':main()
