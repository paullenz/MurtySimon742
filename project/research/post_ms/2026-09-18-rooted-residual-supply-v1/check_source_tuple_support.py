#!/usr/bin/env python3
"""Audit support for SOURCE_TUPLE_SUPPORT_AND_ZERO_BETA_CAPACITY.md."""

from fractions import Fraction
from math import comb
import json
import random


def C_hat(p, u, r, K):
    if u < r or p - K < r:
        return 0
    return ((K + r) * comb(u, r)) // (r * comb(p - K, r))


def Phi(p, u, r, N):
    return sum(max(0, N - C_hat(p, u, r, K)) for K in range(0, p - r + 1))


summary = {}

# 1. Random load profiles filtered through the exact r=3 threshold hierarchy.
random.seed(74214)
valid = 0
trials = 0
while valid < 100_000 and trials < 2_000_000:
    trials += 1
    p = random.randint(3, 10)
    u = random.randint(1, 10)
    a = random.randint(1, 10)
    L = min(p, u)
    ells = [random.randint(0, L) for _ in range(a)]
    r = 3

    ok = True
    for K in range(0, p - r + 1):
        N_K = sum((p - ell) <= K for ell in ells)
        if N_K > C_hat(p, u, r, K):
            ok = False
            break
    if not ok:
        continue

    positive = [ell for ell in ells if ell > 0]
    N = len(positive)
    B = sum(positive)
    assert N * p - B >= Phi(p, u, r, N)

    candidates = [n for n in range(a + 1) if n * p - Phi(p, u, r, n) >= B]
    if candidates:
        assert N >= min(candidates)

    valid += 1

summary["finite_support_valid_random"] = valid
summary["finite_support_trials"] = trials

# 2. Exact rational check of the r=3 continuum support parametrization.
count = 0
for rho_num in range(1, 13):
    rho = Fraction(rho_num, 4)
    for k_num in range(1, 99):
        kappa = Fraction(k_num, 100)
        nu = rho**3 * kappa / (3 * (1 - kappa) ** 3)
        I = kappa * kappa / (2 * (1 - kappa) ** 2)
        phi = nu * kappa - rho**3 * I / 3
        beta = rho**3 * kappa * (2 + kappa) / (6 * (1 - kappa) ** 2)
        assert nu - phi == beta
        count += 1
summary["triple_continuum_exact"] = count

summary["total_checks"] = summary["finite_support_valid_random"] + summary["triple_continuum_exact"]
summary["failures"] = 0
print(json.dumps(summary, indent=2, sort_keys=True))
