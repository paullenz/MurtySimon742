#!/usr/bin/env python3
"""Arithmetic audit for the z=1 closure refinements.

This is deliberately not a D2C graph enumerator. It checks only the exact
integer elimination derived from the full-support normal form and compares
new score gates against the already-preserved coarse z=1 diagnostic box.
"""
from collections import Counter
from math import comb, ceil


def M(n):
    return ((n - 1) ** 2) // 4 + 1


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def exact_relaxation(B, y, C, D0):
    best = None
    arg = None
    for j in range(y + 1):
        for e in range(min(C, y - j) + 1):
            Emin = max(0, B - j - 2 * e)
            # For fixed j,e, increasing E above Emin can only be useful until
            # the residual constraint is met. Testing the exact two relevant
            # values is enough, but a small explicit range is clearer here.
            for E in range(Emin, max(Emin, D0 - j) + 2):
                q = max(0, ceil((D0 - j - E) / 2))
                val = q + E
                if best is None or val < best:
                    best = val
                    arg = (j, e, E, q)
    return best, arg


def closed_form(B, y, C, D0):
    c = min(C, y)
    if B <= y:
        jstar = y
        Estar = 0
    elif B <= y + c:
        jstar = 2 * y - B
        Estar = 0
    else:
        jstar = y - c
        Estar = B - y - c
    val = Estar + ceil(max(0, D0 - jstar - Estar) / 2)
    return val, (jstar, Estar)


def chan_score_floor(A0, E0, L, y, k, p, x, g):
    alpha = L + 2 * (k + 1)
    beta = 2 * y
    demand = L * y * (p + 2 * x - 3 * g)
    extra = max(0, demand - alpha * A0 - beta * E0)
    return A0 + E0 + ceil(extra / max(alpha, beta))


def audit_exact_elimination():
    checks = 0
    for y in range(1, 13):
        for k in range(1, 9):
            C = comb(k + 1, 2)
            for B in range(0, 70):
                for D0 in range(-8, 70):
                    brute, _ = exact_relaxation(B, y, C, D0)
                    form, _ = closed_form(B, y, C, D0)
                    checks += 1
                    if brute != form:
                        return checks, {
                            "B": B, "y": y, "k": k, "C": C, "D0": D0,
                            "brute": brute, "closed": form,
                        }
    return checks, None


def audit_chan_floor():
    checks = 0
    for A0 in range(0, 6):
        for E0 in range(0, 6):
            for alpha in range(1, 9):
                for beta in range(1, 9):
                    for demand in range(0, 31):
                        best = None
                        # Enough because the closed form is never more than
                        # demand + A0 + E0 in this audit box.
                        for A in range(A0, 40):
                            for E in range(E0, 40):
                                if alpha * A + beta * E >= demand:
                                    val = A + E
                                    if best is None or val < best:
                                        best = val
                        form = A0 + E0 + ceil(
                            max(0, demand - alpha * A0 - beta * E0)
                            / max(alpha, beta)
                        )
                        checks += 1
                        if best != form:
                            return checks, {
                                "A0": A0, "E0": E0, "alpha": alpha,
                                "beta": beta, "demand": demand,
                                "brute": best, "closed": form,
                            }
    return checks, None


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
                L = lam + 1
                for x in range(3, a):
                    y = a - x
                    if max(0, x - p) > u:
                        continue
                    stats["old_population_possible"] += 1
                    old_z1 = False
                    common_old = False
                    full_old = False
                    full_cap = False
                    common_chan = False
                    full_chan = False
                    for g in range(p + 1):
                        k = max(0, x - g)
                        if k <= 0 or k + 1 > u:
                            continue
                        g0 = x - T0
                        Eold = (
                            k * (p - 1)
                            if g0 >= 1
                            else max(0, y * k - (1 - g0) * u)
                        )
                        A0 = phi(g)
                        if A0 + Eold <= C0:
                            old_z1 = True

                        Ecore = k * (p + k - 2)
                        if A0 + Ecore <= C0:
                            common_old = True
                        if chan_score_floor(A0, Ecore, L, y, k, p, x, g) <= C0:
                            common_chan = True

                        B = (k + 1) * (p + k - 1)
                        Efull_old = max(0, B - 2 * y)
                        if A0 + Efull_old <= C0:
                            full_old = True

                        C = min(comb(k + 1, 2), y)
                        Efull_cap = max(0, B - y - C)
                        if A0 + Efull_cap <= C0:
                            full_cap = True
                        if chan_score_floor(A0, Efull_cap, L, y, k, p, x, g) <= C0:
                            full_chan = True

                    if old_z1:
                        stats["older_shared_floor_z1_possible"] += 1
                    if common_old:
                        stats["common_buffer_possible"] += 1
                    if full_old:
                        stats["full_support_old_possible"] += 1
                    if full_cap:
                        stats["full_support_cap_possible"] += 1
                    if full_old and not full_cap:
                        stats["full_support_new_cap_rejections"] += 1
                    if common_old or full_old:
                        stats["either_old_z1_support"] += 1
                    if common_old or full_cap:
                        stats["either_after_cap"] += 1
                    if common_chan or full_chan:
                        stats["either_after_cap_and_chan"] += 1
                    if (common_old or full_old) and not (common_chan or full_chan):
                        stats["new_total_rejections_vs_prior_z1"] += 1
                        if len(examples) < 12:
                            examples.append({
                                "p": p, "u": u, "lambda": lam,
                                "a": a, "x": x, "y": y, "C0": C0,
                            })
    return stats, examples


def main():
    checks, failure = audit_exact_elimination()
    chan_checks, chan_failure = audit_chan_floor()
    stats, examples = scan()
    print({
        "exact_elimination_checks": checks,
        "exact_elimination_failure": failure,
        "chan_floor_checks": chan_checks,
        "chan_floor_failure": chan_failure,
        "scan": dict(stats),
        "new_rejection_examples": examples,
        "failures": int(failure is not None) + int(chan_failure is not None),
        "trust_boundary": (
            "exact integer audit of the z=1 normal-form elimination and a bounded "
            "abstract score diagnostic only; not graph realizability evidence"
        ),
    })


if __name__ == "__main__":
    main()
