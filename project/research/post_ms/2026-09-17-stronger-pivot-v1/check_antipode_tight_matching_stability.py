#!/usr/bin/env python3
"""Finite regression for ANTIPODE_TIGHT_MATCHING_STABILITY.md.

Evidence only; the hand proof is the mathematical basis.
Checks all D2C graph-atlas classes through order 7, every maximum-degree root,
and the explicit X_3 hostile control.
"""

from collections import Counter
from itertools import combinations, product
import json
import networkx as nx


def is_d2c(G):
    if len(G) < 2 or not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def antipode_info(G, v, u, w):
    B = set(G.neighbors(v))
    A = set(G) - B - {v}
    if G.has_edge(u, w) or set(nx.common_neighbors(G, u, w)) != {v}:
        return None
    U = {x for x in A if G.has_edge(u, x)}
    W = {x for x in A if G.has_edge(w, x)}
    X = {x for x in B - {u, w} if G.has_edge(u, x)}
    Y = {x for x in B - {u, w} if G.has_edge(w, x)}
    assert not (U & W)
    assert not (X & Y)
    C = A - U - W
    Z = (B - {u, w}) - X - Y
    b = len(B)
    lam = 2 * b - len(G)
    eps_u = b - G.degree(u)
    eps_w = b - G.degree(w)
    eta = len(C) + len(Z)
    assert eps_u + eps_w == lam + 1 + eta
    return {
        "eta": eta,
        "eps_u": eps_u,
        "eps_w": eps_w,
        "C": len(C),
        "Z": len(Z),
    }


def tight_pairs(G, v):
    B = set(G.neighbors(v))
    out = []
    for u, w in combinations(B, 2):
        info = antipode_info(G, v, u, w)
        if info is not None and info["eta"] == 0:
            out.append((u, w))
    return out


def check_full_cover(G, v, pairs):
    B = set(G.neighbors(v))
    A = set(G) - B - {v}
    k = len(pairs)
    assert 2 * k == len(B)

    pair_of = {}
    for i, (u, w) in enumerate(pairs):
        pair_of[u] = i
        pair_of[w] = i

    # Every pair of fibres is joined by a perfect matching.
    for (u, w), (x, y) in combinations(pairs, 2):
        assert sum(G.has_edge(p, q) for p in (u, w) for q in (x, y)) == 2
        for p in (u, w):
            assert sum(G.has_edge(p, q) for q in (x, y)) == 1
        for q in (x, y):
            assert sum(G.has_edge(p, q) for p in (u, w)) == 1

    # Every A-vertex chooses exactly one endpoint of every fibre.
    for x in A:
        for u, w in pairs:
            assert int(G.has_edge(x, u)) + int(G.has_edge(x, w)) == 1

    Q = G.subgraph(B).number_of_edges()
    assert Q == k * (k - 1)
    h_cross = sum(1 for x in A for u in B if not G.has_edge(x, u))
    assert h_cross == len(A) * k
    r = h_cross - Q
    assert r == k * (len(A) - k + 1)

    # Selected/quasi-edge witnesses on B-edges have the forced code shape.
    selected_records = 0
    for p, q in G.subgraph(B).edges():
        reps = []
        for src, exc in ((q, p), (p, q)):
            for x in A:
                if G.has_edge(src, x):
                    continue
                if not G.has_edge(exc, x):
                    continue
                if set(nx.common_neighbors(G, src, x)) == {exc}:
                    reps.append((src, x, exc))
        assert reps, ("missing selected witness", p, q)
        for src, x, exc in reps:
            i = pair_of[exc]
            j = pair_of[src]
            assert i != j
            # Fibre j: choose mate of src.
            u, w = pairs[j]
            mate = u if w == src else w
            assert G.has_edge(x, mate) and not G.has_edge(x, src)
            # Fibre i: choose exception.
            assert G.has_edge(x, exc)
            # Other fibres: choose the endpoint not adjacent to src.
            for ell, (r0, r1) in enumerate(pairs):
                if ell in (i, j):
                    continue
                src_nbrs = [t for t in (r0, r1) if G.has_edge(src, t)]
                assert len(src_nbrs) == 1
                nonnbr = r1 if src_nbrs[0] == r0 else r0
                assert G.has_edge(x, nonnbr)
            # F-separation.
            for y in A:
                assert not (G.has_edge(src, y) and G.has_edge(x, y))
        selected_records += len(reps)
    return Q, r, selected_records


def make_x3():
    k = 3
    G = nx.Graph()
    B = list(product((0, 1), repeat=k))
    root = ("r",)
    A = [("a", i) for i in range(k)]
    G.add_nodes_from([root] + B + A)
    for x in B:
        G.add_edge(root, x)
    for i, ai in enumerate(A):
        for x in B:
            if x[i] == 0:
                G.add_edge(ai, x)
    for x in B:
        for i in range(k):
            y = list(x)
            y[i] ^= 1
            y = tuple(y)
            if x < y:
                G.add_edge(x, y)
    return G, root


def main():
    stats = Counter()
    full_cover_records = []

    for G in nx.graph_atlas_g():
        if len(G) < 3 or not is_d2c(G):
            continue
        stats["atlas_d2c_classes"] += 1
        Delta = max(dict(G.degree()).values())
        for v in G:
            if G.degree(v) != Delta:
                continue
            stats["atlas_max_roots"] += 1
            B = set(G.neighbors(v))
            ants = []
            tight = []
            for u, w in combinations(B, 2):
                info = antipode_info(G, v, u, w)
                if info is None:
                    continue
                ants.append((u, w, info))
                stats["atlas_antipode_edges"] += 1
                if info["eta"] == 0:
                    tight.append((u, w))
                    stats["atlas_tight_antipode_edges"] += 1
            if ants:
                stats["atlas_roots_with_antipode"] += 1
            if tight:
                stats["atlas_roots_with_tight_antipode"] += 1

            # Tight antipodes form a matching.
            degree = Counter()
            for u, w in tight:
                degree[u] += 1
                degree[w] += 1
            assert not degree or max(degree.values()) <= 1

            covered = {x for e in tight for x in e}
            if B and covered == B and 2 * len(tight) == len(B):
                stats["atlas_full_tight_cover_roots"] += 1
                Q, r, reps = check_full_cover(G, v, tight)
                stats["atlas_full_cover_B_edges"] += Q
                stats["atlas_selected_witness_records"] += reps
                A = set(G) - B - {v}
                f = G.subgraph(A).number_of_edges()
                delta = len(B) * (len(G) - len(B)) - G.number_of_edges()
                full_cover_records.append({
                    "n": len(G), "m": G.number_of_edges(),
                    "b": len(B), "a": len(A), "k": len(tight),
                    "Q": Q, "r": r, "f": f, "delta": delta,
                })

    # Mandatory hostile control.
    X3, root = make_x3()
    assert is_d2c(X3)
    pairs = tight_pairs(X3, root)
    assert len(pairs) == 4
    assert {x for e in pairs for x in e} == set(X3.neighbors(root))
    Q, r, reps = check_full_cover(X3, root, pairs)
    assert X3.number_of_nodes() == 12
    assert X3.number_of_edges() == 32
    assert ((12 - 1) ** 2) // 4 + 1 == 31
    assert Q == 12 and r == 0 and reps == 12

    out = {
        "status": "PASS_ANTIPODE_TIGHT_MATCHING_STABILITY",
        **stats,
        "atlas_full_cover_records": full_cover_records,
        "X3_hostile_control": {
            "n": 12, "m": 32, "M_n": 31,
            "tight_antipode_pairs": 4,
            "Q": 12, "r": 0,
            "selected_witness_records": 12,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
