#!/usr/bin/env python3
"""Audit support for DISTINCT_SOURCE_BETA_CEILING_AND_Q_CAPACITY.md.

The mathematical claims are proved by hand in the note.  This script checks
four independent pieces of arithmetic/combinatorics:

1. the local complement-avoidance kernel behind (BQ);
2. the exact finite root-wedge algebra;
3. the finite switching/distinct-source implication over a dense integer grid;
4. the continuum small-rho exclusion and comparison of the new beta-sensitive
   q cap with the old sparse-U cap.
"""

from itertools import combinations, product
import json
import math


def c_lambda(lam):
    num = lam * (lam + 2)
    return (num + 1) // 2 if num % 2 else num // 2


def rhat(p, u, lam):
    a = 2 * p + u - lam - 1
    C0 = p * lam + 3 * p + u * lam + 2 * u - c_lambda(lam) - 4
    if C0 < 0:
        return a, C0, None
    Rstar = max(2, (1 + math.isqrt(1 + 4 * C0)) // 2)
    return a, C0, min(p, Rstar)


def main():
    # ------------------------------------------------------------------
    # 1. Local complement-avoidance kernel.
    # Translate c(x) to the all-zero word.  For each target set I and
    # designated target i in I, enumerate every completion outside I of a
    # source satisfying c(y)|I = c(x)|I Delta {i}.  If |I|>=2 that source
    # can never be the complementary all-one code.
    # ------------------------------------------------------------------
    local_code_checks = 0
    for p in range(1, 9):
        coords = range(p)
        for ell in range(p + 1):
            for Itup in combinations(coords, ell):
                I = set(Itup)
                for i in I:
                    outside = [j for j in coords if j not in I]
                    for bits in product([0, 1], repeat=len(outside)):
                        y = [0] * p
                        y[i] = 1
                        for j, bit in zip(outside, bits):
                            y[j] = bit
                        local_code_checks += 1
                        if ell >= 2:
                            assert not all(y)

    # ------------------------------------------------------------------
    # 2. Exact finite root wedge.
    # If pL <= u(u-L), then L(p+u)<=u^2 and therefore
    # L<=floor(u^2/(p+u)).
    # ------------------------------------------------------------------
    finite_root_wedge_checks = 0
    for p in range(3, 81):
        for u in range(1, p + 1):
            for L in range(1, u):
                if p * L <= u * (u - L):
                    finite_root_wedge_checks += 1
                    assert L <= (u * u) // (p + u)

    # ------------------------------------------------------------------
    # 3. Finite switching/distinct-source implication.
    # On every parameter triple with nonnegative scorecard allowance,
    # compatibility of the switching lower beta bound with B<=au forces
    # pu<=a(u+R_hat).
    # ------------------------------------------------------------------
    finite_switching_compatible_cases = 0
    finite_switching_rejected_cases = 0
    for p in range(3, 81):
        for u in range(1, p + 1):
            for lam in range(0, 2 * p + u - 1):
                a, C0, R = rhat(p, u, lam)
                if a <= 0 or C0 < 0:
                    continue
                beta_lo = max(0, p * u - R * a)
                beta_hi = a * u
                if beta_lo <= beta_hi:
                    finite_switching_compatible_cases += 1
                    assert p * u <= a * (u + R)
                else:
                    finite_switching_rejected_cases += 1

    # ------------------------------------------------------------------
    # 4. Continuum checks.
    # For rho<=2-sqrt(3), every sampled theta>2 violates the strict
    # switching/distinct-source requirement A(rho+R)>rho.
    # ------------------------------------------------------------------
    rho_star = 2 - math.sqrt(3)
    small_rho_boundary_grid_checks = 0
    small_rho_boundary_max_margin = -float("inf")
    small_rho_boundary_max_at = None
    for ir in range(1, 501):
        rho = rho_star * ir / 500
        for it in range(1, 101):
            theta = 2 + rho * it / 101
            A = 2 + rho - theta
            c = theta * (1 + rho) - theta * theta / 2
            if c <= 0:
                continue
            R = min(1.0, math.sqrt(c))
            margin = A * (rho + R) - rho
            small_rho_boundary_grid_checks += 1
            if margin > small_rho_boundary_max_margin:
                small_rho_boundary_max_margin = margin
                small_rho_boundary_max_at = [rho, theta]
            assert margin < 0

    # On the surviving small-rho high-imbalance slice, compare the new
    # beta-sensitive q cap xi<=A(rho+R)-rho with old xi<=R A^2.
    # The hand factorization is
    #   [A(rho+R)-rho] - R A^2 = (1-A)(AR-rho),
    # so it is negative whenever A<1 and AR<rho.
    beta_q_vs_sparse_u_checks = 0
    beta_q_vs_sparse_u_max_difference = -float("inf")
    for ir in range(1, 401):
        rho = rho_star + (0.5 - rho_star) * ir / 400
        theta_cap = 2 + rho * rho / (1 + rho)
        for it in range(1, 101):
            theta = 2 + (theta_cap - 2) * it / 101
            A = 2 + rho - theta
            c = theta * (1 + rho) - theta * theta / 2
            R = min(1.0, math.sqrt(c))
            beta_lb = max(theta - 2, rho - A * R)
            q_new = A * rho - beta_lb
            q_old = R * A * A
            diff = q_new - q_old
            beta_q_vs_sparse_u_checks += 1
            beta_q_vs_sparse_u_max_difference = max(
                beta_q_vs_sparse_u_max_difference, diff
            )
            assert diff < 0

    summary = {
        "local_code_checks": local_code_checks,
        "finite_root_wedge_checks": finite_root_wedge_checks,
        "finite_switching_compatible_cases": finite_switching_compatible_cases,
        "finite_switching_rejected_cases": finite_switching_rejected_cases,
        "small_rho_boundary_grid_checks": small_rho_boundary_grid_checks,
        "small_rho_boundary_max_margin": small_rho_boundary_max_margin,
        "small_rho_boundary_max_at": small_rho_boundary_max_at,
        "beta_q_vs_sparse_u_checks": beta_q_vs_sparse_u_checks,
        "beta_q_vs_sparse_u_max_difference": beta_q_vs_sparse_u_max_difference,
        "total_checks": (
            local_code_checks
            + finite_root_wedge_checks
            + finite_switching_compatible_cases
            + finite_switching_rejected_cases
            + small_rho_boundary_grid_checks
            + beta_q_vs_sparse_u_checks
        ),
        "failures": 0,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
