#!/usr/bin/env python3
"""Exactify a fixed all-rectangle + J_b support for n=29,t=2 hard38.

The support is read from `active_rectangles_greedy` (preferred) or
`active_rectangles_initial` in a sparse-scan checkpoint. All other rectangle
coefficients are fixed to zero. A floating feasible point is only a proposal;
acceptance uses integer numerators X/scale and exact integer row arithmetic.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_rectdiag_sparse_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)

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
        slo=None if lo is None else int(round(lo*scale));shi=None if hi is None else int(round(hi*scale))
        if slo is not None and X[j]<slo:bviol.append((j,'lo',X[j],slo))
        if shi is not None and X[j]>shi:bviol.append((j,'hi',X[j],shi))
    ok=not rowviol and not bviol and len(margins)==38 and max(margins)<=-scale
    meta={'denominator_scale':scale,'proposal_boost':boost,'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,'repairs':{str(M.names[j]):d for j,d in repairs.items()},'row_violations':rowviol[:20],'bound_violations':bviol[:20],'zero_rhs_max_lhs':zero_max,'profile_margin_numerators':margins,'required_profile_margin_numerator':-scale,'worst_margin_numerator':max(margins) if margins else None}
    return (X if ok else None),meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--support-json',type=Path,required=True);ap.add_argument('--boost',type=int,default=2);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    B=json.loads(z.boundary_json.read_text());S=json.loads(z.support_json.read_text());root=S.get('results',S);rec=root.get('hard38_greedy.json',root)
    shapes=rec.get('active_rectangles_greedy') or rec.get('active_rectangles_initial')
    if not shapes:raise SystemExit('no rectangle support found')
    support={(int(q['D']),int(q['V'])) for q in shapes};P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    M,rect,diag=rd.build(P,12,16,10,True)
    for D,V,w in rect:
        if (D,V) not in support:M.bounds[w]=(0,0)
    res=M.solve()
    if not res.success:raise SystemExit('fixed rectdiag support no longer numerically feasible')
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10):
        X,m=exact_attempt(M,res,scale,z.boost);attempts.append({k:v for k,v in m.items() if k not in ('repairs','profile_margin_numerators')})
        if X is not None:chosen=X;meta=m;break
    passed=chosen is not None
    out={'schema':'n29-t2-rectdiag-exact-v1','status':'PASS' if passed else 'FAIL','profiles':len(P),'rectangle_count':len(support),'generator_count':len(support)+1,'rectangles':[{'D':D,'V':V} for D,V in sorted(support)],'diagonal':{'K':16,'c':0},'rows':len(M.rows),'variables':len(M.names),'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,'attempts':attempts,'interpretation':'PASS is exact finite rational evidence that the listed BC rectangles plus J_b admit one common potential over all 38 n29 t2 hard profiles. It is not a support-minimality certificate or unrestricted theorem.'}
    if passed:
        out.update(meta);out['integer_numerators']={str(name):int(chosen[i]) for i,name in enumerate(M.names)};out['generator_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if (isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','Jb') and chosen[i]!=0)}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','repairs','profile_margin_numerators')},indent=2,sort_keys=True))
    if not passed:raise SystemExit(1)
if __name__=='__main__':main()
