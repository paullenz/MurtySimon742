#!/usr/bin/env python3
"""Compare code-level certificate formulae against literal edge-deletion BFS."""
from itertools import product,combinations
from pathlib import Path
import random,json
from check_star_support import CODES,Q,graph
from check_five_coordinate_family import build

def short_pairs(adj):
    pairs=set()
    for x in range(len(adj)):
        reached=set(adj[x])
        for y in adj[x]:reached.update(adj[y])
        pairs.update((x,y) for y in reached if x<y)
    return pairs

def predicted(adj,codes,x,y):
    A=set(range(9,len(adj))); H={z:CODES[codes[z-9]] for z in A}; NA={z:adj[z]&A for z in A}
    out=set()
    def put(a,b):out.add(tuple(sorted((a,b))))
    if x<9:x,y=y,x
    if y<8:
        s=y
        if not(H[x]&Q[s]) and not any(s in H[z] for z in NA[x]):put(x,s)
        for t in Q[s]-H[x]:
            if Q[t]&H[x]=={s} and not any(t in H[z] for z in NA[x]):put(x,t)
        for z in A-{x}:
            if z not in NA[x] and H[x]&H[z]=={s} and not(NA[x]&NA[z]):put(x,z)
            if z in NA[x] and not(H[z]&({s}|Q[s])) and {a for a in NA[z] if s in H[a]}=={x}:put(s,z)
    else:
        if not(H[x]&H[y]) and not(NA[x]&NA[y]):put(x,y)
        for source,head in ((x,y),(y,x)):
            for t in H[head]-H[source]:
                if not(Q[t]&H[source]) and {z for z in NA[source] if t in H[z]}=={head}:put(source,t)
            for z in A-{source,head}:
                if z not in NA[source] and not(H[source]&H[z]) and NA[source]&NA[z]=={head}:put(source,z)
    return out

def main():
    rng=random.Random(2026092114); cases=[]
    # Exhaust all labelled two-A-vertex code choices, with and without their edge.
    for cs in product(CODES,repeat=2):
        for edge in ([],[(0,1)]):cases.append((list(cs),edge))
    # Larger local populations add third targets, competing common neighbours,
    # repeated physical codes, and both endpoint orientations.
    for _ in range(400):
        a=rng.randrange(3,18);cs=rng.choices(list(CODES),k=a);density=rng.choice((0,.1,.3,.6,1))
        edges=[(i,j) for i,j in combinations(range(a),2) if rng.random()<density]
        cases.append((cs,edges))
    cases.append((['C00','C10','C20'],[]))
    for r,q in ((1,0),(1,1),(3,3)):
        _,cs,edges=build(r,q);cases.append((cs,edges))
    checked=0;certs=0
    for cs,edges in cases:
        adj=graph(cs,edges);before=short_pairs(adj)
        for x in range(9,len(adj)):
            for y in sorted(adj[x]):
                if y>=9 and y<x:continue
                expected=predicted(adj,cs,x,y)
                adj[x].remove(y);adj[y].remove(x)
                actual=before-short_pairs(adj)
                adj[x].add(y);adj[y].add(x)
                assert actual==expected,{'codes':cs,'A_edges':edges,'deleted':[x,y],'actual':actual,'expected':expected}
                checked+=1;certs+=len(actual)
    result={'cases':len(cases),'exhaustive_two_A_populations':512,'seeded_larger_populations':400,'actual_D2C_controls':4,'deleted_edges_compared':checked,'individual_lost_distance_two_pairs':certs,'result':'all exact certificate sets equal independent edge-deletion reachability','scope':'Local certificate completeness and physical uniqueness; no claim arbitrary generated fixtures are D2C; no Hall/global-source premise promotion.'}
    Path(__file__).with_name('EXACT_LOCAL_CERTIFICATE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result)
if __name__=='__main__':main()
