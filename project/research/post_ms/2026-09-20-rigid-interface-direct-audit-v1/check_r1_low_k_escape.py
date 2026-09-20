#!/usr/bin/env python3
"""Diagnostic arithmetic replay for the residual-one k=2 escape ray.

This checks closed-form necessary-condition inequalities only. It does not enumerate
or certify graphs.
"""

from math import floor, sqrt


def check(t: int) -> None:
    assert t >= 4
    c = p = lam = t
    y = t - 1
    g0 = 1
    k = 2
    u = x = t + 1
    sf = 2

    A_lam = floor(lam * lam / 2) + lam + 4 + (lam % 2)
    C0 = (lam + 2) * (p + u) + p - A_lam
    assert C0 == floor((3 * t * t + 10 * t - 4) / 2)

    L0 = floor(
        x * g0
        - p / 2
        + max(k * (p + 1) - 2 * floor(sf / 2), k * (p + k - 2 * c))
    ) + 1
    T = k * (g0 + 2) + sf * (c - 2)
    assert L0 == floor(5 * t / 2) + 2
    assert T == 2 * t + 2
    assert L0 > T

    score_floor = (
        k * (p + k - 2)
        + (c - 1) * min(k, p - 1)
        + max(L0, T)
    )
    assert score_floor == floor(13 * t / 2)
    assert score_floor <= C0

    rooted_lhs = k * (x + y - 1) + T
    rooted_rhs = u * (p - lam) + 2 * (c - 1) * u - c * (c - 1) + C0
    assert rooted_lhs == 6 * t
    assert rooted_rhs - rooted_lhs == t * t - 5 * t - 2 + C0
    assert rooted_lhs <= rooted_rhs

    # Pair-local hostile test at the minimal natural pair assignment.
    gp = t - 1
    kp = 2
    SP = 2 * t
    D0 = 5 * p + 5 * u - 3 * lam - 2
    assert D0 == 7 * t + 3
    R = floor((D0 + sqrt(D0 * D0 + 12 * SP)) / 3)
    Ccap = R * (gp + 2 * SP / (lam + 1))
    crossing = 2 * x * y
    one_rhs = y * (p + x + kp)
    crowd = max(0, y * (3 * y - D0))
    assert R >= 4 * t + 2
    assert Ccap > (4 * t + 2) * (t + 2)
    assert Ccap >= crossing
    assert Ccap >= one_rhs
    assert crowd == 0


if __name__ == "__main__":
    for t in range(4, 10001):
        check(t)
    print("ok: k=2 residual-one ray replayed for 4 <= t <= 10000")
