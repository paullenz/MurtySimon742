#!/usr/bin/env python3
"""Exact internal checks of a necessary shared-bundle resource model.

No original-graph enumeration or canonical-bridge validation is performed.
Python enumerates activated bundle subsets; C++ enumerates incoming counts.
"""
from __future__ import annotations
import base64
import gzip
import hashlib
import itertools as it
import json
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path

PREDECESSOR = '888e24fe285db0363a2670370e933963f937a02b'
OPTIONS = tuple(it.product((2, 3), (1, 2), range(4)))
GAPS = (-1, 0, 2)
RADII = tuple(range(1, 7))


def envelope(groups: tuple[tuple[int, int, int], ...], r: int, gap: int) -> int:
    """Maximize monitored incoming count subject to the proved local cost."""
    cap = max(0, r + gap)
    best = 0
    for mask in range(1 << len(groups)):
        mates = external = occurrences = 0
        for t, (g, m, theta) in enumerate(groups):
            if mask & (1 << t):
                mates += g - 1
                external = max(external, theta)
                occurrences += m
        if mates + external <= r:
            best = max(best, min(cap, occurrences))
    return best


def domain():
    for n in range(1, 4):
        for groups in it.product(OPTIONS, repeat=n):
            for gap in GAPS:
                for r in RADII:
                    yield groups, r, gap


