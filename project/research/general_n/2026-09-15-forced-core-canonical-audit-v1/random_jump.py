from pathlib import Path
import csv,random
BASE=Path('/mnt/data/ms742scan')
# states
lines=[x.strip() for x in Path('/mnt/data/canonical_plan/TARGET_INPUT.txt').read_text().splitlines() if x.strip()]
states={}
rawline={}
for line in lines[1:]:
 z=list(map(int,line.split()));layer,sid,a,b,t=z[:5];ns=z[5];s=z[6:6+ns];j=6+ns;nr=z[j];rho=z[j+1:j+1+nr]
 states[(layer,sid)]=(a,b,t,s,rho);rawline[(layer,sid)]=line
# old witnesses
rows={}
for r in csv.DictReader(open('/mnt/data/discovery/POST_PAIR_RELATIONAL_FULL_FINAL_RESULTS.tsv'),delimiter='\t'):
 k=(int(r['layer']),int(r['state_id']))
 if k in states: rows[k]=tuple(map(int,r['witness_q'].split(',')))
known=set()
for fn in ['RESCUE_WITNESSES.tsv','BFS_RESCUES.tsv']:
 for r in csv.DictReader(open(BASE/fn),delimiter='\t'):known.add((int(r['layer']),int(r['state_id'])))
known.add((0,2548))
unres=[k for k in states if k not in known]
R=random.Random(742150926)

def setup(k):
 a,b,t,s,rho=states[k]
 qmax=[max(0,min(a-r,sum(d<=r for d in s))) for r in rho]
 groups=[];lo=0
 while lo<len(rho):
  hi=lo+1
  while hi<len(rho) and rho[hi]==rho[lo]:hi+=1
  groups.append((lo,hi));lo=hi
 return qmax,groups

def canon(q,groups):
 q=list(q)
 for lo,hi in groups:q[lo:hi]=sorted(q[lo:hi])
 return tuple(q)

PER=1200
cands=[]
for k in unres:
 q0=rows[k];qmax,groups=setup(k);pool=set()
 attempts=0
 while len(pool)<PER and attempts<PER*30:
  attempts+=1;q=list(q0)
  # 70% preserve total by 2-12 unit transfers; 30% allow net E shift via increments/decrements
  steps=R.randint(2,12)
  for _ in range(steps):
   if R.random()<0.78:
    dec=[i for i,x in enumerate(q) if x>0]; inc=[j for j,x in enumerate(q) if x<qmax[j]]
    if not dec or not inc:continue
    i=R.choice(dec);j=R.choice(inc)
    if i==j:continue
    q[i]-=1;q[j]+=1
   else:
    if R.random()<0.5:
     inc=[j for j,x in enumerate(q) if x<qmax[j]]
     if inc:q[R.choice(inc)]+=1
    else:
     dec=[i for i,x in enumerate(q) if x>0]
     if dec:q[R.choice(dec)]-=1
  qq=canon(q,groups)
  if qq!=q0:pool.add(qq)
 for qq in pool:cands.append((k,qq))
print('states',len(unres),'candidates',len(cands))
out=BASE/'random_jump.txt'
with out.open('w') as f:
 f.write(str(len(cands))+'\n')
 for cid,(k,q) in enumerate(cands):
  a,b,t,s,rho=states[k]
  f.write(' '.join(map(str,[k[0],k[1],cid,a,b,t,len(s),*s,len(rho),*rho,len(q),*q]))+'\n')
