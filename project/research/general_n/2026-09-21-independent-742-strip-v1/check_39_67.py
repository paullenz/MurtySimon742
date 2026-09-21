#!/usr/bin/env python3
"""Exact rational checker for the first-obstruction/39-over-67 package."""

from fractions import Fraction as Q


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def ceil_div(n, d):
    return -((-n) // d)


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

# All-order 250/429 assembly boundary and inherited finite certificates.
eta_250 = Q(71, 358)
def D250(a):
    return eta_250**2 * (a + 1) ** 2 - Q(1, 4) - Q(121*a*a,3138) - Q(a,8)
require(D250(64) == -Q(534086,50272329), "D250(64)")
require(D250(65) == Q(17187305,402178632) > 0, "D250(65)")
require(D250(66)-D250(65) == Q(22081621,402178632) > 0, "D250 step")
finite_250 = {4:(7,1,1),6:(10,2,2),9:(14,4,5),11:(17,6,8),
              14:(21,9,13),19:(28,16,26),24:(35,25,43),29:(42,36,64)}
exceptions=[]
for a in range(2,65):
    b=ceil_div(250*(a+1),179)
    T=(b-a-1)**2//4
    if Q(T) < Q(121*a*a,3138)+Q(a,8):
        exceptions.append(a)
        require((b,T)==finite_250[a][:2], (a,b,T))
        require(finite_250[a][2] < 2*T, (a,"threshold certificate"))
require(exceptions==list(finite_250), ("250 exceptions",exceptions))
require(Q(250,429)<Q(7,12), "250/429 improvement")


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
    return a, n, difference(a - 1), difference(a), difference(a + 1) - difference(a)


tradeoff_expected = {
    (116, 199): (53, 128, -Q(103645,21617682), Q(4326773,86470728), Q(4907365,86470728)),
    (88, 151): (62, 149, -Q(434953,16606296), Q(169,6276), Q(908963,16606296)),
    (46, 79): (204, 490, -Q(73993,1518792), Q(599,1139094), Q(25171,506264)),
    (85, 146): (346, 831, -Q(126365,15568664), Q(476429,11676498), Q(765953,15568664)),
    (39, 67): (1950, 4681, -Q(26669,1230096), Q(43251,1640128), Q(236671,4920384)),
}
for threshold, expected in tradeoff_expected.items():
    require(threshold_start(*threshold) == expected, (threshold, expected))

print("PASS")
print("Q(l) =", poly_value(QPOLY, l))
print("Q(u) =", poly_value(QPOLY, u))
print("121/1569 - mixed_upper =", Q(121, 1569) - mixed_upper)
print("D(1950) =", D(1950))
print("tradeoff ladder =", tradeoff_expected)
print("all-order threshold = 250/429; exceptions =", exceptions)
