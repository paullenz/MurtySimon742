#!/usr/bin/env python3
"""Regression check for ROOT_EDGE_STABILITY_DICHOTOMY.md.

This is a finite diagnostic over NetworkX's graph atlas (all unlabeled graphs
through order 7).  The theorem itself is proved by hand in the companion note.
"""

from collections import Counter
from math import comb
import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if len(G) < 3 or not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def root_data(G: nx.Graph, v):
    B = set(G.neighbors(v))
    A = set(G.nodes()) - {v} - B
    n = len(G)
    b = len(B)
    a = len(A)
    m = G.number_of_edges()

    F = G.subgraph(A)
    f = F.number_of_edges()
    nu_F = sum(1 for x in A if F.degree(x) > 0)
    Q = G.subgraph(B).number_of_edges()

    delta = b * (n - b) - m
    r = f + delta
    lam = 2 * b - n

    active = {
        u for u in B
        if any(w in B for w in G.neighbors(u))
    }

    private = set()
    antipodes = {}

    for u in active:
        private_A = [
            x for x in A
            if G.has_edge(u, x)
            and len(set(G.neighbors(x)) & B) == 1
        ]
        if private_A:
            private.add(u)
            continue

        ws = [
            w for w in B - {u}
            if not G.has_edge(u, w)
            and set(nx.common_neighbors(G, u, w)) == {v}
        ]
        if ws:
            antipodes[u] = ws

    return {
        "A": A,
        "B": B,
        "a": a,
        "b": b,
        "n": n,
        "m": m,
        "f": f,
        "nu_F": nu_F,
        "Q": Q,
        "delta": delta,
        "r": r,
        "lambda": lam,
        "active": active,
        "private": private,
        "antipodes": antipodes,
    }


def main() -> None:
    d2c_counts = Counter()
    triangle_root_instances = Counter()
    checked_roots = 0

    for G in nx.graph_atlas_g():
        n = len(G)
        if n > 7 or not is_d2c(G):
            continue

        d2c_counts[n] += 1
        Delta = max(dict(G.degree()).values())

        for v in G.nodes():
            if G.degree(v) != Delta:
                continue

            D = root_data(G, v)
            if D["Q"] == 0:
                continue

            checked_roots += 1
            triangle_root_instances[n] += 1

            # Lemma 3.1: every active u is private-supported or has an antipode.
            covered = D["private"] | set(D["antipodes"])
            assert D["active"] <= covered, (
                "root-edge dichotomy failure",
                n,
                nx.to_graph6_bytes(G, header=False).strip(),
                v,
                D,
            )

            # Private witnesses inject into nonisolated F-vertices.
            assert len(D["private"]) <= D["nu_F"] <= 2 * D["f"]

            if D["active"] <= D["private"]:
                # All-private branch: every G[B] edge lies inside the active set.
                assert D["Q"] <= comb(len(D["active"]), 2)
                assert len(D["active"]) <= D["nu_F"]
                assert D["Q"] <= comb(D["nu_F"], 2)
            else:
                # Antipode branch: graph-level forms of (5.2) and (6.2).
                assert D["Q"] + D["r"] >= D["a"]
                assert 2 * D["r"] + D["b"] * D["lambda"] >= D["a"]

    print("D2C isomorphism-class counts:", dict(sorted(d2c_counts.items())))
    print(
        "maximum-degree triangle-root instances:",
        dict(sorted(triangle_root_instances.items())),
    )
    print("checked roots:", checked_roots)
    print("PASS_ROOT_EDGE_STABILITY_ATLAS")


if __name__ == "__main__":
    main()
