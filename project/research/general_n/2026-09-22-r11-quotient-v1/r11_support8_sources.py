#!/usr/bin/env python3
"""Parallel exact physical-source screen for r=11 support-eight strict cores."""
import itertools,json,multiprocessing as mp
from functools import lru_cache
pairs=list(itertools.combinations(range(8),2))
def one(line):
 f=list(map(int,line.split()));case,mask,t=f[:3];R=tuple(f[3:11]);k=8
 edges=[pairs[q] for q in range(28) if mask>>q&1];neigh=[set() for _ in R];deg=[0]*k
 for i,j in edges:neigh[i].add(j);neigh[j].add(i);deg[i]+=1;deg[j]+=1
 need=tuple(max(0,deg[i]-R[i]) for i in range(k));patterns=[]
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
 return None if w is None else {'case':case,'mask':mask,'R':R,'t_upper':t,'edges':edges,'degrees':deg,
  'need':need,'patterns':len(patterns),'states':solve.cache_info().currsize,'witness':[patterns[q][2] for q in w]}
if __name__=='__main__':
 lines=open('r11_support8_masks.txt').read().splitlines()
 with mp.Pool(8) as pool:rows=[r for r in pool.imap_unordered(one,lines,chunksize=2) if r is not None]
 counts={str(i):sum(r['case']==i for r in rows) for i in range(3)}
 print(json.dumps({'core_orbits':len(lines),'source_feasible':len(rows),'source_feasible_by_case':counts,
  'rows':sorted(rows,key=lambda x:(x['case'],x['mask'],x['R'])),
  'scope':'Exact physical-source necessary condition; not graph realization.'},indent=2))
