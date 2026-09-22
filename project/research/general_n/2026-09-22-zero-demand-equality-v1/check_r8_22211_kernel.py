#!/usr/bin/env python3
"""Exact source and supplement kernel for the unique (2,2,2,1,1) r=8 core."""
import itertools,json
R=(2,2,2,1,1);edges=[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4)]
need=(2,2,2,2,2);k=5;neighbors=[set() for _ in R]
for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
patterns=[]
for state in itertools.product(range(3),repeat=k):
    L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
    valid=not any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L)
    if not valid:continue
    if not Z:
        if L:assert False
        continue
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
search(0,R,(0,0,0,0,0),[])
def supplement_ok(pop):
    L=[{i for i,s in enumerate(st) if s==1} for st in pop]
    for u in range(len(pop)):
        for i in L[u]:
            possible=len(L[u])==1
            for w in range(len(pop)):
                if w==u:continue
                forced={(u,j) for j in L[u] if pop[w][j]==0}
                forced|={(w,j) for j in L[w] if pop[u][j]==0}
                possible|=forced=={(u,i)}
            if not possible:return False
    return True
survivors=[p for p in pops if supplement_ok(p)]
out={'R':R,'edges':edges,'selected_lower_bounds':need,'single_source_patterns':len(patterns),
     'source_multisets':len(pops),'supplement_feasible':len(survivors),
     'source_examples':pops[:5],'supplement_examples':survivors[:5],
     'scope':'Exact necessary C-source and B-edge forcing kernel; not graph realization.'}
print(json.dumps(out,indent=2))
