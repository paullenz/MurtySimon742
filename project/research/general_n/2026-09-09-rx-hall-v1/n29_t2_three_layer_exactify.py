#!/usr/bin/env python3
"""Exactify the two compact all-902 n=29,t=2 rectangle+diagonal families.

Floating LP is proposal only. Acceptance is exact integer arithmetic with the
correct scaled normalization: homogeneous rows <=0 and each profile margin
<= -denominator_scale. Envelope rounding repairs alter only the unique free
ell/sig variable in its own homogeneous envelope row.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,hashlib,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('rd',HERE/'n29_t2_layer23_diag012_scan.py');rd=module_from_spec(sp);sp.loader.exec_module(rd)

SUPPORTS={
 '123':{
  'layers':(1,2,3),
  'rect':{(1,0),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(2,11),(2,14),(3,0),(3,1),(3,2),(3,3),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10)},
  'diag':{14,15,16},
  'provenance':{'run_id':34420236306,'artifact_id':10130669785,'artifact_sha256':'db2271c5a6e6e86c1595eb40ee70957ca3'}},
 '234':{
  'layers':(2,3,4),
  'rect':{(2,11),(2,12),(2,13),(2,14),(3,0),(3,2),(3,3),(3,5),(3,7),(3,10),(3,11),(3,12),(4,4),(4,5),(4,6),(4,8),(4,9)},
  'diag':{14,15,16},
  'provenance':{'run_id':34420236306,'artifact_id':10130675087,'artifact_sha256':'0ec568ac5d0dbc8afc72370e3a2304a15aff37c79f5868aa71d9a787207f7574'}}
}

def load_profiles(demands,rows):
    P=rd.allx.load29(demands,rows,2)
    return [{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in P]

def name_hash(names):
    payload=json.dumps([list(x) if isinstance(x,tuple) else x for x in names],separators=(',',':'))
    return hashlib.sha256(payload.encode()).hexdigest()

def exact_attempt(M,res,scale,boost):
    X=[int(round(float(v)*scale*boost)) for v in res.x]
    repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0: continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0: continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1:
            return None,{'failure':'non-envelope homogeneous rounding violation','row':i,'lhs':lhs,'candidates':[str(M.names[j]) for j in cand]}
        j=cand[0]; repairs[j]=max(repairs.get(j,0),lhs)
    for j,d in repairs.items(): X[j]-=d

    rowviol=[]; margins=[]; zero_max=None
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items())
        target=0 if rhs==0 else -scale
        if lhs>target: rowviol.append((i,lhs,target))
        if rhs==0: zero_max=lhs if zero_max is None else max(zero_max,lhs)
        else: margins.append(lhs)
    bviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        slo=None if lo is None else int(round(lo*scale)); shi=None if hi is None else int(round(hi*scale))
        if slo is not None and X[j]<slo: bviol.append((j,'lo',X[j],slo))
        if shi is not None and X[j]>shi: bviol.append((j,'hi',X[j],shi))
    ok=(not rowviol and not bviol and len(margins)==902 and max(margins)<=-scale)
    return (X if ok else None),{
      'scale':scale,'boost':boost,'repair_count':len(repairs),'repair_total':sum(repairs.values()),
      'repair_max':max(repairs.values()) if repairs else 0,'row_violation_count':len(rowviol),
      'row_violations':rowviol[:20],'bound_violation_count':len(bviol),'bound_violations':bviol[:20],
      'zero_rhs_max_lhs':zero_max,'margin_count':len(margins),
      'worst_margin_numerator':max(margins) if margins else None,'best_margin_numerator':min(margins) if margins else None,
      'required_margin_numerator':-scale}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--family',choices=sorted(SUPPORTS),required=True)
    ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    z=ap.parse_args();cfg=SUPPORTS[z.family];P=load_profiles(z.demands_json,z.rows)
    if len(P)!=902: raise SystemExit(f'expected 902 profiles, got {len(P)}')
    M,rect,diag=rd.build(P,12,16,10,cfg['layers'],(14,15,16))
    for D,V,w in rect:
        if (D,V) not in cfg['rect']: M.bounds[w]=(0,0)
    for K,w in diag:
        if K not in cfg['diag']: M.bounds[w]=(0,0)
    res=M.solve()
    out={'schema':'n29-t2-all902-three-layer-exact-v1','family':z.family,'layers':list(cfg['layers']),'profiles':len(P),
         'rows':len(M.rows),'variables':len(M.names),'rectangle_support':[list(x) for x in sorted(cfg['rect'])],
         'diagonal_K':sorted(cfg['diag']),'generator_count':len(cfg['rect'])+len(cfg['diag']),'support_provenance':cfg['provenance'],
         'floating_solve_success':bool(res.success),'floating_status':int(res.status),'floating_message':res.message,
         'floating_point_proposal_only':True,'integer_arithmetic_only_acceptance':True,
         'acceptance_rule':'all RHS=0 rows <=0 exactly; all 902 RHS=-1 margin rows <= -scale exactly; all bounds exact'}
    if not res.success:
        out['status']='FAIL_FLOAT';z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');raise SystemExit(1)
    attempts=[];chosen=None;meta=None
    for boost in (2,3,4,8):
      for scale in (10**6,10**8,10**10):
        X,m=exact_attempt(M,res,scale,boost);attempts.append(m)
        if X is not None:chosen=X;meta=m;break
      if chosen is not None:break
    out['attempts']=attempts;out['status']='PASS' if chosen is not None else 'FAIL_EXACT'
    if chosen is not None:
        out.update(meta);out['name_order_sha256']=name_hash(M.names);out['integer_numerators']=chosen
        out['nonzero_generator_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','J') and chosen[i]!=0}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,separators=(',',':'),sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('integer_numerators','attempts')},indent=2,sort_keys=True))
    if chosen is None:raise SystemExit(1)
if __name__=='__main__':main()
