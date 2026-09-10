#!/usr/bin/env python3
"""Ablate profile-specific dual/resource families under the exact support14 geometry.

Baseline global support: 12 BC rectangles on D={2,3,4} plus J2,J0.
The exact support14 certificate already uses mu-=0, tau1=0 and tau8..tau12=0;
those are fixed to zero in every test. One remaining family is then removed.
Floating structural reconnaissance only; positive reductions require exact replay.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
RECT={(2,11),(2,12),(2,13),(2,14),(3,0),(3,4),(3,7),(3,8),(3,10),(4,3),(4,6),(4,9)}
CASES=['lambda','c','mu+','tau2','tau3','tau4','tau5','tau6','tau7','alltau']

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--drop',choices=CASES,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=base.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw];M,rect,diag=base.build(P,layers=(2,3,4),steps=(14,16))
 for D,V,w in rect:
  if (D,V) not in RECT:M.bounds[w]=(0,0)
 # Remove multiplier families already identically zero in the accepted exact support14 point.
 for i,n in enumerate(M.names):
  if isinstance(n,tuple):
   if n[0]=='mu-':M.bounds[i]=(0,0)
   if n[0]=='tau' and (n[2]==1 or n[2]>=8):M.bounds[i]=(0,0)
 # Drop one remaining family.
 for i,n in enumerate(M.names):
  if not isinstance(n,tuple):continue
  kill=False
  if z.drop in ('lambda','c','mu+') and n[0]==z.drop:kill=True
  elif z.drop.startswith('tau') and z.drop!='alltau' and n[0]=='tau' and n[2]==int(z.drop[3:]):kill=True
  elif z.drop=='alltau' and n[0]=='tau':kill=True
  if kill:M.bounds[i]=(0,0)
 st=time.time();res=M.solve();out={'schema':'n29-t2-support14-dual-family-ablation-v1','profiles':len(P),'global_generators':14,'baseline_zero_families':['mu-','tau1','tau8..tau12'],'drop':z.drop,'success':bool(res.success),'status':int(res.status),'message':res.message,'objective':float(res.fun) if res.success else None,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st,'floating_point_reconnaissance_only':True}
 if res.success:
  ar,ad=base.extract(res,rect,diag);out['active_global_generator_count']=len(ar)+len(ad)
  used={}
  for fam in ['lambda','c','mu+','mu-']:
   used[fam]=sum(1 for i,n in enumerate(M.names) if isinstance(n,tuple) and n[0]==fam and res.x[i]>1e-8)
  for j in range(1,13):used[f'tau{j}']=sum(1 for i,n in enumerate(M.names) if isinstance(n,tuple) and n[0]=='tau' and n[2]==j and res.x[i]>1e-8)
  out['active_profile_multiplier_counts']=used
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
