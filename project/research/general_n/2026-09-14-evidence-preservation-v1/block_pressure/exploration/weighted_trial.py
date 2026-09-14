from block_trial import *

def all_alpha(p,P):
 b=len(p['q']);q,rho=p['q'],p['rho'];ds=[max(0,pp-r+1) for pp,r in zip(P,rho)];seen=set()
 yield ('uniform',[1]*b)
 for name,v in [('q',q),('rho',rho),('pressure',ds)]:
  for h in sorted(set(v)):
   for low,high in [(0,1),(1,0),(1,2),(2,1),(1,3),(3,1)]:
    alpha=tuple(low if x<=h else high for x in v)
    if alpha in seen or not any(alpha):continue
    seen.add(alpha);yield (f'{name}<={h}:{low}/{high}',list(alpha))

def test(p,P,eta,alpha):
 q,rho,s=p['q'],p['rho'],p['s'];b=len(q);ds=[max(0,pp-r+1) for pp,r in zip(P,rho)]
 ss,E,limits,floors=old.projection(s,q,rho);best={0:0}
 for i,(d,h) in enumerate(zip(ss,limits),1):
  scores=[sum(sorted((al*min(e,du) for al,du,qq,rr in zip(alpha,ds,q,rho) if qq>0 and rr>=d),reverse=True)[:d+e]) if d>eta else 0 for e in range(min(E,h)+1)]
  nxt={}
  for total,value in best.items():
   for e in range(min(h,E-total)+1):
    if total+e<floors.get(i,0):continue
    val=value+scores[e]
    if val>nxt.get(total+e,-1):nxt[total+e]=val
  best=nxt
 upper=best.get(E);m=sum(d<=eta for d in s);v=[al*max(0,qq-m) for al,qq in zip(alpha,q)]
 c=[qq+r for qq,r in zip(q,rho)];res=(0,1,0)
 for tau in range(1,max(q)+1):
  demand=sum(qq for qq in q if qq>=tau)
  A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 and q[w]<=c[u] for u in range(b))) for w in range(b)]
  f=[min(aa,r-1) for aa,r in zip(A,rho)];g=[aa-ff for aa,ff in zip(A,f)]
  for theta in sorted({0,*v}):
   val=theta*(demand-sum(f))-sum(max(0,theta-vv)*gg for vv,gg in zip(v,g))
   if val>res[0]:res=(val,tau,theta)
 return dict(eta=eta,upper=upper,lower=res[0],tau=res[1],theta=res[2],gap=res[0]-upper,alpha=alpha)
if __name__=='__main__':
 results=[]
 previous={x['row']:x['best'] for x in json.loads(Path('/mnt/data/source_pressure/block_trials.json').read_text())}
 for row in previous:
  p=rows[row];s,q,rho=p['s'],p['q'],p['rho'];P=old.spill_caps(s,q,rho,old.prior_localized(s,q,rho,old.old_caps(p['a'],s,q,rho)))
  # Focus the genuinely remaining thirteen; old six certificates already frozen.
  if previous[row]['gap']>0:continue
  best=None;trials=0
  for eta in sorted({0,*s}):
   if eta>=max(s):continue
   for name,alpha in all_alpha(p,P):
    d=test(p,P,eta,alpha);trials+=1
    if best is None or d['gap']>best['gap']:best=dict(d,rule=name)
  results.append(dict(row=row,best=best,trials=trials));print(row,best,flush=True)
  Path('/mnt/data/source_pressure/weighted_trials.json').write_text(json.dumps(results,indent=2))
