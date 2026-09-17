#!/usr/bin/env python3
"""Finite regression for TWO_DEFECT_COMPLETE_SWITCHING_CLASSIFICATION.md.

Evidence only; the universal statements in the note are hand proofs.
Uses only the Python standard library.
"""

from functools import lru_cache
import json


def omega_edges(k, p, q, t, epsilon):
    # Exceptional coordinates a=0,b=1; P then Q then t matched leaf pairs.
    sigma = [[0] * k for _ in range(k)]
    z = 2
    for _ in range(p):
        sigma[0][z] = sigma[z][0] = 1
        z += 1
    for _ in range(q):
        sigma[1][z] = sigma[z][1] = 1
        z += 1
    for _ in range(t):
        sigma[z][z + 1] = sigma[z + 1][z] = 1
        z += 2
    assert z == k
    if epsilon:
        sigma[0][1] = sigma[1][0] = 1

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


def valid_tuple(k, p, q, t, epsilon):
    return (
        p + q + 2 * t == k - 2
        and p + epsilon != 1
        and q + epsilon != 1
    )


def tuples_for_k(k):
    for epsilon in (0, 1):
        for p in range(k - 1):
            for q in range(k - 1 - p):
                rem = k - 2 - p - q
                if rem < 0 or rem % 2:
                    continue
                t = rem // 2
                if valid_tuple(k, p, q, t, epsilon):
                    yield p, q, t, epsilon


def exact_tau_formula(k, p, q, t, epsilon):
    assert valid_tuple(k, p, q, t, epsilon)
    if t == 0:
        if epsilon == 0:
            if min(p, q) == 0:
                return 2 * k - 1
            return 2 * k - 3 + 2 * min(p, q)
        return 2 * k - 2 + 2 * min(p, q)

    if p == q == 0:
        assert epsilon == 0
        return 2 * t * t + 2 * t + 3

    a = 2 * max(p - 1, 0) + 2 * max(q - 1, 0) + 2 * min(p, q)
    return a + 2 * t * t + 6 * t + 6


def simple_components(edges):
    adj = {}
    for u, v in edges:
        if u == v:
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
        verts = []
        while stack:
            x = stack.pop()
            verts.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        vset = set(verts)
        ce = set()
        for x in verts:
            for y in adj[x]:
                if y in vset and x < y:
                    ce.add((x, y))
        comps.append((verts, tuple(sorted(ce))))
    return comps


def mvc_component(verts, edges):
    idx = {v: i for i, v in enumerate(verts)}
    e0 = tuple(sorted((min(idx[u], idx[v]), max(idx[u], idx[v])) for u, v in edges))

    @lru_cache(None)
    def solve(es):
        if not es:
            return 0
        deg = {}
        for u, v in es:
            deg[u] = deg.get(u, 0) + 1
            deg[v] = deg.get(v, 0) + 1
        u = max(deg, key=deg.get)
        neigh = {v if x == u else x for x, v in es if x == u or v == u}

        # Include u.
        e1 = tuple(e for e in es if u not in e)
        v1 = 1 + solve(e1)

        # Exclude u, hence include all neighbours of u.
        e2 = tuple(e for e in es if e[0] not in neigh and e[1] not in neigh)
        v2 = len(neigh) + solve(e2)
        return min(v1, v2)

    return solve(e0)


def exact_tau_by_graph(k, p, q, t, epsilon):
    edges = omega_edges(k, p, q, t, epsilon)
    return sum(mvc_component(vs, es) for vs, es in simple_components(edges))


def M(n):
    return ((n - 1) * (n - 1)) // 4 + 1


def lopsided_arithmetic(k):
    a = 2 * k
    r = k * (k + 1)
    h = r // (k - 1)
    f_bound = (h * h) // 4 + 8 * k
    delta_bound = r - f_bound
    n = 4 * k + 1
    base = 2 * k * (n - 2 * k)
    needed = base - M(n)
    return delta_bound, needed


def main():
    tuple_checks = 0
    by_k = {}
    for k in range(5, 11):
        count = 0
        for p, q, t, epsilon in tuples_for_k(k):
            got = exact_tau_by_graph(k, p, q, t, epsilon)
            exp = exact_tau_formula(k, p, q, t, epsilon)
            assert got == exp, (k, p, q, t, epsilon, got, exp)
            count += 1
            tuple_checks += 1
        by_k[str(k)] = count

    # Formula-level scan of the density reduction.
    survivors = set()
    formula_tuples = 0
    for k in range(5, 101):
        for p, q, t, epsilon in tuples_for_k(k):
            formula_tuples += 1
            tau = exact_tau_formula(k, p, q, t, epsilon)
            if tau <= 2 * k:
                if t == 0 and epsilon == 0 and min(p, q) == 0:
                    survivors.add("isolated_star")
                elif t == 0 and epsilon == 1 and min(p, q) == 1:
                    survivors.add("adjacent_lopsided")
                else:
                    raise AssertionError((k, p, q, t, epsilon, tau))

    threshold = None
    records = []
    for k in range(5, 5001):
        delta, need = lopsided_arithmetic(k)
        records.append(delta >= need)
    for k in range(5, 5001):
        if all(records[k - 5 :]):
            threshold = k
            break

    assert threshold == 14
    assert survivors == {"isolated_star", "adjacent_lopsided"}

    summary = {
        "status": "PASS_TWO_DEFECT_COMPLETE_SWITCHING_CLASSIFICATION",
        "exact_graph_tau_replay_k_range": [5, 10],
        "exact_graph_tuple_checks": tuple_checks,
        "tuple_counts_by_k": by_k,
        "formula_density_scan_k_range": [5, 100],
        "formula_tuples_scanned": formula_tuples,
        "only_tau_le_2k_normal_forms": ["isolated_star", "adjacent_lopsided"],
        "adjacent_lopsided_exact_tau": "2k",
        "adjacent_lopsided_F_closure_threshold": 14,
        "complete_two_defect_eventual_threshold": 14,
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism remains outside theorem scope",
        "scope": "finite regression evidence only; universal cover formulas and F-separation claims are hand proofs",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
