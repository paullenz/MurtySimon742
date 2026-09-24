"""Executable local review of finite premises; not an all-order graph proof."""
from pathlib import Path
import itertools as it,json,hashlib,collections,functools,time
import networkx as nx
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

# Independent cover search: branch on an uncovered edge, not on successive
# certificate types as in the preserved labelled-graph DP.
def star_cover(n, es):
 edges=list(it.combinations(range(n),2));edgeidx={e:i for i,e in enumerate(edges)}
 graph=sum(1<<edgeidx[tuple(sorted(e))] for e in es);adj=[0]*n
 for a,b in es:adj[a]|=1<<b;adj[b]|=1<<a
 covers={}
 for s in range(1,(1<<n)-1):
  cover=0
  for a,b in es:
   if (s>>a&1) != (s>>b&1):
    absent=b if s>>a&1 else a
    if (adj[absent]&s).bit_count()==1:cover|=1<<edgeidx[tuple(sorted((a,b))) ]
  if cover:covers[cover]=min(covers.get(cover,99),n-s.bit_count())
 byedge={i:[] for i in range(len(edges)) if graph>>i&1}
 for mask,cost in covers.items():
  for i in byedge:
   if mask>>i&1:byedge[i].append((mask,cost))
 @functools.lru_cache(None)
 def solve(rem):
  if not rem:return 0
  bit=min((i for i in byedge if rem>>i&1),key=lambda i:len(byedge[i]))
  return min(cost+solve(rem&~mask) for mask,cost in byedge[bit])
 return 2*(len(edges)-len(es))+solve(graph)
small=[]
for n in (3,4,5):
 es=list(it.combinations(range(n),2));vals=[]
 for mask in range(1<<len(es)):vals.append(star_cover(n,[e for j,e in enumerate(es) if mask>>j&1]))
 small.append({'x':n,'labelled_graphs':len(vals),'minimum':min(vals),'minimizers':vals.count(min(vals))})
result['independent_labelled_star_cover']=small
atlas=[]
for n in (6,7):
 vals=[star_cover(n,list(g.edges())) for g in nx.graph_atlas_g() if len(g)==n]
 atlas.append({'x':n,'unlabelled_graphs':len(vals),'minimum':min(vals),'minimizers':vals.count(min(vals))})
result['independent_atlas_star_cover']=atlas

# Exact integer budget checks; U is a shared right-endpoint deficit sum.
result['deficit_bounds']={
 'index1_min_total':min(p+q+max(0,73-9*p,45-6*q)+8 for p in range(10) for q in range(7)),
 'index2_two_singletons_min_total':min(p+q+max(0,73-9*p,58-7*q)+12-min(2,9-p)-min(2,8-q) for p in range(3,10) for q in range(2,9)),
 'index2_hard_min_total':min(p+q+max(4,73-9*p,58-7*q)+3+6-min(1,9-p)-min(1,8-q) for p in range(3,10) for q in range(2,9)),
 'n18_50740_feasible_center_pairs':[(p,q) for p in range(9) for q in range(9) if p+q<=16 and 8*p+(16-p-q)>=59 and 8*q+(16-p-q)>=59]}

# Enumerate every relevant index2 B-skeleton up to permutation of the seven
# outer vertices when choosing the omitted endpoint. Unspecified outer-outer
# edges and inactive-A incidences can only add alternate common neighbours.
C0={1,2};C1={1,3,4};V=set(range(1,12));corepairs=list(it.combinations(range(1,5),2));outer=list(range(5,12))
def forced_singletons(adj):
 result=set()
 for i in range(1,5):
  if not adj[i]:continue
  blocked=all(bool(adj[i]&adj[j]) or (i in C0 and j in C0) or (i in C1 and j in C1) for j in V-{i}-adj[i])
  if blocked:result.add(i)
 return result
classes=collections.Counter();hard=[];bad=[]
for omitted in (2,5):
 for bits in range(64):
  e={e for j,e in enumerate(corepairs) if bits>>j&1}
  def has(a,b):return tuple(sorted((a,b))) in e
  if any(has(1,j)+has(2,j)!=1 for j in (3,4)):continue
  if omitted!=2 and (not has(1,2) or has(2,3) or has(2,4)):continue
  patterns=[]
  for t in outer:
   patterns.append([set(s) for z in range(16) if len((s:=[i+1 for i in range(4) if z>>i&1]))>=0 and len(set(s)&C0)==1 and (t==omitted or (len(set(s)&C1)==1 and (set(s)&C0)!=(set(s)&C1)))])
  for choice in it.product(*patterns):
   adj={i:set() for i in V}
   for a,b in e:adj[a].add(b);adj[b].add(a)
   for t,s in zip(outer,choice):
    for a in s:adj[t].add(a);adj[a].add(t)
   f=forced_singletons(adj);classes[(omitted,len(f))]+=1
   if len(f)<2:
    # These must be precisely the two symmetric hard patterns of the note.
    if omitted!=2 or len(f)!=1:bad.append({'omitted':omitted,'edges':sorted(e),'forced':sorted(f)});continue
    w=next(iter(f));other=7-w
    ok=w in (3,4) and e=={tuple(sorted((1,other))),tuple(sorted((2,w)))} and all(s=={2,w} for s in choice)
    if not ok:bad.append({'omitted':omitted,'edges':sorted(e),'forced':sorted(f)})
    else:hard.append({'forced_singleton':w,'edges':sorted(e),'outer_neighbours':[2,w]})
result['index2_skeleton_casecheck']={'counts':{f'omitted_{k[0]}_forced_{k[1]}':v for k,v in classes.items()},'hard_cases':hard,'uncovered_skeletons':bad,'scope':'all relevant core-outer skeletons; not all 19-vertex graphs. Free edges can only strengthen alternate-path obstruction.'}
assert not bad
if args.output:
 Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
