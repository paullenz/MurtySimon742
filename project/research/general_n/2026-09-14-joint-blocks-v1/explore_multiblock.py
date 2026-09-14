import argparse,json,hashlib
from pathlib import Path
import verify_shared_slack as new
from itertools import product
from collections import Counter
from functools import lru_cache


def fullcap(p,levels,nums,es,P):
 q,r=p['q'],p['rho'];D=[max(0,pp-rr+1) for pp,rr in zip(P,r)];out=[]
 for u,qq in enumerate(q):
  ok=[]
  for d in range(D[u]+1):
   count=sum((nn if not v or not d else min(nn,e//d)) for v,nn,e in zip(levels,nums,es) if v<=r[u])
   if count>=qq:ok.append(d)
  if not ok:return None
  out.append(min(P[u],r[u]-1+max(ok)))
 return out

def exact_blocks_upper(p,P,levels,nums,es,eta,alpha):
 q,r=p['q'],p['rho'];D=[max(0,pp-rr+1) for pp,rr in zip(P,r)];total=0
 for v,n,E in zip(levels,nums,es):
  eligible=[u for u in range(len(q)) if q[u] and r[u]>=v];hi=len(eligible)-v
  if hi<0:return None
  score=[sum(sorted((alpha[u]*min(e,D[u]) for u in eligible),reverse=True)[:v+e]) if v>eta else 0 for e in range(min(hi,E)+1)]
  dp={0:0}
  for _ in range(n):
   nd={}
   for used,val in dp.items():
    for e in range(min(hi,E-used)+1):nd[used+e]=max(nd.get(used+e,-1),val+score[e])
   dp=nd
  if E not in dp:return None
  total+=dp[E]
 return total

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--prior',required=True,type=Path);ap.add_argument('--block',required=True,type=Path);ap.add_argument('--remainder',required=True,type=Path);ap.add_argument('--shared-result',required=True,type=Path);args=ap.parse_args()
 prior=new.load_module(args.prior,'multi_prior');block=new.load_module(args.block,'multi_block')
 shared=json.loads(args.shared_result.read_text())
 assert hashlib.sha256(new.canonical(shared)).hexdigest()=='35d4c3c05595102b2a568d986d8bab753059da4a2c59b31689a550aaddb23ce6'
 single={p['row']:p for p in shared['replay']['reports']}
 rows=json.loads(args.remainder.read_text())['rows']
 results=[]
 for p in rows:
  if p['row'] in [240,258,295,342,365,570]:continue
  s,q,r=p['s'],p['q'],p['rho'];levels=sorted(set(s));nums=[s.count(v) for v in levels];P=new.baseline(p,prior)
  ranges=[sp['remaining'] for sp in single[p['row']]['splits']];rep=[];cnt=Counter()
  for cum in product(*ranges):
   full=(0,)+cum+(p['Esel'],);es=[full[i+1]-full[i] for i in range(len(levels))]
   if min(es)<0:continue
   cnt['tuples']+=1
   pc=fullcap(p,levels,nums,es,P)
   if pc is None:cnt['empty_source']+=1;continue
   if sum(pc)<sum(q):cnt['sumcap']+=1;continue
   best=None
   for eta in sorted({0,*levels[:-1]}):
    for alpha in ([1]*len(q),[1 if qq<=2 else 3 for qq in q]):
     up=exact_blocks_upper(p,pc,levels,nums,es,eta,alpha)
     if up is None:best=dict(gap=10**6,kind='empty');break
     low=block.best_lower(q,r,s,pc,eta,alpha)
     if best is None or low['lower']-up>best['gap']:best=dict(gap=low['lower']-up,upper=up,**low)
     if best['gap']>0:break
    if best['gap']>0:break
   if best['gap']>0:cnt['price']+=1
   else:cnt['unrejected']+=1;rep.append(dict(cum=cum,excess=es,best=best,cap=pc))
  results.append(dict(row=p['row'],counts=dict(cnt),unrejected=rep))
 print(json.dumps(results,sort_keys=True,indent=2))
