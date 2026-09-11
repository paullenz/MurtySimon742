#!/usr/bin/env python3
"""Exact regression for the 13-label threshold-tail hand lemma.
Not a proof premise: it rechecks the finite clipping and terminal arithmetic.
"""
from itertools import combinations_with_replacement

A = 13

def C(h, z):
    return (z * (z - 1) + h * (h + 1)) // 2

def gamma(h, W):
    if W <= 0:
        return 0
    z = h
    while W > C(h, z):
        z += 1
    return z

def D(s):
    ans = 0
    for h in range(2, A):
        vals = [x for x in s if x >= h]
        if vals:
            ans += len(vals) - gamma(h, sum(vals))
    return ans

def Q(s):
    return sum(1 for x in s if x >= 1) + D(s)

def clip_one(s, M):
    return tuple(M - 1 if x == M else x for x in s)

# High levels h>=8 must have nonpositive deficit for every possible tail size.
for h in range(8, A):
    for N in range(1, A + 1):
        W = h * N
        assert N - gamma(h, W) <= 0, (h, N)

# Stage-by-stage clipping 7->6->5->4->3 never decreases D.
# It is enough to inspect vectors whose current maximum is M.
checks = 0
for M in (7, 6, 5, 4):
    for s in combinations_with_replacement(range(M + 1), A):
        if s[-1] != M:
            continue
        s2 = clip_one(s, M)
        assert D(s2) >= D(s), (M, s, D(s), D(s2))
        checks += 1

# Terminal max-three domain: D<=8, with equality only at 3^13.
terminal_eq = []
for y in range(A + 1):
    for x in range(y, A + 1):
        s = (0,) * (A - x) + (2,) * (x - y) + (3,) * y
        # Ones do not affect D, so this canonical representative has the same D.
        d = D(s)
        assert d <= 8, (x, y, d)
        if d == 8:
            terminal_eq.append((x, y))
assert terminal_eq == [(13, 13)], terminal_eq

# If all entries are positive, Q=21 can only arise from 3^13.
# Any vector with p<13 has Q<=20. If p=13 and D=8, clipping ends at 3^13;
# the final 4->3 step is strict whenever a 4 remains.
for k in range(1, A + 1):
    s = (3,) * (A - k) + (4,) * k
    assert D(s) <= 7, (k, D(s))

all3 = (3,) * A
assert D(all3) == 8
assert Q(all3) == 21

# N31 equality arithmetic for Delta=17, m=240.
b, t = 17, 2
assert b + 2 * t == 21
S = 39
z2 = gamma(2, 39)
z3 = gamma(3, 39)
assert (z2, z3) == (9, 9)
r = b + z2 + z3
assert r == 35 and S == r + 2 * t
# h=2 capacity is exact: C_2(9)=39.
assert C(2, 9) == 39
# Equality in the capacity algebra has j=6 or 7 and sends 33 or 35 arcs from J.
for j, expected in ((6, 33), (7, 35)):
    rhs = (9 - j) * 2 + j * 9 - j * (j + 1) // 2
    assert rhs == 39
    arcs_from_J = j * 9 - j * (j + 1) // 2
    assert arcs_from_J == expected
    assert arcs_from_J > 9 * 2

print(f"OK: 13-label tail regression; {checks} clipping vectors checked; unique Q=21 profile is 3^13")
