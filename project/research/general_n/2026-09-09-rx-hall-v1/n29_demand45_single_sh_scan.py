#!/usr/bin/env python3
"""Find the smallest explicit SH correction needed by demand 45 individually.

Demand 45 is the only one of the 38 difficult n29 t=2 profiles that is infeasible
with the complete 75-shape BC dictionary and no SH. Test every one of the 12
canonical SH staircases separately on top of all 75 BC shapes. If no singleton
works, test pairs. Floating LP proposal/feasibility evidence; positive supports
can be exactified separately.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,itertools,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)
def tup(g):return tuple(tuple(p) for p in g)
def solve(pf,bc,sh):
    M=cp.build([pf],bc,sh,12,16,10);r=M.solve();return r,M
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());D=json.loads(z.dictionary_json.read_text());bc=[tup(x['generators']) for x in D['BC']];allsh=[tup(x['generators']) for x in D['SH']];hits=[r for r in B['trimmed_survivor_records'] if r['demand_id']==45]
    if not hits:raise SystemExit('demand45 missing');r0=hits[0];pf={'s':r0['s'],'rho':r0['rho'],'demand_id':45};records=[];winners=[];st=time.time()
    for k in (0,1,2):
        for comb in itertools.combinations(range(len(allsh)),k):
            r,M=solve(pf,bc,[allsh[i] for i in comb]);q={'SH_indices':list(comb),'SH_count':k,'success':bool(r.success),'status':int(r.status),'message':r.message,'objective':float(r.fun) if r.success else None}
            if r.success:
                q['SH_weights']=[float(r.x[M.idx[('SH',j)]]) for j in range(k)];q['SH_shapes']=[[[a,b] for a,b in allsh[i]] for i in comb];winners.append(q)
            records.append(q);print(json.dumps({x:y for x,y in q.items() if x not in ('SH_weights','SH_shapes')},sort_keys=True),flush=True)
        if winners:break
    out={'schema':'n29-demand45-single-sh-scan-v1','demand_id':45,'BC_count':len(bc),'SH_candidate_count':len(allsh),'minimum_SH_count_found':min((w['SH_count'] for w in winners),default=None),'winner_count':len(winners),'winners':winners,'tests':len(records),'records':records,'seconds':time.time()-st,'floating_point_reconnaissance_only':True,'interpretation':'Each support is tested only on demand45 with the full 75 BC dictionary. First successful cardinality is a finite LP minimum within the enumerated SH dictionary; exact mathematical use requires rational exactification.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('winners','records')},indent=2,sort_keys=True))
if __name__=='__main__':main()
