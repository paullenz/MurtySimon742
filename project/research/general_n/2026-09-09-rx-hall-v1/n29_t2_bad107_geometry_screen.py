#!/usr/bin/env python3
"""Fast geometry-family screen on the 107 profiles that defeat fixed F=4,3,2.

Any case infeasible here is certainly impossible on the full 902-profile set.
A feasible case is only promoted to a candidate and must then be tested on all
902 profiles.  Global potential weights are free and common within each case;
scalar/envelope variables remain profile-local. Floating reconnaissance only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,time
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
BAD=[0,1,2,3,4,5,6,7,8,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,38,39,40,77,78,79,82,84,87,91,92,93,94,107,112,113,121,126,127,128,129,134,135,136,145,173,178,180,181,192,193,194,195,196,197,208,209,210,211,212,231,232,256,257,258,259,260,368,381,382,385,403,404,410,411,412,415,435,436,437,438,439,440,441,442,483,498,499,501,502,503,505,566,567,570,681,683]
CASES=[
 ('D2', (2,), ()),
 ('D2_J0',(2,),(16,)),
 ('D2_J2',(2,),(14,)),
 ('D2_J02',(2,),(14,16)),
 ('D2_D3',(2,3),()),
 ('D2_D4',(2,4),()),
 ('D2_D3_J02',(2,3),(14,16)),
 ('D2_D4_J02',(2,4),(14,16)),
 ('D2_D3_D4',(2,3,4),()),
 ('D2_D3_D4_J02',(2,3,4),(14,16)),
]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P0=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P0)!=902:raise SystemExit(f'expected902 got {len(P0)}')
 P=[P0[i] for i in BAD];results=[]
 for name,layers,steps in CASES:
  st=time.time();M,rect,diag=rd.build(P,12,16,10,layers,steps);res=M.solve();r={'case':name,'layers':list(layers),'diagonal_K':list(steps),'success':bool(res.success),'status':int(res.status),'message':res.message,'rows':len(M.rows),'variables':len(M.names),'seconds':time.time()-st}
  if res.success:
   ar=[{'D':D,'V':V,'weight':float(res.x[w])} for D,V,w in rect if res.x[w]>1e-8];ad=[{'K':K,'c':16-K,'weight':float(res.x[w])} for K,w in diag if res.x[w]>1e-8];r.update(active_rectangles=ar,active_diagonals=ad,active_generator_count=len(ar)+len(ad),objective=float(res.fun))
  results.append(r);print(json.dumps(r,sort_keys=True),flush=True)
 out={'schema':'n29-t2-bad107-geometry-screen-v1','bad_profile_count':107,'bad_indices':BAD,'floating_point_reconnaissance_only':True,'results':results,'interpretation':'Infeasible cases are ruled out already on the 107 fixed-432 obstruction profiles. Feasible cases require full 902-profile testing and exactification before proof use.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
