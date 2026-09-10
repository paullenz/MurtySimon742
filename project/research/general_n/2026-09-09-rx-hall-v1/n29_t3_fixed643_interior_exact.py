#!/usr/bin/env python3
"""Exactify the fixed n=29,t=3 integer potential via an interior proposal.

The fixed global potential is

    F = 6 B(3,0) + 4 B(3,5) + 3 B(3,9).

A prior zero-gap MILP showed this integer potential is floating-feasible for all
94 profiles, but a proposal solved exactly at the -1 normalization boundary is
numerically awkward to round. Here floating LP is proposal-only: we ask for
successively stronger profile margins, then accept only by the corrected
integer arithmetic rule for the ORIGINAL normalized target -1.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('core',HERE/'n29_t2_three_layer_exactify.py');core=module_from_spec(sp);sp.loader.exec_module(core)
rd=core.rd
WEIGHTS={(3,0):6,(3,5):4,(3,9):3}
PROPOSAL_MARGINS=(1.0001,1.001,1.005,1.01,1.02,1.05,1.1,1.25,1.5,2.0)
SCALES=(10**4,10**6,10**8,10**10)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    raw=rd.allx.load29(z.demands_json,z.rows,3)
    P=[{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]
    if len(P)!=94: raise SystemExit(f'expected 94 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(3,),())
    if sum(1 for rhs in M.rhs if rhs!=0)!=94: raise SystemExit('expected 94 strict profile rows')
    for D,V,w in rect: M.bounds[w]=(WEIGHTS.get((D,V),0),WEIGHTS.get((D,V),0))
    base_rhs=list(M.rhs)
    attempts=[]; chosen=None; chosen_meta=None; chosen_margin=None
    for margin in PROPOSAL_MARGINS:
        M.rhs=[0 if rhs==0 else -margin for rhs in base_rhs]
        res=M.solve()
        rec={'proposal_margin':margin,'floating_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message}
        if res.success:
            rec['scale_attempts']=[]
            for scale in SCALES:
                X,meta=core.exact_attempt(M,res,scale,1)
                rec['scale_attempts'].append(meta)
                if X is not None:
                    chosen=X; chosen_meta=meta; chosen_margin=margin; break
        attempts.append(rec)
        if chosen is not None: break
    M.rhs=base_rhs
    out={'schema':'n29-t3-fixed643-interior-exact-v2','t':3,'profiles':len(P),'rows':len(M.rows),'variables':len(M.names),
         'layers':[3],'rectangle_support':[[3,0],[3,5],[3,9]],'diagonal_K':[],
         'global_potential':'6 B(3,0) + 4 B(3,5) + 3 B(3,9)','fixed_integer_weights':{f'B({D},{V})':v for (D,V),v in sorted(WEIGHTS.items())},
         'integer_weight_sum':sum(WEIGHTS.values()),'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,
         'proof_target':'original normalized strict margin <= -1','proposal_margins':list(PROPOSAL_MARGINS),'attempts':attempts,
         'status':'PASS' if chosen is not None else 'FAIL_EXACT'}
    if chosen is not None:
        out.update(chosen_meta); out['proposal_margin_used']=chosen_margin; out['name_order_sha256']=core.name_hash(M.names);out['integer_numerators']=chosen
        out['nonzero_generator_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','J') and chosen[i]!=0}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','attempts')},indent=2,sort_keys=True))
    if chosen is None: raise SystemExit(1)
if __name__=='__main__':main()
