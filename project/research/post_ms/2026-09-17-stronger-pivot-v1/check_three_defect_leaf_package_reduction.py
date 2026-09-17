#!/usr/bin/env python3
"""Finite regression for THREE_DEFECT_LEAF_PACKAGE_REDUCTION.md.

Evidence only. The formula in the note is a hand decomposition.
Uses only the Python standard library.
"""

from collections import defaultdict, deque
import json


def sigma_state(p, t):
    k = 3 + sum(p) + 2 * t
    sigma = [[0] * k for _ in range(k)]
    nxt = 3
    for i, cnt in enumerate(p):
        for _ in range(cnt):
            sigma[i][nxt] = sigma[nxt][i] = 1
            nxt += 1
    for _ in range(t):
        sigma[nxt][nxt + 1] = sigma[nxt + 1][nxt] = 1
        nxt += 2
    assert nxt == k
    return sigma


def source_code(sigma, source, target, s):
    k = len(sigma)
    sgm = sigma[target][source]
    out = 0
    for h in range(k):
        if h == source:
            val = 1 - s
        elif h == target:
            val = s ^ sgm
        else:
            val = 1 ^ s ^ sigma[source][h]
        out |= val << h
    return out


def leaf_subgraph(p, t):
    sigma = sigma_state(p, t)
    k = len(sigma)
    leaves = list(range(3, k))
    adj = defaultdict(set)
    for ai in range(len(leaves)):
        for bi in range(ai + 1, len(leaves)):
            i, j = leaves[ai], leaves[bi]
            sgm = sigma[i][j]
            for s in (0, 1):
                # source j -> i
                u = source_code(sigma, j, i, s)
                ss = s ^ sgm
                # source i -> j in the paired physical orientation
                v = 0
                for h in range(k):
                    if h == i:
                        val = 1 - ss
                    elif h == j:
                        val = s
                    else:
                        val = 1 ^ ss ^ sigma[i][h]
                    v |= val << h
                adj[u].add(v)
                adj[v].add(u)
    return adj


def exact_component_tau(adj):
    seen = set()
    total = 0
    components = 0
    for root in list(adj):
        if root in seen:
            continue
        q = deque([root])
        seen.add(root)
        comp = []
        while q:
            x = q.popleft()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        components += 1
        cset = set(comp)
        n = len(comp)
        e = sum(len(adj[x] & cset) for x in comp) // 2
        if e == n * (n - 1) // 2:
            total += n - 1
            continue

        # All remaining leaf-package components should be complete bipartite.
        side = {}
        qq = deque([comp[0]])
        side[comp[0]] = 0
        ok = True
        while qq:
            x = qq.popleft()
            for y in adj[x] & cset:
                if y not in side:
                    side[y] = 1 - side[x]
                    qq.append(y)
                elif side[y] == side[x]:
                    ok = False
        assert ok, (n, e)
        A = [x for x in comp if side[x] == 0]
        B = [x for x in comp if side[x] == 1]
        assert e == len(A) * len(B), (n, e, len(A), len(B))
        total += min(len(A), len(B))
    return total, components


def B_formula(p):
    return (
        2 * sum(max(x - 1, 0) for x in p)
        + 2 * sum(min(p[i], p[j]) for i in range(3) for j in range(i + 1, 3))
    )


def L_formula(p, t):
    B = B_formula(p)
    if t == 0:
        return B
    g = sum(x > 0 for x in p)
    return B + 4 * t * g + 2 * t * (t - 1) + 1


def main():
    checked = 0
    max_k = 0
    # Exhaustive attachment triples with S<=12 and t<=5.
    for S in range(13):
        for p0 in range(S + 1):
            for p1 in range(S - p0 + 1):
                p = (p0, p1, S - p0 - p1)
                for t in range(6):
                    k = 3 + S + 2 * t
                    if k < 4:
                        continue
                    adj = leaf_subgraph(p, t)
                    got, _ = exact_component_tau(adj)
                    exp = L_formula(p, t)
                    assert got == exp, (p, t, got, exp)
                    checked += 1
                    max_k = max(max_k, k)

    # Independently replay the finite-width consequences of L<=2k.
    for S in range(41):
        for p0 in range(S + 1):
            for p1 in range(S - p0 + 1):
                p = tuple(sorted((p0, p1, S - p0 - p1)))
                g = sum(x > 0 for x in p)
                x, y, z = p
                for t in range(8):
                    k = 3 + S + 2 * t
                    survives = L_formula(p, t) <= 2 * k
                    if t == 0:
                        predicted = (
                            g == 1
                            or (g == 2 and y <= 5)
                            or (g == 3 and ((x == 1 and y <= 4) or (x == 2 and y == 2)))
                        )
                    elif t == 1:
                        predicted = g == 0 or g == 1 or (g == 2 and y <= 2)
                    elif t == 2:
                        predicted = g in (0, 1)
                    elif t == 3:
                        predicted = g == 0
                    else:
                        predicted = False
                    assert survives == predicted, (p, t, survives, predicted, L_formula(p, t), 2 * k)

    summary = {
        "status": "PASS_THREE_DEFECT_LEAF_PACKAGE_REDUCTION",
        "exact_component_instances": checked,
        "attachment_sum_range": [0, 12],
        "isolated_pair_range": [0, 5],
        "largest_exact_k": max_k,
        "finite_width_replay_attachment_sum_range": [0, 40],
        "finite_width_replay_isolated_pair_range": [0, 7],
        "formula": "B=2 sum(p_i-1)_+ + 2 sum min(p_i,p_j); L=B for t=0, else B+4tg+2t(t-1)+1",
        "scope": "finite regression evidence only; universal formula is hand decomposition",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
