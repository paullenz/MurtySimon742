#!/usr/bin/env python3
"""Minimum-support MILP over the full n29 common staircase dictionary.

Unlike n29_common_active_min_support.py, this does not restrict to the 25 shapes
that happened to receive positive weight in the first L1 common solution.
It uses all candidate BC/SH shapes recorded in N29_COMMON_POTENTIAL_RUN and asks
for minimum support for one common staircase potential across the 38 trimmed
n29 t=2 transfer-survivor profiles. Floating/MILP reconnaissance only until a
selected support is exactified separately.
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
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--common-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--big-m',type=float,default=200);ap.add_argument('--time-limit',type=float,default=600);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());J=json.loads(z.common_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']];q=J['modes']['full'];assert q['success']
    # Full candidate shapes are stored by the common scan as deterministic libraries.
    if 'candidate_BC_shapes' in q: bc=[tuple(tuple(p) for p in g) for g in q['candidate_BC_shapes']]
    else:
        # Backward-compatible recovery: import the library constructor and rebuild it
        # from the 38 profiles exactly as the common scan did.
        raise SystemExit('common checkpoint lacks full candidate shape lists; regenerate with library recording')
    if 'candidate_SH_shapes' in q: sh=[tuple(tuple(p) for p in g) for g in q['candidate_SH_shapes']]
    else: raise SystemExit('common checkpoint lacks full SH candidate shape lists; regenerate with library recording')
    base=cp.build(P,bc,sh,z.a,z.b,z.dmax);names=list(base.names);lb=[];ub=[];integ=[];cost=[]
    for lo,hi in base.bounds:lb.append(-np.inf if lo is None else lo);ub.append(np.inf if hi is None else hi);integ.append(0);cost.append(0.0)
    rows=[dict(r) for r in base.rows];los=[-np.inf]*len(rows);his=list(base.rhs);selectors=[]
    for fam,count in [('BC',len(bc)),('SH',len(sh))]:
        for i in range(count):
            y=len(names);names.append(('Y',fam,i));lb.append(0);ub.append(1);integ.append(1);cost.append(1.0);selectors.append((fam,i,y));rows.append({base.idx[(fam,i)]:1,y:-z.big_m});los.append(-np.inf);his.append(0)
    A=lil_matrix((len(rows),len(names)))
    for i,r in enumerate(rows):
        for j,v in r.items():A[i,j]=v
    res=milp(np.array(cost),integrality=np.array(integ),bounds=Bounds(np.array(lb),np.array(ub)),constraints=LinearConstraint(A.tocsr(),np.array(los),np.array(his)),options={'time_limit':z.time_limit,'mip_rel_gap':0.0})
    out={'schema':'n29-common-global-min-support-v1','success':bool(res.success),'status':int(res.status),'message':res.message,'profiles':len(P),'candidate_BC':len(bc),'candidate_SH':len(sh),'big_m':z.big_m,'time_limit':z.time_limit,'floating_point_reconnaissance_only':True,'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None)}
    if res.x is not None:
        ab=[];ash=[]
        for fam,i,y in selectors:
            if res.x[y]>0.5:
                g=bc[i] if fam=='BC' else sh[i];rec={'index':i,'weight':float(res.x[base.idx[(fam,i)]]),'generators':[list(p) for p in g]};(ab if fam=='BC' else ash).append(rec)
        out.update({'objective':None if res.fun is None else float(res.fun),'BC_count':len(ab),'SH_count':len(ash),'support_count':len(ab)+len(ash),'active_BC':ab,'active_SH':ash})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('active_BC','active_SH')},indent=2,sort_keys=True))
if __name__=='__main__':main()
