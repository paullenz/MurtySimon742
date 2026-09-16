#!/usr/bin/env python3
"""Targeted checks of the tight-interface slack lemma.

These are small A-side interface / scalar tests, NOT canonical graph
realizations, NOT catalogue exclusions, and NOT independent expert review.
The C++ companion scans all binary interfaces; this Python program generates
only interfaces within per-row budgets and compares exact fingerprints.
"""
from __future__ import annotations
import itertools
import json
import math
import subprocess
import tempfile
from pathlib import Path

SCENARIOS = ([(3, 1, k) for k in range(3, 7)]
             + [(3, 2, k) for k in range(5, 8)] + [(4, 1, 4)])
MASK64 = (1 << 64) - 1


def ceildiv(n: int, d: int) -> int:
    assert d > 0
    return -(-n // d)


def interface_checks() -> dict:
    rows = []
    for sid, (d, z, kappa) in enumerate(SCENARIOS):
        edges = list(itertools.combinations(range(d), 2))
        h = kappa - 1 - z * (d - 1)
        n = total = squares = xor = 0
        for ccode in range(1 << d):
            counts = [z + ((ccode >> t) & 1) for t in range(d)]
            ell = sum(counts)
            L = ell - z * d
            for tmask in range(1 << len(edges)):
                absent_internal = [0] * d
                for bit, (u, v) in enumerate(edges):
                    if (tmask >> bit) & 1:
                        absent_internal[u] += 1
                        absent_internal[v] += 1
                allowances = [kappa - 1 - (ell - counts[t])
                              - absent_internal[t] for t in range(d)]
                if min(allowances) < 0:
                    continue
                choices = [[m for m in range(1 << kappa)
                            if m.bit_count() <= allowance]
                           for allowance in allowances]
                for missing in itertools.product(*choices):
                    everywhere_missing = (1 << kappa) - 1
                    any_missing = 0
                    crosscode = 0
                    for t, m in enumerate(missing):
                        everywhere_missing &= m
                        any_missing |= m
                        crosscode |= m << (t * kappa)
                    if everywhere_missing:
                        continue  # Each member of K must meet at least one t.
                    common = kappa - any_missing.bit_count()
                    Q = sum(m.bit_count() for m in missing)
                    mu = tmask.bit_count()
                    deficit = sum(absent_internal[t] + missing[t].bit_count()
                                  for t in range(d))
                    assert deficit == 2 * mu + Q
                    assert 2 * mu + Q <= d * h - (d - 1) * L
                    assert common >= max(0, kappa - d * h + (d - 1) * L + 2 * mu)
                    eta_lower = (d - 1) * common
                    assert d * h + eta_lower >= d * (z + 1) - 1
                    ident = (crosscode | (tmask << (d * kappa))
                             | (ccode << (d * kappa + len(edges)))
                             | (sid << (d * kappa + len(edges) + d)))
                    n += 1
                    total = (total + ident) & MASK64
                    squares = (squares + ident * ident) & MASK64
                    xor ^= ident
        rows.append(dict(d=d, z=z, kappa=kappa, cases=n,
                         sum=total, sum_squares=squares, xor=xor))
    return dict(cases=sum(row['cases'] for row in rows), rows=rows)


def integer_checks() -> dict:
    scalar_cases = refined_cases = threshold_cases = 0
    for d in range(3, 51):
        for z in range(1, d + 1):
            values = []
            k0 = 1 + z * (d - 1)
            for h in range(0, 2 * z + d + 1):
                v = d * h + (d - 1) * max(0, k0 - (d - 1) * h)
                assert v >= d * (z + 1) - 1
                values.append(v)
                scalar_cases += 1
                for L in range(0, 5):
                    if d * h < (d - 1) * L:
                        continue
                    common_lb = max(0, k0 - (d - 1) * h + (d - 1) * L)
                    refined = d * h + (d - 2) * L + (d - 1) * common_lb
                    assert refined >= d * (z + 1) - 1
                    refined_cases += 1
            assert min(values) == d * (z + 1) - 1
            assert values.index(min(values)) == z
            for tau in range(1, 7):
                direct = ceildiv(2 * z * d * (d - 1) + 1 + 2 * tau, d - 2)
                expanded = 2 * z * (d + 1) + ceildiv(4 * z + 1 + 2 * tau, d - 2)
                assert direct == expanded
                a = direct
                assert (d - 2) * a >= 2 * z * d * (d - 1) + 1 + 2 * tau
                assert (d - 2) * (a - 1) < 2 * z * d * (d - 1) + 1 + 2 * tau
                threshold_cases += 1
    rows = []
    for d in range(3, 11):
        tau = 1
        old = 4 * d + 1 + ceildiv(4 + 2 * tau, d - 2)
        new = 4 * d + 4 + ceildiv(9 + 2 * tau, d - 2)
        any_block = 2 * d + 2 + ceildiv(5 + 2 * tau, d - 2)
        rows.append(dict(d=d, tau=tau, old_min_a_for_extras=old,
                         new_min_a_for_extras=new,
                         new_min_a_for_any_tight_block=any_block))
    return dict(scalar_cases=scalar_cases, refined_cases=refined_cases,
                threshold_cases=threshold_cases, thresholds=rows)


def negative_controls() -> list:
    # The d>=3 domain of the integer minimization is essential.
    d, z, h = 2, 1, 0
    actual = d * h + (d - 1) * (1 + z * (d - 1))
    assert actual < d * (z + 1) - 1
    # A predecessor scalar equality is not enough: it must pay common-label slack.
    d, z, a, b, tau = 3, 2, 20, 23, 1
    assert a * (d - 1) + d == b + 2 * tau + z * d * (2 * d - 3)
    assert b >= a + 2
    assert (d - 1) * (a - 2 * z * d) < b + 2 * tau - 1
    # Exact integer minimization differs from the continuous relaxation.
    from fractions import Fraction
    d, z = 5, 2
    h = Fraction(1 + z * (d - 1), d - 1)
    continuous = d * h
    assert continuous < d * (z + 1) - 1
    # Weak K-labels are not all common; all-K unselection is not proved.
    d, z = 3, 2
    kappa = 2 * d
    missing = [1 << t for t in range(d)]
    assert all(m.bit_count() == 1 for m in missing)
    common = kappa - (missing[0] | missing[1] | missing[2]).bit_count()
    assert 0 < common < kappa
    return [dict(kind='d2_not_in_integer_lemma_domain', value=2, claimed_bound=3),
            dict(kind='old_scalar_bound_does_not_imply_new_bound',
                 d=3, z=2, a=20, b=23, tau=1, h=0,
                 eta=0, omitted_common_label_penalty=10,
                 canonical_realization=False),
            dict(kind='h_must_be_integer', d=5, z=2, relaxed_h='9/4',
                 continuous_minimum='45/4', integer_minimum=14),
            dict(kind='do_not_assert_all_K_labels_unselected', d=3, z=2,
                 kappa=6, common_K_labels=3, weak_K_labels=3,
                 scope='Local interface only; not a canonical realization')]


def main() -> None:
    root = Path(__file__).resolve().parent
    py = interface_checks()
    with tempfile.TemporaryDirectory(prefix='interface-slack-') as tmp:
        exe = Path(tmp) / 'verify'
        subprocess.run(['g++', '-std=c++17', '-O2', '-Wall', '-Wextra',
                        str(root / 'verify_slack.cpp'), '-o', str(exe)],
                       check=True, timeout=30)
        cp = subprocess.run([str(exe)], check=True, text=True,
                            stdout=subprocess.PIPE, timeout=40)
    cpp = json.loads(cp.stdout)
    assert cpp == py, {'python': py, 'cpp': cpp}
    result = dict(status='PASS_TARGETED_INTERFACE_AND_INTEGER_CHECKS_ONLY',
                  python_cpp_exact_fingerprints_agree=True,
                  interfaces=py, integer_checks=integer_checks(),
                  negative_controls=negative_controls(),
                  independence='Different enumerators by the same assistant; not independent expert review',
                  original_graph_enumeration='NOT_RUN', catalogue_replay='NOT_RUN',
                  canonical_bridge_validation='NOT_ASSERTED',
                  independent_expert_review='OPEN')
    (root / 'CHECK_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
