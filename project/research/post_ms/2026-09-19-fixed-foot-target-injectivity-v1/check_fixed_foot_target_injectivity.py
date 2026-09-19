#!/usr/bin/env python3
"""Diagnostic replay for fixed-foot target injectivity/shared-core t=1 E2.

This scans the same abstract integer parameter box as the predecessor E1/E2
checkers. It is NOT a D2C graph enumerator and makes no realizability claim.
The graph-theoretic target-injectivity and star-forest statements are proved
in T1_EXCEPTIONAL_TARGET_INJECTIVITY_SHARED_CORE.md, not by this scan.
"""
import math
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
E1 = HERE.parent / "2026-09-19-one-defect-support-cap-v1" / "check_one_defect_support_cap.py"
C = runpy.run_path(str(E1))

C0 = C["C0"]
predecessor_floor = C["predecessor_floor"]
repaired_floor = C["repaired_floor"]
preceding_mg1_score = C["preceding_mg1_score"]
hmin_closed = C["hmin_closed"]
sigma_pair = C["sigma_pair"]
rows_for_state = C["rows_for_state"]
support_sizes = C["support_sizes"]
E1_slot_floor = C["E1_slot_floor"]
refined_pair_lhs = C["refined_pair_lhs"]


def f_closed(R, k):
    """min_{0<=e<=k} e+[R-2e]_+."""
    if R <= 0:
        return 0
    if R <= 2 * k:
        return (R + 1) // 2
    return R - k


def verify_f_closed():
    checks = 0
    for k in range(1, 40):
        for R in range(-100, 201):
            brute = min(e + max(0, R - 2 * e) for e in range(k + 1))
            assert brute == f_closed(R, k), (k, R, brute, f_closed(R, k))
            checks += 1
    return checks


def main():
    f_checks = verify_f_closed()
    c = Counter()
    byk = Counter()
    min_pair_margin = None

    for p in range(3, 19):
        g = p - 1  # t=1
        for u in range(1, 19):
            b = 2 * p + u
            for lam in range(0, b - 3):
                a = b - lam - 1
                if a < 4:
                    continue
                cap = C0(p, u, lam)
                if cap < 0:
                    continue
                for x in range(3, a):
                    y = a - x
                    k = x - g
                    if k <= 0 or k + 1 > u:
                        continue
                    if predecessor_floor(p, x, y, g) > cap:
                        continue
                    if u < x + 2:
                        continue
                    if repaired_floor(p, u, lam, x, y, g) > cap:
                        continue
                    old = preceding_mg1_score(p, u, lam, x, y, g)
                    if old is None or old > cap:
                        continue

                    T0 = a - p
                    N = u - k - 2
                    s1 = max(0, 2 - k)
                    Y0 = y * (p + 2)
                    Q = x * (x - T0) + k * (x - 1) + x - g * (g - 1) + k * N
                    Ebase = k * (p + k) + 2 + k + g * s1
                    if Ebase + Y0 + hmin_closed(Q, k, g, N) > cap:
                        continue

                    P0 = k * (p + k) + 1 + Y0
                    O0 = 1 + k + g * s1
                    sig = sigma_pair(p, u, lam, x, y, g, P0, cap)
                    if sig is None:
                        continue
                    BP = cap - O0 - sig
                    if hmin_closed(Q, k, g, N) > BP:
                        continue

                    rows = rows_for_state(p, u, lam, x, y, g, k, cap, Q, N, BP, Y0)
                    if not rows:
                        continue

                    # Reproduce exactly the predecessor's support-capped E1 route.
                    has_e1 = False
                    for A, M, D, H, Emin, nu, rupper in rows:
                        d0 = g - A
                        if not support_sizes(p, g, k, 1):
                            continue
                        if not ((k > 1 and d0 in (0, 1)) or
                                (k == 1 and 0 <= d0 <= 2)):
                            continue
                        old_lhs = p * (g + 1) + k + M - (k + 1) * d0 + D
                        if old_lhs > cap - sig:
                            continue
                        if rupper < E1_slot_floor(x, y, g, k, A, Emin):
                            continue
                        if refined_pair_lhs(p, g, k, M, d0, D) <= cap - sig:
                            has_e1 = True
                            break

                    if has_e1:
                        continue

                    c["t1_no_E1_states"] += 1
                    byk[k] += 1
                    if k < 3:
                        continue
                    c["t1_no_E1_k_ge_3"] += 1

                    ag_rows = [row for row in rows if row[0] == g]
                    if ag_rows:
                        c["A_eq_g_states"] += 1

                    edge_range = False
                    pair_alive = False
                    rooted_alive = False

                    for A, M, D, H, Emin, nu, _ in ag_rows:
                        Emax = math.comb(g, 2) + k * g

                        # In shared-core R2+R2 the two defects are isolated.
                        # If g=2 there is no nondefect H_M center, hence e_X=0;
                        # otherwise one center may safely be allowed all k leaves.
                        e_hi = k if g >= 3 else 0
                        if Emin > e_hi:
                            continue
                        edge_range = True

                        for eX in range(max(0, Emin), e_hi + 1):
                            # J+e_X<=k.  If M=0, any active wrong-head source
                            # would force a z_*--source nonedge, so J=0.
                            Jmax = 0 if M == 0 else k - eX
                            LX = max(0, D + 2 * (Emax - eX))
                            pair_lhs = p * p + k + M - Jmax + LX
                            margin = pair_lhs - (cap - sig)
                            if min_pair_margin is None or margin < min_pair_margin:
                                min_pair_margin = margin
                            if margin > 0:
                                continue
                            pair_alive = True

                            # Second, independent rooted-slot check.  It is not
                            # needed on the current bounded box because no pair
                            # row survives, but is retained for regression.
                            qmax = math.comb(u, 2) - math.comb(k + 1, 2) - k - M
                            EUmax = cap - Y0 - LX
                            rupper = (p - lam) * (p + u) + qmax + EUmax
                            rlower = a + y + 2 + eX + (1 if eX > 0 else 0)
                            if rupper >= rlower:
                                rooted_alive = True

                    if edge_range:
                        c["shared_core_edge_range_states"] += 1
                    if pair_alive:
                        c["shared_core_pair_survivors"] += 1
                    if rooted_alive:
                        c["shared_core_rooted_survivors"] += 1

    expected = {
        "t1_no_E1_states": 933,
        "t1_no_E1_k_ge_3": 509,
        "A_eq_g_states": 477,
        "shared_core_edge_range_states": 147,
        "shared_core_pair_survivors": 0,
        "shared_core_rooted_survivors": 0,
    }
    expected_by_k = {1:223, 2:201, 3:146, 4:104, 5:82,
                     6:60, 7:53, 8:47, 9:17}
    bad = {key: (want, c[key]) for key, want in expected.items()
           if c[key] != want}
    assert dict(sorted(byk.items())) == expected_by_k, (byk, expected_by_k)
    assert min_pair_margin == 9, min_pair_margin

    print({
        "F_k_closed_form_checks": f_checks,
        "counts": dict(c),
        "no_E1_k_distribution": dict(sorted(byk.items())),
        "minimum_shared_core_pair_failure_margin": min_pair_margin,
        "expected_mismatches": bad,
        "failures": len(bad),
        "trust": "abstract integer/arithmetic diagnostic only; no D2C graph-realizability claim",
    })
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
