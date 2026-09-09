#!/usr/bin/env python3
"""Test the exact n29 16-shape dictionary on the seven n30 hard profiles with fresh weights.

Unlike the all-1003 cross-order test, this does NOT require n29 and n30 to use
the same numerical staircase weights.  It asks only whether the same 9 BC + 7 SH
shape family supports one common n30 weight vector across the seven n30 t=1 hard
profiles.  Success would show that the all-1003 failure is a weight-universality
failure, not a shape-family failure. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('co',HERE/'cross_order_common_potential.py');co=module_from_spec(sp);sp.loader.exec_module(co)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n30-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    N=json.loads(z.n30_json.read_text());J=json.loads(z.support_json.read_text())
    bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    P=[{'order':'n30t1','id':i,'s':r['s'],'rho':r['rho'],'a':13,'b':16,'dmax':11} for i,r in enumerate(N['records'])]
    st=time.time();M=co.build(P,bc,sh);res=M.solve()
    out={'schema':'n30-reweight-n29-fixed16-v1','profiles':len(P),'BC_count':len(bc),'SH_count':len(sh),'support_count':len(bc)+len(sh),'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True,'interpretation':'The n29 16 staircase shapes are fixed, but n30 receives a fresh single common staircase-weight vector; scalar bookkeeping remains profile-specific.'}
    if res.success:
        out['BC_weights']=[float(res.x[M.idx[('BC',i)]]) for i in range(len(bc))]
        out['SH_weights']=[float(res.x[M.idx[('SH',i)]]) for i in range(len(sh))]
        out['active_BC']=[i for i in range(len(bc)) if res.x[M.idx[('BC',i)]]>1e-8]
        out['active_SH']=[i for i in range(len(sh)) if res.x[M.idx[('SH',i)]]>1e-8]
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_weights','SH_weights')},indent=2,sort_keys=True))
if __name__=='__main__':main()
