#!/usr/bin/env python3
"""Finite boundary audit for MINIMUM_DEFECT_TWIN_PACKAGE_COLLAPSE.md.

Requires networkx for graph_atlas_g() and maximum matching.

The hand theorem reduces all minimum defects d>=7 to the pure lopsided state,
then closes d>=9 structurally.  This checker supplies the two small remaining
rooted-core certificates:

* d=7: all rooted seven-vertex exceptional cores at z=3; leaf package plus
  residual cover is already >2k.  Ray monotonicity propagates to z>3.
* d=8: the only analytically nontrivial lopsided subcase has seven distinct
  open neighbourhoods among Q=E\{r}; enumerate every seven-vertex Q graph
  from the NetworkX atlas and every root-neighbour mask, and verify the
  quotient residual Q-Q graph has vertex-cover number at least three.

This is an internal proof-producing certificate, not external review.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
import json
import networkx as nx


def mask_from_edges(d, edges):
    pairs = list(combinations(range(d), 2))
    idx = {e: i for i, e in enumerate(pairs)}
    out = 0
    for a, b in edges:
        if a > b:
            a, b = b, a
        out |= 1 << idx[(a, b)]
    return out


def make_rows_lopsided(d, z, edges, root=None):
    if root is None:
        root = d - 1
    k = d + z
    rows = [0] * k
    for i, j in edges:
        rows[i] |= 1 << j
        rows[j] |= 1 << i
    for leaf in range(d, k):
        rows[root] |= 1 << leaf
        rows[leaf] |= 1 << root
    return rows


def omega_edges(rows):
    k = len(rows)
    allmask = (1 << k) - 1
    out = []
    for i in range(k):
        ri = rows[i]
        for j in range(i + 1, k):
            s = (ri >> j) & 1
            u = (allmask ^ rows[j]) ^ (1 << i)
            v = ((allmask ^ ri) if s == 0 else ri) ^ (1 << j)
            out.append((u, v))
            out.append((allmask ^ u, allmask ^ v))
    return out


def leaf_package_vertices(rows, d):
    k = len(rows)
    allmask = (1 << k) - 1
    leaves = range(d, k)
    out = set()
    for i, j in combinations(leaves, 2):
        ri = rows[i]
        s = (ri >> j) & 1
        u = (allmask ^ rows[j]) ^ (1 << i)
        v = ((allmask ^ ri) if s == 0 else ri) ^ (1 << j)
        out.update((u, v, allmask ^ u, allmask ^ v))
    return out


def residual_edges(rows, d):
    lv = leaf_package_vertices(rows, d)
    return [(u, v) for u, v in omega_edges(rows) if u not in lv and v not in lv]


def exact_vertex_cover(edges):
    simple = set(tuple(sorted(e)) for e in edges)
    forced = {u for u, v in simple if u == v}
    simple = {
        (u, v) for u, v in simple
        if u != v and u not in forced and v not in forced
    }
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
        C = set(comp)
        es = tuple(sorted(e for e in simple if e[0] in C and e[1] in C))

        @lru_cache(None)
        def solve(cur):
            if not cur:
                return 0
            degree = Counter()
            nbr = defaultdict(set)
            for a, b in cur:
                degree[a] += 1
                degree[b] += 1
                nbr[a].add(b)
                nbr[b].add(a)
            u = max(degree, key=degree.get)
            take_u = 1 + solve(tuple(e for e in cur if u not in e))
            N = nbr[u]
            take_N = len(N) + solve(tuple(
                e for e in cur if e[0] not in N and e[1] not in N
            ))
            return min(take_u, take_N)

        total += solve(es)
    return total


def matching_size(edges):
    G = nx.Graph()
    G.add_edges_from((u, v) for u, v in edges if u != v)
    return len(nx.algorithms.matching.max_weight_matching(G, maxcardinality=True))


def relabel_rooted_graph(G, root, d):
    others = [v for v in G.nodes() if v != root]
    mp = {v: i for i, v in enumerate(others)}
    mp[root] = d - 1
    return [(mp[u], mp[v]) for u, v in G.edges()]


def d7_audit(atlas7):
    d = 7
    z = 3
    k = d + z
    leaf_cover = 2 * (z - 1)
    target_residual = 2 * k - leaf_cover + 1  # 17
    valid = 0
    matching_short = []
    min_matching = None
    for gi, G in enumerate(atlas7):
        for root in G.nodes():
            if any(G.degree(v) == 1 for v in G.nodes() if v != root):
                continue
            valid += 1
            edges = relabel_rooted_graph(G, root, d)
            rows = make_rows_lopsided(d, z, edges)
            re = residual_edges(rows, d)
            nu = matching_size(re)
            min_matching = nu if min_matching is None else min(min_matching, nu)
            if nu < target_residual:
                tau = exact_vertex_cover(re)
                matching_short.append((gi, root, nu, tau))

    assert valid == 4376, valid
    assert len(matching_short) == 15, len(matching_short)
    assert min_matching == 15, min_matching
    min_tau_short = min(row[3] for row in matching_short)
    assert min_tau_short == 19, min_tau_short
    min_margin = leaf_cover + min_tau_short - 2 * k
    assert min_margin == 3, min_margin
    return {
        "valid_rooted_cores": valid,
        "z_base": z,
        "matching_target": target_residual,
        "matching_short_cases": len(matching_short),
        "min_matching": min_matching,
        "min_exact_residual_cover_among_short_cases": min_tau_short,
        "min_leaf_plus_residual_minus_2k": min_margin,
    }


def q_rows_from_core(d, edges):
    rows = [0] * d
    for a, b in edges:
        rows[a] |= 1 << b
        rows[b] |= 1 << a
    return rows


def bad_pair_count(d, edges, root):
    rows = q_rows_from_core(d, edges)
    Q = [x for x in range(d) if x != root]
    centres = {(1 << root) | (1 << u) for u in Q}
    b = 0
    for x, y in combinations(Q, 2):
        if (rows[x] ^ (1 << y)) in centres or (rows[y] ^ (1 << x)) in centres:
            b += 1
    return b


def quotient_residual_edges(d, edges, root):
    rows = q_rows_from_core(d, edges)
    Q = [x for x in range(d) if x != root]
    centres = {(1 << root) | (1 << u) for u in Q}
    out = []
    for x, y in combinations(Q, 2):
        cx = rows[x] ^ (1 << y)
        cy = rows[y] ^ (1 << x)
        if cx in centres or cy in centres:
            continue
        out.append((cx, cy))
    return out


def cover_at_most_two(edges):
    """Return 0/1/2 if that cover size works; return 3 if tau>=3.

    Loops force their incident vertex.
    """
    simple = set(tuple(sorted(e)) for e in edges)
    forced = {u for u, v in simple if u == v}
    if len(forced) >= 3:
        return 3
    rem = [
        e for e in simple
        if e[0] != e[1] and e[0] not in forced and e[1] not in forced
    ]
    if not rem:
        return len(forced)
    if len(forced) == 2:
        return 3
    if len(forced) == 1:
        common = set(rem[0])
        for e in rem[1:]:
            common &= set(e)
        return 2 if common else 3

    common = set(rem[0])
    for e in rem[1:]:
        common &= set(e)
    if common:
        return 1

    a, b = rem[0]
    for u in (a, b):
        left = [e for e in rem if u not in e]
        if not left:
            return 1
        common = set(left[0])
        for e in left[1:]:
            common &= set(e)
        if common:
            return 2
    return 3


def d8_all_distinct_audit(atlas7):
    """Enumerate Q on seven vertices plus all 2^7 root-neighbour masks."""
    d = 8
    root = 7
    valid_all_distinct = 0
    max_bad = 0
    cover_le_two = 0

    for G in atlas7:
        degH = [G.degree(i) for i in range(7)]
        for root_mask in range(1 << 7):
            # Q vertices carry no pendant leaves, hence may not have total degree 1.
            if any(degH[x] + ((root_mask >> x) & 1) == 1 for x in range(7)):
                continue
            edges = list(G.edges())
            for x in range(7):
                if (root_mask >> x) & 1:
                    edges.append((x, root))
            rows = q_rows_from_core(d, edges)
            if len({rows[x] for x in range(7)}) != 7:
                continue
            valid_all_distinct += 1
            max_bad = max(max_bad, bad_pair_count(d, edges, root))
            qr = quotient_residual_edges(d, edges, root)
            if cover_at_most_two(qr) <= 2:
                cover_le_two += 1

    assert valid_all_distinct == 66513, valid_all_distinct
    assert max_bad == 9, max_bad
    assert cover_le_two == 0, cover_le_two
    return {
        "valid_all_distinct_rooted_cores": valid_all_distinct,
        "max_absorbed_Q_pair_count": max_bad,
        "quotient_residual_cover_le_2_cases": cover_le_two,
        "certified_quotient_residual_cover_lower_bound": 3,
        "certified_full_complementary_residual_cover_lower_bound": 6,
    }


def main():
    atlas7 = [G for G in nx.graph_atlas_g() if G.number_of_nodes() == 7]
    assert len(atlas7) == 1044
    summary = {
        "status": "PASS_D7_D8_LOPSIDED_BOUNDARY",
        "atlas_unlabelled_graphs_on_7_vertices": len(atlas7),
        "d7": d7_audit(atlas7),
        "d8_all_distinct": d8_all_distinct_audit(atlas7),
        "trust_boundary": (
            "finite rooted-core certificate using NetworkX graph atlas; "
            "unbounded propagation/reduction is supplied by hand structural lemmas"
        ),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
