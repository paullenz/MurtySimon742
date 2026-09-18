#!/usr/bin/env python3
"""Audit support for RESIDUAL_SPLIT_ALIGNED_MATCHED_CAPACITY.md.

The random checks audit algebra only.  The finite scan is a diagnostic using
only the root-imbalance beta floor and the r=3 source-support profile; it is
not a proof search or a substitute for the hand inequalities.
"""

from fractions import Fraction
from math import comb, isqrt
import bisect
import json
import random

random.seed(74218011)


def c_lambda(lam):
    return (lam * (lam + 2) + 1) // 2


def D_M(p, u, lam):
    return (4 * p + 2 * u - c_lambda(lam) - 1) // 2


def R_A(L):
    return max(2, (1 + isqrt(1 + 4 * L)) // 2)


def R_code(S, p, u, lam):
    D0 = 5 * p + 5 * u - 3 * lam - 2
    return max(0, (D0 + isqrt(D0 * D0 + 12 * S)) // 3)


def cap_plus(p, u, lam, S, E):
    a = 2 * p + u - lam - 1
    LA = S - E
    L0 = lam + 1
    R = R_code(S, p, u, lam)
    r = R_A(LA)
    matched = min(Fraction(a * r, 1),
                  Fraction(p * R, 2) + Fraction(r * LA, L0))
    nonmatched = Fraction(R * (2 * LA + S), 2 * L0)
    return matched + nonmatched


def phi3_array(p, u, Nmax):
    if p < 3:
        return [0] * (Nmax + 1)
    cu = comb(u, 3)
    thresholds = []
    for K in range(0, p - 2):
        den = 3 * comb(p - K, 3)
        thresholds.append(((K + 3) * cu) // den if den else 0)
    return [sum(max(0, N - c) for c in thresholds)
            for N in range(Nmax + 1)]


summary = {}

# 1. Exact residual split.
N = 200_000
for _ in range(N):
    p = random.randint(1, 50)
    u = random.randint(0, 50)
    lam = random.randint(0, 2 * p + u - 1)
    delta = random.randint(-500, 500)
    q = random.randint(0, comb(u, 2) if u >= 2 else 0)
    E = random.randint(0, 500)
    Q = p * (p + u - 1) + q
    f = (p - lam) * (p + u) + q + E - delta
    assert delta == E + Q - f - lam * (p + u) + p
summary["residual_split_identity"] = N

# 2. q floor from s<=au.
target = 200_000
valid = 0
while valid < target:
    p = random.randint(1, 50)
    u = random.randint(1, 50)
    lam = random.randint(0, 2 * p + u - 1)
    a = 2 * p + u - lam - 1
    if a < 0:
        continue
    q = random.randint(0, comb(u, 2) if u >= 2 else 0)
    s = random.randint(0, a * u)
    E = u * (p + u - 1) - 2 * q - s
    if E < 0:
        continue
    q_floor = max(0, (u * (lam - p) - E + 1) // 2)
    assert q >= q_floor
    valid += 1
summary["cross_edge_q_floor"] = valid

# 3. Load-one compression.
N = 150_000
for _ in range(N):
    p = random.randint(2, 30)
    u = random.randint(1, 30)
    a = random.randint(1, 30)
    m = min(p, u)
    ells = [random.randint(0, m) for __ in range(a)]
    B = sum(ells)
    N1 = sum(ell == 1 for ell in ells)
    if m >= 2:
        bound = (m * a - B) // (m - 1)
        assert N1 <= bound
        assert a * u - B + N1 <= a * u - B + bound
summary["load_one_compression"] = N

# 4. Abstract algebra behind the aligned-code matched cap.
N = 200_000
for _ in range(N):
    pair_count = random.randint(1, 30)
    p = random.randint(pair_count, 80)
    cuts = sorted(random.sample(range(1, p), pair_count - 1)) \
        if pair_count > 1 else []
    gs = []
    prev = 0
    for cut in cuts + [p]:
        gs.append(cut - prev)
        prev = cut

    R = random.randint(0, 60)
    LA = random.randint(0, 500)
    L0 = random.randint(1, 40)
    r = random.randint(2, 30)
    majority_caps = [Fraction(random.randint(0, R), 2)
                     for __ in range(pair_count)]
    paired_budget = Fraction(r * LA, L0)
    paired = random.randint(0, int(paired_budget)) \
        if paired_budget >= 1 else 0
    traffic_upper = sum(Fraction(g) * m
                        for g, m in zip(gs, majority_caps)) + paired
    assert traffic_upper <= Fraction(p * R, 2) + paired_budget
summary["aligned_matched_cap"] = N

# 5. Monotonicity needed for scalar split feasibility.
N = 100_000
for _ in range(N):
    p = random.randint(2, 30)
    u = random.randint(0, 30)
    lam = random.randint(0, 2 * p + u - 2)
    S = random.randint(0, 500)
    E = random.randint(0, S)
    c = cap_plus(p, u, lam, S, E)
    if E < S:
        assert cap_plus(p, u, lam, S, E + 1) <= c
    assert cap_plus(p, u, lam, S + 1, E) >= c
summary["split_cap_monotonicity"] = N

# 6. Conservative scalar diagnostic: 3<=p<=30, 1<=u<=2p.
# Only RBF and the r=3 support profile are used for the beta/source floor.
parameter_tuples = 0
beta_impossible = 0
remaining = 0
old_closures = 0
new_closures = 0
positive_F0 = 0
positive_F0_matched_improvements = 0
min_ratio = None

for p in range(3, 31):
    for u in range(1, 2 * p + 1):
        maxa = 2 * p + u - 1
        ph = phi3_array(p, u, maxa)
        capacities = [n * p - ph[n] for n in range(maxa + 1)]

        for lam in range(0, 2 * p + u):
            a = 2 * p + u - lam - 1
            if a <= 0:
                continue
            dm = D_M(p, u, lam)
            C0 = 2 * (dm - 1) + lam * (p + u) - p
            if C0 < 0:
                continue
            parameter_tuples += 1

            m = min(p, u)
            B = max(0, p * (lam + 1 - 2 * p))
            if B > m * a:
                beta_impossible += 1
                continue

            if B == 0:
                Nsup = 0
            else:
                Nsup = (B + m - 1) // m
                j = bisect.bisect_left(capacities, B, 0, a + 1)
                if j > a:
                    beta_impossible += 1
                    continue
                Nsup = max(Nsup, j)
                if Nsup > a:
                    beta_impossible += 1
                    continue

            E = max(0,
                    u * (p + u - 1) - 3 * a * u + B
                    + u * Nsup - 2 * a)
            if E > C0:
                beta_impossible += 1
                continue

            if m == 1:
                qmax = min(comb(u, 2), a * u)
            else:
                N1max = (m * a - B) // (m - 1)
                qmax = min(comb(u, 2), a * u - B + N1max)
            E = max(E, max(0, u * (lam - p) - 2 * qmax))
            if E > C0:
                new_closures += 1
                remaining += 1
                continue

            remaining += 1
            F0 = (p - lam) * (p + u) - dm + 1
            R = R_code(C0, p, u, lam)
            LA = C0 - E
            old_cap = (Fraction(a * R_A(LA), 1)
                       + Fraction(R * (2 * LA + C0), 2 * (lam + 1)))
            if F0 > old_cap:
                old_closures += 1

            qfloor = max(0, (u * (lam - p) - E + 1) // 2)
            new_cap = cap_plus(p, u, lam, C0, E)
            if F0 + E + qfloor > new_cap:
                new_closures += 1

            if old_cap > 0:
                ratio = float(new_cap / old_cap)
                min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
            if F0 > 0:
                positive_F0 += 1
                old_matched = Fraction(a * R_A(LA), 1)
                aligned_matched = (Fraction(p * R, 2)
                                   + Fraction(R_A(LA) * LA, lam + 1))
                if aligned_matched < old_matched:
                    positive_F0_matched_improvements += 1

summary["diagnostic_parameter_tuples"] = parameter_tuples
summary["diagnostic_beta_impossible"] = beta_impossible
summary["diagnostic_remaining"] = remaining
summary["diagnostic_old_scalar_closures"] = old_closures
summary["diagnostic_new_scalar_closures"] = new_closures
summary["diagnostic_min_capacity_ratio"] = min_ratio
summary["diagnostic_positive_F0"] = positive_F0
summary["diagnostic_positive_F0_matched_improvements"] = positive_F0_matched_improvements

summary["algebra_checks_total"] = (
    summary["residual_split_identity"]
    + summary["cross_edge_q_floor"]
    + summary["load_one_compression"]
    + summary["aligned_matched_cap"]
    + summary["split_cap_monotonicity"]
)
summary["failures"] = 0

print(json.dumps(summary, indent=2, sort_keys=True))
