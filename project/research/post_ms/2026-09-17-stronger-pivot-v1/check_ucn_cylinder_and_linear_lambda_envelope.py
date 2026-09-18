#!/usr/bin/env python3
"""Regression support for the 18 Sep UCN/cylinder and linear-lambda checkpoint.

This checker is audit support only.  The mathematical claims are the hand
counting arguments in

- UNIQUE_COMMON_NEIGHBOR_SLACK_AND_CYLINDER_CRITICALITY.md
- LINEAR_LAMBDA_COARSE_ENVELOPE_FROM_ALPHA_BETA_COERCIVITY.md

Checks:
1. the unique-common-neighbour slack/hole identity on every graph-atlas graph
   of orders 3..7;
2. the standard critical triangle-edge witness property on every D2C graph in
   the same atlas range;
3. exact rational negativity of the theta=13/4 envelope polynomial on a dense
   grid of rho in [27/14,2], plus the theta_- / high-regime ordering.
"""

from fractions import Fraction
import itertools
import json
import math

import networkx as nx


def common_neighbors(G, u, v):
    return set(G[u]) & set(G[v])


def is_d2c(G):
    if len(G) < 2 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def main():
    atlas = [G for G in nx.graph_atlas_g() if 3 <= len(G) <= 7]

    ucn_pairs = 0
    ucn_failures = []
    for G in atlas:
        n = len(G)
        b = max(dict(G.degree()).values())
        lam = 2 * b - n
        eps = {v: b - G.degree(v) for v in G}
        for z, w in itertools.combinations(G.nodes(), 2):
            if G.has_edge(z, w):
                continue
            if len(common_neighbors(G, z, w)) != 1:
                continue
            ucn_pairs += 1
            holes = set(G.nodes()) - {z, w} - set(G[z]) - set(G[w])
            rhs = eps[z] + eps[w] - (lam + 1)
            if len(holes) != rhs:
                ucn_failures.append((len(G), z, w, len(holes), rhs))

    d2c = [G for G in atlas if is_d2c(G)]
    triangle_edges = 0
    witness_failures = []
    for G in d2c:
        for x, z in G.edges():
            if not common_neighbors(G, x, z):
                continue
            triangle_edges += 1
            ok = False
            for w in G.nodes():
                if w in (x, z):
                    continue
                if (not G.has_edge(x, w)
                        and common_neighbors(G, x, w) == {z}):
                    ok = True
                if (not G.has_edge(z, w)
                        and common_neighbors(G, z, w) == {x}):
                    ok = True
            if not ok:
                witness_failures.append((len(G), x, z))

    grid_points = 10001
    envelope_failures = []
    minimum_root_gap = float("inf")
    maximum_theta_13_margin = -float("inf")
    lo = Fraction(27, 14)
    hi = Fraction(2, 1)

    for j in range(grid_points):
        rho = lo + (hi - lo) * Fraction(j, grid_points - 1)

        # At theta=13/4 the LCE margin is exactly
        # 7(32 rho^2 - 72 rho + 15)/96 and must be negative.
        margin = Fraction(7, 96) * (32 * rho * rho - 72 * rho + 15)
        maximum_theta_13_margin = max(maximum_theta_13_margin, float(margin))
        if not margin < 0:
            envelope_failures.append(("theta_13_4_sign", j, str(rho), str(margin)))

        rf = float(rho)
        theta_minus = (
            5 * rf + 7 - math.sqrt(11 * rf * rf + 4 * rf + 1)
        ) / 3
        high_regime = 2 + rf * (1 - 1 / math.sqrt(2))
        minimum_root_gap = min(minimum_root_gap, theta_minus - high_regime)
        if theta_minus + 1e-12 < high_regime:
            envelope_failures.append(("root_below_regime", j, rf, theta_minus, high_regime))
        if theta_minus >= 13 / 4 + 1e-12:
            envelope_failures.append(("root_not_below_13_4", j, rf, theta_minus))

    failures = len(ucn_failures) + len(witness_failures) + len(envelope_failures)
    summary = {
        "graph_atlas_graphs_orders_3_to_7": len(atlas),
        "unique_common_neighbour_pairs_checked": ucn_pairs,
        "unique_common_neighbour_failures": len(ucn_failures),
        "d2c_graph_atlas_classes": len(d2c),
        "critical_triangle_edges_checked": triangle_edges,
        "critical_triangle_edge_witness_failures": len(witness_failures),
        "linear_lambda_ratio_grid_points": grid_points,
        "linear_lambda_envelope_failures": len(envelope_failures),
        "minimum_theta_minus_minus_high_regime": minimum_root_gap,
        "maximum_theta_13_4_margin": maximum_theta_13_margin,
        "total_failures": failures,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    if failures:
        print("UCN failures:", ucn_failures[:10])
        print("witness failures:", witness_failures[:10])
        print("envelope failures:", envelope_failures[:10])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
