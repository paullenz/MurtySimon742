#!/usr/bin/env python3
"""Physical source-state multiset screen for four optimistic r=6 cores."""
import itertools,json
from pathlib import Path
data=json.loads(Path('R6_CORE_SCREEN.json').read_text())
orbits=data['(2, 1, 1, 1, 1)']['orbit_representatives']
R=(2,1,1,1,1);out={}
for q,orbit in enumerate(orbits,1):
    rep=orbit['representative'];edges=[tuple(e) for e in rep['edges']]
    neighbors=[set() for _ in R]
    for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
    need=tuple(rep['selected_lower_bounds'])
    patterns=[]
    for state in itertools.product(range(3),repeat=5):
        L={i for i,s in enumerate(state) if s==1}
        Z={i for i,s in enumerate(state) if s==2}
        if not Z:continue
        if any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L):continue
        z=tuple(int(i in Z) for i in range(5));x=tuple(int(i in L) for i in range(5))
        patterns.append((z,x,state))
    count=[0];examples=[]
    def search(start,remaining,x,chosen):
        if not any(remaining):
            if all(x[i]>=need[i] for i in range(5)):
                count[0]+=1
                if len(examples)<5:examples.append(chosen)
            return
        for k in range(start,len(patterns)):
            z,l,state=patterns[k]
            if all(z[i]<=remaining[i] for i in range(5)):
                search(k,tuple(remaining[i]-z[i] for i in range(5)),
                       tuple(x[i]+l[i] for i in range(5)),chosen+[state])
    search(0,R,(0,0,0,0,0),[])
    out[f'orbit_{q}']={'edges':edges,'degrees':rep['degrees'],'t_upper':rep['t_upper'],
      'selected_lower_bounds':need,'single_source_patterns':len(patterns),
      'surviving_source_multisets':count[0],'first_survivors':examples,
      'scope':'Necessary source states only; no B-edges, supplements, criticality or D2C realization.'}
print(json.dumps(out,indent=2))
