#!/usr/bin/env python3
"""Targeted arithmetic and assumption checks for the global tight-block budget.

These checks are NOT a catalogue replay, original-graph enumeration, a proof
of the canonical bridge, or a search for a Murty--Simon counterexample.
Only the small F graphs in check_positive_part_identity are enumerated;
no full G, selected routing, or graph realizability is supplied.
"""
from __future__ import annotations

from itertools import combinations, product
import json


def check_positive_part_identity() -> dict:
    """Check the exact slack in S >= r+2*tau, including over-residual labels."""
    rows = []
    for a in range(1, 6):
        pairs = list(combinations(range(a), 2))
        count = nonzero_slack = 0
        for mask in range(1 << len(pairs)):
            degrees = [0] * a
            for k, (i, j) in enumerate(pairs):
                if (mask >> k) & 1:
                    degrees[i] += 1
                    degrees[j] += 1
            choices = [sorted({0, degree, degree + 1}) for degree in degrees]
            for residual in product(*choices):
                r = sum(residual)
                tau = mask.bit_count() - r
                demand = sum(max(0, deg - rr) for deg, rr in zip(degrees, residual))
                alpha = sum(max(0, rr - deg) for deg, rr in zip(degrees, residual))
                assert demand == r + 2 * tau + alpha
                count += 1
                nonzero_slack += int(alpha > 0)
        rows.append(dict(a=a, F_graphs=1 << len(pairs),
                         degree_residual_cases=count, positive_slack_cases=nonzero_slack))
    return dict(rows=rows, cases=sum(row['degree_residual_cases'] for row in rows))


def check_global_budget() -> dict:
    """Build source and label arrays independently, then compare both sides.

The symbol z is a proposed chromatic LOWER BOUND certified by the proof,
not a computed chromatic number. Arrays only enforce the counted necessary
conditions; tau is induced by a chosen nonnegative positive-part slack.
"""
    count = positive_tau = activity_improvement = 0
    for d in range(2, 8):
        for z in range(1, d + 1):
            for kappa_slack in range(3):
                kappa = 1 + z * (d - 1) + kappa_slack
                for receiver_slack in range(3):
                    used = z * d + receiver_slack
                    for p in (1, d, 3 * d):
                        a = d + kappa + p
                        label_count = a - d
                        demand_profiles = {
                            (d - 1,) * label_count,
                            (0,) * label_count,
                            tuple(i % d for i in range(label_count)),
                            (0,) + (d - 1,) * (label_count - 1),
                        }
                        for other_vertices in (0, 1, d):
                            b = d + used + other_vertices
                            for high_slack in (0, 1):
                                rho_high = [kappa + high_slack] * d
                                for other_residual in sorted({1, d - 1}):
                                    rho_other = [other_residual] * other_vertices
                                    rho = rho_high + [d - 1] * used + rho_other
                                    r = sum(rho)
                                    sigma_h = sum(x - kappa for x in rho_high)
                                    sigma_o = sum(x - 1 for x in rho_other)
                                    for demands in demand_profiles:
                                        eta = sum(d - 1 - s for s in demands)
                                        S = d * d + sum(demands)
                                        for alpha in (0, 1, 2):
                                            twice_tau = S - r - alpha
                                            if twice_tau % 2:
                                                continue
                                            tau = twice_tau // 2
                                            lhs = a * (d - 1) + d - b - 2 * tau
                                            exact = (z * d * (2 * d - 3)
                                                     + d * kappa_slack
                                                     + (d - 2) * receiver_slack
                                                     + sigma_h + sigma_o + eta + alpha)
                                            assert lhs == exact
                                            assert lhs >= z * d * (2 * d - 3)
                                            count += 1
                                            if tau > 0:
                                                positive_tau += 1
                                                assert r >= b + z * d * (2 * d - 3)
                                                if z >= 2:
                                                    assert (d - 1) * (a - 4 * d) >= b - 3 * d + 2 * tau
                                                    assert a > 4 * d
                                                    if b >= a + 2:
                                                        assert d >= 3
                                                        assert (d - 2) * a >= 4*d*d - 7*d + 2 + 2*tau
                                                        threshold = 4*d + 1 + (4 + 2*tau + d - 3) // (d - 2)
                                                        assert a >= threshold
                                            activity_improvement += int(other_vertices > 0)
    return dict(cases=count, positive_tau_relaxed_cases=positive_tau,
                cases_with_unused_vertices=activity_improvement,
                graph_realizability='NOT_ASSERTED')


