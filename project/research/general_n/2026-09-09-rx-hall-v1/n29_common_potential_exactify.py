#!/usr/bin/env python3
"""Exactify a selected common n29 staircase-potential support correctly.

A floating feasible point is proposal only. Integer numerators X are interpreted
as the rational point X/scale. Homogeneous rows therefore have scaled RHS 0,
while every profile margin row with continuous RHS -1 must be checked against
integer RHS -scale. A safety boost >1 is applied before rounding; this preserves
homogeneous inequalities and gives room for deterministic downward ell/sig
rounding repair while strengthening the negative profile margins.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def parse_support(J):
    if 'active_BC' in J and 'active_SH' in J:
        return [tuple(tuple(p) for p in x['generators']) for x in J['active_BC']],[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
    if 'BC_shapes' in J and 'SH_shapes' in J:
        return [tuple(tuple(p) for p in g) for g in J['BC_shapes']],[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    raise ValueError('unrecognised support schema')
def srhs(rhs,scale):
    if rhs==0:return 0
    if rhs==-1:return -scale
    raise RuntimeError(('unexpected rhs',rhs))
def exact_attempt(M,res,scale,boost):
    X=[int(round(float(v)*scale*boost)) for v in res.x];repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0:continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0:continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1:raise RuntimeError(('cannot identify envelope',i,lhs,[M.names[j] for j in cand]))
        j=cand[0];repairs[j]=max(repairs.get(j,0),lhs)
    for j,d in repairs.items():X[j]-=d
    rowviol=[];zero_max=None;margins=[]
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items());target=srhs(rhs,scale)
        if lhs>target:rowviol.append((i,lhs,target))
        if rhs==0:zero_max=lhs if zero_max is None else max(zero_max,lhs)
        else:margins.append(lhs)
    bviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        if lo is not None and X[j] < int(round(lo*scale)):bviol.append((j,'lo',X[j],lo))
        if hi is not None and X[j] > int(round(hi*scale)):bviol.append((j,'hi',X[j],hi))
    ok=not rowviol and not bviol and len(margins)==38 and max(margins)<=-scale
    meta={'denominator_scale':scale,'proposal_boost':boost,'repairs':{str(M.names[j]):d for j,d in repairs.items()},'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,'row_violations':rowviol[:20],'bound_violations':bviol[:20],'zero_rhs_max_lhs':zero_max,'profile_margin_numerators':margins,'required_profile_margin_numerator':-scale,'worst_margin_numerator':max(margins) if margins else None,'correct_scaled_rhs_rule':True}
    return (X if ok else None),meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--boost',type=int,default=2);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());J=json.loads(z.support_json.read_text());bc,sh=parse_support(J);P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    M=cp.build(P,bc,sh,z.a,z.b,z.dmax);res=M.solve()
    if not res.success:raise SystemExit('selected support no longer numerically feasible')
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10):
        X,m=exact_attempt(M,res,scale,z.boost);attempts.append({k:v for k,v in m.items() if k not in ('profile_margin_numerators','repairs')})
        if X is not None:chosen=X;meta=m;break
    passed=chosen is not None
    out={'schema':'n29-common-potential-exact-rational-v2','status':'PASS' if passed else 'FAIL','profiles':len(P),'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'BC_shapes':[[list(p) for p in g] for g in bc],'SH_shapes':[[list(p) for p in g] for g in sh],'rows':len(M.rows),'variables':len(M.names),'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'correct_scaled_rhs_rule':True,'attempts':attempts,'interpretation':'PASS gives an exact rational point X/scale for one common F+G across all 38 n29 profiles, with profile-specific scalar dual multipliers. Finite evidence only.'}
    if passed:out.update(meta);out['integer_numerators']={str(name):int(chosen[i]) for i,name in enumerate(M.names)}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','BC_shapes','SH_shapes','repairs','profile_margin_numerators')},indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
