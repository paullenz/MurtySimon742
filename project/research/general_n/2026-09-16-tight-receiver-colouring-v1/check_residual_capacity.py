#!/usr/bin/env python3
"""Adversarial checks of the new tight-receiver/capacity reduction.

Enumerates coloured tight-receiver incidence patterns, NOT original
Murty-Simon graphs. For each tight label, a partition of the d high sources
specifies which sources use the same receiver. Different tight labels use
disjoint receiver pools. This implements the globally consistent omitted
label condition in the proof. No downloaded inputs or nonstandard packages.
"""
from __future__ import annotations
from itertools import combinations, product
import json


def partitions(n: int) -> list[tuple[int, ...]]:
    """Restricted-growth words: each set partition exactly once."""
    if n < 1:
        raise ValueError("n must be positive")
    out: list[tuple[int, ...]] = []
    def visit(word: tuple[int, ...], maximum: int) -> None:
        if len(word) == n:
            out.append(word)
            return
        for value in range(maximum + 2):
            visit(word + (value,), max(maximum, value))
    visit((0,), 0)
    return out


def analyse(pattern: tuple[tuple[int, ...], ...]) -> dict:
    d = len(pattern)
    counts = [max(part) + 1 for part in pattern]
    used = sum(counts)
    # Least possible |K| from the degree/residual inequalities, allowing F[T]
    # to be complete. This is NOT a graph-realizability assertion.
    kappa_lower = max(used - count + 1 for count in counts)
    edges = [(u, v) for u, v in combinations(range(d), 2)
             if all(part[u] != part[v] for part in pattern)]
    adj = [0] * d
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    triangles = any(adj[u] & adj[v] for u, v in edges)
    assert (d - 1) * used <= d * (kappa_lower - 1)
    if edges:
        assert used >= 2 * d
        assert min(counts) >= 2
        assert kappa_lower >= 2 * d - 1
    # Each partition IS a proper colouring of Gamma. Choosing the one
    # with fewest blocks gives a stronger bound than clique-freeness.
    colour_bound = min(counts)
    assert colour_bound <= used // d
    if d >= 2:
        assert colour_bound <= (kappa_lower - 1) // (d - 1)
    smallest = pattern[counts.index(colour_bound)]
    assert all(smallest[u] != smallest[v] for u, v in edges)
    sizes = [smallest.count(c) for c in range(colour_bound)]
    assert len(edges) <= (d*d - sum(x*x for x in sizes)) // 2
    b, r = divmod(d, colour_bound)
    balanced_bound = (d*d-r*(b+1)**2-(colour_bound-r)*b*b)//2
    assert len(edges) <= balanced_bound
    if d >= 2 and kappa_lower < 3 * d - 2:
        assert used < 3 * d
        assert colour_bound <= 2
        assert not triangles
        assert len(edges) <= d * d // 4
    if triangles:
        assert min(counts) >= 3
        assert kappa_lower >= 3 * d - 2
    return dict(d=d, used=used, kappa_lower=kappa_lower,
                edges=len(edges), triangles=bool(triangles),
                proper_colours=colour_bound, balanced_edge_bound=balanced_bound)


def main() -> None:
    rows = []
    for d in range(1, 5):
        parts = partitions(d)
        count = nonempty = triangles = 0
        minimum_kappa_with_edge = None
        minimum_kappa_with_triangle = None
        for pattern in product(parts, repeat=d):
            data = analyse(pattern)
            count += 1
            if data['edges']:
                nonempty += 1
                minimum_kappa_with_edge = min(
                    minimum_kappa_with_edge or data['kappa_lower'],
                    data['kappa_lower'])
            if data['triangles']:
                triangles += 1
                minimum_kappa_with_triangle = min(
                    minimum_kappa_with_triangle or data['kappa_lower'],
                    data['kappa_lower'])
        if d >= 2:
            assert minimum_kappa_with_edge == 2*d - 1
        if d >= 3:
            assert minimum_kappa_with_triangle == 3*d - 2
        rows.append(dict(d=d, partitions=len(parts), patterns=count,
                         nonempty_disjointness_graphs=nonempty,
                         patterns_with_triangle=triangles,
                         minimum_kappa_with_edge=minimum_kappa_with_edge,
                         minimum_kappa_with_triangle=minimum_kappa_with_triangle))

    controls = []
    # The strict thresholds cannot be improved using just the incidence and
    # degree-counting reduction. These are auxiliary patterns, not graphs G.
    for d in range(2, 11):
        word = tuple([0]*(d//2) + [1]*(d-d//2))
        data = analyse(tuple([word]*d))
        assert data['used'] == 2*d
        assert data['kappa_lower'] == 2*d-1
        assert data['edges'] == d*d//4
        controls.append(dict(kind='two_group_boundary', **data))
    for d in range(3, 11):
        word = tuple([0, 1] + [2]*(d-2))
        data = analyse(tuple([word]*d))
        assert data['used'] == 3*d
        assert data['kappa_lower'] == 3*d-2
        assert data['triangles']
        controls.append(dict(kind='three_group_boundary', **data))
    # Arbitrarily many UNUSED receivers do not change the used incidence
    # pattern; a raw |M| threshold must not be substituted for |U| here.
    word = (0, 0, 0, 0)
    data = analyse(tuple([word]*4))
    assert data['used'] == 4 and data['kappa_lower'] == 4 and data['edges'] == 0
    controls.append(dict(kind='unused_receiver_control',
                         unused_receivers=100, raw_receiver_pool=104, **data))

    # The predecessor's anonymous five-set C5 control cannot be a
    # tight-label receiver system: each of five proper colourings would
    # need at least three distinct receivers, but only 13 exist.
    sets = [{0,1,2,8,9}, {3,4,5,10,11}, {0,1,2,6,7},
            {3,4,5,8,9}, {6,7,10,11,12}]
    edges = [(u,v) for u,v in combinations(range(5),2)
             if sets[u].isdisjoint(sets[v])]
    assert edges == [(0,1),(0,4),(1,2),(2,3),(3,4)]
    assert len(set().union(*sets)) == 13 < 3*5
    assert not any(all(col[u] != col[v] for u,v in edges)
                   for col in product(range(2), repeat=5))
    assert any(all(col[u] != col[v] for u,v in edges)
               for col in product(range(3), repeat=5))
    controls.append(dict(kind='historical_C5_not_tight_label_realizable',
                         d=5, used=13, chromatic_number=3,
                         required_receivers_at_least=15))

    print(json.dumps(dict(
        status='PASS_NECESSARY_RECEIVER_PATTERNS_ONLY',
        rows=rows, patterns=sum(row['patterns'] for row in rows),
        controls=controls, control_count=len(controls),
        graph_realizability='NOT_ASSERTED', catalogue_replay='NOT_RUN',
        independent_expert_review='OPEN',
        limits='Checks test the new incidence/threshold reduction, not the canonical bridge or an enumeration of original graphs.'
    ), indent=2))


if __name__ == '__main__':
    main()
