#!/usr/bin/env python3
"""Standalone exhaustive regression for abstract crossing-dominance exactness."""

from itertools import product
import json


def hall_capacity(S, n, P, arcs):
    y = [sum((u, w) in arcs for u in S) for w in range(n)]
    H = sum(min(P[w], y[w]) for w in range(n))
    return H, y


def rearranged_capacity(S, n, P, arcs, layers):
    _, y = hall_capacity(S, n, P, arcs)
    U = 0
    for L in layers:
        top = max([P[w] for w in L] + [y[w] for w in L])
        for k in range(1, top + 1):
            alpha = sum(P[w] >= k for w in L)
            beta = sum(y[w] >= k for w in L)
            U += min(alpha, beta)
    return U


def crossing_dominance_ok(n, P, arcs, layers):
    for L in layers:
        for x in L:
            for y in L:
                if P[x] >= P[y]:
                    continue
                if (x, y) not in arcs or (y, x) not in arcs:
                    return False
                for z in range(n):
                    if z in (x, y):
                        continue
                    if (z, x) in arcs and (z, y) not in arcs:
                        return False
                    if (x, z) in arcs and (y, z) not in arcs:
                        return False
    return True


def scan(n, layers, capacity_values, demand_vectors):
    pairs = [(u, w) for u in range(n) for w in range(n) if u != w]
    layer_of = {v: i for i, L in enumerate(layers) for v in L}
    out = {
        "n": n,
        "layers": [list(L) for L in layers],
        "capacity_values": list(capacity_values),
        "valid_capacity_digraph_profiles": 0,
        "valid_demand_instances": 0,
        "pointwise_gap_instances": 0,
        "pointwise_gap_source_sets": 0,
        "mincut_mismatches": 0,
    }

    for P in product(capacity_values, repeat=n):
        for bits in range(1 << len(pairs)):
            arcs = {pairs[i] for i in range(len(pairs)) if (bits >> i) & 1}
            if not crossing_dominance_ok(n, P, arcs, layers):
                continue
            out["valid_capacity_digraph_profiles"] += 1

            for demands in demand_vectors:
                out["valid_demand_instances"] += 1
                min_h = 10**9
                min_u = 10**9
                has_gap = False

                for mask in range(1 << n):
                    S = [i for i in range(n) if (mask >> i) & 1]
                    H, _ = hall_capacity(S, n, P, arcs)
                    U = rearranged_capacity(S, n, P, arcs, layers)
                    D = sum(demands[layer_of[u]] for u in S)
                    min_h = min(min_h, H - D)
                    min_u = min(min_u, U - D)
                    if U > H:
                        has_gap = True
                        out["pointwise_gap_source_sets"] += 1

                if has_gap:
                    out["pointwise_gap_instances"] += 1
                if min_h != min_u:
                    out["mincut_mismatches"] += 1
                    raise AssertionError(
                        f"minimum mismatch P={P} demands={demands} exact={min_h} rearranged={min_u}"
                    )
    return out


def main():
    one_layer = scan(
        n=4,
        layers=((0, 1, 2, 3),),
        capacity_values=(0, 1, 2),
        demand_vectors=((d,) for d in (0, 1, 2)),
    )
    two_layer = scan(
        n=4,
        layers=((0, 1), (2, 3)),
        capacity_values=(0, 1),
        demand_vectors=product((0, 1, 2), repeat=2),
    )
    result = {"result": "PASS", "one_layer": one_layer, "two_layer": two_layer}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
