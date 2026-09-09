#!/usr/bin/env python3
"""Test and exactify a hand-rounded integer rectdiag potential on n29 t2 hard38.

Candidate global weights, inferred from the sparse exact/floating support but then
fixed independently as integers:

D=2: V11=72, V12=72, V13=126
D=3: V0=366, V5=61, V6=48, V7=48, V8=48, V9=54, V10=72
J_b = 90.

Only profile-specific scalar dual variables remain free. A floating solve is
proposal; exact acceptance uses scaled integer arithmetic with these global
weights pinned exactly.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_rectdiag_sparse_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)
PAT={(2,11):72,(2,12):72,(2,13):126,(3,0):366,(3,5):61,(3,6):48,(3,7):48,(3,8):48,(3,9):54,(3,10):72}
JWEIGHT=90

def exact_attempt(M,res,scale,boost,pinned):
    X=[int(round(float(v)*scale*boost)) for v in res.x]
    # Override pinned global weights: they are exact values, not boosted proposals.
    for j,val in pinned.items():X[j]=int(val*scale)
    repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0:continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0:continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1:raise RuntimeError(('repair failure',i,lhs,[M.names[j] for j in cand]))
        j=cand[0];repairs[j]=max(repairs.get(j,0),lhs)
    for j,d in repairs.items():X[j]-=d
    viol=[];marg=[];zero=None;bviol=[]
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items());target=0 if rhs==0 else -scale
        if lhs>target:viol.append((i,lhs,target))
        if rhs==0:zero=lhs if zero is None else max(zero,lhs)
        else:marg.append(lhs)
    # Only enforce original nonneg/fixed bounds, except pinned equality values are exact.
    for j,(lo,hi) in enumerate(M.bounds):
        if j in pinned:
            if X[j]!=int(pinned[j]*scale):bviol.append((j,'pin',X[j],int(pinned[j]*scale)))
            continue
        if lo is not None and X[j]<int(round(lo*scale)):bviol.append((j,'lo',X[j],int(round(lo*scale))))
        if hi is not None and X[j]>int(round(hi*scale)):bviol.append((j,'hi',X[j],int(round(hi*scale))))
    ok=not viol and not bviol and len(marg)==38 and max(marg)<=-scale
    return (X if ok else None),{'scale':scale,'boost':boost,'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,'zero_rhs_max_lhs':zero,'row_violations':viol[:20],'bound_violations':bviol[:20],'margin_count':len(marg),'worst_margin_numerator':max(marg) if marg else None,'required_margin_numerator':-scale}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--boundary-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args();B=json.loads(z.boundary_json.read_text());P=[{'s':r['s'],'rho':r['rho'],'demand_id':r['demand_id']} for r in B['trimmed_survivor_records']]
    M,rect,diag=rd.build(P,12,16,10,True);pinned={}
    for D,V,w in rect:
        val=PAT.get((D,V),0);M.bounds[w]=(val,val);pinned[w]=val
    M.bounds[diag]=(JWEIGHT,JWEIGHT);pinned[diag]=JWEIGHT
    res=M.solve();out={'schema':'n29-t2-rectdiag-integer-pattern-v1','profiles':len(P),'floating_feasible':bool(res.success),'floating_status':int(res.status),'floating_message':res.message,'rectangles':[{'D':D,'V':V,'weight':w} for (D,V),w in sorted(PAT.items())],'diagonal':{'K':16,'c':0,'weight':JWEIGHT},'generator_count':11,'global_weights_hand_fixed_integers':True,'floating_proposal_only':True,'integer_acceptance':True}
    if not res.success:
        out['status']='FAIL_FLOAT';z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(1)
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10):
        X,m=exact_attempt(M,res,scale,2,pinned);attempts.append(m)
        if X is not None:chosen=X;meta=m;break
    out['attempts']=attempts;out['status']='PASS' if chosen is not None else 'FAIL_EXACT'
    if chosen is not None:
        out.update(meta);out['integer_numerators']={str(name):int(chosen[i]) for i,name in enumerate(M.names)}
    out['interpretation']='PASS means the hand-fixed integer global potential 72,72,126;366,61,48,48,48,54,72;J=90 admits exact rational profile-specific dual multipliers over all 38 hard n29 t2 profiles. It remains finite evidence, not an unrestricted theorem.'
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='integer_numerators'},indent=2,sort_keys=True))
    if chosen is None:raise SystemExit(1)
if __name__=='__main__':main()
