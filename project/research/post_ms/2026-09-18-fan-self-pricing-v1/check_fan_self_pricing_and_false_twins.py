#!/usr/bin/env python3
"""Exact audit support for the self-priced fan and false-twin support package.

This checker is deliberately secondary to the hand proofs in:
  SELF_PRICED_COMPLEMENT_PAIR_FANS_AND_ROOTED_GATE.md
  FALSE_TWIN_PRIVATE_SUPPORT_AND_BIPARTITE_STABILITY.md

It checks:
  1. exact inversion of the aligned-code self-pricing quadratic;
  2. the substitution M_P <= R_code(S_P) into the pair fan inequality;
  3. the false-twin private-support and strengthened missing-edge floor
     on every diameter-2-critical graph in NetworkX's graph atlas (n <= 7).
"""

from __future__ import annotations

from collections import defaultdict
from math import isqrt

import networkx as nx


def r_code(D0: int, s: int) -> int:
    """floor((D0 + sqrt(D0^2 + 12s))/3), clipped at zero."""
    q = D0 * D0 + 12 * s
    r = (D0 + isqrt(q)) // 3
    return max(0, r)


def audit_aligned_code_inversion() -> tuple[int, int]:
    checks = failures = 0
    for D0 in range(-30, 81):
        for s in range(301):
            R = r_code(D0, s)
            for w in range(101):
                # AC1 is equivalent to 4s >= max(0, w(3w-2D0)).
                if 4 * s >= max(0, w * (3 * w - 2 * D0)):
                    checks += 1
                    if w > R:
                        failures += 1
    return checks, failures


def audit_self_priced_fan_substitution() -> tuple[int, int]:
    """Audit: if PFC3 holds for any M <= R_code(s), SPF holds with R_code(s)."""
    checks = failures = 0
    for D0 in range(-15, 46, 3):
        for L in range(1, 16):
            for T in range(-10, 21, 3):
                for s in range(0, 81, 2):
                    R = r_code(D0, s)
                    for M in range(R + 1):
                        # Clear denominators in
                        # d(2d-T-1) <= (1+2M/L)s.
                        for d in range(21):
                            lhs = L * d * (2 * d - T - 1)
                            if lhs <= (L + 2 * M) * s:
                                checks += 1
                                if lhs > (L + 2 * R) * s:
                                    failures += 1
    return checks, failures


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


def false_twin_classes(G: nx.Graph):
    groups = defaultdict(list)
    for v in G:
        groups[frozenset(G.neighbors(v))].append(v)
    for W, D in groups.items():
        if len(D) >= 2:
            yield set(D), set(W)


def audit_false_twin_support():
    d2c_graphs = 0
    twin_classes = 0
    active_vertices = 0
    private_witness_checks = 0
    support_cap_checks = 0
    missing_floor_checks = 0
    failures = 0

    for G0 in nx.graph_atlas_g():
        if len(G0) > 7:
            continue
        G = nx.Graph(G0)
        if not is_d2c(G):
            continue
        d2c_graphs += 1

        for D, W in false_twin_classes(G):
            twin_classes += 1
            d = len(D)
            w = len(W)
            Z = set(G) - D - W
            z = len(Z)
            Wplus = {x for x in W if any(y in W for y in G.neighbors(x))}
            active_vertices += len(Wplus)

            # FT1/FT2. For different x the singleton condition makes the
            # witness candidate sets automatically disjoint, so existence
            # for each x is enough to establish an injection.
            for x in Wplus:
                private_witness_checks += 1
                ok = any((set(G.neighbors(y)) & W) == {x} for y in Z)
                if not ok:
                    failures += 1

            # FT4.
            support_cap_checks += 1
            eW = G.subgraph(W).number_of_edges()
            cap = min(w, z) * (min(w, z) - 1) // 2
            if eW > cap:
                failures += 1

            # FT5.
            missing_floor_checks += 1
            missing2 = w * (w - 1) - 2 * eW
            floor2 = max(0, d + 2 * w - len(G)) * (len(G) - d - 1)
            if missing2 < floor2:
                failures += 1

    return {
        "d2c_atlas_graphs": d2c_graphs,
        "false_twin_classes": twin_classes,
        "internally_active_W_vertices": active_vertices,
        "private_witness_checks": private_witness_checks,
        "support_cap_checks": support_cap_checks,
        "strengthened_missing_floor_checks": missing_floor_checks,
        "failures": failures,
    }


def main() -> None:
    inv_checks, inv_fail = audit_aligned_code_inversion()
    fan_checks, fan_fail = audit_self_priced_fan_substitution()
    twins = audit_false_twin_support()

    print("aligned_code_inversion_checks", inv_checks)
    print("aligned_code_inversion_failures", inv_fail)
    print("self_priced_fan_primitive_checks", fan_checks)
    print("self_priced_fan_primitive_failures", fan_fail)
    for key, value in twins.items():
        print(key, value)

    total_failures = inv_fail + fan_fail + twins["failures"]
    if total_failures:
        raise SystemExit(f"FAIL: {total_failures} audit failures")
    print("PASS")


if __name__ == "__main__":
    main()
