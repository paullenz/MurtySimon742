#!/usr/bin/env python3
"""Arithmetic audit for ONE_CODE_PAIR_PURIFICATION.md.

Diagnostic only.  This does not establish graph realizability or any
upstream criticality premise.
"""

import math
from collections import Counter


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def psi(p, x):
    return min(phi(g) + max(0, x - g) * (p - 1) for g in range(p + 1))


def rcode(D0, s):
    return max(0, math.floor((D0 + math.sqrt(D0 * D0 + 12 * s)) / 3))


def verify_psi_formula(pmax=80, xmax=160):
    checked = 0
    for p in range(3, pmax + 1):
        for x in range(3, xmax + 1):
            brute = psi(p, x)
            candidates = [(x - 2) * (p - 1)]
            hi = min(p, x)
            if hi >= 3:
                centre = p / 2
                gs = {3, hi, int(math.floor(centre)), int(math.ceil(centre))}
                for g in gs:
                    g = min(hi, max(3, g))
                    candidates.append(g * g - p * g + x * (p - 1))
            exact = min(candidates)
            assert brute == exact, (p, x, brute, exact)

            continuous = max(
                0,
                math.floor(min(x * (x - 1), x * (p - 1) - p * p / 4) - 2),
            )
            assert brute >= continuous, (p, x, brute, continuous)
            checked += 1
    return checked


def scan_psi(pmax=18, umax=18):
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
                    # Old one-code population gate, using only mu_X<=p.
                    if max(0, x - p) > u:
                        continue
                    stats["old_population_possible"] += 1
                    g0 = x - T0
                    if g0 >= 1 and psi(p, x) > C0:
                        stats["psi_rejected"] += 1
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
                                    "Psi": psi(p, x),
                                }
                            )
    return stats, examples


def existential_scan(pmax=18, umax=18, use_crowd=True, use_one=True, use_chan=True):
    """Generous existential g_P scan.

    The scan maximizes local capacity subject only to the shared total
    scorecard C0.  Rejection is therefore a valid diagnostic obstruction;
    survival is not graph evidence.
    """
    stats = Counter()
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
                L = lam + 1
                D0 = 5 * p + 5 * u - 3 * lam - 2
                R = rcode(D0, C0)

                for x in range(3, a):
                    y = a - x
                    if max(0, x - p) > u:
                        continue
                    stats["old_population_possible"] += 1
                    feasible = False

                    for gp in range(p + 1):
                        k = max(0, x - gp)
                        if k > u:
                            continue

                        gamma0 = phi(gp)
                        g0 = x - T0
                        if g0 >= 1:
                            E0 = k * (p - 1)
                        else:
                            # Generous choice u_bar=u minimizes the truncation floor.
                            E0 = max(0, y * k - (1 - g0) * u)

                        # The gamma and U floors spend disjoint L_A and E_U
                        # parts of the same scorecard S=L_A+E_U.
                        if gamma0 + E0 > C0:
                            continue

                        if use_crowd and 3 * y >= D0 and y * (3 * y - D0) > C0:
                            continue

                        if use_one:
                            # Deliberately generous: put all scorecard into P,
                            # and all non-E_U remainder into local A-slack.
                            LYmax = C0 - E0
                            lhs = R * (gp + 2 * C0 / L) + LYmax
                            rhs = y * (p + x + k)
                            if lhs < rhs:
                                continue

                        if use_chan and gp <= x:
                            # Maximize CHAN-P over local LY,E_bar while keeping
                            # gamma0 A-slack and E0 U-slack somewhere in S.
                            coef_L = 1 + 2 * u / L
                            coef_E = 2 * y / L
                            if coef_L >= coef_E:
                                max_chan = coef_L * (C0 - E0) + coef_E * E0
                            else:
                                max_chan = coef_E * (C0 - gamma0)
                            if max_chan < y * (p + 2 * x - 3 * gp):
                                continue

                        feasible = True
                        break

                    if feasible:
                        stats["survive"] += 1
                    else:
                        stats["rejected"] += 1
    return stats


def main():
    formula_checks = verify_psi_formula()
    psi_stats, examples = scan_psi()

    shared_only = existential_scan(use_crowd=False, use_one=False, use_chan=False)
    with_crowd = existential_scan(use_crowd=True, use_one=False, use_chan=False)
    with_one = existential_scan(use_crowd=True, use_one=True, use_chan=False)
    full = existential_scan(use_crowd=True, use_one=True, use_chan=True)

    out = {
        "psi_formula_checks": formula_checks,
        "psi_scan": dict(psi_stats),
        "psi_rejection_examples": examples,
        "shared_gamma_plus_U_only": dict(shared_only),
        "plus_CROWD": dict(with_crowd),
        "plus_generous_ONE": dict(with_one),
        "plus_CHAN": dict(full),
        "failures": 0,
        "trust_boundary": (
            "arithmetic/parameter diagnostic only; graph premises are proved or "
            "regressed separately"
        ),
    }
    print(out)


if __name__ == "__main__":
    main()
