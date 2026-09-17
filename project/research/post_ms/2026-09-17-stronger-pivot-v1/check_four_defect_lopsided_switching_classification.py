#!/usr/bin/env python3
"""Finite exact regression for FOUR_DEFECT_LOPSIDED_SWITCHING_CLASSIFICATION.md.

Evidence only.  The universal rooted-core table and F-separation argument remain
hand mathematics.  This checker reconstructs the exact orientation-code graph,
computes exact vertex-cover sizes for all valid labelled rooted cores at
k=8,...,12, and replays the eventual arithmetic thresholds.
"""

from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations
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


CORE_PAIRS = list(combinations(range(4), 2))


def core_degrees(mask):
    d = [0] * 4
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            d[i] += 1
            d[j] += 1
    return d


def valid(mask):
    d = core_degrees(mask)
    # r=0 has k-4 pendant leaves and is automatically non-leaf for k>=8.
    return all(d[i] != 1 for i in (1, 2, 3))


def canonical(mask):
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


def make_sigma(k, mask):
    sigma = [[0] * k for _ in range(k)]
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            sigma[i][j] = sigma[j][i] = 1
    for d in range(4, k):
        sigma[0][d] = sigma[d][0] = 1
    return sigma


# Canonical rooted masks and exact tau-2k offsets.
EXPECTED = {
    0: 4,    # empty
    11: 3,   # K3 through root + isolated
    30: 4,   # C4
    31: 0,   # K4-e, missing edge away from root
    56: 4,   # non-root K3 + isolated root
    57: 1,   # paw, root pendant
    59: 4,   # K4-e, missing root edge
    63: -2,  # K4
}


def M(n):
    return ((n - 1) * (n - 1)) // 4 + 1


def closed(k, lam, exceptional):
    a = 2 * k - lam - 1
    r = k * (k - lam)
    h = r // (k - 1)
    f_bound = (h * h) // 4 + exceptional * k
    delta = r - f_bound
    n = 1 + 2 * k + a
    needed = 2 * k * (a + 1) - M(n)
    return delta >= needed


def eventual_threshold(lam, exceptional_fn, start=8, end=5000):
    flags = [closed(k, lam, exceptional_fn(lam)) for k in range(start, end + 1)]
    for i, flag in enumerate(flags):
        if flag and all(flags[i:]):
            return start + i
    return None


def main():
    checked = 0
    types = set()
    low_types = set()
    for k in range(8, 13):
        labelled = 0
        for mask in range(64):
            if not valid(mask):
                continue
            labelled += 1
            c = canonical(mask)
            assert c in EXPECTED
            tau = exact_vertex_cover(omega_edges(make_sigma(k, mask)))
            assert tau == 2 * k + EXPECTED[c], (k, mask, c, tau)
            types.add(c)
            if tau <= 2 * k:
                low_types.add(c)
            checked += 1
        assert labelled == 18

    assert types == set(EXPECTED)
    assert low_types == {31, 63}
    assert checked == 90

    thresholds = {
        "K4_lambda_1": eventual_threshold(1, lambda lam: 10 - 2 * lam),
        "K4_lambda_0": eventual_threshold(0, lambda lam: 10 - 2 * lam),
        "K4_lambda_minus_1": eventual_threshold(-1, lambda lam: 10 - 2 * lam),
        "K4_minus_nonroot_edge_lambda_minus_1": eventual_threshold(-1, lambda lam: 10),
    }
    assert thresholds == {
        "K4_lambda_1": 15,
        "K4_lambda_0": 17,
        "K4_lambda_minus_1": 19,
        "K4_minus_nonroot_edge_lambda_minus_1": 16,
    }

    summary = {
        "status": "PASS_FOUR_DEFECT_LOPSIDED_SWITCHING_CLASSIFICATION",
        "exact_k_range": [8, 12],
        "valid_labelled_rooted_core_instances": checked,
        "rooted_core_types": len(types),
        "tau_offsets_by_canonical_mask": {str(k): v for k, v in EXPECTED.items()},
        "low_cover_canonical_masks": sorted(low_types),
        "arithmetic_replay_k_range": [8, 5000],
        "closure_thresholds": thresholds,
        "uniform_lopsided_threshold": 19,
        "scope": "finite exact regression and arithmetic audit only; universal structural claims are hand proofs",
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
