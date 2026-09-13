#!/usr/bin/env python3
"""Deterministic reconnaissance for a maximum-cut reformulation of Murty--Simon.

This is evidence only, never a proof.  It:
1. exhaustively checks every unlabeled graph in NetworkX's graph atlas (orders <= 7);
2. deterministically generates edge-minimal diameter-two graphs at orders 8..12;
3. checks sampled positive blow-ups of C5 through order 30.

For every checked D2C graph and every maximum cut X|Y found, it tests
    |X||Y| - e(G) >= 0,
which is equivalent on that cut to
    (# missing cross pairs) - (# internal edges) >= 0.

The degree-square diagnostic is included only as a negative control: that inequality is
known to be false for D2C graphs in general (Loh--Ma), so its survival here is not evidence
for a universal theorem.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import json
import math
import random

import networkx as nx


SEED = 74220260913


def is_d2c(G: nx.Graph) -> bool:
    if G.number_of_nodes() < 2 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def maximum_cut_records(G: nx.Graph):
    nodes = list(G.nodes())
    first, rest = nodes[0], nodes[1:]
    best = -1
    records = []
    for mask in range(1 << len(rest)):
        X = {first}
        X.update(v for j, v in enumerate(rest) if (mask >> j) & 1)
        cut = sum((u in X) != (v in X) for u, v in G.edges())
        if cut > best:
            best = cut
            records = []
        if cut == best:
            x = len(X)
            y = G.number_of_nodes() - x
            records.append({
                "x": x,
                "y": y,
                "product_minus_edges": x * y - G.number_of_edges(),
            })
    return best, records


def minimize_diameter_two(n: int, p: float, graph_seed: int):
    G = nx.gnp_random_graph(n, p, seed=graph_seed)
    if not nx.is_connected(G) or nx.diameter(G) > 2:
        return None
    rng = random.Random(graph_seed ^ 0x742)
    edges = list(G.edges())
    rng.shuffle(edges)
    # Once an edge is indispensable for diameter <=2, later deletions cannot make it
    # dispensable, because distances only increase.  One pass therefore suffices.
    for e in edges:
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            G = H
    assert is_d2c(G)
    return G


def sampled_positive_compositions(total: int, limit: int, rng: random.Random):
    count = math.comb(total - 1, 4)
    if count <= limit:
        return [
            (a, b-a, c-b, d-c, total-d)
            for a, b, c, d in combinations(range(1, total), 4)
        ]
    out = set()
    while len(out) < limit:
        cuts = sorted(rng.sample(range(1, total), 4))
        out.add((cuts[0], cuts[1]-cuts[0], cuts[2]-cuts[1],
                 cuts[3]-cuts[2], total-cuts[3]))
    return sorted(out)


def c5_blowup_maxcut(weights):
    """Exact maximum cut over a C5 blow-up using cluster split counts.

    The objective is multilinear, and this enumeration also includes split clusters,
    so it does not assume a priori that a maximum cut keeps each twin class intact.
    """
    n = sum(weights)
    m = sum(weights[i] * weights[(i + 1) % 5] for i in range(5))
    best = -1
    products = []
    for xs in product(*[range(w + 1) for w in weights]):
        cut = 0
        for i in range(5):
            j = (i + 1) % 5
            ai, aj = weights[i], weights[j]
            xi, xj = xs[i], xs[j]
            cut += xi * (aj - xj) + (ai - xi) * xj
        side = sum(xs)
        xy = side * (n - side)
        if cut > best:
            best, products = cut, [xy]
        elif cut == best:
            products.append(xy)
    return {
        "n": n,
        "m": m,
        "maxcut": best,
        "minimum_product_minus_edges_over_maxcuts": min(products) - m,
        "maximum_product_minus_edges_over_maxcuts": max(products) - m,
    }


def inspect_graph(G: nx.Graph):
    best, cuts = maximum_cut_records(G)
    n, m = G.number_of_nodes(), G.number_of_edges()
    return {
        "n": n,
        "m": m,
        "maxcut": best,
        "number_of_maxcuts_up_to_complement": len(cuts),
        "minimum_product_minus_edges_over_maxcuts":
            min(r["product_minus_edges"] for r in cuts),
        "degree_square_gap":
            sum(d * d for _, d in G.degree()) - n * m,
    }


def main():
    atlas_graphs = [G.copy() for G in nx.graph_atlas_g() if is_d2c(G)]

    rng = random.Random(SEED)
    generated = []
    attempts = Counter()
    for n in range(8, 13):
        for k in range(300):
            p = rng.uniform(0.25, 0.80)
            attempts[n] += 1
            G = minimize_diameter_two(n, p, 100000 * n + k)
            if G is not None:
                generated.append(G)

    graph_records = [
        {"source": "atlas", **inspect_graph(G)} for G in atlas_graphs
    ] + [
        {"source": "deterministic_greedy_random", **inspect_graph(G)}
        for G in generated
    ]

    c5_rng = random.Random(SEED ^ 0xC5)
    c5_records = []
    for total in range(5, 31):
        for weights in sampled_positive_compositions(total, 100, c5_rng):
            c5_records.append({
                "weights": list(weights),
                **c5_blowup_maxcut(weights),
            })

    payload = {
        "schema": "maximum-cut-recon-v1",
        "scope": (
            "Reconnaissance only.  No sampled or exhaustive finite check proves the "
            "maximum-cut inequality or Murty--Simon."
        ),
        "seed": SEED,
        "networkx_version": nx.__version__,
        "atlas": {
            "d2c_graphs": len(atlas_graphs),
            "order_counts": dict(sorted(Counter(
                G.number_of_nodes() for G in atlas_graphs).items())),
        },
        "generated": {
            "attempts": dict(sorted(attempts.items())),
            "d2c_instances": len(generated),
            "order_counts": dict(sorted(Counter(
                G.number_of_nodes() for G in generated).items())),
        },
        "maximum_cut_test": {
            "instances": len(graph_records),
            "violations": sum(
                r["minimum_product_minus_edges_over_maxcuts"] < 0
                for r in graph_records),
            "minimum_margin": min(
                r["minimum_product_minus_edges_over_maxcuts"]
                for r in graph_records),
        },
        "degree_square_negative_control": {
            "violations_in_this_sample": sum(
                r["degree_square_gap"] > 0 for r in graph_records),
            "maximum_gap_in_this_sample": max(
                r["degree_square_gap"] for r in graph_records),
            "warning": (
                "The Caccetta--Haggkvist degree-square inequality is known false "
                "for D2C graphs in general; this diagnostic is not a conjecture."
            ),
        },
        "c5_blowup_test": {
            "sampled_weight_vectors": len(c5_records),
            "orders": [5, 30],
            "violations": sum(
                r["minimum_product_minus_edges_over_maxcuts"] < 0
                for r in c5_records),
            "minimum_margin": min(
                r["minimum_product_minus_edges_over_maxcuts"]
                for r in c5_records),
        },
    }
    print(json.dumps(payload, indent=2))
    with open("MAXCUT_RECON.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main()
