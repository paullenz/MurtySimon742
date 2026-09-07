#!/usr/bin/env python3
"""Falsification tests; never a substitute for the universal mathematical proofs.
Exhaustive labelled graphs n=3..6, plus seeded edge-minimal graphs n=7..18.
"""
from __future__ import annotations
import sys
if sys.flags.optimize:
    raise RuntimeError('Regression checks require Python without -O or PYTHONOPTIMIZE.')

from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import importlib.util
import json
import random
from coupled import profile_data,check_certificate,scalar_max,n27_fixture


def diam2(G):
    return all((G[u]>>w)&1 or G[u]&G[w] for u in range(len(G)) for w in range(u+1,len(G)))


def bipartite(G):
    colours={}
    for u in range(len(G)):
        if u in colours:continue
        colours[u]=0;todo=[u]
        while todo:
            v=todo.pop()
            for w in range(len(G)):
                if not (G[v]>>w)&1:continue
                if w in colours:
                    if colours[w]==colours[v]:return False
                else:colours[w]=1-colours[v];todo.append(w)
    return True


def critical(G):
    n=len(G)
    if sum(x.bit_count() for x in G)==n*(n-1) or not diam2(G):return False
    for u,w in combinations(range(n),2):
        if not (G[u]>>w)&1:continue
        G[u]^=1<<w;G[w]^=1<<u
        redundant=diam2(G)
        G[u]^=1<<w;G[w]^=1<<u
        if redundant:return False
    return True


def validate_graph(G,counts,rng=None):
    n=len(G);full=(1<<n)-1
    H=[full^(1<<u)^G[u] for u in range(n)]
    a=min(x.bit_count() for x in H)
    assert a>0
    for v in range(n):
        if H[v].bit_count()!=a:continue
        A=[i for i in range(n) if (H[v]>>i)&1]
        B=[u for u in range(n) if u!=v and not (H[v]>>u)&1]
        b=len(B);choices=[]
        for u,w in combinations(B,2):
            if (H[u]>>w)&1:continue
            options=[]
            for source,supp in [(u,w),(w,u)]:
                for i in A:
                    if (H[source]>>i)&1 and (H[source]|H[i])==full^(1<<supp):
                        options.append((source,i,supp))
            assert options
            choices.append(options)
        selections=product(*choices) if rng is None else [tuple(rng.choice(x) for x in choices)]
        for selected in selections:
            counts['selections']+=1
            marked={(u,i) for u,i,w in selected}
            residual={(u,i) for u in B for i in A if (H[u]>>i)&1 and (u,i) not in marked}
            rho=[sum((u,i) in residual for i in A) for u in B]
            R=[sum((u,i) in residual for u in B) for i in A]
            d=[sum(i!=j and not (H[i]>>j)&1 for j in A) for i in A]
            s=[max(0,di-ri) for di,ri in zip(d,R)]
            r=sum(rho);t=sum(d)//2-r
            if t>0:counts['positive_surplus']+=1
            assert all(si<a for si in s)
            assert sum(F(si*si,a-si) for si in s)<=r
            counts['charging_checks']+=1
            if all(rho):
                assert sum(F(si*(si-1),a-si) for si in s)<=r-b
                counts['active_charging_checks']+=1
                if a>=5:
                    assert b+2*t<scalar_max(a)[0]
                    counts['strict_scalar_checks']+=1
            profile={'d':d,'rho':rho,'R':R}
            data=profile_data(profile)
            permitted=set(data['triples'])
            incoming=[0]*b;outgoing=[0]*b
            for u,i,w in selected:
                ui=B.index(u);ii=A.index(i);wi=B.index(w)
                assert (ui,ii,wi) in permitted
                outgoing[ui]+=1;incoming[wi]+=1
            assert all(q<=c for q,c in zip(outgoing,data['c']))
            assert all(p<=c for p,c in zip(incoming,data['p']))
            # Reconstruct exact B-degree identity, not just its consequence.
            for j,w in enumerate(B):
                assert H[w].bit_count()==b-1+rho[j]-incoming[j]
            counts['triple_domain_checks']+=len(selected)


