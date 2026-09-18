#!/usr/bin/env python3
"""Graph-atlas audit for the one-hole fan classification.

The checker verifies only generic finite kernels available without rebuilding
the partial-Boolean core:

* an all-one-hole witness graph is clique minus a matching;
* missing witness pairs are mutual unique holes;
* the tau=1 head-stability count;
* relative to a maximum-degree root, an A-type witness (nonadjacent to the
  root) has the root as its unique hole; pairs of such witnesses are adjacent.

Present witness-witness edges are restricted to non-direct edges, matching the
live Boolean application where same-code witnesses share tight-core common
neighbours. This is audit support only.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter

import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if len(G) < 2 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for u, v in list(G.edges()):
        H = G.copy()
        H.remove_edge(u, v)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def N(G: nx.Graph, x: int) -> set[int]:
    return set(G.neighbors(x))


def admissible(G: nx.Graph, witnesses: list[int]) -> bool:
    for i, j in itertools.combinations(range(len(witnesses)), 2):
        wi, wj = witnesses[i], witnesses[j]
        if G.has_edge(wi, wj) and not (N(G, wi) & N(G, wj)):
            return False
    return True


def main() -> None:
    graphs = [G.copy() for G in nx.graph_atlas_g() if is_d2c(G)]
    stats = Counter()
    failures: list[tuple] = []

    # Generic all-one-hole fans.
    for G in graphs:
        V = set(G)
        for x in G:
            Nx = N(G, x)
            Y = V - {x} - Nx
            certs: list[tuple[int, int, int]] = []  # head, witness, unique hole

            for w in G:
                if w == x or G.has_edge(x, w):
                    continue
                common = Nx & N(G, w)
                if len(common) != 1:
                    continue
                h = next(iter(common))
                Z = V - {x, w} - Nx - N(G, w)
                if len(Z) != 1:
                    continue
                certs.append((h, w, next(iter(Z))))

            for r in range(2, len(certs) + 1):
                for sub in itertools.combinations(certs, r):
                    heads = [h for h, _, _ in sub]
                    witnesses = [w for _, w, _ in sub]
                    if len(set(heads)) != r or not admissible(G, witnesses):
                        continue

                    stats["generic_one_hole_fans"] += 1

                    for i, wi in enumerate(witnesses):
                        missing = [
                            j
                            for j, wj in enumerate(witnesses)
                            if i != j and not G.has_edge(wi, wj)
                        ]
                        stats["complement_degree_checks"] += 1
                        if len(missing) > 1:
                            failures.append(("complement_degree", len(G), x, sub, i))
                        for j in missing:
                            if sub[i][2] != witnesses[j] or sub[j][2] != wi:
                                failures.append(("mutual_hole_pair", len(G), x, sub, i, j))

                    t = [len((N(G, h) & Y) - {w}) for h, w, _ in sub]
                    R = math.floor((1 + math.sqrt(1 + 12 * r)) / 2)
                    stats["tau_one_head_stability_checks"] += 1
                    if sum(1 for ti in t if ti > 1) > R:
                        failures.append(("tau_one_head_stability", len(G), x, sub, t, R))

    # Root-hole identification for A-type witnesses.
    for G in graphs:
        b = max(dict(G.degree()).values())
        V = set(G)
        for v in G:
            if G.degree(v) != b:
                continue
            A = {x for x in G if x != v and not G.has_edge(v, x)}
            for x in A:
                Nx = N(G, x)
                certs: list[tuple[int, int, int]] = []
                for w in G:
                    if w in {x, v} or G.has_edge(x, w):
                        continue
                    common = Nx & N(G, w)
                    if len(common) != 1:
                        continue
                    h = next(iter(common))
                    if h not in A:
                        continue
                    Z = V - {x, w} - Nx - N(G, w)
                    if len(Z) != 1:
                        continue
                    certs.append((h, w, next(iter(Z))))

                for r in range(2, len(certs) + 1):
                    for sub in itertools.combinations(certs, r):
                        heads = [h for h, _, _ in sub]
                        witnesses = [w for _, w, _ in sub]
                        if len(set(heads)) != r or not admissible(G, witnesses):
                            continue
                        stats["rooted_one_hole_fans"] += 1
                        IA = [
                            i
                            for i, (_, w, _) in enumerate(sub)
                            if w in A
                        ]
                        for i in IA:
                            stats["A_witness_root_hole_checks"] += 1
                            if sub[i][2] != v:
                                failures.append(("A_witness_not_root_hole", len(G), v, x, sub, i))
                        for i, j in itertools.combinations(IA, 2):
                            stats["A_witness_clique_pair_checks"] += 1
                            if not G.has_edge(witnesses[i], witnesses[j]):
                                failures.append(("A_witness_pair_missing", len(G), v, x, sub, i, j))

    summary = {
        "d2c_isomorphism_classes": len(graphs),
        "statistics": dict(stats),
        "failures": len(failures),
        "failure_examples": failures[:20],
        "trust_boundary": (
            "Graph-atlas audit only. Boolean-code conclusions, U/A witness "
            "capacity bounds, and eventual/asymptotic statements are not "
            "proved by this scan."
        ),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
