#!/usr/bin/env python3
"""Parallel exact physical-source screen for r=10 partition (2,1^8)."""
import itertools,json,multiprocessing as mp
from functools import lru_cache
R=(2,1,1,1,1,1,1,1,1);k=9
upairs=list(itertools.combinations(range(1,9),2))
def one(line):
 f=list(map(int,line.split()));ug,hs,t=f[:3]
 edges=[upairs[q] for q in range(28) if ug>>q&1]+[(0,i+1) for i in range(8) if hs>>i&1]
 neigh=[set() for _ in R];deg=[0]*k
 for i,j in edges:neigh[i].add(j);neigh[j].add(i);deg[i]+=1;deg[j]+=1
 P={i for i in range(k) if deg[i]>R[i]};need=tuple(max(0,deg[i]-R[i]) for i in range(k));patterns=[]
 for state in itertools.product(range(3),repeat=k):
  L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
  if not Z or any(not neigh[i]<=L|Z or len(neigh[i]&L)>R[i] for i in L):continue
  patterns.append((tuple(int(i in Z) for i in range(k)),tuple(int(i in L) for i in range(k)),state))
 @lru_cache(None)
 def solve(rem,x):
  if not any(rem):return () if all(x[i]>=need[i] for i in range(k)) else None
  for q,(z,l,state) in enumerate(patterns):
   if all(z[i]<=rem[i] for i in range(k)):
    tail=solve(tuple(rem[i]-z[i] for i in range(k)),tuple(min(need[i],x[i]+l[i]) for i in range(k)))
    if tail is not None:return (q,)+tail
  return None
 w=solve(R,(0,)*k)
 return None if w is None else {'unit_mask':ug,'heavy_neighbour_mask':hs,'t_upper':t,'edges':edges,
  'degrees':deg,'P':sorted(P),'need':need,'patterns':len(patterns),'states':solve.cache_info().currsize,
  'witness':[patterns[q][2] for q in w]}
if __name__=='__main__':
 lines=open('r10_211111111_masks.txt').read().splitlines()
 with mp.Pool(6) as pool: rows=[r for r in pool.imap_unordered(one,lines) if r is not None]
 print(json.dumps({'R':R,'core_orbits':len(lines),'source_feasible':len(rows),
  'rows':sorted(rows,key=lambda x:(x['unit_mask'],x['heavy_neighbour_mask'])),
  'scope':'Exact physical-source necessary condition; not graph realization.'},indent=2))
