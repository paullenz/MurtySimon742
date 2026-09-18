#!/usr/bin/env python3
"""Exact finite audit for SIX_DEFECT_LOPSIDED_SUPPORT_EXCLUSION.md.

The infinite z-direction is handled by the hand coordinatewise residual
monotonicity lemma.  This checker audits the finite six-vertex exceptional
cores at z=3 and the explicit all-z decomposition of the sole dangerous
rooted core.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations
import json

D = 6
ROOT = 5
CORE_PAIRS = list(combinations(range(D), 2))
DANGEROUS = 27551


def make_state(z, mask):
    k = D + z
    sigma = [[0] * k for _ in range(k)]
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            sigma[i][j] = sigma[j][i] = 1
    for x in range(D, k):
        sigma[ROOT][x] = sigma[x][ROOT] = 1
    return sigma


def valid_core(z, mask):
    deg = [0] * D
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            deg[i] += 1
            deg[j] += 1
    deg[ROOT] += z
    return all(x != 1 for x in deg)


def omega_edges(sigma):
    """Physical orientation-code edges, retaining parallel multiplicity."""
    k = len(sigma)
    rows = []
    for i in range(k):
        m = 0
        for j in range(k):
            if sigma[i][j]:
                m |= 1 << j
        rows.append(m)
    allmask = (1 << k) - 1
    out = []
    for i in range(k):
        for j in range(i + 1, k):
            sgm = sigma[i][j]
            u = (allmask ^ rows[j]) ^ (1 << i)
            v = ((allmask ^ rows[i]) if sgm == 0 else rows[i]) ^ (1 << j)
            out.append((u, v, i, j))
            out.append((allmask ^ u, allmask ^ v, i, j))
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


def leaf_vertices(z, mask):
    edges = omega_edges(make_state(z, mask))
    leaves = list(range(D, D + z))
    leaf_pairs = set(combinations(leaves, 2))
    out = set()
    for u, v, i, j in edges:
        if (i, j) in leaf_pairs:
            out.add(u)
            out.add(v)
    return out


def residual_tau(z, mask):
    edges = omega_edges(make_state(z, mask))
    lv = leaf_vertices(z, mask)
    return exact_vertex_cover([(u, v) for u, v, _, _ in edges if u not in lv and v not in lv])


def full_tau(z, mask):
    return exact_vertex_cover([(u, v) for u, v, _, _ in omega_edges(make_state(z, mask))])


def canonical_rooted(mask):
    edges = {CORE_PAIRS[b] for b in range(len(CORE_PAIRS)) if (mask >> b) & 1}
    others = [i for i in range(D) if i != ROOT]
    reps = []
    for perm in permutations(others):
        mp = {ROOT: ROOT}
        mp.update(dict(zip(others, perm)))
        moved = {tuple(sorted((mp[i], mp[j]))) for i, j in edges}
        m = 0
        for b, e in enumerate(CORE_PAIRS):
            if e in moved:
                m |= 1 << b
        reps.append(m)
    return min(reps)


def component_signature(z, mask):
    mult = Counter(tuple(sorted((u, v))) for u, v, _, _ in omega_edges(make_state(z, mask)))
    adj = defaultdict(set)
    for u, v in mult:
        if u != v:
            adj[u].add(v)
            adj[v].add(u)
    seen = set()
    sig = []
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
        es = [e for e in mult if e[0] in C and e[1] in C]
        degs = tuple(sorted(len(adj[x]) for x in C))
        vc = exact_vertex_cover(es)
        sig.append((len(C), len(es), sum(mult[e] for e in es), degs, vc))
    return Counter(sig)


def main():
    z = 3
    k = D + z
    B = 2 * (z - 1)
    valid = 0
    dangerous = []
    full_min_excess = None
    for mask in range(1 << len(CORE_PAIRS)):
        if not valid_core(z, mask):
            continue
        valid += 1
        r = residual_tau(z, mask)
        if B + r <= 2 * k:
            dangerous.append(mask)
        ex = full_tau(z, mask) - 2 * k
        full_min_excess = ex if full_min_excess is None else min(full_min_excess, ex)
    assert valid == 15572, valid
    assert len(dangerous) == 15, len(dangerous)
    assert {canonical_rooted(m) for m in dangerous} == {DANGEROUS}
    assert full_min_excess == 2, full_min_excess

    formula_rows = []
    for z in range(2, 9):
        k = D + z
        tau = full_tau(z, DANGEROUS)
        assert tau == 2 * k + 2, (z, tau, 2*k+2)
        sig = component_signature(z, DANGEROUS)
        # 4 doubled K2; 2 K_{z+1}; 8 K_{1,z+2}; one balanced double-star.
        expected = Counter()
        expected[(2, 1, 2, (1, 1), 1)] = 4
        expected[(z+1, z*(z+1)//2, z*(z+1)//2, tuple([z]*(z+1)), z)] = 2
        expected[(z+3, z+2, z+2, tuple([1]*(z+2)+[z+2]), 1)] = 8
        expected[(2*z+4, 2*z+3, 2*z+6, tuple([1]*(2*z+2)+[z+2,z+2]), 2)] = 1
        assert sig == expected, (z, sig, expected)
        formula_rows.append({"z": z, "k": k, "tau": tau, "excess": tau-2*k})

    # The finite lower-order support obstruction.
    empty_tau = full_tau(2, 0)
    assert empty_tau == 16 == 2 * (D + 2)

    summary = {
        "status": "PASS_SIX_DEFECT_LOPSIDED_SUPPORT_EXCLUSION",
        "threshold_k": 9,
        "z3_valid_labelled_cores": valid,
        "z3_additive_dangerous_labelled_cores": len(dangerous),
        "z3_dangerous_rooted_classes": [DANGEROUS],
        "dangerous_core_description": "K2 join 2K2, with one K2 vertex the pendant root",
        "z3_full_min_tau_minus_2k": full_min_excess,
        "dangerous_formula_rows": formula_rows,
        "boundary_z2_empty_core_tau_minus_2k": empty_tau - 2 * (D + 2),
        "trust_boundary": "finite exact six-vertex core audit plus hand coordinatewise residual monotonicity; external review open"
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
