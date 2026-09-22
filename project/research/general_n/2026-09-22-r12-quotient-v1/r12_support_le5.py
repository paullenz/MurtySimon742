#!/usr/bin/env python3
"""Exact r=12 quotient/source screen for residual support at most five."""
import itertools
import json
import sys
from functools import lru_cache


def parts(n, hi=None):
    if n == 0:
        yield (); return
    for x in range(min(n, hi or n), 0, -1):
        for tail in parts(n-x, x):
            yield (x,) + tail


def perms_for(residual):
    groups = [tuple(i for i, x in enumerate(residual) if x == value)
              for value in sorted(set(residual), reverse=True)]
    for choices in itertools.product(
            *(itertools.permutations(group) for group in groups)):
        permutation = list(range(len(residual)))
        for group, image in zip(groups, choices):
            for i, j in zip(group, image):
                permutation[i] = j
        yield tuple(permutation)


def datum(residual, pairs, mask):
    k = len(residual); degree = [0] * k
    neigh = [set() for _ in residual]; edges = []
    for q, (i, j) in enumerate(pairs):
        if mask >> q & 1:
            edges.append((i, j)); degree[i] += 1; degree[j] += 1
            neigh[i].add(j); neigh[j].add(i)
    positive = {i for i in range(k) if degree[i] > residual[i]}
    nonpositive = set(range(k)) - positive
    if any((degree[i]-residual[i])**2 >
           sum(residual[j] for j in neigh[i]) for i in positive):
        return None
    e_pos = sum(i in positive and j in positive for i, j in edges)
    e_non = sum(i in nonpositive and j in nonpositive for i, j in edges)
    slack = sum(i in nonpositive and residual[i] == 1 and degree[i] == 0
                for i in range(k))
    strict = e_pos - e_non - sum(residual[i] for i in positive) - slack
    return None if strict <= 0 else (edges, degree, neigh, positive, strict)


def source(residual, data):
    edges, degree, neigh, positive, strict = data
    k = len(residual)
    need = tuple(max(0, degree[i]-residual[i]) for i in range(k))
    patterns = []
    for state in itertools.product(range(3), repeat=k):
        left = {i for i, s in enumerate(state) if s == 1}
        zero = {i for i, s in enumerate(state) if s == 2}
        if not zero or any(not neigh[i] <= left | zero or
                           len(neigh[i] & left) > residual[i] for i in left):
            continue
        patterns.append((tuple(int(i in zero) for i in range(k)),
                         tuple(int(i in left) for i in range(k)), state))

    @lru_cache(None)
    def solve(rem, covered):
        if not any(rem):
            return () if all(covered[i] >= need[i] for i in range(k)) else None
        for q, (zero, left, state) in enumerate(patterns):
            if all(zero[i] <= rem[i] for i in range(k)):
                tail = solve(
                    tuple(rem[i]-zero[i] for i in range(k)),
                    tuple(min(need[i], covered[i]+left[i]) for i in range(k)))
                if tail is not None:
                    return (q,) + tail
        return None

    witness = solve(residual, (0,) * k)
    return None if witness is None else [patterns[q][2] for q in witness]


output = {}
for residual in parts(12):
    k = len(residual)
    if k > 5:
        continue
    pairs = list(itertools.combinations(range(k), 2))
    index = {edge: q for q, edge in enumerate(pairs)}
    permutations = list(perms_for(residual))
    representatives = {}
    for mask in range(1 << len(pairs)):
        data = datum(residual, pairs, mask)
        if data is None:
            continue
        best = min(sum(
            1 << index[tuple(sorted((p[i], p[j])))]
            for q, (i, j) in enumerate(pairs) if mask >> q & 1)
            for p in permutations)
        if best not in representatives:
            representatives[best] = datum(residual, pairs, best)
    feasible = []
    for mask, data in representatives.items():
        witness = source(residual, data)
        if witness is not None:
            feasible.append({
                "mask": mask, "t_upper": data[4], "edges": data[0],
                "degrees": data[1], "witness": witness})
    output[str(residual)] = {
        "support": k, "strict_orbits": len(representatives),
        "source_feasible": len(feasible), "feasible": feasible}
    print(residual, len(representatives), len(feasible), file=sys.stderr, flush=True)
print(json.dumps(output, indent=2))
