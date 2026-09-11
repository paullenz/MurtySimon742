#!/usr/bin/env python3
"""Category ablation for the eight nontrivial N30 m=226 endpoint rows.

Purpose: identify which parts of the historical grouped LP are genuinely needed
for infeasibility, to guide a hand proof.  This is research tooling, not proof.
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

def solve_filtered(m,drop):
 u=[x for i,x in enumerate(m.ub) if ubkind(m,i) not in drop]
 e=[x for i,x in enumerate(m.eq) if eqkind(m,i) not in drop]
 N=len(m.names)
 def mat(rows):
  rr=[];cc=[];vv=[];b=[]
  for i,(d,bb) in enumerate(rows):
   b.append(bb)
   for j,c in d.items():rr.append(i);cc.append(j);vv.append(c)
  return coo_matrix((vv,(rr,cc)),shape=(len(rows),N)).tocsr(),np.array(b,float)
 A,b=mat(u);E,f=mat(e)
 return linprog(np.zeros(N),A_ub=A,b_ub=b,A_eq=E,b_eq=f,bounds=(0,None),method='highs').status

def main():
 cats=['Tmon','Ppair','source_label_cap','nested_endpoint','bounds','label_norm','label_totals','forced_tail','source_norm','Pflow','source_q','label_x_tail']
 out={'schema':'n30-m226-eight-model-ablation-v2','rows':[]}
 for tag,s,rho in ROWS:
  m=build(s,rho,2); assert solve_filtered(m,set())==2
  single={c:solve_filtered(m,{c}) for c in cats}
  probes={
   'no_pair_or_Tmon':{'Ppair','Tmon'},
   'no_source_label_cap':{'source_label_cap'},
   'no_Pflow':{'Pflow'},
   'no_nested':{'nested_endpoint'},
   'no_nested_no_sourcecap':{'nested_endpoint','source_label_cap'},
   'no_Pflow_no_pair':{'Pflow','Ppair'},
   'drop_all_apparently_inessential':{'Ppair','Tmon','bounds','source_label_cap'},
   'core_six_only':{'Ppair','Tmon','bounds','source_label_cap','label_norm','label_totals'},
   'core_six_plus_label_norm':{'Ppair','Tmon','bounds','source_label_cap','label_totals'},
   'core_six_plus_label_totals':{'Ppair','Tmon','bounds','source_label_cap','label_norm'},
  }
  multi={k:solve_filtered(m,v) for k,v in probes.items()}
  out['rows'].append({'tag':tag,'single_drop_status':single,'probe_status':multi})
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
