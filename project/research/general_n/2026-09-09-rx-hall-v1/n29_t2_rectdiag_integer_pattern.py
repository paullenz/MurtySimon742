#!/usr/bin/env python3
"""Test and exactify a hand-rounded integer rectdiag potential ray on n29 t2 hard38.

Candidate normalized global weights:

D=2: V11=72, V12=72, V13=126
D=3: V0=366, V5=61, V6=48, V7=48, V8=48, V9=54, V10=72
J_b = 90.

Audit history
-------------
v1 contained a scaling bug: it multiplied profile-specific dual variables without
multiplying the pinned global potential.  v2 fixed that scaling, but its exact
acceptance still demanded the *floating normalization* margin <= -C after integer
rounding.  That is stronger than the logical Farkas requirement.  Once all zero-
RHS coefficient inequalities are exact, the contradiction row only has to be
strictly negative.  The normalization -1 (or -C) is an LP convenience, not part
of the mathematical certificate.

This v3 therefore:
  * scales the whole global potential ray consistently;
  * uses strengthened floating margins -C for numerical slack;
  * repairs/checks zero-RHS rows in integer arithmetic;
  * accepts a profile only when its final integer contradiction numerator is < 0.

Dividing an accepted scaled certificate by the ray scale C preserves strict
negativity and recovers the normalized small-integer global potential.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_rectdiag_sparse_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
PAT={(2,11):72,(2,12):72,(2,13):126,(3,0):366,(3,5):61,(3,6):48,(3,7):48,(3,8):48,(3,9):54,(3,10):72}
JWEIGHT=90

def exact_attempt(M,res,denom,pinned):
    X=[int(round(float(v)*denom)) for v in res.x]
    for j,val in pinned.items(): X[j]=int(val*denom)
    repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0: continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0: continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1: raise RuntimeError(('repair failure',i,lhs,[M.names[j] for j in cand]))
        j=cand[0]; repairs[j]=max(repairs.get(j,0),lhs)
    for j,d in repairs.items(): X[j]-=d

    zero_viol=[]; margins=[]; zero_max=None; bviol=[]
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if rhs==0:
            zero_max=lhs if zero_max is None else max(zero_max,lhs)
            if lhs>0: zero_viol.append((i,lhs,0))
        else:
            margins.append({'row':i,'lhs_numerator':lhs,'floating_target_numerator':int(round(float(rhs)*denom))})

    for j,(lo,hi) in enumerate(M.bounds):
        if j in pinned:
            target=int(pinned[j]*denom)
            if X[j]!=target: bviol.append((j,'pin',X[j],target))
            continue
        if lo is not None and X[j]<int(round(lo*denom)): bviol.append((j,'lo',X[j],int(round(lo*denom))))
        if hi is not None and X[j]>int(round(hi*denom)): bviol.append((j,'hi',X[j],int(round(hi*denom))))

    nonnegative_margin=[m for m in margins if m['lhs_numerator']>=0]
    ok=not zero_viol and not bviol and len(margins)==38 and not nonnegative_margin
    meta={
        'denominator_scale':denom,
        'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,
        'zero_rhs_max_lhs':zero_max,'zero_row_violations':zero_viol[:20],'bound_violations':bviol[:20],
        'margin_count':len(margins),'nonnegative_margin_count':len(nonnegative_margin),'nonnegative_margins':nonnegative_margin[:20],
        'worst_margin_numerator':max((m['lhs_numerator'] for m in margins),default=None),
        'strict_negativity_required':True,
        'floating_margin_targets_are_normalization_only':True
    }
    return (X if ok else None),meta

def run_ray(P,ray_scale):
    M,rect,diag=rd.build(P,12,16,10,True); pinned={}
    for D,V,w in rect:
        val=ray_scale*PAT.get((D,V),0); M.bounds[w]=(val,val); pinned[w]=val
    val=ray_scale*JWEIGHT; M.bounds[diag]=(val,val); pinned[diag]=val
    M.rhs=[(-ray_scale if rhs==-1 else rhs) for rhs in M.rhs]
    res=M.solve()
    rec={'ray_scale':ray_scale,'floating_feasible':bool(res.success),'floating_status':int(res.status),'floating_message':res.message}
    if not res.success: return rec,None,None,M
    attempts=[]; chosen=None; meta=None
    for denom in (10**6,10**8,10**10):
        X,m=exact_attempt(M,res,denom,pinned); attempts.append(m)
        if X is not None: chosen=X; meta=m; break
    rec['attempts']=attempts; rec['exact_pass']=chosen is not None
    if meta: rec.update(meta)
    return rec,chosen,pinned,M

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--boundary-json',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text()); P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    out={
        'schema':'n29-t2-rectdiag-integer-pattern-v3','profiles':len(P),
        'normalized_rectangles':[{'D':D,'V':V,'weight':w} for (D,V),w in sorted(PAT.items())],
        'normalized_diagonal':{'K':16,'c':0,'weight':JWEIGHT},'generator_count':11,
        'global_weights_hand_fixed_integers':True,'integer_arithmetic_only_acceptance':True,
        'audit_history':[
            'v1 invalid exactification scaling: profile duals boosted without global potential',
            'v2 corrected scaling but incorrectly required the arbitrary LP margin normalization after rounding',
            'v3 accepts exactly the logical requirement: all homogeneous rows <=0 and every contradiction margin <0'
        ]
    }
    runs=[]; accepted=None
    for C in (2,10,100):
        rec,X,pinned,M=run_ray(P,C); runs.append(rec)
        if X is not None: accepted=(C,X,M); break
    out['ray_attempts']=runs; out['status']='PASS' if accepted else 'FAIL_EXACT'
    if accepted:
        C,X,M=accepted; out['accepted_ray_scale']=C
        out['normalization']='Divide every accepted rational dual coefficient by accepted_ray_scale. The global potential then has exactly the normalized small-integer weights listed above; every contradiction margin remains strictly negative.'
        out['scaled_integer_numerators']={str(name):int(X[i]) for i,name in enumerate(M.names)}
        out['accepted_denominator_scale']=next(r['denominator_scale'] for r in runs if r.get('exact_pass'))
        out['worst_normalized_margin']=next(r['worst_margin_numerator']/r['denominator_scale']/C for r in runs if r.get('exact_pass'))
    out['interpretation']='PASS is exact finite rational evidence for the normalized small-integer global potential ray on all 38 n29 t2 hard profiles. It is not a support-minimality certificate or unrestricted theorem.'
    z.output.parent.mkdir(parents=True,exist_ok=True); z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='scaled_integer_numerators'},indent=2,sort_keys=True))
    if not accepted: raise SystemExit(1)
if __name__=='__main__': main()
