#!/usr/bin/env python3
"""Promote the three bad107-minimal SH3 family combinations to all 902 t=2 profiles.

Bad107 lattice run 34501499674 found exactly three inclusion-minimal feasible
families within D3+SH3+subset{D2,D4,J0,J2}:

 A = D2 + D3 + J0 + SH3
 B = D2 + D3 + J2 + SH3
 C = D3 + J0 + J2 + SH3

(D4 is absent from all three.)  This script tests each on the complete 902-profile
n=29,t=2 RX-Hall frontier. Floating reconnaissance only. Any survivor must be
support-pruned / exactified before proof use.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('lat',HERE/'n29_t2_bad107_sh3_subset_lattice.py');lat=module_from_spec(sp);sp.loader.exec_module(lat)
rd=lat.rd
CASES=[
 ('A_D2_D3_J0_SH3',{'D2','J0'}),
 ('B_D2_D3_J2_SH3',{'D2','J2'}),
 ('C_D3_J0_J2_SH3',{'J0','J2'}),
]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P)!=902:raise SystemExit(f'expected 902 got {len(P)}')
 results=[]
 for name,opt in CASES:
  st=time.time();M,rect,diag,sh,layers,steps=lat.build(P,opt);res=M.solve();rec={'case':name,'optional_families':sorted(opt),'families':['D3','SH3']+sorted(opt),'layers':list(layers),'diagonal_K':list(steps),'SH_threshold':3,'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':float(time.time()-st)}
  if res.success:
   rec['objective']=float(res.fun);rec['SH3_weight']=float(res.x[sh]);rec['active_rectangles']=[{'D':D,'V':V,'weight':float(res.x[w])} for D,V,w in rect if res.x[w]>1e-8];rec['active_diagonals']=[{'K':K,'c':16-K,'weight':float(res.x[w])} for K,w in diag if res.x[w]>1e-8];rec['active_generator_count']=int(len(rec['active_rectangles'])+len(rec['active_diagonals'])+(1 if res.x[sh]>1e-8 else 0))
  results.append(rec);print(json.dumps(rec,sort_keys=True),flush=True)
 out={'schema':'n29-t2-SH3-minimal-families-full902-v1','profiles':902,'bad107_lattice_run':34501499674,'floating_point_reconnaissance_only':True,'results':results,'survivors':[r['case'] for r in results if r['success']],'interpretation':'These are exactly the three inclusion-minimal family survivors from the bad107 D3+SH3 lattice. A full902 success is still floating discovery only; exactification and independent replay are required before replacing the trusted 16-generator certificate.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
