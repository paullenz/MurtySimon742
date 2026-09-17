#!/usr/bin/env python3
"""Regression/replay for ZERO_RESIDUAL_TIGHT_COVER_CLASSIFICATION.md.

Evidence only; the hand argument in the markdown note is the mathematical basis.
The script checks the two surviving normal forms, the switching/factorization
calculation, and the cut-degree obstruction through a wide finite range.
"""

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


def build_full_cover(k, sigma_edges, codes):
    """Build the full-tight Boolean normal form with F empty."""
    G = nx.Graph()
    root = ("r",)
    B = [("b", i, t) for i in range(k) for t in (0, 1)]
    A = [("a", j) for j in range(len(codes))]
    G.add_nodes_from([root] + B + A)
    for u in B:
        G.add_edge(root, u)

    sigma = {tuple(sorted(e)) for e in sigma_edges}
    for i, j in combinations(range(k), 2):
        s = 1 if (i, j) in sigma else 0
        for t in (0, 1):
            G.add_edge(("b", i, t), ("b", j, t ^ s))

    for j, code in enumerate(codes):
        x = ("a", j)
        assert len(code) == k
        for i, t in enumerate(code):
            G.add_edge(x, ("b", i, t))
    return G, root, B, A


def switched_edges(k, sigma_edges, code):
    sigma = {tuple(sorted(e)) for e in sigma_edges}
    out = set()
    for i, j in combinations(range(k), 2):
        bit = ((i, j) in sigma) ^ bool(code[i] ^ code[j])
        if bit:
            out.add((i, j))
    return out


def is_perfect_matching(k, edges):
    deg = [0] * k
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    return all(d == 1 for d in deg)


def selected_reps(G, B, A):
    """All canonical A-cross quasi-edge witnesses for B-edges."""
    reps = {}
    for p, q in G.subgraph(B).edges():
        key = frozenset((p, q))
        cur = []
        for src, exc in ((q, p), (p, q)):
            for x in A:
                if G.has_edge(src, x):
                    continue
                if not G.has_edge(exc, x):
                    continue
                if set(nx.common_neighbors(G, src, x)) == {exc}:
                    cur.append((src, x, exc))
        reps[key] = cur
    return reps


def verify_r0_bijection(G, root, B, A):
    k = len(B) // 2
    Q = G.subgraph(B).number_of_edges()
    h_cross = sum(1 for x in A for u in B if not G.has_edge(x, u))
    r = h_cross - Q
    assert Q == k * (k - 1)
    assert r == 0
    assert len(A) == k - 1
    assert G.subgraph(A).number_of_edges() == 0

    reps = selected_reps(G, B, A)
    # At r=0 every H-cross edge must be selected, so the total number of
    # possible/used canonical incidences in these normal forms is exactly Q.
    assert all(reps[e] for e in reps)
    flat = [rec for vals in reps.values() for rec in vals]
    assert len(flat) == Q
    cross = {(src, x) for src, x, exc in flat}
    assert len(cross) == Q
    assert len(cross) == h_cross
    return Q, r


def make_T6():
    """Dailly--Foucaud--Hansberg T_6, stated there to be H5."""
    G = nx.Graph()
    G.add_nodes_from(["u", "v", "a1", "a2", "b1", "b2"])
    for i in (1, 2):
        G.add_edge(f"a{i}", f"b{i}")
        G.add_edge("u", f"a{i}")
        G.add_edge("u", f"b{i}")
        G.add_edge("v", f"b{i}")
    return G


def make_X3():
    d = 3
    G = nx.Graph()
    B = list(product((0, 1), repeat=d))
    root = ("rX",)
    A = [("aX", i) for i in range(d)]
    G.add_nodes_from([root] + B + A)
    for x in B:
        G.add_edge(root, x)
    for i, ai in enumerate(A):
        for x in B:
            if x[i] == 0:
                G.add_edge(ai, x)
    for x in B:
        for i in range(d):
            y = list(x)
            y[i] ^= 1
            y = tuple(y)
            if x < y:
                G.add_edge(x, y)
    return G


def main():
    # Cut obstruction: a nontrivial cut of K_k can be 2-regular only at k=4.
    cut_checks = 0
    for k in range(3, 5001):
        possible = False
        for s in range(1, k):
            cut_checks += 1
            if s == 2 and k - s == 2:
                possible = True
        assert possible == (k == 4)

    # k=2 normal form: one A-label, one 1-factor of K2.
    G2, r2, B2, A2 = build_full_cover(
        2,
        {(0, 1)},
        [(0, 0)],
    )
    assert is_d2c(G2)
    assert len(G2) == 6 and G2.number_of_edges() == 8
    assert nx.is_isomorphic(G2, make_T6())
    Q2, res2 = verify_r0_bijection(G2, r2, B2, A2)
    assert Q2 == 2 and res2 == 0

    # k=4: gauge-fix the first factor to M0.  The other two factor cuts have
    # two complementary code representatives each, leaving four finite choices.
    M0 = {(0, 1), (2, 3)}
    M1 = {(0, 2), (1, 3)}
    M2 = {(0, 3), (1, 2)}
    c0 = (0, 0, 0, 0)
    c1_choices = [(1, 0, 0, 1), (0, 1, 1, 0)]
    c2_choices = [(1, 0, 1, 0), (0, 1, 0, 1)]
    X3 = make_X3()
    assert is_d2c(X3)
    assert len(X3) == 12 and X3.number_of_edges() == 32
    assert ((12 - 1) ** 2) // 4 + 1 == 31

    variants = 0
    for c1 in c1_choices:
        for c2 in c2_choices:
            variants += 1
            codes = [c0, c1, c2]
            switched = [switched_edges(4, M0, c) for c in codes]
            assert switched == [M0, M1, M2]
            assert all(is_perfect_matching(4, M) for M in switched)
            assert set().union(*switched) == set(combinations(range(4), 2))
            assert sum(len(M) for M in switched) == 6

            G4, r4, B4, A4 = build_full_cover(4, M0, codes)
            assert is_d2c(G4)
            assert len(G4) == 12 and G4.number_of_edges() == 32
            Q4, res4 = verify_r0_bijection(G4, r4, B4, A4)
            assert Q4 == 12 and res4 == 0
            assert nx.is_isomorphic(G4, X3)

    out = {
        "status": "PASS_ZERO_RESIDUAL_TIGHT_COVER_CLASSIFICATION",
        "cut_degree_checks_through_k_5000": cut_checks,
        "surviving_fibre_counts": [2, 4],
        "k2": {
            "n": 6,
            "m": 8,
            "Q": Q2,
            "r": res2,
            "isomorphic_to_T6_H5": True,
        },
        "k4": {
            "normal_form_variants_after_gauge": variants,
            "all_isomorphic_to_X3": True,
            "n": 12,
            "m": 32,
            "M_n": 31,
            "Q": 12,
            "r": 0,
        },
        "trust_boundary": (
            "finite regression and normal-form isomorphism only; direct adjacency-list "
            "identification of X3 with the published 2024 Figure 1 remains open"
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
