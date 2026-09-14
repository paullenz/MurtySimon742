import json
import verify_block_pressure as b
import verify_capped_spill as c
from collections import Counter
rs=json.load(open('/mnt/data/work/REMAINDER_12.json'))['rows']
p=next(p for p in rs if p['row']==295)
s,q,rho=p['s'],p['q'],p['rho'];P=c.spill_caps(s,q,rho,c.prior_localized(s,q,rho,c.old_caps(p['a'],s,q,rho)))
print(json.dumps(p,indent=2));print('P',P, 'D', [max(0,p-r+1) for p,r in zip(P,rho)])
print('labels',Counter(s),'sources', Counter(zip(q,rho,P)))
for name,alpha in [('uniform',[1]*len(q)),('three_above_q2',[1 if qq<=2 else 3 for qq in q])]:
 for eta in sorted({0,*s}):
  if eta>=max(s):continue
  upper=b.dp_upper(s,q,rho,P,eta,alpha);lower=b.best_lower(q,rho,s,P,eta,alpha)
  print(name,eta,'upper',upper,lower,'gap',lower['lower']-upper)
ss,E,lim,flo=b.projection(s,q,rho);tab=b.scores(ss,q,rho,P,0,[1]*len(q),E,lim)
best={0:(0,[])}
for i,(h,ts) in enumerate(zip(lim,tab),1):
 nxt={}
 for used,(val,path) in best.items():
  for e in range(min(h,E-used)+1):
   j=used+e
   if j < flo.get(i,0):continue
   if j not in nxt or val+ts[e]>nxt[j][0]:nxt[j]=(val+ts[e],path+[e])
 best=nxt
print('one max',best[E]);print('scores',[(si,ei,tab[i][ei]) for i,(si,ei) in enumerate(zip(s,best[E][1]))]); print('floors',flo)
# True singleton lower bounds from all sources.
xlo=[sum(qq==sum(d<=r for d in s) and qq>0 and di<=r for qq,r in zip(q,rho)) for di in s]
elo=[max(0,lo-d) for lo,d in zip(xlo,s)];print('xlo',xlo,'elo',elo)
best={0:(0,[])}
for i,(h,ts,lo) in enumerate(zip(lim,tab,elo),1):
 nxt={}
 for used,(val,path) in best.items():
  for e in range(lo,min(h,E-used)+1):
   j=used+e
   if j<flo.get(i,0):continue
   if j not in nxt or val+ts[e]>nxt[j][0]:nxt[j]=(val+ts[e],path+[e])
 best=nxt
print('improved max',best.get(E))
