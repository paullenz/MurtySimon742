#!/usr/bin/env python3
"""Arithmetic audit for the 19 Sep criticality-sharpened z=1 branches.

Diagnostic only.  This is not a D2C graph enumerator and does not establish
rigid-cut realizability.  It checks only the integer score profiles stated in
OMITTED_PAIR_NONEDGE_FORCING.md, OUTSIDE_U_SCORE_ELIMINATION.md and
UNLOADED_COMMON_BUFFER_SOURCE_EDGE_DICHOTOMY.md.
"""

from collections import Counter


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def common_theta(p, u, x, y, g):
    """Return exact unloaded common-buffer score floor after E_core."""
    k = x - g
    assert k > 0 and k + 1 <= u
    uo = u - k - 1
    A0 = phi(g)
    Ecore = k * (p + k - 2)

    # r=0: buffer anticomplete to Y.
    best = Ecore + (p - g) + max(A0, y * (p - g + 1))
    best_tag = (0, None)

    # r>=1: every source-buffer edge is triangle-free.
    P0 = p + k + uo
    for r in range(1, y + 1):
        dmax = min(uo, P0 - r)
        if dmax < 0:
            continue
        Lr = y * (p - g + 1) - r
        for d in range(dmax + 1):
            eps_b = P0 - r - d
            val = Ecore + eps_b + max(A0, Lr + r * d)
            if val < best:
                best = val
                best_tag = (r, d)
    return best, best_tag


def full_support_floor(p, u, lam, x, y, g):
    """Forced-nu plus outside-spill parameter-only score floor."""
    k = x - g
    assert k > 0 and k + 1 <= u
    uo = u - k - 1
    B = (k + 1) * (p + k - 1)
    Rout = uo * max(0, p - g + 1 - lam)
    return B + max(phi(g), y * (p - g + 1) + Rout)


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

                T0 = a - p
                for x in range(3, a):
                    y = a - x
                    if max(0, x - p) > u:
                        continue

                    old_z1 = False
                    old_common = False
                    old_full = False
                    new_common = False
                    new_full = False
                    cheapest_common_tag = None
                    cheapest_common = None

                    for g in range(p + 1):
                        k = x - g
                        if k <= 0 or k + 1 > u:
                            continue

                        # Predecessor shared and z=1 support gates.
                        g0 = x - T0
                        if g0 >= 1:
                            Eold = k * (p - 1)
                        else:
                            Eold = max(0, y * k - (1 - g0) * u)
                        if phi(g) + Eold <= C0:
                            old_z1 = True

                        Ecore = k * (p + k - 2)
                        if phi(g) + Ecore <= C0:
                            old_common = True

                        Efull = max(0, (k + 1) * (p + k - 1) - 2 * y)
                        if phi(g) + Efull <= C0:
                            old_full = True

                        cval, ctag = common_theta(p, u, x, y, g)
                        if cval <= C0:
                            new_common = True
                            if cheapest_common is None or cval < cheapest_common:
                                cheapest_common = cval
                                cheapest_common_tag = ctag

                        if full_support_floor(p, u, lam, x, y, g) <= C0:
                            new_full = True

                    if old_z1:
                        stats["older_shared_floor_z1_possible"] += 1
                    if old_common:
                        stats["predecessor_common_buffer_possible"] += 1
                    if old_full:
                        stats["predecessor_full_support_possible"] += 1
                    if old_common or old_full:
                        stats["predecessor_either_z1_support_possible"] += 1

                    if new_common:
                        stats["criticality_common_buffer_possible"] += 1
                        if cheapest_common_tag[0] == 0:
                            stats["criticality_common_cheapest_r0"] += 1
                        else:
                            stats["criticality_common_cheapest_rpositive"] += 1
                    if new_full:
                        stats["criticality_full_support_possible"] += 1
                    if new_common or new_full:
                        stats["criticality_either_z1_support_possible"] += 1

                    if old_z1 and not (new_common or new_full):
                        stats["criticality_rejected_from_older_shared"] += 1
                        if len(examples) < 12:
                            examples.append(
                                {
                                    "p": p,
                                    "u": u,
                                    "lambda": lam,
                                    "a": a,
                                    "x": x,
                                    "y": y,
                                    "C0": C0,
                                }
                            )

    return stats, examples


def main():
    stats, examples = scan()
    expected = {
        "older_shared_floor_z1_possible": 86820,
        "predecessor_common_buffer_possible": 76463,
        "predecessor_full_support_possible": 77310,
        "predecessor_either_z1_support_possible": 78167,
        "criticality_common_buffer_possible": 64892,
        "criticality_full_support_possible": 59028,
        "criticality_either_z1_support_possible": 64892,
        "criticality_common_cheapest_r0": 40589,
        "criticality_common_cheapest_rpositive": 24303,
        "criticality_rejected_from_older_shared": 21928,
    }
    failures = {}
    for key, value in expected.items():
        if stats[key] != value:
            failures[key] = {"expected": value, "actual": stats[key]}

    print(
        {
            "scan": dict(stats),
            "expected_mismatches": failures,
            "rejection_examples": examples,
            "failures": len(failures),
            "trust_boundary": (
                "integer score-profile replay only; not graph realizability or a proof "
                "of any upstream rigid-cut premise"
            ),
        }
    )


if __name__ == "__main__":
    main()
