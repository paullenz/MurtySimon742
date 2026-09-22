#!/usr/bin/env python3
"""Exact r=11 quotient/source screen for residual support at most five."""
import itertools,json
from functools import lru_cache
def parts(n,hi=None):
 if n==0:yield ();return
 for x in range(min(n,hi or n),0,-1):
  for tail in parts(n-x,x):yield (x,)+tail
def perms_for(R):
 groups=[tuple(i for i,x in enumerate(R) if x==v) for v in sorted(set(R),reverse=True)]
 for choices in itertools.product(*(itertools.permutations(g) for g in groups)):
  p=list(range(len(R)))
  for g,image in zip(groups,choices):
   for i,j in zip(g,image):p[i]=j
  yield tuple(p)
def datum(R,pairs,mask):
 k=len(R);deg=[0]*k;neigh=[set() for _ in R];edges=[]
 for q,(i,j) in enumerate(pairs):
  if mask>>q&1:edges.append((i,j));deg[i]+=1;deg[j]+=1;neigh[i].add(j);neigh[j].add(i)
 P={i for i in range(k) if deg[i]>R[i]};N=set(range(k))-P
 if any((deg[i]-R[i])**2>sum(R[j] for j in neigh[i]) for i in P):return None
 eP=sum(i in P and j in P for i,j in edges);eN=sum(i in N and j in N for i,j in edges)
 slack=sum(i in N and R[i]==1 and deg[i]==0 for i in range(k))
 t=eP-eN-sum(R[i] for i in P)-slack
 return None if t<=0 else (edges,deg,neigh,P,t)
def source(R,d):
 edges,deg,neigh,P,t=d;k=len(R);need=tuple(max(0,deg[i]-R[i]) for i in range(k));patterns=[]
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
 return None if w is None else [patterns[q][2] for q in w]
out={}
for R in parts(11):
 k=len(R)
 if k>5:continue
 pairs=list(itertools.combinations(range(k),2));idx={e:q for q,e in enumerate(pairs)};perms=list(perms_for(R));reps={}
 for mask in range(1<<len(pairs)):
  d=datum(R,pairs,mask)
  if d is None:continue
  best=min(sum((1<<idx[tuple(sorted((p[i],p[j])))]) for q,(i,j) in enumerate(pairs) if mask>>q&1) for p in perms)
  if best not in reps:reps[best]=datum(R,pairs,best)
 feasible=[]
 for mask,d in reps.items():
  w=source(R,d)
  if w is not None:feasible.append({'mask':mask,'t_upper':d[4],'edges':d[0],'degrees':d[1],'witness':w})
 out[str(R)]={'support':k,'strict_orbits':len(reps),'source_feasible':len(feasible),'feasible':feasible}
 print(R,len(reps),len(feasible),flush=True)
print(json.dumps(out,indent=2))
