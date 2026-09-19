#!/usr/bin/env python3
"""Arithmetic audit for ONE_CODE_BIDIRECTIONAL_RESERVOIR.md.

This checker verifies only the explicit finite minimization / scorecard-relaxed
consequences of the hand theorem. It is not a graph-realizability checker.
"""

import math
import random
from collections import Counter


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def dplus(y, t, T0):
    return (y + t) * (y + t - T0) - t


def dminus(s, T0):
    return s * (s - T0 - 1)


def theta_brute(y, k, T0, u):
    best = None
    arg = None
    for s in range(k, u + 1):
        for t in range(0, u - s + 1):
            val = max(0, dplus(y, t, T0)) + max(0, dminus(s, T0)) - 2 * y * (s - k)
            if best is None or val < best:
                best = val
                arg = (s, t)
    return best, arg


def t_candidates(y, T0, hi):
    """Exact candidate set for minimizing the convex D_+(t) positive part."""
    centre = (T0 + 1 - 2 * y) / 2
    vals = {0, hi, math.floor(centre), math.ceil(centre)}
    return sorted({min(hi, max(0, int(v))) for v in vals})


def theta_reduced(y, k, T0, u):
    best = None
    arg = None
    for s in range(k, u + 1):
        hi = u - s
        for t in t_candidates(y, T0, hi):
            val = max(0, dplus(y, t, T0)) + max(0, dminus(s, T0)) - 2 * y * (s - k)
            if best is None or val < best:
                best = val
                arg = (s, t)
    return best, arg


def verify_theta_reduction(trials=100000, seed=742):
    rng = random.Random(seed)
    for _ in range(trials):
        u = rng.randint(1, 40)
        k = rng.randint(0, u)
        y = rng.randint(1, 60)
        T0 = rng.randint(-8, 70)
        brute, _ = theta_brute(y, k, T0, u)
        reduced, _ = theta_reduced(y, k, T0, u)
        assert brute == reduced, (y, k, T0, u, brute, reduced)
    return trials


def scan(pmax=18, umax=18):
    """Reproduce the deliberately generous THETA-GATE diagnostic.

    For each old-population-feasible one-code state, search for at least one
    gamma count g that survives the previously established shared gamma/U
    score floor. Then ask whether *any* allocation u_-,u_+ can satisfy the
    scorecard-relaxed cylinder gate. The gate gives the entire C0 scorecard
    to the two crowding deficits, so its rejections are deliberately robust
    while its survivors carry no graph-realizability meaning.
    """
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

                    # Preserved old one-code population gate using mu_X<=p.
                    if max(0, x - p) > u:
                        continue
                    stats["old_population_possible"] += 1

                    shared_possible = False
                    reservoir_possible = False

                    for g in range(p + 1):
                        k = max(0, x - g)
                        if k > u:
                            continue

                        g0 = x - T0
                        A0 = phi(g)
                        if g0 >= 1:
                            E0 = k * (p - 1)
                        else:
                            # Generous global-u version of the preserved
                            # truncated local U-slack floor.
                            E0 = max(0, y * k - (1 - g0) * u)

                        if A0 + E0 > C0:
                            continue
                        shared_possible = True

                        theta, _ = theta_reduced(y, k, T0, u)
                        if theta <= C0:
                            reservoir_possible = True
                            break

                    if not shared_possible:
                        stats["shared_gamma_plus_U_rejected"] += 1

                    if reservoir_possible:
                        stats["reservoir_survive"] += 1
                    else:
                        stats["reservoir_rejected"] += 1
                        if shared_possible and len(examples) < 12:
                            examples.append(
                                {
                                    "p": p,
                                    "u": u,
                                    "lambda": lam,
                                    "a": a,
                                    "x": x,
                                    "y": y,
                                    "T0": T0,
                                    "C0": C0,
                                }
                            )

    stats["additional_reservoir_rejections"] = (
        stats["reservoir_rejected"] - stats["shared_gamma_plus_U_rejected"]
    )
    return stats, examples


def main():
    theta_checks = verify_theta_reduction()
    stats, examples = scan()
    out = {
        "theta_reduction_checks": theta_checks,
        "scan": dict(stats),
        "additional_rejection_examples": examples,
        "failures": 0,
        "trust_boundary": (
            "arithmetic audit of the scorecard-relaxed cylinder gate only; "
            "the reservoir theorem is hand-derived and rigid-cut realizability "
            "remains conditional"
        ),
    }
    print(out)


if __name__ == "__main__":
    main()
