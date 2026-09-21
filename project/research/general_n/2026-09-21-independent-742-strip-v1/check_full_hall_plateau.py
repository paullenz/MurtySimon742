#!/usr/bin/env python3
"""Exact rational inequalities used by FULL_HALL_PLATEAU_OBSTRUCTION.md."""

from fractions import Fraction as Q
from math import comb


def require(condition, label):
    if not condition:
        raise AssertionError(label)


# Elementary square-root brackets.
require(Q(2645, 1000) ** 2 < 7, "lower sqrt7 bracket")
require(Q(2646, 1000) ** 2 > 7, "upper sqrt7 bracket")

# arcsin(z) = z sum c_k z^(2k), z^2=1/8.  Keep k=0..3,
# bound all later c_k by 1, and use z<177/500.
series = Q(0)
for k in range(4):
    coefficient = Q(comb(2 * k, k), 4**k * (2 * k + 1))
    series += coefficient * Q(1, 8) ** k
tail = Q(1, 8) ** 4 / Q(7, 8)
arcsin_upper = Q(177, 500) * (series + tail)
require(arcsin_upper < Q(181, 500), "arcsin rational upper")

f_lower = Q(1, 4) - Q(1323, 500) / 32 - Q(181, 500) / 4
require(f_lower == Q(1229, 16000), "f lower identity")

beta = Q(139, 100)
turan_coefficient = (beta - 1) ** 2 / 4
require(f_lower / 2 > turan_coefficient, "plateau above Turan requirement")

# Coarse feasibility margins from gamma in (2645/4000,2646/4000).
gamma_lo = Q(2645, 4000)
gamma_hi = Q(2646, 4000)
ell_lo = beta - gamma_hi
q_hi = Q(1, 4) / gamma_lo
p_hi = Q(1, 4) / ell_lo
C_lo = Q(1, 2) - Q(5, 64)  # inherited f<5/64

require(q_hi < C_lo, "selected endpoint margin")
require(p_hi < beta - 1, "incoming low-source cap")
require(q_hi < ell_lo, "high-to-low row capacity")
require(p_hi < gamma_lo, "high-to-low column capacity")
require(Q(1, 4) + q_hi < 1, "selected/residual row disjointness")

# Disjoint high selected/residual layers and positive low residual remainder.
high_column_used_upper = Q(1, 4) + gamma_hi * Q(1, 4)
phi_lower = Q(1, 4) - Q(5, 64)
low_residual_remainder = phi_lower - gamma_hi * Q(1, 4)
require(high_column_used_upper < gamma_lo, "two high-layer column capacity")
require(low_residual_remainder > Q(6, 1000), "positive low residual remainder")

print("PASS")
print("arcsin margin =", Q(181, 500) - arcsin_upper)
print("f lower =", f_lower)
print("surplus coefficient margin =", f_lower / 2 - turan_coefficient)
print("q upper, p upper, C lower =", q_hi, p_hi, C_lo)
print("low residual remainder lower =", low_residual_remainder)
