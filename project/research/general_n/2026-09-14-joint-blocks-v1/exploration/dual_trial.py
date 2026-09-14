from slack_trial import *
from fractions import Fraction

def dual_tail(p,J,options,tau):
 q,r=p['q'],p['rho'];P=baseline(p);c=[qq+rr for qq,rr in zip(q,r)];n=len(q)
 A=[min(P[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(n))) for w in range(n)]
 free=[min(aa,rr-1) for aa,rr in zip(A,r)];lim=[aa-ff for aa,ff in zip(A,free)]
 oo=[[(d,k) for d,k in opt if d<=ll] for opt,ll in zip(options,lim)]
 prices={Fraction(0)}
 for op in oo:
  for d,k in op:
   for d1,k1 in op:
    if k1>k and d1>=d:prices.add(Fraction(d1-d,k1-k))
 best=None
 for price in sorted(prices):
  rewards=[max(d-price*k for d,k in opt) for opt in oo]
  bd=sum(free)+J*price+sum(rewards)
  if best is None or bd<best[0]:best=(bd,price,rewards)
 dem=sum(qq for qq in q if qq>=tau)
 return dict(tau=tau,demand=dem,upper=str(best[0]),price=str(best[1]),gap=str(dem-best[0]))

for p in rows:
 if p['row'] in [295,365,570]:continue
 report=prior_reports[p['row']]
 bests=[]
 for sp in report['splits']:
  eta=sp['eta'];covered=[];un=[]
  for e in sp['unrejected_e_low']:
   data=branch_data(p,eta,e)
   b=max((dual_tail(p,*data,tau) for tau in range(1,max(p['q'])+1)),key=lambda x:Fraction(x['gap']))
   if Fraction(b['gap'])>0:covered.append(dict(e=e,**b))
   else:un.append(e)
  bests.append(dict(eta=eta,covered=covered,remaining=un))
 print(p['row'],bests,flush=True)
