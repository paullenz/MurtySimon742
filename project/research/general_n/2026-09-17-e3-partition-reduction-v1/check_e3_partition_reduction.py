#!/usr/bin/env python3
"""Replay guard for E3_PARTITION_REDUCTION.md.

This is not a graph search. It independently checks:
  * the inherited zero-excess gap G(k),
  * validity of the old local source inequality for E=3 partitions
    (1,1,1) and (2,1),
  * the unique arithmetic boundary for (2,1), and
  * the local failure mechanism for partition (3).
"""

A = 20
B = 23


def delta(k: int) -> int:
    if k <= 14:
        return 6
    if k == 15:
        return 5
    if k == 16:
        return 2
    return 0


def U0(k: int) -> int:
    r = 76 + k
    return 624 + 13 * k + min(14 * k, r)


def L0(k: int) -> int:
    c4_cap = (33 + k) // 3
    return 780 + 15 * k - delta(k) * c4_cap


G = [L0(k) - U0(k) for k in range(21)]
assert min(G) == 2
assert [k for k, g in enumerate(G) if g == 2] == [12]


def excess_capacity(partition, g):
    """Number of distinct labels with excess >= g in a worst compatible row."""
    if g <= 0:
        return A
    return sum(1 for e in partition if e >= g)


def local_states(k: int, rho: int, partition):
    out = []
    demand_compatible = 0 if rho < 4 else (A - k if rho == 4 else A)
    for p in range(rho + 3):  # incoming cap p<=rho+2
        for q in range(min(A - rho, B - 1 - p, demand_compatible) + 1):
            if q == 0:
                out.append((p, q))
                continue
            g = max(0, p - rho + 1)
            if q > excess_capacity(partition, g):
                continue
            out.append((p, q))
    return out


def support_value(p: int, q: int) -> int:
    return 10 * p + 15 * q - q * (p + q)


for partition in [(1, 1, 1), (2, 1)]:
    for k in range(21):
        d = delta(k)
        for rho in range(1, 21):
            rhs = 10 * rho + 20 + (d if rho == 4 else 0)
            for p, q in local_states(k, rho, partition):
                assert support_value(p, q) <= rhs, (
                    partition,
                    k,
                    rho,
                    p,
                    q,
                    support_value(p, q),
                    rhs,
                )

# Partition (1,1,1): label increment <= 72+3=75, source increment=75.
for k in range(21):
    assert L0(k) + 75 > U0(k) + 75

# Partition (2,1): label increment <=72+5=77, source increment=75.
# Only k=12 can meet the relaxed bounds at equality.
equality_ks = []
for k in range(21):
    source_lower = L0(k) + 75
    label_upper = U0(k) + 77
    if source_lower <= label_upper:
        equality_ks.append((k, source_lower, label_upper))
assert equality_ks == [(12, L0(12) + 75, U0(12) + 77)]
assert equality_ks[0][1] == equality_ks[0][2]

# At k=12 equality in the residual-mass estimate forces rho=(5^5,4^15,1^3).
# Enumerate locally tight states for partition (2,1) and record the largest p.
k = 12
part = (2, 1)
max_p_tight = {}
for rho in (1, 4, 5):
    rhs = 10 * rho + 20 + (delta(k) if rho == 4 else 0)
    tight = [(p, q) for p, q in local_states(k, rho, part)
             if support_value(p, q) == rhs]
    assert tight, (rho, "no tight state")
    max_p_tight[rho] = max(p for p, q in tight)

assert max_p_tight == {1: 3, 4: 3, 5: 7}, max_p_tight
max_total_p = 3 * max_p_tight[1] + 15 * max_p_tight[4] + 5 * max_p_tight[5]
assert max_total_p == 89
assert max_total_p < 95  # Q=83+k=95

# Partition (3): exhibit the exact local mechanism that breaks the old support bound.
# At rho=5, p=rho+2=7, q=1, g=3 is allowed by one excess-three label.
rho = 5
p = 7
q = 1
assert q <= excess_capacity((3,), max(0, p - rho + 1))
lhs = support_value(p, q)
rhs = 10 * rho + 20
assert (lhs, rhs, lhs - rhs) == (77, 70, 7)

print("PASS_E3_PARTITION_REDUCTION")
print("closed_partitions=(1,1,1),(2,1)")
print("sole_remaining_partition=(3)")
print("k12_partition21_tight_incoming_cap=89<Q95")
print("partition3_local_support_failure=rho5,p7,q1,bonus7")
