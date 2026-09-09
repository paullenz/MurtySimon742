#!/usr/bin/env python3
"""Stratify n29 common-potential complexity by maximum demand H0=max(s).

Uses the 25-shape active common library (17 BC + 8 SH) and solves a separate
minimum-support MILP for each H0 class among the 38 trimmed t=2 survivors.
This is floating reconnaissance intended to test whether the extra n29 SH/BC
shapes form a nested maximum-demand correction family.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def solve(P,bc,sh,a,b,dmax,big_m,time_limit):
    base=cp.build(P,bc,sh,a,b,dmax);names=list(base.names);lb=[];ub=[];integ=[];cost=[]
    for lo,hi in base.bounds:lb.append(-np.inf if lo is None else lo);ub.append(np.inf if hi is None else hi);integ.append(0);cost.append(0.0)
    rows=[dict(r) for r in base.rows];los=[-np.inf]*len(rows);his=list(base.rhs);sels=[]
    for fam,count in [('BC',len(bc)),('SH',len(sh))]:
        for i in range(count):
            y=len(names);names.append(('Y',fam,i));lb.append(0);ub.append(1);integ.append(1);cost.append(1.0);sels.append((fam,i,y));rows.append({base.idx[(fam,i)]:1,y:-big_m});los.append(-np.inf);his.append(0)
    A=lil_matrix((len(rows),len(names)))
    for i,r in enumerate(rows):
        for j,v in r.items():A[i,j]=v
    res=milp(np.array(cost),integrality=np.array(integ),bounds=Bounds(np.array(lb),np.array(ub)),constraints=LinearConstraint(A.tocsr(),np.array(los),np.array(his)),options={'time_limit':time_limit,'mip_rel_gap':0.0})
    out={'success':bool(res.success),'status':int(res.status),'message':res.message,'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None)}
    if res.x is not None:
        A1=[];A2=[]
        for fam,i,y in sels:
            if res.x[y]>0.5:
                rec={'index':i,'generators':[list(p) for p in (bc[i] if fam=='BC' else sh[i])],'weight':float(res.x[base.idx[(fam,i)]])};(A1 if fam=='BC' else A2).append(rec)
        out.update({'support_count':len(A1)+len(A2),'BC_count':len(A1),'SH_count':len(A2),'active_BC':A1,'active_SH':A2,'objective':None if res.fun is None else float(res.fun)})
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--common-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--big-m',type=float,default=200);ap.add_argument('--time-limit',type=float,default=120);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());J=json.loads(z.common_json.read_text());q=J['modes']['full'];bc=[tuple(tuple(p) for p in g) for g in q['active_BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in q['active_SH_shapes']]
    raw=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']];groups={}
    for p in raw:groups.setdefault(max(p['s']),[]).append(p)
    results={}
    for H,P in sorted(groups.items()):
        results[str(H)]={'profiles':len(P),'minimum':solve(P,bc,sh,z.a,z.b,z.dmax,z.big_m,z.time_limit)}
    out={'schema':'n29-hmax-support-stratification-v1','profiles':len(raw),'candidate_BC':len(bc),'candidate_SH':len(sh),'floating_point_reconnaissance_only':True,'results':results,'interpretation':'Separate support minima by H0=max(s), inside the 25-shape active common library. Used to detect nested maximum-demand correction structure.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({H:{'profiles':v['profiles'],'support_count':v['minimum'].get('support_count'),'BC':v['minimum'].get('BC_count'),'SH':v['minimum'].get('SH_count'),'gap':v['minimum'].get('mip_gap')} for H,v in results.items()},indent=2,sort_keys=True))
if __name__=='__main__':main()
