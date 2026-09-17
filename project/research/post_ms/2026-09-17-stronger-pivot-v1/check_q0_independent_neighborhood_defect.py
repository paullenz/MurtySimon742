#!/usr/bin/env python3
"""Regression checks for Q0_INDEPENDENT_NEIGHBORHOOD_DEFECT_THEOREM.md.

Finite checks are evidence only; the hand proof is the mathematical basis.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter

import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if G.number_of_nodes() < 2 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for a, b in list(G.edges()):
        H = G.copy()
        H.remove_edge(a, b)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def common(G: nx.Graph, a, b):
    return set(G.neighbors(a)) & set(G.neighbors(b))


def build_Xk(k: int):
    G = nx.Graph()
    B = list(itertools.product([0, 1], repeat=k))
    root = ("r",)
    A = [("a", i) for i in range(k)]
    G.add_nodes_from([root] + B + A)

    for x in B:
        for i in range(k):
            y = list(x)
            y[i] ^= 1
            y = tuple(y)
            if x < y:
                G.add_edge(x, y)

    for x in B:
        G.add_edge(root, x)

    for i, a in enumerate(A):
        for x in B:
            if x[i] == 0:
                G.add_edge(a, x)

    return G, root


def M(n: int) -> int:
    return ((n - 1) ** 2) // 4 + 1


def main() -> None:
    counts = Counter()
    failures = []

    for G in nx.graph_atlas_g():
        n = G.number_of_nodes()
        if n < 3 or not nx.is_connected(G):
            continue
        if not is_d2c(G):
            continue

        counts["atlas_d2c"] += 1
        if nx.is_bipartite(G):
            continue
        counts["atlas_nonbip_d2c"] += 1

        b = max(dict(G.degree()).values())
        for v in G.nodes():
            if G.degree(v) != b:
                continue

            B = set(G.neighbors(v))
            if G.subgraph(B).number_of_edges() != 0:
                continue

            A = set(G.nodes()) - {v} - B
            F = G.subgraph(A)
            f = F.number_of_edges()
            delta = b * (n - b) - G.number_of_edges()

            counts["q0_max_roots"] += 1
            if f:
                counts["q0_nonbip_roots_fpositive"] += 1

            R = {}
            d = {}
            e = {}
            E = 0
            for x in A:
                R[x] = b - len(B & set(G.neighbors(x)))
                d[x] = F.degree(x)
                e[x] = R[x] - d[x]
                E += e[x]
                if e[x] < 0:
                    failures.append(("negative_e", n, v, x, e[x]))

            if delta != f + E:
                failures.append(("defect_identity", n, v, delta, f, E))

            if delta < b - 1:
                failures.append(("main_bound", n, v, b, delta))

            # Triangle-free F-edge payment.
            for x, y in F.edges():
                if not common(G, x, y):
                    counts["triangle_free_F_edges"] += 1
                    if delta < b - 1:
                        failures.append(("triangle_free_payment", n, v, x, y, b, delta))

            # General source-foot local dichotomy.
            for u in B:
                S = A & set(G.neighbors(u))
                T = A - S
                active = [
                    x for x in S
                    if any(y in S for y in F.neighbors(x))
                ]
                if active:
                    counts["source_internal_active_instances"] += 1

                no_type1 = []
                footsets = {}

                for x in active:
                    type1 = []
                    for p in set(G.neighbors(u)) - {x}:
                        if G.has_edge(p, x):
                            continue
                        if common(G, p, x) == {u}:
                            type1.append(p)

                    type2 = []
                    for y in set(G.neighbors(x)) - {u}:
                        if G.has_edge(y, u):
                            continue
                        if common(G, y, u) == {x}:
                            type2.append(y)

                    if not (type1 or type2):
                        failures.append(("cross_critical_no_arm", n, v, u, x))

                    # Whenever Type I occurs, replay the hand payment directly.
                    for p in type1:
                        if p == v:
                            if R[x] < b - 1:
                                failures.append(("type1_root_payment", n, v, u, x, R[x], b))
                        elif p in A:
                            if R[p] + R[x] < b - 1:
                                failures.append(("type1_A_payment", n, v, u, p, x, R[p], R[x], b))

                    if not type1:
                        no_type1.append(x)
                        valid = [
                            y for y in type2
                            if y in T and (set(F.neighbors(y)) & S) == {x}
                        ]
                        if not valid:
                            failures.append(("no_type1_no_private_foot", n, v, u, x, type2))
                        footsets[x] = set(valid)

                # Foot sets for distinct active vertices must be disjoint.
                xs = list(footsets)
                for i in range(len(xs)):
                    for j in range(i + 1, len(xs)):
                        if footsets[xs[i]] & footsets[xs[j]]:
                            failures.append(("foot_overlap", n, v, u, xs[i], xs[j]))

                if active and len(no_type1) == len(active):
                    counts["pure_foot_sources"] += 1
                    if len(active) > len(T):
                        failures.append(("source_foot_count", n, v, u, len(active), len(T)))

    # Mandatory hostile control: theorem must not apply at its unique max root.
    X3, root = build_Xk(3)
    x3_b = X3.degree(root)
    x3_B = set(X3.neighbors(root))
    x3_Q = X3.subgraph(x3_B).number_of_edges()
    x3 = {
        "n": X3.number_of_nodes(),
        "m": X3.number_of_edges(),
        "M_n": M(X3.number_of_nodes()),
        "Delta": x3_b,
        "Q_at_unique_max_root": x3_Q,
        "is_D2C": is_d2c(X3),
    }
    if not x3["is_D2C"] or x3["n"] != 12 or x3["m"] != 32 or x3["M_n"] != 31 or x3_Q <= 0:
        failures.append(("X3_control", x3))

    if failures:
        raise AssertionError(json.dumps(failures[:20], indent=2, default=str))

    summary = {
        "status": "PASS_Q0_INDEPENDENT_NEIGHBORHOOD_DEFECT",
        "scope": "graph-atlas regression through order 7 plus X3 hostile control; not a proof and not a promotion",
        **dict(counts),
        "X3_hostile_control": x3,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
