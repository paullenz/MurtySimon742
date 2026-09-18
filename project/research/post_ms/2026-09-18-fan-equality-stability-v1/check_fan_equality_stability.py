#!/usr/bin/env python3
"""Independent graph-atlas audit for fan equality/stability kernels.

This checker audits only the generic graph-theoretic statements that do not
require reconstructing the partial-Boolean core:

* unique-common-neighbour fan hole normal form;
* the threshold head-or-hole stability inequality, conditional on every
  present witness-witness edge being non-direct (the live Boolean setting
  guarantees this because same-code witnesses share tight-core neighbours);
* zero-hole fan clean-head/direct-matching conclusion under the same condition;
* the generic false-twin private-certifier / sparse-common-side theorem.

It is audit support only, not a proof of the Boolean/Hamming consequences or
of any eventual second-extremal theorem.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict

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


def nbrs(G: nx.Graph, x: int) -> set[int]:
    return set(G.neighbors(x))


def main() -> None:
    graphs = [G.copy() for G in nx.graph_atlas_g() if is_d2c(G)]
    stats = Counter()
    failures: list[tuple] = []

    # ------------------------------------------------------------------
    # Unique-common-neighbour fan stability.
    # ------------------------------------------------------------------
    for G in graphs:
        V = set(G)
        n = len(G)

        for x in G:
            Nx = nbrs(G, x)
            certs: list[tuple[int, int]] = []  # (head, witness)

            for w in G:
                if w == x or G.has_edge(x, w):
                    continue
                common = Nx & nbrs(G, w)
                if len(common) != 1:
                    continue
                h = next(iter(common))
                certs.append((h, w))

            # Enumerate small fans with distinct heads and witnesses. Atlas
            # order <=7 keeps this finite.
            for r in range(2, len(certs) + 1):
                for sub in itertools.combinations(certs, r):
                    heads = [h for h, _ in sub]
                    witnesses = [w for _, w in sub]
                    if len(set(heads)) != r or len(set(witnesses)) != r:
                        continue

                    # In the live Boolean application every present W-edge is
                    # non-direct because all witnesses share p>=1 tight-core
                    # neighbours. Impose exactly that hypothesis here.
                    if any(
                        G.has_edge(witnesses[i], witnesses[j])
                        and not (nbrs(G, witnesses[i]) & nbrs(G, witnesses[j]))
                        for i, j in itertools.combinations(range(r), 2)
                    ):
                        continue

                    stats["admissible_ucn_fans"] += 1
                    Y = V - {x} - Nx
                    g: list[int] = []
                    t: list[int] = []

                    for h, w in sub:
                        Z = V - {x, w} - Nx - nbrs(G, w)
                        gi = len(Z)
                        ti = len((nbrs(G, h) & Y) - {w})
                        g.append(gi)
                        t.append(ti)

                        # Exact witness-neighbourhood normal form.
                        expected = {h} | (Y - {w} - Z)
                        stats["exact_neighbourhood_checks"] += 1
                        if nbrs(G, w) != expected:
                            failures.append(
                                ("exact_witness_neighbourhood", n, x, h, w)
                            )

                    Gmass = sum(g)
                    missing = sum(
                        1
                        for i, j in itertools.combinations(range(r), 2)
                        if not G.has_edge(witnesses[i], witnesses[j])
                    )
                    stats["witness_missing_edge_checks"] += 1
                    if 2 * missing > Gmass:
                        failures.append(
                            ("witness_missing_edge_bound", n, x, r, Gmass, missing)
                        )

                    # Threshold stability.
                    for tau in range(0, max(g + [0]) + 3):
                        bad = [
                            i for i in range(r) if g[i] <= tau and t[i] > tau
                        ]
                        stats["threshold_stability_checks"] += 1
                        if len(bad) * (len(bad) - 1) > 3 * Gmass:
                            failures.append(
                                (
                                    "threshold_bad_set",
                                    n,
                                    x,
                                    r,
                                    tau,
                                    Gmass,
                                    g,
                                    t,
                                )
                            )

                        high = sum(1 for gi in g if gi > tau)
                        if high * (tau + 1) > Gmass:
                            failures.append(
                                ("high_hole_markov", n, x, r, tau, Gmass, g)
                            )

                        R = math.floor((1 + math.sqrt(1 + 12 * Gmass)) / 2)
                        good = sum(
                            1
                            for i in range(r)
                            if g[i] <= tau and t[i] <= tau
                        )
                        lower = r - Gmass // (tau + 1) - R
                        if good < lower:
                            failures.append(
                                (
                                    "good_index_count",
                                    n,
                                    x,
                                    r,
                                    tau,
                                    Gmass,
                                    good,
                                    lower,
                                )
                            )

                    # Exact zero-hole consequence.
                    if Gmass == 0:
                        stats["zero_hole_fans"] += 1
                        non_direct_matching = 0
                        for h, w in sub:
                            if nbrs(G, h) & nbrs(G, w):
                                non_direct_matching += 1
                        if non_direct_matching > 1:
                            failures.append(
                                (
                                    "zero_hole_more_than_one_dirty_head",
                                    n,
                                    x,
                                    sub,
                                    t,
                                )
                            )

    # ------------------------------------------------------------------
    # Generic false-twin quotient theorem.
    # ------------------------------------------------------------------
    for G in graphs:
        n = len(G)
        classes: dict[frozenset[int], list[int]] = defaultdict(list)
        for y in G:
            classes[frozenset(nbrs(G, y))].append(y)

        for W_key, twins in classes.items():
            if len(twins) < 2:
                continue
            W = set(W_key)
            D = set(twins)
            d = len(D)
            w = len(W)
            if w < 2:
                continue

            stats["false_twin_classes"] += 1

            private: set[int] = set()
            for q in set(G) - W - D:
                inter = nbrs(G, q) & W
                if len(inter) == 1:
                    private |= inter

            for z in W:
                stats["false_twin_vertex_checks"] += 1
                if z in private:
                    continue
                internal_degree = len(nbrs(G, z) & W)
                internal_nondegree = (w - 1) - internal_degree
                if internal_degree > 0 and internal_nondegree < d:
                    failures.append(
                        (
                            "false_twin_private_sparse_dichotomy",
                            n,
                            tuple(sorted(D)),
                            z,
                            d,
                            w,
                            internal_degree,
                            internal_nondegree,
                        )
                    )

            ebar = sum(
                1
                for a, b in itertools.combinations(W, 2)
                if not G.has_edge(a, b)
            )
            lower_twice = min(d, w - 1) * max(0, 2 * w + d - n)
            stats["false_twin_global_floor_checks"] += 1
            if 2 * ebar < lower_twice:
                failures.append(
                    (
                        "false_twin_global_floor",
                        n,
                        tuple(sorted(D)),
                        d,
                        w,
                        ebar,
                        lower_twice,
                    )
                )

    summary = {
        "d2c_isomorphism_classes": len(graphs),
        "statistics": dict(stats),
        "failures": len(failures),
        "failure_examples": failures[:20],
        "trust_boundary": (
            "Graph-atlas audit only. The Boolean-code/Hamming statements, "
            "the identification of zero-hole A/U witnesses with U, and all "
            "asymptotic/eventual claims remain outside this finite audit."
        ),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
