#!/usr/bin/env python3
"""Definition-level small-graph challenge for SELECTION_FREE.md.

Evidence only.  Reconstructs the complement bridge directly from D2C graphs,
enumerates candidate quasi-edges, tests the raw pointwise restrictions, checks
the candidate-capacity subset inequality when t>0, and builds two deterministic
legal representative systems per root to challenge the selected-excess lemma.
"""
from collections import Counter
from itertools import combinations
import json
import random
import networkx as nx

from maxcut_recon import SEED, is_d2c, minimize_diameter_two


def open_neigh(H,u):
    return set(H.neighbors(u))


def analyse_root(G,v):
    H=nx.complement(G)
    V=set(H.nodes())
    A=sorted(H.neighbors(v)); Aset=set(A)
    B=sorted(V-Aset-{v}); Bset=set(B)
    a=len(A); b=len(B); m=G.number_of_edges(); t=m-b*(a+1)
    assert H.degree(v)==min(dict(H.degree()).values())==a
    d={i:(a-1)-sum(1 for j in A if j!=i and H.has_edge(i,j)) for i in A}
    c={u:sum(H.has_edge(u,i) for i in A) for u in B}
    mu={u:sum(not H.has_edge(u,w) for w in B if w!=u) for u in B}
    C={i:sum(H.has_edge(i,u) for u in B) for i in A}
    pair_candidates={}
    candidate_count=0
    for ix,u in enumerate(B):
        for w in B[ix+1:]:
            if H.has_edge(u,w):
                continue
            opts=[]
            for src,exc in ((u,w),(w,u)):
                for i in A:
                    if not H.has_edge(src,i):
                        continue
                    if open_neigh(H,src)|open_neigh(H,i)==V-{exc}:
                        assert d[i] <= c[src]-1
                        assert C[i] >= mu[src]
                        opts.append((src,i,exc))
                        candidate_count+=1
            assert opts, (G.number_of_nodes(),v,u,w)
            pair_candidates[(u,w)]=sorted(opts)
    K={u:{i for i in A if H.has_edge(u,i) and d[i]<=c[u]-1 and C[i]>=mu[u]} for u in B}
    subset_checks=0
    sharp_subset_checks=0
    for mask in range(1<<b):
        U={B[j] for j in range(b) if (mask>>j)&1}
        em=sum(not H.has_edge(u,w) for u,w in combinations(sorted(U),2))
        assert em <= sum(len(K[u]) for u in U), (G.number_of_nodes(),v,U,em,K)
        subset_checks+=1
        if t>0:
            kappa={u:min(c[u]-1,len(K[u])) for u in B}
            assert em <= sum(kappa[u] for u in U), (G.number_of_nodes(),v,U,em,kappa)
            lhs=sum(mu[u] for u in U)-len(U)*(b-len(U))
            assert lhs <= 2*sum(kappa[u] for u in U)
            sharp_subset_checks+=1
    selection_checks=0
    for choose_last in (False,True):
        selected=[]
        for pair,opts in sorted(pair_candidates.items()):
            selected.append(opts[-1] if choose_last else opts[0])
        selected_edges={(u,i) for u,i,w in selected}
        assert len(selected_edges)==len(selected)
        q={u:0 for u in B}; p={u:0 for u in B}; x={i:0 for i in A}
        for u,i,w in selected:
            q[u]+=1; p[w]+=1; x[i]+=1
        rho={u:c[u]-q[u] for u in B}
        R={i:C[i]-x[i] for i in A}
        assert all(z>=0 for z in rho.values()) and all(z>=0 for z in R.values())
        s={i:max(0,d[i]-R[i]) for i in A}
        for u,i,w in selected:
            if s[i]>0:
                assert p[u]-rho[u]+1 <= x[i]-s[i], (G.number_of_nodes(),v,u,i)
        left=0
        for u in B:
            qp=sum(1 for uu,i,w in selected if uu==u and s[i]>0)
            left += qp*max(0,p[u]-rho[u]+1)
        right=sum(x[i]*(x[i]-s[i]) for i in A if s[i]>0)
        assert left<=right
        selection_checks+=1
    return candidate_count,subset_checks,sharp_subset_checks,selection_checks,t


def main():
    atlas=[G.copy() for G in nx.graph_atlas_g() if is_d2c(G)]
    rng=random.Random(SEED)
    generated=[]
    for n in range(8,13):
        for k in range(300):
            p=rng.uniform(.25,.80)
            G=minimize_diameter_two(n,p,100000*n+k)
            if G is not None: generated.append(G)
    graphs=atlas+generated
    roots=triples=subsets=sharp_subsets=selections=positive=0
    order_counts=Counter()
    for G in graphs:
        H=nx.complement(G); mindeg=min(dict(H.degree()).values())
        for v in G.nodes():
            if H.degree(v)!=mindeg: continue
            roots+=1; order_counts[G.number_of_nodes()]+=1
            a,b,bs,c,t=analyse_root(G,v)
            triples+=a; subsets+=b; sharp_subsets+=bs; selections+=c; positive+=(t>0)
    out={
        'schema':'selection-free-small-graph-challenge-v1',
        'scope':'Evidence only; direct graph-definition challenge, not proof.',
        'seed':SEED,'graphs':len(graphs),'roots':roots,
        'root_order_counts':dict(sorted(order_counts.items())),
        'candidate_triples_checked':triples,
        'positive_surplus_roots':positive,
        'candidate_set_subset_inequalities_checked':subsets,
        'positive_surplus_sharpened_subset_inequalities_checked':sharp_subsets,
        'representative_systems_checked':selections,
        'violations':0,'status':'PASS'
    }
    print(json.dumps(out,indent=2))
    with open('SELECTION_FREE_SMALL_CHECK.json','w') as f:
        json.dump(out,f,indent=2);f.write('\n')

if __name__=='__main__':main()
