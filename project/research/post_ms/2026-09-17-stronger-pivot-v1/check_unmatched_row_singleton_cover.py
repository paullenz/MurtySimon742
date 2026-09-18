#!/usr/bin/env python3
"""Finite regression for UNMATCHED_ROW_SINGLETON_COVER.md.

For each NetworkX graph-atlas graph K of exact order p=3,...,7, construct
Psi(K) with edges {A_i,{i}}, where A_i is the open non-neighbour set of i,
solve tau(Psi(K)) exactly by brute force, and verify

    tau(Psi(K)) = 1
iff
    K is K_p or K_{p-1} disjoint union K_1.

The finite scan is regression evidence only; the theorem is proved by hand in
the companion note.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter

import networkx as nx


def psi_graph(K: nx.Graph) -> nx.Graph:
    V = list(K.nodes())
    H = nx.Graph()
    for i in V:
        A_i = frozenset(j for j in V if j != i and not K.has_edge(i, j))
        singleton = frozenset((i,))
        H.add_edge(A_i, singleton)
    return H


def exact_vertex_cover_number(H: nx.Graph) -> int:
    nodes = list(H.nodes())
    edges = list(H.edges())
    for k in range(len(nodes) + 1):
        for C_tuple in itertools.combinations(nodes, k):
            C = set(C_tuple)
            if all(x in C or y in C for x, y in edges):
                return k
    raise AssertionError("finite graph has no vertex cover")


def is_complete_or_clique_plus_isolate(K: nx.Graph) -> bool:
    p = len(K)
    if K.number_of_edges() == p * (p - 1) // 2:
        return True

    isolates = [v for v, d in K.degree() if d == 0]
    if len(isolates) != 1:
        return False

    R = K.copy()
    R.remove_node(isolates[0])
    return R.number_of_edges() == (p - 1) * (p - 2) // 2


def main() -> None:
    summary = {
        "scope": "NetworkX graph atlas, every unlabelled graph of exact order p=3,...,7",
        "orders": {},
        "violations": [],
    }

    for p in range(3, 8):
        graphs = [G for G in nx.graph_atlas_g() if len(G) == p]
        distribution = Counter()
        one_code_graphs = []

        for index, K in enumerate(graphs):
            tau = exact_vertex_cover_number(psi_graph(K))
            distribution[tau] += 1

            predicted_one = is_complete_or_clique_plus_isolate(K)
            actual_one = tau == 1
            if actual_one:
                one_code_graphs.append(
                    {
                        "atlas_index_within_order": index,
                        "edges": K.number_of_edges(),
                        "degree_sequence": sorted(d for _, d in K.degree()),
                    }
                )

            if predicted_one != actual_one:
                summary["violations"].append(
                    {
                        "p": p,
                        "atlas_index_within_order": index,
                        "edges": K.number_of_edges(),
                        "degree_sequence": sorted(d for _, d in K.degree()),
                        "tau": tau,
                        "predicted_one": predicted_one,
                    }
                )

        summary["orders"][str(p)] = {
            "graphs": len(graphs),
            "tau_distribution": {
                str(k): distribution[k] for k in sorted(distribution)
            },
            "one_code_graphs": one_code_graphs,
        }

    print(json.dumps(summary, indent=2, sort_keys=True))
    assert not summary["violations"]
    for p in range(3, 8):
        assert len(summary["orders"][str(p)]["one_code_graphs"]) == 2


if __name__ == "__main__":
    main()
