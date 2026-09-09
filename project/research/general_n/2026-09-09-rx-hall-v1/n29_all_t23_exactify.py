#!/usr/bin/env python3
"""Exactify one common 16-shape staircase potential across all 996 n29 profiles.

Rebuilds the t=2 and t=3 positive zero-slack hard profiles, solves the shared
16-shape envelope LP only as a proposal, scales/boosts the proposal to integer
numerators, deterministically repairs each free ell/sig envelope downward to
satisfy all homogeneous rows, and then checks every row and bound with Python
integer arithmetic. Profile margin rows have rational rhs -1 and therefore
integer rhs -scale. PASS is exact finite evidence; no floating infeasibility or
feasibility is accepted by itself.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('cp',HERE/'n29_common_potential_profile_scalars.py');cp=module_from_spec(sp);sp.loader.exec_module(cp)

def load(dp,rp,t):
    D=json.loads(Path(dp).read_text());out=[]
    for line in Path(rp).read_text().splitlines():
        if not line.strip():continue
        z=list(map(int,line.split()));did,total,rho=z[0],z[1],z[2:];s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t:out.append({'s':s,'rho':rho,'demand_id':did,'t':t})
    return out

def exact_attempt(M,res,scale,boost,expected_profiles):
    X=[int(round(float(v)*scale*boost)) for v in res.x];repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0:continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0:continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1:raise RuntimeError(('cannot identify envelope',i,lhs,[M.names[j] for j in cand]))
        j=cand[0];repairs[j]=max(repairs.get(j,0),lhs)
    for j,d in repairs.items():X[j]-=d
    rowviol=[];margins=[];zero_max=None
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items());target=0 if rhs==0 else -scale
        if lhs>target:rowviol.append((i,lhs,target))
        if rhs==0:zero_max=lhs if zero_max is None else max(zero_max,lhs)
        else:margins.append(lhs)
    bviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        if lo is not None and X[j] < int(round(lo*scale)):bviol.append((j,'lo',X[j],lo))
        if hi is not None and X[j] > int(round(hi*scale)):bviol.append((j,'hi',X[j],hi))
    ok=not rowviol and not bviol and len(margins)==expected_profiles and max(margins)<=-scale
    meta={'denominator_scale':scale,'proposal_boost':boost,'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,'row_violations':rowviol[:20],'bound_violations':bviol[:20],'zero_rhs_max_lhs':zero_max,'worst_margin_numerator':max(margins) if margins else None,'required_profile_margin_numerator':-scale,'correct_scaled_rhs_rule':True}
    return (X if ok else None),meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--t2-demands',type=Path,required=True);ap.add_argument('--t2-rows',type=Path,required=True);ap.add_argument('--t3-demands',type=Path,required=True);ap.add_argument('--t3-rows',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--dmax',type=int,required=True);ap.add_argument('--boost',type=int,default=2);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P2=load(z.t2_demands,z.t2_rows,2);P3=load(z.t3_demands,z.t3_rows,3);P=P2+P3;J=json.loads(z.support_json.read_text());bc=[tuple(tuple(p) for p in g) for g in J['BC_shapes']];sh=[tuple(tuple(p) for p in g) for g in J['SH_shapes']]
    M=cp.build(P,bc,sh,z.a,z.b,z.dmax);res=M.solve()
    if not res.success:raise SystemExit('shared 16-shape support no longer numerically feasible')
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10):
        X,m=exact_attempt(M,res,scale,z.boost,len(P));attempts.append(m)
        if X is not None:chosen=X;meta=m;break
    passed=chosen is not None
    out={'schema':'n29-all-t23-common-exact-v1','status':'PASS' if passed else 'FAIL','profiles':len(P),'t2_profiles':len(P2),'t3_profiles':len(P3),'support_count':len(bc)+len(sh),'BC_count':len(bc),'SH_count':len(sh),'rows':len(M.rows),'variables':len(M.names),'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'attempts':attempts,'interpretation':'PASS gives one exact rational common F+G staircase-weight vector across all 996 n29 t2+t3 hard profiles; scalar multipliers/envelopes remain profile-specific. Finite evidence only.'}
    if passed:
        out.update(meta);out['BC_shapes']=[[list(p) for p in g] for g in bc];out['SH_shapes']=[[list(p) for p in g] for g in sh];out['integer_staircase_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BC','SH')}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('BC_shapes','SH_shapes','integer_staircase_numerators','attempts')},indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
