#!/usr/bin/env python3
"""Finite regression for ANTIPODE_BRANCHING_ERROR_PAYMENT.md.

Scans all NetworkX graph-atlas graphs (orders <= 7), retains diameter-2-critical
isomorphism classes, tests every root, constructs the rooted antipode graph,
and verifies

    3 * sum_{y in N_J(w)} eta(yw) >= d_J(w)(d_J(w)-1)

for every antipode centre w, together with the summed global inequality.

This is regression evidence only; it is not the proof of the theorem.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter

import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if len(G) < 3 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def rooted_antipode_graph(G: nx.Graph, v):
    B = list(G.neighbors(v))
    J = nx.Graph()
    J.add_nodes_from(B)
    eta = {}
    for u, w in itertools.combinations(B, 2):
        if G.has_edge(u, w):
            continue
        if set(G.neighbors(u)) & set(G.neighbors(w)) != {v}:
            continue
        err = sum(
            1
            for z in G.nodes()
            if z not in {v, u, w}
            and not G.has_edge(z, u)
            and not G.has_edge(z, w)
        )
        J.add_edge(u, w)
        eta[frozenset((u, w))] = err
    return J, eta


def main() -> None:
    stats = Counter()
    min_local_margin = None
    max_antipode_degree = 0
    local_violations = []
    global_violations = []

    for G in nx.graph_atlas_g():
        if len(G) < 3 or not is_d2c(G):
            continue

        stats["d2c_graphs"] += 1
        stats[f"d2c_n{len(G)}"] += 1

        for v in G.nodes():
            stats["roots"] += 1
            J, eta = rooted_antipode_graph(G, v)

            if J.number_of_edges():
                stats["roots_with_antipode"] += 1
                stats["antipode_edges_over_roots"] += J.number_of_edges()

            for w, d in J.degree():
                if d == 0:
                    continue
                stats["antipode_centres"] += 1
                if d >= 2:
                    stats["branching_centres"] += 1
                max_antipode_degree = max(max_antipode_degree, d)

                eta_sum = sum(eta[frozenset((w, y))] for y in J.neighbors(w))
                margin = 3 * eta_sum - d * (d - 1)
                if min_local_margin is None or margin < min_local_margin:
                    min_local_margin = margin
                if margin < 0:
                    local_violations.append(
                        {
                            "n": len(G),
                            "root": v,
                            "centre": w,
                            "degree": d,
                            "eta_sum": eta_sum,
                            "margin": margin,
                        }
                    )

            eta_total = sum(eta.values())
            degree_curvature = sum(d * (d - 1) for _, d in J.degree())
            global_margin = 6 * eta_total - degree_curvature
            if global_margin < 0:
                global_violations.append(
                    {
                        "n": len(G),
                        "root": v,
                        "eta_total": eta_total,
                        "degree_curvature": degree_curvature,
                        "margin": global_margin,
                    }
                )

    summary = {
        "scope": "NetworkX graph atlas, all D2C isomorphism classes through order 7, every root",
        "d2c_graphs": stats["d2c_graphs"],
        "d2c_by_order": {
            str(n): stats[f"d2c_n{n}"] for n in range(3, 8)
        },
        "roots_tested": stats["roots"],
        "roots_with_antipode": stats["roots_with_antipode"],
        "antipode_edges_over_roots": stats["antipode_edges_over_roots"],
        "antipode_centres": stats["antipode_centres"],
        "branching_centres": stats["branching_centres"],
        "maximum_antipode_degree": max_antipode_degree,
        "minimum_local_integer_margin": min_local_margin,
        "local_violations": local_violations,
        "global_violations": global_violations,
    }

    print(json.dumps(summary, indent=2, sort_keys=True))

    assert not local_violations
    assert not global_violations


if __name__ == "__main__":
    main()
