#!/usr/bin/env python3
"""Diagnostic for ZERO_BUFFER_LOCAL_PAIR_FEASIBILITY.md.

Checks the integer A/U minimization and bounded parameter impact.  This is not
a D2C graph enumerator and does not verify the raw criticality theorems.
"""

from collections import Counter
import math


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def ceil_div(a, b):
    return (a + b - 1) // b


def rcode(p, u, lam, score):
    D0 = 5 * p + 5 * u - 3 * lam - 2
    return (D0 + math.isqrt(D0 * D0 + 12 * score)) // 3


def min_s_cap(p, u, lam, x, y, C0):
    L = lam + 1
    target = 2 * x * y * L
    lo, hi = 0, C0 + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if rcode(p, u, lam, mid) * (p * L + 2 * mid) >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def audit_integer_AU():
    checks = 0
    for A in range(0, 12):
        for B in range(0, 12):
            for cL in range(1, 8):
                for cE in range(1, 8):
                    for T in range(0, 80):
                        formula = A + B + ceil_div(
                            max(0, T - cL * A - cE * B), max(cL, cE)
                        )
                        brute = None
                        for l in range(A, A + 100):
                            for e in range(B, B + 100):
                                if cL * l + cE * e >= T:
                                    val = l + e
                                    if brute is None or val < brute:
                                        brute = val
                        assert formula == brute
                        checks += 1
    return checks


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

                D0 = 5 * p + 5 * u - 3 * lam - 2
                RA = rcode(p, u, lam, C0) // 2
                if RA <= 0:
                    continue

                for x in range(p + 1, a):
                    y = a - x
                    k = x - p
                    if k + 1 > u:
                        continue

                    Ecore = k * (p + k - 2)
                    predecessor = Ecore + max(phi(p), y)
                    if predecessor > C0:
                        continue

                    stats["zero_buffer_predecessor_pass"] += 1

                    m0 = ceil_div(k, RA)
                    A = y * (1 + m0)
                    B = Ecore
                    s_geom = A + B

                    L = lam + 1
                    target = L * y * k
                    base_capacity = (k + 1) * A + y * B
                    extra = ceil_div(
                        max(0, target - base_capacity), max(k + 1, y)
                    )
                    s_AU = s_geom + extra

                    s_crowd = max(0, y * (3 * y - D0))
                    s_cap = min_s_cap(p, u, lam, x, y, C0)
                    s_star = max(s_geom, s_AU, s_crowd, s_cap)

                    if s_AU > s_geom:
                        stats["directed_AU_strictly_raises_local_floor"] += 1
                    if s_cap > s_geom:
                        stats["Ccap_strictly_raises_local_floor"] += 1
                    if s_crowd > s_geom:
                        stats["CROWD_strictly_raises_local_floor"] += 1

                    if s_star > C0:
                        stats["local_pair_rejections"] += 1
                        if len(examples) < 12:
                            examples.append(
                                {
                                    "p": p,
                                    "u": u,
                                    "lambda": lam,
                                    "x": x,
                                    "y": y,
                                    "k": k,
                                    "C0": C0,
                                    "R_A": RA,
                                    "m0": m0,
                                    "s_geom": s_geom,
                                    "s_AU": s_AU,
                                    "s_cap": s_cap,
                                    "s_crowd": s_crowd,
                                }
                            )
                    else:
                        stats["local_pair_pass"] += 1

    return stats, examples


def main():
    au_checks = audit_integer_AU()
    stats, examples = scan()

    expected = {
        "zero_buffer_predecessor_pass": 17174,
        "local_pair_rejections": 113,
        "local_pair_pass": 17061,
        "directed_AU_strictly_raises_local_floor": 5280,
        "Ccap_strictly_raises_local_floor": 0,
        "CROWD_strictly_raises_local_floor": 0,
    }
    mismatches = {
        key: {"expected": value, "actual": stats[key]}
        for key, value in expected.items()
        if stats[key] != value
    }

    print(
        {
            "integer_AU_minimization_checks": au_checks,
            "scan": dict(stats),
            "expected_mismatches": mismatches,
            "rejection_examples": examples,
            "failures": len(mismatches),
            "trust_boundary": (
                "integer local-pair arithmetic only; not graph realizability "
                "or proof of upstream criticality localization"
            ),
        }
    )


if __name__ == "__main__":
    main()
