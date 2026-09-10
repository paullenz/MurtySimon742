#!/usr/bin/env python3
"""Exactification attempt for a simple hand-rounded 11-term n=29,t=2 3-D potential.

Potential:
  D3 V=6,7,8,9 weights 3,3,3,3
  D3 V=10,11,12,13 weights 4,4,4,4
  J2 (K=14) weight 8
  J0 (K=16) weight 7
  SH3 weight 29

The vector is suggested by the full-902 floating optimum, but acceptance is by
corrected exact integer arithmetic only. Floating LP is proposal machinery for
profile-local scalar/envelope variables. An interior proposal is requested to
make rational rounding robust; the checked proof target remains margin <= -1.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json,hashlib
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('lat',HERE/'n29_t2_bad107_sh3_subset_lattice.py');lat=module_from_spec(sp);sp.loader.exec_module(lat)
sp2=spec_from_file_location('core',HERE/'n29_t2_three_layer_exactify.py');core=module_from_spec(sp2);sp2.loader.exec_module(core)
rd=lat.rd
RECT={(3,6):3,(3,7):3,(3,8):3,(3,9):3,(3,10):4,(3,11):4,(3,12):4,(3,13):4}
DIAG={14:8,16:7};SH=29
PROPOSAL_MARGINS=(1.0001,1.001,1.005,1.01,1.02,1.05,1.1,1.25)
SCALES=(10**4,10**6,10**8)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
 if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
 M,rect,diag,sh,layers,steps=lat.build(P,{'J0','J2'})
 for D,V,w in rect:M.bounds[w]=(RECT.get((D,V),0),RECT.get((D,V),0))
 for K,w in diag:M.bounds[w]=(DIAG.get(K,0),DIAG.get(K,0))
 M.bounds[sh]=(SH,SH)
 base_rhs=list(M.rhs);chosen=None;meta=None;pm=None;attempts=[]
 for margin in PROPOSAL_MARGINS:
  M.rhs=[0 if rhs==0 else -margin for rhs in base_rhs];res=M.solve();rec={'proposal_margin':margin,'floating_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message}
  if res.success:
   rec['scale_attempts']=[]
   for scale in SCALES:
    X,m=core.exact_attempt(M,res,scale,1);rec['scale_attempts'].append(m)
    if X is not None:chosen=X;meta=m;pm=margin;break
  attempts.append(rec)
  if chosen is not None:break
 M.rhs=base_rhs
 fixed={f'B({D},{V})':v for (D,V),v in sorted(RECT.items())};fixed.update({f'J({16-K})':v for K,v in sorted(DIAG.items())});fixed['SH3']=SH
 out={'schema':'n29-t2-sh3-c11-fixed-simple-exact-v1','status':'PASS' if chosen is not None else 'FAIL_EXACT','t':2,'profiles':len(P),'rows':len(M.rows),'variables':len(M.names),'layers':list(layers),'rectangle_support':[list(x) for x in sorted(RECT)],'diagonal_K':sorted(DIAG),'SH_threshold':3,'fixed_integer_weights':fixed,'integer_weight_sum':sum(fixed.values()),'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,'proof_target':'original normalized strict margin <= -1','proposal_margins':list(PROPOSAL_MARGINS),'attempts':attempts}
 if chosen is not None:
  out.update(meta);out['proposal_margin_used']=pm;out['name_order_sha256']=core.name_hash(M.names);out['integer_numerators']=chosen
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('attempts','integer_numerators')},indent=2,sort_keys=True))
 if chosen is None:raise SystemExit(1)
if __name__=='__main__':main()
