from block_trial import *
from itertools import product

def prep(p):
 s,q,rho=p['s'],p['q'],p['rho'];a,b=p['a'],p['b']
 P=old.spill_caps(s,q,rho,old.prior_localized(s,q,rho,old.old_caps(a,s,q,rho)))
 ds=[max(0,pp-rr+1) for pp,rr in zip(P,rho)];ss,E,limits,floors=old.projection(s,q,rho)
 scores=[[sum(sorted((min(e,du) for du,qq,rr in zip(ds,q,rho) if qq>0 and rr>=d),reverse=True)[:d+e]) if d else 0 for e in range(min(E,h)+1)] for d,h in zip(ss,limits)]
 c=[qq+rr for qq,rr in zip(q,rho)];receiver=[]
 for tau in range(1,max(q)+1):
  demand=sum(qq for qq in q if qq>=tau)
  A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 and q[w]<=c[u] for u in range(b))) for w in range(b)]
  f=[min(aa,r-1) for aa,r in zip(A,rho)];g=[aa-ff for aa,ff in zip(A,f)]
  receiver.append((tau,demand-sum(f),g))
 return P,ss,E,limits,floors,scores,receiver

def weigh(p,pr,betas):
 P,s,E,limits,floors,scores,receivers=pr
 levels=sorted(set([0]+[d for d in s if d<max(s)]))
 W={d:sum(beta for eta,beta in zip(levels,betas) if d>eta) for d in s}
 v=[sum(beta*max(0,qq-s.count(0)-sum(0<d<=eta for d in s)) for eta,beta in zip(levels,betas)) for qq in p['q']]
 best={0:0}
 for i,(d,h,sc) in enumerate(zip(s,limits,scores),1):
  nxt={}
  for total,value in best.items():
   for e in range(min(h,E-total)+1):
    if total+e<floors.get(i,0):continue
    val=value+W[d]*sc[e]
    if val>nxt.get(total+e,-1):nxt[total+e]=val
  best=nxt
 upper=best.get(E)
 res=(0,0,0)
 for tau,demand,g in receivers:
  for theta in sorted(set([0]+v)):
   val=theta*demand-sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))
   if val>res[0]:res=(val,tau,theta)
 return dict(upper=upper,lower=res[0],tau=res[1],theta=res[2],gap=res[0]-upper,levels=levels,beta=list(betas))
if __name__=='__main__':
 results=[]
 remainder=json.loads((root/'data/SYNTHETIC_REMAINDER_19.json').read_text())
 for raw in remainder:
  p=rows[raw['row']];pr=prep(p);levels=sorted(set([0]+[d for d in p['s'] if d<max(p['s'])]));best=None
  for beta in product(range(3),repeat=len(levels)):
   if not any(beta):continue
   d=weigh(p,pr,beta)
   if best is None or d['gap']>best['gap']:best=d
  results.append(dict(row=p['row'],best=best));print(p['row'],best,flush=True)
 Path('/mnt/data/source_pressure/multiblock_trials.json').write_text(json.dumps(results,indent=2))
