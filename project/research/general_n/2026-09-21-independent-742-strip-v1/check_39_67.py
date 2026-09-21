#!/usr/bin/env python3
"""Exact rational checker for the first-obstruction/39-over-67 package."""

from fractions import Fraction as Q


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def poly_value(coefficients, x):
    result = Q(0)
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


P = [Q(0), Q(0), Q(2), Q(-4), Q(0), Q(2, 3), Q(0), Q(1, 10), Q(0), Q(3, 56)]
QPOLY = [Q(4), Q(-12), Q(0), Q(10, 3), Q(0), Q(7, 10), Q(0), Q(27, 56)]

l = Q(345053, 1_000_000)
u = Q(345054, 1_000_000)

require(poly_value(QPOLY, l) > 0, "Q(l) positive")
require(poly_value(QPOLY, u) < 0, "Q(u) negative")
qprime_upper = -Q(12) + Q(10, 2) + Q(7, 8) + Q(27, 64)
require(qprime_upper == -Q(365, 64) < 0, "Q decreasing")

mixed_upper = (
    2 * u**2
    - 4 * l**3
    + Q(2, 3) * u**5
    + Q(1, 10) * u**7
    + Q(3, 56) * u**9
)
require(mixed_upper < Q(121, 1569), "scalar rational margin")


def D(a):
    return (
        Q(121 * (a + 1) ** 2, 3136)
        - Q(1, 4)
        - Q(121 * a * a, 3138)
        - Q(a, 8)
    )


require(D(1949) == -Q(26669, 1230096) < 0, "minimality diagnostic")
require(D(1950) == Q(43251, 1640128) > 0, "large-a start")
require(D(1951) - D(1950) == Q(236671, 4920384) > 0, "first forward difference")
require((D(1952) - D(1951)) > (D(1951) - D(1950)), "forward differences increase")

require(Q(39, 67) < Q(7, 12), "strict threshold improvement")
require(Q(5 * 4681, 12) - 1 > 1949, "order cutoff")
require(Q(5 * 4680, 12) - 1 <= 1949, "cutoff minimal for this assembly")


def threshold_start(p, q):
    alpha = Q(p, q)
    eta = Q(2 * p - q, 2 * (q - p))

    def difference(a):
        return eta**2 * (a + 1) ** 2 - Q(1, 4) - Q(121 * a * a, 3138) - Q(a, 8)

    a = 2
    while difference(a) <= 0:
        a += 1
    require(difference(a + 1) - difference(a) > 0, (p, q, "forward difference"))
    require(alpha < Q(7, 12), (p, q, "improvement"))
    n = 6
    while Q(5 * n, 12) - 1 <= a - 1:
        n += 1
    return a, n


tradeoff_expected = {
    (116, 199): (53, 128),
    (88, 151): (62, 149),
    (46, 79): (204, 490),
    (85, 146): (346, 831),
    (39, 67): (1950, 4681),
}
for threshold, expected in tradeoff_expected.items():
    require(threshold_start(*threshold) == expected, (threshold, expected))

print("PASS")
print("Q(l) =", poly_value(QPOLY, l))
print("Q(u) =", poly_value(QPOLY, u))
print("121/1569 - mixed_upper =", Q(121, 1569) - mixed_upper)
print("D(1950) =", D(1950))
print("tradeoff ladder =", tradeoff_expected)
