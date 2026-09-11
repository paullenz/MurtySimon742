#!/usr/bin/env python3
"""Small exact arithmetic regression for the N31 hand route."""

n = 31
Turan = n * n // 4
assert Turan == 240
assert 19 * 12 > 7 * n  # Delta=19 lies strictly above 7n/12.
assert 18 * (31 - 18) == 234
assert 17 * (31 - 17) == 238
assert 16 * (31 - 16) == 240

# Delta=16 witness-deficit tables.
def witness_rhs(h, o):
    return h * (h - 1) // 2 + h * (31 - h) + o * (o - 1)

row241 = []
for h in range(8):
    o = 14 - 2 * h
    row241.append(witness_rhs(h, o))
assert row241 == [182, 162, 149, 143, 144, 152, 167, 189]
assert max(row241) < 241

row240 = []
for h in range(9):
    o = 16 - 2 * h
    row240.append(witness_rhs(h, o))
assert row240 == [240, 212, 191, 177, 170, 170, 177, 191, 212]
assert row240.count(240) == 1 and row240[0] == 240

# Equality witness count.
assert 2 * (16 * 15 // 2) == 240

print("OK: N31 hand-route arithmetic tables and degree thresholds")
