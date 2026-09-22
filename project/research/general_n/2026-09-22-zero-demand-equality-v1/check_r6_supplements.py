#!/usr/bin/env python3
"""Necessary selected-supplement edge feasibility for r=6 equality kernels."""
import json
from pathlib import Path
data=json.loads(Path('R6_EQUALITY_SOURCE_SCREEN.json').read_text());out={}
for key,entry in data.items():
    survivors=[];tested=entry['surviving_source_multisets']
    # Only first three were stored; rerun enumeration is needed for entries
    # with more survivors, so import the source generator logic by reproducing
    # the finite state recursion here.
    R=tuple(entry['R']);k=len(R);edges=[tuple(e) for e in entry['edges']]
    neighbors=[set() for _ in R]
    for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
    P=set(entry['P']);need=tuple(entry['selected_lower_bounds']);patterns=[]
    import itertools
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
        valid=not any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L)
        if not valid or not Z:continue
        patterns.append((tuple(int(i in Z) for i in range(k)),tuple(int(i in L) for i in range(k)),state))
    populations=[]
    def search(start,remaining,x,chosen):
        if not any(remaining):
            if all(x[i]>=need[i] for i in range(k)):populations.append(tuple(chosen))
            return
        for j in range(start,len(patterns)):
            z,l,state=patterns[j]
            if all(z[i]<=remaining[i] for i in range(k)):
                search(j,tuple(remaining[i]-z[i] for i in range(k)),
                       tuple(x[i]+l[i] for i in range(k)),chosen+[state])
    search(0,R,tuple(0 for _ in R),[])
    assert len(populations)==tested
    for pop in populations:
        L=[{i for i,s in enumerate(state) if s==1} for state in pop]
        uncovered=[]
        for u in range(len(pop)):
            for i in L[u]:
                # A fresh universal source can supplement only when it would
                # be common to exactly this one selected label at u.
                possible=len(L[u])==1
                for w in range(len(pop)):
                    if w==u:continue
                    forced={(u,j) for j in L[u] if pop[w][j]==0}
                    forced|={(w,j) for j in L[w] if pop[u][j]==0}
                    if forced=={(u,i)}:possible=True
                if not possible:uncovered.append((u,i))
        if not uncovered:survivors.append(pop)
    out[key]={'source_multisets_tested':tested,'supplement_feasible':len(survivors),
      'first_survivors':survivors[:3],
      'test':'Every selected incidence has an active B-edge forcing exactly that incidence, or a universal supplement when its source has one selected label.',
      'scope':'Necessary B-layer condition only; candidate edges are not jointly checked for A-common-neighbour uniqueness or D2C realization.'}
print(json.dumps(out,indent=2))
