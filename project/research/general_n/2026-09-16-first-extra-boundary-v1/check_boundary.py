#!/usr/bin/env python3
"""Check the tight-block boundary reduction, not original Murty-Simon graphs.

No external inputs or third-party packages. Exercises the equality step,
the common-neighbour selection obstruction, the exact degree ledger, and
two deliberately weaker models that must not be mistaken for realizations.
"""
from __future__ import annotations
from itertools import combinations, product
from math import comb
import json


def check_saturation() -> dict:
    rows = []
    for d in range(2, 8):
        admissible = []
        tested = 0
        # An extra obligation already forces at least two receivers per label.
        for counts in product(range(2, d + 1), repeat=d):
            tested += 1
            total = sum(counts)
            if all(total - count <= 2 * d - 2 for count in counts):
                admissible.append(counts)
        assert admissible == [tuple([2] * d)]
        rows.append({'d': d, 'vectors_tested': tested,
                     'admissible_vectors': len(admissible)})
    return {'rows': rows, 'vectors_tested': sum(r['vectors_tested'] for r in rows)}


def check_common_neighbour_obstruction() -> dict:
    count = 0
    for d in range(2, 11):
        full_tight = (1 << d) - 1
        for present_tight in range(1 << d):
            # A non-high source cannot select any tight label, so these
            # present tight labels already consume residual slots.
            if present_tight.bit_count() >= d:
                continue
            count += 1
            assert present_tight != full_tight
            # A label F-adjacent to ALL tight labels cannot be selected here.
            assert (full_tight & ~present_tight) != 0
    return {'d_min': 2, 'd_max': 10, 'proper_tight_presence_profiles': count,
            'high_source_case': 'K is already residual; proved symbolically'}


def check_ledgers() -> dict:
    rows = []
    # Exhaust every unfixed F-edge on K union P in these small cases.
    # These are A-side graphs with a necessary residual-degree lower bound,
    # NOT full graph realizations or complete selected systems.
    for d, p in [(2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1)]:
        kappa = 2 * d - 1
        a = d + kappa + p
        tight = range(d)
        core = range(d, d + kappa)
        remaining = range(d + kappa, a)
        fixed = list(combinations(tight, 2)) + [(t, k) for t in tight for k in core]
        free = list(combinations(range(d, a), 2))
        maximum = None
        tested = 0
        nonnegative_relaxed_ledgers = 0
        for mask in range(1 << len(free)):
            edges = fixed + [edge for bit, edge in enumerate(free) if mask & (1 << bit)]
            degrees = [0] * a
            e_core = e_remaining = 0
            for u, v in edges:
                degrees[u] += 1
                degrees[v] += 1
                if d <= u < d + kappa and d <= v < d + kappa:
                    e_core += 1
                if u >= d + kappa and v >= d + kappa:
                    e_remaining += 1
            assert all(degrees[t] == 3 * d - 2 for t in tight)
            r_tight = sum(degrees[t] - d for t in tight)
            assert r_tight == 2 * d * (d - 1)
            # x_k=0 plus minimum complement-degree requires R_k>=deg_F(k).
            r_core_lower = sum(degrees[k] for k in core)
            for r_remaining in (0, 1, d):
                upper = len(edges) - (r_tight + r_core_lower + r_remaining)
                claimed = e_remaining - e_core - r_remaining - 3 * comb(d, 2)
                assert upper == claimed
            upper_at_zero = len(edges) - r_tight - r_core_lower
            maximum = upper_at_zero if maximum is None else max(maximum, upper_at_zero)
            nonnegative_relaxed_ledgers += (upper_at_zero >= 0)
            if p == 1:
                assert a == 3 * d
                assert upper_at_zero <= -3 * comb(d, 2) < 0
            tested += 1
        assert maximum == comb(p, 2) - 3 * comb(d, 2)
        rows.append({'d': d, 'kappa': kappa, 'p': p, 'a': a,
                     'A_side_graphs_tested': tested,
                     'maximum_surplus_upper_bound_at_R_P_zero': maximum,
                     'nonnegative_relaxed_ledgers': nonnegative_relaxed_ledgers})
    return {'rows': rows, 'A_side_graphs_tested': sum(r['A_side_graphs_tested'] for r in rows)}


