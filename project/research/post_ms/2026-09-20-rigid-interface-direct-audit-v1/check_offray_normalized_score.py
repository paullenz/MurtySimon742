#!/usr/bin/env python3
"""Diagnostic grid for the residual-one k=2 off-ray normalized score.

This is not a proof or completeness scan. It samples the asymptotic functional
from ONE_CODE_R1_K2_OFFRAY_NORMALIZED_SCORE_AND_HIGH_Y_GAP.md to identify
candidate scaling regions for subsequent analytic work.
"""

from math import sqrt


def s0(kappa, theta):
    return ((1.0 + kappa) ** 2 - theta**2) / 2.0


def root_margin(kappa, theta):
    return s0(kappa, theta) + kappa * theta - 1.0


def score(kappa, theta, eta, t):
    # q=eta*t; physical domain 0<=eta<=kappa, 0<=t<=kappa-eta.
    if eta == 0.0:
        y0 = kappa * theta
        z0 = kappa * theta
        return z0 + y0 + kappa * (kappa - theta)
    q = eta * t
    y0 = eta * theta + max(0.0, theta * (kappa - 2.0 * eta), t * t)
    z0 = max(kappa * theta + eta, eta + y0)
    return z0 + y0 + kappa * (kappa - theta) - 2.0 * q


def grid_min(kappa, theta, steps=240):
    best = (float("inf"), None)
    for i in range(steps + 1):
        eta = kappa * i / steps
        if i == 0:
            val = score(kappa, theta, 0.0, 0.0)
            if val < best[0]:
                best = (val, (0.0, 0.0))
            continue
        tmax = kappa - eta
        for j in range(steps + 1):
            t = tmax * j / steps
            val = score(kappa, theta, eta, t)
            if val < best[0]:
                best = (val, (eta, t))
    return best


def main():
    print("theta root_kappa sample_feasible_kappa_range")
    for theta in (0.50, 0.75, 0.90, 0.95, 0.97, 0.98, 0.99, 0.995, 0.999, 1.0):
        root_k = sqrt(2.0 * (theta * theta + theta + 1.0)) - (1.0 + theta)
        feasible = []
        for i in range(36, 161):
            kappa = i / 100.0
            if root_margin(kappa, theta) < 0:
                continue
            val, _ = grid_min(kappa, theta, steps=80)
            if val <= s0(kappa, theta):
                feasible.append(kappa)
        if feasible:
            rng = f"[{min(feasible):.2f},{max(feasible):.2f}]"
        else:
            rng = "none on sampled grid"
        print(f"{theta:.3f} {root_k:.6f} {rng}")

    # The analytic endpoint theorem says theta=1 has no true feasible point.
    # A coarse grid can only overestimate the minimum score, so this final line
    # is a consistency check, not a proof.
    print("theta=1 analytic endpoint: strictly closed for every kappa>0")


if __name__ == "__main__":
    main()
