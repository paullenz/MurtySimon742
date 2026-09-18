#!/usr/bin/env python3
"""Finite regression for BOOLEAN_ANTIPODE_FAN_PAYMENT.md.

Scans all NetworkX graph-atlas D2C graphs through order seven at every
maximum-degree root. Tight rooted B-antipodes are extracted, their endpoints
are removed to obtain U, and every U-U antipode fan is checked whenever at
least one tight pair is present.

Regression targets:

  sum_{y in Y} eta(yz) >= C(|Y|,2) + nonedges(G[Y]),

and the partial-Boolean consequence that every U-U antipode partner of one
centre chooses the opposite endpoint in every tight fibre.

This is regression evidence only; the hand proof is the mathematical basis.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter

import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if len(G) < 3 or not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for edge in list(G.edges()):
        H = G.copy()
        H.remove_edge(*edge)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def is_antipode(G: nx.Graph, v, x, y) -> bool:
    return (
        not G.has_edge(x, y)
        and set(G.neighbors(x)) & set(G.neighbors(y)) == {v}
    )


def eta(G: nx.Graph, v, x, y) -> int:
    return sum(
        1
        for z in G.nodes()
        if z not in {v, x, y}
        and not G.has_edge(z, x)
        and not G.has_edge(z, y)
    )


def main() -> None:
    stats = Counter()
    violations = []
    fibre_violations = []
    examples = []
    min_margin = None

    for G in nx.graph_atlas_g():
        if len(G) < 3 or not is_d2c(G):
            continue

        stats["d2c_graphs"] += 1
        stats[f"d2c_n{len(G)}"] += 1
        Delta = max(dict(G.degree()).values())

        for v in G.nodes():
            if G.degree(v) != Delta:
                continue
            stats["maximum_degree_roots"] += 1
            B = set(G.neighbors(v))

            tight = []
            for x, y in itertools.combinations(B, 2):
                if is_antipode(G, v, x, y) and eta(G, v, x, y) == 0:
                    tight.append((x, y))

            endpoints = [x for pair in tight for x in pair]
            if len(endpoints) != len(set(endpoints)):
                raise AssertionError("tight antipodes failed matching property")
            if not tight:
                continue

            stats["roots_with_tight_pair"] += 1
            U = B - set(endpoints)

            for z in U:
                Y = [y for y in U if y != z and is_antipode(G, v, z, y)]
                if not Y:
                    continue

                stats["fan_centres"] += 1
                stats["fan_partner_incidences"] += len(Y)
                if len(Y) >= 2:
                    stats["branching_fan_centres"] += 1

                # Every partner must choose the endpoint opposite z in every
                # tight fibre. This is the finite shadow of the Boolean-code
                # complement statement used in the proof.
                for y in Y:
                    for r, s in tight:
                        z_pattern = (G.has_edge(z, r), G.has_edge(z, s))
                        y_pattern = (G.has_edge(y, r), G.has_edge(y, s))
                        if (
                            sum(z_pattern) != 1
                            or sum(y_pattern) != 1
                            or z_pattern == y_pattern
                        ):
                            fibre_violations.append(
                                {
                                    "n": len(G),
                                    "root": v,
                                    "centre": z,
                                    "partner": y,
                                    "tight_pair": [r, s],
                                    "centre_pattern": z_pattern,
                                    "partner_pattern": y_pattern,
                                }
                            )

                err = sum(eta(G, v, z, y) for y in Y)
                nonedges = sum(
                    1
                    for y1, y2 in itertools.combinations(Y, 2)
                    if not G.has_edge(y1, y2)
                )
                rhs = len(Y) * (len(Y) - 1) // 2 + nonedges
                margin = err - rhs
                min_margin = margin if min_margin is None else min(min_margin, margin)

                if margin < 0:
                    violations.append(
                        {
                            "n": len(G),
                            "root": v,
                            "centre": z,
                            "fan_degree": len(Y),
                            "eta_sum": err,
                            "partner_nonedges": nonedges,
                            "margin": margin,
                        }
                    )

                examples.append(
                    {
                        "n": len(G),
                        "b": Delta,
                        "lambda": 2 * Delta - len(G),
                        "tight_pairs": len(tight),
                        "u": len(U),
                        "fan_degree": len(Y),
                        "eta_sum": err,
                        "partner_nonedges": nonedges,
                        "margin": margin,
                    }
                )

    summary = {
        "scope": "NetworkX graph atlas, all D2C isomorphism classes through order 7, every maximum-degree root",
        "d2c_graphs": stats["d2c_graphs"],
        "d2c_by_order": {str(n): stats[f"d2c_n{n}"] for n in range(3, 8)},
        "maximum_degree_roots": stats["maximum_degree_roots"],
        "roots_with_tight_pair": stats["roots_with_tight_pair"],
        "fan_centres": stats["fan_centres"],
        "branching_fan_centres": stats["branching_fan_centres"],
        "fan_partner_incidences": stats["fan_partner_incidences"],
        "minimum_integer_margin": min_margin,
        "fibre_violations": fibre_violations,
        "fan_inequality_violations": violations,
        "fan_examples": examples,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

    assert not fibre_violations
    assert not violations


if __name__ == "__main__":
    main()
