#!/usr/bin/env python3
"""Generic standard-library exact replay for n29 t2 three-layer certificates.

Reconstructs variable order and all finite inequalities from profile data. It
imports neither SciPy/NumPy nor the exactifier/LP builder. The diagonal list is
read from the certificate, so the same checker covers the 3-step and c={0,2}
2-step families.
"""
from pathlib import Path
from collections import Counter
import argparse,hashlib,json

def tterm(rho,q,p,j): return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
def load_profiles(dp,rp,t=2):
    D=json.loads(Path(dp).read_text());out=[]
    for line in Path(rp).read_text().splitlines():
        z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
        if min(s)>0 and sum(s)==sum(rho)+2*t:out.append({'s':s,'rho':rho,'demand_id':did})
    return out

def alloc(names,idx,name):idx[name]=len(names);names.append(name);return idx[name]
def name_hash(names):
    payload=json.dumps([list(x) for x in names],separators=(',',':'))
    return hashlib.sha256(payload.encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--exact-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
    E=json.loads(z.exact_json.read_text());P=load_profiles(z.demands_json,z.rows)
    if E.get('status')!='PASS':raise SystemExit('exact source is not PASS')
    if len(P)!=902:raise SystemExit(f'expected 902 profiles, got {len(P)}')
    layers=tuple(E['layers']);diagKs=tuple(E['diagonal_K']);rect_support={tuple(x) for x in E['rectangle_support']};diag_support=set(diagKs);scale=int(E['scale']);X=list(map(int,E['integer_numerators']))
    names=[];idx={};rect=[]
    for D in layers:
        for V in range(17):rect.append((D,V,alloc(names,idx,('BCrect',D,V))))
    diag=[(K,alloc(names,idx,('J',K))) for K in diagKs]
    profmeta=[]
    for pi,pf in enumerate(P):
        lam=alloc(names,idx,('lambda',pi));cc=alloc(names,idx,('c',pi));mp=alloc(names,idx,('mu+',pi));mm=alloc(names,idx,('mu-',pi));taus={j:alloc(names,idx,('tau',pi,j)) for j in range(1,13)}
        sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={s:alloc(names,idx,('ell',pi,s)) for s in sorted(sc)};sigs={r:alloc(names,idx,('sig',pi,r)) for r in sorted(rc)};profmeta.append((lam,cc,mp,mm,taus,sc,rc,ells,sigs))
    missing_len=(len(X)!=len(names));hash_ok=(E.get('name_order_sha256')==name_hash(names));violations=[];zero_max=None;margins=[];boundviol=[]
    def addpot_lhs(d,h,factor,sign):
        v=16-h;tot=0
        for D,V,w in rect:
            if d>=D and v>=V:tot+=sign*factor*X[w]
        for K,w in diag:
            if d+v>=K:tot+=sign*factor*X[w]
        return tot
    if not missing_len:
      for D,V,w in rect:
        if X[w]<0:boundviol.append((str(names[w]),'nonnegative',X[w]))
        if (D,V) not in rect_support and X[w]!=0:boundviol.append((str(names[w]),'fixed_zero',X[w]))
      for K,w in diag:
        if X[w]<0:boundviol.append((str(names[w]),'nonnegative',X[w]))
        if K not in diag_support and X[w]!=0:boundviol.append((str(names[w]),'fixed_zero',X[w]))
      for pi,pf in enumerate(P):
        lam,cc,mp,mm,taus,sc,rc,ells,sigs=profmeta[pi]
        for j in [lam,cc,mp,mm,*taus.values()]:
            if X[j]<0:boundviol.append((str(names[j]),'nonnegative',X[j]))
        for s in sorted(sc):
            e=ells[s]
            for R in range(10-s+1):
                for x in range(s,16-R+1):
                    lhs=X[e]-R*X[lam]-x*X[cc]+addpot_lhs(R+s,R+x,x,-1);zero_max=lhs if zero_max is None else max(zero_max,lhs)
                    if lhs>0 and len(violations)<20:violations.append(('label',pi,s,R,x,lhs))
        for rho in sorted(rc):
            sg=sigs[rho];qmax=min(12-rho,sum(si<=rho for si in pf['s']))
            for q in range(qmax+1):
                pmax=min(rho+3,15-q)
                for pp in range(pmax+1):
                    lhs=X[sg]-(q-pp)*X[mp]+(q-pp)*X[mm]+q*X[cc]
                    for j in range(1,13):lhs-=tterm(rho,q,pp,j)*X[taus[j]]
                    lhs+=addpot_lhs(rho+q-1,q+pp,q,1);zero_max=lhs if zero_max is None else max(zero_max,lhs)
                    if lhs>0 and len(violations)<20:violations.append(('source',pi,rho,q,pp,lhs))
        lhs=sum(pf['rho'])*X[lam]-sum(n*X[ells[s]] for s,n in sc.items())-sum(n*X[sigs[r]] for r,n in rc.items());margins.append(lhs)
        if lhs>-scale and len(violations)<20:violations.append(('margin',pi,lhs,-scale))
    passflag=(not missing_len and hash_ok and not violations and not boundviol and len(margins)==902 and max(margins)<=-scale and zero_max<=0)
    out={'schema':'n29-t2-all902-three-layer-independent-replay-v2','family':E.get('family'),'status':'PASS' if passflag else 'FAIL','profiles':len(P),'diagonal_K':list(diagKs),'variables_expected':len(names),'variables_received':len(X),'name_order_hash_ok':hash_ok,'scale':scale,'row_violation_count':len(violations),'row_violations':violations,'bound_violation_count':len(boundviol),'bound_violations':boundviol[:20],'zero_rhs_max_lhs':zero_max,'margin_count':len(margins),'worst_margin_numerator':max(margins) if margins else None,'required_margin_numerator':-scale,'standard_library_only':True,'imports_lp_builder':False,'imports_exactifier':False}
    z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not passflag:raise SystemExit(1)
if __name__=='__main__':main()
