#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import json


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def minimal_r(a, S):
    """Smallest integer r>=0 with 3 S^3 <= a^2 r(2r+1)."""
    D = a * a + 24 * S ** 3
    q = isqrt(D)
    r = max(0, (q - a) // (4 * a) - 2)
    while a * a * r * (2 * r + 1) < 3 * S ** 3:
        r += 1
    while r > 0 and a * a * (r - 1) * (2 * (r - 1) + 1) >= 3 * S ** 3:
        r -= 1
    return r


def scalar_surplus_audit(max_a=200):
    cases = 0
    minimum_strict_margin = None
    worst = None
    largest_excess = None
    largest_excess_case = None
    for a in range(1, max_a + 1):
        for S in range(1, a * (a - 1) + 1):
            r = minimal_r(a, S)
            # t is integral and 2t<=S-r, so this is the largest admissible t.
            t = (S - r) // 2
            margin = 32 * a * a + 81 - 648 * t
            require(margin > 0, ('surplus bound', a, S, r, t, margin))
            if minimum_strict_margin is None or margin < minimum_strict_margin:
                minimum_strict_margin = margin
                worst = {'a': a, 'S': S, 'r': r, 't': t, 'scaled_margin': margin}
            excess = Fraction(t) - Fraction(4 * a * a, 81)
            if largest_excess is None or excess > largest_excess:
                largest_excess = excess
                largest_excess_case = {'a': a, 'S': S, 'r': r, 't': t,
                                       'excess_over_4a2_81': str(excess)}
            cases += 1
    return {
        'max_a': max_a,
        'scalar_cases': cases,
        'minimum_scaled_strict_margin': minimum_strict_margin,
        'minimum_margin_case': worst,
        'largest_integer_excess_observed': str(largest_excess),
        'largest_excess_case': largest_excess_case,
    }


def degree_assembly_audit(max_n=5000):
    cases = 0
    minimum_margin = None
    worst = None
    for n in range(6, max_n + 1):
        bmin = (13 * n + 21) // 22
        for b in range(bmin, n - 1):  # a>=1; universal vertex handled separately
            a = n - 1 - b
            t_required = n * n // 4 - b * (n - b)
            # The surplus theorem says 648 t < 32 a^2+81. Density at least
            # floor(n^2/4) says t>=t_required. These conflict if this margin
            # is nonnegative.
            margin = 648 * t_required - (32 * a * a + 81)
            require(margin >= 0,
                    ('degree assembly', n, a, b, t_required, margin))
            if minimum_margin is None or margin < minimum_margin:
                minimum_margin = margin
                worst = {'n': n, 'a': a, 'b': b,
                         't_required': t_required, 'scaled_margin': margin}
            cases += 1
    # Mandatory boundary control: K(2,3) at n=5 meets the degree ratio and
    # balanced edge count, so the strict theorem cannot simply start at n=4.
    n, b, a = 5, 3, 1
    t_required = n * n // 4 - b * (n - b)
    require(22 * b >= 13 * n and t_required == 0,
            ('K23 boundary', n, a, b, t_required))
    return {
        'max_n': max_n,
        'degree_cases': cases,
        'minimum_scaled_margin': minimum_margin,
        'minimum_margin_case': worst,
        'K23_boundary_control': {'n': 5, 'a': 1, 'b': 3, 't_required': 0},
    }


def sharp_scalar_family():
    # For every k>=1 set a=27k, S=216k^2, r=144k^2, t=36k^2.
    # Then S=r+2t and t/a^2=4/81 exactly. The cubic inequality holds because
    # its leading quadratic term is equality and the +r term is positive.
    checks = []
    for k in [1, 2, 3, 10, 100]:
        a = 27 * k
        S = 216 * k * k
        r = 144 * k * k
        t = 36 * k * k
        require(S == r + 2 * t, ('family ledger', k))
        require(3 * S ** 3 <= a * a * r * (2 * r + 1), ('family cubic', k))
        require(Fraction(t, a * a) == Fraction(4, 81), ('family ratio', k))
        checks.append({'k': k, 'a': a, 'S': S, 'r': r, 't': t})
    return {
        'formula': 'a=27k, S=216k^2, r=144k^2, t=36k^2',
        'ratio': 't/a^2=4/81',
        'meaning': '4/81 cannot be lowered using only the cubic inequality and S>=r+2t',
        'sample_checks': checks,
    }


def main():
    out = {
        'schema': 'surplus-degree-adversarial-v1',
        'scalar_surplus': scalar_surplus_audit(),
        'degree_assembly': degree_assembly_audit(),
        'sharp_scalar_family': sharp_scalar_family(),
        'scope': 'scalar consequences only; the sharp family is not asserted graph-realisable',
        'status': 'PASS',
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
