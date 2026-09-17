#!/usr/bin/env python3
"""Replay guard for QUADRATIC_ENDPOINT.md.

Checks the exact local support constants and the displayed global gaps for
all k=0..20. The Markdown hand proof is primary; this is not a graph search.
"""

A = 20
B = 23


def delta(k: int) -> int:
    if k <= 14:
        return 6
    if k == 15:
        return 5
    if k == 16:
        return 2
    return 0


def local_K(k: int, rho: int) -> int:
    p_cap = rho + B - A - 1  # rho+2
    if rho < 4:
        q_cap = 0
    elif rho == 4:
        q_cap = min(A - rho, A - k)
    else:
        q_cap = A - rho

    best = -10**9
    for q in range(q_cap + 1):
        if q == 0:
            p_max = p_cap
        else:
            p_max = min(p_cap, rho - 1)  # zero selected excess
        for p in range(p_max + 1):
            if p + q > B - 1:
                continue
            value = 10 * p + 15 * q - q * (p + q)
            best = max(best, value)
    return best


for k in range(21):
    d = delta(k)
    for rho in range(1, 21):
        expected = 10 * rho + 20 + (d if rho == 4 else 0)
        got = local_K(k, rho)
        assert got == expected, (k, rho, got, expected)

    Q = 80 + k
    r = 76 + k
    c4_cap = (33 + k) // 3
    endpoint_upper = 624 + 13 * k + min(18 * k, r)
    source_lower = 780 + 15 * k - d * c4_cap
    assert source_lower > endpoint_upper, (
        k,
        source_lower,
        endpoint_upper,
        c4_cap,
        d,
    )

print("PASS_QUADRATIC_ENDPOINT")
print("verified_k=0..20 verified_rho=1..20")
print("all zero-excess mixed 4/5 cases have strict source-vs-label gap")
