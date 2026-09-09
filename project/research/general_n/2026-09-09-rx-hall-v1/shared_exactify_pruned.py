#!/usr/bin/env python3
"""Exactify a pruned shared staircase-potential solution by integer scaling.

Rebuilds the exact integer-coefficient shared envelope LP for the support stored
in a greedy-prune JSON, scales and rounds a floating feasible point, then repairs
only the free per-profile envelope variables ell/sig downward by the exact
amount needed to restore every homogeneous envelope row. Final acceptance uses
Python integer arithmetic only. Floating-point values are proposal only.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('shared_greedy_prune',HERE/'shared_greedy_prune.py');gp=module_from_spec(spec);spec.loader.exec_module(gp)

def eval_rows(M,X):
    vals=[]
    for row,rhs in zip(M.rows,M.rhs):
        vals.append(sum(int(c)*X[j] for j,c in row.items()))
    return vals

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

    pre=eval_rows(M,X)
    # Each structural envelope row has rhs 0 and one free ell/sig variable with
    # coefficient +1. For any positive residual, lowering that variable fixes the
    # row and cannot hurt any other structural row containing the same envelope.
    repair={}
    for i,(row,rhs,lhs) in enumerate(zip(M.rows,M.rhs,pre)):
        if rhs!=0 or lhs<=0:continue
        candidates=[]
        for j,c in row.items():
            nm=M.names[j]
            if c==1 and isinstance(nm,tuple) and nm and nm[0] in ('ell','sig'):
                candidates.append(j)
        if len(candidates)!=1:
            raise SystemExit(f'cannot identify unique envelope var in violated row {i}: lhs={lhs}, candidates={candidates}')
        j=candidates[0];repair[j]=max(repair.get(j,0),lhs)
    for j,amt in repair.items():X[j]-=amt

    post=eval_rows(M,X)
    bound_viol=[]
    for i,(lo,hi) in enumerate(M.bounds):
        x=X[i]
        if lo is not None and lo!=-float('inf') and x < int(round(z.scale*lo)):bound_viol.append((i,'lo',x,lo))
        if hi is not None and hi!=float('inf') and x > int(round(z.scale*hi)):bound_viol.append((i,'hi',x,hi))
    row_viol=[];margin_vals=[];zero_max=None
    for i,(lhs,rhs) in enumerate(zip(post,M.rhs)):
        if lhs>rhs:row_viol.append((i,lhs,rhs))
        if rhs==-1:margin_vals.append(lhs)
        else:zero_max=lhs if zero_max is None else max(zero_max,lhs)
    passed=(not bound_viol and not row_viol and margin_vals and max(margin_vals)<=-1)
    repairs=[{'var_index':j,'name':str(M.names[j]),'amount':amt} for j,amt in sorted(repair.items())]
    out={'schema':'n30-shared-pruned-exact-integer-v2','status':'PASS' if passed else 'FAIL','scale':z.scale,'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'variables':len(M.names),'rows':len(M.rows),'pre_repair_positive_zero_rows':sum(rhs==0 and lhs>0 for lhs,rhs in zip(pre,M.rhs)),'repair_variable_count':len(repair),'repair_total':sum(repair.values()),'repair_max':max(repair.values()) if repair else 0,'repairs':repairs,'bound_violations':bound_viol[:20],'row_violations':row_viol[:20],'zero_rhs_max_lhs':zero_max,'profile_margin_lhs':margin_vals,'worst_margin_lhs':max(margin_vals) if margin_vals else None,'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'interpretation':'PASS gives an exact integer feasible point for the shared staircase envelope LP after scaling, rounding, and deterministic downward repair of free envelope variables. It is finite n30 evidence, not a universal theorem.'}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='repairs'},indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
