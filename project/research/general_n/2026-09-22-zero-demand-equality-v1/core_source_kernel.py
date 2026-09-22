#!/usr/bin/env python3
"""Necessary local source patterns only; survivors are NOT actual graphs."""
import itertools,json
R=(2,1,1,1)
cases={'diamond_heavy_degree_three':[(0,1),(0,2),(0,3),(1,2),(1,3)],
       'diamond_heavy_degree_two':[(1,2),(1,3),(2,3),(0,1),(0,2)]}
out={}
for name,edges in cases.items():
    neighbors=[set() for _ in R]
    for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
    need=tuple(max(0,len(neighbors[i])-R[i]) for i in range(4))
    patterns=[]
    for state in itertools.product(range(3),repeat=4):
        L={i for i,s in enumerate(state) if s==1}
        Z={i for i,s in enumerate(state) if s==2}
        if not Z:continue
        if any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L):continue
        patterns.append((tuple(int(i in Z) for i in range(4)),tuple(int(i in L) for i in range(4)),state))
    survivors=[]
    def search(start,remaining,x,chosen):
        if not any(remaining):
            if all(x[i]>=need[i] for i in range(4)):survivors.append(chosen)
            return
        for k in range(start,len(patterns)):
            z,l,state=patterns[k]
            if all(z[i]<=remaining[i] for i in range(4)):
                search(k,tuple(remaining[i]-z[i] for i in range(4)),tuple(x[i]+l[i] for i in range(4)),chosen+[state])
    search(0,R,(0,0,0,0),[])
    out[name]={'edges':edges,'R':R,'selected_lower_bounds':need,'patterns':len(patterns),'survivor_multisets':len(survivors),'first_survivors':survivors[:5],
               'scope':'Necessary source patterns only; no supplements, source-source edges, or D2C realization asserted.'}
print(json.dumps(out,indent=2))
