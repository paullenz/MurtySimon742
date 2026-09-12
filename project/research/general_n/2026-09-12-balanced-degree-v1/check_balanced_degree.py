#!/usr/bin/env python3
"""Exact integer/rational regression for BALANCED_DEGREE_THEOREM.md.

This script is not a proof premise. It checks the endpoint formulas in the
symbolic odd-order witness-deficit argument for a wide range of k.
"""
from fractions import Fraction


def F(k, T, h):
    o = T - 2*h
    assert o >= 0
    return h*(h-1)//2 + h*(2*k+1-h) + o*(o-1)


def main():
    for k in range(3, 10000):
        M = k*(k+1)

        # equality level T=k+1
        T = k+1
        H = T//2
        vals = [F(k,T,h) for h in range(H+1)]
        assert max(vals) == M
        assert vals[0] == M
        assert all(v < M for v in vals[1:])
        if k % 2:
            expected = Fraction(M) - Fraction((k-1)*(k+1), 8)
        else:
            expected = Fraction(M) - Fraction(k*(k+6), 8)
        assert F(k,T,H) == expected

        # first above-Turan deficit level T=k-1
        T = k-1
        H = T//2
        vals = [F(k,T,h) for h in range(H+1)]
        assert max(vals) < M
        if k % 2:
            expected = Fraction((k-1)*(7*k+3), 8)
        else:
            expected = Fraction((k-2)*(7*k+4), 8)
        assert F(k,T,H) == expected

    print("PASS: balanced-degree endpoint algebra checked exactly for 3<=k<10000")


if __name__ == "__main__":
    main()
