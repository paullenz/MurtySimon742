#!/usr/bin/env python3
"""Reconnaissance for a sparse staircase potential shared by all seven n30 profiles.

Candidate BC staircases are the unique minimal-generator shapes appearing in
the preserved BC cut library across all seven profiles. Candidate SH shapes are
the four generated exceptional-state corrections. A single set of nonnegative
weights, and shared lambda,c,mu,tau2,tau3, must produce envelope margin >=1 for
every profile. L1 objective encourages a small/common potential.

Floating-point output is reconnaissance only until exactified.
"""
from collections import Counter
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

def leq(a,b):return all(x<=y for x,y in zip(a,b))
def min_gens(points):
    pts=sorted(set(tuple(p) for p in points))
    return tuple(p for p in pts if not any(q!=p and leq(q,p) for q in pts))
def inside(pt,gens):return any(leq(g,pt) for g in gens)
def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

class LP:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
    def var(self,name,b=(None,None),cost=0.0):
        if name in self.idx:return self.idx[name]
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.c.append(cost);self.bounds.append(b);return i
    def le(self,row,rhs):self.rows.append(row);self.rhs.append(rhs)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)))
        for i,r in enumerate(self.rows):
            for j,v in r.items():A[i,j]=v
        return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bc-json',type=Path,required=True);ap.add_argument('--sh-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.bc_json.read_text());S=json.loads(z.sh_json.read_text())
    bcset=set()
    for rec in B['records']:
        for cut in rec['cuts']:
            pts=[(x['R']+x['s'],-(x['R']+x['x'])) for x in cut['label_states']]
            g=min_gens(pts)
            if g:bcset.add(g)
    bcshapes=sorted(bcset);shshapes=[tuple(tuple(x) for x in c['generators']) for c in S['sh_cuts']]
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['records']]
    M=LP();lam=M.var(('coef','lambda'),(0,None),1);cc=M.var(('coef','c'),(0,None),1);mp=M.var(('coef','mu+'),(0,None),1);mm=M.var(('coef','mu-'),(0,None),1);t2=M.var(('coef','tau2'),(0,None),1);t3=M.var(('coef','tau3'),(0,None),1)
    bw=[M.var(('BC',i),(0,None),1) for i in range(len(bcshapes))];sw=[M.var(('SH',i),(0,None),1) for i in range(len(shshapes))]
    def addpot(row,coord_bc,coord_sh,factor,sign):
        for i,g in enumerate(bcshapes):
            if inside(coord_bc,g):row[bw[i]]=row.get(bw[i],0)+sign*factor
        for i,g in enumerate(shshapes):
            if inside(coord_sh,g):row[sw[i]]=row.get(sw[i],0)+sign*factor
    meta=[]
    for pi,p in enumerate(P):
        sc=Counter(p['s']);rc=Counter(p['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(z.dmax-s+1):
                for x in range(s,z.b-R+1):
                    d=R+s;h=R+x;row={e:1,lam:-R,cc:-x};addpot(row,(d,-h),(s,-h),x,-1);M.le(row,0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(z.a-rho,sum(si<=rho for si in p['s']))
            for q in range(qmax+1):
                pmax=min(rho+z.b-z.a-1,z.b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;beta=q+pp;row={sg:1,mp:-(q-pp),mm:(q-pp),t2:-tterm(rho,q,pp,2),t3:-tterm(rho,q,pp,3),cc:q};addpot(row,(alpha,-beta),(rho,-beta),q,1);M.le(row,0)
        r=sum(p['rho']);row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1);meta.append({'profile':pi,'demand_id':p['demand_id'],'r':r})
    res=M.solve();out={'schema':'n30-shared-sparse-staircase-recon-v1','success':bool(res.success),'status':int(res.status),'message':res.message,'BC_candidate_shapes':len(bcshapes),'SH_candidate_shapes':len(shshapes),'floating_point_reconnaissance_only':True,'profiles':meta}
    if res.success:
        x=res.x;actbc=[{'index':i,'weight':float(x[v]),'generators':[list(p) for p in bcshapes[i]]} for i,v in enumerate(bw) if x[v]>1e-8];actsh=[{'index':i,'weight':float(x[v]),'generators':[list(p) for p in shshapes[i]]} for i,v in enumerate(sw) if x[v]>1e-8]
        margins=[]
        for pi,p in enumerate(P):
            sc=Counter(p['s']);rc=Counter(p['rho']);left=sum(n*x[M.idx[('ell',pi,s)]] for s,n in sc.items())+sum(n*x[M.idx[('sig',pi,rho)]] for rho,n in rc.items());margins.append(float(left-x[lam]*sum(p['rho'])))
        out.update({'objective':float(res.fun),'coefficients':{'lambda':float(x[lam]),'c':float(x[cc]),'mu':float(x[mp]-x[mm]),'tau2':float(x[t2]),'tau3':float(x[t3])},'active_BC':actbc,'active_SH':actsh,'active_BC_count':len(actbc),'active_SH_count':len(actsh),'margins':margins,'min_margin':min(margins)})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in out if k not in ('active_BC','active_SH','profiles')},indent=2,sort_keys=True))
if __name__=='__main__':main()
