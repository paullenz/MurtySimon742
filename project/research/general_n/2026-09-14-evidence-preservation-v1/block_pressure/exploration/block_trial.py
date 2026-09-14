from explore import *

def block_upper(s,q,rho,P,eta):
 ds=[max(0,p-r+1) for p,r in zip(P,rho)]
 s,E,limits,floors=old.projection(s,q,rho)
 best={0:0}
 for i,(d,h) in enumerate(zip(s,limits),1):
  scores=[sum(sorted((min(e,du) for du,qq,rr in zip(ds,q,rho) if qq>0 and rr>=d),reverse=True)[:d+e]) if d>eta else 0 for e in range(min(E,h)+1)]
  nxt={}
  for total,value in best.items():
   for e in range(min(h,E-total)+1):
    if total+e<floors.get(i,0):continue
    nxt[total+e]=max(nxt.get(total+e,-1),value+scores[e])
  best=nxt
 return best.get(E)

def block_lower(q,rho,s,P,eta):
 b=len(q);m=sum(d<=eta for d in s);v=[max(0,qq-m) for qq in q];c=[qq+r for qq,r in zip(q,rho)];best=(0,1,0)
 for tau in range(1,max(q,default=0)+1):
  demand=sum(x for x in q if x>=tau)
  A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 and q[w]<=c[u] for u in range(b))) for w in range(b)]
  f=[min(aa,r-1) for aa,r in zip(A,rho)];g=[aa-ff for aa,ff in zip(A,f)]
  for theta in sorted({0,*v}):
   val=theta*(demand-sum(f))-sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))
   if val>best[0]:best=(val,tau,theta)
 return dict(lower=best[0],tau=best[1],theta=best[2])

if __name__=='__main__':
 out=[]
 for p in rows:
  s,q,rho=p['s'],p['q'],p['rho'];a,b=p['a'],p['b'];P=old.spill_caps(s,q,rho,old.prior_localized(s,q,rho,old.old_caps(a,s,q,rho)))
  env=old.envelope(s,q,rho,b-a);test=old.priced_lower(q,rho,s,P)
  if old.rejected(test,env):continue
  trials=[]
  for eta in sorted({0,*s}):
   env=block_upper(s,q,rho,P,eta);test=block_lower(q,rho,s,P,eta)
   trials.append(dict(eta=eta,upper=env,**test,gap=test['lower']-env))
  out.append(dict(row=p['row'],best=max(trials,key=lambda z:z['gap']),trials=trials))
 print('\n'.join(str((p['row'],p['best'])) for p in out))
 Path('/mnt/data/source_pressure/block_trials.json').write_text(json.dumps(out,indent=2))
