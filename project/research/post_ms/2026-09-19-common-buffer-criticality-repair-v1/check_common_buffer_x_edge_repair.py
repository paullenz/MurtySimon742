#!/usr/bin/env python3
"""Audit arithmetic for COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md.

Diagnostic only.  This checks the convex outside-witness slack floor and the
bounded parameter arithmetic.  It is not a D2C graph enumerator and does not
verify the raw triangle-edge criticality classification.
"""

from collections import Counter
import math


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def rcode(p, u, lam, score):
    D0 = 5 * p + 5 * u - 3 * lam - 2
    return (D0 + math.isqrt(D0 * D0 + 12 * score)) // 3


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for first in range(1, n - k + 2):
        for tail in compositions(n - first, k - 1):
            yield (first,) + tail


def audit_convex_reuse():
    checks = 0
    min_margin = 10**9
    for p in range(1, 8):
        for x in range(1, 10):
            for ell in range(1, 9):
                for m in range(1, ell + 1):
                    for loads in compositions(ell, m):
                        lhs = sum(max(0, p - x + t) for t in loads)
                        rhs = max(0, ell - (x - p) * m)
                        assert lhs >= rhs
                        min_margin = min(min_margin, lhs - rhs)
                        checks += 1
    return checks, min_margin


def scan(pmax=18, umax=18):
    stats = Counter()
    examples = []

    for p in range(3, pmax + 1):
        for u in range(1, umax + 1):
            b = 2 * p + u
            for lam in range(0, b - 3):
                a = b - lam - 1
                if a < 4:
                    continue
                n = 2 * b - lam
                DM = b * (n - b) - M(n)
                C0 = 2 * (DM - 1) + lam * (p + u) - p
                if C0 < 0:
                    continue

                Rcode = rcode(p, u, lam, C0)
                RA = Rcode // 2

                for x in range(3, a):
                    y = a - x
                    for g in range(p + 1):
                        k = x - g
                        if k <= 0 or k + 1 > u:
                            continue

                        Ecore = k * (p + k - 2)
                        old = Ecore + (p - g) + max(
                            phi(g), y * (p - g + 1)
                        )
                        if old > C0:
                            continue

                        stats["predecessor_r0_equality_g_branches"] += 1

                        if RA == 0:
                            ell0 = k
                            m0 = k
                            repaired = 10**30
                        else:
                            matched_cap = 2 * (p - g) * RA
                            ell0 = max(0, k - matched_cap)
                            m0 = (ell0 + RA - 1) // RA if ell0 else 0
                            repaired = Ecore + (p - g) + max(
                                phi(g), y * (p - g + 1 + m0)
                            )

                        if ell0 > 0:
                            stats["positive_forced_outside_load"] += 1
                            stats["sum_forced_outside_sources"] += ell0
                            stats["sum_forced_distinct_witness_floor"] += m0
                            if g == p:
                                stats["positive_load_with_g_eq_p"] += 1
                            if len(examples) < 12:
                                examples.append(
                                    {
                                        "p": p,
                                        "u": u,
                                        "lambda": lam,
                                        "x": x,
                                        "y": y,
                                        "g": g,
                                        "k": k,
                                        "C0": C0,
                                        "R_code": Rcode,
                                        "R_A": RA,
                                        "ell0": ell0,
                                        "m0": m0,
                                        "old_floor": old,
                                        "repaired_floor": repaired,
                                    }
                                )

                        if g == p:
                            stats["zero_buffer_predecessor_pass"] += 1
                            assert ell0 == k

                        if repaired > C0:
                            stats["repaired_floor_rejections"] += 1
                            if g == p:
                                stats["zero_buffer_rejections"] += 1
                        else:
                            stats["repaired_floor_pass"] += 1
                            if g == p:
                                stats["zero_buffer_pass"] += 1

    return stats, examples


def main():
    convex_checks, min_margin = audit_convex_reuse()
    stats, examples = scan()

    expected = {
        "predecessor_r0_equality_g_branches": 345219,
        "positive_forced_outside_load": 17174,
        "positive_load_with_g_eq_p": 17174,
        "zero_buffer_predecessor_pass": 17174,
        "repaired_floor_rejections": 113,
        "zero_buffer_rejections": 113,
        "zero_buffer_pass": 17061,
    }
    mismatches = {
        key: {"expected": value, "actual": stats[key]}
        for key, value in expected.items()
        if stats[key] != value
    }

    print(
        {
            "convex_reuse_checks": convex_checks,
            "minimum_convex_margin": min_margin,
            "scan": dict(stats),
            "expected_mismatches": mismatches,
            "examples": examples,
            "failures": len(mismatches),
            "trust_boundary": (
                "arithmetic and convexity audit only; not graph realizability "
                "and not a proof of raw criticality localization"
            ),
        }
    )


if __name__ == "__main__":
    main()
