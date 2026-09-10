#!/usr/bin/env python3
"""Floating falsification test: can all 94 n=29,t=3 profiles share one scalar
template when the global potential is fixed to

    F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9)?

Only lambda,c,mu+/mu-,tau_1..tau_12 are tied across profiles.  Envelope
variables ell/sig remain profile-local.  Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
WEIGHTS={(3,0):6,(3,5):4,(3,9):3}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,3);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=94: raise SystemExit(f'expected 94 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(3,),())
    for D,V,w in rect:
        val=WEIGHTS.get((D,V),0);M.bounds[w]=(val,val)
    scalar_keys=[('lambda',),('c',),('mu+',),('mu-',)]+[('tau',j) for j in range(1,13)]
    for pi in range(1,len(P)):
        for key in scalar_keys:
            if key[0]=='tau': n0=('tau',0,key[1]);ni=('tau',pi,key[1])
            else: n0=(key[0],0);ni=(key[0],pi)
            a=M.idx[n0];b=M.idx[ni]
            M.le({b:1,a:-1},0);M.le({a:1,b:-1},0)
    st=time.time();res=M.solve()
    out={'schema':'n29-t3-fixed643-common-scalar-scan-v1','profiles':len(P),'global_potential':'6 B(3,0) + 4 B(3,5) + 3 B(3,9)','success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
    if res.success:
        vals={}
        for key in scalar_keys:
            name=('tau',0,key[1]) if key[0]=='tau' else (key[0],0)
            vals['tau'+str(key[1]) if key[0]=='tau' else key[0]]=float(res.x[M.idx[name]])
        out['common_scalar_values']=vals
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
