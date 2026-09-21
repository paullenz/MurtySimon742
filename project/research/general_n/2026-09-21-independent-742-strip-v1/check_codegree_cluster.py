#!/usr/bin/env python3
"""Exact asymptotic constants for the positive-density codegree cluster."""

from fractions import Fraction as Q

kappa = Q(1265625, 5094049)
loss = Q(2250, 2257)
c = Q(6771, 16000)
theta = Q(1, 5)
x = Q(1, 4)
beta = Q(139, 100)

fraction = (kappa - theta) / (c - theta)
pair_occurrence_coefficient = x * x / (2 * beta)
high_occurrence_coefficient = fraction * pair_occurrence_coefficient
distinct_pair_coefficient = high_occurrence_coefficient / beta

assert fraction == Q(3949043200, 18190848979)
assert fraction > Q(2170, 10000)
assert pair_occurrence_coefficient == Q(25, 1112)
assert distinct_pair_coefficient == Q(1234076000000, 351465393123259)
assert distinct_pair_coefficient > Q(351, 100000)
assert (kappa - theta) * 21 > loss

print("PASS")
print("high occurrence fraction =", fraction, float(fraction))
print("pair occurrence coefficient =", pair_occurrence_coefficient)
print("distinct high pair coefficient =", distinct_pair_coefficient, float(distinct_pair_coefficient))

