#!/usr/bin/env python3
"""Arithmetic replay for the residual-one orientation-covering stress-ray consequence.

This is a diagnostic of the closed-form score margin only. It does not enumerate graphs.
"""


def margin(t: int) -> int:
    c = p = 2 * t
    k = t + 1
    base_w = k * (p + k - 2)
    escape = (c - 1) * min(k, p - 1)
    sf = k
    L0 = 8 * t * t - t + 2 - 2 * (sf // 2)
    C0 = 12 * t * t + 6 * t - 4
    return C0 - base_w - escape - L0


def closed_form(t: int) -> int:
    return -t * t + 4 * t - 4 + 2 * ((t + 1) // 2)


def main() -> None:
    for t in range(2, 10001):
        got = margin(t)
        want = closed_form(t)
        if got != want:
            raise AssertionError(("identity", t, got, want))
        if t >= 5 and got >= 0:
            raise AssertionError(("unexpected survivor", t, got))
    assert margin(4) == 0
    assert margin(5) == -3
    print("checked t=2..10000")
    print("M(4)=", margin(4), "M(5)=", margin(5))
    print("status: PASS")


if __name__ == "__main__":
    main()
