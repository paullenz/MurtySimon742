#!/usr/bin/env python3
"""Finite regression for FIRST_POSITIVE_RESIDUAL_TIGHT_COVER_GAP.md.

The universal theorem is hand mathematics. This script independently checks the
orientation-code graph through all switching gauges for k<=5 by default and k=6
with --extended, and checks the local one-defect switching classification.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations
import argparse
import json


def canonical_signings(k):
    free=[(i,j) for i in range(1,k) for j in range(i+1,k)]
    for mask in range(1<<len(free)):
        s=[[0]*k for _ in range(k)]
        for t,(i,j) in enumerate(free):
            s[i][j]=s[j][i]=(mask>>t)&1
        yield mask,s


def defect_graph(k,s,c):
    bits=[(c>>i)&1 for i in range(k)]
    E=set(); deg=[0]*k
    for i in range(k):
        for j in range(i+1,k):
            if (bits[i]^bits[j]) != s[i][j]:
                E.add((i,j)); deg[i]+=1; deg[j]+=1
    return frozenset(E),tuple(deg)


def orientation_codes(k,s,i,j,alpha):
    """Two Boolean witness codes for the physical B-edge.

    i<j, endpoint bit alpha in fibre i, and beta=alpha xor sigma_ij in fibre j.
    """
    beta=alpha^s[i][j]
    x=[0]*k                 # source j -> target i
    x[j]=1-beta; x[i]=alpha
    for h in range(k):
        if h not in (i,j):
            x[h]=1^beta^s[j][h]
    y=[0]*k                 # source i -> target j
    y[i]=1-alpha; y[j]=beta
    for h in range(k):
        if h not in (i,j):
            y[h]=1^alpha^s[i][h]
    xx=sum(bit<<h for h,bit in enumerate(x))
    yy=sum(bit<<h for h,bit in enumerate(y))
    return xx,yy


def omega_edges(k,s):
    E=set()
    for i in range(k):
        for j in range(i+1,k):
            for alpha in (0,1):
                x,y=orientation_codes(k,s,i,j,alpha)
                if x!=y:
                    E.add(tuple(sorted((x,y))))
                else:
                    raise AssertionError("orientation codes unexpectedly coincide")
    return frozenset(E)


def min_vertex_cover_size(edges):
    @lru_cache(None)
    def rec(E):
        if not E:
            return 0
        deg=Counter()
        for u,v in E:
            deg[u]+=1; deg[v]+=1
        u,v=max(E,key=lambda e:deg[e[0]]+deg[e[1]])
        Eu=frozenset(e for e in E if u not in e)
        Ev=frozenset(e for e in E if v not in e)
        return 1+min(rec(Eu),rec(Ev))
    return rec(edges)


def cut_edges(k,S):
    S=set(S)
    return frozenset((i,j) for i in range(k) for j in range(i+1,k)
                     if ((i in S)!=(j in S)))


def phi(k,E):
    deg=[0]*k
    for i,j in E:
        deg[i]+=1; deg[j]+=1
    return k-sum(d==1 for d in deg),tuple(deg)


def is_star_at(k,E,a):
    want=frozenset(tuple(sorted((a,v))) for v in range(k) if v!=a)
    return E==want


def is_star_plus_k2_at(k,E,a,b):
    # exceptional a in L, partner-exception b in switched state
    others=[v for v in range(k) if v not in (a,b)]
    # exactly one c among others is paired with b, all remaining others join a
    for c in others:
        want={tuple(sorted((b,c)))}
        want.update(tuple(sorted((a,v))) for v in others if v!=c)
        if E==frozenset(want):
            return True
    return False


def check_one_defect_pair_classification(k):
    base_edges=[(i,j) for i in range(k) for j in range(i+1,k)]
    checked=0
    for mask in range(1<<len(base_edges)):
        E=frozenset(base_edges[t] for t in range(len(base_edges)) if (mask>>t)&1)
        p,de=phi(k,E)
        if p!=1:
            continue
        a=next(i for i,d in enumerate(de) if d!=1)
        for s in range(1,k):
            if s>k//2:
                continue
            for S in combinations(range(k),s):
                F=E^cut_edges(k,S)
                q,df=phi(k,F)
                if q!=1 or F==E:
                    continue
                checked+=1
                b=next(i for i,d in enumerate(df) if d!=1)
                assert a!=b
                assert set(S)=={a,b} or set(range(k))-set(S)=={a,b}
                assert is_star_at(k,E,a) or is_star_plus_k2_at(k,E,a,b)
    return checked


def run(max_k):
    distributions={}
    total_signings=0
    for k in range(3,max_k+1):
        dist=Counter()
        for _,s in canonical_signings(k):
            tau=min_vertex_cover_size(omega_edges(k,s))
            dist[tau]+=1
            if k>=5:
                assert tau>=k+1
        total_signings+=sum(dist.values())
        distributions[k]=dict(sorted(dist.items()))

    pair_checks={}
    for k in (5,6):
        pair_checks[k]=check_one_defect_pair_classification(k)

    return {
        "status":"PASS_FIRST_POSITIVE_RESIDUAL_TIGHT_COVER_GAP",
        "orientation_code_switching_signings_checked":total_signings,
        "min_vertex_cover_distributions":distributions,
        "one_defect_switch_pair_records":pair_checks,
        "scope":"finite regression evidence only; the universal code-cover and residual-gap statements are hand proofs",
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--extended",action="store_true",help="include all 1024 canonical k=6 signings")
    args=ap.parse_args()
    print(json.dumps(run(6 if args.extended else 5),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
