#!/usr/bin/env python3
"""Exact, standard-library audit of selected-excess tail losses and Hall slack.

No graph-realizability or whole-state exclusion is inferred from these tests.
The direct cap implementation follows scan_post_pair_relational.cpp at
81560e92698d07992df4a53976ee1ea8efaaeb4d; the threshold implementation is separate.
"""
from __future__ import annotations
from itertools import combinations_with_replacement
from random import Random
import json


def demand_threshold(E: int, z: int, j: int) -> int:
    if min(E, z) < 0 or j < 1:
        raise ValueError('E,z must be nonnegative and j positive')
    return min(E, z) + max(E-z, 0)//j + 1


def excess_loss(q: int, E: int, z: int, k: int) -> int:
    if min(q, E, z, k) < 0:
        raise ValueError('nonnegative integer parameters required')
    return sum(q >= demand_threshold(E,z,j) for j in range(1,k+2))


def direct_excess_loss(q: int, E: int, z: int, k: int) -> int:
    if q == 0:
        return 0
    ks = min(z, q, E)
    if q == ks:
        return 0
    extra = (E-ks)//(q-ks)
    return max(0, k+1-extra)


def direct_caps(a: int, qr: tuple[tuple[int,int], ...], E: int, z: int):
    b = len(qr)
    q, rho = zip(*qr)
    c = [q[u]+rho[u] for u in range(b)]
    D = [[u != w and q[u] <= c[w]+1 and q[w] <= c[u]
          for w in range(b)] for u in range(b)]
    degree = [sum(D[u][v] or D[v][u] for v in range(b)) for u in range(b)]
    P=[]
    for u in range(b):
        p = min(rho[u]+b-a-1, b-1-q[u])
        if q[u] > 0:
            ks=min(z,q[u],E)
            if q[u] > ks:
                p=min(p,rho[u]+(E-ks)//(q[u]-ks)-1)
        P.append(min(p,degree[u]-q[u]))
    return q,rho,c,D,degree,P


def audit_profile(a: int, qr: tuple[tuple[int,int], ...], E: int, z: int,
                  masks: list[int] | None = None):
    b=len(qr)
    k=b-a-1
    assert k >= 0 and 0 <= z <= a
    assert all(q >= 0 and r >= 1 and q+r <= a for q,r in qr)
    q,rho,c,D,deg,P=direct_caps(a,qr,E,z)
    ell=[excess_loss(x,E,z,k) for x in q]
    eta=[max(0,c[u]+k-deg[u]-ell[u]) for u in range(b)]
    for u in range(b):
        assert P[u] == rho[u]+k-ell[u]-eta[u]
    layer_sum=sum(sum(x >= demand_threshold(E,z,j) for x in q) for j in range(1,k+2))
    assert sum(ell) == layer_sum
    if min(P) < 0:
        return {'legal_caps':False,'cuts':0,'deficient':0,'tail_deficient':0}
    Q=sum(q)
    r=sum(rho)
    G=Q-r  # Algebraic test variable; not asserted to arise from a legal graph.
    B0=b*k-G-sum(ell)-sum(eta)
    assert sum(P)-Q == B0
    assert B0 == b*k-(Q-r-E)-E-layer_sum-sum(eta)
    if masks is None:
        masks=list(range(1<<b))
    deficient=tail_deficient=0
    for mask in masks:
        S=[u for u in range(b) if mask>>u&1]
        demand=sum(q[u] for u in S)
        y=[sum(D[u][w] for u in S) for w in range(b)]
        H=sum(min(P[w],y[w]) for w in range(b))
        unused=sum(max(P[w]-y[w],0) for w in range(b))
        outside=Q-demand
        margin=H-demand
        assert margin == B0+outside-unused
        assert margin == b*k-G-layer_sum-sum(eta)+outside-unused
        deficient += margin < 0
        if S == [u for u in range(b) if q[u]>=min((q[v] for v in S),default=max(q)+1)]:
            tail_deficient += margin < 0
    return {'legal_caps':True,'cuts':len(masks),'deficient':deficient,'tail_deficient':tail_deficient}


def boundary_counterexample():
    # Archived cap-only non-tail witness: full bridge ledger deliberately absent.
    qr=((1,1),)+((3,1),)*6
    q,rho,c,D,deg,P=direct_caps(4,qr,19,4)
    margins=[]
    for tau in range(1,5):
        S=[u for u in range(7) if q[u]>=tau]
        margins.append(sum(min(P[w],sum(D[u][w] for u in S)) for w in range(7))-sum(q[u] for u in S))
    singleton=sum(min(P[w],D[0][w]) for w in range(7))-q[0]
    assert P==[3]*7 and singleton==-1 and margins==[2,3,3,0]
    # Demonstrates that neither our algebra nor positive Q-r licenses a tail theorem.
    assert sum(q)-sum(rho)==12 and sum(q)-sum(rho)-19==-7
    return {'caps':P,'singleton_margin':singleton,'tail_margins':margins,
            'Q_minus_r_minus_E':-7,'full_bridge_ledger':'FAILS'}


def main():
    scalar=0
    for k in range(7):
        for q in range(25):
            for E in range(41):
                for z in range(25):
                    assert excess_loss(q,E,z,k)==direct_excess_loss(q,E,z,k)
                    scalar+=1
    totals={'profiles':0,'nonnegative_cap_profiles':0,'source_sets':0,'deficient_source_sets':0}
    for a,b in ((2,3),(2,4),(3,4),(3,5)):
        universe=[(q,r) for r in range(1,a+1) for q in range(a-r+1)]
        for qr in combinations_with_replacement(universe,b):
            Q=sum(q for q,r in qr)
            for E in range(Q+1):
                for z in range(a+1):
                    ans=audit_profile(a,qr,E,z)
                    totals['profiles']+=1
                    totals['nonnegative_cap_profiles']+=ans['legal_caps']
                    totals['source_sets']+=ans['cuts']
                    totals['deficient_source_sets']+=ans['deficient']
    rng=Random(74220260914)
    random_cuts=0
    random_valid=0
    for _ in range(10000):
        a=rng.randrange(2,13)
        b=a+rng.randrange(1,6)
        qr=tuple((lambda r:(rng.randrange(a-r+1),r))(rng.randrange(1,a+1)) for _ in range(b))
        E=rng.randrange(sum(q for q,r in qr)+1)
        z=rng.randrange(a+1)  # Deliberately not restricted by z<=E.
        masks=[0,(1<<b)-1]+[rng.randrange(1<<b) for _ in range(8)]
        ans=audit_profile(a,qr,E,z,masks)
        random_cuts+=ans['cuts']
        random_valid+=ans['legal_caps']
    report={'schema':'selected-excess-tail-loss-v1','result':'PASS',
            'scalar_identities':scalar,'exhaustive':totals,
            'random_profiles':10000,'random_nonnegative_cap_profiles':random_valid,
            'random_source_sets':random_cuts,'random_seed':74220260914,
            'archived_non_tail_counterexample':boundary_counterexample(),
            'trust_boundary':'Local exact finite audit; not independent external review; no frontier promotion'}
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