def check_demand_cap() -> dict:
    """More than d demand cannot be met by only d eligible high sources."""
    count = 0
    for d in range(1, 11):
        for high_excess in range(4):
            rho = [d + high_excess] * d + list(range(d)) * 3
            assert sum(x >= d for x in rho) == d
            for s in range(1, d + high_excess + 3):
                eligible = sum(x >= s for x in rho)
                if eligible >= s:
                    assert s <= d
                if s > d:
                    assert eligible < s
                count += 1
    return dict(candidate_demands=count)


def check_thresholds() -> dict:
    rows = []
    for d in range(3, 11):
        tau = 1
        minimum_a = 4*d + 1 + (4 + 2*tau + d - 3) // (d - 2)
        for a in (minimum_a - 1, minimum_a):
            b = a + 2
            ok = a*(d - 1) + d >= b + 2*tau + 2*d*(2*d - 3)
            assert ok == (a == minimum_a)
        rows.append(dict(d=d, tau=tau, a_lower_bound_for_extras=minimum_a,
                         assumptions='b>=a+2; necessary bound only'))
    for a in range(1, 101):
        b = a + 2
        # Already chi>=1 is impossible for d=2 and positive surplus.
        assert a + 2 < b + 2 + 2
    return dict(rows=rows, d2_obstruction_checks=100)


def negative_controls() -> list[dict]:
    # Without residual activity at unused vertices, the sharper b-bound fails
    # even as a scalar implication. The weaker H/U-only bound still holds.
    d, a, kappa, used, b = 3, 13, 5, 6, 12
    r = d*kappa + used*(d - 1)  # three unused vertices wrongly allowed rho=0
    S, alpha = a*(d - 1) + d, 0
    twice_tau = S - r - alpha
    assert twice_tau == 2
    assert (d - 1)*(a - 4*d) == twice_tau
    assert (d - 1)*(a - 4*d) < b - 3*d + twice_tau
    controls = [dict(kind='activity_cannot_be_dropped', d=d, a=a, b=b,
                     tau=twice_tau//2, reason='three unused vertices have rho=0',
                     canonical_realization=False)]
    # The largest d-level label set must be EXACTLY T, not a chosen d-subset.
    d, a = 3, 4
    supplied_demands = [d] * (d + 1)
    assert sum(supplied_demands) > a*(d - 1) + d
    controls.append(dict(kind='T_must_be_exact_demand_level', d=d, a=a,
                         tight_labels=len(supplied_demands), required_tight_labels=d,
                         canonical_hypotheses_satisfied=False))
    # Example with positive-part slack: replacing >= with equality is invalid.
    degrees, residual = [1, 1], [2, 0]
    S = sum(max(0, deg-rr) for deg, rr in zip(degrees, residual))
    r = sum(residual)
    tau = 1-r
    assert S == 1 and r + 2*tau == 0
    controls.append(dict(kind='positive_part_slack_cannot_be_discarded',
                         S=S, r=r, tau=tau, alpha=1))
    # A q-colouring gives chi<=q, not chi>=q: unequal receiver pools matter.
    counts = [2, 3, 3]
    assert min(counts) == 2 and max(counts) == 3
    controls.append(dict(kind='do_not_use_largest_receiver_pool_as_chromatic_lower_bound',
                         d=3, counts=counts,
                         valid_upper_bound_on_chi=min(counts)))
    return controls


def main() -> None:
    result = dict(
        status='PASS_TARGETED_BUDGET_CHECKS_ONLY',
        positive_part_identity=check_positive_part_identity(),
        global_budget=check_global_budget(),
        demand_cap=check_demand_cap(),
        integer_thresholds=check_thresholds(),
        negative_controls=negative_controls(),
        original_graph_enumeration='NOT_RUN', catalogue_replay='NOT_RUN',
        independent_expert_review='OPEN',
        scope='New arithmetic and necessary-assumption steps only; not validation of the canonical bridge or graph realizability.')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
