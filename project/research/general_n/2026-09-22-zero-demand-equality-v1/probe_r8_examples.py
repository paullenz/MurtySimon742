#!/usr/bin/env python3
"""Exact source feasibility probe on saved r=8 example cores only."""
import itertools,json
from functools import lru_cache
from pathlib import Path
data=json.loads(Path('R8_CORE_CENSUS.json').read_text());out={}
for partition,entry in data.items():
    if not entry.get('first_examples'):continue
    R=tuple(int(x.strip()) for x in partition.strip('()').split(',') if x.strip());k=len(R)
    rows=[]
    for q,rep in enumerate(entry['first_examples'],1):
        neighbors=[set() for _ in R]
        for i,j in rep['edges']:neighbors[i].add(j);neighbors[j].add(i)
        P=set(rep['P']);need=tuple(rep['selected_lower_bounds']);patterns=[]
        for state in itertools.product(range(3),repeat=k):
            L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
            valid=not any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L)
            if not valid:continue
            if not Z:
                assert not (L&P);continue
            patterns.append((tuple(int(i in Z) for i in range(k)),tuple(int(i in L) for i in range(k))))
        @lru_cache(None)
        def feasible(rem,x):
            if not any(rem):return all(x[i]>=need[i] for i in range(k))
            for z,l in patterns:
                if all(z[i]<=rem[i] for i in range(k)):
                    nr=tuple(rem[i]-z[i] for i in range(k))
                    nx=tuple(min(need[i],x[i]+l[i]) for i in range(k))
                    if feasible(nr,nx):return True
            return False
        ok=feasible(R,tuple(0 for _ in R))
        rows.append({'example':q,'source_feasible':ok,'single_source_patterns':len(patterns),
                     'memo_states':feasible.cache_info().currsize,'degrees':rep['degrees'],'t_upper':rep['t_upper']})
    out[partition]={'examples_tested':len(rows),'source_feasible_examples':sum(r['source_feasible'] for r in rows),'rows':rows,
      'scope':'Only first saved labelled examples, not all cores or signatures.'}
print(json.dumps(out,indent=2))
