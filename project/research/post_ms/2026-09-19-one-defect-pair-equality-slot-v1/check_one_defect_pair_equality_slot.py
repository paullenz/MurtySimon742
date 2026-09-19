#!/usr/bin/env python3
"""Diagnostic replay for ONE_DEFECT_PAIR_EQUALITY_SLOT_FEEDBACK.md.

Abstract integer parameter scan only. This is not a D2C graph enumerator and
makes no graph-realizability claim. It independently checks the new closed
d0=0 Psi formula and replays only the additional slot floors derived from
pair equality / near-equality.
"""
import math, runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREV = HERE.parent / "2026-09-19-one-defect-support-cap-v1" / "check_one_defect_support_cap.py"
C = runpy.run_path(str(PREV))

W = C["W"]
C0 = W["C0"]
predecessor_floor = W["predecessor_floor"]
repaired_floor = W["repaired_floor"]
preceding_mg1_score = W["preceding_mg1_score"]
hmin_closed = W["hmin_closed"]
sigma_pair = W["sigma_pair"]
rows_for_state = W["rows_for_state"]
sphere_survives = W["sphere_survives"]
support_sizes = W["support_sizes"]
E1_slot_floor = W["E1_slot_floor"]
RN_range = W["RN_range"]

F0 = C["F0"]
psi_old = C["psi"]
refined_pair_lhs = C["refined_pair_lhs"]


