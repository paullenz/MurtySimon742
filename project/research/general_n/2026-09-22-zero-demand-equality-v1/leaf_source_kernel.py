#!/usr/bin/env python3
"""Necessary local source patterns only; survivors are NOT actual graphs."""
import itertools,json
cases={'triangle_heavy_one_link':((2,1,1,1,0),[(0,1),(0,4),(1,2),(1,3),(2,3)]),
       'triangle_disjoint_heavy_star':((2,1,1,1,0,0),[(0,4),(0,5),(1,2),(1,3),(2,3)])}
out={}
for name,(R,edges) in cases.items():
    n=len(R)
    neighbors=[set() for _ in R]
    for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
    need=tuple(max(0,len(neighbors[i])-R[i]) for i in range(n))
    patterns=[]
    for state in itertools.product(range(3),repeat=n):
        L={i for i,s in enumerate(state) if s==1}
        Z={i for i,s in enumerate(state) if s==2}
        if not Z:continue
        if any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L):continue
        patterns.append((tuple(int(i in Z) for i in range(n)),tuple(int(i in L) for i in range(n)),state))
    survivors=[]
    def search(start,remaining,x,chosen):
        if not any(remaining):
            if all(x[i]>=need[i] for i in range(n)):survivors.append(chosen)
            return
        for k in range(start,len(patterns)):
            z,l,state=patterns[k]
            if all(z[i]<=remaining[i] for i in range(n)):
                search(k,tuple(remaining[i]-z[i] for i in range(n)),tuple(x[i]+l[i] for i in range(n)),chosen+[state])
    search(0,R,tuple(0 for _ in R),[])
    if name=='triangle_heavy_one_link':
        assert len(survivors)==6
        for population in survivors:
            assert all(s[1]!=0 for s in population)
            assert any(s[1]==1 and sum(t==1 for t in s)>=2 for s in population)
    out[name]={'edges':edges,'R':R,'selected_lower_bounds':need,'patterns':len(patterns),'survivor_multisets':len(survivors),'first_survivors':survivors[:6],
               'scope':'Necessary source patterns only; no supplements, source-source edges, or D2C realization asserted.'}
print(json.dumps(out,indent=2))