def mate_occurrence_checks() -> dict:
    tested = feasible = 0
    by_g = {}
    for g in range(2, 5):
        local = 0
        for m in (1, 2):
            for n_o in range(1, 4):
                for targets in it.product(range(-1, n_o), repeat=g*m):
                    tested += 1
                    labels_at = [set() for _ in range(n_o)]
                    for pos, v in enumerate(targets):
                        if v >= 0:
                            labels_at[v].add(pos//m)
                    # Distinct label types within one full bundle cannot share.
                    if any(len(s) > 1 for s in labels_at):
                        continue
                    feasible += 1
                    local += 1
                    escaped = targets.count(-1)
                    eps = min(g-1, escaped//m)
                    for i in range(g):
                        residual_receivers = {v for v, labels in enumerate(labels_at)
                                              if any(j != i for j in labels)}
                        assert len(residual_receivers) >= g-1-eps
                    # All label types with no O-destination consume m escapes.
                    lost = sum(all(v < 0 for v in targets[i*m:(i+1)*m])
                               for i in range(g))
                    assert lost <= escaped//m
        by_g[str(g)] = local
    return {'assignments_tested': tested, 'admissible_label_type_assignments': feasible,
            'admissible_by_bundle_size': by_g,
            'scope': 'One-bundle monitored destinations with explicit escape symbols; not graphs'}


def union_checks() -> int:
    cases = 0
    for n in range(1, 4):
        for sizes in it.product((2, 3), repeat=n):
            for arriving in it.product(*(range(-1, g) for g in sizes)):
                active = [t for t, label in enumerate(arriving) if label >= 0]
                for outside_masks in it.product(range(8), repeat=len(active)):
                    mates = {(t, j) for t in active for j in range(sizes[t])
                             if j != arriving[t]}
                    ext_union = 0
                    theta_max = 0
                    for mask in outside_masks:
                        ext_union |= mask
                        theta_max = max(theta_max, mask.bit_count())
                    actual_min_residual = len(mates) + ext_union.bit_count()
                    bound = sum(sizes[t]-1 for t in active) + theta_max
                    assert actual_min_residual >= bound
                    cases += 1
    return cases


def endpoint_scalar_checks() -> int:
    cases = 0
    for h0 in range(6):
        for g in range(2, 5):
            for m in (1, 2):
                for escaped in range(g*m+1):
                    eps = min(g-1, escaped//m)
                    for s in range(1, 5):
                        for source_cap in range(6):
                            theta = max(0, h0+s-source_cap-eps)
                            for extra in range(3):
                                residual = h0+g-1-eps+extra
                                degree = residual+s
                                # Give the source the most generous possible
                                # residual-neighbour contribution and L-neighbours.
                                source_neighbours = min(source_cap, degree)
                                selected_neighbours = degree-source_neighbours
                                in_family = min(g-1, selected_neighbours)
                                outside_family = selected_neighbours-in_family
                                assert outside_family >= theta
                                cases += 1
    return cases


def minimum_excess(capacities: tuple[int, ...], obligations: int) -> int | None:
    """Unbounded relaxed receiver-resource cover, not full routing."""
    if obligations <= 0:
        return 0
    if capacities[0] > 0:
        return 0  # arbitrarily many free degree-one receivers in this model
    inf = 10**9
    dp = [0] + [inf] * obligations
    for need in range(1, obligations+1):
        for r, cap in enumerate(capacities, 1):
            if cap:
                dp[need] = min(dp[need], (r-1)+dp[max(0, need-cap)])
    return None if dp[-1] == inf else dp[-1]


def controls_and_application() -> dict:
    closed = tuple((2, 2, 3) for _ in range(5))
    f = tuple(envelope(closed, r, 1) for r in range(1, 5))
    assert f == (0, 0, 0, 2)
    assert minimum_excess(f, 20) == 30
    # One escaped arc is fewer than two, so no entire label type is lost.
    assert min(1, 1//2) == 0
    assert minimum_excess(f, 19) == 30
    ratio = max(Fraction(f[r-1], r-1) for r in range(2, 5))
    assert ratio == Fraction(2, 3)
    one_leak_linear = Fraction(19, 1)/ratio
    assert -(-one_leak_linear.numerator//one_leak_linear.denominator) == 29
    # Two arcs of the same label share one set of residual labels.
    shared_residual = {'mate', 'x', 'y', 'z'}
    assert len(shared_residual)-1 == 3 < 2*3
    # External residual labels of different bundles may overlap completely.
    external = {'x', 'y', 'z'}
    real_union = {'mate_A', 'mate_B'} | external
    assert len(real_union) == 5 < 4+4
    # Positive demand is required for Delta=R+s.
    delta, residual = 0, 5
    demand = max(0, delta-residual)
    assert demand == 0 and delta < residual+demand
    # A present mate that is selected at O is not a residual incidence.
    r_o, s_o = {'x', 'y', 'z'}, {'mate'}
    assert 'mate' in (r_o | s_o) and 'mate' not in r_o
    # A degree-one receiver can have zero excess and positive capacity.
    assert envelope(((2, 2, 0),), 1, 1) == 2
    # If one whole two-source label type escapes, a mate occurrence is lost.
    g, m, targets = 2, 2, (0, 0, -1, -1)
    assert targets.count(-1)//m == 1
    residual_for_label_zero = {v for v in targets[m:] if v >= 0}
    assert len(residual_for_label_zero) == 0 < g-1
    # Resource-only witness: ten receivers, one mate and same 3 external
    # labels each; two monitored arcs of one label per receiver.
    witness = []
    for t in range(5):
        for incoming in range(2):
            witness.append({'bundle': t, 'incoming_label': incoming,
                            'monitored_arcs': 2,
                            'L_residual': [[t, 1-incoming]],
                            'external_residual': ['x', 'y', 'z'], 'rho': 4})
    assert sum(w['monitored_arcs'] for w in witness) == 20
    assert sum(w['rho']-1 for w in witness) == 30
    return {'omega34': {'Q': 20, 'local_capacity_r1_to_r4': list(f),
                       'minimum_used_receivers': 10, 'minimum_sigma_O': 30,
                       'branch_budget_constant': 134,
                       'global_budget_constant': 105,
                       'old_minimum_a_tau1': 35, 'new_minimum_a_tau1': 35},
            'one_arc_leakage': {'Q_into_O_lower': 19, 'linear_rounded_bound': 29,
                                'integer_resource_bound': 30,
                                'scope': 'Assumes all other bundle hypotheses and a certified leakage bound'},
            'resource_only_witness': witness,
            'negative_controls': ['same_label_sources_reuse_one_receiver',
                                  'external_labels_count_max_not_sum',
                                  'positive_demand_needed_for_degree_identity',
                                  'O_must_not_select_the_monitored_label_family',
                                  'degree_one_receivers_may_have_free_capacity',
                                  'whole_label_type_leakage_reduces_compulsory_residual_occurrences'],
            'witness_scope': 'Resource envelope only; not a full canonical system or original graph'}


def main() -> None:
    root = Path(__file__).resolve().parent
    py = bytes(envelope(groups, r, gap) for groups, r, gap in domain())
    assert len(py) == 78624
    with tempfile.TemporaryDirectory(prefix='shared-bundle-') as td:
        exe = Path(td)/'verify_budget'
        subprocess.run(['g++', '-std=c++17', '-O2', '-Wall', '-Wextra',
                        str(root/'verify_budget.cpp'), '-o', str(exe)],
                       check=True, timeout=30)
        cp = subprocess.run([str(exe)], stdout=subprocess.PIPE, check=True, timeout=40)
    assert cp.stdout == py, 'Python/C++ full capacity table differs'
    digest = hashlib.sha256(py).hexdigest()
    (root/'EXACT_COSTS.bin').write_bytes(py)
    archive = base64.b64encode(gzip.compress(py, mtime=0)).decode('ascii')+'\n'
    (root/'EXACT_COSTS.bin.gz.b64').write_text(archive)
    result = {'status': 'PASS_TARGETED_SHARED_BUNDLE_CHECKS_ONLY',
              'predecessor': PREDECESSOR,
              'exact_capacity_table': {'rows': len(py), 'python_cpp_full_byte_agreement': True,
                                      'sha256': digest,
                                      'domain': {'groups': [1, 2, 3], 'options': [list(x) for x in OPTIONS],
                                                 'gap_order': list(GAPS), 'r_order': list(RADII)},
                                      'encoding': 'one unsigned byte per cost, in domain generator order'},
              'mate_occurrences': mate_occurrence_checks(),
              'residual_union_set_cases': union_checks(),
              'positive_demand_endpoint_scalar_cases': endpoint_scalar_checks(),
              'application_and_controls': controls_and_application(),
              'original_graph_enumeration': 'NOT_RUN', 'catalogue_replay': 'NOT_RUN',
              'canonical_bridge_validation': 'NOT_ASSERTED', 'independent_expert_review': 'OPEN',
              'implementations': 'Both written by the same assistant, with different capacity enumerations'}
    (root/'CHECK_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('application_and_controls',)}, indent=2))


if __name__ == '__main__':
    main()
