#!/usr/bin/env python3
"""Fixed-cardinality MILP feasibility for the common n29 F+G dictionary.

Uses the full 75 BC + 12 SH generated dictionary and the same 38-profile common
potential model with profile-specific scalar duals. Imposes sum(selectors)<=K
and asks only for feasibility. Status interpretation:
  FEASIBLE: a K-shape (or smaller) floating proposal exists;
  INFEASIBLE: MILP solver proved no such proposal in this dictionary/model;
  UNKNOWN: time limit or other nonterminal status.
Reconnaissance only until a feasible support is exactified.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('ms',HERE/'n29_common_potential_min_support.py');ms=module_from_spec(sp);sp.loader.exec_module(ms);cp=ms.cp

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--k',type=int,required=True);ap.add_argument('--big-m',type=float,default=200);ap.add_argument('--time-limit',type=float,default=600);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    bcpool={ms.trim(tuple(tuple(p) for p in x['generators']),z.dmax) for x in S['active_BC']};shpool={tuple(tuple(p) for p in x['generators']) for x in S['active_SH']}
    for r in C['records']:
        for x in r['cuts']:
            g=tuple(tuple(p) for p in x['generators']);(bcpool if x['family']=='BC' else shpool).add(g)
    bc=sorted(bcpool);sh=sorted(shpool);base=cp.build(P,bc,sh,z.a,z.b,z.dmax);names=list(base.names);lb=[];ub=[];integ=[];cost=[]
    for lo,hi in base.bounds:lb.append(-np.inf if lo is None else lo);ub.append(np.inf if hi is None else hi);integ.append(0);cost.append(0.0)
    rows=[dict(r) for r in base.rows];los=[-np.inf]*len(rows);his=list(base.rhs);selectors=[]
    for fam,count in [('BC',len(bc)),('SH',len(sh))]:
        for i in range(count):
            y=len(names);names.append(('Y',fam,i));lb.append(0);ub.append(1);integ.append(1);cost.append(0.0);selectors.append((fam,i,y));rows.append({base.idx[(fam,i)]:1,y:-z.big_m});los.append(-np.inf);his.append(0)
    rows.append({y:1 for fam,i,y in selectors});los.append(-np.inf);his.append(z.k)
    A=lil_matrix((len(rows),len(names)))
    for i,r in enumerate(rows):
        for j,v in r.items():A[i,j]=v
    res=milp(np.array(cost),integrality=np.array(integ),bounds=Bounds(np.array(lb),np.array(ub)),constraints=LinearConstraint(A.tocsr(),np.array(los),np.array(his)),options={'time_limit':z.time_limit,'mip_rel_gap':0.0})
    if res.status==0:verdict='FEASIBLE'
    elif res.status==2:verdict='INFEASIBLE'
    else:verdict='UNKNOWN'
    out={'schema':'n29-common-support-fixed-k-v1','k':z.k,'verdict':verdict,'status':int(res.status),'message':res.message,'profiles':len(P),'candidate_BC':len(bc),'candidate_SH':len(sh),'big_m':z.big_m,'time_limit':z.time_limit,'floating_point_milp_reconnaissance_only':True,'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None)}
    if res.x is not None:
        ab=[];ash=[]
        for fam,i,y in selectors:
            if res.x[y]>0.5:
                rec={'index':i,'weight':float(res.x[base.idx[(fam,i)]]),'generators':[list(p) for p in (bc[i] if fam=='BC' else sh[i])]};(ab if fam=='BC' else ash).append(rec)
        out.update({'BC_count':len(ab),'SH_count':len(ash),'support_count':len(ab)+len(ash),'active_BC':ab,'active_SH':ash})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_BC','active_SH')},indent=2,sort_keys=True))
if __name__=='__main__':main()
