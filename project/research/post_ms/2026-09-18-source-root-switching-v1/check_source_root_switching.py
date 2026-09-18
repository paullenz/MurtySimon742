#!/usr/bin/env python3
"""Audit support for SOURCE_ROOT_SWITCHING_ENVELOPE_AND_WEIGHTED_U_EDGE_CAPACITY.md.

The mathematical claims are proved by hand in the note.  This script only
regresses the algebraic exclusion margins and the rooted triangle-edge
criticality kernel on the NetworkX graph atlas.
"""

from fractions import Fraction
import json
import math
import networkx as nx


def cbe_upper(rho, theta, kappa, r=3):
    A = 2 + rho - theta
    return A * (1 - kappa) + (kappa * kappa / r) * (rho / (1 - kappa)) ** r


def cbl_lower(rho, theta):
    A = 2 + rho - theta
    c = theta * (1 + rho) - theta * theta / 2
    R = min(1.0, math.sqrt(max(0.0, c)))
    return max(0.0, rho - A * R)


def is_d2c(G):
    if len(G) < 2 or not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def main():
    # Exact endpoint certificates used in the hand proofs.
    k = Fraction(13, 20)
    rho = Fraction(4, 25)
    lhs = k - k * k * rho * rho / (3 * (1 - k) ** 3)
    rho16_exact = lhs * lhs - 2 * rho
    assert rho16_exact == Fraction(67447921, 264710250000)
    assert rho16_exact > 0

    two_fifths_exact = Fraction(1171, 2025) ** 2 - Fraction(198, 625)
    assert two_fifths_exact == Fraction(72163, 4100625)
    assert two_fifths_exact > 0

    # Dense grid: rho<=4/25, theta>2 must violate CBL<=CBE at kappa=13/20.
    n_rho16 = 0
    min_rho16 = float("inf")
    min_rho16_at = None
    for ir in range(1, 401):
        rr = (4 / 25) * ir / 400
        for it in range(1, 251):
            th = 2 + rr * it / 251
            margin = cbl_lower(rr, th) - cbe_upper(rr, th, 13 / 20, 3)
            n_rho16 += 1
            if margin < min_rho16:
                min_rho16 = margin
                min_rho16_at = [rr, th]
            assert margin > 0

    # Dense grid: rho<=1/2, theta>=2+2rho/5 violates CBL<=CBE at kappa=2/5.
    n_two_fifths = 0
    min_two_fifths = float("inf")
    min_two_fifths_at = None
    for ir in range(1, 501):
        rr = 0.5 * ir / 500
        th0 = 2 + 0.4 * rr
        for it in range(0, 201):
            th = th0 + (2 + rr - th0) * it / 201
            if th >= 2 + rr:
                continue
            margin = cbl_lower(rr, th) - cbe_upper(rr, th, 2 / 5, 3)
            n_two_fifths += 1
            if margin < min_two_fifths:
                min_two_fifths = margin
                min_two_fifths_at = [rr, th]
            assert margin > 0

    # Quantitative source-root envelope: a small positive kappa already beats
    # the old 2+rho/2 line for every sampled rho>0.
    n_source_root = 0
    kappa = 0.01
    for ir in range(1, 1001):
        rr = 2 * ir / 1000
        cap = (
            4 + rr - (2 + rr) * kappa
            + (kappa * kappa / 3) * (rr / (1 - kappa)) ** 3
        ) / (2 - kappa)
        assert cap < 2 + rr / 2
        n_source_root += 1

    # Independent graph audit of the structural kernel behind (WU): in every
    # D2C graph in the atlas through order seven, every edge inside the
    # neighbourhood of a maximum-degree root admits an A-side oriented
    # unique-common-neighbour certificate, and every such certificate obeys
    # the required slack inequality.
    atlas = [G for G in nx.graph_atlas_g() if len(G) >= 3 and is_d2c(G)]
    n_triangle = 0
    for G in atlas:
        Delta = max(dict(G.degree()).values())
        for v, dv in G.degree():
            if dv != Delta:
                continue
            B = set(G.neighbors(v))
            Aset = set(G.nodes()) - B - {v}
            b = len(B)
            a = len(Aset)
            lam = b - a - 1
            for y, z in G.edges():
                if y not in B or z not in B:
                    continue
                n_triangle += 1
                found = False
                for src, head in ((y, z), (z, y)):
                    for w in Aset:
                        if set(G.neighbors(src)) & set(G.neighbors(w)) == {head}:
                            eps_src = b - G.degree(src)
                            eps_w = b - G.degree(w)
                            assert eps_src + eps_w >= lam + 1
                            found = True
                assert found

    summary = {
        "rho16_grid_checks": n_rho16,
        "rho16_min_margin": min_rho16,
        "rho16_min_at": min_rho16_at,
        "two_fifths_grid_checks": n_two_fifths,
        "two_fifths_min_margin": min_two_fifths,
        "two_fifths_min_at": min_two_fifths_at,
        "source_root_strict_checks": n_source_root,
        "d2c_atlas_classes": len(atlas),
        "rooted_triangle_kernel_checks": n_triangle,
        "exact_rho16_endpoint": [rho16_exact.numerator, rho16_exact.denominator],
        "exact_two_fifths_endpoint": [two_fifths_exact.numerator, two_fifths_exact.denominator],
        "total_checks": n_rho16 + n_two_fifths + n_source_root + n_triangle,
        "failures": 0,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
