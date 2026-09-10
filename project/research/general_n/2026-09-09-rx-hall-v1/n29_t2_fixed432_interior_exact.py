#!/usr/bin/env python3
"""Exactify the simple n=29,t=2 potential

    F = 4 B(2,0) + 3 B(2,3) + 2 B(2,6).

This is the t=2 instance of the simple pattern first isolated exactly at t=3:
    2t B(t,0) + (t+1) B(t,2t-1) + t B(t,3t).

Floating optimization is proposal only. We request a tiny interior margin and
accept solely by corrected scaled integer arithmetic for the original -1 target.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('core',HERE/'n29_t2_three_layer_exactify.py');core=module_from_spec(sp);sp.loader.exec_module(core)
rd=core.rd
WEIGHTS={(2,0):4,(2,3):3,(2,6):2}
PROPOSAL_MARGINS=(1.0001,1.001,1.005,1.01,1.02,1.05,1.1,1.25,1.5,2.0)
SCALES=(10**4,10**6,10**8,10**10)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,2);P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=902: raise SystemExit(f'expected 902 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(2,),())
    expected=sum(1 for rhs in M.rhs if rhs!=0)
    if expected!=902: raise SystemExit(f'expected 902 strict rows, got {expected}')
    for D,V,w in rect:
        val=WEIGHTS.get((D,V),0);M.bounds[w]=(val,val)
    base_rhs=list(M.rhs);attempts=[];chosen=None;meta=None;used=None
    for margin in PROPOSAL_MARGINS:
        M.rhs=[0 if rhs==0 else -margin for rhs in base_rhs]
        res=M.solve();rec={'proposal_margin':margin,'floating_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message}
        if res.success:
            rec['scale_attempts']=[]
            for scale in SCALES:
                X,m=core.exact_attempt(M,res,scale,1);rec['scale_attempts'].append(m)
                if X is not None: chosen=X;meta=m;used=margin;break
        attempts.append(rec)
        if chosen is not None:break
    M.rhs=base_rhs
    out={'schema':'n29-t2-fixed432-interior-exact-v1','t':2,'profiles':len(P),'rows':len(M.rows),'variables':len(M.names),
         'layers':[2],'rectangle_support':[[2,0],[2,3],[2,6]],'diagonal_K':[],
         'global_potential':'4 B(2,0) + 3 B(2,3) + 2 B(2,6)','fixed_integer_weights':{f'B({D},{V})':v for (D,V),v in sorted(WEIGHTS.items())},
         'integer_weight_sum':sum(WEIGHTS.values()),'pattern_formula':'2t B(t,0)+(t+1)B(t,2t-1)+tB(t,3t)',
         'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,'proof_target':'original normalized strict margin <= -1','attempts':attempts,
         'status':'PASS' if chosen is not None else 'FAIL_EXACT'}
    if chosen is not None:
        out.update(meta);out['proposal_margin_used']=used;out['name_order_sha256']=core.name_hash(M.names);out['integer_numerators']=chosen
        out['nonzero_generator_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','J') and chosen[i]!=0}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','attempts')},indent=2,sort_keys=True))
    if chosen is None:raise SystemExit(1)
if __name__=='__main__':main()
