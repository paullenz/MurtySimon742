#!/usr/bin/env python3
"""New caps and priced tails on the earlier 713 sampled RELAXED profiles."""
import csv,json,collections
from pathlib import Path
from verify_localized_fixed_tail import localized
from verify_priced_tail import lower_bound
ROOT=Path(__file__).parent
C=collections.Counter();examples=[]
for raw in csv.DictReader((ROOT/'SYNTHETIC_INTERVAL_PROFILES.tsv').open(),delimiter='\t'):
    p={k:([int(x) for x in v.split(',')] if k in ('q','rho','s','P') else int(v)) for k,v in raw.items()}
    q,rho,s=[p[k] for k in ('q','rho','s')];cap,trace=localized(p['a'],q,rho,s,p['Esel'])
    E=p['Esel'];z=s.count(0);env=E*(E+max(s));v=[max(0,x-z) for x in q];c=[x+y for x,y in zip(q,rho)]
    hall=False;priced=False
    for tau in range(1,max(q)+1):
        A=[min(cap[w],sum(u!=w and tau<=q[u]<=c[w]+1 for u in range(len(q)))) for w in range(len(q))]
        demand=sum(x for x in q if x>=tau)
        hall |= demand>sum(A)
        priced |= any(lower_bound(A,[r-1 for r in rho],v,demand,theta)>env for theta in {0,*v,env+max(v)+1})
    C['profiles']+=1;C['localized_interval_rejected']+=hall;C['priced_tail_rejected']+=priced;C['not_rejected']+=not priced
    if not priced and len(examples)<1:examples.append(p)
assert dict(C)==dict(profiles=713,localized_interval_rejected=652,priced_tail_rejected=652,not_rejected=61)
result=dict(counts=dict(C),scope='713 previously sampled bridge relaxations; passing a priced-tail screen is not graph realization',unrejected_example=examples)
(ROOT/'SYNTHETIC_PRICED_TAIL_RECHECK.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(C),indent=2))
