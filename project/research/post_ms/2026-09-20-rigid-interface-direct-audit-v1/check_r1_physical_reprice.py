#!/usr/bin/env python3
"""Audit-only arithmetic replay for the r=1 physical repricing package.

This script does not enumerate graphs. It checks the one-variable inequalities
and the preserved exact stress family used in
ONE_CODE_R1_PHYSICAL_REPRICE_AND_PRIVATE_ORIENTATION.md.
"""


def active_conservation(lam: int, r: int, eps: int) -> int:
    return eps + r * max(0, lam + r - eps)


def stress_row(t: int, sf: int):
    p = c = 2 * t
    y = 1
    g0 = 2 * t - 1
    lam = 4 * t - 2
    u = x = 3 * t
    k = t + 1

    base_w = k * (p + k - 2)
    T = k * (g0 + 2) + sf * (c - 2)

    term1 = k * (p + 1) - 2 * (sf // 2)
    term2 = k * (p + k - 2 * c)
    twice_real = 2 * x * g0 - p + 2 * max(term1, term2)
    L0 = twice_real // 2 + 1

    # lambda is even on this family.
    A_lam = lam * lam // 2 + lam + 4
    C0 = (lam + 2) * (p + u) + p - A_lam

    rooted_rhs_minus_Z = (
        u * (p - lam)
        + 2 * (c - 1) * u
        - c * (c - 1)
        + C0
        - k * (x + y - 1)
    )

    score_margin = C0 - (base_w + max(L0, T))
    rooted_margin = rooted_rhs_minus_Z - T
    return base_w, T, L0, C0, score_margin, rooted_margin


def main():
    # Exact one-variable conservation: eps+r[lambda+r-eps]_+ >= lambda+r.
    checks = 0
    for lam in range(0, 80):
        for r in range(1, 40):
            for eps in range(0, 200):
                checks += 1
                got = active_conservation(lam, r, eps)
                if got < lam + r:
                    raise AssertionError((lam, r, eps, got))

    # Replay the stress family through t=1000 and every admissible image size.
    stress_checks = 0
    min_score_margin = None
    min_rooted_margin = None
    worst_score = None
    worst_rooted = None

    for t in range(2, 1001):
        for sf in range(2, t + 2):
            stress_checks += 1
            base_w, T, L0, C0, sm, rm = stress_row(t, sf)
            if not (L0 > T):
                raise AssertionError(("L0_not_dominant", t, sf, L0, T))
            if sm <= 0:
                raise AssertionError(("score_closed_unexpectedly", t, sf, sm))
            if rm <= 0:
                raise AssertionError(("rooted_closed_unexpectedly", t, sf, rm))
            if min_score_margin is None or sm < min_score_margin:
                min_score_margin = sm
                worst_score = (t, sf, sm)
            if min_rooted_margin is None or rm < min_rooted_margin:
                min_rooted_margin = rm
                worst_rooted = (t, sf, rm)

    print("active-conservation checks:", checks)
    print("stress-family (t,s_f) checks:", stress_checks)
    print("minimum positive score margin:", worst_score)
    print("minimum positive rooted margin:", worst_rooted)
    print("status: PASS")


if __name__ == "__main__":
    main()
