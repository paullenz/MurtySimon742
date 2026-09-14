import sys,json,csv,collections
from pathlib import Path
import prior as old
root=Path('/mnt/data/capped_previous/MurtySimon742_Capped_Spill_2026-09-14')
rows=[]
for row,raw in enumerate(csv.DictReader((root/'data/SYNTHETIC_INTERVAL_PROFILES.tsv').open(),delimiter='\t')):
 p={k:([int(x) for x in v.split(',')] if k in ('s','q','rho','P') else int(v)) for k,v in raw.items()};p['row']=row;rows.append(p)

def source_upper(s,q,rho,P,alpha=None):
 if alpha is None:alpha=[1]*len(q)
 ds=[max(0,p-r+1) for p,r in zip(P,rho)]
 s,E,limits,floors=old.projection(s,q,rho)
 if any(h<0 for h in limits):return None
 best={0:0}
 for i,(d,h) in enumerate(zip(s,limits),1):
  scores=[sum(sorted((al*min(e,du) for al,du,qq,rr in zip(alpha,ds,q,rho) if qq>0 and rr>=d),reverse=True)[:d+e]) if d else 0 for e in range(min(E,h)+1)]
  nxt={}
  for total,value in best.items():
   for e in range(min(h,E-total)+1):
    if total+e < floors.get(i,0):continue
    val=value+scores[e]
    nxt[total+e]=max(nxt.get(total+e,-1),val)
  best=nxt
 return best.get(E)

def weighted_lower(q,rho,s,P,alpha=None, exact=False):
 if alpha is None:alpha=[1]*len(q)
 b=len(q);z=s.count(0);v=[al*max(0,qq-z) for qq,al in zip(q,alpha)];c=[qq+r for qq,r in zip(q,rho)]
 best=(0,1,0);hall=False
 for tau in range(1,max(q,default=0)+1):
  demand=sum(x for x in q if x>=tau)
  A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 and (not exact or q[w]<=c[u]) for u in range(b))) for w in range(b)]
  if min(A)<0:return None
  hall |= demand>sum(A)
  f=[min(aa,r-1) for aa,r in zip(A,rho)];g=[aa-ff for aa,ff in zip(A,f)]
  for theta in sorted({0,*v}):
   val=theta*(demand-sum(f))-sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))
   if val>best[0]:best=(val,tau,theta)
 return dict(lower=best[0],tau=best[1],theta=best[2],hall=hall)

if __name__=='__main__':
 from time import monotonic
 start=monotonic();out=[]
 for p in rows:
  s,q,rho=p['s'],p['q'],p['rho'];a,b=p['a'],p['b'];P=old.spill_caps(s,q,rho,old.prior_localized(s,q,rho,old.old_caps(a,s,q,rho)))
  env=old.envelope(s,q,rho,b-a);test=old.priced_lower(q,rho,s,P)
  if old.rejected(test,env):continue
  capenv=source_upper(s,q,rho,P);test2=weighted_lower(q,rho,s,P,exact=True)
  out.append(dict(row=p['row'],oldenv=env,newenv=capenv,lower=test['lower'],exact_lower=test2['lower'],new_reject=test2['hall'] or test2['lower']>capenv))
 print(json.dumps(out,indent=2));print('seconds',monotonic()-start)
 Path('/mnt/data/source_pressure/source_specific_trial.json').write_text(json.dumps(out,indent=2))
