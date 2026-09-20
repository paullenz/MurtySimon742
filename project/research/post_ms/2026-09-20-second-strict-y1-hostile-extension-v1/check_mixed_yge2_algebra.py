#!/usr/bin/env python3
"""Independent diagnostic replay for the algebraic endgame in SECOND_STRICT_MIXED_YGE2_CLOSURE.md.

This is an audit aid, not a proof substitute.  It checks the exact COMB identity
and F+2P positivity over a broad integer box using only the definitions in the
proof note.
"""

from math import floor


def row(p: int, x: int, omega: int, y: int):
    u = x + omega
    a = x + y
    b = 2 * p + u
    n = 1 + a + b
    lam = 2 * p + omega - 1 - y
    if lam < 0:
        return None

    M = ((n - 1) ** 2) // 4 + 1
    D_M = b * (n - b) - M
    C0 = 2 * (D_M - 1) + lam * (p + u) - p

    P = (omega - 1) * max(0, p - x + omega + 1)
    S_min = (
        (x - 1) * (p + x - 2)
        + (omega - 1)
        + (p + 1)
        + (p + omega - 1)
        + y * (p + omega)
        + x * (p + x - y)
        + P
    )
    A = C0 - S_min

    R_max = (
        (p - lam) * (p + u)
        + (x - 1) * omega
        + C0
        - x * (p + x - y)
        - y * (p + omega)
    )
    B = R_max - (x + y)

    eps = (n - 1) & 1
    F = (
        8 * p * p
        + 6 * p * omega
        - 8 * p * y
        - 26 * p
        + 3 * omega * omega
        - 10 * omega * x
        + 2 * omega * y
        - 6 * omega
        + 12 * x * x
        - 8 * x * y
        - 16 * x
        + 5 * y * y
        + 8 * y
        + 42
        - 5 * eps
    )
    return A, B, F, P


def main():
    checked = 0
    min_fp = None
    min_row = None
    for p in range(2, 21):
        for omega in range(2, 21):
            for x in range(3, 31):
                for y in range(2, 2 * p + omega):
                    out = row(p, x, omega, y)
                    if out is None:
                        continue
                    A, B, F, P = out
                    # 4B+A = -(F+2P)/2.
                    assert 2 * (4 * B + A) + F + 2 * P == 0, (
                        p,
                        x,
                        omega,
                        y,
                        A,
                        B,
                        F,
                        P,
                    )
                    fp = F + 2 * P
                    assert fp > 0, (p, x, omega, y, F, P)
                    if min_fp is None or fp < min_fp:
                        min_fp = fp
                        min_row = (p, x, omega, y, F, P)
                    checked += 1

    print(f"checked_rows={checked}")
    print(f"minimum_F_plus_2P={min_fp}")
    print(f"minimum_row={min_row}")


if __name__ == "__main__":
    main()
