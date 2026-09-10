#!/usr/bin/env python3
"""Exactify the n29,t=3 three-rectangle common potential.

Floating probe 34459663744 greedily reduced the t-parametric language to
B(3,0), B(3,5), B(3,9), with no diagonal steps. Floating solve proposes;
corrected scaled integer arithmetic accepts.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('core',HERE/'n29_t2_three_layer_exactify.py');core=module_from_spec(sp);sp.loader.exec_module(core)
rd=core.rd
RECT={(3,0),(3,5),(3,9)}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,3);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P)!=94:raise SystemExit(f'expected 94 t3 profiles, got {len(P)}')
 M,rect,diag=rd.build(P,12,16,10,(3,),())
 for D,V,w in rect:
  if (D,V) not in RECT:M.bounds[w]=(0,0)
 res=M.solve();out={'schema':'n29-t3-three-rectangle-exact-v1','t':3,'profiles':len(P),'rows':len(M.rows),'variables':len(M.names),'layers':[3],'rectangle_support':[list(x) for x in sorted(RECT)],'diagonal_K':[],'generator_count_allowed':3,'floating_solve_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message,'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,'acceptance_rule':'all RHS=0 rows <=0 exactly; all 94 RHS=-1 margin rows <= -scale exactly; all bounds exact'}
 if not res.success:
  out['status']='FAIL_FLOAT';z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');raise SystemExit(1)
 attempts=[];chosen=None;meta=None
 for boost in (2,3,4,8):
  for scale in (10**6,10**8,10**10):
   X,m=core.exact_attempt(M,res,scale,boost);attempts.append(m)
   if X is not None:chosen=X;meta=m;break
  if chosen is not None:break
 out['attempts']=attempts;out['status']='PASS' if chosen is not None else 'FAIL_EXACT'
 if chosen is not None:
  out.update(meta);out['name_order_sha256']=core.name_hash(M.names);out['integer_numerators']=chosen
  nz={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','J') and chosen[i]!=0};out['nonzero_generator_numerators']=nz;out['nonzero_generator_count']=len(nz)
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','attempts')},indent=2,sort_keys=True))
 if chosen is None:raise SystemExit(1)
if __name__=='__main__':main()
