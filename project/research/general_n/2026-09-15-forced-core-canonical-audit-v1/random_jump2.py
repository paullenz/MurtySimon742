from pathlib import Path
import csv,random,collections
BASE=Path('/mnt/data/ms742scan')
lines=[x.strip() for x in Path('/mnt/data/ms742scan/localplan/TARGET_INPUT.txt').read_text().splitlines() if x.strip()]
states={};raw={}
for line in lines[1:]:
 z=list(map(int,line.split()));layer,sid,a,b,t=z[:5];ns=z[5];s=z[6:6+ns];j=6+ns;nr=z[j];rho=z[j+1:j+1+nr]
 states[(layer,sid)]=(a,b,t,s,rho);raw[(layer,sid)]=line
rows={}
for r in csv.DictReader(open('/mnt/data/ms742scan/final/POST_PAIR_RELATIONAL_FULL_FINAL_RESULTS.tsv'),delimiter='\t'):
 k=(int(r['layer']),int(r['state_id']))
 if k in states: rows[k]=tuple(map(int,r['witness_q'].split(',')))
known=set()
for fn in ['RESCUE_WITNESSES.tsv','BFS_RESCUES.tsv']:
 for r in csv.DictReader(open(BASE/fn),delimiter='\t'):known.add((int(r['layer']),int(r['state_id'])))
for sid in [2548,10067,10210,11079,10043,9013,9552,6103]: known.add((0,sid))
unres=[k for k in states if k not in known]
print('unresolved',len(unres))
R=random.Random(742150927)

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

PER=3500
cands=[]
for ix,k in enumerate(unres):
 q0=rows[k];qmax,groups=setup(k);pool=set();attempts=0
 while len(pool)<PER and attempts<PER*60:
  attempts+=1
  # mix mutation-based and direct classwise random perturbations
  if R.random()<0.78:
   q=list(q0);steps=R.randint(3,35)
   for _ in range(steps):
    u=R.random()
    if u<0.67:
     dec=[i for i,x in enumerate(q) if x>0];inc=[j for j,x in enumerate(q) if x<qmax[j]]
     if dec and inc:
      i=R.choice(dec);j=R.choice(inc)
      if i!=j:q[i]-=1;q[j]+=1
    elif u<0.835:
     inc=[j for j,x in enumerate(q) if x<qmax[j]]
     if inc:q[R.choice(inc)]+=1
    else:
     dec=[i for i,x in enumerate(q) if x>0]
     if dec:q[R.choice(dec)]-=1
  else:
   # perturb each equal-rho class around its old mean, preserving sorted canonical form
   q=list(q0)
   for lo,hi in groups:
    if R.random()<0.7:
     for i in range(lo,hi):
      delta=R.randint(-3,3)
      q[i]=max(0,min(qmax[i],q[i]+delta))
  qq=canon(q,groups)
  if qq!=q0:pool.add(qq)
 for qq in pool:cands.append((k,qq))
 if (ix+1)%25==0: print('generated',ix+1,len(cands))
out=BASE/'random_jump2.txt'
with out.open('w') as f:
 f.write(str(len(cands))+'\n')
 for cid,(k,q) in enumerate(cands):
  a,b,t,s,rho=states[k]
  f.write(' '.join(map(str,[k[0],k[1],cid,a,b,t,len(s),*s,len(rho),*rho,len(q),*q]))+'\n')
print('candidates',len(cands),'fileMB',out.stat().st_size/1e6)