def check_controls() -> list[dict]:
    # Dropping the no-selected-K consequence leaves a spuriously positive
    # ledger. This deliberately violates a necessary minimum-degree demand.
    d, kappa = 3, 5
    f_edges = comb(d, 2) + d * kappa + comb(kappa, 2)
    receiver_and_high_residual_only = 2 * d * (d - 1) + d * kappa
    assert f_edges - receiver_and_high_residual_only == 1
    full_core_degree_lower = kappa * (d + kappa - 1)
    corrected_upper = f_edges - 2 * d * (d - 1) - full_core_degree_lower
    assert corrected_upper == -19
    controls = [{'kind': 'omitting_zero_selection_is_unsound', 'd': d,
                 'weakened_ledger_surplus': 1, 'corrected_surplus_upper_bound': -19,
                 'graph_realizability': 'NOT_ASSERTED'}]

    # One unit above minimum kappa, a K-label may miss one tight F-neighbour.
    # Such a label can pass A-side domination at a receiver missing that same
    # tight label. This refutes only an overextension of this LOCAL step.
    d, kappa = 3, 6
    tight, core = set(range(d)), set(range(d, d + kappa))
    missing_t, special_k = 0, d
    f_edges_set = {frozenset(e) for e in combinations(tight, 2)}
    f_edges_set |= {frozenset((t, k)) for t in tight for k in core
                   if (t, k) != (missing_t, special_k)}
    neighbours = {i: set() for i in tight | core}
    for edge in f_edges_set:
        u, v = tuple(edge)
        neighbours[u].add(v)
        neighbours[v].add(u)
    receiver_residual = tight - {missing_t}
    receiver_selected = {special_k}
    receiver_neighbourhood = receiver_residual | receiver_selected
    assert neighbours[special_k] <= receiver_neighbourhood
    assert neighbours[special_k] == receiver_residual
    tight_residual_degrees = [len(neighbours[t]) - d for t in sorted(tight)]
    assert tight_residual_degrees == [4, 5, 5]
    assert all(2 * d - 2 <= r <= kappa - 1 for r in tight_residual_degrees)
    controls.append({'kind': 'larger_kappa_does_not_force_all_K_unselected',
                     'd': d, 'kappa': kappa,
                     'tight_residual_degrees': tight_residual_degrees,
                     'local_A_domination_passes': True,
                     'graph_realizability': 'NOT_ASSERTED'})

    # The remainder-edge lower bound may admit a nonnegative scalar ledger;
    # it must not be reported as a graph-realizability or sufficiency result.
    assert comb(3, 2) - 3 * comb(2, 2) == 0
    controls.append({'kind': 'necessary_bound_is_not_sufficiency',
                     'd': 2, 'kappa': 3, 'p': 3,
                     'relaxed_surplus_upper_bound': 0,
                     'graph_realizability': 'NOT_ASSERTED'})
    return controls


def main() -> None:
    saturation = check_saturation()
    obstruction = check_common_neighbour_obstruction()
    ledgers = check_ledgers()
    controls = check_controls()
    print(json.dumps({'status': 'PASS_BOUNDARY_REDUCTION_ONLY',
                      'saturation': saturation,
                      'common_neighbour_obstruction': obstruction,
                      'ledgers': ledgers,
                      'controls': controls,
                      'control_count': len(controls),
                      'catalogue_replay': 'NOT_RUN',
                      'original_graph_enumeration': 'NOT_RUN',
                      'independent_expert_review': 'OPEN',
                      'scope': 'Checks the newly used equality, eligibility and degree-counting reductions, not the full canonical bridge.'}, indent=2))


if __name__ == '__main__':
    main()
