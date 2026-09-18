#!/usr/bin/env python3

from math import comb
from fractions import Fraction
import random
import json


def U_r(p, u, K, r):
    return ((K + r) * comb(u, r)) // (r * comb(p - K, r))


summary = {
    "finite_3p_checks": 0,
    "finite_3p_failures": 0,
    "layer_cake_checks": 0,
    "layer_cake_failures": 0,
    "rational_cap_checks": 0,
    "rational_cap_failures": 0,
}

# Finite 3p corollary.  lambda=3p is the weakest boundary case;
# increasing lambda only raises the beta lower bound and lowers a.
for p in range(10, 401):
    ucap = U_r(p, 2 * p, 1, 3)
    summary["finite_3p_checks"] += 1
    if ucap > 2 * p - 2:
        summary["finite_3p_failures"] += 1

    # At lambda=3p, positive a requires u>=p+2.
    for u in range(p + 2, 2 * p + 1):
        a = u - p - 1
        beta_lower = p * (p + 1)
        beta_upper = a * (p - 2) + 2 * U_r(p, u, 1, 3)
        summary["finite_3p_checks"] += 1
        if not beta_upper < beta_lower:
            summary["finite_3p_failures"] += 1

# Exact dyadic layer-cake identity used in the cylinder-scale proof.
rng = random.Random(742)
for _ in range(10000):
    p = rng.randint(3, 25)
    a = rng.randint(0, 30)
    deficits = [rng.randint(0, p) for _ in range(a)]

    # Multiply sum_x 2^{-k_x} by 2^p.
    lhs = sum(2 ** (p - k) for k in deficits)

    # sum_{K>=0} N_K / 2^{K+1}; after K=p-1 the tail is a/2^p.
    rhs = sum(
        sum(1 for k in deficits if k <= K) * 2 ** (p - K - 1)
        for K in range(p)
    ) + a

    summary["layer_cake_checks"] += 1
    if lhs != rhs:
        summary["layer_cake_failures"] += 1

# Exact rational endpoint in Corollary 6.1.
theta = Fraction(3227, 1088)
kappa = Fraction(1, 9)
rho = Fraction(2, 1)
A = Fraction(2, 1) + rho - theta
rhs = A * (1 - kappa) + (kappa * kappa / Fraction(3, 1)) * (
    rho / (1 - kappa)
) ** 3
summary["rational_cap_checks"] += 1
if theta - Fraction(2, 1) != rhs:
    summary["rational_cap_failures"] += 1

# A deterministic exact-rational grid just above the claimed cap.
theta_test = theta + Fraction(1, 100000)
for j in range(1, 2001):
    rho = Fraction(j, 1000)
    A = Fraction(2, 1) + rho - theta_test
    if A <= 0:
        continue
    rhs = A * (1 - kappa) + (kappa * kappa / Fraction(3, 1)) * (
        rho / (1 - kappa)
    ) ** 3
    summary["rational_cap_checks"] += 1
    if not theta_test - Fraction(2, 1) > rhs:
        summary["rational_cap_failures"] += 1

summary["total_checks"] = (
    summary["finite_3p_checks"]
    + summary["layer_cake_checks"]
    + summary["rational_cap_checks"]
)
summary["total_failures"] = (
    summary["finite_3p_failures"]
    + summary["layer_cake_failures"]
    + summary["rational_cap_failures"]
)

print(json.dumps(summary, indent=2, sort_keys=True))

assert summary["total_failures"] == 0
