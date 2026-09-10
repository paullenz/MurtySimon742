#!/usr/bin/env python3
"""Exactify a compact n=29,t=2 rectangle+diagonal common potential.

Floating HiGHS is proposal-only. Acceptance scales/boosts the full proposal,
repairs only free ell/sig envelope variables downward on homogeneous rows, and
then checks every inequality and bound using Python integers. Nonhomogeneous
profile margins have rational RHS -1, hence integer RHS -scale.

A PASS is finite exact evidence conditional on the graph-to-profile bridge.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
import argparse,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('base',HERE/'n29_t2_layer23_diag012_scan.py');base=module_from_spec(sp);sp.loader.exec_module(base)
sp2=spec_from_file_location('allx',HERE/'cross_order_all1003_fixed16.py');allx=module_from_spec(sp2);sp2.loader.exec_module(allx)

def load_profiles(dp,rp):
    raw=allx.load29(dp,rp,2)
    return [{'s':p['s'],'rho':p['rho'],'demand_id':p.get('id')} for p in raw]

def exact_attempt(M,res,scale,boost,expected_profiles):
    X=[int(round(float(v)*scale*boost)) for v in res.x]
    repairs={}
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        if rhs!=0: continue
        lhs=sum(int(c)*X[j] for j,c in row.items())
        if lhs<=0: continue
        cand=[j for j,c in row.items() if c==1 and isinstance(M.names[j],tuple) and M.names[j][0] in ('ell','sig')]
        if len(cand)!=1:
            return None,{'failure':'cannot_identify_envelope','row':i,'lhs':lhs,'candidates':[str(M.names[j]) for j in cand]}
        j=cand[0]; repairs[j]=max(repairs.get(j,0),lhs)
    for j,d in repairs.items(): X[j]-=d
    rowviol=[]; margins=[]; zero_max=None
    for i,(row,rhs) in enumerate(zip(M.rows,M.rhs)):
        lhs=sum(int(c)*X[j] for j,c in row.items())
        target=0 if rhs==0 else int(rhs)*scale
        if lhs>target: rowviol.append((i,lhs,target))
        if rhs==0: zero_max=lhs if zero_max is None else max(zero_max,lhs)
        else: margins.append(lhs)
    bviol=[]
    for j,(lo,hi) in enumerate(M.bounds):
        if lo is not None and X[j] < int(round(lo*scale)): bviol.append((j,'lo',X[j],lo))
        if hi is not None and X[j] > int(round(hi*scale)): bviol.append((j,'hi',X[j],hi))
    ok=(not rowviol and not bviol and len(margins)==expected_profiles and max(margins)<=-scale)
    meta={'denominator_scale':scale,'proposal_boost':boost,'repair_count':len(repairs),'repair_total':sum(repairs.values()),'repair_max':max(repairs.values()) if repairs else 0,'row_violations':rowviol[:20],'bound_violations':bviol[:20],'zero_rhs_max_lhs':zero_max,'worst_margin_numerator':max(margins) if margins else None,'required_profile_margin_numerator':-scale,'correct_scaled_rhs_rule':True}
    return (X if ok else None),meta

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--layers',required=True);ap.add_argument('--boost',type=int,default=2);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--certificate',type=Path,required=True);z=ap.parse_args()
    layers=tuple(int(x) for x in z.layers.split(','));
    if layers not in ((1,2,3),(2,3,4)): raise SystemExit('layers must be 1,2,3 or 2,3,4')
    P=load_profiles(z.demands_json,z.rows);M,rect,diag=base.build(P,layers=layers,steps=(14,15,16));res=M.solve()
    if not res.success: raise SystemExit('compact family is no longer numerically feasible')
    chosen=None;meta=None;attempts=[]
    for scale in (10**6,10**8,10**10,10**12):
        X,m=exact_attempt(M,res,scale,z.boost,len(P));attempts.append(m)
        if X is not None: chosen=X;meta=m;break
    passed=chosen is not None
    out={'schema':'n29-t2-compact-exact-v1','status':'PASS' if passed else 'FAIL','profiles':len(P),'layers':list(layers),'diagonal_K':[14,15,16],'diagonal_c':[2,1,0],'rows':len(M.rows),'variables':len(M.names),'integer_arithmetic_only_acceptance':True,'floating_point_proposal_only':True,'attempts':attempts}
    if passed:
        cert={'schema':'n29-t2-compact-certificate-v1','layers':list(layers),'scale':meta['denominator_scale'],'boost':z.boost,'profiles':len(P),'X':chosen}
        raw=(json.dumps(cert,separators=(',',':'))+'\n').encode();z.certificate.parent.mkdir(parents=True,exist_ok=True)
        with gzip.open(z.certificate,'wb',compresslevel=9,mtime=0) as f:f.write(raw)
        sha=hashlib.sha256(z.certificate.read_bytes()).hexdigest();out.update(meta);out['certificate_sha256']=sha;out['certificate_file']=z.certificate.name
        out['integer_generator_numerators']={str(M.names[i]):int(chosen[i]) for i in range(len(M.names)) if isinstance(M.names[i],tuple) and M.names[i][0] in ('BCrect','J')}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('attempts','integer_generator_numerators')},indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)
if __name__=='__main__':main()
