#!/usr/bin/env python3
"""Try to repair demand 45's 13-shape support by adding one generated staircase.

For each of the 74 shapes outside the demand-45 optimum, solve the common-weight
LP across all 38 hard n29 t=2 profiles on support D45 union {candidate}. Stop at
the first feasible 14-shape repair. This is floating reconnaissance only; a
positive result must be exactified.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('pc',HERE/'n29_common_potential_profile_scalars.py');pc=module_from_spec(sp);sp.loader.exec_module(pc)
sp2=spec_from_file_location('pm',HERE/'n29_demand45_pair_min_support_scan.py');pm=module_from_spec(sp2);sp2.loader.exec_module(pm)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--correction-json',type=Path,required=True);ap.add_argument('--demand45-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());C=json.loads(z.correction_json.read_text());D=json.loads(z.demand45_json.read_text())
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    allbc,allsh=pm.build_dictionary(S,C,10);Q=D['minimum'];dbc=sorted({tuple(tuple(p) for p in x['generators']) for x in Q['active_BC']});dsh=sorted({tuple(tuple(p) for p in x['generators']) for x in Q['active_SH']})
    candidates=[('BC',g) for g in allbc if g not in set(dbc)]+[('SH',g) for g in allsh if g not in set(dsh)];records=[];winner=None
    for k,(fam,g) in enumerate(candidates):
        bc=sorted(set(dbc)|({g} if fam=='BC' else set()));sh=sorted(set(dsh)|({g} if fam=='SH' else set()))
        st=time.time();M=pc.build(P,bc,sh,12,16,10);res=M.solve();q={'candidate_number':k,'family':fam,'generators':[list(p) for p in g],'success':bool(res.success),'status':int(res.status),'message':res.message,'seconds':time.time()-st,'objective':float(res.fun) if res.success else None}
        records.append(q);print(json.dumps(q,sort_keys=True),flush=True)
        if res.success:
            winner=dict(q);winner['BC_shapes']=[[list(p) for p in h] for h in bc];winner['SH_shapes']=[[list(p) for p in h] for h in sh];winner['BC_weights']=[float(res.x[M.idx[('BC',i)]]) for i in range(len(bc))];winner['SH_weights']=[float(res.x[M.idx[('SH',i)]]) for i in range(len(sh))];break
    out={'schema':'n29-demand45-one-addition-scan-v1','profiles':len(P),'base_support':13,'candidate_count':len(candidates),'candidates_tested':len(records),'winner':winner,'records':records,'floating_point_reconnaissance_only':True,'interpretation':'A winner is a 14-shape support obtained by adding one generated staircase to the demand-45 optimum; common weights are shared across all 38 profiles.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True))
if __name__=='__main__':main()
