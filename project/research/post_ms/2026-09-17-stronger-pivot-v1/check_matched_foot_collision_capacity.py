#!/usr/bin/env python3
"""Audit the Boolean sign algebra in MATCHED_FOOT_COLLISION_CAPACITY.md.

Hand proofs are primary.  We exhaust all 2-lift signings through p=6 and verify
that complementary endpoint source codes and gamma-collision classes have the
claimed switching-zero structure.
"""

from collections import defaultdict
from itertools import combinations
import json

summary = {
    "signings": 0,
    "gamma_collision_classes": 0,
    "gamma_collision_pairs": 0,
    "endpoint_complement_checks": 0,
    "failures": 0,
}

for p in range(2, 7):
    pairs = [(i, j) for i in range(p) for j in range(i + 1, p)]
    for mask in range(1 << len(pairs)):
        sigma = [[0] * p for _ in range(p)]
        for bit, (i, j) in enumerate(pairs):
            val = (mask >> bit) & 1
            sigma[i][j] = sigma[j][i] = val

        gamma = {}
        for i in range(p):
            for s in (0, 1):
                code = []
                for j in range(p):
                    if j == i:
                        code.append(1 - s)
                    else:
                        code.append(1 ^ s ^ sigma[i][j])
                gamma[(i, s)] = tuple(code)

            assert all(
                a ^ b == 1
                for a, b in zip(gamma[(i, 0)], gamma[(i, 1)])
            )
            summary["endpoint_complement_checks"] += 1

        buckets = defaultdict(list)
        for endpoint, code in gamma.items():
            buckets[code].append(endpoint)

        for endpoints in buckets.values():
            if len(endpoints) <= 1:
                continue
            summary["gamma_collision_classes"] += 1
            for (i, si), (j, sj) in combinations(endpoints, 2):
                assert i != j
                assert sigma[i][j] == (si ^ sj)
                assert sigma[i][j] ^ si ^ sj == 0
                summary["gamma_collision_pairs"] += 1

        summary["signings"] += 1

summary["total_checks"] = (
    summary["signings"]
    + summary["gamma_collision_classes"]
    + summary["gamma_collision_pairs"]
    + summary["endpoint_complement_checks"]
)

print(json.dumps(summary, indent=2, sort_keys=True))
