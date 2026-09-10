#!/usr/bin/env python3
"""Exact arithmetic acceptance for the fixed n=29,t=3 potential

    F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9).

The global coefficients are fixed constants.  Floating LP is used only to
propose the profile-specific scalar/envelope variables; acceptance is exact
integer arithmetic under the corrected scaled RHS rule.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('core',HERE/'n29_t2_three_layer_exactify.py');core=module_from_spec(sp);sp.loader.exec_module(core)
rd=core.rd
WEIGHTS={(3,0):6,(3,5):4,(3,9):3}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,3);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=94: raise SystemExit(f'expected 94 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(3,),())
    if sum(1 for rhs in M.rhs if rhs!=0)!=94: raise SystemExit('expected 94 strict margin rows')
    for D,V,w in rect:
        val=WEIGHTS.get((D,V),0);M.bounds[w]=(val,val)
    res=M.solve()
    out={'schema':'n29-t3-fixed-integer-643-exact-v1','t':3,'profiles':len(P),'rows':len(M.rows),'variables':len(M.names),'global_potential':'6 B(3,0) + 4 B(3,5) + 3 B(3,9)','fixed_integer_weights':{f'B({D},{V})':v for (D,V),v in sorted(WEIGHTS.items())},'integer_weight_sum':sum(WEIGHTS.values()),'floating_solve_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message,'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,'acceptance_rule':'all RHS=0 rows <=0 exactly; all 94 RHS=-1 rows <= -scale exactly; all fixed generator bounds exact','coefficient_discovery_run':34484528809,'coefficient_discovery_status':'zero-gap MILP optimum within this three-rectangle integer family'}
    if not res.success:
        out['status']='FAIL_FLOAT';z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');raise SystemExit(1)
    attempts=[];chosen=None;meta=None
    for scale in (10**4,10**6,10**8,10**10):
        X,m=core.exact_attempt(M,res,scale,1);attempts.append(m)
        if X is not None:chosen=X;meta=m;break
    out['attempts']=attempts;out['status']='PASS' if chosen is not None else 'FAIL_EXACT'
    if chosen is not None:
        out.update(meta);out['name_order_sha256']=core.name_hash(M.names);out['integer_numerators']=chosen
        out['nonzero_generator_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','J') and chosen[i]!=0}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','attempts')},indent=2,sort_keys=True))
    if chosen is None: raise SystemExit(1)
if __name__=='__main__':main()
