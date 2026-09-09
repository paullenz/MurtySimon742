#!/usr/bin/env python3
"""Test the exact n30 three-SH core against n29 with the full 75-shape BC dictionary.

Modes:
  hard38 : the 38 difficult n29 t=2 profiles after boundary specialization;
  t2     : all 902 regenerated n29 t=2 hard profiles;
  t3     : all 94 regenerated n29 t=3 hard profiles;

BC weights and the three SH weights are common across every profile in the chosen
mode; scalar dual bookkeeping remains profile-specific. Floating reconnaissance
only. A compact positive result must be exactified before theorem use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('pc',HERE/'n29_common_potential_profile_scalars.py');pc=module_from_spec(sp);sp.loader.exec_module(pc)
sp2=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp2);sp2.loader.exec_module(allx)

def tup(g):return tuple(tuple(p) for p in g)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['hard38','t2','t3'],required=True)
    ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--n30-exact',type=Path,required=True)
    ap.add_argument('--boundary-json',type=Path);ap.add_argument('--demands-json',type=Path);ap.add_argument('--rows',type=Path)
    ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    D=json.loads(z.dictionary_json.read_text());E=json.loads(z.n30_exact.read_text())
    bc=[tup(x['generators']) for x in D['BC']];sh=[tup(g) for g in E['SH_shapes']]
    if z.mode=='hard38':
        if not z.boundary_json:raise SystemExit('--boundary-json required')
        B=json.loads(z.boundary_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    else:
        if not z.demands_json or not z.rows:raise SystemExit('--demands-json and --rows required')
        t=2 if z.mode=='t2' else 3;P=allx.load29(z.demands_json,z.rows,t)
        # strip cross-order metadata: build() only uses s/rho.
        P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P]
    st=time.time();M=pc.build(P,bc,sh,12,16,10);res=M.solve()
    out={'schema':'n29-sh3-fullbc-scan-v1','mode':z.mode,'profiles':len(P),'BC_count':len(bc),'SH_count':len(sh),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True,'interpretation':'All 75 canonical n29 BC shapes are available, but SH is restricted to the three exact n30 SH shapes; staircase weights are common within the selected profile set.'}
    if res.success:
        ab=[i for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8];ash=[i for i in range(len(sh)) if res.x[M.idx[('SH',i)]]>1e-8]
        out.update({'active_BC':ab,'active_SH':ash,'active_BC_count':len(ab),'active_SH_count':len(ash),'BC_weights':[float(res.x[M.idx[('BC',i)]]) for i in ab],'SH_weights':[float(res.x[M.idx[('SH',i)]]) for i in ash]})
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_weights','SH_weights')},indent=2,sort_keys=True))
if __name__=='__main__':main()
