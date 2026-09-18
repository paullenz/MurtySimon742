#!/usr/bin/env python3
"""Independent arithmetic/combinatorial audit support.

This checker does not prove the promoted graph-theoretic statements.  It audits:
- the combined complementary-pair algebra on random nonnegative integer data;
- the four-vertex safe-incidence table exhaustively;
- the integer compression 4 R_eta - eta <= 6;
- the second-extremal edge-envelope arithmetic used by the z=4 theorem.
"""

from itertools import combinations
from math import floor, sqrt
from collections import Counter
import json
import random


def M(n):
    return floor((n - 1) ** 2 / 4) + 1


def edges_from_mask(mask):
    pairs = list(combinations(range(4), 2))
    return {
        tuple(sorted(e))
        for i, e in enumerate(pairs)
        if (mask >> i) & 1
    }


def adj(E, u, v):
    return tuple(sorted((u, v))) in E


def dominates(E, S):
    S = set(S)
    for z in range(4):
        if z not in S and not any(adj(E, z, s) for s in S):
            return False
    return True


def safe_coords(E, S):
    """Coordinates satisfying the hand-safe conditions from Lemma 5.1."""
    S = set(S)
    out = []
    for z in S:
        # wz must be triangular.
        if not any(q != z and q in S and adj(E, z, q) for q in S):
            continue

        ok = True

        # Forward Z-witness q: q is in S and nonadjacent to z.
        # It is blocked if z,q already have another common J-neighbour.
        for q in S:
            if q == z:
                continue
            if not adj(E, z, q):
                common = [
                    r for r in range(4)
                    if r not in (z, q) and adj(E, z, r) and adj(E, q, r)
                ]
                if not common:
                    ok = False
                    break
        if not ok:
            continue

        # Reverse Z-witness q: q is adjacent to z but outside S.
        # It is blocked if q has a second neighbour in S besides z.
        for q in range(4):
            if q in S or q == z:
                continue
            if adj(E, z, q):
                second = [r for r in S if r != z and adj(E, q, r)]
                if not second:
                    ok = False
                    break

        if ok:
            out.append(z)
    return out


summary = {}

# ------------------------------------------------------------------
# 1. Combined complementary-pair capacity algebra.
# ------------------------------------------------------------------
random.seed(7421801)
trials = 500_000
failures = 0

for _ in range(trials):
    L = random.randint(1, 30)  # lambda+1

    n0 = random.randint(0, 20)
    n1 = random.randint(0, 20)
    t0 = random.randint(0, 20)
    t1 = random.randint(0, 20)

    N0, N1 = n0 + t0, n1 + t1
    w0, w1 = N0 + n0, N1 + n1

    LA0 = random.randint(0, 50)
    LA1 = random.randint(0, 50)
    U0 = random.randint(0, 50)
    U1 = random.randint(0, 50)
    S0, S1 = LA0 + U0, LA1 + U1

    # Saturate the three preserved weighted upper bounds independently.
    D = (n1 * LA0 + n0 * LA1) // L
    C0 = (N1 * LA0 + n0 * S1) // L
    C1 = (N0 * LA1 + n1 * S0) // L

    R = max(w0, w1)
    # Exact doubled version of CCP:
    # 2 L (D+C0+C1) <= R [2(LA0+LA1)+(S0+S1)].
    lhs = 2 * L * (D + C0 + C1)
    rhs = R * (2 * (LA0 + LA1) + S0 + S1)
    if lhs > rhs:
        failures += 1
        break

summary["combined_pair_random_trials"] = trials
summary["combined_pair_failures"] = failures
assert failures == 0

# ------------------------------------------------------------------
# 2. Safe-incidence table for the dense four-vertex kernels.
# ------------------------------------------------------------------
dense_cases = 0
dense_failures = 0
dense_by_edges = Counter()

for mask in range(64):
    E = edges_from_mask(mask)
    e = len(E)
    if e < 4:
        continue
    for r in (3, 4):
        for S in combinations(range(4), r):
            if not dominates(E, S):
                continue
            dense_cases += 1
            dense_by_edges[e] += 1
            if len(safe_coords(E, S)) < r - 2:
                dense_failures += 1

summary["dense_four_vertex_safe_cases"] = dense_cases
summary["dense_four_vertex_safe_failures"] = dense_failures
summary["dense_four_vertex_cases_by_edge_count"] = dict(dense_by_edges)
assert dense_failures == 0

# P4 is the one sparse kernel also handled by the safe-incidence lemma.
P4 = {(0, 1), (1, 2), (2, 3)}
p4_cases = 0
p4_failures = 0
for r in (3, 4):
    for S in combinations(range(4), r):
        if not dominates(P4, S):
            continue
        p4_cases += 1
        if len(safe_coords(P4, S)) < r - 2:
            p4_failures += 1
summary["p4_safe_cases"] = p4_cases
summary["p4_safe_failures"] = p4_failures
assert p4_failures == 0

# ------------------------------------------------------------------
# 3. Integer hole-compression inequality.
# ------------------------------------------------------------------
eta_checks = 0
for eta in range(100_001):
    R = floor((1 + sqrt(1 + 4 * eta)) / 2)
    assert 4 * R - eta <= 6
    eta_checks += 1
summary["eta_compression_checks"] = eta_checks
summary["eta_compression_failures"] = 0

# ------------------------------------------------------------------
# 4. z=4 internally-active edge envelope.
# ------------------------------------------------------------------
active_checks = 0
for d in range(2, 250):
    for w in range(d + 1, 350):
        n = d + w + 4
        if n < 17:
            continue
        # z=4, t=2, eta=0 is the weakest instance of FH5.
        ub = w * (n - w) + 6 - 2 * (w - 1) + 1
        assert ub <= M(n)
        active_checks += 1
summary["z4_active_envelope_checks"] = active_checks
summary["z4_active_envelope_failures"] = 0

# ------------------------------------------------------------------
# 5. Independent-W kernel edge envelopes.
# ------------------------------------------------------------------
# Uniform upper bounds proved in the note for the individual kernels.
bounds = [
    ("one_edge", lambda d, w: d * w + 2 * w + d + 1),
    ("p3_isolated", lambda d, w: d * w + 2 * w + 4),
    ("twoK2", lambda d, w: d * w + 2 * w + 6),
    ("P4_safe", lambda d, w: d * w + 2 * w + 9),
    ("K3_isolated", lambda d, w: d * w + 2 * w + 4),
    ("star", lambda d, w: d * w + w + d + 4),
    ("dense_safe", lambda d, w: d * w + 2 * w + 12),
]

kernel_checks = 0
for name, fn in bounds:
    for d in range(2, 300):
        for w in range(d + 1, 400):
            n = d + w + 4
            if n < 23:
                continue
            assert fn(d, w) <= M(n), (name, d, w, n, fn(d, w), M(n))
            kernel_checks += 1

summary["z4_kernel_n23_checks"] = kernel_checks
summary["z4_kernel_n23_failures"] = 0

summary["total_checks"] = (
    summary["combined_pair_random_trials"]
    + summary["dense_four_vertex_safe_cases"]
    + summary["p4_safe_cases"]
    + summary["eta_compression_checks"]
    + summary["z4_active_envelope_checks"]
    + summary["z4_kernel_n23_checks"]
)
summary["failures"] = 0

print(json.dumps(summary, indent=2, sort_keys=True))
