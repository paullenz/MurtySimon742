#!/usr/bin/env python3
"""Exact constants in the robust signature-stability plateau band."""

from fractions import Fraction as Q

d = Q(27, 64)
x = X = Q(1, 4)
c = Q(6771, 16000)
q = Q(19, 50)

linear = d * d * x * x / (c * q * X)
constant = d * x / (q * X)

assert linear == Q(759375, 2744512)
assert linear > Q(2766, 10000)
assert constant == Q(675, 608)
assert constant < Q(1111, 1000)

automatic_linear = d * d * x * x / (c * c * X)
automatic_constant = d * x / (c * X)
assert automatic_linear == Q(1265625, 5094049)
assert automatic_linear > Q(2484, 10000)
assert automatic_constant == Q(2250, 2257)
assert automatic_constant < 1

print("PASS")
print("linear coefficient =", linear, float(linear))
print("constant loss =", constant, float(constant))
print("automatic endpoint-cap coefficient =", automatic_linear, float(automatic_linear))
print("automatic endpoint-cap loss =", automatic_constant, float(automatic_constant))
