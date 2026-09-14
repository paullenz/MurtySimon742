from weighted_trial import *
import numpy as np
from scipy.optimize import linprog

def dual_oracle(p,P,eta,alpha,gamma,scale=1,trace=False):
 s,q,rho=p['s'],p['q'],p['rho'];b=len(q);dmax=[max(0,pp-r+1) for pp,r in zip(P,rho)]
 ss,E,limits,floors=old.projection(s,q,rho);best={0:(0,[])};sources=[];scores=[]
 for d,h in zip(ss,limits):
  by_e=[];sc=[]
  for e in range(min(E,h)+1):
   vals=sorted(((scale*al*min(e,du) * (d>eta)-g,u) for u,(al,du,g,qq,r) in enumerate(zip(alpha,dmax,gamma,q,rho)) if qq>0 and r>=d),reverse=True)
   selected=vals[:d+e]
   by_e.append([u for _,u in selected]);sc.append(sum(v for v,_ in selected))
  sources.append(by_e);scores.append(sc)
 for i,(d,h,sc) in enumerate(zip(ss,limits,scores),1):
  nxt={}
  for total,(value,es) in best.items():
   for e in range(min(h,E-total)+1):
    if total+e<floors.get(i,0):continue
    val=value+sc[e]
    if total+e not in nxt or val>nxt[total+e][0]:nxt[total+e]=(val,es+[e])
  best=nxt
 if E not in best:return None
 val,es=best[E];usage=[0]*b;raw=0
 for d,e,by_e in zip(ss,es,sources):
  for u in by_e[e]:usage[u]+=1;raw+=scale*alpha[u]*min(e,dmax[u])*(d>eta)
 upper=val+sum(g*qq for g,qq in zip(gamma,q))
 return dict(upper=upper,usage=usage,raw=raw,e=es) if trace else upper

def optimize(p,P,eta,alpha,iters=100):
 b=len(P);q=np.array(p['q']);gamma=np.zeros(b);cuts=[];best=None
 lower=test(p,P,eta,alpha);seen=set()
 for step in range(iters):
  oracle=dual_oracle(p,P,eta,alpha,list(gamma),trace=True)
  # exact rounded certificate on integer 64 grid
  g=[round(x*64) for x in gamma];ex=dual_oracle(p,P,eta,alpha,g,scale=64)
  if best is None or ex<best['upper_scaled']:
   best=dict(lower,upper_scaled=ex,scale=64,gamma=g,gap_scaled=64*lower['lower']-ex,iterations=step+1)
  if best['gap_scaled']>0:break
  counts=tuple(oracle['usage']);raw=oracle['raw'];key=(counts,raw)
  if key in seen:break
  seen.add(key);cuts.append((counts,raw))
  A=[list(q-np.array(count))+[-1] for count,_ in cuts];bb=[-rr for _,rr in cuts]
  obj=[0]*b+[1]
  res=linprog(obj,A_ub=np.array(A),b_ub=np.array(bb),bounds=[(-100,100)]*b+[(None,None)],method='highs')
  if not res.success:break
  gamma=res.x[:-1]
 return best
if __name__=='__main__':
 results=[]
 for row in [108,160,240,258,295,338,342,347,365,471,570,586]:
  p=rows[row];s,q,rho=p['s'],p['q'],p['rho'];P=old.spill_caps(s,q,rho,old.prior_localized(s,q,rho,old.old_caps(p['a'],s,q,rho)))
  best=None
  for eta in sorted({0,*s}):
   if eta>=max(s):continue
   d=optimize(p,P,eta,[1]*len(q),60)
   if best is None or d['gap_scaled']>best['gap_scaled']:best=d
   if d['gap_scaled']>0:break
  results.append(dict(row=row,best=best));print(row,best,flush=True)
  Path('/mnt/data/source_pressure/dual_trials.json').write_text(json.dumps(results,indent=2))
