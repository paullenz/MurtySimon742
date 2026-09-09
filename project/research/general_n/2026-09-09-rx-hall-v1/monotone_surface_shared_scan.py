#!/usr/bin/env python3
"""Reconnaissance: one shared monotone F+G envelope for all n=30 hard profiles.

This script works entirely at the direct-envelope level. It uses no Z, W/L
feasibility LP, Hall cut generation or Farkas acceptance. It asks whether a
single pair of nonnegative monotone grid functions F(d,h), G(s,h), together
with shared lambda,c,mu,tau2,tau3, can give a strictly positive envelope margin
for every one of the seven residual-budget hard profiles simultaneously.

Floating-point success is RECONNAISSANCE ONLY. A later exactification is
required before any mathematical promotion.
"""
from collections import Counter
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)

class Builder:
    def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.obj=[];self.bounds=[]
    def var(self,name,bound=(None,None),cost=0.0):
        if name in self.idx:return self.idx[name]
        i=len(self.names);self.idx[name]=i;self.names.append(name);self.obj.append(cost);self.bounds.append(bound);return i
    def le(self,row,b):self.rows.append(row);self.rhs.append(b)
    def solve(self):
        A=lil_matrix((len(self.rows),len(self.names)),dtype=float)
        for i,row in enumerate(self.rows):
            for j,c in row.items():A[i,j]=c
        return linprog(np.array(self.obj),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def load_profiles(path):
    z=json.loads(Path(path).read_text());return [{'s':x['s'],'rho':x['rho'],'demand_id':x['demand_id']} for x in z['unresolved']]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--profiles',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=load_profiles(z.profiles);M=Builder()
    lam=M.var(('coef','lambda'),(0,None),1.0);c=M.var(('coef','c'),(0,None),1.0);mp=M.var(('coef','mu_plus'),(0,None),1.0);mm=M.var(('coef','mu_minus'),(0,None),1.0);t2=M.var(('coef','tau2'),(0,None),1.0);t3=M.var(('coef','tau3'),(0,None),1.0)
    # Use common grids large enough for every legal local coordinate in this regime.
    F={};G={};eps=1e-6
    for d in range(z.a+1):
        for h in range(z.b+1):F[d,h]=M.var(('F',d,h),(0,None),eps)
    for s in range(z.a+1):
        for h in range(z.b+1):G[s,h]=M.var(('G',s,h),(0,None),eps)
    # Remove irrelevant additive constants.
    M.le({F[0,z.b]:1},0);M.le({F[0,z.b]:-1},0);M.le({G[0,z.b]:1},0);M.le({G[0,z.b]:-1},0)
    # Monotonicity: increasing first coordinate, decreasing h.
    for d in range(z.a):
        for h in range(z.b+1):M.le({F[d,h]:1,F[d+1,h]:-1},0)
    for d in range(z.a+1):
        for h in range(z.b):M.le({F[d,h+1]:1,F[d,h]:-1},0)
    for s in range(z.a):
        for h in range(z.b+1):M.le({G[s,h]:1,G[s+1,h]:-1},0)
    for s in range(z.a+1):
        for h in range(z.b):M.le({G[s,h+1]:1,G[s,h]:-1},0)

    profile_meta=[]
    for pi,p in enumerate(P):
        sc=Counter(p['s']);rc=Counter(p['rho']);ells={};sigs={}
        for s,n in sorted(sc.items()):
            e=M.var(('ell',pi,s),(None,None));ells[s]=e
            for R in range(z.dmax-s+1):
                for x in range(s,z.b-R+1):
                    d=R+s;h=R+x
                    # ell <= lambda R + c x + x(F+G)
                    M.le({e:1,lam:-R,c:-x,F[d,h]:-x,G[s,h]:-x},0)
        for rho,n in sorted(rc.items()):
            sg=M.var(('sigma',pi,rho),(None,None));sigs[rho]=sg
            qmax=min(z.a-rho,sum(si<=rho for si in p['s']))
            for q in range(qmax+1):
                pmax=min(rho+z.b-z.a-1,z.b-1-q)
                for pp in range(pmax+1):
                    alpha=rho+q-1;beta=q+pp
                    row={sg:1,mp:-(q-pp),mm:(q-pp),t2:-tterm(rho,q,pp,2),t3:-tterm(rho,q,pp,3),c:q}
                    if q:
                        row[F[alpha,beta]]=row.get(F[alpha,beta],0)+q
                        row[G[rho,beta]]=row.get(G[rho,beta],0)+q
                    M.le(row,0)
        r=sum(p['rho'])
        # sum mult ell + sum mult sigma - lambda*r >= 1.
        row={lam:r}
        for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
        for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
        M.le(row,-1)
        profile_meta.append({'profile':pi,'demand_id':p['demand_id'],'s':p['s'],'rho':p['rho'],'r':r})
    res=M.solve();out={'schema':'n30-shared-monotone-surface-envelope-recon-v1','success':bool(res.success),'status':int(res.status),'message':res.message,'profiles':profile_meta,'floating_point_reconnaissance_only':True}
    if res.success:
        sol=res.x
        out['objective']=float(res.fun);out['coefficients']={'lambda':float(sol[lam]),'c':float(sol[c]),'mu':float(sol[mp]-sol[mm]),'tau2':float(sol[t2]),'tau3':float(sol[t3])}
        margins=[]
        for pi,p in enumerate(P):
            sc=Counter(p['s']);rc=Counter(p['rho']);left=sum(n*sol[M.idx[('ell',pi,s)]] for s,n in sc.items())+sum(n*sol[M.idx[('sigma',pi,rho)]] for rho,n in rc.items());margin=left-sol[lam]*sum(p['rho']);margins.append(float(margin))
        out['margins']=margins;out['min_margin']=min(margins)
        # Compact the positive surfaces by reporting distinct rounded levels and all jump points.
        def compact(grid,firstmax):
            vals=[];jumps=[]
            for u in range(firstmax+1):
                prev=None
                for h in range(z.b+1):
                    v=float(sol[grid[u,h]])
                    if abs(v)<1e-9:v=0.0
                    vals.append(round(v,8))
                    if prev is None or abs(v-prev)>1e-7:jumps.append([u,h,v])
                    prev=v
            return {'distinct_levels':len(set(vals)),'nonzero_cells':sum(abs(v)>1e-9 for v in vals),'jumps':jumps}
        out['F_summary']=compact(F,z.a);out['G_summary']=compact(G,z.a)
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in out if k not in ('F_summary','G_summary','profiles')},indent=2,sort_keys=True))
if __name__=='__main__':main()
