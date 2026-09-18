#!/usr/bin/env python3
"""Audit support for ROOTED_TRIANGLE_RESIDUAL_AND_BETA_DEGREE_SUPPLY.md.

The hand proofs are primary. This script checks the algebraic identities and
synthetic local capacity inequalities independently over large finite samples.
"""

from math import ceil
import json
import random

summary = {}

# 1. Exact second-extremal residual threshold.
count = 0
for p in range(1, 26):
    for u in range(0, 21):
        for lam in range(-1, 2 * p + u):
            a = 2 * p + u - lam - 1
            if a < 0:
                continue
            b = 2 * p + u
            n = a + b + 1
            M = ((n - 1) ** 2) // 4 + 1
            D = b * (n - b) - M
            c_lam = ceil(lam * (lam + 2) / 2)
            D2 = ceil((4 * p + 2 * u - c_lam - 2) / 2)
            assert D == D2
            count += 1
summary["threshold_identity_exact"] = count

# 2. Residual/slack/rooted-triangle transfer identities.
random.seed(74211)
count = 0
for _ in range(200_000):
    p = random.randint(1, 30)
    u = random.randint(0, 30)
    lam = random.randint(-1, 2 * p + u - 1)
    a = 2 * p + u - lam - 1
    q = random.randint(0, max(0, u * (u - 1) // 2))
    s = random.randint(0, max(0, a * u))
    f = random.randint(0, max(0, a * (a - 1) // 2))

    Q = p * (p + u - 1) + q
    r = (p + u) * (a - p) + p - s - q
    delta = r - f
    E_U = u * (p + u - 1) - 2 * q - s
    L_A = a * (p + u) - s - 2 * f

    assert E_U + L_A == 2 * delta + lam * (p + u) - p
    assert r + Q == L_A + 2 * f
    assert delta + Q == L_A + f
    assert delta == E_U + Q - f - lam * (p + u) + p
    count += 1
summary["transfer_algebra_random"] = count

# 3. Local complement-code/non-neighbour degree-supply bookkeeping.
random.seed(74212)
count = 0
for _ in range(250_000):
    u = random.randint(1, 30)
    p = random.randint(1, 30)
    a = random.randint(1, 30)
    L = min(p, u)

    B = s = q = N1 = s0 = 0
    for _x in range(a):
        ell = random.randint(0, L)
        d = random.randint(ell, u)
        if ell >= 2:
            w = random.randint(0, u - d)
        elif ell == 1:
            w = random.randint(0, u - d + 1)
            N1 += 1
        else:
            w = random.randint(0, u)
            s0 += d
        B += ell
        s += d
        q += w

    assert q + s <= a * u + s0 + N1
    assert 2 * q + s <= 2 * a * u - B + s0 + 2 * N1
    count += 1
summary["local_degree_supply_random"] = count

# 4. Zero-load compression and coarse E_U floor.
random.seed(74213)
count = 0
for _ in range(250_000):
    u = random.randint(1, 30)
    p = random.randint(1, 30)
    a = random.randint(1, 30)
    L = min(p, u)

    ells = []
    ds = []
    ws = []
    for _x in range(a):
        ell = random.randint(0, L)
        d = random.randint(ell, u)
        if ell >= 2:
            w = random.randint(0, u - d)
        elif ell == 1:
            w = random.randint(0, u - d + 1)
        else:
            w = random.randint(0, u)
        ells.append(ell)
        ds.append(d)
        ws.append(w)

    B = sum(ells)
    s = sum(ds)
    q = sum(ws)
    N0 = sum(ell == 0 for ell in ells)
    N1 = sum(ell == 1 for ell in ells)
    s0 = sum(d for ell, d in zip(ells, ds) if ell == 0)

    if B:
        assert N0 <= a - ceil(B / L)
    else:
        assert N0 <= a

    E_U = u * (p + u - 1) - 2 * q - s
    exact_floor = u * (p + u - 1) - 2 * a * u + B - s0 - 2 * N1
    coarse_floor = (
        u * (p + u - 1)
        - 3 * a * u
        + B
        + u * ceil(B / L)
        - 2 * a
    )
    assert E_U >= exact_floor
    assert E_U >= coarse_floor
    count += 1
summary["zero_load_compression_random"] = count

summary["total_checks"] = sum(summary.values())
summary["failures"] = 0
print(json.dumps(summary, indent=2, sort_keys=True))
