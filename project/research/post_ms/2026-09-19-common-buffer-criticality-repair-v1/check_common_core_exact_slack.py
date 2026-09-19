#!/usr/bin/env python3
"""Arithmetic diagnostic for COMMON_CORE_EXACT_SLACK_AND_REVERSE_DEFICIT.md.

Not a D2C graph enumerator.  Replays only the sharpened common-buffer score
floors on the same bounded parameter box as predecessor diagnostics.
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


def old_common_theta(p, u, x, y, g):
    k = x - g
    uo = u - k - 1
    Ecore = k * (p + k - 2)
    A0 = phi(g)
    best = Ecore + (p - g) + max(A0, y * (p - g + 1))
    P0 = p + k + uo
    for r in range(1, y + 1):
        dmax = min(uo, P0 - r)
        if dmax < 0:
            continue
        Lr = y * (p - g + 1) - r
        for d in range(dmax + 1):
            best = min(
                best,
                Ecore + (P0 - r - d) + max(A0, Lr + r * d),
            )
    return best


def repaired_oldcore_theta(p, u, lam, x, y, g, C0):
    """Immediate predecessor after orientation repair, before exact core count."""
    k = x - g
    uo = u - k - 1
    Ecore = k * (p + k - 2)
    A0 = phi(g)
    RA = rcode(p, u, lam, C0) // 2
    if RA <= 0:
        best = 10**30
    else:
        ell0 = max(0, k - 2 * (p - g) * RA)
        m0 = (ell0 + RA - 1) // RA if ell0 else 0
        best = Ecore + (p - g) + max(A0, y * (p - g + 1 + m0))
    P0 = p + k + uo
    for r in range(1, y + 1):
        dmax = min(uo, P0 - r)
        if dmax < 0:
            continue
        Lr = y * (p - g + 1) - r
        for d in range(dmax + 1):
            best = min(
                best,
                Ecore + (P0 - r - d) + max(A0, Lr + r * d),
            )
    return best


def sharp_common_theta(p, u, lam, x, y, g, C0):
    k = x - g
    uo = u - k - 1
    Ecore = k * (p + k - 1)
    A0 = phi(g)
    RA = rcode(p, u, lam, C0) // 2

    if RA <= 0:
        best = 10**30
    else:
        ell0 = max(0, k - 2 * (p - g) * RA)
        m0 = (ell0 + RA - 1) // RA if ell0 else 0
        reverse_head = max(0, k - p) if g == p else 0
        best = (
            Ecore
            + reverse_head
            + (p - g)
            + max(A0, y * (p - g + 1 + m0))
        )

    P0 = p + k + uo
    for r in range(1, y + 1):
        dmax = min(uo, P0 - r)
        if dmax < 0:
            continue
        Lr = y * (p - g + 1) - r
        for d in range(dmax + 1):
            best = min(
                best,
                Ecore + (P0 - r - d) + max(A0, Lr + r * d),
            )
    return best


def full_support_floor(p, u, lam, x, y, g):
    k = x - g
    uo = u - k - 1
    B = (k + 1) * (p + k - 1)
    Rout = uo * max(0, p - g + 1 - lam)
    return B + max(phi(g), y * (p - g + 1) + Rout)


def scan(pmax=18, umax=18):
    s = Counter()
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

                for x in range(3, a):
                    y = a - x
                    old = repaired = sharp = full = False
                    for g in range(p + 1):
                        k = x - g
                        if k <= 0 or k + 1 > u:
                            continue
                        old |= old_common_theta(p, u, x, y, g) <= C0
                        repaired |= (
                            repaired_oldcore_theta(p, u, lam, x, y, g, C0)
                            <= C0
                        )
                        sharp |= sharp_common_theta(p, u, lam, x, y, g, C0) <= C0
                        full |= full_support_floor(p, u, lam, x, y, g) <= C0

                    if old:
                        s["predecessor_common_states"] += 1
                    if repaired:
                        s["orientation_repaired_common_states"] += 1
                    if sharp:
                        s["sharp_common_states"] += 1
                    if repaired and not sharp:
                        s["new_exclusions_vs_repaired"] += 1
                    if old and not sharp:
                        s["new_exclusions_vs_predecessor"] += 1
                    if sharp or full:
                        s["sharp_z1_support_union"] += 1

    return s


def zero_buffer_branch_scan(pmax=18, umax=18):
    s = Counter()
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
                RA = rcode(p, u, lam, C0) // 2
                if RA <= 0:
                    continue
                for x in range(p + 1, a):
                    y = a - x
                    k = x - p
                    if k + 1 > u:
                        continue
                    old = k * (p + k - 2) + max(phi(p), y)
                    if old > C0:
                        continue
                    s["zero_buffer_predecessor_branches"] += 1
                    m0 = (k + RA - 1) // RA
                    core = k * (p + k - 1)
                    floor_core = core + max(phi(p), y * (1 + m0))
                    floor_head = (
                        core + max(0, k - p) + max(phi(p), y * (1 + m0))
                    )
                    if floor_core > C0:
                        s["zero_buffer_rejected_core"] += 1
                    if floor_head > C0:
                        s["zero_buffer_rejected_head"] += 1
                    else:
                        s["zero_buffer_head_pass"] += 1
    return s


def main():
    states = scan()
    branches = zero_buffer_branch_scan()
    expected = {
        "predecessor_common_states": 64892,
        "orientation_repaired_common_states": 64867,
        "sharp_common_states": 64079,
        "new_exclusions_vs_repaired": 788,
        "new_exclusions_vs_predecessor": 813,
        "sharp_z1_support_union": 64079,
        "zero_buffer_predecessor_branches": 17174,
        "zero_buffer_rejected_core": 594,
        "zero_buffer_rejected_head": 644,
        "zero_buffer_head_pass": 16530,
    }
    merged = dict(states)
    merged.update(branches)
    mismatches = {
        k: {"expected": v, "actual": merged.get(k, 0)}
        for k, v in expected.items()
        if merged.get(k, 0) != v
    }
    print(
        {
            "scan": merged,
            "expected_mismatches": mismatches,
            "failures": len(mismatches),
            "trust_boundary": (
                "score-profile replay only; not graph realization or a proof of "
                "the singleton-head/core-degree theorem"
            ),
        }
    )


if __name__ == "__main__":
    main()
