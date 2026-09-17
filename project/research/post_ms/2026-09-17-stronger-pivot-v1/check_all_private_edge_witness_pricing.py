#!/usr/bin/env python3
"""Regression for ALL_PRIVATE_EDGE_WITNESS_PRICING.md.

This is evidence, not a proof.  It checks:
  * every all-private maximum-degree triangle root in the NetworkX graph atlas
    through order 7 against APW and the explicit edge-witness charging map;
  * the dense second-extremal arithmetic for 14 <= n <= 5000.
"""

from __future__ import annotations

import json
import math
import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if G.number_of_nodes() < 3 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def M(n: int) -> int:
    return ((n - 1) ** 2) // 4 + 1


def atlas_regression(out: dict) -> None:
    for G0 in nx.graph_atlas_g():
        n = G0.number_of_nodes()
        if n < 3 or n > 7:
            continue
        G = nx.convert_node_labels_to_integers(G0)
        if not is_d2c(G):
            continue

        out["d2c_isomorphism_classes"] += 1
        Delta = max(dict(G.degree()).values())

        for v in [u for u, deg in G.degree() if deg == Delta]:
            B = set(G.neighbors(v))
            A = set(G.nodes()) - B - {v}
            GB = G.subgraph(B)
            Q = GB.number_of_edges()
            if Q == 0:
                continue

            out["maximum_degree_triangle_roots"] += 1
            T = {u for u in B if GB.degree(u) > 0}

            private = {}
            for u in T:
                candidates = [x for x in A if (set(G.neighbors(x)) & B) == {u}]
                if not candidates:
                    break
                private[u] = min(candidates)
            else:
                out["all_private_roots"] += 1
                b = len(B)
                t = len(T)
                C = t * (t - 1) // 2
                s = C - Q
                delta = b * (n - b) - G.number_of_edges()
                X = set(private.values())
                assert len(X) == t
                Y = A - X
                d = C - G.subgraph(X).number_of_edges()
                E = sum(1 for y in Y for w in B if not G.has_edge(y, w))

                if delta - s < t * (b - t) + d:
                    out["strong_payment_violations"] += 1
                    out["result"] = "FAIL"

                apw_rhs = C + 2 * s + 2 * t * (b - t)
                if 3 * delta < apw_rhs:
                    out["apw_violations"] += 1
                    out["result"] = "FAIL"

                charges = []
                for u0, w0 in GB.edges():
                    found = None
                    for u, w in ((u0, w0), (w0, u0)):
                        for z in A:
                            if not G.has_edge(z, u) or G.has_edge(z, w):
                                continue
                            common = set(nx.common_neighbors(G, z, w))
                            if common == {u}:
                                found = (u, w, z)
                                break
                        if found is not None:
                            break
                    if found is None:
                        out["missing_edge_witnesses"] += 1
                        out["result"] = "FAIL"
                        continue

                    u, w, z = found
                    if z == private[u]:
                        if G.has_edge(private[u], private[w]):
                            out["invalid_type1_charges"] += 1
                            out["result"] = "FAIL"
                        charge = ("F", min(u, w), max(u, w))
                    else:
                        if z in X or z not in Y or G.has_edge(z, w):
                            out["invalid_type2_charges"] += 1
                            out["result"] = "FAIL"
                        charge = ("AB", z, w)
                    charges.append(charge)

                if len(charges) != Q or len(set(charges)) != Q:
                    out["charge_injectivity_violations"] += 1
                    out["result"] = "FAIL"

                if Q > d + E:
                    out["charge_budget_violations"] += 1
                    out["result"] = "FAIL"

                out["profiles"].append(
                    {
                        "n": n,
                        "b": b,
                        "t": t,
                        "Q": Q,
                        "delta": delta,
                        "s": s,
                        "d": d,
                        "E": E,
                        "apw_rhs": apw_rhs,
                    }
                )


def dense_arithmetic_regression(out: dict) -> None:
    for n in range(14, 5001):
        m0 = M(n) + 1
        bmin = math.ceil(2 * m0 / n)
        for b in range(bmin, n):
            delta_upper = b * (n - b) - m0
            if b < 7:
                out["dense_arithmetic_violations"] += 1
                out["result"] = "FAIL"
                return

            # APW with s>=0 is weakest at the minimum of the concave
            # Phi_b(t)=C(t,2)+2t(b-t), attained at t=2 or t=b.
            phi2 = 4 * b - 7
            phib = b * (b - 1) // 2
            phi_min = min(phi2, phib)
            if phi_min != phi2:
                out["endpoint_minimum_violations"] += 1
                out["result"] = "FAIL"
                return

            # If an all-private root existed then 3*delta >= phi_min.
            # delta is maximized at the smallest allowed m, namely m0.
            if 3 * delta_upper >= phi_min:
                out["dense_arithmetic_violations"] += 1
                out["first_dense_failure"] = {
                    "n": n,
                    "b": b,
                    "m0": m0,
                    "delta_upper": delta_upper,
                    "phi_min": phi_min,
                }
                out["result"] = "FAIL"
                return

    out["dense_checked_through_n"] = 5000


def main() -> None:
    out = {
        "result": "PASS",
        "atlas_max_order": 7,
        "d2c_isomorphism_classes": 0,
        "maximum_degree_triangle_roots": 0,
        "all_private_roots": 0,
        "strong_payment_violations": 0,
        "apw_violations": 0,
        "missing_edge_witnesses": 0,
        "invalid_type1_charges": 0,
        "invalid_type2_charges": 0,
        "charge_injectivity_violations": 0,
        "charge_budget_violations": 0,
        "endpoint_minimum_violations": 0,
        "dense_arithmetic_violations": 0,
        "profiles": [],
    }

    atlas_regression(out)
    dense_arithmetic_regression(out)

    print(json.dumps(out, indent=2, sort_keys=True))
    if out["result"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
