#!/usr/bin/env python3
"""Proof-producing finite audit for the four-defect no-pair core lemma.

This is deliberately not the infinite argument.  The hand note proves the
leaf-package decomposition and the ray-extension lemma.  What remains is a
finite four-coordinate exceptional-core lemma.  For every valid labelled
4-vertex core and every bounded base attachment pattern, this script builds
the residual core-witness graph directly from the forced orientation-code
formula, deletes every code used by the leaf-leaf package, and constructs an
explicit vertex-disjoint matching by a deterministic greedy rule.

The matching sizes certified here are exactly the constants used in the hand
argument.  No numerical extrapolation in the unbounded pendant parameter is
used.
"""

from itertools import combinations
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
                out.append((u, v, i, j, s))
    return out


def make_state(p, mask):
    k = 4 + sum(p)
    sigma = [[0] * k for _ in range(k)]
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            sigma[i][j] = sigma[j][i] = 1
    cur = 4
    groups = []
    for i, pi in enumerate(p):
        group = []
        for _ in range(pi):
            sigma[i][cur] = sigma[cur][i] = 1
            group.append(cur)
            cur += 1
        groups.append(group)
    return sigma, groups


def valid_core(p, mask):
    deg = [0] * 4
    for bit, (i, j) in enumerate(CORE_PAIRS):
        if (mask >> bit) & 1:
            deg[i] += 1
            deg[j] += 1
    return all(p[i] + deg[i] != 1 for i in range(4))


def core_witness_edges(p, mask):
    sigma, groups = make_state(p, mask)
    all_edges = omega_edges(sigma)
    leaves = [x for group in groups for x in group]
    leaf_pairs = set(combinations(leaves, 2))

    leaf_vertices = set()
    for u, v, i, j, _ in all_edges:
        if (i, j) in leaf_pairs:
            leaf_vertices.add(u)
            leaf_vertices.add(v)

    reps = {group[0] for group in groups if group}
    edges = set()
    origins = {}
    for u, v, i, j, s in all_edges:
        keep = (i < 4 and j < 4) or (i < 4 and j in reps) or (j < 4 and i in reps)
        if not keep or u in leaf_vertices or v in leaf_vertices or u == v:
            continue
        e = tuple(sorted((u, v)))
        edges.add(e)
        origins.setdefault(e, (i, j, s))
    return edges, origins


def greedy_matching(edges):
    # Deterministic proof witness: repeatedly match a minimum-degree
    # nonisolated vertex to a minimum-degree neighbour.
    adj = {}
    for u, v in edges:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    chosen = []
    while True:
        live = [u for u in adj if adj[u]]
        if not live:
            break
        u = min(live, key=lambda x: (len(adj[x]), x))
        v = min(adj[u], key=lambda x: (len(adj[x]), x))
        chosen.append(tuple(sorted((u, v))))
        for x in list(adj.get(u, ())):
            adj[x].discard(u)
        for x in list(adj.get(v, ())):
            adj[x].discard(v)
        adj[u].clear()
        adj[v].clear()
    return chosen


def patterns():
    out = [("g2_y1", (0, 0, 1, 2), 12)]
    for y in range(2, 7):
        out.append((f"g2_y{y}", (0, 0, y, max(y, 3)), 14))
    for x, y in ((1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3)):
        out.append((f"g3_x{x}_y{y}", (0, x, y, max(y, 2)), 20))
    for w, x, y in ((1,1,1),(1,1,2),(1,1,3)):
        out.append((f"g4_{w}_{x}_{y}", (w, x, y, max(y, 2)), 18))
    return out


def main():
    rows = []
    total = 0
    for name, p, target in patterns():
        valid = 0
        minimum = None
        for mask in range(64):
            if not valid_core(p, mask):
                continue
            valid += 1
            edges, origins = core_witness_edges(p, mask)
            matching = greedy_matching(edges)
            # Explicit certificate checks.
            used = set()
            for e in matching:
                assert e in edges
                u, v = e
                assert u not in used and v not in used
                used.add(u)
                used.add(v)
                assert e in origins
            assert len(matching) >= target, (name, p, mask, len(matching), target)
            minimum = len(matching) if minimum is None else min(minimum, len(matching))
            total += 1
        rows.append({
            "name": name,
            "base_attachment": list(p),
            "valid_labelled_cores": valid,
            "target_matching": target,
            "minimum_greedy_matching": minimum,
        })

    summary = {
        "status": "PASS_FOUR_DEFECT_NO_PAIR_CORE_MATCHING_CERTIFICATES",
        "labelled_core_instances": total,
        "rows": rows,
        "ray_extension": "hand lemma in accompanying note; no z extrapolation is performed here",
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
