#!/usr/bin/env python3
"""Independent small-graph audit for the A-edge fan geometry package.

This checker intentionally audits only the generic graph-theoretic kernels:

* direct-fan independence;
* exact direct-fan hole representation relative to a maximum-degree root;
* external unique-common-neighbour hole counts;
* the off-diagonal induced-matching rule for two certificates sharing a source.

It does not prove the partial-Boolean degree formulas or any asymptotic theorem.
"""

from __future__ import annotations

import itertools
import json
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


def main() -> None:
    graphs = [G.copy() for G in nx.graph_atlas_g() if is_d2c(G)]
    stats = Counter()
    failures: list[tuple] = []

    for G in graphs:
        n = len(G)
        b = max(dict(G.degree()).values())
        lam = 2 * b - n

        for v, dv in G.degree():
            if dv != b:
                continue

            A = [x for x in G if x != v and not G.has_edge(v, x)]

            # Direct fans.
            for x in A:
                Y = [
                    y
                    for y in A
                    if G.has_edge(x, y)
                    and not (set(G.neighbors(x)) & set(G.neighbors(y)))
                ]
                if Y:
                    stats["direct_fans"] += 1
                    stats["direct_fan_incidences"] += len(Y)

                for y, y2 in itertools.combinations(Y, 2):
                    stats["direct_fan_leaf_pairs"] += 1
                    if G.has_edge(y, y2):
                        failures.append(("direct_fan_not_independent", n, v, x, y, y2))

                W = set(G) - {v} - set(G.neighbors(x))
                for y in Y:
                    holes = W - set(G.neighbors(y))
                    expected = (b - G.degree(x)) + (b - G.degree(y)) - (lam + 1)
                    stats["direct_hole_identities"] += 1
                    if len(holes) != expected:
                        failures.append(
                            (
                                "direct_hole_count",
                                n,
                                v,
                                x,
                                y,
                                len(holes),
                                expected,
                            )
                        )
                    if set(G.neighbors(y)) != W - holes:
                        failures.append(("direct_partition_identity", n, v, x, y))

                for y, y2 in itertools.combinations(Y, 2):
                    H1 = W - set(G.neighbors(y))
                    H2 = W - set(G.neighbors(y2))
                    sym = len(set(G.neighbors(y)) ^ set(G.neighbors(y2)))
                    if sym > len(H1) + len(H2):
                        failures.append(("direct_symmetric_difference", n, v, x, y, y2))

            # External UCN fans sharing an A-source.
            for z in A:
                certs: list[tuple[int, int]] = []
                for w in G:
                    if w in (z, v) or G.has_edge(z, w):
                        continue
                    common = set(G.neighbors(z)) & set(G.neighbors(w))
                    if len(common) != 1:
                        continue
                    h = next(iter(common))
                    certs.append((w, h))

                    external_holes = (
                        set(G)
                        - {z, w}
                        - set(G.neighbors(z))
                        - set(G.neighbors(w))
                    )
                    expected = (b - G.degree(z)) + (b - G.degree(w)) - (lam + 1)
                    stats["ucn_pairs"] += 1
                    if len(external_holes) != expected:
                        failures.append(
                            (
                                "ucn_hole_count",
                                n,
                                v,
                                z,
                                w,
                                h,
                                len(external_holes),
                                expected,
                            )
                        )

                for (w, h), (w2, h2) in itertools.combinations(certs, 2):
                    if w == w2 or h == h2:
                        continue
                    stats["fan_pair_tests"] += 1
                    if G.has_edge(w, h2) or G.has_edge(w2, h):
                        failures.append(("off_diagonal_matching_failure", n, v, z, w, h, w2, h2))

                    if not G.has_edge(w, w2):
                        stats["nonadjacent_witness_pair_hole_tests"] += 1
                        holes1 = (
                            set(G)
                            - {z, w}
                            - set(G.neighbors(z))
                            - set(G.neighbors(w))
                        )
                        holes2 = (
                            set(G)
                            - {z, w2}
                            - set(G.neighbors(z))
                            - set(G.neighbors(w2))
                        )
                        if w2 not in holes1 or w not in holes2:
                            failures.append(("witness_pair_not_holes", n, v, z, w, w2))

    summary = {
        "d2c_isomorphism_classes": len(graphs),
        "statistics": dict(stats),
        "failures": len(failures),
        "failure_examples": failures[:20],
        "trust_boundary": (
            "Graph-atlas audit only; this does not prove the partial-Boolean "
            "degree formulas or the fan-capacity theorems."
        ),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
