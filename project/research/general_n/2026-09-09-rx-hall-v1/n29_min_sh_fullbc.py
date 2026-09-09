#!/usr/bin/env python3
"""Minimize SH support for n29 while all 75 canonical BC shapes remain available.

The finite common-potential LP is augmented with one binary selector per SH shape
and constraints w_SH <= M*y.  BC weights are unrestricted nonnegative continuous
variables from the complete canonical 75-shape dictionary.  The objective is the
number of active SH shapes.  Modes hard38, t2, t3 match n29_sh3_fullbc_scan.py.

This is MILP support-minimality evidence under coefficient cap M, not an exact
mathematical nonexistence certificate.  Positive selected supports should be
exactified separately.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('pc',HERE/'n29_common_potential_profile_scalars.py');pc=module_from_spec(sp);sp.loader.exec_module(pc)
sp2=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp2);sp2.loader.exec_module(allx)

def tup(g):return tuple(tuple(p) for p in g)

def load_profiles(z):
    if z.mode=='hard38':
        B=json.loads(z.boundary_json.read_text());return [{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    t=2 if z.mode=='t2' else 3;P=allx.load29(z.demands_json,z.rows,t);return [{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P]

def solve(P,bc,sh,Mcap,time_limit):
    base=pc.build(P,bc,sh,12,16,10);names=list(base.names);lb=[];ub=[];integ=[];cost=[]
    for lo,hi in base.bounds:
        lb.append(-np.inf if lo is None else lo);ub.append(np.inf if hi is None else hi);integ.append(0);cost.append(0.0)
    rows=[dict(r) for r in base.rows];los=[-np.inf]*len(rows);his=list(base.rhs);selectors=[]
    for j in range(len(sh)):
        y=len(names);names.append(('YSH',j));lb.append(0);ub.append(1);integ.append(1);cost.append(1.0);selectors.append((j,y))
        rows.append({base.idx[('SH',j)]:1,y:-Mcap});los.append(-np.inf);his.append(0)
    A=lil_matrix((len(rows),len(names)))
    for i,r in enumerate(rows):
        for j,v in r.items():A[i,j]=v
    st=time.time();res=milp(np.array(cost),integrality=np.array(integ),bounds=Bounds(np.array(lb),np.array(ub)),constraints=LinearConstraint(A.tocsr(),np.array(los),np.array(his)),options={'time_limit':time_limit,'mip_rel_gap':0.0})
    out={'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':None if res.fun is None else float(res.fun),'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None),'seconds':time.time()-st,'big_m':Mcap,'rows':len(rows),'variables':len(names)}
    if res.x is not None:
        active=[j for j,y in selectors if res.x[y]>0.5];out['SH_support_count']=len(active);out['active_SH_indices']=active;out['SH_weights']=[float(res.x[base.idx[('SH',j)]]) for j in active]
        ab=[i for i in range(len(bc)) if res.x[base.idx[('BC',i)]]>1e-8];out['active_BC_count']=len(ab);out['active_BC_indices']=ab
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['hard38','t2','t3'],required=True);ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--boundary-json',type=Path);ap.add_argument('--demands-json',type=Path);ap.add_argument('--rows',type=Path);ap.add_argument('--time-limit',type=float,default=300);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    D=json.loads(z.dictionary_json.read_text());bc=[tup(x['generators']) for x in D['BC']];sh=[tup(x['generators']) for x in D['SH']];P=load_profiles(z)
    r200=solve(P,bc,sh,200,z.time_limit);validation=None
    if r200.get('SH_support_count') is not None:validation=solve(P,bc,sh,1000,z.time_limit)
    out={'schema':'n29-min-sh-fullbc-v1','mode':z.mode,'profiles':len(P),'BC_count':len(bc),'SH_candidate_count':len(sh),'M200':r200,'M1000_validation':validation,'floating_milp_reconnaissance_only':True,'interpretation':'All 75 BC shapes remain available. Binary selectors minimize the number of active SH shapes. Matching zero-gap minima at M=200 and M=1000 are strong computational support-minimality evidence, not exact impossibility certificates.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
