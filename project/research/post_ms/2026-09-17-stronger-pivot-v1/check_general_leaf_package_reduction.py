#!/usr/bin/env python3
"""Finite exact regression for GENERAL_LEAF_PACKAGE_REDUCTION.md.

Evidence only. The universal d>=3 leaf-package theorem is the hand proof.
The checker reconstructs the exact orientation-code graph, restricts to
quotient pairs whose two coordinates are leaves, computes an exact minimum
vertex cover, and compares it with the closed formula.
"""

from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
import json


def omega_edges(sigma):
    k = len(sigma)
    out = []
    for i in range(k):
        for j in range(i + 1, k):
            sgm = sigma[i][j]
            for s in (0, 1):
                u = 0
                for h in range(k):
                    if h == j:
                        val = 1 - s
                    elif h == i:
                        val = s ^ sgm
                    else:
                        val = 1 ^ s ^ sigma[j][h]
                    u |= val << h

                ss = s ^ sgm
                v = 0
                for h in range(k):
                    if h == i:
                        val = 1 - ss
                    elif h == j:
                        val = s
                    else:
                        val = 1 ^ ss ^ sigma[i][h]
                    v |= val << h
                out.append((u, v, i, j))
    return out


def exact_vertex_cover(edges):
    simple = set(tuple(sorted(e)) for e in edges)
    forced = {u for u, v in simple if u == v}
    simple = {(u, v) for u, v in simple if u != v and u not in forced and v not in forced}
    adj = defaultdict(set)
    for u, v in simple:
        adj[u].add(v)
        adj[v].add(u)

    seen = set()
    total = len(forced)
    for root in list(adj):
        if root in seen:
            continue
        stack = [root]
        seen.add(root)
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)

        index = {v: i for i, v in enumerate(comp)}
        n = len(comp)
        local = tuple(
            (index[u], index[v])
            for u, v in simple
            if u in index and v in index and index[u] < index[v]
        )

        @lru_cache(None)
        def solve(es):
            if not es:
                return 0
            degree = [0] * n
            nbr = [set() for _ in range(n)]
            for a, b in es:
                degree[a] += 1
                degree[b] += 1
                nbr[a].add(b)
                nbr[b].add(a)
            u = max(range(n), key=lambda x: degree[x])
            include_u = tuple((a, b) for a, b in es if a != u and b != u)
            best = 1 + solve(include_u)
            N = nbr[u]
            exclude_u = tuple((a, b) for a, b in es if a not in N and b not in N)
            return min(best, len(N) + solve(exclude_u))

        total += solve(local)
    return total


def make_state(d, p, t):
    k = d + sum(p) + 2 * t
    sigma = [[0] * k for _ in range(k)]
    # Use a complete exceptional core so all designated exceptional coordinates
    # are certainly non-leaves. The leaf-leaf package itself is core-independent.
    for i, j in combinations(range(d), 2):
        sigma[i][j] = sigma[j][i] = 1

    leaves = []
    cur = d
    for i, count in enumerate(p):
        for _ in range(count):
            sigma[i][cur] = sigma[cur][i] = 1
            leaves.append(cur)
            cur += 1
    for _ in range(t):
        u, v = cur, cur + 1
        cur += 2
        sigma[u][v] = sigma[v][u] = 1
        leaves.extend((u, v))
    assert cur == k
    return sigma, set(leaves)


def formula(p, t):
    g = sum(x > 0 for x in p)
    B = 2 * sum(max(x - 1, 0) for x in p)
    B += 2 * sum(min(p[i], p[j]) for i, j in combinations(range(len(p)), 2))
    if t == 0:
        return B
    return B + 4 * t * g + 2 * t * (t - 1) + 1


def main():
    checked = 0
    for d in range(3, 7):
        for p in product(range(3), repeat=d):
            for t in range(3):
                k = d + sum(p) + 2 * t
                if k > 13:
                    continue
                sigma, leaves = make_state(d, p, t)
                leaf_edges = [
                    (u, v)
                    for u, v, i, j in omega_edges(sigma)
                    if i in leaves and j in leaves
                ]
                got = exact_vertex_cover(leaf_edges)
                expected = formula(p, t)
                assert got == expected, (d, p, t, k, got, expected)
                checked += 1

    assert checked == 1766
    summary = {
        "status": "PASS_GENERAL_LEAF_PACKAGE_REDUCTION",
        "defect_range": [3, 6],
        "attachment_values": [0, 1, 2],
        "isolated_pair_values": [0, 1, 2],
        "maximum_k": 13,
        "exact_instances": checked,
        "failures": 0,
        "scope": "finite exact regression only; universal d>=3 formula remains a hand proof",
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
