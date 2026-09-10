#!/usr/bin/env python3
"""Exactify the successful c={0,2} all-902 three-layer n29,t2 potentials.

Uses the support found by run 34455927836. Floating LP is proposal only;
acceptance delegates to the corrected whole-point scaling/rounding checker and
is then independently replayed by n29_t2_three_layer_verify.py.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('core',HERE/'n29_t2_three_layer_exactify.py');core=module_from_spec(sp);sp.loader.exec_module(core)
rd=core.rd
SUPPORTS={
 '123':{
  'layers':(1,2,3),'diag':{14,16},
  'rect':{(1,0),(1,5),(1,7),(1,11),(1,12),(1,13),(1,14),(1,15),(2,11),(2,12),(2,13),(3,0),(3,1),(3,2),(3,4),(3,6),(3,7),(3,8),(3,9),(3,10)},
  'provenance':{'run_id':34455927836,'artifact_id':10143566744,'artifact_digest':'sha256:044484ef98fcc06651406ae30920e56e9ced782fe72a7e73ca3db8aa5774f1fa'}},
 '234':{
  'layers':(2,3,4),'diag':{14,16},
  'rect':{(2,11),(2,12),(2,13),(2,14),(3,0),(3,2),(3,4),(3,5),(3,7),(3,8),(3,10),(3,12),(4,1),(4,2),(4,3),(4,6),(4,9)},
  'provenance':{'run_id':34455927836,'artifact_id':10143563571,'artifact_digest':'sha256:38ecb3965842126dc5a2afd70d67b98df91e8c1e371f0af9ce3de5a873d298d9'}}
}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--family',choices=sorted(SUPPORTS),required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    cfg=SUPPORTS[z.family];P=core.load_profiles(z.demands_json,z.rows)
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,cfg['layers'],(14,16))
    for D,V,w in rect:
        if (D,V) not in cfg['rect']:M.bounds[w]=(0,0)
    for K,w in diag:
        if K not in cfg['diag']:M.bounds[w]=(0,0)
    res=M.solve()
    out={'schema':'n29-t2-all902-three-layer-c02-exact-v1','family':z.family,'layers':list(cfg['layers']),'profiles':len(P),'rows':len(M.rows),'variables':len(M.names),'rectangle_support':[list(x) for x in sorted(cfg['rect'])],'diagonal_K':sorted(cfg['diag']),'diagonal_c':[2,0],'generator_count':len(cfg['rect'])+len(cfg['diag']),'support_provenance':cfg['provenance'],'floating_solve_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message,'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,'acceptance_rule':'all RHS=0 rows <=0 exactly; all 902 RHS=-1 margin rows <= -scale exactly; all bounds exact'}
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
        out['nonzero_generator_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','J') and chosen[i]!=0}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','attempts')},indent=2,sort_keys=True))
    if chosen is None:raise SystemExit(1)
if __name__=='__main__':main()
