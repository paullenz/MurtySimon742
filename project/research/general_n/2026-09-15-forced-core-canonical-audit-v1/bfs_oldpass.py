from pathlib import Path
import csv,subprocess,tempfile,collections,random
BASE=Path('/mnt/data/ms742scan')
# parse states
lines=[x.strip() for x in Path('/mnt/data/canonical_plan/TARGET_INPUT.txt').read_text().splitlines() if x.strip()];states={}
for line in lines[1:]:
 z=list(map(int,line.split()));layer,sid,a,b,t=z[:5];ns=z[5];s=z[6:6+ns];j=6+ns;nr=z[j];rho=z[j+1:j+1+nr];states[(layer,sid)]=(a,b,t,s,rho)
rows={}
for r in csv.DictReader(open('/mnt/data/ms742scan/final/POST_PAIR_RELATIONAL_FULL_FINAL_RESULTS.tsv'),delimiter='\t'):
 k=(int(r['layer']),int(r['state_id']))
 if k in states: rows[k]=tuple(map(int,r['witness_q'].split(',')))
resc=set()
for fn in ['neigh1_out.tsv','neigh2_out.tsv','random_rescue_out.tsv']:
 for r in csv.DictReader(open(BASE/fn),delimiter='\t'):
  if r.get('pass')=='1':resc.add((int(r['layer']),int(r['state_id'])))
unres=[k for k in states if k not in resc]
print('start unresolved',len(unres))

def setup(k):
 a,b,t,s,rho=states[k]; qmax=[max(0,min(a-r,sum(d<=r for d in s))) for r in rho]; groups=[];lo=0
 while lo<len(rho):
  hi=lo+1
  while hi<len(rho) and rho[hi]==rho[lo]:hi+=1
  groups.append((lo,hi));lo=hi
 return qmax,groups
setups={k:setup(k) for k in unres}
def neigh(q,qmax,groups):
 n=len(q)
 for i in range(n):
  if q[i]<=0:continue
  for j in range(n):
   if i==j or q[j]>=qmax[j]:continue
   x=list(q);x[i]-=1;x[j]+=1
   for lo,hi in groups:x[lo:hi]=sorted(x[lo:hi])
   yield tuple(x)
front={k:{rows[k]} for k in unres}; seen={k:{rows[k]} for k in unres};found={}
R=random.Random(1509)
for depth in range(1,16):
 cand=[]
 for k in list(front):
  if k in found:continue
  qmax,groups=setups[k];pool=set()
  for q in front[k]:
   for x in neigh(q,qmax,groups):
    if x not in seen[k]:pool.add(x)
  # cap huge front expansion deterministically/randomly
  arr=sorted(pool)
  if len(arr)>1500:
   R.shuffle(arr);arr=arr[:1500]
  for x in arr:seen[k].add(x)
  for x in arr:cand.append((k,x))
 print('depth',depth,'candidates',len(cand),'active',sum(1 for k in front if k not in found and front.get(k)))
 if not cand:break
 inp=BASE/f'bfs_d{depth}.txt';outp=BASE/f'bfs_d{depth}_out.tsv'
 with inp.open('w') as f:
  f.write(str(len(cand))+'\n')
  for cid,(k,q) in enumerate(cand):
   a,b,t,s,rho=states[k];f.write(' '.join(map(str,[k[0],k[1],cid,a,b,t,len(s),*s,len(rho),*rho,len(q),*q]))+'\n')
 subprocess.run([str(BASE/'stages'),str(inp),str(outp)],check=True)
 newfront={k:set() for k in unres if k not in found}
 stats=collections.Counter()
 rr=list(csv.DictReader(open(outp),delimiter='\t'))
 assert len(rr)==len(cand)
 for cid,r in enumerate(rr):
  k,q=cand[cid]
  old=r['oldpass']=='1';core=r['corepass']=='1';stats[(old,core,int(r['stage']))]+=1
  if old and core and k not in found:found[k]=q
  elif old and not core and k not in found:newfront[k].add(q)
 # beam oldpass/corefail only, cap 250 each
 for k,qs in newfront.items():
  arr=sorted(qs)
  if len(arr)>250: arr=arr[:250]
  newfront[k]=set(arr)
 front=newfront
 print(' found this/total',sum(1 for k in found if k in states),len(found),'old-corefail frontier',sum(len(x) for x in front.values()),'stats',stats.most_common(6))
 if len(found)==len(unres):break
# write witnesses
with (BASE/'BFS_RESCUES.tsv').open('w') as f:
 f.write('layer\tstate_id\twitness_q\n')
 for k,q in sorted(found.items()):f.write(f'{k[0]}\t{k[1]}\t'+','.join(map(str,q))+'\n')
print('FINAL NEW RESCUES',len(found))
