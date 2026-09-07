#!/usr/bin/env python3
"""Exact arithmetic diagnostics for the 2026-09-07 all-order attack.

This is a NECESSARY-CONDITION screen, not a graph enumerator or an all-order
proof verifier. A surviving row is not a graph. A rejected row depends on the
candidate mathematical lemmas in ATTACK.md. No frozen theorem ledger is changed.
Python standard library only. Usage: python3 screen.py --output RESULTS.json
"""
from __future__ import annotations
import argparse
import json
import platform
from fractions import Fraction
from math import comb
from pathlib import Path


def choose2(n: int) -> int:
    if n < 0:
        raise ValueError('negative binomial argument')
    return n * (n - 1) // 2


def fan_strict_bound(n: int) -> Fraction:
    return Fraction(n*n, 4) + Fraction(5*n*n - 81*n + 280, 1600)


def max_integer_below(x: Fraction) -> int:
    return (x.numerator - 1) // x.denominator


def bands(n: int, b: int, m: int) -> list[dict[str, int]]:
    """Feasible (k,h,r interval) for scalar necessary conditions only."""
    a = n - 1 - b
    if a < 1:
        return []
    t = m - b*(n-b)
    if t <= 0:
        raise ValueError('the residual-activity reduction needs t>0')
    L = choose2(a) - t
    answer = []
    # Early h-index budget, avoiding any degree-profile enumeration.
    if b + 2*t > (a+1)**2 // 4:
        return answer
    for k in range(a):
        if L < b + k + choose2(a-k-1):
            continue
        cmin = (a*k + 1) // 2
        for h in range(1, min(a, b) + 1):
            lo = b + h*(h-1)
            hi = min(L - cmin, a*h - 2*t)
            if lo <= hi:
                answer.append({'k': k, 'h': h, 'r_min': lo, 'r_max': hi})
    return answer


def order_row(n: int) -> dict:
    target = n*n // 4
    low = (n+1)//2
    # Non-bipartite dense graphs of degree <=low are handled by the
    # general witness argument in ATTACK.md, not by this scalar scan.
    rows = {}
    for b in range(low+1, n-1):
        kept = bands(n, b, target)
        if kept:
            rows[str(b)] = kept
    upper = max_integer_below(fan_strict_bound(n))
    return {
        'n': n, 'target_edges': target,
        'fan_strict_bound': str(fan_strict_bound(n)),
        'above_bound_edge_counts': list(range(target+1, upper+1)),
        'remaining_degrees_at_equality': [int(b) for b in rows],
        'scalar_bands_at_equality': rows,
        'scope': 'necessary scalar conditions only; NOT a completed order proof'
    }


def arithmetic_checks() -> dict:
    # An independent exhaustive maximum check for the completed square.
    quadratic_count = 0
    for a in range(1, 151):
        for b in range(a+1, a+11):
            lhs = max((a+1)*h-h*h-b for h in range(1, min(a,b)+1))
            assert lhs == (a+1)**2//4-b
            quadratic_count += 1
    # Verify the near-half odd-order witness polynomial and its unique equality
    # endpoint for every admissible h, without using an optimizer.
    odd_cases = 0
    for s in range(2, 501):
        n = 2*s+1
        target = s*(s+1)
        for h in range((s+1)//2+1):
            o_bound = s+1-2*h
            value = choose2(h) + h*(n-h) + o_bound*(o_bound-1)
            assert value <= target
            assert (value == target) == (h == 0)
            odd_cases += 1
    # The algebraic high-degree cutoff uses alpha=(3+sqrt(2))/7.
    # b >= alpha*n iff 7b-3n >= 0 and (7b-3n)^2 >= 2n^2.
    # Check the exact finite bound for all such b at these tested orders.
    cutoff_cases = 0
    for n in range(4, 1001):
        for b in range((n+1)//2+1, n-1):
            z = 7*b-3*n
            if z >= 0 and z*z >= 2*n*n:
                t = n*n//4 - b*(n-b)
                assert t > 0
                assert b+2*t > (n-b)**2//4
                cutoff_cases += 1
    return {'integer_quadratic_maxima': quadratic_count,
            'odd_witness_endpoint_cases': odd_cases,
            'high_degree_integer_checks': cutoff_cases,
            'status': 'PASS; finite algebra regression tests, not universal proof'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('RESULTS.json'))
    args = parser.parse_args()
    result = {
        'date': '2026-09-07',
        'status': 'REPRODUCED arithmetic; candidate graph-theoretic derivations; external review OPEN',
        'environment': {'python': platform.python_version(), 'implementation': platform.python_implementation()},
        'checks': arithmetic_checks(),
        'orders': [order_row(n) for n in [27,28,29,30,31,32,33,34,35,40,50,100]],
        'limitations': ['No full residual-profile sweep was run.',
                       'No order above 27 is claimed resolved.',
                       'Positive-surplus counterexamples are not supplied by this test.',
                       'The candidate 0.630601937... cutoff is proved algebraically in ATTACK.md; tests are supporting checks only.']
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result['checks'], indent=2))
    for row in result['orders']:
        print(row['n'], row['target_edges'], row['above_bound_edge_counts'], row['remaining_degrees_at_equality'])

if __name__ == '__main__':
    main()
