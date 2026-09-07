#!/usr/bin/env python3
"""Exhaustive labelled-graph and witness-selection tests through n=6.

Tests are falsification checks, NOT a proof of universal graph lemmas.
No positive-surplus graph occurs; that absence is explicitly reported.
Standard-library only. All selections are enumerated, without sampling.
"""
from itertools import combinations, product
from pathlib import Path
import json
import math


def diameter_at_most_two(adj):
    return all((adj[i] >> j) & 1 or adj[i] & adj[j]
               for i in range(len(adj)) for j in range(i+1, len(adj)))


def is_bipartite(adj):
    colour = [-1]*len(adj)
    for root in range(len(adj)):
        if colour[root] != -1:
            continue
        colour[root] = 0
        todo = [root]
        while todo:
            u = todo.pop()
            for w in range(len(adj)):
                if (adj[u] >> w) & 1:
                    if colour[w] == colour[u]:
                        return False
                    if colour[w] == -1:
                        colour[w] = 1-colour[u]
                        todo.append(w)
    return True


def check(n, G, m, counts):
    full = (1 << n)-1
    H = [full ^ (1 << u) ^ G[u] for u in range(n)]
    a = min(row.bit_count() for row in H)
    assert a > 0
    for v in range(n):
        if H[v].bit_count() != a:
            continue
        A = [i for i in range(n) if (H[v] >> i) & 1]
        B = [u for u in range(n) if u != v and not (H[v] >> u) & 1]
        b = len(B)
        t = m-b*(n-b)
        choices = []
        for u, w in combinations(B, 2):
            if (H[u] >> w) & 1:
                continue
            opts = []
            for source, supplement in [(u,w),(w,u)]:
                for i in A:
                    if (H[source] >> i) & 1 and H[source] | H[i] == full ^ (1 << supplement):
                        opts.append((source,i,supplement))
            assert opts
            choices.append(opts)
        counts['root_instances'] += 1
        counts['largest_selection_product'] = max(counts['largest_selection_product'], math.prod(map(len,choices)))
        for selected in product(*choices):
            counts['selection_instances'] += 1
            if t > 0:
                counts['positive_surplus_instances'] += 1
            S = {(u,i) for u,i,w in selected}
            assert len(S) == len(selected)
            residual = {(u,i) for u in B for i in A if (H[u] >> i) & 1 and (u,i) not in S}
            r = len(residual)
            rho = {u: sum((u,i) in residual for i in A) for u in B}
            R = {i: sum((u,i) in residual for u in B) for i in A}
            d = {i: sum(j != i and not (H[i] >> j) & 1 for j in A) for i in A}
            assert sum(d.values()) == 2*(r+t)
            for u,i,w in selected:
                assert d[i] <= rho[u]+R[i]
                assert d[i] <= rho[u]+rho[w]
            h = max([0]+[j for j in range(1,b+1) if sum(q >= j for q in rho.values()) >= j])
            assert all(max(0,d[i]-R[i]) <= h for i in A)
            assert r+2*t <= a*h
            active = all(q >= 1 for q in rho.values())
            if t > 0:
                assert active
            if active:
                counts['all_B_residual_active_instances'] += 1
                assert r >= b+h*(h-1)
                assert b+2*t <= (a+1)**2//4
                ec = sum((H[i] >> j) & 1 for i,j in combinations(A,2))
                L = ec+r
                for x in A:
                    Y = [i for i in A if (H[x] >> i) & 1]
                    k = len(Y)
                    ey = sum((H[i] >> j) & 1 for i,j in combinations(Y,2))
                    assert L >= b+k+math.comb(a-k-1,2)+ey
                    counts['local_vertex_inequality_checks'] += 1


def main():
    counts = {key:0 for key in ['graphs', 'diameter_two_critical', 'non_bipartite_critical',
             'root_instances','selection_instances','largest_selection_product',
             'positive_surplus_instances','all_B_residual_active_instances',
             'local_vertex_inequality_checks']}
    for n in range(3,7):
        pairs = list(combinations(range(n),2))
        for mask in range(1 << len(pairs)):
            counts['graphs'] += 1
            G = [0]*n
            edges = []
            for k,(u,w) in enumerate(pairs):
                if (mask >> k) & 1:
                    G[u] |= 1 << w
                    G[w] |= 1 << u
                    edges.append((u,w))
            if len(edges) == len(pairs) or not diameter_at_most_two(G):
                continue
            critical = True
            for u,w in edges:
                G[u] ^= 1 << w
                G[w] ^= 1 << u
                redundant = diameter_at_most_two(G)
                G[u] ^= 1 << w
                G[w] ^= 1 << u
                if redundant:
                    critical = False
                    break
            if not critical:
                continue
            counts['diameter_two_critical'] += 1
            if is_bipartite(G):
                continue
            counts['non_bipartite_critical'] += 1
            check(n,G,len(edges),counts)
    result = {'status':'PASS', 'coverage':'all labelled simple graphs of orders 3 through 6; all selected-quasi-edge choices at all minimum-degree complement roots of the non-bipartite critical graphs', 'counts':counts, 'limitations':'No positive-surplus graph occurred. These finite tests do not prove residual activity for arbitrary positive surplus, nor the universal theorem. Same-assistant implementation, not external review.'}
    Path(__file__).with_name('SMALL_GRAPH_TESTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
