#!/usr/bin/env python3
"""Diagnostic replay for the residual-one k=2 exact-ray score closure.

This is NOT a graph enumeration and NOT a substitute for the analytic proof in
ONE_CODE_R1_K2_ALL_YU_TRIANGULAR_AND_EXACT_RAY_ASYMPTOTIC_CLOSURE.md.

It minimizes a conservative real-valued finite-p lower bound over the integer
parameters b=|B0| and C=e(B0,U\B0).  The isolation term uses the real Cauchy
lower bound rather than an integer ceiling, so any positive margin is safe for
this relaxation.  Candidate-point minimization is checked exhaustively for
small p when --self-test is supplied.
"""

from __future__ import annotations

import argparse
import math


def C0(p: int) -> int:
    return (3 * p * p + 10 * p - 4) // 2


def score_lower_bound(p: int, b: int, C: int) -> float:
    """Conservative lower bound for E_U+L_A at fixed (p,b,C)."""
    u = p + 1
    y = p - 1
    d = u - b

    # Global H/Y hole floor with the extra double-hole price of B0.
    z_total = p * p + (b - 1) * p - 2

    # All non-B0 U-sources have total oriented U--U capacity at most 2.
    # Hence e(U) <= C + 2d, and E_U = Z - 2e(U) on the exact ray.
    e_u_slack = max(0.0, z_total - 2 * C - 4 * d)

    # Y is independent.  B0 is Y-anticomplete.
    # Capacity holes in D=U\B0:
    cap_holes_D = y * (d - b) - d

    # All but 2d cross edges are sourced in B0.  Cauchy isolation charge.
    R = max(0.0, C - 2 * d)
    iso_holes_D = max(0.0, R * (R - b) / (b * b))

    z_y = b * y + max(0.0, cap_holes_D, iso_holes_D)
    l_y = max(0.0, z_y - y)

    return e_u_slack + l_y


def candidate_minimum(p: int) -> tuple[float, int, int]:
    """Minimize over the analytic candidate points for each b."""
    best = (float("inf"), -1, -1)
    for b in range(2, p + 2):
        d = p + 1 - b
        cmax = b * d
        candidates = {0, cmax}

        def add_near(x: float, radius: int = 4) -> None:
            base = math.floor(x)
            for k in range(-radius, radius + 1):
                c = base + k
                if 0 <= c <= cmax:
                    candidates.add(c)

        add_near(2 * d)
        add_near(2 * d + b)

        A = (p - 1) * (d - b) - d
        if A > 0:
            # Isolation term meets the capacity-hole term.
            R = b * (1.0 + math.sqrt(1.0 + 4.0 * A)) / 2.0
            add_near(2 * d + R)

        # Stationary point once the isolation term is active.
        add_near(2 * d + b * b + b / 2.0)

        for C in candidates:
            val = score_lower_bound(p, b, C)
            if val < best[0]:
                best = (val, b, C)

    return best


def exhaustive_minimum(p: int) -> tuple[float, int, int]:
    best = (float("inf"), -1, -1)
    for b in range(2, p + 2):
        d = p + 1 - b
        for C in range(b * d + 1):
            val = score_lower_bound(p, b, C)
            if val < best[0]:
                best = (val, b, C)
    return best


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-p", type=int, default=10000)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        for p in range(5, 31):
            a = candidate_minimum(p)
            e = exhaustive_minimum(p)
            if abs(a[0] - e[0]) > 1e-9:
                raise SystemExit(f"candidate mismatch at p={p}: {a} != {e}")
        print("small-p candidate self-test: PASS")

    first_persistent = None
    all_positive_after = True
    records = []
    for p in range(args.max_p, 2, -1):
        val, b, C = candidate_minimum(p)
        margin = val - C0(p)
        if margin <= 0:
            all_positive_after = False
        elif all_positive_after:
            first_persistent = p
        records.append((p, val, b, C, margin))

    # The descending pass above makes first_persistent the smallest p in the
    # scanned range after which all scanned margins are positive.
    if first_persistent is None:
        print("no persistent positive range found")
    else:
        val, b, C = candidate_minimum(first_persistent)
        print(
            "diagnostic persistent positive range begins at p=",
            first_persistent,
            " margin=",
            val - C0(first_persistent),
            " b=",
            b,
            " C=",
            C,
            sep="",
        )

    eta_star = 1.0 / 3.0
    t_star = 1.0 / math.sqrt(3.0)
    asymptotic_floor = 2.0 - 2.0 / (3.0 * math.sqrt(3.0))
    print(f"analytic eta*=1/3={eta_star:.12f}")
    print(f"analytic t*=1/sqrt(3)={t_star:.12f}")
    print(f"analytic score coefficient={asymptotic_floor:.12f}")
    print(f"asymptotic margin over 3/2={asymptotic_floor - 1.5:.12f}")


if __name__ == "__main__":
    main()
