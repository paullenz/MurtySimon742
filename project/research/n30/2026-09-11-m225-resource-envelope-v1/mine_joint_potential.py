#!/usr/bin/env python3
"""Discover compact monotone potentials on N30's remaining positive rows.

All functions are nondecreasing in (s,d,v). Discovery uses float LP; positive
outputs include separately evaluated rational envelope gaps, not solver status.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import argparse,json
import numpy as np
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'2026-09-11-m225-hall-continuation-v1'

SHAPES=['dv','min_dv','sv','min_sv']+[f'diag_{k}' for k in range(4)]+['sh2']

def phi(name,s,d,v):
    if name=='dv':return d*v
    if name=='min_dv':return min(d,v)
    if name=='sv':return s*v
    if name=='min_sv':return min(s,v)
    if name=='sh2':return int(s>=2)
    if name.startswith('diag_'):return int(d+v>=16-int(name.split('_')[1]))
    if name.startswith('bc_'):
        _,D,V=name.split('_');return int(d>=int(D) and v>=int(V))
    raise ValueError(name)

def label_states(s,rhos,dmax=12,cap=True):
    H=sum(r>=s for r in rhos)
    return [(R,x) for R in range(dmax-s+1) for x in range(s,min(16-R,H if cap else 16)+1)]

def source_states(r,s):
    return [(q,p) for q in range(min(13-r,sum(si<=r for si in s))+1) for p in range(r+3)]

def lcoeff(s,R,x,shapes):
    return [R,x,0]+[0]*12+[x*phi(f,s,R+s,16-R-x) for f in shapes]

def scoeff(r,q,p,shapes):
    return [0,-q,q-p]+[q*(q>=j+1)-p*(r+q>=j) for j in range(1,13)]+[-q*phi(f,r,r+q-1,16-q-p) for f in shapes]

def exact_gap(pf,shapes,weights,dmax=12,cap=True):
    s=pf['s'];rhos=pf['rho'];SC=Counter(s);RC=Counter(rhos)
    ell={si:min(sum(a*b for a,b in zip(weights,lcoeff(si,R,x,shapes))) for R,x in label_states(si,rhos,dmax,cap)) for si in SC}
    sig={r:min(sum(a*b for a,b in zip(weights,scoeff(r,q,p,shapes))) for q,p in source_states(r,s)) for r in RC}
    gap=sum(n*ell[si] for si,n in SC.items())+sum(n*sig[r] for r,n in RC.items())-weights[0]*sum(rhos)
    return gap,ell,sig

def search(pf,shapes=SHAPES,dmax=12,cap=True):
    s=pf['s'];rhos=pf['rho'];ss=sorted(set(s));rs=sorted(set(rhos));NW=15+len(shapes)
    n=NW+len(ss)+len(rs);A=[]
    for i,si in enumerate(ss):
        for R,x in label_states(si,rhos,dmax,cap):A.append([-v for v in lcoeff(si,R,x,shapes)]+[int(i==j) for j in range(len(ss))]+[0]*len(rs))
    for i,r in enumerate(rs):
        for q,p in source_states(r,s):A.append([-v for v in scoeff(r,q,p,shapes)]+[0]*len(ss)+[int(i==j) for j in range(len(rs))])
    obj=[sum(rhos)]+[0]*(NW-1)+[-s.count(si) for si in ss]+[-rhos.count(r) for r in rs]
    norm=[0]*15+[1]*len(shapes)+[0]*(len(ss)+len(rs))
    bounds=[(0,None),(None,None),(None,None)]+[(0,None)]*(NW-3)+[(None,None)]*(len(ss)+len(rs))
    sol=linprog(obj,A_ub=A,b_ub=np.zeros(len(A)),A_eq=[norm],b_eq=[1],bounds=bounds,method='highs')
    out={**pf,'status':int(sol.status),'dmax':dmax,'label_source_cap':cap}
    if sol.success:
        out['float_gap']=-float(sol.fun)
        w=[F(float(x)).limit_denominator(1000000) for x in sol.x[:NW]]
        g,l,sg=exact_gap(pf,shapes,w,dmax,cap)
        out.update(weights=list(map(str,w)),exact_gap=str(g),exact_positive=g>0,
                   ell={s:str(v) for s,v in l.items()},sigma={r:str(v) for r,v in sg.items()})
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--dmax',type=int,default=12);ap.add_argument('--no-label-cap',action='store_true');ap.add_argument('--rectangles',action='store_true');ap.add_argument('--only-unresolved',action='store_true');args=ap.parse_args()
    shapes=SHAPES+([f'bc_{D}_{V}' for D in range(1,6) for V in range(6,16)] if args.rectangles else [])
    rows=json.loads((OLD/'REMAINING_150_POSITIVE_ROWS.json').read_text());out=[]
    if args.only_unresolved:
        old=json.loads((HERE/'JOINT_SMALL_DMAX12_DISCOVERY.json').read_text())['rows']
        keep={(tuple(r['s']),tuple(r['rho'])) for r in old if not r['exact_positive']}
        rows=[r for r in rows if (tuple(r['s']),tuple(r['rho'])) in keep]
    for i,pf in enumerate(rows):
        out.append(search(pf,shapes,args.dmax,not args.no_label_cap))
        if (i+1)%25==0:print(i+1,sum(r.get('exact_positive',False) for r in out),flush=True)
    suffix='RECTANGLES' if args.rectangles else 'SMALL'
    (HERE/f'JOINT_{suffix}_DMAX{args.dmax}_DISCOVERY.json').write_text(json.dumps({'schema':'n30-joint-envelope-discovery-v1','shapes':shapes,'rows':out},indent=2)+'\n')
    print('positive',sum(r.get('exact_positive',False) for r in out),'of',len(out),'statuses',dict(Counter(r['status'] for r in out)))
