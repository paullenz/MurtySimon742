#!/usr/bin/env python3
"""Arithmetic audit for MINIMAL_RESERVOIR_PAIR_HALL_ALLOCATION.md.

Diagnostic only. This is not a D2C graph enumerator and does not establish
realizability of any abstract parameter state.
"""
import math
from collections import Counter


def phi(g):
    return g * (g - 1) if g >= 3 else 0


def C0(p, u, lam):
    H = ((lam + 1) ** 2) // 4
    return (lam + 3) * p + (lam + 2) * u - 2 * H - 4


def predecessor_floor(p, x, y, g):
    k = x - g
    t = p - g
    return k * (p + k - 1) + t + max(phi(g), y * (t + 1))


def repaired_floor(p, u, lam, x, y, g):
    k = x - g
    t = p - g
    Ecore = k * (p + k)
    Eout = t + g * (t - k + 1) if k <= t else 0
    LY = y * (p + 2)
    return Ecore + t + Eout + max(phi(g), LY)


def preceding_mg1_score(p, u, lam, x, y, g):
    """Exact score relaxation used by the immediately preceding checker."""
    k = x - g
    t = p - g
    a = x + y
    T0 = a - p
    uo = u - k - 1
    N = uo - 1
    if N < g:
        return None
    s1 = max(0, t - k + 1)
    Ebase = k * (p + k) + 2 * t + k + g * s1
    LY = y * (p + 2)
    Lcore = max(0, k * (k - T0))
    best = None
    for A in range(g + 1):
        for M in range(N + 1):
            dstar = N - M
            ZX = k * (x - 1) + x + A + k * dstar
            eXmax = g * (g - 1) // 2 + k * A
            LX = max(0, x * (x - T0) + ZX - 2 * eXmax)
            S = Ebase + A + M + max(phi(g), LY, Lcore, LX)
            best = S if best is None else min(best, S)
    return best


def hmin_closed(Q, k, g, N):
    """Closed form for min A+M+[Q-(2k-1)A-kM]_+."""
    if Q <= 0:
        return 0
    cA = 2 * k - 1
    cM = k
    CA = cA * g
    CT = CA + cM * N
    if Q <= CA:
        return (Q + cA - 1) // cA
    if Q <= CT:
        return g + (Q - CA + cM - 1) // cM
    return g + N + Q - CT


def new_floor(p, u, lam, x, y, g):
    k = x - g
    t = p - g
    a = x + y
    T0 = a - p
    N = u - k - 2
    s1 = max(0, t - k + 1)
    Ebase = k * (p + k) + 2 * t + k + g * s1
    LY = y * (p + 2)
    BX = x * (x - T0) + k * (x - 1) + x - g * (g - 1)
    Q = BX + k * N
    return Ebase + LY + hmin_closed(Q, k, g, N), Q, N


def rcode(D, s):
    return max(0, math.floor((D + math.sqrt(D * D + 12 * s)) / 3))


def pair_capacity(p, u, lam, g, s):
    D = 5 * p + 5 * u - 3 * lam - 2
    L = lam + 1
    return rcode(D, s) * (g + 2 * s / L)


def sigma_pair(p, u, lam, x, y, g, P0, cap):
    """Minimum local pair score meeting exact crossing Ccap, if <=cap."""
    if P0 > cap:
        return None
    target = 2 * x * y
    if pair_capacity(p, u, lam, g, P0) + 1e-12 >= target:
        return P0
    if pair_capacity(p, u, lam, g, cap) + 1e-12 < target:
        return None
    lo, hi = P0, cap
    while lo < hi:
        mid = (lo + hi) // 2
        if pair_capacity(p, u, lam, g, mid) + 1e-12 >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def verify_hmin():
    checks = 0
    for k in range(1, 10):
        for g in range(0, 10):
            for N in range(0, 10):
                for Q in range(-5, 100):
                    brute = min(
                        A + M + max(0, Q - (2 * k - 1) * A - k * M)
                        for A in range(g + 1)
                        for M in range(N + 1)
                    )
                    closed = hmin_closed(Q, k, g, N)
                    assert brute == closed, (k, g, N, Q, brute, closed)
                    checks += 1
    return checks


def main():
    st = Counter()
    h_checks = verify_hmin()

    for p in range(3, 19):
        for u in range(1, 19):
            b = 2 * p + u
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

                        st["preceding_mg1_survivors"] += 1
                        if t == 1:
                            st["t1_preceding_mg1_survivors"] += 1

                        Snew, Q, N = new_floor(p, u, lam, x, y, g)

                        s1 = max(0, t - k + 1)
                        Kp = k * (p + k) + t
                        LY = y * (p + 2)
                        O0 = t + k + g * s1
                        P0 = Kp + LY

                        # CROWD is analytically dominated by LY; replay it anyway.
                        Dcode = 5 * p + 5 * u - 3 * lam - 2
                        crowd = max(0, y * (3 * y - Dcode))
                        assert P0 >= crowd

                        sig = sigma_pair(p, u, lam, x, y, g, P0, cap)
                        if sig is None:
                            st["pair_capacity_no_budget"] += 1
                        else:
                            if sig > P0:
                                st["sigma_strictly_above_P0"] += 1
                            # Exact crossing capacity plus LY implies ONE-P.
                            assert (
                                pair_capacity(p, u, lam, g, sig) + LY + 1e-9
                                >= y * (p + 2 * x - g)
                            )

                        if Snew > cap:
                            st["additive_hall_rejected"] += 1
                            if t == 1:
                                st["t1_additive_hall_rejected"] += 1
                            continue

                        st["additive_hall_survivors"] += 1
                        if t == 1:
                            st["t1_additive_hall_survivors"] += 1

                        # Exact pair-local elimination: H_min <= C0-O0-sigma_P.
                        if sig is None or hmin_closed(Q, k, g, N) > cap - O0 - sig:
                            st["pair_gate_extra_rejected"] += 1
                        else:
                            st["pair_gate_survivors"] += 1

    expected = {
        "preceding_mg1_survivors": 123585,
        "additive_hall_rejected": 13198,
        "additive_hall_survivors": 110387,
        "pair_gate_survivors": 110387,
        "t1_preceding_mg1_survivors": 5520,
        "t1_additive_hall_rejected": 116,
        "t1_additive_hall_survivors": 5404,
    }
    mismatches = {k: (v, st[k]) for k, v in expected.items() if st[k] != v}

    print({
        "hmin_bruteforce_checks": h_checks,
        "counts": dict(st),
        "expected_mismatches": mismatches,
        "failures": len(mismatches),
        "trust": "abstract integer/arithmetic diagnostic only; no graph-realizability claim",
    })


if __name__ == "__main__":
    main()
