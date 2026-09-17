#!/usr/bin/env python3
"""Finite diagnostic only: maximum-degree triangle roots in D2C graphs through n=7.

Requires networkx. graph_atlas_g contains one representative of each unlabeled
simple graph with at most 7 vertices. This script is NOT a proof of the general
statement and is retained only as exact small-order evidence.
"""

import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if G.number_of_nodes() < 3 or not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for u, v in list(G.edges()):
        H = G.copy()
        H.remove_edge(u, v)
        # Disconnection counts as diameter increasing beyond 2.
        if nx.is_connected(H) and nx.diameter(H) == 2:
            return False
    return True


def triangles(G: nx.Graph):
    # enumerate_all_cliques emits cliques in nondecreasing size; retain 3-cliques.
    return [tuple(c) for c in nx.enumerate_all_cliques(G) if len(c) == 3]


def main():
    rows = {}
    failures = []
    for G0 in nx.graph_atlas_g():
        n = G0.number_of_nodes()
        if not (3 <= n <= 7):
            continue
        G = nx.convert_node_labels_to_integers(G0)
        if not is_d2c(G):
            continue
        row = rows.setdefault(n, dict(d2c=0, triangle_bearing=0, failures=0))
        row["d2c"] += 1
        ts = triangles(G)
        if not ts:
            continue
        row["triangle_bearing"] += 1
        deg = dict(G.degree())
        Delta = max(deg.values())
        max_vertices = {v for v, d in deg.items() if d == Delta}
        triangle_vertices = set().union(*(set(t) for t in ts))
        if not (max_vertices & triangle_vertices):
            row["failures"] += 1
            failures.append((n, nx.to_graph6_bytes(G, header=False).decode().strip()))

    expected = {
        3: dict(d2c=1, triangle_bearing=0, failures=0),
        4: dict(d2c=2, triangle_bearing=0, failures=0),
        5: dict(d2c=3, triangle_bearing=0, failures=0),
        6: dict(d2c=5, triangle_bearing=1, failures=0),
        7: dict(d2c=10, triangle_bearing=4, failures=0),
    }
    assert rows == expected, (rows, expected)
    assert not failures, failures
    print("PASS_FINITE_DIAGNOSTIC_ONLY")
    for n in sorted(rows):
        print(n, rows[n])


if __name__ == "__main__":
    main()
