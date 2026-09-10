#!/usr/bin/env python3
"""Generic standard-library exact replay for n=29 common BC potentials.

Supports t=2 or t=3 and arbitrary listed D layers / diagonal K values. Rebuilds
variable order and every envelope/margin inequality without importing SciPy,
NumPy, the LP builder or the exactifier.
"""
from pathlib import Path
from collections import Counter
import argparse,hashlib,json

def tterm(rho,q,p,j):return (q if q>=j+1 else 0)-(p if rho+q>=j else 0)
def load_profiles(dp,rp,t):
 D=json.loads(Path(dp).read_text());out=[]
 for line in Path(rp).read_text().splitlines():
  z=list(map(int,line.split()));did=z[0];rho=z[2:];s=D[did]['s']
  if min(s)>0 and sum(s)==sum(rho)+2*t:out.append({'s':s,'rho':rho,'demand_id':did})
 return out
def alloc(names,name):names.append(name);return len(names)-1
def name_hash(names):return hashlib.sha256(json.dumps([list(x) for x in names],separators=(',',':')).encode()).hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--t',type=int,required=True);ap.add_argument('--demands-json',type=Path,required=True);ap.add_argument('--rows',type=Path,required=True);ap.add_argument('--exact-json',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);z=ap.parse_args()
 E=json.loads(z.exact_json.read_text());P=load_profiles(z.demands_json,z.rows,z.t)
 if E.get('status')!='PASS':raise SystemExit('exact source is not PASS')
 if len(P)!=int(E['profiles']):raise SystemExit(f'profile mismatch {len(P)} != {E["profiles"]}')
 layers=tuple(E['layers']);diagKs=tuple(E.get('diagonal_K',[]));rect_support={tuple(x) for x in E['rectangle_support']};scale=int(E['scale']);X=list(map(int,E['integer_numerators']));names=[];rect=[]
 for D in layers:
  for V in range(17):rect.append((D,V,alloc(names,('BCrect',D,V))))
 diag=[(K,alloc(names,('J',K))) for K in diagKs];meta=[]
 for pi,pf in enumerate(P):
  lam=alloc(names,('lambda',pi));cc=alloc(names,('c',pi));mp=alloc(names,('mu+',pi));mm=alloc(names,('mu-',pi));taus={j:alloc(names,('tau',pi,j)) for j in range(1,13)};sc=Counter(pf['s']);rc=Counter(pf['rho']);ells={s:alloc(names,('ell',pi,s)) for s in sorted(sc)};sigs={r:alloc(names,('sig',pi,r)) for r in sorted(rc)};meta.append((lam,cc,mp,mm,taus,sc,rc,ells,sigs))
 hash_ok=E.get('name_order_sha256')==name_hash(names);length_ok=len(X)==len(names);viol=[];bviol=[];marg=[];zero_max=None
 def pot(d,h,factor,sign):
  v=16-h;tot=0
  for D,V,w in rect:
   if d>=D and v>=V:tot+=sign*factor*X[w]
  for K,w in diag:
   if d+v>=K:tot+=sign*factor*X[w]
  return tot
 if length_ok:
  for D,V,w in rect:
   if X[w]<0:bviol.append((str(names[w]),'negative',X[w]))
   if (D,V) not in rect_support and X[w]!=0:bviol.append((str(names[w]),'fixed_zero',X[w]))
  for K,w in diag:
   if X[w]<0:bviol.append((str(names[w]),'negative',X[w]))
  for pi,pf in enumerate(P):
   lam,cc,mp,mm,taus,sc,rc,ells,sigs=meta[pi]
   for j in [lam,cc,mp,mm,*taus.values()]:
    if X[j]<0:bviol.append((str(names[j]),'negative',X[j]))
   for s in sorted(sc):
    e=ells[s]
    for R in range(10-s+1):
     for x in range(s,16-R+1):
      lhs=X[e]-R*X[lam]-x*X[cc]+pot(R+s,R+x,x,-1);zero_max=lhs if zero_max is None else max(zero_max,lhs)
      if lhs>0 and len(viol)<20:viol.append(('label',pi,s,R,x,lhs))
   for rho in sorted(rc):
    sg=sigs[rho];qmax=min(12-rho,sum(si<=rho for si in pf['s']))
    for q in range(qmax+1):
     pmax=min(rho+3,15-q)
     for pp in range(pmax+1):
      lhs=X[sg]-(q-pp)*X[mp]+(q-pp)*X[mm]+q*X[cc]
      for j in range(1,13):lhs-=tterm(rho,q,pp,j)*X[taus[j]]
      lhs+=pot(rho+q-1,q+pp,q,1);zero_max=lhs if zero_max is None else max(zero_max,lhs)
      if lhs>0 and len(viol)<20:viol.append(('source',pi,rho,q,pp,lhs))
   lhs=sum(pf['rho'])*X[lam]-sum(n*X[ells[s]] for s,n in sc.items())-sum(n*X[sigs[r]] for r,n in rc.items());marg.append(lhs)
   if lhs>-scale and len(viol)<20:viol.append(('margin',pi,lhs,-scale))
 ok=length_ok and hash_ok and not viol and not bviol and len(marg)==len(P) and max(marg)<=-scale and zero_max<=0
 out={'schema':'n29-common-potential-independent-replay-v1','t':z.t,'status':'PASS' if ok else 'FAIL','profiles':len(P),'variables_expected':len(names),'variables_received':len(X),'name_order_hash_ok':hash_ok,'scale':scale,'row_violation_count':len(viol),'row_violations':viol,'bound_violation_count':len(bviol),'bound_violations':bviol[:20],'zero_rhs_max_lhs':zero_max,'margin_count':len(marg),'worst_margin_numerator':max(marg) if marg else None,'required_margin_numerator':-scale,'standard_library_only':True,'imports_lp_builder':False,'imports_exactifier':False}
 z.output.parent.mkdir(parents=True,exist_ok=True);z.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
 if not ok:raise SystemExit(1)
if __name__=='__main__':main()
