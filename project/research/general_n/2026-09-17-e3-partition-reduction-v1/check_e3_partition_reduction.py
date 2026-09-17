#!/usr/bin/env python3
"""Replay guard for E3_PARTITION_REDUCTION.md.

This is not a graph search. It independently checks:
  * the preserved failure of the first 10/15 coefficient attempt,
  * the corrected 12/15 local source inequality for partitions
    (1,1,1) and (2,1),
  * the global source-vs-label gap for every k=0..20, and
  * the exact local obstruction that remains for partition (3).
"""

A = 20
B = 23


def U0(k: int) -> int:
    r = 76 + k
    return 624 + 13 * k + min(14 * k, r)


def excess_capacity(partition, g):
    if g <= 0:
        return A
    return sum(1 for e in partition if e >= g)


def local_states(k: int, rho: int, partition):
    out = []
    demand_compatible = 0 if rho < 4 else (A - k if rho == 4 else A)
    for p in range(rho + 3):  # p<=rho+2
        qmax = min(A - rho, B - 1 - p, demand_compatible)
        for q in range(qmax + 1):
            if q > 0:
                g = max(0, p - rho + 1)
                if q > excess_capacity(partition, g):
                    continue
            out.append((p, q))
    return out


def support10(p: int, q: int) -> int:
    return 10 * p + 15 * q - q * (p + q)


def support12(p: int, q: int) -> int:
    return 12 * p + 15 * q - q * (p + q)


# Preserve the failed first attempt: partition (1,1,1), rho=5,p=5,q=3.
assert support10(5, 3) == 71
assert 10 * 5 + 20 == 70
assert support10(5, 3) > 70

# Corrected local theorem: support12 <= 12rho+24 for both split partitions.
for partition in [(1, 1, 1), (2, 1)]:
    for k in range(21):
        for rho in range(1, 21):
            rhs = 12 * rho + 24
            for p, q in local_states(k, rho, partition):
                lhs = support12(p, q)
                assert lhs <= rhs, (partition, k, rho, p, q, lhs, rhs)

# At E=3, Q=83+k and r=76+k, so the corrected support theorem gives
# source >= 27Q-12r-24*23 = 777+15k.
# Partition (2,1) has the larger label increment: +77.
for k in range(21):
    source_lower = 777 + 15 * k
    label_upper_21 = U0(k) + 77
    label_upper_111 = U0(k) + 75
    assert source_lower > label_upper_21, (k, source_lower, label_upper_21)
    assert source_lower > label_upper_111

# Check the simple closed-form minimum gaps in the two k regimes.
small_gaps = [777 + 15 * k - (U0(k) + 77) for k in range(0, 6)]
large_gaps = [777 + 15 * k - (U0(k) + 77) for k in range(6, 21)]
assert min(small_gaps) == 16
assert min(large_gaps) == 6

# Partition (3) genuinely escapes the corrected local support theorem.
# rho=4,p=6,q=1 has g=3 and is allowed by the unique excess-three label.
rho, p, q = 4, 6, 1
g = max(0, p - rho + 1)
assert g == 3
assert q <= excess_capacity((3,), g)
assert support12(p, q) == 80
assert 12 * rho + 24 == 72
assert support12(p, q) - (12 * rho + 24) == 8

# rho=5 gives the same mechanism with surplus 7.
rho, p, q = 5, 7, 1
assert max(0, p - rho + 1) == 3
assert support12(p, q) == 91
assert 12 * rho + 24 == 84
assert support12(p, q) - (12 * rho + 24) == 7

print("PASS_E3_PARTITION_REDUCTION")
print("closed_partitions=(1,1,1),(2,1)")
print("sole_remaining_partition=(3)")
print("minimum_global_gap_partition21=6")
print("preserved_failed_10_15_state=rho5,p5,q3")
print("partition3_12_15_failure=rho4,p6,q1,bonus8")
