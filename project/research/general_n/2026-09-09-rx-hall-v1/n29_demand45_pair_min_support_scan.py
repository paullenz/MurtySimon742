#!/usr/bin/env python3
"""Search for a two-profile lower-bound witness for the n29 common support size.

Demand 45 has a zero-gap 13-shape minimum in the full generated 75 BC + 12 SH
dictionary. Any common 13-shape potential for all 38 hard profiles must therefore
also be an optimal 13-shape solution for demand 45. Pair demand 45 with each of
the other 37 profiles and solve the full-dictionary minimum-support MILP. If a
pair has certified optimum 14, it is a compact computational lower-bound witness
for the 38-profile problem (subject to the stated big-M coefficient cap).

For the first 14-support pair found at M=200, automatically re-solve at M=1000
to guard against a coefficient-cap artefact. Floating/MILP reconnaissance only;
this does not constitute an exact mathematical infeasibility certificate.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def build_dictionary(S,C,dmax):
    basebc={cp.trim(tuple(tuple(p) for p in x['generators']),dmax) for x in S['active_BC']}
    basesh={tuple(tuple(p) for p in x['generators']) for x in S['active_SH']}
    bc=set(basebc);sh=set(basesh)
    for r in C['records']:
        for x in r['cuts']:
            g=tuple(tuple(p) for p in x['generators']);(bc if x['family']=='BC' else sh).add(g)
    return sorted(bc),sorted(sh)

def solve_pair(P,bc,sh,big_m,time_limit):
    base=cp.build(P,bc,sh,12,16,10);names=list(base.names);lb=[];ub=[];integ=[];cost=[]
    for lo,hi in base.bounds:
        lb.append(-np.inf if lo is None else lo);ub.append(np.inf if hi is None else hi);integ.append(0);cost.append(0.0)
    rows=[dict(r) for r in base.rows];los=[-np.inf]*len(rows);his=list(base.rhs);selectors=[]
    for fam,count in [('BC',len(bc)),('SH',len(sh))]:
        for i in range(count):
            y=len(names);names.append(('Y',fam,i));lb.append(0);ub.append(1);integ.append(1);cost.append(1.0);selectors.append((fam,i,y))
            rows.append({base.idx[(fam,i)]:1,y:-big_m});los.append(-np.inf);his.append(0)
    A=lil_matrix((len(rows),len(names)))
    for i,r in enumerate(rows):
        for j,v in r.items():A[i,j]=v
    st=time.time();res=milp(np.array(cost),integrality=np.array(integ),bounds=Bounds(np.array(lb),np.array(ub)),constraints=LinearConstraint(A.tocsr(),np.array(los),np.array(his)),options={'time_limit':time_limit,'mip_rel_gap':0.0})
    q={'success':bool(res.success),'status':int(res.status),'message':res.message,'seconds':time.time()-st,'mip_gap':getattr(res,'mip_gap',None),'mip_node_count':getattr(res,'mip_node_count',None),'objective':None if res.fun is None else float(res.fun),'big_m':big_m,'rows':len(rows),'variables':len(names)}
    if res.x is not None:
        ab=[];ash=[]
        for fam,i,y in selectors:
            if res.x[y]>0.5:
                rec={'index':i,'weight':float(res.x[base.idx[(fam,i)]])};(ab if fam=='BC' else ash).append(rec)
        q.update({'BC_count':len(ab),'SH_count':len(ash),'support_count':len(ab)+len(ash),'active_BC':ab,'active_SH':ash})
    return q

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--time-limit',type=float,default=90);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text())
    profiles=[{'position':i,'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for i,r in enumerate(B['trimmed_survivor_records'])]
    hits=[p for p in profiles if p['demand_id']==45]
    if not hits:raise SystemExit('demand 45 not found')
    d45=hits[0];bc,sh=build_dictionary(S,C,10);records=[];witness=None
    for p in profiles:
        if p['position']==d45['position']:continue
        pair=[{'s':d45['s'],'rho':d45['rho'],'demand_id':45},{'s':p['s'],'rho':p['rho'],'demand_id':p['demand_id']}]
        q=solve_pair(pair,bc,sh,200,z.time_limit);q.update({'other_position':p['position'],'other_demand_id':p['demand_id']})
        print(json.dumps({k:v for k,v in q.items() if k not in ('active_BC','active_SH')},sort_keys=True),flush=True);records.append(q)
        if q['success'] and q.get('support_count') is not None and q['support_count']>=14 and (q.get('mip_gap') in (0,0.0,None)):
            v=solve_pair(pair,bc,sh,1000,z.time_limit);v.update({'other_position':p['position'],'other_demand_id':p['demand_id']});q['validation_M1000']=v
            if v['success'] and v.get('support_count') is not None and v['support_count']>=14 and (v.get('mip_gap') in (0,0.0,None)):
                witness={'other_position':p['position'],'other_demand_id':p['demand_id'],'M200_support':q['support_count'],'M1000_support':v['support_count']};break
    out={'schema':'n29-demand45-pair-min-support-scan-v1','demand45_position':d45['position'],'demand45_id':45,'candidate_BC':len(bc),'candidate_SH':len(sh),'profiles_total':len(profiles),'pairs_tested':len(records),'witness':witness,'records':records,'floating_milp_reconnaissance_only':True,'interpretation':'A witness with optimum 14 at M=200 and M=1000 is a compact computational lower-bound witness against common support 13 under both coefficient caps; exact mathematical infeasibility is not claimed.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True))
if __name__=='__main__':main()
