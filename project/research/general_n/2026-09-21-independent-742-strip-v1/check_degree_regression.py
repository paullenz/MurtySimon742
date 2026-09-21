#!/usr/bin/env python3
"""Finite consistency regression for every row of the threshold ladder.

This is not proof by exhaustion; the proof is the convex degree assembly.
"""

from fractions import Fraction as Q


def ceil_fraction(frac):
    return -((-frac.numerator) // frac.denominator)


rows = [
    (Q(250, 429), 6),
    (Q(116, 199), 128),
    (Q(88, 151), 149),
    (Q(46, 79), 490),
    (Q(85, 146), 831),
    (Q(39, 67), 4681),
]

checked = 0
finite_caps = {4:1,6:2,9:5,11:8,14:13,19:26,24:43,29:64}
for alpha, start_n in rows:
    for n in range(start_n, 10_001):
        for b in range(ceil_fraction(alpha * n), ceil_fraction(Q(7, 12) * n)):
            a = n - 1 - b
            required = (b - a - 1) ** 2 // 4
            scalar_upper = Q(121 * a * a, 3138) + Q(a, 8)
            if a in finite_caps:
                assert finite_caps[a] < 2 * required, (alpha,n,a,b,required)
            else:
                assert required >= scalar_upper, (alpha, n, a, b, required, scalar_upper)
            checked += 1

print(f"PASS: {checked} below-7/12 degree pairs through n=10000")
