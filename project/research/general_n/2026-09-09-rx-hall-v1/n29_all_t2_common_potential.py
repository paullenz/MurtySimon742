#!/usr/bin/env python3
"""Test one common 16-shape staircase potential across all n29 t=2 hard profiles.

The 16-shape support was exactified for the 38 profiles surviving the specialised
n30 dictionary. Here we keep exactly those BC/SH shapes and require one common
nonnegative staircase-weight vector across all 902 independently regenerated
n29 t=2 RX-Hall hard profiles. Profile-specific lambda,c,mu,tau_h and envelope
variables remain free, matching the established symbolic separation between the
combinatorial potential and scalar dual bookkeeping. Floating reconnaissance
only; success must be exactified separately.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text());out=[]
    for line in Path(rp).read_text().splitlines():
        if not line.strip():continue
        z=list(map(int,line.split()));did,total,rho=z[0],z[1],z[2:];s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t:out.append({'s':s,'rho':rho,'demand_id':did})
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--t',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();J=json.loads(z.support_json.read_text());P=load(z.demands_json,z.rows,z.t)
    bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    start=time.time();M=cp.build(P,bc,sh,z.a,z.b,z.dmax);res=M.solve()
    out={'schema':'n29-all-t2-common-16-shape-v1','scope':{'a':z.a,'b':z.b,'dmax':z.dmax,'t':z.t},'profiles':len(P),'BC_count':len(bc),'SH_count':len(sh),'support_count':len(bc)+len(sh),'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-start,'floating_point_reconnaissance_only':True,'interpretation':'Success means one staircase-weight vector works across all n29 t=2 hard profiles, with profile-specific scalar multipliers/envelopes. It is not proof evidence until exactified.'}
    if res.success:
        out['objective']=float(res.fun);out['BC_weights']=[float(res.x[M.idx[('BC',i)]]) for i in range(len(bc))];out['SH_weights']=[float(res.x[M.idx[('SH',i)]]) for i in range(len(sh))];out['active_BC']=sum(w>1e-8 for w in out['BC_weights']);out['active_SH']=sum(w>1e-8 for w in out['SH_weights'])
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_weights','SH_weights')},indent=2,sort_keys=True))
    if not res.success:raise SystemExit(2)
if __name__=='__main__':main()
