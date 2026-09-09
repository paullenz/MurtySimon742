#!/usr/bin/env python3
"""Test one fixed 16-shape staircase potential across 1003 n29+n30 hard profiles.

Profiles:
  * 902 n29 t=2 hard profiles, (a,b,dmax)=(12,16,10)
  * 94 n29 t=3 hard profiles, same order
  * 7 n30 t=1 hard profiles, (13,16,11)
The BC/SH shape support is exactly the exactified n29 16-shape support. One
staircase-weight vector is shared across all 1003 profiles; scalar dual
multipliers and envelope variables remain profile-specific. Floating
reconnaissance only; success must be exactified separately.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('co',HERE/'cross_order_common_potential.py');co=module_from_spec(sp);sp.loader.exec_module(co)

def load29(dp,rp,t):
    D=json.loads(Path(dp).read_text());out=[]
    for line in Path(rp).read_text().splitlines():
        if not line.strip():continue
        z=list(map(int,line.split()));did,rho=z[0],z[2:];s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t:out.append({'order':f'n29t{t}','id':did,'s':s,'rho':rho,'a':12,'b':16,'dmax':10})
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--t2-demands',type=Path,required=True);ap.add_argument('--t2-rows',type=Path,required=True);ap.add_argument('--t3-demands',type=Path,required=True);ap.add_argument('--t3-rows',type=Path,required=True);ap.add_argument('--n30-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();J=json.loads(z.support_json.read_text());bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    P=load29(z.t2_demands,z.t2_rows,2)+load29(z.t3_demands,z.t3_rows,3);N30=json.loads(z.n30_json.read_text())
    for i,r in enumerate(N30['records']):P.append({'order':'n30t1','id':i,'s':r['s'],'rho':r['rho'],'a':13,'b':16,'dmax':11})
    start=time.time();M=co.build(P,bc,sh);res=M.solve();counts={k:sum(p['order']==k for p in P) for k in ('n29t2','n29t3','n30t1')}
    out={'schema':'cross-order-all1003-fixed16-v1','profiles':len(P),'profile_counts':counts,'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-start,'floating_point_reconnaissance_only':True,'interpretation':'Success means one fixed 16-shape F+G staircase-weight vector works across all 996 n29 and seven n30 hard profiles; scalar bookkeeping remains profile-specific.'}
    if res.success:
        out['BC_weights']=[float(res.x[M.idx[('BC',i)]]) for i in range(len(bc))];out['SH_weights']=[float(res.x[M.idx[('SH',i)]]) for i in range(len(sh))];out['active_BC']=sum(w>1e-8 for w in out['BC_weights']);out['active_SH']=sum(w>1e-8 for w in out['SH_weights'])
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_weights','SH_weights')},indent=2,sort_keys=True))
    if not res.success:raise SystemExit(2)
if __name__=='__main__':main()
