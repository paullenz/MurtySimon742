#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement
import json


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def minimum_tail_for_profile(s):
    """Return the componentwise-minimal nonincreasing z_h sequence.

    Assumptions modelled here are only those used by the aggregation proof:
    * H=max s_i and z_h>=H for 1<=h<=H;
    * 2W_h<=z_h^2-z_h+h(h+1);
    * z_h is nonincreasing in h (it is a residual-degree tail count).

    Any larger feasible tail only increases r_H and therefore the right side
    of the target cubic inequality.
    """
    H = max(s, default=0)
    if H == 0:
        return [], [], 0
    W = [sum(x for x in s if x >= h) for h in range(1, H + 1)]
    z = []
    for h, w in enumerate(W, 1):
        zz = H
        while 2 * w > zz * zz - zz + h * (h + 1):
            zz += 1
        z.append(zz)
    for k in range(H - 2, -1, -1):
        z[k] = max(z[k], z[k + 1])
    return W, z, H


def audit(max_a=11):
    total_profiles = 0
    nonzero_profiles = 0
    threshold_levels = 0
    minimum_integer_slack = None
    worst_ratio = None
    worst_profile = None

    for a in range(1, max_a + 1):
        for s in combinations_with_replacement(range(a), a):
            total_profiles += 1
            W, z, H = minimum_tail_for_profile(s)
            if H == 0:
                continue
            nonzero_profiles += 1
            threshold_levels += H
            S = sum(s)
            Q = sum(W)
            rH = sum(z)

            require(all(z[k] >= z[k + 1] for k in range(H - 1)),
                    ('tail monotonicity', a, s, z))
            require(all(zz >= H for zz in z),
                    ('max-demand confinement', a, s, z, H))
            require(all(2 * w <= zz * zz - zz + h * (h + 1)
                        for h, (w, zz) in enumerate(zip(W, z), 1)),
                    ('threshold capacity', a, s, W, z))
            require(Q == sum(x * x for x in s),
                    ('layer cake', a, s, Q))
            require(S * S <= a * Q,
                    ('first Cauchy consequence', a, s, S, Q))

            # The stronger observation used in the tightened hand proof.
            # Since every z_h>=H and there are H active levels,
            # r_H=sum_h z_h >= H^2.
            require(rH >= H * H,
                    ('truncated residual mass', a, s, H, rH))

            # Exact rational version of the summed threshold estimate:
            # 2 sum W_h/z_h <= r_H + (H^2+2)/3
            #                         <= (4 r_H+2)/3.
            weighted_cost = sum((Fraction(2 * w, zz)
                                 for w, zz in zip(W, z)), Fraction(0))
            require(weighted_cost <= Fraction(rH) + Fraction(H * H + 2, 3),
                    ('weighted threshold sum', a, s, W, z, weighted_cost))
            require(weighted_cost <= Fraction(4 * rH + 2, 3),
                    ('rH relaxation', a, s, rH, weighted_cost))

            # This final integer inequality is the aggregation theorem after
            # the two standard Cauchy-Schwarz applications. Checking the
            # componentwise-minimal feasible tail is adversarial: every other
            # feasible tail has r_H at least this large and the RHS increases.
            lhs = 3 * S ** 3
            rhs = a * a * rH * (2 * rH + 1)
            require(lhs <= rhs,
                    ('cubic aggregation', a, s, H, W, z, lhs, rhs))

            slack = rhs - lhs
            if minimum_integer_slack is None or slack < minimum_integer_slack:
                minimum_integer_slack = slack
            ratio = Fraction(rhs, lhs)
            if worst_ratio is None or ratio < worst_ratio:
                worst_ratio = ratio
                worst_profile = {
                    'a': a,
                    'demands': list(s),
                    'H': H,
                    'r_H': rH,
                    'lhs_3S3': lhs,
                    'rhs_a2rH2rH1': rhs,
                }

    return {
        'schema': 'layer-aggregation-adversarial-v1',
        'max_a': max_a,
        'complete_sorted_demand_profiles': total_profiles,
        'nonzero_profiles': nonzero_profiles,
        'threshold_levels_checked': threshold_levels,
        'minimum_integer_slack': minimum_integer_slack,
        'worst_rhs_over_lhs': str(worst_ratio),
        'worst_profile': worst_profile,
        'stronger_checked_statement': '3 S^3 <= a^2 r_H(2 r_H+1), r_H=sum_{h<=H} z_h',
        'scope': 'abstract aggregation consequences only; no graph realisability claim',
        'status': 'PASS',
    }


if __name__ == '__main__':
    print(json.dumps(audit(), indent=2, sort_keys=True))
