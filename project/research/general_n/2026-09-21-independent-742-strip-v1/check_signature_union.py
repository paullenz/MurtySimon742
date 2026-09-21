#!/usr/bin/env python3
"""Exact rational constants for the signature-union plateau corollary."""

from fractions import Fraction as Q

C_lower = Q(27, 64)
gamma_lower = Q(529, 800)
codegree_lower = C_lower * gamma_lower

assert codegree_lower == Q(14283, 51200)
assert codegree_lower > Q(2789, 10000)
assert gamma_lower > Q(66, 100)

print("PASS")
print("C*gamma lower =", codegree_lower, float(codegree_lower))

