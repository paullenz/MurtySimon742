#!/usr/bin/env python3
"""Finite selected-incidence soundness and independent DP checks; no graph claim."""
from itertools import product
import json
import random
from source_prices import envelope, brute_envelope


def main():
    configurations = 0
    for b in range(1, 4):
        for a in range(1, 4):
            for mask in range(1 << (a * b)):
                X = [[(mask >> (u * a + i)) & 1 for i in range(a)] for u in range(b)]
                q = [sum(row) for row in X]
                x = [sum(X[u][i] for u in range(b)) for i in range(a)]
                for original_s in product(*(range(v + 1) for v in x)):
                    order = sorted(range(a), key=lambda i: original_s[i])
                    s = [original_s[i] for i in order]
                    e = [x[i] - original_s[i] for i in order]
                    Y = [[row[i] for i in order] for row in X]
                    rho = [max([1] + [s[i] for i in range(a) if Y[u][i]]) for u in range(b)]
                    D = [1 + (mask + u) % 3 for u in range(b)]
                    d = [min([D[u]] + [e[i] for i in range(a) if Y[u][i] and s[i] > 0])
                         for u in range(b)]
                    alpha = [u + 1 for u in range(b)]
                    prices = [(-3, 0, 5)[(u + configurations) % 3] for u in range(b)]
                    xi = configurations % 2
                    actual = sum(alpha[u] * d[u] for u in range(b)
                                 for i in range(a) if Y[u][i] and s[i] > xi)
                    bound = envelope(q, rho, s, D, sum(e), alpha, prices, scale=2, xi=xi)
                    assert bound is not None and 2 * actual <= bound['upper_scaled']
                    configurations += 1
    rng = random.Random(74220260914)
    brute_checks, feasible = 0, 0
    for _ in range(600):
        b, a = rng.randint(1, 4), rng.randint(1, 3)
        q = [rng.randint(0, a) for _ in range(b)]
        s = sorted(rng.randint(0, b) for _ in range(a))
        E = sum(q) - sum(s)
        if not 0 <= E <= 6:
            continue
        rho = [rng.randint(1, b) for _ in range(b)]
        D = [rng.randint(0, 3) for _ in range(b)]
        alpha = [rng.randint(0, 3) for _ in range(b)]
        prices = [rng.randint(-5, 5) for _ in range(b)]
        xi, scale = rng.randint(0, 2), rng.randint(1, 3)
        fast = envelope(q, rho, s, D, E, alpha, prices, scale=scale, xi=xi)
        slow = brute_envelope(q, rho, s, D, E, alpha, prices, scale=scale, xi=xi)
        assert (None if fast is None else fast['upper_scaled']) == slow
        brute_checks += 1
        feasible += slow is not None
    # Three sources, two positive labels: one high-weight source cannot be used twice.
    args = ([1, 1, 2], [1, 1, 1], [1, 1], [1, 1, 1], 2, [10, 1, 1])
    unpriced = envelope(*args, [0, 0, 0])
    priced = envelope(*args, [9, 0, 0])
    assert unpriced['upper_scaled'] == 22 and priced['upper_scaled'] == 13
    # The actual matrix [[1,0],[0,1],[1,1]] with all pressures 1 has charge 13.
    # Omitting the exact row-budget restoration would incorrectly give 4 < 13.
    assert priced['upper_scaled'] - 9 == 4
    # Retain zero-demand columns in the pricing sum, including their negative scores.
    zero_args = ([1], [1], [0], [0], 1, [1])
    assert envelope(*zero_args, [-5])['upper_scaled'] == 0
    # Impossible fixed-prefix boundary is genuinely empty, not a zero optimum.
    assert envelope(*args, [0, 0, 0], fixed_prefix=(0, 1)) is None
    output = {'schema': 'source-price-verification-v1',
              'exhaustive_incidence_demand_configurations': configurations,
              'brute_force_dp_comparisons': brute_checks,
              'nonempty_brute_projections': feasible,
              'strict_toy': {'unpriced': 22, 'priced': 13, 'actual_charge': 13},
              'hostile_checks': ['missing row restoration', 'zero-demand signed price', 'empty fixed-prefix branch'],
              'scope': 'All binary matrices with 1<=sources,labels<=3 and every compatible demand vector; deterministic rho/caps/weights/prices per configuration. Not exhaustive parameter assignments, positive-surplus scalar profiles, or graphs.',
              'result': 'PASS'}
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
