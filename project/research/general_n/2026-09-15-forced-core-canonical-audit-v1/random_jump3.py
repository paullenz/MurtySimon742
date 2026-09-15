from pathlib import Path
import csv,random
BASE=Path('/mnt/data/ms742scan')
lines=[x.strip() for x in (BASE/'localplan/TARGET_INPUT.txt').read_text().splitlines() if x.strip()]
states={}
for line in lines[1:]:
 z=list(map(int,line.split()));layer,sid,a,b,t=z[:5];ns=z[5];s=z[6:6+ns];j=6+ns;nr=z[j];rho=z[j+1:j+1+nr]
 states[(layer,sid)]=(a,b,t,s,rho)
rows={}
for r in csv.DictReader(open(BASE/'final/POST_PAIR_RELATIONAL_FULL_FINAL_RESULTS.tsv'),delimiter='\t'):
 k=(int(r['layer']),int(r['state_id']))
 if k in states: rows[k]=tuple(map(int,r['witness_q'].split(',')))
known=set()
for fn in ['RESCUE_WITNESSES.tsv','BFS_RESCUES.tsv']:
 for r in csv.DictReader(open(BASE/fn),delimiter='\t'):known.add((int(r['layer']),int(r['state_id'])))
for sid in [2548,10067,10210,11079,10043,9013,9552,6103,7611,8281,8732]:known.add((0,sid))
unres=[k for k in states if k not in known]
R=random.Random(742150928)

def setup(k):
 a,b,t,s,rho=states[k];n=len(rho)
 qmax=[max(0,min(a-r,sum(d<=r for d in s))) for r in rho]
 groups=[];lo=0
 while lo<n:
  hi=lo+1
  while hi<n and rho[hi]==rho[lo]:hi+=1
  groups.append((lo,hi));lo=hi
 return qmax,groups

def canon(q,groups):
 q=list(q)
 for lo,hi in groups:q[lo:hi]=sorted(q[lo:hi])
 return tuple(q)

PER=3000
cands=[]
for k in unres:
 q0=rows[k];qmax,groups=setup(k);n=len(q0);pool=set();attempts=0
 while len(pool)<PER and attempts<PER*20:
  attempts+=1;q=list(q0);steps=R.randint(4,50)
  for _ in range(steps):
   u=R.random()
   if u<0.7:
    # attempt transfer with random endpoints
    for __ in range(8):
     i=R.randrange(n);j=R.randrange(n)
     if i!=j and q[i]>0 and q[j]<qmax[j]:q[i]-=1;q[j]+=1;break
   elif u<0.85:
    for __ in range(8):
     j=R.randrange(n)
     if q[j]<qmax[j]:q[j]+=1;break
   else:
    for __ in range(8):
     i=R.randrange(n)
     if q[i]>0:q[i]-=1;break
  qq=canon(q,groups)
  if qq!=q0:pool.add(qq)
 for qq in pool:cands.append((k,qq))
print('unresolved',len(unres),'candidates',len(cands))
out=BASE/'random_jump3.txt'
with out.open('w') as f:
 f.write(str(len(cands))+'\n')
 for cid,(k,q) in enumerate(cands):
  a,b,t,s,rho=states[k]
  f.write(' '.join(map(str,[k[0],k[1],cid,a,b,t,len(s),*s,len(rho),*rho,len(q),*q]))+'\n')
