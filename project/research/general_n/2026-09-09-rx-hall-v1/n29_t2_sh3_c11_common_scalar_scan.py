#!/usr/bin/env python3
"""Floating falsification test: can all 902 n=29,t=2 profiles share one scalar
bookkeeping template under the exact 11-term 3-D potential?

Global potential fixed to:
  3 B(3,6..9) + 4 B(3,10..13) + 8 J2 + 7 J0 + 29 SH3.
Only lambda,c,mu+/mu-,tau_1..tau_12 are tied across profiles. Envelope
variables remain profile-local. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('lat',HERE/'n29_t2_bad107_sh3_subset_lattice.py');lat=module_from_spec(sp);sp.loader.exec_module(lat)
rd=lat.rd
RECT={(3,6):3,(3,7):3,(3,8):3,(3,9):3,(3,10):4,(3,11):4,(3,12):4,(3,13):4}
DIAG={14:8,16:7};SH=29

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
 M,rect,diag,sh,layers,steps=lat.build(P,{'J0','J2'})
 for D,V,w in rect:M.bounds[w]=(RECT.get((D,V),0),RECT.get((D,V),0))
 for K,w in diag:M.bounds[w]=(DIAG.get(K,0),DIAG.get(K,0))
 M.bounds[sh]=(SH,SH)
 scalar_keys=[('lambda',),('c',),('mu+',),('mu-',)]+[('tau',j) for j in range(1,13)]
 for pi in range(1,len(P)):
  for key in scalar_keys:
   if key[0]=='tau':n0=('tau',0,key[1]);ni=('tau',pi,key[1])
   else:n0=(key[0],0);ni=(key[0],pi)
   a=M.idx[n0];b=M.idx[ni];M.le({b:1,a:-1},0);M.le({a:1,b:-1},0)
 st=time.time();res=M.solve();out={'schema':'n29-t2-sh3-c11-common-scalar-scan-v1','profiles':len(P),'global_potential':'3 B(3,6..9)+4 B(3,10..13)+8 J2+7 J0+29 SH3','success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
 if res.success:
  vals={}
  for key in scalar_keys:
   name=('tau',0,key[1]) if key[0]=='tau' else (key[0],0);vals['tau'+str(key[1]) if key[0]=='tau' else key[0]]=float(res.x[M.idx[name]])
  out['common_scalar_values']=vals
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
