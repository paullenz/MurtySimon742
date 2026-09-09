#!/usr/bin/env python3
"""Minimum-support MILP for one selected n29 trimmed-survivor profile over the full dictionary.

Rebuilds the full specialised-base plus pairwise-correction staircase library and
selects one profile by demand_id and optional occurrence index. Used to test
whether the extreme support complexity of demand 45 is intrinsic or an artefact
of restricting to the first common solution's active library. Floating/MILP
reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('gm',HERE/'n29_common_global_min_support.py');gm=module_from_spec(sp);sp.loader.exec_module(gm)
sp2=spec_from_file_location('hs',HERE/'n29_hmax_support_scan.py');hs=module_from_spec(sp2);sp2.loader.exec_module(hs)
sp3=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp3);sp3.loader.exec_module(cp)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--demand-id',type=int,required=True);ap.add_argument('--occurrence',type=int,default=0);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--big-m',type=float,default=200);ap.add_argument('--time-limit',type=float,default=180);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text())
    matches=[r for r in B['trimmed_survivor_records'] if r['demand_id']==z.demand_id];r=matches[z.occurrence];P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']}]
    bc={cp.trim(tuple(tuple(p) for p in x['generators']),z.dmax) for x in S['active_BC']};sh={tuple(tuple(p) for p in x['generators']) for x in S['active_SH']}
    for rr in C['records']:
        for x in rr['cuts']:
            g=tuple(tuple(p) for p in x['generators']);(bc if x['family']=='BC' else sh).add(g)
    bc=sorted(bc);sh=sorted(sh);m=hs.solve(P,bc,sh,z.a,z.b,z.dmax,z.big_m,z.time_limit)
    out={'schema':'n29-single-full-min-support-v1','demand_id':z.demand_id,'occurrence':z.occurrence,'s':r['s'],'rho':r['rho'],'S':sum(r['s']),'H0':max(r['s']),'candidate_BC':len(bc),'candidate_SH':len(sh),'minimum':m,'floating_point_reconnaissance_only':True}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'demand_id':z.demand_id,'candidate_BC':len(bc),'candidate_SH':len(sh),'support':m.get('support_count'),'BC':m.get('BC_count'),'SH':m.get('SH_count'),'gap':m.get('mip_gap')},indent=2))
if __name__=='__main__':main()
