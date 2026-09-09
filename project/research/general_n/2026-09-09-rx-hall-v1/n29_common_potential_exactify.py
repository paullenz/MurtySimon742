#!/usr/bin/env python3
"""Exactify a selected common n29 staircase-potential support.

The support is supplied either as active_BC/active_SH records (MILP output) or
BC_shapes/SH_shapes (prune output). Rebuild the 38-profile common-potential LP,
solve numerically only to propose continuous coefficients, scale/round all
variables to integers, then repair tiny positive homogeneous envelope residuals
by lowering the corresponding free ell/sig envelope variable. Final acceptance
checks every row and bound using Python integer arithmetic only.

PASS is finite exact evidence for the selected support. It is not a universal
Murty--Simon theorem and does not make the numerical solver proof-producing.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def parse_support(J):
    if 'active_BC' in J and 'active_SH' in J:
        bc=[tuple(tuple(p) for p in x['generators']) for x in J['active_BC']]
        sh=[tuple(tuple(p) for p in x['generators']) for x in J['active_SH']]
        return bc,sh
    if 'BC_shapes' in J and 'SH_shapes' in J:
        bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']]
        sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
        return bc,sh
    raise ValueError('unrecognised support schema')

def exact_attempt(M,res,scale):
    X=[int(round(float(v)*scale)) for v in res.x]
    # Initial exact bound check. All finite lower bounds in this model are 0.
    bviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        if lo is not None and X[j] < int(round(lo*scale)):bviol.append((j,'lo',X[j],lo))
        if hi is not None and X[j] > int(round(hi*scale)):bviol.append((j,'hi',X[j],hi))
    if bviol:return None,{'bound_violations':bviol[:20]}
    # Every homogeneous envelope row has one free ell/sig variable with coeff +1.
    repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0:continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0:continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1:raise RuntimeError(('cannot identify envelope',i,lhs,[M.names[j] for j in cand]))
        j=cand[0];repairs[j]=max(repairs.get(j,0),lhs)
    for j,d in repairs.items():X[j]-=d
    # Recheck exactly after repair.
    rowviol=[];zero_max=None;margins=[]
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs>rhs:rowviol.append((i,lhs,rhs))
        if rhs==0:zero_max=lhs if zero_max is None else max(zero_max,lhs)
        elif rhs==-1:margins.append(lhs)
        else:raise RuntimeError(('unexpected rhs',i,rhs))
    bviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        if lo is not None and X[j] < int(round(lo*scale)):bviol.append((j,'lo',X[j],lo))
        if hi is not None and X[j] > int(round(hi*scale)):bviol.append((j,'hi',X[j],hi))
    ok=(not rowviol and not bviol and len(margins)==38 and max(margins)<=-1)
    meta={'scale':scale,'repairs':{str(M.names[j]):d for j,d in repairs.items()},'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,'row_violations':rowviol[:20],'bound_violations':bviol[:20],'zero_rhs_max_lhs':zero_max,'profile_margin_lhs':margins,'worst_margin_lhs':max(margins) if margins else None}
    return (X if ok else None),meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());J=json.loads(z.support_json.read_text());bc,sh=parse_support(J);P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    M=cp.build(P,bc,sh,z.a,z.b,z.dmax);res=M.solve()
    if not res.success:raise SystemExit('selected support no longer numerically feasible')
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10,10**12):
        X,m=exact_attempt(M,res,scale);attempts.append({k:v for k,v in m.items() if k not in ('profile_margin_lhs','repairs')})
        if X is not None:chosen=X;meta=m;break
    passed=chosen is not None
    out={'schema':'n29-common-potential-exact-integer-v1','status':'PASS' if passed else 'FAIL','profiles':len(P),'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'BC_shapes':[[list(p) for p in g] for g in bc],'SH_shapes':[[list(p) for p in g] for g in sh],'rows':len(M.rows),'variables':len(M.names),'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'attempts':attempts,'interpretation':'PASS gives an exact integer feasible point for one common F+G across all 38 n29 profiles, with profile-specific scalar dual multipliers. Finite evidence only.'}
    if passed:
        out.update(meta);out['integer_variables']={str(name):int(chosen[i]) for i,name in enumerate(M.names)}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_variables','BC_shapes','SH_shapes','repairs','profile_margin_lhs')},indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
