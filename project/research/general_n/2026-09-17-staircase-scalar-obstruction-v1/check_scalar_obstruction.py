#!/usr/bin/env python3
"""Exact audit for the 2026-09-17 scalar-staircase obstruction witness.

This checks an abstract parameter profile only. It does not construct a diameter-two
edge-critical graph and is not a counterexample to Murty-Simon.
"""
from math import comb

A = 20
B = 23
T_SURPLUS = 2
DEMANDS = [4] * A
RHOS = [5] * 5 + [4] * 11 + [1] * 7
LABEL_R = [4] * 16 + [3] * 4
LABEL_D = [r + 4 for r in LABEL_R]


def eg_graphical(seq):
    d = sorted(seq, reverse=True)
    if sum(d) % 2:
        return False
    n = len(d)
    for k in range(1, n + 1):
        if sum(d[:k]) > k * (k - 1) + sum(min(x, k) for x in d[k:]):
            return False
    return True


def gale_ryser(rows, cols):
    r = sorted(rows, reverse=True)
    c = sorted(cols, reverse=True)
    if sum(r) != sum(c):
        return False
    if any(x < 0 or x > len(c) for x in r):
        return False
    if any(x < 0 or x > len(r) for x in c):
        return False
    for k in range(1, len(r) + 1):
        if sum(r[:k]) > sum(min(k, x) for x in c):
            return False
    return True


def tail_count(seq, d):
    return sum(x >= d for x in seq)


def heavy_local_cost(h, T, H, p):
    ramp = max(0, T - max(h, H + p))
    return h * H + h * p + H * ramp - h * H * (H > h)


def restricted_C(h, T, P, c):
    return max(
        heavy_local_cost(h, T, H, p)
        for H in range(c + 1)
        for p in range(P + 1)
    )


def check():
    S = sum(DEMANDS)
    r = sum(RHOS)
    assert A + B + 1 == 44
    assert B * (A + 1) + T_SURPLUS == 485
    assert (A + B + 1) ** 2 // 4 == 484
    assert S == 80 and r == 76
    assert r + 2 * T_SURPLUS == S

    # Exact label-side ledger compatibility.
    assert sum(LABEL_R) == r
    assert sum(LABEL_D) == 2 * (r + T_SURPLUS)
    assert all(max(0, d - R) == 4 for d, R in zip(LABEL_D, LABEL_R))
    assert eg_graphical(LABEL_D)
    assert gale_ryser(RHOS, LABEL_R)

    # Tail identities and full staircase-capacity inequalities.
    K = {d: tail_count(DEMANDS, d) for d in range(1, 7)}
    N = {d: tail_count(RHOS, d) for d in range(1, 7)}
    assert [N[d] for d in range(1, 7)] == [23, 16, 16, 16, 5, 0]
    assert [K[d] for d in range(1, 7)] == [20, 20, 20, 20, 0, 0]
    assert sum(K[d] - N[d] for d in range(1, 7)) == 2 * T_SURPLUS
    sc_slacks = {}
    for d in range(1, 6):
        W = sum(s for s in DEMANDS if s >= d)
        if W == 0:
            continue
        assert N[d] >= d
        rhs = d * N[d] + comb(N[d] - d, 2)
        assert W <= rhs
        sc_slacks[d] = rhs - W

    # Canonical charging inequalities.
    charge_101 = sum(s * (s - 1) / (A - s) for s in DEMANDS)
    charge_102 = sum(s * (A + 1 - 2 * s) / (A - s) for s in DEMANDS)
    assert r - B >= charge_101
    assert charge_102 >= B + 2 * T_SURPLUS

    # Residual h-index is 5; the h=5 exact square face is absent.
    assert N[5] == 5 and N[6] == 0 and K[5] == 0
    assert B + 2 * T_SURPLUS <= (A - 5) * 4  # h-index saturation, k=u=0.

    # Exact restricted heavy-load family, every integer cutoff T>=h.
    # Finite ranges are checked exactly. For larger T, choosing H=c,p=0
    # on each rho=4 or 5 source gives a linear lower bound.
    finite_caps = {1: 17, 2: 18, 3: 20, 4: 22}
    heavy_min_slack = {}
    for h in range(1, 5):
        best = None
        stop = finite_caps[h]
        for T in range(h, stop):
            lhs = h * sum(max(T, s) for s in DEMANDS if s >= h)
            rhs = h * r
            for rho in RHOS:
                if rho < h:
                    continue
                P = rho + B - A - 1  # rho+2
                count = sum(h <= s <= rho for s in DEMANDS)
                c = min(A - rho, count)
                rhs += restricted_C(h, T, P, c)
            slack = rhs - lhs
            assert slack >= 0
            if best is None or slack < best[0]:
                best = (slack, T)
        heavy_min_slack[h] = best

        # For T>=stop, T>=16 and c>h on the 16 high sources.
        # Sum c = 5*15+11*16 = 251; sum c^2 = 3941.
        T0 = stop
        tail_slack = (251 - 20 * h) * T0 + 76 * h - 3941
        assert tail_slack >= 0
        assert 251 - 20 * h > 0

    return {
        "status": "PASS",
        "scope": "abstract scalar profile only; not graph realizability",
        "parameters": {
            "a": A,
            "b": B,
            "n": A + B + 1,
            "t": T_SURPLUS,
            "m": B * (A + 1) + T_SURPLUS,
        },
        "demand_profile": {"4": 20},
        "residual_profile": {"5": 5, "4": 11, "1": 7},
        "staircase_slacks": sc_slacks,
        "heavy_min_finite_slack": heavy_min_slack,
        "graphical_degree_checks": {"F": True, "residual_bipartite": True},
    }


if __name__ == "__main__":
    import json

    print(json.dumps(check(), indent=2, sort_keys=True))
