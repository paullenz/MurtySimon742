#!/usr/bin/env python3
"""Test each of the 38 difficult n29 t=2 profiles individually with BC only.

All 75 canonical BC staircase shapes are available and SH is absent. Each profile
gets its own BC weights and scalar dual bookkeeping. This distinguishes intrinsic
need for the lost-coordinate SH correction from SH merely helping one *common*
potential cover several individually-BC-feasible profiles. Floating LP evidence;
individual infeasibility is a finite model result for the full generated BC library.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)
def tup(g):return tuple(tuple(p) for p in g)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());D=json.loads(z.dictionary_json.read_text());bc=[tup(x['generators']) for x in D['BC']];records=[];st=time.time()
    for pos,r in enumerate(B['trimmed_survivor_records']):
        pf={'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']};t0=time.time();M=cp.build([pf],bc,[],12,16,10);res=M.solve();q={'position':pos,'demand_id':r['demand_id'],'s':r['s'],'rho':r['rho'],'success':bool(res.success),'status':int(res.status),'message':res.message,'seconds':time.time()-t0,'objective':float(res.fun) if res.success else None}
        if res.success:
            ab=[i for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8];q['active_BC_count']=len(ab);q['active_BC_indices']=ab
        records.append(q);print(json.dumps({k:v for k,v in q.items() if k not in ('s','rho','active_BC_indices')},sort_keys=True),flush=True)
    out={'schema':'n29-hard38-bc-only-individual-v1','profiles':len(records),'BC_count':len(bc),'SH_count':0,'feasible_count':sum(r['success'] for r in records),'infeasible_count':sum(not r['success'] for r in records),'infeasible_positions':[r['position'] for r in records if not r['success']],'infeasible_demand_ids':[r['demand_id'] for r in records if not r['success']],'seconds':time.time()-st,'floating_point_reconnaissance_only':True,'records':records,'interpretation':'Each profile is solved separately with the complete canonical n29 BC dictionary and no SH. All-feasible means SH is not individually necessary on these 38 profiles, even if common BC-only weights fail.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True))
if __name__=='__main__':main()
