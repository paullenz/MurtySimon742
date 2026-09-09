#!/usr/bin/env python3
"""Isolate which n30 hard profiles obstruct the exact n29 16-shape order-wide potential.

For each of the seven n30 t=1 hard profiles separately, solve one LP containing
all 996 n29 profiles plus that single n30 profile, with the exactified n29 9 BC
+ 7 SH support and one common staircase-weight vector. Scalar dual bookkeeping
remains profile-specific. This is floating reconnaissance; infeasibility is a
structural negative for the stated LP, while feasible cases would need exact
verification before theorem use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp);sp.loader.exec_module(allx)
sp2=spec_from_file_location('co',HERE/'cross_order_common_potential.py');co=module_from_spec(sp2);sp2.loader.exec_module(co)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--t2-demands',type=Path,required=True);ap.add_argument('--t2-rows',type=Path,required=True)
    ap.add_argument('--t3-demands',type=Path,required=True);ap.add_argument('--t3-rows',type=Path,required=True)
    ap.add_argument('--n30-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    J=json.loads(z.support_json.read_text());bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    P29=allx.load29(z.t2_demands,z.t2_rows,2)+allx.load29(z.t3_demands,z.t3_rows,3)
    N30=json.loads(z.n30_json.read_text())
    rec=[]
    for i,r in enumerate(N30['records']):
        pf={'order':'n30t1','id':i,'s':r['s'],'rho':r['rho'],'a':13,'b':16,'dmax':11}
        start=time.time();M=co.build(P29+[pf],bc,sh);res=M.solve()
        q={'n30_index':i,'s':r['s'],'rho':r['rho'],'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-start}
        if res.success:
            q['BC_weights']=[float(res.x[M.idx[('BC',j)]]) for j in range(len(bc))]
            q['SH_weights']=[float(res.x[M.idx[('SH',j)]]) for j in range(len(sh))]
        rec.append(q);print(json.dumps({k:v for k,v in q.items() if k not in ('BC_weights','SH_weights')},sort_keys=True),flush=True)
    out={'schema':'cross-order-n30-single-obstruction-scan-v1','n29_profiles':len(P29),'n30_profiles_tested':len(rec),'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'feasible_indices':[r['n30_index'] for r in rec if r['success']],'infeasible_indices':[r['n30_index'] for r in rec if not r['success']],'floating_point_reconnaissance_only':True,'records':rec,'interpretation':'Each test shares one fixed staircase-weight vector across all 996 n29 profiles and exactly one n30 hard profile.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2,sort_keys=True))
if __name__=='__main__':main()
