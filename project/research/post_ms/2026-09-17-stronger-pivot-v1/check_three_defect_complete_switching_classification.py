#!/usr/bin/env python3
"""Independent finite audit for THREE_DEFECT_COMPLETE_SWITCHING_CLASSIFICATION.md.

Evidence only.  The universal theorem remains the hand argument in the note.
This checker reconstructs the physical orientation-code graph from the 2-lift
signing formula, computes exact minimum vertex covers by componentwise branch
and bound, and compares them against the claimed B+C_H table.

Only the Python standard library is used.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
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
    # Parallel edges do not affect vertex-cover size.  A loop forces its vertex.
    simple = set(tuple(sorted(e)) for e in edges)
    forced = {u for u, v in simple if u == v}
    simple = {(u, v) for u, v in simple if u != v and u not in forced and v not in forced}

    adj = defaultdict(set)
    for u, v in simple:
        adj[u].add(v)
        adj[v].add(u)

    seen = set()
    components = []
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
        components.append(comp)

    total = len(forced)
    for comp in components:
        index = {v: i for i, v in enumerate(comp)}
        local_edges = tuple(
            (index[u], index[v])
            for u, v in simple
            if u in index and v in index and index[u] < index[v]
        )
        n = len(comp)

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

            # If u is excluded, all neighbours of u must be included.
            N = nbr[u]
            exclude_u = tuple((a, b) for a, b in es if a not in N and b not in N)
            best = min(best, len(N) + solve(exclude_u))
            return best

        total += solve(local_edges)
    return total


def make_sigma(k, p, core_mask):
    sigma = [[0] * k for _ in range(k)]
    core_pairs = ((0, 1), (0, 2), (1, 2))
    for bit, (i, j) in enumerate(core_pairs):
        if (core_mask >> bit) & 1:
            sigma[i][j] = sigma[j][i] = 1
    d = 3
    for i, count in enumerate(p):
        for _ in range(count):
            sigma[i][d] = sigma[d][i] = 1
            d += 1
    assert d == k
    return sigma


def core_degrees(mask):
    deg = [0, 0, 0]
    for bit, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
        if (mask >> bit) & 1:
            deg[i] += 1
            deg[j] += 1
    return deg


def core_type(mask):
    m = mask.bit_count()
    return ("empty", "edge", "P3", "K3")[m]


def valid(p, mask):
    d = core_degrees(mask)
    return all(p[i] + d[i] != 1 for i in range(3))


def leaf_bound(p):
    return 2 * sum(max(x - 1, 0) for x in p) + 2 * sum(
        min(p[i], p[j]) for i, j in combinations(range(3), 2)
    )


def predicted_increment(p, mask):
    typ = core_type(mask)
    g = sum(x > 0 for x in p)
    d = core_degrees(mask)

    if typ == "empty":
        return 8 if g == 1 else 14

    if typ == "edge":
        w = d.index(0)
        ends = [i for i in range(3) if i != w]
        return 10 if p[w] == 0 and min(p[i] for i in ends) == 1 else 14

    if typ == "P3":
        c = d.index(2)
        ends = [i for i in range(3) if i != c]
        if p[c] == 1:
            return 10
        if p[c] == 0 and min(p[i] for i in ends) == 1:
            return 12
        return 14

    # K3
    if g == 1:
        return 7
    if g >= 2 and any(x == 1 for x in p):
        return 10
    return 14


def main():
    checked = 0
    low_cover = Counter()
    for k in range(7, 13):
        S = k - 3
        for p0 in range(S + 1):
            for p1 in range(S - p0 + 1):
                p = (p0, p1, S - p0 - p1)
                for mask in range(8):
                    if not valid(p, mask):
                        continue
                    sigma = make_sigma(k, p, mask)
                    edges = omega_edges(sigma)
                    assert len(edges) == k * (k - 1)
                    tau = exact_vertex_cover(edges)
                    predicted = leaf_bound(p) + predicted_increment(p, mask)
                    assert tau == predicted, (k, p, mask, tau, predicted)
                    if tau <= 2 * k:
                        low_cover[(core_type(mask), sum(x > 0 for x in p))] += 1
                    checked += 1

    # Across k=7,...,12 the only low-cover no-pair states are the two
    # lopsided rays: empty-core star and triangle-star.
    assert set(low_cover) == {("empty", 1), ("K3", 1)}
    assert sum(low_cover.values()) == 36

    summary = {
        "status": "PASS_THREE_DEFECT_COMPLETE_SWITCHING_CLASSIFICATION",
        "exact_k_range": [7, 12],
        "valid_labelled_parameter_instances": checked,
        "expected_instance_count": 916,
        "table_failures": 0,
        "low_cover_types": {
            "empty_core_g1": low_cover[("empty", 1)],
            "K3_core_g1": low_cover[("K3", 1)],
        },
        "low_cover_total": sum(low_cover.values()),
        "scope": "independent finite exact audit only; universal classification remains a hand proof",
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
    }
    assert checked == 916
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
