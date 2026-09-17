#!/usr/bin/env python3
"""Finite exact audit for FIVE_DEFECT_COMPLETE_SUPPORT_EXCLUSION.md.

The infinite part is not scanned: the accompanying hand lemmas give the
leaf-package finite-width reduction and residual ray monotonicity.  This file
checks the remaining finite 5-vertex exceptional cores at one base point per
ray and verifies the three explicit lopsided low-core formulas.
"""

from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations
import json

D = 5
CORE_PAIRS = list(combinations(range(D), 2))


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
                out.append((u, v, i, j, s))
    return out


def exact_vertex_cover(edge_pairs):
    simple = set(tuple(sorted(e)) for e in edge_pairs)
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
            (min(idx[u], idx[v]), max(idx[u], idx[v]))
            for u, v in simple
            if u in idx and v in idx
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

        total += solve(tuple(sorted(set(local))))
    return total


def make_state(p, t, mask):
    k = D + sum(p) + 2 * t
    sigma = [[0] * k for _ in range(k)]
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            sigma[i][j] = sigma[j][i] = 1
    cur = D
    groups = []
    for i, pi in enumerate(p):
        group = []
        for _ in range(pi):
            sigma[i][cur] = sigma[cur][i] = 1
            group.append(cur)
            cur += 1
        groups.append(group)
    pairs = []
    for _ in range(t):
        sigma[cur][cur + 1] = sigma[cur + 1][cur] = 1
        pairs.append((cur, cur + 1))
        cur += 2
    return sigma, groups, pairs


def valid_core(p, mask):
    deg = [0] * D
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            deg[i] += 1
            deg[j] += 1
    return all(p[i] + deg[i] != 1 for i in range(D))


def leaf_package_value(p, t):
    g = sum(x > 0 for x in p)
    B = 2 * sum(max(x - 1, 0) for x in p)
    B += 2 * sum(min(p[i], p[j]) for i in range(D) for j in range(i + 1, D))
    if t:
        B += 4 * t * g + 2 * t * (t - 1) + 1
    return B


def residual_edges(p, t, mask):
    sigma, groups, pairs = make_state(p, t, mask)
    all_edges = omega_edges(sigma)
    leaves = [x for group in groups for x in group]
    leaves += [x for pair in pairs for x in pair]
    leaf_pairs = set(combinations(leaves, 2))
    leaf_vertices = set()
    for u, v, i, j, _ in all_edges:
        if (i, j) in leaf_pairs:
            leaf_vertices.add(u)
            leaf_vertices.add(v)
    return [
        (u, v) for u, v, _, _, _ in all_edges
        if u not in leaf_vertices and v not in leaf_vertices
    ]


def full_tau(p, t, mask):
    sigma, _, _ = make_state(p, t, mask)
    return exact_vertex_cover([(u, v) for u, v, _, _, _ in omega_edges(sigma)])


def canonical_rooted(mask, root=4):
    edges = {CORE_PAIRS[b] for b in range(len(CORE_PAIRS)) if (mask >> b) & 1}
    others = [i for i in range(D) if i != root]
    reps = []
    for perm in permutations(others):
        mp = {root: root}
        for old, new in zip(others, perm):
            mp[old] = new
        moved = {tuple(sorted((mp[i], mp[j]))) for i, j in edges}
        m = 0
        for b, e in enumerate(CORE_PAIRS):
            if e in moved:
                m |= 1 << b
        reps.append(m)
    return min(reps)


def no_pair_bases():
    out = []
    for a in range(0, 4):
        for b in range(a, 5):
            for c in range(b, 7):
                for d in range(c, 11):
                    g = sum(x > 0 for x in (a, b, c, d)) + 1
                    if 4*a + 3*b + 2*c + d <= 5 + g:
                        out.append((a, b, c, d))
    return out


def min_additive_margin(p, t):
    L = leaf_package_value(p, t)
    k = D + sum(p) + 2 * t
    best = None
    valid = 0
    for mask in range(1 << len(CORE_PAIRS)):
        if not valid_core(p, mask):
            continue
        valid += 1
        r = exact_vertex_cover(residual_edges(p, t, mask))
        margin = L + r - 2 * k
        best = margin if best is None else min(best, margin)
    return best, valid


def main():
    # t=0 finite-width list: every nonlopsided base has positive additive margin.
    no_pair_rows = []
    bases = no_pair_bases()
    assert len(bases) == 23
    for base in bases:
        if base == (0, 0, 0, 0):
            continue
        z = max(base[-1], 2)
        p = base + (z,)
        margin, valid = min_additive_margin(p, 0)
        assert margin > 0, (base, z, margin)
        no_pair_rows.append({"base": list(base), "z": z, "margin": margin, "valid_cores": valid})

    # t=1 and t=2 surviving pendant rays.
    pair_rows = []
    pair_bases = [
        ((0,0,0,0,2), 1),
        ((0,0,0,1,2), 1),
        ((0,0,0,2,2), 1),
        ((0,0,0,3,3), 1),
        ((0,0,0,4,4), 1),
        ((0,0,1,1,2), 1),
        ((0,0,0,0,2), 2),
    ]
    for p, t in pair_bases:
        margin, valid = min_additive_margin(p, t)
        assert margin > 0
        pair_rows.append({"p": list(p), "t": t, "margin": margin, "valid_cores": valid})

    # g=0 fixed isolated-pair cases relevant to k>=8.
    fixed = {}
    for t, expected in ((2,3),(3,11),(4,23)):
        p = (0,0,0,0,0)
        margin, valid = min_additive_margin(p, t)
        assert margin == expected, (t, margin)
        fixed[str(t)] = {"margin": margin, "valid_cores": valid}

    # Lopsided t=0 base z=3. The additive split can fail only in three rooted classes.
    p = (0,0,0,0,3)
    L = leaf_package_value(p, 0)
    k = D + sum(p)
    dangerous = set()
    for mask in range(1 << len(CORE_PAIRS)):
        if not valid_core(p, mask):
            continue
        r = exact_vertex_cover(residual_edges(p, 0, mask))
        if L + r <= 2 * k:
            dangerous.add(canonical_rooted(mask))
    assert dangerous == {861, 894, 895}, dangerous

    # Explicit full-cover formulas for the three dangerous rooted cores.
    formulas = {861: 2, 894: 2, 895: 1}  # tau - 2k
    for z in range(3, 9):
        pz = (0,0,0,0,z)
        kz = D + z
        for mask, excess in formulas.items():
            tau = full_tau(pz, 0, mask)
            assert tau == 2 * kz + excess, (z, mask, tau, excess)

    # Finite boundary: z=2 has equality states, so the support theorem starts at k=8.
    p2 = (0,0,0,0,2)
    equality = 0
    for mask in range(1 << len(CORE_PAIRS)):
        if valid_core(p2, mask) and full_tau(p2, 0, mask) == 2 * (D + 2):
            equality += 1
    assert equality == 5

    summary = {
        "status": "PASS_FIVE_DEFECT_COMPLETE_SUPPORT_EXCLUSION",
        "no_pair_bounded_patterns": len(bases),
        "nonlopsided_no_pair_rows": no_pair_rows,
        "isolated_pair_rows": pair_rows,
        "g0_fixed_pair_cases": fixed,
        "lopsided_dangerous_rooted_cores": [861, 894, 895],
        "lopsided_excess_formulas": {"861": 2, "894": 2, "895": 1},
        "lopsided_z_checked": [3, 8],
        "z2_equality_labelled_cores": equality,
        "support_threshold_k": 8,
        "scope": "finite core audit after hand finite-width and ray-monotonicity reductions",
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
