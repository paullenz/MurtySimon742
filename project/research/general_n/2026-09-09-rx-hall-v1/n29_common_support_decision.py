#!/usr/bin/env python3
"""Decision MILP: is a common n29 staircase potential possible with support <=K?

Rebuilds the full 75 BC + 12 SH candidate dictionary for the 38 trimmed t=2
profiles. Instead of minimizing support, imposes sum(selector)<=K and asks for
feasibility. This is intended to settle K=12 and K=13 faster than a full global
cardinality optimization. Floating/MILP reconnaissance only; any feasible support
is exactified separately.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--K',type=int,required=True);ap.add_argument('--big-m',type=float,default=200);ap.add_argument('--time-limit',type=float,default=300);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    bc={cp.trim(tuple(tuple(p) for p in x['generators']),z.dmax) for x in S['active_BC']};sh={tuple(tuple(p) for p in x['generators']) for x in S['active_SH']}
    for rr in C['records']:
        for x in rr['cuts']:
            g=tuple(tuple(p) for p in x['generators']);(bc if x['family']=='BC' else sh).add(g)
    bc=sorted(bc);sh=sorted(sh);base=cp.build(P,bc,sh,z.a,z.b,z.dmax);names=list(base.names);lb=[];ub=[];integ=[];cost=[]
    for lo,hi in base.bounds:lb.append(-np.inf if lo is None else lo);ub.append(np.inf if hi is None else hi);integ.append(0);cost.append(0.0)
    rows=[dict(r) for r in base.rows];los=[-np.inf]*len(rows);his=list(base.rhs);sels=[]
    for fam,count in [('BC',len(bc)),('SH',len(sh))]:
        for i in range(count):
            y=len(names);names.append(('Y',fam,i));lb.append(0);ub.append(1);integ.append(1);cost.append(0.0);sels.append((fam,i,y));rows.append({base.idx[(fam,i)]:1,y:-z.big_m});los.append(-np.inf);his.append(0)
    rows.append({y:1 for _,_,y in sels});los.append(-np.inf);his.append(float(z.K))
    A=lil_matrix((len(rows),len(names)))
    for i,r in enumerate(rows):
        for j,v in r.items():A[i,j]=v
    res=milp(np.array(cost),integrality=np.array(integ),bounds=Bounds(np.array(lb),np.array(ub)),constraints=LinearConstraint(A.tocsr(),np.array(los),np.array(his)),options={'time_limit':z.time_limit,'mip_rel_gap':0.0})
    out={'schema':'n29-common-support-decision-v1','K':z.K,'profiles':len(P),'candidate_BC':len(bc),'candidate_SH':len(sh),'feasible':bool(res.success),'status':int(res.status),'message':res.message,'time_limit':z.time_limit,'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None),'floating_point_reconnaissance_only':True}
    if res.x is not None:
        ab=[];ash=[]
        for fam,i,y in sels:
            if res.x[y]>0.5:
                g=bc[i] if fam=='BC' else sh[i];rec={'index':i,'weight':float(res.x[base.idx[(fam,i)]]),'generators':[list(p) for p in g]};(ab if fam=='BC' else ash).append(rec)
        out.update({'support_count':len(ab)+len(ash),'BC_count':len(ab),'SH_count':len(ash),'active_BC':ab,'active_SH':ash})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_BC','active_SH')},indent=2,sort_keys=True))
if __name__=='__main__':main()
