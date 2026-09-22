#!/usr/bin/env python3
"""Necessary physical-source screen for r=7 product-equality core orbits."""
import itertools,json,sys
from pathlib import Path
data=json.loads(Path('R7_EQUALITY_CORE_SCREEN.json').read_text());out={}
for partition,entry in data.items():
    R=tuple(int(x.strip()) for x in partition.strip('()').split(',') if x.strip())
    for q,orbit in enumerate(entry['orbit_representatives'],1):
        rep=orbit['representative'];k=len(R);edges=[tuple(e) for e in rep['edges']]
        neighbors=[set() for _ in R]
        for i,j in edges:neighbors[i].add(j);neighbors[j].add(i)
        P=set(rep['P']);need=tuple(rep['selected_lower_bounds']);patterns=[];free_p_assertions=0
        for state in itertools.product(range(3),repeat=k):
            L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
            valid=not any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L)
            if not valid:continue
            if not Z:
                # A residual-free source may select whole N-components, but
                # can never help a positive-demand P label.
                assert not (L&P);free_p_assertions+=bool(L);continue
            patterns.append((tuple(int(i in Z) for i in range(k)),
                             tuple(int(i in L) for i in range(k)),state))
        count=[0];examples=[]
        def search(start,remaining,x,chosen):
            if not any(remaining):
                if all(x[i]>=need[i] for i in range(k)):
                    count[0]+=1
                    if len(examples)<1:examples.append(chosen)
                return
            for j in range(start,len(patterns)):
                z,l,state=patterns[j]
                if all(z[i]<=remaining[i] for i in range(k)):
                    search(j,tuple(remaining[i]-z[i] for i in range(k)),
                           tuple(x[i]+l[i] for i in range(k)),chosen+[state])
        search(0,R,tuple(0 for _ in R),[])
        out[f'{partition}/orbit_{q}']={'R':R,'edges':edges,'h':rep['h'],'P':sorted(P),
          'selected_lower_bounds':need,'single_source_patterns':len(patterns),
          'residual_free_N_patterns_omitted':free_p_assertions,
          'surviving_source_multisets':count[0],'first_survivors':examples,
          'scope':'Necessary C-source states; zero-label attachments, supplements, B-edges and criticality omitted.'}
payload=json.dumps(out,indent=2)+'\n'
if '--output' in sys.argv:
    Path(sys.argv[sys.argv.index('--output')+1]).write_text(payload)
else:
    print(payload,end='')
