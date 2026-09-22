#!/usr/bin/env python3
"""Necessary supplement-edge feasibility for r=7 equality kernels."""
import itertools,json
from pathlib import Path
summary=json.loads(Path('R7_EQUALITY_SOURCE_SCREEN.json').read_text());out={}
for key,entry in summary.items():
    if not entry['surviving_source_multisets']:continue
    R=tuple(entry['R']);k=len(R);edges=[tuple(e) for e in entry['edges']]
    neighbors=[set() for _ in R]
    for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
    P=set(entry['P']);need=tuple(entry['selected_lower_bounds']);patterns=[];free=[]
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
        valid=not any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L)
        if not valid:continue
        if not Z:
            assert not (L&P);free.append(state);continue
        patterns.append((tuple(int(i in Z) for i in range(k)),tuple(int(i in L) for i in range(k)),state))
    populations=[]
    def search(start,remaining,x,chosen):
        if not any(remaining):
            if all(x[i]>=need[i] for i in range(k)):populations.append(tuple(chosen))
            return
        for q in range(start,len(patterns)):
            z,l,state=patterns[q]
            if all(z[i]<=remaining[i] for i in range(k)):
                search(q,tuple(remaining[i]-z[i] for i in range(k)),
                       tuple(x[i]+l[i] for i in range(k)),chosen+[state])
    search(0,R,tuple(0 for _ in R),[])
    assert len(populations)==entry['surviving_source_multisets']
    survivors=[]
    def forced_between(state_u,u_id,state_w,w_id):
        Lu={i for i,s in enumerate(state_u) if s==1}
        Lw={i for i,s in enumerate(state_w) if s==1}
        forced={(u_id,i) for i in Lu if state_w[i]==0}
        forced|={(w_id,j) for j in Lw if state_u[j]==0}
        return forced
    for pop in populations:
        L=[{i for i,s in enumerate(state) if s==1} for state in pop];uncovered=[]
        for u,state_u in enumerate(pop):
            for i in L[u]:
                possible=False
                for w,state_w in enumerate(pop):
                    if w!=u and forced_between(state_u,u,state_w,w)=={(u,i)}:possible=True
                # An arbitrary fresh residual-free source of any valid N-state
                # may be used. Its own selected incidences are optimistically
                # left for other edges.
                for q,state_w in enumerate(free):
                    if forced_between(state_u,u,state_w,('free',q))=={(u,i)}:possible=True
                if not possible:uncovered.append((u,i))
        if not uncovered:survivors.append(pop)
    out[key]={'source_multisets_tested':len(populations),'residual_free_types_available':len(free),
      'supplement_feasible':len(survivors),'first_survivors':survivors[:3],
      'scope':'Necessary B-edge forcing only; free N-state obligations, A-common neighbours, criticality and graph realization relaxed.'}
print(json.dumps(out,indent=2))
