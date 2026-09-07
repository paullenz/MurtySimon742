#!/usr/bin/env python3
"""Separate exact checker. Standard library only; does not import coupled.py.

The source caps are recomputed by augmenting-path matching, not the discovery
program's sorted threshold matching. Both programs are by the same assistant.
Usage: python3 verify_certificate.py RESULTS.json
"""
from __future__ import annotations
import json
from itertools import combinations
from pathlib import Path
import sys


def reconstruct(profile: dict) -> dict:
    d, rho, R = [profile[k] for k in ('d','rho','R')]
    a,b = len(d),len(rho)
    if a < 1 or b < 1 or len(R) != a:
        raise ValueError('invalid profile dimensions')
    if any(type(x) is not int for arr in (d,rho,R) for x in arr):
        raise ValueError('noninteger profile')
    if any(x<0 or x>=a for x in d) or any(x<0 or x>a for x in rho) or any(x<0 or x>b for x in R):
        raise ValueError('profile entry out of range')
    if sum(rho)!=sum(R) or sum(d)%2:
        raise ValueError('invalid ledger')
    cap=[min(a-r,b-1) for r in rho]
    demand=[max(0,d[i]-R[i]) for i in range(a)]
    while True:
        updated=[]
        for u in range(b):
            feasible=0
            for q in range(1,cap[u]+1):
                edges={i:[w for w in range(b) if w!=u and rho[w]+cap[w]>=q-1
                          and d[i]<=rho[u]+rho[w]]
                       for i in range(a) if d[i]<=rho[u]+R[i] and d[i]<=rho[u]+q-1}
                owner={}
                def augment(i,seen):
                    for w in edges[i]:
                        if w in seen:continue
                        seen.add(w)
                        if w not in owner or augment(owner[w],seen):
                            owner[w]=i
                            return True
                    return False
                for i in edges:
                    augment(i,set())
                if len(owner)>=q:feasible=q
            updated.append(feasible)
        if updated==cap:break
        cap=updated
    E=[{u for u in range(b) if cap[u]>0 and d[i]<=rho[u]+R[i]
        and d[i]<=rho[u]+cap[u]-1} for i in range(a)]
    forced=[E[i] if len(E[i])==demand[i] and demand[i]>0 else set() for i in range(a)]
    forced_count=[sum(u in F for F in forced) for u in range(b)]
    triples=set()
    for u in range(b):
        for i in range(a):
            lower=max(1,forced_count[u],d[i]-rho[u]+1)
            if u not in E[i] or lower>cap[u]:continue
            for w in range(b):
                if w==u or w in forced[i]:continue
                if d[i]>rho[u]+rho[w] or rho[w]+cap[w]<lower-1:continue
                triples.add((u,i,w))
    sink=[max(0,min(b-1,r+b-a-1)) for r in rho]
    return {'a':a,'b':b,'s':demand,'c':cap,'p':sink,'triples':triples}


def verify(profile: dict, certificate: dict) -> dict:
    D=reconstruct(profile);a,b=D['a'],D['b']
    capacities={('source',u):D['c'][u] for u in range(b)}
    capacities.update({('incidence',u,i):1 for u in range(b) for i in range(a)})
    capacities.update({('pair',u,w):1 for u,w in combinations(range(b),2)})
    capacities.update({('supplement',w):D['p'][w] for w in range(b)})
    y=certificate['label_weights']
    if len(y)!=a or any(type(x) is not int or x<0 for x in y):
        raise ValueError('invalid label weights')
    weights={}
    for row in certificate['resource_weights']:
        key,value=tuple(row[:-1]),row[-1]
        if key not in capacities or key in weights or type(value) is not int or value<0:
            raise ValueError('invalid resource weights')
        weights[key]=value
    for u,i,w in D['triples']:
        cover=sum(weights.get(k,0) for k in [('source',u),('incidence',u,i),
                  ('pair',min(u,w),max(u,w)),('supplement',w)])
        if y[i]>cover:
            raise ValueError('uncovered permissible triple')
    lhs=sum(y[i]*D['s'][i] for i in range(a))
    rhs=sum(capacities[k]*z for k,z in weights.items())
    if lhs<=rhs:raise ValueError('no strict contradiction')
    return {'status':'SEPARATE_EXACT_CHECK_PASS','weighted_demand':lhs,
            'weighted_capacity':rhs,'allowed_triples':len(D['triples']),
            'source_caps':D['c'],'supplement_caps':D['p']}


if __name__=='__main__':
    filename=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('RESULTS.json')
    result=json.loads(filename.read_text())
    print(json.dumps(verify(result['n27_profile'],result['n27_discovery']['certificate']),indent=2))
