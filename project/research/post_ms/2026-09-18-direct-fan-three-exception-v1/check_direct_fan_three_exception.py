#!/usr/bin/env python3
"""Independent audit support for DIRECT_FAN_BOUNDED_SURPLUS_THREE_EXCEPTION_GATE.md.

The hand proofs in the theorem note are authoritative.  This script checks the
integer inequalities and small exact z=3 false-twin quotient models used as
regression diagnostics.
"""

from collections import Counter
from itertools import product
from math import comb

import networkx as nx


def M(n: int) -> int:
    return ((n - 1) ** 2) // 4 + 1


def check_integer_envelopes(limit: int = 120) -> Counter:
    c = Counter()

    # Rooted direct fans satisfy w>=d.  Check the independent-W envelopes.
    for d in range(2, limit + 1):
        for w in range(d, limit + 1):
            n2 = d + w + 2
            n3 = d + w + 3
            for eta in range(d - 1):  # 0 <= eta <= d-2
                c["z2_independent"] += 1
                assert d * w + eta + 3 <= M(n2)

                c["z3_one_edge_independent"] += 1
                assert d * w + w + eta + 3 <= M(n3)

            c["z3_path_or_triangle_independent"] += 1
            assert d * w + w + 4 <= M(n3)

    # Active-W z=2 criterion, valid from n>=7.
    for n in range(7, 2 * limit + 1):
        h = n // 2
        for w in range(2, n - 1):
            B = n * n // 4 - w * (n - w)
            c["z2_active"] += 1
            assert B + 2 * w - 4 >= h - 1

    # Active-W z=3 criterion, valid from n>=11.
    for n in range(11, 2 * limit + 1):
        h = n // 2
        for w in range(2, n - 1):
            B = n * n // 4 - w * (n - w)
            c["z3_active_t2"] += 1
            assert B + 2 * w - 6 >= h - 1
            if w >= 3:
                c["z3_active_t3"] += 1
                assert B + 3 * (w - 1) - 3 - 3 >= h - 1

    return c


def check_path_incidence(limit: int = 30) -> int:
    """Check E<=eta+2 from (BH27)-(BH28)."""
    checks = 0
    for A in range(limit + 1):
        for B in range(limit + 1):
            for C in range(limit + 1):
                if A + B == 0:
                    continue
                if A + C == 0 or B + C == 0:
                    continue
                eta = max(
                    A * (A + C - 1) if A else 0,
                    B * (B + C - 1) if B else 0,
                )
                E = A + B + C
                checks += 1
                assert E <= eta + 2
    return checks


def check_triangle_incidence(limit: int = 12) -> int:
    """Check the K3 high-type inequality E<=eta+1.

    Coordinates 1 and 2 are assumed to have singleton W-types, as forced by
    the vertex-cover argument for the three Z-edges.
    """
    checks = 0
    for a12 in range(limit + 1):
        for a13 in range(limit + 1):
            for a23 in range(limit + 1):
                for a123 in range(limit + 1):
                    X1 = a12 + a13 + a123
                    X2 = a12 + a23 + a123
                    eta = max(X1 * X1, X2 * X2)
                    E = a12 + a13 + a23 + 2 * a123
                    checks += 1
                    assert E <= eta + 1
    return checks


def build_false_twin_z3(d, mults, z_edges):
    G = nx.Graph()
    D = [("d", i) for i in range(d)]
    Z = [("z", i) for i in range(3)]
    G.add_nodes_from(D + Z)
    for mask, multiplicity in enumerate(mults, start=1):
        for k in range(multiplicity):
            w = ("w", mask, k)
            G.add_node(w)
            for u in D:
                G.add_edge(u, w)
            for i in range(3):
                if (mask >> i) & 1:
                    G.add_edge(w, ("z", i))
    for i, j in z_edges:
        G.add_edge(("z", i), ("z", j))
    return G


def is_d2c(G) -> bool:
    if not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for u, v in list(G.edges()):
        H = G.copy()
        H.remove_edge(u, v)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def exact_z3_regression(max_multiplicity: int = 2):
    """Exhaust exact eta=0, z=3 quotient models with small type multiplicity.

    This is not used as proof.  It checks that every triangle-containing D2C
    model encountered obeys m<=M(n).
    """
    all_z_edges = [(0, 1), (0, 2), (1, 2)]
    checked = d2c = triangular = 0
    by_z_edge_count = Counter()

    for bits in range(8):
        z_edges = [all_z_edges[i] for i in range(3) if (bits >> i) & 1]
        for mults in product(range(max_multiplicity + 1), repeat=7):
            if sum(mults) == 0:
                continue
            # Every Z-vertex must have a W-neighbour to be at distance two
            # from the false-twin class.
            if any(
                sum(m for mask, m in enumerate(mults, start=1) if (mask >> i) & 1) == 0
                for i in range(3)
            ):
                continue
            checked += 1
            G = build_false_twin_z3(2, mults, z_edges)
            if not is_d2c(G):
                continue
            d2c += 1
            if not any(nx.triangles(G, u) for u in G):
                continue
            triangular += 1
            by_z_edge_count[len(z_edges)] += 1
            assert G.number_of_edges() <= M(G.number_of_nodes())

    return {
        "checked": checked,
        "d2c": d2c,
        "triangle_containing_d2c": triangular,
        "triangle_d2c_by_z_edge_count": dict(by_z_edge_count),
    }


def main():
    envelope = check_integer_envelopes()
    path_checks = check_path_incidence()
    triangle_checks = check_triangle_incidence()
    exact = exact_z3_regression()

    total = sum(envelope.values()) + path_checks + triangle_checks + exact["checked"]
    print("DIRECT_FAN_THREE_EXCEPTION_AUDIT_OK")
    print("integer_envelopes", dict(envelope))
    print("path_incidence_checks", path_checks)
    print("triangle_incidence_checks", triangle_checks)
    print("exact_z3_regression", exact)
    print("total_checks", total)


if __name__ == "__main__":
    main()
