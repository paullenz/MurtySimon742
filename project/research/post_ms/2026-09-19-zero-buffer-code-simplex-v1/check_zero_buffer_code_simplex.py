#!/usr/bin/env python3
"""Diagnostic audit for ZERO_BUFFER_CODE_SIMPLEX_AND_SMALL_LAMBDA_CLOSURE.md.

Arithmetic only.  It does not establish the D2C criticality or code-simplex
premises used by the hand proof.
"""

def H(lam):
    return ((lam + 1) ** 2) // 4

def c0(p, k, rho, lam):
    u = k + rho
    return (lam + 3) * p + (lam + 2) * u - 2 * H(lam) - 4

def ly(p, rho, lam):
    return rho * (p + rho - lam - 1)

def core(p, k):
    return k * (p + k)

def qgate(p, k, rho, lam):
    return (
        (k + rho - lam - 3) * p
        + k * (k - lam - 2)
        + rho * (rho - 2 * lam - 3)
        + 2 * H(lam)
        + 4
    )

def check_algebra():
    for lam in range(0, 12):
        for p in range(1, 30):
            for k in range(1, 20):
                for rho in range(1, 35):
                    assert qgate(p, k, rho, lam) == core(p, k) + ly(p, rho, lam) - c0(p, k, rho, lam)

def structural_scan(limit=80):
    out = {}
    for lam in (1, 2, 3):
        surv = []
        for p in range(4, limit + 1):
            for k in range(1, limit + 1):
                for rho in range(p + 2, limit + 1):
                    if qgate(p, k, rho, lam) <= 0:
                        surv.append((p, rho, k))
        out[lam] = surv
    assert out[1] == []
    assert out[2] == []
    assert out[3] == [(4, 6, 1), (4, 6, 2), (4, 6, 3)]
    return out

def lambda3_followup():
    p = 4
    rho = 6
    lam = 3
    assert core(p, 3) + ly(p, rho, lam) + 3 == 60
    assert c0(p, 3, rho, lam) == 57

    k = 2
    u = k + rho
    uo = rho - 1
    x = p + k
    dphys = u * uo + k * (x - 1) + max(x, uo)
    emin = core(p, k) + k
    dmax = 2 * p + u - H(lam) - 2
    upper_2q_plus_e = 2 * (24 + dmax) - emin
    assert dphys == 56
    assert emin == 14
    assert dmax == 10
    assert upper_2q_plus_e == 54
    assert upper_2q_plus_e < dphys

    tuples = []
    k = 1
    for delta in range(7, 10):
        S = 2 * delta + 29
        for EU in range(0, S + 1):
            LA = S - EU
            LX = LA - 36
            q = 19 + delta - EU
            if EU < 6 or LA < 36 or LX < 0 or q > 19 or q < 0:
                continue
            if 2 * q + EU < 44:
                continue
            tuples.append((delta, EU, q, LX))
    expected = [
        (7, 7, 19, 0),
        (8, 8, 19, 1),
        (8, 9, 18, 0),
        (9, 9, 19, 2),
        (9, 10, 18, 1),
        (9, 11, 17, 0),
    ]
    assert tuples == expected
    return tuples

if __name__ == "__main__":
    check_algebra()
    print({"small_lambda_survivors": structural_scan(), "lambda3_last_tuples": lambda3_followup(), "failures": 0})
