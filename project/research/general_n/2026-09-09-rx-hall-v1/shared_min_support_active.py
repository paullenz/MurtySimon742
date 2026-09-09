#!/usr/bin/env python3
"""Minimum-support MILP restricted to the 31-shape active L1 shared library.

This is floating/MILP reconnaissance only. It reuses the exact same envelope
constraints as shared_greedy_prune, but asks for the minimum number of selected
BC/SH shapes among the shapes active in a supplied shared sparse solution.
"""
from collections import Counter
from pathlib import Path
import argparse,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
import importlib.util
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('gp',HERE/'shared_greedy_prune.py');gp=importlib.util.module_from_spec(sp);sp.loader.exec_module(gp)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--bc-json',type=Path,required=True);ap.add_argument('--shared-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--big-m',type=float,default=200);ap.add_argument('--time-limit',type=float,default=300);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 B=json.loads(z.bc_json.read_text());J=json.loads(z.shared_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['records']]
 bc=[tuple(tuple(p) for p in x['generators']) for x in J['active_BC']];sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
 base=gp.build(P,bc,sh,z.a,z.b,z.dmax);n0=len(base.names);names=list(base.names);lb=[];ub=[];integ=[];cost=[]
 for lo,hi in base.bounds:
  lb.append(-np.inf if lo is None else lo);ub.append(np.inf if hi is None else hi);integ.append(0);cost.append(0.0)
 rows=[dict(r) for r in base.rows];los=[-np.inf]*len(rows);his=list(base.rhs); selectors=[]
 for fam,count in [('BC',len(bc)),('SH',len(sh))]:
  for i in range(count):
   y=len(names);names.append(('Y',fam,i));lb.append(0);ub.append(1);integ.append(1);cost.append(1);selectors.append((fam,i,y))
   w=base.idx[(fam,i)];rows.append({w:1,y:-z.big_m});los.append(-np.inf);his.append(0)
 A=lil_matrix((len(rows),len(names)))
 for i,r in enumerate(rows):
  for j,v in r.items():A[i,j]=v
 res=milp(np.array(cost),integrality=np.array(integ),bounds=Bounds(np.array(lb),np.array(ub)),constraints=LinearConstraint(A.tocsr(),np.array(los),np.array(his)),options={'time_limit':z.time_limit,'mip_rel_gap':0.0})
 out={'schema':'n30-active-library-min-support-v1','success':bool(res.success),'status':int(res.status),'message':res.message,'candidate_BC':len(bc),'candidate_SH':len(sh),'floating_point_reconnaissance_only':True,'big_m':z.big_m,'time_limit':z.time_limit}
 if res.x is not None:
  actbc=[];actsh=[]
  for fam,i,y in selectors:
   if res.x[y]>0.5:
    rec={'index':i,'weight':float(res.x[base.idx[(fam,i)]]),'generators':[list(p) for p in (bc[i] if fam=='BC' else sh[i])]}
    (actbc if fam=='BC' else actsh).append(rec)
  out.update({'objective':None if res.fun is None else float(res.fun),'active_BC':actbc,'active_SH':actsh,'BC_count':len(actbc),'SH_count':len(actsh),'support_count':len(actbc)+len(actsh),'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None)})
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_BC','active_SH')},indent=2,sort_keys=True))
if __name__=='__main__':main()
