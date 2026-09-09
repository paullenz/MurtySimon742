#!/usr/bin/env python3
"""Exactify selected pure-BC common potentials for all 94 n29 t=3 hard profiles.

The canonical 75-shape BC dictionary is fixed. Candidate supports come from the
zero-SH minimum-SH scan (M=200, M=1000, or their union). Floating LP is proposal
only. Acceptance scales to rational integer numerators, repairs free ell/sig
envelopes downward, and checks every row and bound with Python integer arithmetic.
Profile margin rhs -1 is checked against -scale.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)
sp2=spec_from_file_location('ex',HERE/'n29_all_t23_exactify.py');ex=module_from_spec(sp2);sp2.loader.exec_module(ex)

def tup(g):return tuple(tuple(p) for p in g)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--demands',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True)
    ap.add_argument('--dictionary-json',type=Path,required=True);ap.add_argument('--min-sh-json',type=Path,required=True)
    ap.add_argument('--candidate',choices=['M200','M1000','union'],required=True)
    ap.add_argument('--a',type=int,default=12);ap.add_argument('--b',type=int,default=16);ap.add_argument('--dmax',type=int,default=10)
    ap.add_argument('--boost',type=int,default=2);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=ex.load(z.demands,z.rows,3);D=json.loads(z.dictionary_json.read_text());S=json.loads(z.min_sh_json.read_text())
    i200=list(S['M200']['active_BC_indices']);i1000=list(S['M1000_validation']['active_BC_indices'])
    if z.candidate=='M200':idx=sorted(i200)
    elif z.candidate=='M1000':idx=sorted(i1000)
    else:idx=sorted(set(i200)|set(i1000))
    allbc=[tup(x['generators']) for x in D['BC']];bc=[allbc[i] for i in idx];sh=[]
    M=cp.build(P,bc,sh,z.a,z.b,z.dmax);res=M.solve()
    if not res.success:
        out={'schema':'n29-t3-pure-bc-exact-v1','candidate':z.candidate,'status':'NUMERIC_INFEASIBLE','profiles':len(P),'BC_indices':idx,'BC_count':len(bc),'SH_count':0,'rows':len(M.rows),'variables':len(M.names),'floating_point_proposal_only':True}
        z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(2)
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10):
        X,m=ex.exact_attempt(M,res,scale,z.boost,len(P));attempts.append(m)
        if X is not None:chosen=X;meta=m;break
    passed=chosen is not None
    out={'schema':'n29-t3-pure-bc-exact-v1','candidate':z.candidate,'status':'PASS' if passed else 'FAIL','profiles':len(P),'BC_indices':idx,'BC_count':len(bc),'SH_count':0,'support_count':len(bc),'rows':len(M.rows),'variables':len(M.names),'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'correct_scaled_rhs_rule':True,'attempts':attempts,'interpretation':'PASS gives an exact rational pure-BC common staircase potential across all 94 regenerated n29 t=3 hard profiles. No SH correction is used. Finite evidence conditional on the RX-Hall bridge/frontier preparation.'}
    if passed:
        out.update(meta);out['BC_shapes']=[[list(p) for p in g] for g in bc];out['integer_BC_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0]=='BC'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','integer_BC_numerators','attempts')},indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
