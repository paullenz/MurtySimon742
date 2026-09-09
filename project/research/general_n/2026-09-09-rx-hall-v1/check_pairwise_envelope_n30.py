#!/usr/bin/env python3
"""Exact standard-library check of the direct n=30 pairwise-envelope certificate."""
from collections import Counter
import json

A=13;B=16;DMAX=11
S=[1,1,2,2]+[3]*9
RHO=[1]*8+[2]+[3]*7
LAM=4698; C=5258; MU=6640; TAU={2:461,3:461}
BC=[
 (2322,[(1,-2),(3,-4),(4,-6),(6,-8),(9,-9)]),
 (955,[(1,-1),(2,-4),(3,-9),(4,-13)]),
 (1566,[(1,-2),(2,-3),(3,-4),(4,-5)]),
 (2215,[(1,-1),(2,-4)]),
 (1190,[(1,-1),(2,-2),(3,-5),(6,-6),(7,-7),(8,-10),(11,-12)]),
 (2826,[(1,-3)]),
]
SH=[
 (1459,[(1,-1),(2,-5),(3,-6)]),
 (1674,[(1,-1),(2,-7)]),
 (1998,[(1,-1),(2,-2),(3,-11)]),
]

def inside(pt,gens):return any(g[0]<=pt[0] and g[1]<=pt[1] for g in gens)
def psi_label(s,R,x):
    d=R+s;h=R+x
    return sum(w for w,g in BC if inside((d,-h),g))+sum(w for w,g in SH if inside((s,-h),g))
def psi_source(rho,q,p):
    alpha=rho+q-1;beta=q+p
    return sum(w for w,g in BC if inside((alpha,-beta),g))+sum(w for w,g in SH if inside((rho,-beta),g))
def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
def lscore(s,R,x):return LAM*R+C*x+x*psi_label(s,R,x)
def sscore(rho,q,p):
    return MU*(q-p)+sum(w*tterm(rho,q,p,j) for j,w in TAU.items())-C*q-q*psi_source(rho,q,p)

def main():
    sc=Counter(S);rc=Counter(RHO);labels=[];sources=[]
    for s,n in sorted(sc.items()):
        vals=[]
        for R in range(DMAX-s+1):
            for x in range(s,B-R+1):vals.append((lscore(s,R,x),R,x,psi_label(s,R,x)))
        m=min(vals)
        labels.append({'s':s,'multiplicity':n,'minimum':m[0],'first_minimizer':{'R':m[1],'x':m[2]},'psi_at_minimizer':m[3],'states_checked':len(vals)})
    for rho,n in sorted(rc.items()):
        qmax=min(A-rho,sum(si<=rho for si in S));vals=[]
        for q in range(qmax+1):
            pmax=min(rho+B-A-1,B-1-q)
            for p in range(pmax+1):vals.append((sscore(rho,q,p),q,p,psi_source(rho,q,p)))
        m=min(vals)
        sources.append({'rho':rho,'multiplicity':n,'qmax':qmax,'minimum':m[0],'first_minimizer':{'q':m[1],'p':m[2]},'psi_at_minimizer':m[3],'states_checked':len(vals)})
    left=sum(x['multiplicity']*x['minimum'] for x in labels)+sum(x['multiplicity']*x['minimum'] for x in sources)
    r=sum(RHO);right=LAM*r;gap=left-right
    assert [(x['s'],x['minimum'],x['first_minimizer']['R'],x['first_minimizer']['x']) for x in labels]==[(1,21030,1,1),(2,41590,4,2),(3,58659,5,3)]
    assert [(x['rho'],x['minimum'],x['first_minimizer']['q'],x['first_minimizer']['p']) for x in sources]==[(1,-19922,2,1),(2,-37093,3,2),(3,-44300,2,4)]
    assert left==146602 and right==145638 and gap==964
    print(json.dumps({'schema':'n30-direct-pairwise-envelope-check-v1','labels':labels,'sources':sources,'r':r,'lambda':LAM,'envelope_left_lower_bound':left,'lambda_r':right,'contradiction_margin':gap,'status':'PASS'},indent=2,sort_keys=True))
if __name__=='__main__':main()
