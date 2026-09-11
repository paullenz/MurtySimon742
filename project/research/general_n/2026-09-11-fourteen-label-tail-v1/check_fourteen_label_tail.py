#!/usr/bin/env python3
"""Exact regression for the 14-label threshold-tail hand theorem.
This follows the displayed hand proof and is not a proof premise.
"""
A = 14

def C(h, z):
    return (z * (z - 1) + h * (h + 1)) // 2

def gamma(h, W):
    if W <= 0:
        return 0
    z = h
    while W > C(h, z):
        z += 1
    return z

def D(v):
    ans = 0
    for h in range(2, A):
        vals = [x for x in v if x >= h]
        if vals:
            ans += len(vals) - gamma(h, sum(vals))
    return ans

def Q(v):
    return sum(x >= 1 for x in v) + D(v)

# h>=9 has nonpositive level deficit at the minimum possible tail weight.
for h in range(9, A):
    for N in range(1, A + 1):
        assert N - gamma(h, h * N) <= 0, (h, N)

expected = {
    8: {14: (1, 6)},
    7: {13: (1, 5), 14: (1, 6)},
    6: {11: (1, 3), 12: (1, 4), 13: (1, 4), 14: (2, 5)},
    5: {10: (1, 3), 11: (1, 3), 12: (2, 3), 13: (2, 3), 14: (3, 4)},
    4: {9: (1, 2), 10: (1, 2), 11: (2, 2), 12: (2, 2), 13: (3, 3), 14: (3, 3)},
}

# Recompute every safe-interval minimum in the clipping table.
for M in (8, 7, 6, 5, 4):
    positive = {}
    for k in range(1, A + 1):
        loss = k - gamma(M, M * k)
        if loss <= 0:
            continue
        gain = 0
        lo = M * k
        hi = M * k + (M - 1) * (A - k)
        for h in range(2, M):
            drop = min(gamma(h, W) - gamma(h, W - k)
                       for W in range(lo, hi + 1))
            gain += drop
        assert gain >= loss, (M, k, loss, gain)
        positive[k] = (loss, gain)
    assert positive == expected[M], (M, positive)

# Terminal max-three domain and unique D=9 case.
terminal_eq = []
for y in range(A + 1):
    for x in range(y, A + 1):
        v = [0] * (A - x) + [2] * (x - y) + [3] * y
        d = D(v)
        assert d <= 9, (x, y, d)
        if d == 9:
            terminal_eq.append((x, y))
assert terminal_eq == [(14, 14)]

# Max-four equality layer among positive vectors.
seq4 = []
for k in range(A + 1):
    v = [3] * (A - k) + [4] * k
    seq4.append(D(v))
assert seq4 == [9, 5, 6, 7, 8, 8, 8, 7, 7, 8, 7, 8, 8, 9, 9]

# Max-five preimages of the two max-four equality profiles containing fours.
seq5_13 = []
for j in range(1, 14):
    v = [3] + [4] * (13 - j) + [5] * j
    seq5_13.append(D(v))
assert seq5_13 == [5, 6, 7, 6, 7, 7, 6, 6, 6, 7, 7, 8, 8]
assert 9 not in seq5_13

seq5_14 = []
for j in range(1, 15):
    v = [4] * (14 - j) + [5] * j
    seq5_14.append(D(v))
assert seq5_14 == [5, 6, 6, 7, 8, 7, 7, 7, 7, 7, 7, 8, 8, 8]
assert 9 not in seq5_14

for v in ([3] * 14, [3] + [4] * 13, [4] * 14):
    assert D(v) == 9 and Q(v) == 23

print("OK: fourteen-label hand theorem arithmetic and equality tables")
