#!/usr/bin/env python3
"""Exact arithmetic replay for the selected-witness Hall strictness example."""

A, B, T = 10, 20, 0
s = [2] + [3] * 9
x = [2] + [3] * 9
R = [4, 2, 2] + [3] * 7
C = [R[i] + x[i] for i in range(A)]
e = [x[i] - s[i] for i in range(A)]

rho = [3] * 5 + [2] * 7 + [0] * 8
p = [2] * 5 + [1] * 7 + [6, 6] + [0] * 6
q = [0] * 5 + [5, 4, 4, 4, 4, 4, 4] + [0] * 8
Q = sum(s)

# Selected incidence matrix: rows are B-sources, columns are A-labels.
sel = [[0] * A for _ in range(B)]
high_patterns = [
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 0),
    (4, 0, 1),
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 0),
]
for j, srcs in enumerate(high_patterns, start=1):
    for u in srcs:
        sel[u][j] = 1
sel[5][0] = 1
sel[6][0] = 1

# Residual incidence matrix, explicitly disjoint from sel.
res = [[0] * A for _ in range(B)]
# High-source residual edges.
for u, labs in {
    0: (2, 3, 7),
    1: (3, 4, 8),
    2: (4, 5, 9),
    3: (1, 5, 6),
    4: (1, 2, 6),
}.items():
    for i in labs:
        res[u][i] = 1
# Low-source residual edges.
for u, labs in {
    5: (3, 7),
    6: (4, 8),
    7: (0, 5),
    8: (0, 6),
    9: (0, 7),
    10: (0, 9),
    11: (8, 9),
}.items():
    for i in labs:
        res[u][i] = 1

assert sum(s) == sum(x) == Q == 29
assert sum(R) == sum(rho) == 29
assert sum(s) == sum(rho) + 2 * T
assert sum(p) == sum(q) == Q
assert C == [6, 5, 5] + [6] * 7
assert e == [0] * A

# Exact selected and residual margins and pair disjointness.
assert [sum(sel[u][i] for u in range(B)) for i in range(A)] == x
assert [sum(res[u][i] for u in range(B)) for i in range(A)] == R
assert [sum(res[u]) for u in range(B)] == rho
assert all(not (sel[u][i] and res[u][i]) for u in range(B) for i in range(A))

# Every displayed selected edge obeys the inherited local bridge conditions.
for u in range(B):
    assert p[u] + q[u] <= B - 1
    assert p[u] <= rho[u] + B - A - 1
    for i in range(A):
        if sel[u][i]:
            assert s[i] <= rho[u]
            assert e[i] >= max(0, p[u] - rho[u] + 1)
            assert p[u] + q[u] <= C[i]

# Reconstruct the excess-aware local source envelope A_u(p_u).
def local_A(u):
    best = 0
    for i in range(A):
        if s[i] <= 0 or s[i] > rho[u]:
            continue
        if e[i] < max(0, p[u] - rho[u] + 1):
            continue
        best = max(best, min(C[i] - p[u], B - 1 - p[u]))
    return max(0, best)

local_caps = [local_A(u) for u in range(B)]
assert all(q[u] <= local_caps[u] for u in range(B))
assert sum(local_caps) >= Q

# The global selected-witness Hall cut catches the reuse that the local envelope misses.
active_low = [u for u in range(B) if q[u] > 0 and rho[u] <= 2]
eligible_low_labels = [i for i in range(A) if s[i] <= 2]
hall_capacity = sum(x[i] for i in eligible_low_labels)
hall_deficiency = len(active_low) - hall_capacity
assert len(active_low) == 7
assert eligible_low_labels == [0]
assert hall_capacity == 2
assert hall_deficiency == 5

# Direct admissible-neighbour union for this active set is also just L0.
def neighbours(u):
    out = []
    for i in range(A):
        if (s[i] <= rho[u]
            and e[i] >= max(0, p[u] - rho[u] + 1)
            and C[i] >= p[u] + q[u]):
            out.append(i)
    return out

union = sorted(set(i for u in active_low for i in neighbours(u)))
assert union == [0]
assert len(active_low) > sum(x[i] for i in union)

print("PASS_SELECTED_WITNESS_HALL_STRICTNESS")
print(f"Q={Q} local_cap_sum={sum(local_caps)}")
print(f"active_rho_le_2={len(active_low)} witness_capacity={hall_capacity} deficiency={hall_deficiency}")
print(f"selected_column_margins={x}")
print(f"residual_column_margins={R}")
