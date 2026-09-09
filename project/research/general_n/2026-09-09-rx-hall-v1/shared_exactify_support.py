#!/usr/bin/env python3
"""Exactify a selected shared staircase support with correct rational scaling.

Input support JSON supplies active_BC/active_SH generator shapes. Rebuild the
shared continuous envelope LP, use its floating solution only as a proposal,
form integer numerators with explicit denominator `scale`, apply a safety boost,
repair only homogeneous ell/sig rounding residuals, and verify every row/bound
with Python integer arithmetic.

For rational point X/scale, a continuous RHS -1 becomes integer RHS -scale.
This corrected rule supersedes the earlier faulty exactifier that compared the
scaled numerator to -1.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('gp',HERE/'shared_greedy_prune.py');gp=module_from_spec(sp);sp.loader.exec_module(gp)

def eval_rows(M,X):return [sum(int(c)*X[j] for j,c in row.items()) for row in M.rows]
def scaled_rhs(rhs,scale):
    if rhs==0:return 0
    if rhs==-1:return -scale
    raise RuntimeError(('unexpected rhs',rhs))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--bc-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--scale',type=int,default=1000000);ap.add_argument('--boost',type=int,default=2);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 B=json.loads(z.bc_json.read_text());J=json.loads(z.support_json.read_text());assert J.get('active_BC') is not None and J.get('active_SH') is not None
 P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['records']]
 bc=[tuple(tuple(p) for p in x['generators']) for x in J['active_BC']];sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
 M,res=gp.solve(P,bc,sh,z.a,z.b,z.dmax)
 if not res.success:raise SystemExit('selected support continuous LP infeasible')
 X=[int(round(z.scale*z.boost*float(x))) for x in res.x];pre=eval_rows(M,X);repair={}
 for i,(row,rhs,lhs) in enumerate(zip(M.rows,M.rhs,pre)):
  if rhs!=0 or lhs<=0:continue
  cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j] and M.names[j][0] in ('ell','sig')]
  if len(cand)!=1:raise SystemExit(f'row {i} cannot be repaired uniquely: lhs={lhs}, cand={cand}')
  j=cand[0];repair[j]=max(repair.get(j,0),lhs)
 for j,v in repair.items():X[j]-=v
 post=eval_rows(M,X);bviol=[]
 for i,(lo,hi) in enumerate(M.bounds):
  if lo is not None and lo!=-float('inf') and X[i] < int(round(z.scale*lo)):bviol.append((i,'lo',X[i],lo))
  if hi is not None and hi!=float('inf') and X[i] > int(round(z.scale*hi)):bviol.append((i,'hi',X[i],hi))
 rviol=[];marg=[];zmax=None
 for i,(lhs,rhs) in enumerate(zip(post,M.rhs)):
  sr=scaled_rhs(rhs,z.scale)
  if lhs>sr:rviol.append((i,lhs,sr))
  if rhs==-1:marg.append(lhs)
  else:zmax=lhs if zmax is None else max(zmax,lhs)
 passed=not bviol and not rviol and len(marg)==len(P) and max(marg)<=-z.scale
 out={'schema':'shared-selected-support-exact-rational-v2','status':'PASS' if passed else 'FAIL','source_support_schema':J.get('schema'),'denominator_scale':z.scale,'proposal_boost':z.boost,'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'BC_shapes':[[list(p) for p in g] for g in bc],'SH_shapes':[[list(p) for p in g] for g in sh],'continuous_objective':float(res.fun),'variables':len(M.names),'rows':len(M.rows),'pre_repair_positive_zero_rows':sum(rhs==0 and lhs>0 for lhs,rhs in zip(pre,M.rhs)),'repair_variable_count':len(repair),'repair_total':sum(repair.values()),'repair_max':max(repair.values()) if repair else 0,'bound_violations':bviol[:20],'row_violations':rviol[:20],'zero_rhs_max_lhs':zmax,'profile_margin_numerators':marg,'required_profile_margin_numerator':-z.scale,'worst_margin_numerator':max(marg) if marg else None,'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'correct_scaled_rhs_rule':True,'interpretation':'PASS gives an exact rational feasible point X/scale. Structural rows are checked against 0 and profile margin rows against -scale. Finite evidence only; not a universal theorem.'}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','SH_shapes','profile_margin_numerators')},indent=2,sort_keys=True))
 if not passed:raise SystemExit(1)
if __name__=='__main__':main()
