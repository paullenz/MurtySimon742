#!/usr/bin/env python3
"""Finite exact regression for FOUR_DEFECT_ISOLATED_PAIR_EXCLUSION.md.

Evidence only.  Reconstructs the physical orientation-code graph and computes
exact minimum vertex covers.  The eventual universal reductions remain the
hand arguments in the accompanying notes.
"""

from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations
import json

CORE_PAIRS = list(combinations(range(4), 2))


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
                out.append((u, v))
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
        idx = {v: i for i, v in enumerate(comp)}
        n = len(comp)
        local = tuple(
            (idx[u], idx[v])
            for u, v in simple
            if u in idx and v in idx and idx[u] < idx[v]
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
            e1 = tuple((a, b) for a, b in es if a != u and b != u)
            best = 1 + solve(e1)
            N = nbr[u]
            e2 = tuple((a, b) for a, b in es if a not in N and b not in N)
            return min(best, len(N) + solve(e2))

        total += solve(local)
    return total


def core_degrees(mask):
    d = [0] * 4
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            d[i] += 1
            d[j] += 1
    return d


def canonical_rooted(mask):
    edges = {CORE_PAIRS[b] for b in range(6) if (mask >> b) & 1}
    reps = []
    for perm in permutations((1, 2, 3)):
        mp = {0: 0, 1: perm[0], 2: perm[1], 3: perm[2]}
        moved = {tuple(sorted((mp[i], mp[j]))) for i, j in edges}
        m = 0
        for b, e in enumerate(CORE_PAIRS):
            if e in moved:
                m |= 1 << b
        reps.append(m)
    return min(reps)


def make_state(z, y, t, mask):
    # p=(z,y,0,0), where y=0 is the one-group case.
    k = 4 + z + y + 2 * t
    sigma = [[0] * k for _ in range(k)]
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            sigma[i][j] = sigma[j][i] = 1
    cur = 4
    for _ in range(z):
        sigma[0][cur] = sigma[cur][0] = 1
        cur += 1
    for _ in range(y):
        sigma[1][cur] = sigma[cur][1] = 1
        cur += 1
    for _ in range(t):
        sigma[cur][cur + 1] = sigma[cur + 1][cur] = 1
        cur += 2
    assert cur == k
    return sigma


def valid(mask, y):
    d = core_degrees(mask)
    # Coordinate 0 has z>=4 leaves and is automatically non-leaf.
    if y + d[1] == 1:
        return False
    return d[2] != 1 and d[3] != 1


T1_G1 = {0: 8, 11: 16, 30: 14, 31: 12, 56: 19, 57: 17, 59: 16, 63: 16}
T2_G1 = {0: 16, 11: 32, 30: 26, 31: 24, 56: 35, 57: 33, 59: 32, 63: 32}


def main():
    one_group_checks = 0
    for t, expected in ((1, T1_G1), (2, T2_G1)):
        for z in range(4, 9):
            k = 4 + z + 2 * t
            for mask in range(64):
                if not valid(mask, 0):
                    continue
                c = canonical_rooted(mask)
                assert c in expected
                tau = exact_vertex_cover(omega_edges(make_state(z, 0, t, mask)))
                assert tau - 2 * k == expected[c], (t, z, mask, c, tau)
                one_group_checks += 1

    min_excess = {}
    two_group_checks = 0
    for y in (1, 2, 3):
        best = None
        for z in range(4, 9):
            k = 4 + z + y + 2
            local_best = None
            for mask in range(64):
                if not valid(mask, y):
                    continue
                tau = exact_vertex_cover(omega_edges(make_state(z, y, 1, mask)))
                excess = tau - 2 * k
                assert excess > 0
                local_best = excess if local_best is None else min(local_best, excess)
                two_group_checks += 1
            if best is None:
                best = local_best
            else:
                assert local_best == best
        min_excess[str(y)] = best

    assert min_excess == {"1": 14, "2": 18, "3": 20}

    summary = {
        "status": "PASS_FOUR_DEFECT_ISOLATED_PAIR_EXCLUSION",
        "one_group_z_range": [4, 8],
        "one_group_exact_instances": one_group_checks,
        "t1_g1_minimum_excess": min(T1_G1.values()),
        "t2_g1_minimum_excess": min(T2_G1.values()),
        "two_group_y_values": [1, 2, 3],
        "two_group_z_range": [4, 8],
        "two_group_exact_instances": two_group_checks,
        "two_group_minimum_excess_by_y": min_excess,
        "eventual_uniform_k_threshold": 13,
        "scope": "finite exact regression only; universal ray reductions are hand proofs",
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
