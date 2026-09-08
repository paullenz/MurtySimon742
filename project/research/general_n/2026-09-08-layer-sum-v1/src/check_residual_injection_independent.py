#!/usr/bin/env python3
"""Independent residual-injection audit for the layer-sum candidate.

Does not import check_layers.py. Exhaustive through n=6; additionally builds
fixed deterministic larger critical graphs to exercise the forced residual
map nonvacuously. The larger sample is evidence only, not exhaustive.
"""
from itertools import combinations, product
from hashlib import sha256
import json


def graph_from_mask(n, mask):
    adj=[0]*n
    for k,(u,v) in enumerate(combinations(range(n),2)):
        if (mask>>k)&1:
            adj[u]|=1<<v; adj[v]|=1<<u
    return adj


def diameter_at_most_two(adj):
    n=len(adj); allv=(1<<n)-1
    for u in range(n):
        reach=(1<<u)|adj[u]
        for v in range(n):
            if (adj[u]>>v)&1: reach |= adj[v]
        if reach != allv: return False
    return True


def critical(adj):
    if not diameter_at_most_two(adj): return False
    for u,v in combinations(range(len(adj)),2):
        if (adj[u]>>v)&1:
            changed=adj.copy(); changed[u]^=1<<v; changed[v]^=1<<u
            if diameter_at_most_two(changed): return False
    return True


def complement(adj):
    n=len(adj); allv=(1<<n)-1
    return [allv ^ (1<<u) ^ adj[u] for u in range(n)]


def adjacent_total_dominates(H,x,y):
    return bool((H[x]>>y)&1) and (H[x]|H[y]) == (1<<len(H))-1


def raw_choices(G,H,v):
    n=len(G); allv=(1<<n)-1
    A=[i for i in range(n) if (H[v]>>i)&1]
    B=[u for u in range(n) if u!=v and not ((H[v]>>u)&1)]
    choices=[]
    for u,w in combinations(B,2):
        if (H[u]>>w)&1: continue
        H2=H.copy(); H2[u]|=1<<w; H2[w]|=1<<u
        opts=[]
        for x,y in combinations(range(n),2):
            if not adjacent_total_dominates(H2,x,y): continue
            if x in (u,w) and y not in (u,w):
                source,label=x,y
            elif y in (u,w) and x not in (u,w):
                source,label=y,x
            else:
                continue
            supplement=w if source==u else u
            if label in A and ((H[source]>>label)&1) and \
                    (H[source]|H[label]) == (allv ^ (1<<supplement)):
                opts.append((source,label,supplement))
        assert opts
        choices.append(opts)
    return A,B,choices


def check_selection(G,H,A,B,chosen):
    selected={(u,i):w for u,i,w in chosen}
    assert len(selected)==len(chosen)
    residual={(u,i) for u in B for i in A
              if ((H[u]>>i)&1) and (u,i) not in selected}
    rho={u:sum((u,i) in residual for i in A) for u in B}
    R={i:sum((u,i) in residual for u in B) for i in A}
    d={i:sum((G[i]>>j)&1 for j in A) for i in A}
    checked=forced=0
    for u,i,w in chosen:
        # The final source-demand inequality.
        assert d[i] <= rho[u]+R[i]
        checked += 1
        supplements=[]
        for j in A:
            if not ((G[i]>>j)&1): continue  # j is not an F-neighbour
            if (u,j) not in selected: continue
            z=selected[(u,j)]
            assert z != w
            # ui dominates z while u misses z, so iz is present in H.
            assert (H[i]>>z)&1
            # j misses both i and z; therefore iz cannot be selected with a
            # B-exception and must be residual. Cross edges are stored B,A.
            assert not ((H[j]>>z)&1)
            assert (z,i) in residual
            supplements.append(z); forced += 1
        # Different selected uj edges at one source have different supplements.
        assert len(supplements)==len(set(supplements))
    return checked,forced


def greedy(n,seed):
    adj=[((1<<n)-1)^(1<<u) for u in range(n)]
    edges=list(combinations(range(n),2))
    edges.sort(key=lambda e: sha256(
        f'residual-audit:{n}:{seed}:{e[0]}:{e[1]}'.encode()).digest())
    for u,v in edges:
        adj[u]^=1<<v; adj[v]^=1<<u
        if not diameter_at_most_two(adj):
            adj[u]|=1<<v; adj[v]|=1<<u
    assert critical(adj)
    return adj


def run():
    s={'small_graphs':0,'small_critical':0,'small_roots':0,
       'small_systems':0,'small_selected_edges':0,'small_forced_targets':0,
       'sample_graphs':0,'sample_roots':0,'sample_systems':0,
       'sample_selected_edges':0,'sample_forced_targets':0,
       'sample_nonzero_forced_systems':0}
    digest=sha256()
    for n in range(3,7):
        for mask in range(1<<(n*(n-1)//2)):
            s['small_graphs']+=1
            G=graph_from_mask(n,mask)
            if not critical(G): continue
            s['small_critical']+=1; H=complement(G)
            md=min(x.bit_count() for x in H)
            for v in [x for x in range(n) if H[x].bit_count()==md]:
                s['small_roots']+=1
                A,B,choices=raw_choices(G,H,v)
                for chosen in product(*choices):
                    c,f=check_selection(G,H,A,B,chosen)
                    s['small_systems']+=1; s['small_selected_edges']+=c
                    s['small_forced_targets']+=f
                    digest.update((json.dumps(['small',n,mask,v,chosen],
                                               separators=(',',':'))+'\n').encode())
    for n in [7,8,10,12,16,20,25,30]:
        for seed in range(20):
            G=greedy(n,seed); H=complement(G); s['sample_graphs']+=1
            md=min(x.bit_count() for x in H)
            for v in [x for x in range(n) if H[x].bit_count()==md]:
                s['sample_roots']+=1
                A,B,choices=raw_choices(G,H,v)
                candidates=[tuple(opts[0] for opts in choices),
                            tuple(opts[-1] for opts in choices)]
                unique=[]
                for chosen in candidates:
                    if chosen not in unique: unique.append(chosen)
                for chosen in unique:
                    c,f=check_selection(G,H,A,B,chosen)
                    s['sample_systems']+=1; s['sample_selected_edges']+=c
                    s['sample_forced_targets']+=f
                    s['sample_nonzero_forced_systems']+=bool(f)
                    digest.update((json.dumps(['sample',n,seed,v,chosen],
                                               separators=(',',':'))+'\n').encode())
    result={'status':'PASS','stats':s,'ordered_case_sha256':digest.hexdigest(),
            'expected_ordered_case_sha256':'5e33b3ad7d7fc8d1276ebab7de09dc03026346779d41e1a4411032dd9acc069a',
            'small_scope':'all labelled graphs 3<=n<=6; all minimum-degree roots; all quasi-edge choices',
            'larger_scope':'160 deterministic greedy critical graphs; first/last choice systems only',
            'external_independence':False,'formal_proof':False}
    assert result['ordered_case_sha256']==result['expected_ordered_case_sha256']
    assert s['sample_forced_targets']==588 and s['sample_nonzero_forced_systems']==163
    return result

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
