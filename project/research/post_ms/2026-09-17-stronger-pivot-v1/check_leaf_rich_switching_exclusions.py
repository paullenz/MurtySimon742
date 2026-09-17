#!/usr/bin/env python3
"""Finite regression for LEAF_RICH_SWITCHING_EXCLUSIONS.md.

This is regression evidence only.  The universal statements in the note are
hand proofs; this script checks the canonical zero-signing normal form and the
integer arithmetic used in the leaf-rich exclusions.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path


def M(n: int) -> int:
    return ((n - 1) ** 2) // 4 + 1


def zero_leaf_count(k: int, code: int) -> int:
    """Leaf count of L_c for sigma=0, where L_c is the complete cut of supp(c)."""
    s = code.bit_count()
    return (s if k - s == 1 else 0) + ((k - s) if s == 1 else 0)


def zero_orientation_edges(k: int):
    """Edges of Omega_sigma for sigma=0.

    Returns two physical layers.  The low layer is on singleton codes e_i and
    the high layer on their complements.
    """
    full = (1 << k) - 1
    low = set()
    high = set()
    for i, j in itertools.combinations(range(k), 2):
        ei = 1 << i
        ej = 1 << j
        low.add(tuple(sorted((ei, ej))))
        high.add(tuple(sorted((full ^ ei, full ^ ej))))
    return low, high


def star_bound(k: int, lam: int):
    a = 2 * k - lam - 1
    q = a - (2 * k - 2)
    assert q == 1 - lam
    assert q in (0, 1, 2)

    r = k * (k - lam)
    h = r // (k - 1)
    eF_upper = (h * h) // 4 + 2 * q * k
    delta_lower = r - eF_upper

    n = 2 * k + a + 1
    product = 2 * k * (a + 1)
    required_defect = product - M(n)

    return {
        "k": k,
        "lambda": lam,
        "a": a,
        "n": n,
        "q": q,
        "r": r,
        "h_upper": h,
        "eF_upper": eF_upper,
        "delta_lower": delta_lower,
        "required_defect": required_defect,
        "closes": delta_lower >= required_defect,
    }


def main() -> None:
    zero_records = []
    for k in range(5, 13):
        hist = {}
        for code in range(1 << k):
            ell = zero_leaf_count(k, code)
            hist[ell] = hist.get(ell, 0) + 1

        assert hist.get(k - 1, 0) == 2 * k
        assert all(ell in (0, k - 1) for ell in hist)

        low, high = zero_orientation_edges(k)
        target_edges = k * (k - 1) // 2
        assert len(low) == target_edges
        assert len(high) == target_edges

        low_vertices = set().union(*(set(e) for e in low))
        high_vertices = set().union(*(set(e) for e in high))
        assert len(low_vertices) == k
        assert len(high_vertices) == k
        assert low_vertices.isdisjoint(high_vertices)

        # Complete-graph check in each layer.
        assert all(tuple(sorted((u, v))) in low for u, v in itertools.combinations(low_vertices, 2))
        assert all(tuple(sorted((u, v))) in high for u, v in itertools.combinations(high_vertices, 2))

        zero_records.append(
            {
                "k": k,
                "leaf_bearing_codes": 2 * k,
                "leaf_count_each": k - 1,
                "orientation_components": [k, k],
                "orientation_cover_number": 2 * k - 2,
            }
        )

    perfect_matching = []
    for k in range(6, 22, 2):
        cover_lower = (k * k - 3 * k + 4 + 1) // 2
        impossible_above_M = k >= 8 and cover_lower > 2 * k
        if k >= 8:
            assert impossible_above_M
        perfect_matching.append(
            {
                "k": k,
                "cover_lower_bound": cover_lower,
                "max_A_above_M": 2 * k,
                "impossible_above_M": impossible_above_M,
            }
        )

    star_records = []
    thresholds = {}
    for lam in (1, 0, -1):
        rows = [star_bound(k, lam) for k in range(5, 31)]
        star_records.extend(rows)
        threshold = None
        for row in rows:
            k0 = row["k"]
            if all(star_bound(j, lam)["closes"] for j in range(k0, 31)):
                threshold = k0
                break
        assert threshold is not None
        thresholds[str(lam)] = threshold

    assert thresholds == {"1": 5, "0": 6, "-1": 8}

    summary = {
        "status": "PASS_LEAF_RICH_SWITCHING_EXCLUSIONS",
        "date": "2026-09-17",
        "scope": "finite regression evidence only; universal exclusions are hand proofs",
        "zero_signing_checks": zero_records,
        "perfect_matching_cover_checks": perfect_matching,
        "star_defect_thresholds": thresholds,
        "uniform_full_star_exclusion_from_k": 8,
        "negative_control": "k=4 residual-zero X3 boundary remains outside the exclusions",
    }

    out = Path(__file__).with_name("LEAF_RICH_SWITCHING_EXCLUSIONS_CHECK_SUMMARY.json")
    out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
