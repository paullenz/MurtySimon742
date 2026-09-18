#!/usr/bin/env python3
"""Proof-producing finite audit for SIX_DEFECT_COMPLETE_SUPPORT_EXCLUSION.md.

The hand coordinatewise-monotonicity theorem removes all pendant sizes beyond
the finite 0/1/2 status boundary.  This checker enumerates that boundary and
all labelled six-vertex exceptional cores.  It uses explicit residual
matchings, not an assumed optimum, except for the single fixed empty-core
case whose residual graph is solved exactly and checked by components.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
import json

D = 6
CORE_PAIRS = list(combinations(range(D), 2))
NCORE = 1 << len(CORE_PAIRS)


def precompute_cores():
    rows, degs = [], []
    for mask in range(NCORE):
        r = [0] * D
        d = [0] * D
        for bit, (i, j) in enumerate(CORE_PAIRS):
            if (mask >> bit) & 1:
                r[i] |= 1 << j
                r[j] |= 1 << i
                d[i] += 1
                d[j] += 1
        rows.append(tuple(r))
        degs.append(tuple(d))
    return rows, degs

CORE_ROWS, CORE_DEG = precompute_cores()


def leaf_value(p, t):
    B = 2 * sum(max(x - 1, 0) for x in p)
    B += 2 * sum(min(p[i], p[j]) for i in range(D) for j in range(i + 1, D))
    if t:
        g = sum(x > 0 for x in p)
        B += 4 * t * g + 2 * t * (t - 1) + 1
    return B


def valid_core(p, mask):
    return all(CORE_DEG[mask][i] + p[i] != 1 for i in range(D))


def make_rows(p, t, mask):
    k = D + sum(p) + 2 * t
    rows = list(CORE_ROWS[mask]) + [0] * (k - D)
    leaves = []
    cur = D
    for parent, size in enumerate(p):
        for _ in range(size):
            rows[parent] |= 1 << cur
            rows[cur] |= 1 << parent
            leaves.append(cur)
            cur += 1
    for _ in range(t):
        a, b = cur, cur + 1
        rows[a] |= 1 << b
        rows[b] |= 1 << a
        leaves.extend((a, b))
        cur += 2
    return rows, leaves


def omega_edges(rows):
    k = len(rows)
    allmask = (1 << k) - 1
    out = set()
    for i in range(k):
        ri = rows[i]
        for j in range(i + 1, k):
            s = (ri >> j) & 1
            u = (allmask ^ rows[j]) ^ (1 << i)
            v = ((allmask ^ ri) if s == 0 else ri) ^ (1 << j)
            out.add((u, v) if u <= v else (v, u))
            u, v = allmask ^ u, allmask ^ v
            out.add((u, v) if u <= v else (v, u))
    return out


def leaf_vertices(rows, leaves):
    k = len(rows)
    allmask = (1 << k) - 1
    out = set()
    for aa in range(len(leaves)):
        i = leaves[aa]
        ri = rows[i]
        for bb in range(aa + 1, len(leaves)):
            j = leaves[bb]
            s = (ri >> j) & 1
            u = (allmask ^ rows[j]) ^ (1 << i)
            v = ((allmask ^ ri) if s == 0 else ri) ^ (1 << j)
            out.update((u, v, allmask ^ u, allmask ^ v))
    return out


def residual_edges(p, t, mask):
    rows, leaves = make_rows(p, t, mask)
    es = omega_edges(rows)
    lv = leaf_vertices(rows, leaves)
    return [(u, v) for u, v in es if u not in lv and v not in lv]


def greedy_matching_size(edges, target=None):
    """Construct an explicit matching by a deterministic min-degree rule."""
    adj = defaultdict(set)
    for u, v in edges:
        if u == v:
            continue
        adj[u].add(v)
        adj[v].add(u)
    count = 0
    while adj:
        zeros = [x for x, N in adj.items() if not N]
        for x in zeros:
            adj.pop(x, None)
        if not adj:
            break
        u = min(adj, key=lambda x: (len(adj[x]), x))
        v = min(adj[u], key=lambda x: (len(adj.get(x, ())), x))
        for w in list(adj[u]):
            if w in adj:
                adj[w].discard(u)
        for w in list(adj.get(v, ())):
            if w in adj:
                adj[w].discard(v)
        adj.pop(u, None)
        adj.pop(v, None)
        count += 1
        if target is not None and count >= target:
            return count
    return count


def exact_vertex_cover(edges):
    simple = set(tuple(sorted(e)) for e in edges)
    forced = {u for u, v in simple if u == v}
    simple = {(u, v) for u, v in simple if u != v and u not in forced and v not in forced}
    adj = defaultdict(set)
    for u, v in simple:
        adj[u].add(v)
        adj[v].add(u)
    total = len(forced)
    seen = set()
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
        es = tuple(sorted({
            (min(idx[u], idx[v]), max(idx[u], idx[v]))
            for u, v in simple if u in idx and v in idx
        }))

        @lru_cache(None)
        def solve(cur):
            if not cur:
                return 0
            degree = [0] * n
            nbr = [set() for _ in range(n)]
            for a, b in cur:
                degree[a] += 1
                degree[b] += 1
                nbr[a].add(b)
                nbr[b].add(a)
            u = max(range(n), key=lambda q: degree[q])
            take_u = 1 + solve(tuple(e for e in cur if u not in e))
            N = nbr[u]
            take_N = len(N) + solve(tuple(e for e in cur if e[0] not in N and e[1] not in N))
            return min(take_u, take_N)

        total += solve(es)
    return total


def boundary_patterns():
    """Sorted coordinatewise-minimal status representatives for k>=9."""
    out = {}
    for t in range(0, 6):
        for p0 in combinations_with_replacement(range(3), D):
            q = list(p0)
            k = D + sum(q) + 2 * t
            if k < 9:
                twos = [i for i, x in enumerate(q) if x == 2]
                if not twos:
                    continue
                q[twos[-1]] += 9 - k
                k = 9
            q = tuple(q)
            L = leaf_value(q, t)
            status = tuple(0 if x == 0 else 1 if x == 1 else 2 for x in q)
            if L <= 2 * k:
                out.setdefault((t, status), (t, q, k, L))
    rows = sorted(out.values())
    assert len(rows) == 31, len(rows)
    assert Counter(t for t, _, _, _ in rows) == Counter({0:14, 1:8, 2:5, 3:3, 4:1})
    return rows


def component_signature(edges):
    adj = defaultdict(set)
    for u, v in edges:
        if u != v:
            adj[u].add(v)
            adj[v].add(u)
    seen = set()
    sig = Counter()
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
        C = set(comp)
        ces = [(u, v) for u, v in edges if u in C and v in C]
        degs = tuple(sorted(len(adj[x]) for x in C))
        sig[(len(C), len(set(ces)), degs, exact_vertex_cover(ces))] += 1
    return sig


def main():
    rows = boundary_patterns()
    lopsided = (0, (0,0,0,0,0,3))
    certificates = []
    special_failures = []

    for t, p, k, L in rows:
        if (t, p) == lopsided:
            # Audited independently in check_six_defect_lopsided_support_exclusion.py.
            continue
        target = 2 * k - L + 1
        valid = 0
        min_margin = None
        failures = []
        for mask in range(NCORE):
            if not valid_core(p, mask):
                continue
            valid += 1
            m = greedy_matching_size(residual_edges(p, t, mask), target=target)
            margin = L + m - 2 * k
            min_margin = margin if min_margin is None else min(min_margin, margin)
            if margin <= 0:
                failures.append((mask, m))
        if failures:
            special_failures.append((t, p, k, L, valid, failures))
        else:
            assert min_margin >= 1
            certificates.append({
                "t": t, "p": list(p), "k": k, "leaf_cover": L,
                "valid_cores": valid, "min_greedy_matching_margin": min_margin
            })

    assert len(certificates) == 29
    assert len(special_failures) == 1
    t, p, k, L, valid, failures = special_failures[0]
    assert (t, p, k, L, valid) == (2, (0,0,0,0,0,0), 10, 5, 13757)
    assert failures == [(0, 14)], failures

    # Sole generic-matching miss: exact residual decomposition for empty core.
    re = residual_edges(p, t, 0)
    tauR = exact_vertex_cover(re)
    assert tauR == 18
    sig = component_signature(re)
    expected = Counter({
        (7, 6, (1,1,1,1,1,1,6), 1): 8,  # 8 K_{1,6}
        (6, 15, (5,5,5,5,5,5), 5): 2,   # 2 K_6
    })
    assert sig == expected, (sig, expected)
    assert L + tauR - 2 * k == 3

    summary = {
        "status": "PASS_COMPLETE_SIX_DEFECT_SUPPORT_EXCLUSION",
        "threshold_k": 9,
        "boundary_patterns": 31,
        "boundary_patterns_by_t": {"0":14,"1":8,"2":5,"3":3,"4":1},
        "lopsided_pattern": [0,0,0,0,0,3],
        "generic_matching_certified_patterns": len(certificates),
        "generic_min_margin": min(row["min_greedy_matching_margin"] for row in certificates),
        "sole_generic_matching_miss": {
            "t": 2, "p": [0,0,0,0,0,0], "k": 10,
            "core_mask": 0, "residual_decomposition": "8 K_(1,6) + 2 K_6",
            "leaf_plus_residual_cover_minus_2k": 3
        },
        "certificates": certificates,
        "trust_boundary": "hand coordinatewise monotonicity plus finite explicit matching certificates; external review open"
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
