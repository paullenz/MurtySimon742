#!/usr/bin/env python3
"""Floating extremal compression test for n29,t3 fixed potential 6,4,3.

Can profiles 1..93 share one scalar template, leaving profile 0 as the only
exception?  Since profile 0 is already pairwise incompatible with profiles 5
and 30 under this fixed F, success would give the smallest possible scalar
partition size (two) for this potential. Discovery only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
W={(3,0):6,(3,5):4,(3,9):3}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,3);P0=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P0)!=94:raise SystemExit(f'expected94 got {len(P0)}')
 P=P0[1:];M,rect,diag=rd.build(P,12,16,10,(3,),())
 for D,V,w in rect:
  val=W.get((D,V),0);M.bounds[w]=(val,val)
 keys=[('lambda',),('c',),('mu+',),('mu-',)]+[('tau',j) for j in range(1,13)]
 for pi in range(1,len(P)):
  for key in keys:
   if key[0]=='tau':n0=('tau',0,key[1]);ni=('tau',pi,key[1])
   else:n0=(key[0],0);ni=(key[0],pi)
   a=M.idx[n0];b=M.idx[ni];M.le({b:1,a:-1},0);M.le({a:1,b:-1},0)
 st=time.time();res=M.solve();out={'schema':'n29-t3-fixed643-except0-common-scan-v1','included_original_indices':list(range(1,94)),'profile_count':93,'success':bool(res.success),'status':int(res.status),'message':res.message,'seconds':time.time()-st,'rows':len(M.rows),'variables':len(M.names),'floating_point_reconnaissance_only':True}
 if res.success:
  vals={}
  for key in keys:
   name=('tau',0,key[1]) if key[0]=='tau' else (key[0],0);v=float(res.x[M.idx[name]])
   if abs(v)>1e-9:vals['tau'+str(key[1]) if key[0]=='tau' else key[0]]=v
  out['theta_nonzero']=vals
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
