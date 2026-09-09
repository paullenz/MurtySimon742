#!/usr/bin/env python3
"""Test demand 45's globally minimal 13-shape support on all 38 hard n29 t=2 profiles.

The support itself is fixed to the 7 BC + 6 SH shapes selected by the exact
zero-gap single-profile minimum for demand 45. The 13 staircase weights are
free but common across all 38 profiles; scalar dual multipliers and envelope
variables remain profile-specific. Floating reconnaissance only. If feasible,
demand 45 supplies the matching lower bound 13 within this generated dictionary,
so the common-support cardinality is pinned to 13 pending exactification.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('pc',HERE/'n29_common_potential_profile_scalars.py');pc=module_from_spec(sp);sp.loader.exec_module(pc)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--boundary-json',type=Path,required=True)
    ap.add_argument('--demand45-json',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text())
    D=json.loads(z.demand45_json.read_text())
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    Q=D['minimum']
    bc=[tuple(tuple(p) for p in x['generators']) for x in Q['active_BC']]
    sh=[tuple(tuple(p) for p in x['generators']) for x in Q['active_SH']]
    start=time.time();M=pc.build(P,bc,sh,12,16,10);res=M.solve()
    out={
      'schema':'n29-demand45-support-common38-v1',
      'profiles':len(P),
      'demand45_lower_bound_support':int(Q['support_count']),
      'BC_count':len(bc),'SH_count':len(sh),'support_count':len(bc)+len(sh),
      'success':bool(res.success),'status':int(res.status),'message':res.message,
      'objective':float(res.fun) if res.success else None,
      'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-start,
      'floating_point_reconnaissance_only':True,
      'interpretation':'The 13 support shapes are fixed from demand 45; staircase weights are common across all 38 profiles, while scalar dual bookkeeping is profile-specific.'
    }
    out['BC_shapes']=[[list(p) for p in g] for g in bc]
    out['SH_shapes']=[[list(p) for p in g] for g in sh]
    if res.success:
        out['BC_weights']=[float(res.x[M.idx[('BC',i)]]) for i in range(len(bc))]
        out['SH_weights']=[float(res.x[M.idx[('SH',i)]]) for i in range(len(sh))]
        out['threshold_union']=sorted({j for pi in range(len(P)) for j in range(1,13) if res.x[M.idx[('tau',pi,j)]]>1e-8})
    z.output.parent.mkdir(parents=True,exist_ok=True)
    z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','SH_shapes','BC_weights','SH_weights')},indent=2,sort_keys=True))
if __name__=='__main__':main()
