#!/usr/bin/env python3
"""Exact arithmetic sanity checks for N29_D16_STANDALONE_BRIDGE.md.

These checks do not prove the graph lemmas. They guard the displayed scalar
identities and corrected cumulative-tail normalization against transcription or
algebra errors.
"""
from fractions import Fraction
from math import comb

a=12;b=16

# Charging simplification.
for s in range(a):
    lhs=Fraction(s,1)-Fraction(s*(s-1),a-s)
    rhs=Fraction(s*(a+1-2*s),a-s)
    assert lhs==rhs

# Threshold extremal identity, over a range far beyond n=29's z<=16.
for z in range(50):
    for h in range(z+1):
        q=z-h
        target=h*z+comb(q,2)
        for j in range(z+1):
            raw=(z-j)*h+j*z-j*(j+1)//2
            gap=target-raw
            assert 2*gap==(q-j)*(q-j-1)
            assert gap>=0

# Correct cumulative-tail selected-slot identity:
# E[x 1{x>=h}] = (h-1)T_h + sum_{j=h}^U T_j, pointwise in integer x.
for U in range(20):
    for x in range(U+1):
        for h in range(1,U+1):
            rhs=((h-1) if x>=h else 0)+sum(1 for j in range(h,U+1) if x>=j)
            lhs=x if x>=h else 0
            assert lhs==rhs

# Isolated-C contradiction at the two n=29 scopes.
for t in (2,3):
    assert b>a-1-t

print('bridge exact sanity: PASS')
