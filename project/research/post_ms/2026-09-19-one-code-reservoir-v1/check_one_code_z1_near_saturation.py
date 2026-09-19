#!/usr/bin/env python3
"""Arithmetic diagnostic for ONE_CODE_Z1_NEAR_SATURATION.md.

This scans only the explicit score floors derived in the hand theorem. It is
not a graph-realizability checker and does not enumerate D2C graphs.
"""

from collections import Counter


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


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
                    stats["old_population_possible"] += 1

                    old_z1 = False
                    core = False
                    full = False
                    for g in range(p + 1):
                        k = max(0, x - g)
                        if k <= 0 or k + 1 > u:
                            continue

                        g0 = x - T0
                        if g0 >= 1:
                            Eold = k * (p - 1)
                        else:
                            Eold = max(0, y * k - (1 - g0) * u)

                        if phi(g) + Eold <= C0:
                            old_z1 = True

                        Ecore = k * (p + k - 2)
                        if phi(g) + Ecore <= C0:
                            core = True

                        Efull = max(0, (k + 1) * (p + k - 1) - 2 * y)
                        if phi(g) + Efull <= C0:
                            full = True

                    if old_z1:
                        stats["older_shared_floor_z1_possible"] += 1
                    if core:
                        stats["common_buffer_possible"] += 1
                    if full:
                        stats["full_support_possible"] += 1
                    if core or full:
                        stats["either_z1_support_possible"] += 1
                    if old_z1 and not (core or full):
                        stats["new_z1_rejected"] += 1
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
    print(
        {
            "scan": dict(stats),
            "new_rejection_examples": examples,
            "failures": 0,
            "trust_boundary": (
                "arithmetic diagnostic of the two z=1 score gates only; "
                "rigid-cut realizability remains conditional"
            ),
        }
    )


if __name__ == "__main__":
    main()
