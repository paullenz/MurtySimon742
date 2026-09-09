#!/usr/bin/env python3
"""Greedy support compression for the common n29 F+G potential.

Starts from the L1-active common staircase support in a saved successful
n29-common-potential-profile-scalars checkpoint. Keeps the staircase weights
common across all 38 profiles while refitting profile-specific scalar duals and
envelopes after each deletion. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--common-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());J=json.loads(z.common_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    q=J['modes']['full'];assert q['success'];bc=[tuple(tuple(p) for p in g) for g in q['active_BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in q['active_SH_shapes']]
    history=[];changed=True
    while changed:
        changed=False
        for fam,i in [('BC',i) for i in range(len(bc))]+[('SH',i) for i in range(len(sh))]:
            xb=bc[:i]+bc[i+1:] if fam=='BC' else list(bc);xs=sh[:i]+sh[i+1:] if fam=='SH' else list(sh)
            M,res=cp.build(P,xb,xs,z.a,z.b,z.dmax),None
            res=M.solve()
            if res.success:
                history.append({'family':fam,'index':i,'remaining_BC':len(xb),'remaining_SH':len(xs),'objective':float(res.fun)});bc,sh=xb,xs;changed=True;break
    M=cp.build(P,bc,sh,z.a,z.b,z.dmax);res=M.solve();assert res.success
    active_thresholds=sorted({j for pi in range(len(P)) for j in range(1,z.a+1) if res.x[M.idx[('tau',pi,j)]]>1e-8})
    out={'schema':'n29-common-potential-greedy-prune-v1','success':True,'profiles':len(P),'initial_BC':q['active_BC'],'initial_SH':q['active_SH'],'final_BC':len(bc),'final_SH':len(sh),'support_count':len(bc)+len(sh),'BC_shapes':[[list(p) for p in g] for g in bc],'SH_shapes':[[list(p) for p in g] for g in sh],'objective':float(res.fun),'active_threshold_union':active_thresholds,'variables':{str(name):float(res.x[i]) for i,name in enumerate(M.names)},'history':history,'floating_point_reconnaissance_only':True,'interpretation':'Locally deletion-minimal common F+G support across all 38 n29 profiles, with profile-specific scalar duals. Must be exactified.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','SH_shapes','variables','history')},indent=2,sort_keys=True))
if __name__=='__main__':main()
