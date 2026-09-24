"""Executable local review of finite premises; not an all-order graph proof."""
from pathlib import Path
import itertools as it,json,hashlib,collections,functools,time
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output')
args=parser.parse_args()
root=Path(__file__).resolve().parents[4]
result={}

def cycle_count(mapping):
 seen=set();n=0
 for i in range(len(mapping)):
  if i in seen:continue
  n+=1;j=i
  while j not in seen:seen.add(j);j=mapping[j]
 return n
perms=list(it.permutations(range(7)))
sums=[]
for n in [7,8]:
 edges=list(it.combinations(range(n),2));idx={e:i for i,e in enumerate(edges)}
 total=0
 for p in perms:
  q=p if n==7 else (0,)+tuple(x+1 for x in p)
  total+=1<<cycle_count([idx[tuple(sorted((q[i],q[j])))] for i,j in edges])
 assert total%len(perms)==0;sums.append(total//len(perms))
result['burnside_counts']=dict(unit_graphs=sums[0],rooted_graphs=sums[1])

p=root/'project/research/general_n/2026-09-22-r9-quotient-v1/R9_SUPPORT8_CORE_MASKS.txt'
rows=[list(map(int,line.split())) for line in p.read_text().splitlines()]
edges=list(it.combinations(range(8),2));idx={e:i for i,e in enumerate(edges)}
maps=[]
for p in perms:
 q=(0,)+tuple(x+1 for x in p)
 maps.append([idx[tuple(sorted((q[i],q[j])))] for i,j in edges])
representatives=set(); ts=collections.Counter()
for row in rows:
 mask,t,*degree=row;indices=[i for i in range(28) if mask>>i&1]
 orbit_min=min(sum(1<<mapping[i] for i in indices) for mapping in maps)
 assert orbit_min not in representatives;representatives.add(orbit_min)
 adj=[set() for _ in range(8)]
 for i in indices:a,b=edges[i];adj[a].add(b);adj[b].add(a)
 assert list(map(len,adj))==degree
 R=[2]+[1]*7;P={i for i in range(8) if degree[i]>R[i]}
 assert all((degree[i]-R[i])**2<=sum(R[j] for j in adj[i]) for i in P)
 value=sum(a in P and b in P for i,(a,b) in enumerate(edges) if mask>>i&1)-sum(a not in P and b not in P for i,(a,b) in enumerate(edges) if mask>>i&1)-sum(R[i] for i in P)-sum(i not in P and R[i]==1 and degree[i]==0 for i in range(8))
 assert value==t and t>0;ts[t]+=1
result['r9_masks']={'checked':len(rows),'colour_inequivalent':len(representatives),'t_upper_counts':dict(ts),'mask_digest_encoding':'ascending decimal masks, one per line, final newline','mask_sha256':hashlib.sha256(('\n'.join(map(str,sorted(r[0] for r in rows)))+'\n').encode()).hexdigest()}

result['implementation_status']='FRESH_RECONSTRUCTION_2026_09_24_NOT_HISTORICAL_RECOVERY'
if args.output:
 Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
