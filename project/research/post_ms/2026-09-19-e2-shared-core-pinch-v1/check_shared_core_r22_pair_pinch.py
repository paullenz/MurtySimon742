#!/usr/bin/env python3
"""Diagnostic replay for SHARED_CORE_R22_PAIR_PINCH.md.

Abstract integer parameter scan only. This is NOT a D2C graph enumerator and
makes no graph-realizability claim.
"""
import math, runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREV = HERE.parent / "2026-09-19-one-defect-pair-equality-slot-v1" / "check_one_defect_pair_equality_slot.py"
E1 = runpy.run_path(str(PREV))

W = E1["W"]
C0 = W["C0"]
predecessor_floor = W["predecessor_floor"]
repaired_floor = W["repaired_floor"]
preceding_mg1_score = W["preceding_mg1_score"]
hmin_closed = W["hmin_closed"]
sigma_pair = W["sigma_pair"]
rows_for_state = W["rows_for_state"]
support_sizes = W["support_sizes"]
E1_slot_floor = W["E1_slot_floor"]
refined_pair_lhs = E1["refined_pair_lhs"]


def eta2(j):
    """Least q>=0 with binom(q+2,2)>=j."""
    if j <= 0:
        return 0
    q = 0
    while (q + 2) * (q + 1) // 2 < j:
        q += 1
    return q


def main():
    c = Counter()
    byk = Counter()
    shared_byk = Counter()
    exact_byk = Counter()
    near_byk = Counter()

    for p in range(3, 19):
      g = p - 1  # t=1
      for u in range(1, 19):
        b = 2*p + u
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
            Q = x*(x - T0) + k*(x - 1) + x - g*(g - 1) + k*N
            Ebase = k*(p + k) + 2 + k + g*s1
            if Ebase + Y0 + hmin_closed(Q, k, g, N) > cap:
                continue

            P0 = k*(p + k) + 1 + Y0
            O0 = 1 + k + g*s1
            sig = sigma_pair(p, u, lam, x, y, g, P0, cap)
            if sig is None:
                continue
            BP = cap - O0 - sig
            if hmin_closed(Q, k, g, N) > BP:
                continue

            rows = rows_for_state(p, u, lam, x, y, g, k, cap, Q, N, BP, Y0)
            if not rows:
                continue
            c["t1_pair_hall_states"] += 1

            # Reproduce the predecessor's support-capped E1 route.
            has_e1 = False
            for A, M, D, H, Emin, nu, rupper in rows:
                d0 = g - A
                if not support_sizes(p, g, k, 1):
                    continue
                if not ((k > 1 and d0 in (0, 1)) or (k == 1 and 0 <= d0 <= 2)):
                    continue
                old_lhs = p*(g + 1) + k + M - (k + 1)*d0 + D
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

            # Shared-core/double-active R2+R2: h=1,c=2,d0=2, so A=g-2.
            Astar = g - 2
            Emax = math.comb(g, 2) + k*Astar
            shared = False
            exact = False
            near = False

            for A, M, D, H, Emin, nu, rupper in rows:
                if A != Astar:
                    continue

                pair_lhs = p*(g + 1) + k + M - 2*(k + 1) + max(D, -6)
                if pair_lhs > cap - sig:
                    continue

                # Universal two-zero-edge slot floor.
                universal_floor = a + y + 2 + eta2(max(0, Emin - 2))
                if rupper >= universal_floor:
                    shared = True

                pair_slack = (cap - sig) - pair_lhs
                if D <= -6 and pair_slack <= 1:
                    # All three bidirected channels are active. All surviving
                    # X-edges have positive Hamming excess, and Hall gives
                    # Delta <= floor((s-D)/2).
                    e_pin = max(Emin, Emax - math.floor((pair_slack - D) / 2))
                    pinch_floor = a + y + 2 + eta2(max(0, e_pin))
                    if rupper >= pinch_floor:
                        near = True
                        if pair_slack == 0:
                            exact = True

            if shared:
                c["shared_core_route_states"] += 1
                shared_byk[k] += 1
            else:
                c["no_shared_core_route_states"] += 1

            if exact:
                c["shared_core_deep_exact_states"] += 1
                exact_byk[k] += 1
            if near:
                c["shared_core_deep_slack_le_1_states"] += 1
                near_byk[k] += 1

    expected = {
        "t1_pair_hall_states": 5404,
        "t1_no_E1_states": 933,
        "t1_no_E1_k_ge_3": 509,
        "shared_core_route_states": 65,
        "no_shared_core_route_states": 444,
        "shared_core_deep_exact_states": 48,
        "shared_core_deep_slack_le_1_states": 49,
    }
    bad = {key: (want, c[key]) for key, want in expected.items() if c[key] != want}

    expected_k = {1:223, 2:201, 3:146, 4:104, 5:82, 6:60, 7:53, 8:47, 9:17}
    expected_shared = {3:23, 4:15, 5:17, 6:6, 7:4}
    expected_exact = {3:23, 4:11, 5:11, 6:3}
    expected_near = {3:23, 4:11, 5:11, 6:4}

    assert dict(sorted(byk.items())) == expected_k, (byk, expected_k)
    assert dict(sorted(shared_byk.items())) == expected_shared, (shared_byk, expected_shared)
    assert dict(sorted(exact_byk.items())) == expected_exact, (exact_byk, expected_exact)
    assert dict(sorted(near_byk.items())) == expected_near, (near_byk, expected_near)

    print({
        "counts": dict(c),
        "no_E1_k_distribution": dict(sorted(byk.items())),
        "shared_core_route_by_k": dict(sorted(shared_byk.items())),
        "deep_exact_by_k": dict(sorted(exact_byk.items())),
        "deep_slack_le_1_by_k": dict(sorted(near_byk.items())),
        "expected_mismatches": bad,
        "failures": len(bad),
        "trust": "abstract integer/arithmetic diagnostic only; no D2C graph-realizability claim",
    })
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
