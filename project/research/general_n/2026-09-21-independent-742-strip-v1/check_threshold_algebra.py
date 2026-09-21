#!/usr/bin/env python3
"""Exhaustive integer replay of the threshold-capacity algebraic gap."""

count = 0
for z in range(1, 81):
    for h in range(1, z + 1):
        q = z - h
        target = h * z + q * (q - 1) // 2
        for j in range(z + 1):
            source_bound = (z - j) * h + j * z - j * (j + 1) // 2
            gap = target - source_bound
            expected = (q - j) * (q - j - 1) // 2
            assert gap == expected
            assert gap >= 0
            count += 1

print(f"PASS: {count} exact integer triples checked")
