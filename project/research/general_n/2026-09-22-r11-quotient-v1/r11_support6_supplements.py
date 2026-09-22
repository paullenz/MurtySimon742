#!/usr/bin/env python3
"""Exact source-population and supplement forcing for four r=11 support-six kernels."""
import itertools,json
R=(3,2,2,2,1,1);pairs=list(itertools.combinations(range(6),2));MASKS=(15870,16352,16360,16376)
def run(mask):
 edges=[pairs[q] for q in range(15) if mask>>q&1];k=6;neigh=[set() for _ in R];deg=[0]*k
 for i,j in edges:neigh[i].add(j);neigh[j].add(i);deg[i]+=1;deg[j]+=1
 P={i for i in range(k) if deg[i]>R[i]};need=tuple(max(0,deg[i]-R[i]) for i in range(k));patterns=[]
 for state in itertools.product(range(3),repeat=k):
  L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
  if not Z or any(not neigh[i]<=L|Z or len(neigh[i]&L)>R[i] for i in L):continue
  patterns.append((tuple(int(i in Z) for i in range(k)),tuple(int(i in L) for i in range(k)),state))
 pops=[]
 def search(start,rem,x,chosen):
  if not any(rem):
   if all(x[i]>=need[i] for i in range(k)):pops.append(tuple(chosen))
   return
  for q in range(start,len(patterns)):
   z,l,state=patterns[q]
   if all(z[i]<=rem[i] for i in range(k)):
    search(q,tuple(rem[i]-z[i] for i in range(k)),tuple(x[i]+l[i] for i in range(k)),chosen+[state])
 search(0,R,(0,)*k,[])
 def supp_ok(pop):
  L=[{i for i,s in enumerate(st) if s==1} for st in pop]
  for u in range(len(pop)):
   for i in L[u]:
    possible=len(L[u])==1
    for w in range(len(pop)):
     if w==u:continue
     forced={(u,j) for j in L[u] if pop[w][j]==0}|{(w,j) for j in L[w] if pop[u][j]==0}
     possible |= forced=={(u,i)}
    if not possible:return False
  return True
 survivors=[p for p in pops if supp_ok(p)]
 return {'mask':mask,'R':R,'edges':edges,'degrees':deg,'P':sorted(P),'need':need,'patterns':len(patterns),
  'source_multisets':len(pops),'supplement_feasible':len(survivors),
  'source_examples':pops[:10],'supplement_examples':survivors[:10]}
print(json.dumps({str(m):run(m) for m in MASKS},indent=2))