def eta(j):
    """Least q>=0 with binom(q+1,2)>=j."""
    if j <= 0:
        return 0
    q = max(0, (math.isqrt(1 + 8*j) - 1) // 2)
    while q * (q + 1) // 2 < j:
        q += 1
    while q > 0 and (q - 1) * q // 2 >= j:
        q -= 1
    return q


def psi0_closed(k, D):
    """Closed form for min_Delta [D+2Delta]_+ - F_k(Delta), k>1."""
    assert k > 1
    if D >= -7:
        return max(D, -4)
    return max(math.ceil(D / 2) - 1, -(k + 2))


def verify_psi0_closed():
    checks = 0
    for k in range(2, 30):
        for D in range(-120, 121):
            brute = min(max(0, D + 2*Delta) - F0(k, Delta)
                        for Delta in range(k + 70))
            closed = psi0_closed(k, D)
            old = psi_old(k, 0, D)
            assert brute == closed == old, (k, D, brute, closed, old)
            checks += 1
    return checks


def d1_universal_slot(a, y, e):
    """d0=1: the k defect-core zero-rho edges are already forbidden."""
    return a + y + 1 + eta(max(0, e - 1))


def d1_equality_slot(a, y, g, k, D):
    """Exact pair-minimum positive-edge floor in d0=1."""
    Emax = g * (g - 1) // 2 + k * (g - 1)
    jplus = max(0, Emax - max(1, math.floor(-D / 2)))
    return a + y + 1 + eta(jplus)


def d1_near_right_slot(a, y, g, k, D):
    """One unit above the d0=1 right-arm pair minimum, D<=-2."""
    assert D <= -2
    Emax = g * (g - 1) // 2 + k * (g - 1)
    jplus = max(0, Emax - math.floor((1 - D) / 2))
    return a + y + 1 + eta(jplus)


def d0_equality_slot(a, y, g, k, D):
    """Exact pair-minimum positive-edge floor in d0=0, k>1."""
    assert k > 1
    Emax = g * (g - 1) // 2 + k * g
    if -5 <= D <= -3:
        jplus = max(0, Emax - 2)
    else:
        jplus = max(0, Emax - max(k + 1, math.floor(-D / 2)))
    return a + y + 1 + eta(jplus)


def main():
    psi_checks = verify_psi0_closed()
    c = Counter()
    by_t = Counter()

    for p in range(3, 19):
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
            for g in range(0, p):
              k = x - g
              t = p - g
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
              s1 = max(0, t - k + 1)
              Y0 = y * (p + 2)
              Q = x*(x - T0) + k*(x - 1) + x - g*(g - 1) + k*N
              Ebase = k*(p + k) + 2*t + k + g*s1
              if Ebase + Y0 + hmin_closed(Q, k, g, N) > cap:
                  continue

              P0 = k*(p + k) + t + Y0
              O0 = t + k + g*s1
              sig = sigma_pair(p, u, lam, x, y, g, P0, cap)
              if sig is None:
                  continue
              BP = cap - O0 - sig
              if hmin_closed(Q, k, g, N) > BP:
                  continue

              rows = rows_for_state(p, u, lam, x, y, g, k, cap, Q, N, BP, Y0)
              sphere = sphere_survives(p, u, lam, x, y, g, k, cap, Q, N, Y0, sig)

              current_e1 = False
              sharpened_e1 = False
              e2 = False
              current_rows = 0
              sharpened_rows = 0

              for A, M, D, H, Emin, nu, rupper in rows:
                  d0 = g - A

                  # Reproduce the current support-capped E=1 row exactly.
                  e1_current = False
                  if support_sizes(p, g, k, 1) and (
                      (k > 1 and d0 in (0, 1)) or
                      (k == 1 and 0 <= d0 <= 2)
                  ):
                      old_lhs = p*(g + 1) + k + M - (k + 1)*d0 + D
                      old_r1 = E1_slot_floor(x, y, g, k, A, Emin)
                      if old_lhs <= cap - sig and rupper >= old_r1:
                          new_lhs = refined_pair_lhs(p, g, k, M, d0, D)
                          if new_lhs <= cap - sig:
                              e1_current = True
                              current_e1 = True
                              current_rows += 1

                  if e1_current:
                      floor = E1_slot_floor(x, y, g, k, A, Emin)
                      source = "old"

                      if k > 1 and d0 == 1:
                          f = d1_universal_slot(a, y, Emin)
                          if f > floor:
                              floor = f
                              source = "d1_universal"

                          pair_lhs = refined_pair_lhs(p, g, k, M, d0, D)
                          slack = (cap - sig) - pair_lhs

                          if slack == 0:
                              f = d1_equality_slot(a, y, g, k, D)
                              if f > floor:
                                  floor = f
                                  source = "d1_equality"
                          elif slack == 1 and D <= -2:
                              f = d1_near_right_slot(a, y, g, k, D)
                              if f > floor:
                                  floor = f
                                  source = "d1_near"

                      elif k > 1 and d0 == 0:
                          pair_lhs = refined_pair_lhs(p, g, k, M, d0, D)
                          slack = (cap - sig) - pair_lhs
                          if slack == 0:
                              f = d0_equality_slot(a, y, g, k, D)
                              if f > floor:
                                  floor = f
                                  source = "d0_equality"

                      if rupper >= floor:
                          sharpened_e1 = True
                          sharpened_rows += 1
                      else:
                          c["row_rejections"] += 1
                          c["row_rejections_" + source] += 1
                          by_t[("row", t)] += 1

                  r2, _ = RN_range(p, x, y, g, k, Emin, 2)
                  if r2 is not None and rupper >= r2:
                      e2 = True

              if current_e1:
                  c["current_E1_states"] += 1
                  c["current_E1_rows"] += current_rows
                  if t == 1:
                      c["t1_current_E1_states"] += 1
                      c["t1_current_E1_rows"] += current_rows
              if sharpened_e1:
                  c["sharpened_E1_states"] += 1
                  c["sharpened_E1_rows"] += sharpened_rows
                  if t == 1:
                      c["t1_sharpened_E1_states"] += 1
                      c["t1_sharpened_E1_rows"] += sharpened_rows
              if current_e1 and not sharpened_e1:
                  c["E1_state_closures"] += 1
                  by_t[("state", t)] += 1

              current_union = current_e1 or e2 or sphere
              sharpened_union = sharpened_e1 or e2 or sphere
              if current_union:
                  c["current_union"] += 1
              if sharpened_union:
                  c["sharpened_union"] += 1
              if current_union and not sharpened_union:
                  c["union_rejections"] += 1
              if t == 1 and current_union:
                  c["t1_current_union"] += 1
              if t == 1 and sharpened_union:
                  c["t1_sharpened_union"] += 1

              # The exact E=2 fallback diagnostic is meaningful only in t=1
              # states that have no support-capped E=1 route.
              if t == 1 and current_union and not current_e1:
                  c["t1_no_E1_states"] += 1
                  if e2:
                      c["t1_no_E1_with_E2_route"] += 1
                      by_t[("noE1_k", k)] += 1

    expected = {
        "current_E1_states": 48677,
        "sharpened_E1_states": 48672,
        "E1_state_closures": 5,
        "current_E1_rows": 1094326,
        "sharpened_E1_rows": 1094065,
        "row_rejections": 261,
        "row_rejections_d1_universal": 199,
        "row_rejections_d1_equality": 28,
        "row_rejections_d1_near": 1,
        "row_rejections_d0_equality": 33,
        "t1_current_E1_states": 4471,
        "t1_sharpened_E1_states": 4471,
        "t1_current_E1_rows": 111204,
        "t1_sharpened_E1_rows": 111197,
        "current_union": 64457,
        "sharpened_union": 64457,
        "union_rejections": 0,
        "t1_current_union": 5404,
        "t1_sharpened_union": 5404,
        "t1_no_E1_states": 933,
        "t1_no_E1_with_E2_route": 933,
    }
    bad = {key: (want, c[key]) for key, want in expected.items()
           if c[key] != want}

    expected_state_by_t = {4: 2, 8: 1, 9: 1, 11: 1}
    got_state_by_t = {t: by_t[("state", t)] for t in range(1, 19)
                      if by_t[("state", t)]}
    assert got_state_by_t == expected_state_by_t, (got_state_by_t, expected_state_by_t)

    expected_noE1_k = {1:223, 2:201, 3:146, 4:104, 5:82,
                       6:60, 7:53, 8:47, 9:17}
    got_noE1_k = {k: by_t[("noE1_k", k)] for k in range(1, 20)
                  if by_t[("noE1_k", k)]}
    assert got_noE1_k == expected_noE1_k, (got_noE1_k, expected_noE1_k)

    print({
        "psi0_formula_checks": psi_checks,
        "counts": dict(c),
        "E1_state_closures_by_t": got_state_by_t,
        "t1_no_E1_E2_k_distribution": got_noE1_k,
        "expected_mismatches": bad,
        "failures": len(bad),
        "trust": "abstract integer/arithmetic diagnostic only; no graph-realizability claim",
    })
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
