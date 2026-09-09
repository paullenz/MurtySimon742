#!/usr/bin/env python3
"""Reconnaissance: can the minimized exceptional 6+3 shapes separate all 7 profiles?

Uses exactly the six BC and three indispensable SH staircase shapes from the
unit-bound-free exceptional certificate, but re-optimises their nonnegative
weights and shared lambda,c,mu,tau2,tau3 across all seven hard profiles.
Reports shared feasibility and individual feasibility under the same shape
library. Floating point is reconnaissance only.
"""
from collections import Counter
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

BC=[
 ((1,-2),(3,-4),(4,-6),(6,-8),(9,-9)),
 ((1,-1),(2,-4),(3,-9),(4,-13)),
 ((1,-2),(2,-3),(3,-4),(4,-5)),
 ((1,-1),(2,-4)),
 ((1,-1),(2,-2),(3,-5),(6,-6),(7,-7),(8,-10),(11,-12)),
 ((1,-3),),
]
SH=[
 ((1,-1),(2,-5),(3,-6)),
 ((1,-1),(2,-7)),
 ((1,-1),(2,-2),(3,-11)),
]

def inside(pt,g):return any(a<=pt[0] and b<=pt[1] for a,b in g)
def tt(r,q,p,j):return (q if q>=j+1 else 0)-(p if r+q>=j else 0)

class LP:
 def __init__(self):self.names=[];self.idx={};self.rows=[];self.rhs=[];self.c=[];self.bounds=[]
 def var(self,n,b=(None,None),cost=0):
  if n in self.idx:return self.idx[n]
  i=len(self.names);self.idx[n]=i;self.names.append(n);self.c.append(cost);self.bounds.append(b);return i
 def le(self,r,b):self.rows.append(r);self.rhs.append(b)
 def solve(self):
  A=lil_matrix((len(self.rows),len(self.names)))
  for i,r in enumerate(self.rows):
   for j,v in r.items():A[i,j]=v
  return linprog(np.array(self.c),A_ub=A.tocsr(),b_ub=np.array(self.rhs),bounds=self.bounds,method='highs')

def solve(profiles,a,b,dmax):
 M=LP();lam=M.var('lambda',(0,None),1);c=M.var('c',(0,None),1);mp=M.var('mu+',(0,None),1);mm=M.var('mu-',(0,None),1);t2=M.var('tau2',(0,None),1);t3=M.var('tau3',(0,None),1)
 bw=[M.var(('BC',i),(0,None),1) for i in range(6)];sw=[M.var(('SH',i),(0,None),1) for i in range(3)]
 def pot(row,bcpt,shpt,factor,sign):
  for i,g in enumerate(BC):
   if inside(bcpt,g):row[bw[i]]=row.get(bw[i],0)+sign*factor
  for i,g in enumerate(SH):
   if inside(shpt,g):row[sw[i]]=row.get(sw[i],0)+sign*factor
 meta=[]
 for pi,p in enumerate(profiles):
  sc=Counter(p['s']);rc=Counter(p['rho']);ells={};sigs={}
  for s,n in sorted(sc.items()):
   e=M.var(('ell',pi,s),(None,None));ells[s]=e
   for R in range(dmax-s+1):
    for x in range(s,b-R+1):
     h=R+x;row={e:1,lam:-R,c:-x};pot(row,(R+s,-h),(s,-h),x,-1);M.le(row,0)
  for rho,n in sorted(rc.items()):
   sg=M.var(('sig',pi,rho),(None,None));sigs[rho]=sg;qmax=min(a-rho,sum(si<=rho for si in p['s']))
   for q in range(qmax+1):
    pmax=min(rho+b-a-1,b-1-q)
    for pp in range(pmax+1):
     beta=q+pp;row={sg:1,mp:-(q-pp),mm:(q-pp),t2:-tt(rho,q,pp,2),t3:-tt(rho,q,pp,3),c:q};pot(row,(rho+q-1,-beta),(rho,-beta),q,1);M.le(row,0)
  row={lam:sum(p['rho'])}
  for s,n in sc.items():row[ells[s]]=row.get(ells[s],0)-n
  for rho,n in rc.items():row[sigs[rho]]=row.get(sigs[rho],0)-n
  M.le(row,-1);meta.append((ells,sigs))
 res=M.solve();out={'success':bool(res.success),'status':int(res.status),'message':res.message}
 if res.success:
  x=res.x;out['objective']=float(res.fun);out['coefficients']={'lambda':float(x[lam]),'c':float(x[c]),'mu':float(x[mp]-x[mm]),'tau2':float(x[t2]),'tau3':float(x[t3]),'BC':[float(x[v]) for v in bw],'SH':[float(x[v]) for v in sw]};marg=[]
  for pi,p in enumerate(profiles):
   sc=Counter(p['s']);rc=Counter(p['rho']);ells,sigs=meta[pi];left=sum(n*x[ells[s]] for s,n in sc.items())+sum(n*x[sigs[r]] for r,n in rc.items());marg.append(float(left-x[lam]*sum(p['rho'])))
  out['margins']=marg;out['min_margin']=min(marg);out['active_shapes']=sum(v>1e-8 for v in out['coefficients']['BC'])+sum(v>1e-8 for v in out['coefficients']['SH'])
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--profiles',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();raw=json.loads(z.profiles.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in raw['unresolved']]
 shared=solve(P,z.a,z.b,z.dmax);individual=[]
 for i,p in enumerate(P):individual.append({'profile':i,'demand_id':p['demand_id'],**solve([p],z.a,z.b,z.dmax)})
 out={'schema':'n30-shared-nine-shape-recon-v1','BC_shapes':[[list(x) for x in g] for g in BC],'SH_shapes':[[list(x) for x in g] for g in SH],'shared':shared,'individual':individual,'floating_point_reconnaissance_only':True}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'shared':shared,'individual_success':[x['success'] for x in individual]},indent=2,sort_keys=True))
if __name__=='__main__':main()
