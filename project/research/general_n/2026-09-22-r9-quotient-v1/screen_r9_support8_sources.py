#!/usr/bin/env python3
"""Exact physical-source feasibility for the r=9 support-eight core orbits."""
import itertools, json
from functools import lru_cache
R=(2,1,1,1,1,1,1,1);k=8
pairs=list(itertools.combinations(range(k),2))
rows=[]
for line in open("r9_support8_masks.txt"):
    fields=list(map(int,line.split()));mask,t=fields[:2]
    edges=[pairs[q] for q in range(len(pairs)) if mask>>q&1]
    neighbors=[set() for _ in R];deg=[0]*k
    for i,j in edges:neighbors[i].add(j);neighbors[j].add(i);deg[i]+=1;deg[j]+=1
    P={i for i in range(k) if deg[i]>R[i]}
    need=tuple(max(0,deg[i]-R[i]) for i in range(k))
    patterns=[]
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
        if any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L):continue
        if not Z:
            if L&P:continue
            continue
        patterns.append((tuple(int(i in Z) for i in range(k)),
                         tuple(int(i in L) for i in range(k)),state))
    @lru_cache(None)
    def solve(rem,x):
        if not any(rem):return () if all(x[i]>=need[i] for i in range(k)) else None
        for q,(z,l,state) in enumerate(patterns):
            if all(z[i]<=rem[i] for i in range(k)):
                tail=solve(tuple(rem[i]-z[i] for i in range(k)),
                           tuple(min(need[i],x[i]+l[i]) for i in range(k)))
                if tail is not None:return (q,)+tail
        return None
    w=solve(R,(0,)*k)
    if w is not None:
        rows.append({'mask':mask,'t_upper':t,'edges':edges,'degrees':deg,'P':sorted(P),
                     'need':need,'patterns':len(patterns),'states':solve.cache_info().currsize,
                     'witness':[patterns[q][2] for q in w]})
print(json.dumps({'R':R,'core_orbits':69,'source_feasible':len(rows),'rows':rows,
 'scope':'Exact physical-source necessary condition on colour-preserving core orbits; not graph realization.'},indent=2))