def graph_tests():
    exhaustive=dict(graphs=0,critical=0,nonbipartite=0,selections=0,positive_surplus=0,
                    charging_checks=0,active_charging_checks=0,strict_scalar_checks=0,triple_domain_checks=0)
    for n in range(3,7):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            exhaustive['graphs']+=1;G=[0]*n
            for k,(u,w) in enumerate(pairs):
                if (mask>>k)&1:G[u]|=1<<w;G[w]|=1<<u
            if not critical(G):continue
            exhaustive['critical']+=1
            if bipartite(G):continue
            exhaustive['nonbipartite']+=1
            validate_graph(G,exhaustive)
    rng=random.Random(74220260907)
    samples={k:0 for k in exhaustive}
    kept=[]
    for n in range(7,19):
        for trial in range(20):
            G=[0]*n;pairs=list(combinations(range(n),2))
            density=[0.35,0.6,0.85,1.0][trial%4]
            for u,w in pairs:
                if rng.random()<density:G[u]|=1<<w;G[w]|=1<<u
            samples['graphs']+=1
            if not diam2(G):continue
            rng.shuffle(pairs)
            for u,w in pairs:
                if not (G[u]>>w)&1:continue
                G[u]^=1<<w;G[w]^=1<<u
                if not diam2(G):G[u]|=1<<w;G[w]|=1<<u
            assert critical(G)
            samples['critical']+=1
            if bipartite(G):continue
            samples['nonbipartite']+=1
            kept.append({'n':n,'adjacency_bitmasks':G})
            validate_graph(G,samples,rng)
    return {'exhaustive_n3_to_n6':exhaustive,'seeded_n7_to_n18':samples,
            'seed':74220260907,'sample_graphs':kept}


def abstract_tests():
    examined=valid=active=0
    # An independent test of the charging lemma on three-state incidence
    # matrices (absent/residual/selected), not on graphs or criticality.
    for a,b in [(2,3),(3,3),(3,4)]:
        for cells in product(range(3),repeat=a*b):
            examined+=1
            rho=[sum(cells[i*b+u]==1 for i in range(a)) for u in range(b)]
            s=[sum(cells[i*b+u]==2 for u in range(b)) for i in range(a)]
            if any(cells[i*b+u]==2 and rho[u]<s[i] for i in range(a) for u in range(b)):continue
            valid+=1;r=sum(rho)
            assert all(si<a for si in s)
            assert sum(F(si*si,a-si) for si in s)<=r
            if all(rho):
                active+=1
                assert sum(F(si*(si-1),a-si) for si in s)<=r-b
    return {'examined':examined,'eligible':valid,'all_sources_residual_active':active,'status':'PASS'}


def certificate_tests():
    p=n27_fixture()
    y=[0]*11;y[10]=1
    cert={'label_weights':y,'resource_weights':[]}
    good=check_certificate(p,cert)
    # Ensure a forged zero-demand certificate is rejected.
    bad={'label_weights':[0]*11,'resource_weights':[]}
    try:check_certificate(p,bad)
    except ValueError:pass
    else:raise AssertionError('accepted forged certificate')
    return {'n27_regression':good,'forged_certificate_rejected':True}


def separate_checker_tests():
    from verify_certificate import reconstruct, verify
    rng=random.Random(613270459)
    count=0
    for _ in range(250):
        a=rng.randrange(2,13);b=rng.randrange(a+1,a+6)
        probability=rng.choice([0.1,0.25,0.5,0.9])
        matrix=[[rng.random()<probability for _ in range(b)] for _ in range(a)]
        R=[sum(row) for row in matrix]
        rho=[sum(matrix[i][u] for i in range(a)) for u in range(b)]
        d=[rng.randrange(a) for _ in range(a)]
        if sum(d)%2:d[-1] += 1 if d[-1]<a-1 else -1
        profile={'d':d,'rho':rho,'R':R}
        first=profile_data(profile);second=reconstruct(profile)
        assert all(first[k]==second[k] for k in ['a','b','s','c','p'])
        assert set(first['triples'])==second['triples']
        count+=1
    cert={'label_weights':[0]*10+[1],'resource_weights':[]}
    passed=verify(n27_fixture(),cert)
    return {'profile_domain_comparisons':count,'seed':613270459,
            'n27_separate_check':passed,
            'scope':'Two algorithms written by the same assistant; not external review.'}


if __name__=='__main__':
    out={'status':'PASS','graph_tests':graph_tests(),'abstract_matrix_tests':abstract_tests(),
         'certificate_tests':certificate_tests(),'separate_checker_tests':separate_checker_tests(),
         'limitations':'Same-assistant finite falsification tests, not universal proofs or external review. Seeded graph tests select one quasi-edge assignment per root, not all assignments.'}
    Path(__file__).with_name('TEST_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='graph_tests'},indent=2))
    print(json.dumps({k:v for k,v in out['graph_tests'].items() if k!='sample_graphs'},indent=2))
