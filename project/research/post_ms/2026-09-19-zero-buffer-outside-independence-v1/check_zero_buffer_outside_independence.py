#!/usr/bin/env python3
"""Arithmetic audit for ZERO_BUFFER_OUTSIDE_INDEPENDENCE_AND_LAMBDA5_CLOSURE.md.

This checks only integer algebra/classification. It does not prove the raw
D2C criticality theorem U_o independent or graph realizability.
"""

def H(lam):
    return ((lam + 1) ** 2) // 4

def c0(p, k, rho, lam):
    return (lam + 3) * p + (lam + 2) * (k + rho) - 2 * H(lam) - 4

def floors(p, k, rho, lam):
    assert p >= 4 and rho >= p + 2 and k >= 1
    uo = rho - 1
    x = p + k
    y = p + rho - lam - 1
    R = rho - p - 2
    J = max(x, uo)
    EU = k * (p + k - 1) + uo * (rho - k - 2) + J + 2 * k
    eX_cap = k * R
    LX_raw = x * (lam + 1 - rho) + k * (x - 1) + J - 2 * eX_cap
    LX = max(0, LX_raw)
    LY = rho * y
    return LY + EU + LX, LY, EU, LX, eX_cap

def scan(lam, limit=80):
    out = []
    for p in range(4, limit + 1):
        for k in range(1, limit + 1):
            for rho in range(p + 2, limit + 1):
                if p + rho - lam - 1 <= 0:
                    continue
                lo, LY, EU, LX, ecap = floors(p, k, rho, lam)
                hi = c0(p, k, rho, lam)
                if lo <= hi:
                    out.append((p, rho, k, lo, hi, LY, EU, LX, ecap))
    return out

def main():
    assert scan(3) == []
    assert scan(4) == []

    s5 = scan(5)
    assert [(p, rho, k) for p, rho, k, *_ in s5] == [(4, 6, 1)]
    assert s5[0][3:] == (59, 59, 24, 26, 9, 0)

    s6 = scan(6)
    assert sorted((p, rho, k) for p, rho, k, *_ in s6) == [
        (4, 6, 1),
        (4, 6, 2),
        (4, 7, 1),
        (4, 7, 2),
    ]

    p, rho, k = 4, 6, 1
    uo = rho - 1
    Hcore = 1
    J = 5
    q = (k + 1) * uo - Hcore
    EU = k * (p + k - 1) + uo * (rho - k - 2) + J + 2 * Hcore
    assert (q, EU) == (9, 26)

    print({
        "lambda3_survivors": 0,
        "lambda4_survivors": 0,
        "lambda5_scalar_survivors_before_raw_edge_check": [(4, 6, 1)],
        "lambda6_frontier": [(4, 6, 1), (4, 6, 2), (4, 7, 1), (4, 7, 2)],
        "failures": 0,
    })

if __name__ == "__main__":
    main()
