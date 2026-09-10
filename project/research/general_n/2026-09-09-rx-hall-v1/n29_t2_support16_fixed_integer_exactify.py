#!/usr/bin/env python3
"""Exactify the human-readable 16-term n=29,t=2 BC potential.

The primitive global weights were found by the multiplier-8 reconnaissance:
  D=2: V11,12,13,14 -> 11,12,28,8
  D=3: V0,4,7,8,10,12 -> 41,8,8,8,11,5
  D=4: V2,3,6,9 -> 5,5,6,8
  J2(K14),J0(K16) -> 15,14.

HiGHS is used only to propose the profile-specific scalar/envelope variables.
Acceptance is exact Python integer arithmetic with every profile margin checked
against -scale.  A positive global_scale_factor merely multiplies the entire
certificate; dividing by it recovers the primitive global potential and still
leaves a strict contradiction.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('core',HERE/'n29_t2_three_layer_exactify.py');core=module_from_spec(sp);sp.loader.exec_module(core)
rd=core.rd
W={
 ('r',2,11):11,('r',2,12):12,('r',2,13):28,('r',2,14):8,
 ('r',3,0):41,('r',3,4):8,('r',3,7):8,('r',3,8):8,('r',3,10):11,('r',3,12):5,
 ('r',4,2):5,('r',4,3):5,('r',4,6):6,('r',4,9):8,
 ('j',14):15,('j',16):14}
RECT={(k[1],k[2]) for k in W if k[0]=='r'}

def exact_attempt(M,res,rect,diag,scale,gscale):
    X=[int(round(float(v)*scale*gscale)) for v in res.x]
    fixed={}
    for D,V,j in rect: fixed[j]=gscale*W.get(('r',D,V),0)
    for K,j in diag: fixed[j]=gscale*W[('j',K)]
    for j,val in fixed.items(): X[j]=val*scale
    repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0: continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0: continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1:return None,{'failure':'non-envelope homogeneous violation','row':i,'lhs':lhs,'candidates':[str(M.names[j]) for j in cand]}
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
        if j in fixed:
            want=fixed[j]*scale
            if X[j]!=want:bviol.append((j,'fixed',X[j],want))
        else:
            if lo is not None and X[j] < int(round(lo*scale*gscale)):bviol.append((j,'lo',X[j],lo))
            if hi is not None and X[j] > int(round(hi*scale*gscale)):bviol.append((j,'hi',X[j],hi))
    ok=not rowviol and not bviol and len(margins)==902 and max(margins)<=-scale
    return (X if ok else None),{'scale':scale,'global_scale_factor':gscale,'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,'row_violation_count':len(rowviol),'row_violations':rowviol[:20],'bound_violation_count':len(bviol),'bound_violations':bviol[:20],'zero_rhs_max_lhs':zero_max,'margin_count':len(margins),'worst_margin_numerator':max(margins) if margins else None,'best_margin_numerator':min(margins) if margins else None,'required_margin_numerator':-scale}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    P=core.load_profiles(z.demands_json,z.rows)
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,(2,3,4),(14,16))
    for D,V,j in rect:M.bounds[j]=(W.get(('r',D,V),0),W.get(('r',D,V),0))
    for K,j in diag:M.bounds[j]=(W[('j',K)],W[('j',K)])
    res=M.solve();out={'schema':'n29-t2-support16-fixed-integer-exact-v1','t':2,'layers':[2,3,4],'diagonal_K':[14,16],'rectangle_support':[list(x) for x in sorted(RECT)],'primitive_integer_weights':{str(k):v for k,v in W.items()},'profiles':len(P),'rows':len(M.rows),'variables':len(M.names),'floating_solve_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message,'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,'acceptance_rule':'all RHS=0 rows <=0 exactly; all 902 RHS=-1 margin rows <=-scale exactly; primitive global potential fixed exactly up to one common positive factor'}
    if not res.success:
        out['status']='FAIL_FLOAT';z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');raise SystemExit(1)
    attempts=[];chosen=None;meta=None
    for gscale in (1,2,4,8,16):
      for scale in (10**6,10**8,10**10):
        X,m=exact_attempt(M,res,rect,diag,scale,gscale);attempts.append(m)
        if X is not None:chosen=X;meta=m;break
      if chosen is not None:break
    out['attempts']=attempts;out['status']='PASS' if chosen is not None else 'FAIL_EXACT'
    if chosen is not None:
        out.update(meta);out['name_order_sha256']=core.name_hash(M.names);out['integer_numerators']=chosen
        out['strict_primitive_interpretation']='Divide every certificate coefficient by global_scale_factor. The listed primitive integer potential is then exact and the final margin remains strictly negative.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','attempts')},indent=2,sort_keys=True))
    if chosen is None:raise SystemExit(1)
if __name__=='__main__':main()
