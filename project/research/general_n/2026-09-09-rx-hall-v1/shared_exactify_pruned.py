#!/usr/bin/env python3
"""Exactify a pruned shared staircase-potential solution by integer scaling.

Rebuilds the exact integer-coefficient shared envelope LP for the support stored
in a greedy-prune JSON, reads the floating solution variables emitted by that
run, scales all variables by an integer K and rounds to integers, then checks
every row and every bound with Python integer arithmetic. Because all structural
rows are homogeneous (rhs 0) and each profile margin row has rhs -1, a robust
scaled solution can survive rounding and become an exact rational/integer
feasible point. Floating values are proposal only; PASS requires exact checks.
"""
from collections import Counter
from pathlib import Path
import argparse,json,ast
import shared_greedy_prune as gp

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bc-json',type=Path,required=True);ap.add_argument('--pruned-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--scale',type=int,default=1000000);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.bc_json.read_text());J=json.loads(z.pruned_json.read_text());assert J['success'] and J.get('variables')
    P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['records']]
    bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    M=gp.build(P,bc,sh,z.a,z.b,z.dmax)
    vals=J['variables'];X=[];missing=[]
    for name in M.names:
        key=str(name)
        if key not in vals:missing.append(key);X.append(0)
        else:X.append(int(round(z.scale*float(vals[key]))))
    if missing:raise SystemExit(f'missing {len(missing)} variables, first={missing[:3]}')
    bound_viol=[]
    for i,(lo,hi) in enumerate(M.bounds):
        x=X[i]
        if lo is not None and lo!=-float('inf') and x < int(round(z.scale*lo)):bound_viol.append((i,'lo',x,lo))
        if hi is not None and hi!=float('inf') and x > int(round(z.scale*hi)):bound_viol.append((i,'hi',x,hi))
    row_vals=[];row_viol=[];margin_vals=[];zero_max=None
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items())
        ok=lhs<=rhs
        if not ok:row_viol.append((i,lhs,rhs))
        row_vals.append(lhs)
        if rhs==-1:margin_vals.append(lhs)
        else:zero_max=lhs if zero_max is None else max(zero_max,lhs)
    # nonnegative potential/global coefficients are exactly nonnegative by bounds.
    passed=(not bound_viol and not row_viol and margin_vals and max(margin_vals)<=-1)
    out={'schema':'n30-shared-pruned-exact-integer-v1','status':'PASS' if passed else 'FAIL','scale':z.scale,'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'variables':len(M.names),'rows':len(M.rows),'bound_violations':bound_viol[:20],'row_violations':row_viol[:20],'zero_rhs_max_lhs':zero_max,'profile_margin_lhs':margin_vals,'worst_margin_lhs':max(margin_vals) if margin_vals else None,'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'interpretation':'PASS gives an exact integer feasible point for the shared staircase envelope LP after scaling/rounding the floating proposal. It is finite n30 evidence, not a universal theorem.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
