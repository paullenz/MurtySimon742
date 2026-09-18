#!/usr/bin/env python3
"""Finite regression for COMPLETE_ROW_GLOBAL_NORMAL_FORM.md.

Evidence only. The structural lemmas in the note are hand arguments.
Uses only the Python standard library.
"""

from functools import lru_cache
import json
import math


def zero_core_edges(p):
    """Matched zero-signing core: Q and Q' are two disjoint p-cliques."""
    out = set()
    for side in (0, 1):
        for i in range(p):
            for j in range(i + 1, p):
                out.add(((i, side), (j, side)))
    return out


def selected_row_graph(p, mask):
    """K_z after selecting Q/Q' endpoints according to Boolean mask."""
    out = set()
    for i in range(p):
        for j in range(i + 1, p):
            if ((mask >> i) & 1) == ((mask >> j) & 1):
                out.add((i, j))
    return out


def row_singleton_edges(p, mask):
    K = selected_row_graph(p, mask)
    out = []
    for i in range(p):
        A = 0
        for j in range(p):
            if i == j:
                continue
            e = (min(i, j), max(i, j))
            if e not in K:
                A |= 1 << j
        out.append((A, 1 << i))
    return out


def minimum_vertex_cover(edges):
    """Exact branch recursion on a small graph whose vertices are integer codes."""
    forced = set()
    es = set()
    for u, v in edges:
        if u == v:
            forced.add(u)
        else:
            es.add(tuple(sorted((u, v))))

    if forced:
        es = {e for e in es if e[0] not in forced and e[1] not in forced}

    @lru_cache(None)
    def solve(es_tuple):
        if not es_tuple:
            return 0
        es0 = list(es_tuple)
        deg = {}
        for u, v in es0:
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
        u = max(deg, key=deg.get)
        neigh = set()
        for x, y in es0:
            if x == u:
                neigh.add(y)
            elif y == u:
                neigh.add(x)

        include_u = tuple(sorted(e for e in es0 if u not in e))
        a = 1 + solve(include_u)

        include_neigh = tuple(
            sorted(e for e in es0 if e[0] not in neigh and e[1] not in neigh)
        )
        b = len(neigh) + solve(include_neigh)
        return min(a, b)

    return len(forced) + solve(tuple(sorted(es)))


def omega_edges_zero(p):
    """Preserved full-tight forced-code formula specialized to zero signing."""
    sigma = [[0] * p for _ in range(p)]
    out = []
    for i in range(p):
        for j in range(i + 1, p):
            sgm = sigma[i][j]
            for s in (0, 1):
                u = 0
                for h in range(p):
                    if h == j:
                        val = 1 - s
                    elif h == i:
                        val = s ^ sgm
                    else:
                        val = 1 ^ s ^ sigma[j][h]
                    u |= val << h

                ss = s ^ sgm
                v = 0
                for h in range(p):
                    if h == i:
                        val = 1 - ss
                    elif h == j:
                        val = s
                    else:
                        val = 1 ^ ss ^ sigma[i][h]
                    v |= val << h
                out.append((u, v))
    return out


def simple_components(edges):
    adj = {}
    for u, v in edges:
        if u == v:
            adj.setdefault(u, set())
            continue
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)

    seen = set()
    comps = []
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
        comps.append(comp)
    return comps, adj


def main():
    summary = {
        "p_range": [3, 10],
        "row_instances": 0,
        "row_failures": 0,
        "omega_failures": 0,
        "core_failures": 0,
        "arithmetic_instances": 0,
        "arithmetic_failures": 0,
    }

    for p in range(3, 11):
        core = zero_core_edges(p)
        if len(core) != 2 * math.comb(p, 2):
            summary["core_failures"] += 1

        for mask in range(1 << p):
            summary["row_instances"] += 1
            r = mask.bit_count()
            K = selected_row_graph(p, mask)
            expected_edges = math.comb(r, 2) + math.comb(p - r, 2)
            if len(K) != expected_edges:
                summary["core_failures"] += 1

            tau = minimum_vertex_cover(row_singleton_edges(p, mask))
            expected_tau = 1 if r in {0, 1, p - 1, p} else 2
            if tau != expected_tau:
                summary["row_failures"] += 1

        omega = omega_edges_zero(p)
        comps, adj = simple_components(omega)
        two_cliques = (
            len(comps) == 2
            and sorted(len(c) for c in comps) == [p, p]
            and all(all(len(adj[x]) == p - 1 for x in c) for c in comps)
        )
        if not two_cliques or minimum_vertex_cover(omega) != 2 * p - 2:
            summary["omega_failures"] += 1

    # Wider arithmetic replay of the support-surplus equivalences.
    for p in range(3, 51):
        for u in range(0, 2 * p + 6):
            for lam in range(-1, 6):
                a = 2 * p + u - lam - 1
                if a < 0:
                    continue
                summary["arithmetic_instances"] += 1
                R_A = a - (2 * p - 2)
                e1 = a <= 3 * p - 3
                e2 = u <= p + lam - 2
                e3 = R_A <= p - 1
                if R_A != u - lam + 1 or not (e1 == e2 == e3):
                    summary["arithmetic_failures"] += 1

    assert summary["row_failures"] == 0
    assert summary["omega_failures"] == 0
    assert summary["core_failures"] == 0
    assert summary["arithmetic_failures"] == 0
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
