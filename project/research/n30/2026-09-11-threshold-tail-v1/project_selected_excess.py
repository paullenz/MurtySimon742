#!/usr/bin/env python3
"""Project the eight N30 m=226 endpoint relaxations onto M and E=M-S.

For each row compare the feasible total selected-edge count under:
  A. all current constraints except supplement P-flow;
  B. all current constraints except nested endpoint load.
If the M intervals separate, that exposes an immediate scalar hand proof.
"""
from __future__ import annotations
import json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

HERE=Path(__file__).resolve().parent
MODEL_DIR=HERE.parent/'2026-09-08-minimal-kernel-recon-v1'
sys.path.insert(0,str(MODEL_DIR))
from n30_threshold_model import build

ROWS=[
 ('2233',[2,2]+[3]*11,[1]*7+[2]+[3]*8),
 ('2331',[2]+[3]*12,[1]*7+[3]*9),
 ('3^13-r35a',[3]*13,[1]*7+[3]*8+[4]),
 ('3^13-r35b',[3]*13,[1]*6+[2]+[3]*9),
 ('3344',[3]*4+[4]*9,[1]*6+[3]*2+[4]*8),
 ('3344b',[3]*2+[4]*11,[1]*5+[2]+[3]+[4]*9),
 ('3444',[3]+[4]*12,[1]*5+[2]+[4]*10),
 ('4^13',[4]*13,[1]*5+[3]+[4]*10),
]

def types(m,row):return {m.names[j][0] for j in row}
def ubkind(m,i):
 if i>=m.bound_start:return 'bounds'
 row,r=m.ub[i];t=types(m,row)
 if t<= {'T','Y'}:return 'Tmon'
 if t=={'P'}:return 'Ppair'
 if t<= {'W','Z'} and 'W'in t:return 'source_label_cap'
 if t<= {'T','Z'}:return 'nested_endpoint'
 return 'ub_other'
def eqkind(m,i):
 row,r=m.eq[i];t=types(m,row)
 if t=={'Y'}:
  if r==1:return 'label_norm'
  return 'label_totals'
 if t<= {'T','Y'}:return 'forced_tail'
 if t=={'W'}:return 'source_norm'
 if t<= {'W','P'} and 'P'in t:return 'Pflow'
 if t<= {'W','Z'} and 'Z'in t:return 'source_q'
 if t<= {'T','Z'} and 'Z'in t:return 'label_x_tail'
 return 'eq_other'

def matrices(m,drop):
 u=[x for i,x in enumerate(m.ub) if ubkind(m,i) not in drop]
 e=[x for i,x in enumerate(m.eq) if eqkind(m,i) not in drop]
 N=len(m.names)
 def mat(rows):
  rr=[];cc=[];vv=[];b=[]
  for i,(d,bb) in enumerate(rows):
   b.append(bb)
   for j,c in d.items():rr.append(i);cc.append(j);vv.append(c)
  return coo_matrix((vv,(rr,cc)),shape=(len(rows),N)).tocsr(),np.array(b,float)
 A,b=mat(u);E,f=mat(e);return A,b,E,f

def M_objective(m,rho):
 # W variables are fractions within each residual-degree group.
 from collections import Counter
 SG=sorted(Counter(rho).items())
 c=np.zeros(len(m.names))
 for j,nm in enumerate(m.names):
  if isinstance(nm,tuple) and nm[0]=='W':
   _,k,q,p=nm;c[j]=SG[k][1]*q
 return c

def rng(m,rho,drop):
 A,b,E,f=matrices(m,drop);c=M_objective(m,rho)
 lo=linprog(c,A_ub=A,b_ub=b,A_eq=E,b_eq=f,bounds=(0,None),method='highs')
 hi=linprog(-c,A_ub=A,b_ub=b,A_eq=E,b_eq=f,bounds=(0,None),method='highs')
 def val(res,sign=1):
  return None if not res.success else float(sign*res.fun)
 return {'status_min':int(lo.status),'status_max':int(hi.status),'M_min':val(lo),'M_max':val(hi,-1)}

def main():
 out={'schema':'n30-m226-selected-excess-projection-v1','rows':[]}
 for tag,s,rho in ROWS:
  m=build(s,rho,2);S=sum(s)
  cases={
   'without_Pflow':rng(m,rho,{'Pflow'}),
   'without_nested':rng(m,rho,{'nested_endpoint'}),
   'without_Pflow_pair_Tmon_sourcecap_bounds':rng(m,rho,{'Pflow','Ppair','Tmon','source_label_cap','bounds'}),
   'without_nested_pair_Tmon_sourcecap_bounds':rng(m,rho,{'nested_endpoint','Ppair','Tmon','source_label_cap','bounds'}),
  }
  for q in cases.values():
   if q['M_min'] is not None:q['E_min']=q['M_min']-S
   if q['M_max'] is not None:q['E_max']=q['M_max']-S
  out['rows'].append({'tag':tag,'S':S,'r':sum(rho),'cases':cases})
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
