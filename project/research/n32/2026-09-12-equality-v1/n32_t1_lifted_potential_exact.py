#!/usr/bin/env python3
"""Exact replay of the lifted N30 t=1 potential on the N32 equality frontier.

Input frontier rows are produced independently by check_n32_t1_frontier.cpp.
The fixed 13-term global potential is the natural b=17 lift of the exact N30
potential: BC v-thresholds and diagonal K-thresholds are shifted up by one;
the s>=2 term is unchanged. Floating LP is proposal only. Acceptance is exact
integer arithmetic after one-sided ell/sigma repair.

Expected complete result:
  frontier profiles             381
  monotone-tail impossible        1
  genuine positive states      1984
  exact lifted-potential certs  1369
  positive survivors            615
  zero-demand states             61
"""
from collections import Counter
from pathlib import Path
import argparse
import csv
import json
import numpy as np
from scipy.optimize import linprog

A = 14
B = 17
DMAX = 12

BC = {
    (1,8):7, (1,11):11, (1,13):5, (1,14):21, (1,15):29, (1,16):39,
    (2,13):6,
    (3,9):5, (3,10):8, (3,12):11,
}
DIAG = {16:17, 17:8}
SH = {(2,0):39}


def cap(h, z):
    return (z * (z - 1) + h * (h + 1)) // 2


def gamma(h, W):
    if W <= 0:
        return 0
    z = h
    while W > cap(h, z):
        z += 1
    return z


def min_rho_closure(s):
    raw = {h: 0 for h in range(2, A)}
    for h in range(2, A):
        vals = [x for x in s if x >= h]
        if vals:
            raw[h] = gamma(h, sum(vals))
    z = {A: 0}
    running = 0
    for h in range(A - 1, 1, -1):
        running = max(running, raw[h])
        z[h] = running
    z[1] = B
    rho = []
    for k in range(1, A):
        rho.extend([k] * (z[k] - z[k + 1]))
    assert len(rho) == B
    monotone_extra = sum(z[h] - raw[h] for h in range(2, A))
    return tuple(rho), monotone_extra


def rho_variants(rho0, E):
    cur = {tuple(rho0)}
    for _ in range(E):
        nxt = set()
        for rho in cur:
            for i, x in enumerate(rho):
                if x >= A:
                    continue
                y = list(rho)
                y[i] += 1
                y.sort()
                nxt.add(tuple(y))
        cur = nxt
    return sorted(cur)


def phi(s, d, h):
    v = B - h
    ans = 0
    for (D, V), w in BC.items():
        if d >= D and v >= V:
            ans += w
    for K, w in DIAG.items():
        if d + v >= K:
            ans += w
    for (S, V), w in SH.items():
        if s >= S and v >= V:
            ans += w
    return ans


def tterm(rho, q, p, j):
    return (q if q >= j + 1 else 0) - (p if rho + q >= j else 0)


def build_envelope_system(s, rho):
    sc = Counter(s)
    rc = Counter(rho)
    r = sum(rho)
    names = ['lambda', 'c', 'mu'] + [f'tau{j}' for j in range(1, A + 1)]
    names += [f'ell:{x}' for x in sc]
    names += [f'sigma:{x}' for x in rc]
    idx = {name: i for i, name in enumerate(names)}
    n = len(names)

    local = []  # (coefficient dict, rhs, repair variable)
    for sv in sc:
        ell = idx[f'ell:{sv}']
        for R in range(DMAX - sv + 1):
            for x in range(sv, B - R + 1):
                row = {ell: 1, idx['lambda']: -R, idx['c']: -x}
                rhs = x * phi(sv, R + sv, R + x)
                local.append((row, rhs, ell))

    for rv in rc:
        sig = idx[f'sigma:{rv}']
        qmax = min(A - rv, sum(si <= rv for si in s))
        for q in range(qmax + 1):
            pmax = min(rv + B - A - 1, B - 1 - q)
            for p in range(pmax + 1):
                row = {sig: 1, idx['mu']: -(q - p), idx['c']: q}
                for j in range(1, A + 1):
                    tv = tterm(rv, q, p, j)
                    if tv:
                        row[idx[f'tau{j}']] = -tv
                rhs = -q * phi(rv, rv + q - 1, q + p)
                local.append((row, rhs, sig))

    gap = {idx['lambda']: r}
    for sv, mult in sc.items():
        gap[idx[f'ell:{sv}']] = -mult
    for rv, mult in rc.items():
        gap[idx[f'sigma:{rv}']] = -mult

    A_ub = np.zeros((len(local) + 1, n))
    b_ub = np.zeros(len(local) + 1)
    for i, (row, rhs, _) in enumerate(local):
        for j, coef in row.items():
            A_ub[i, j] = coef
        b_ub[i] = rhs
    for j, coef in gap.items():
        A_ub[-1, j] = coef
    b_ub[-1] = -1.0

    nonnegative_count = 3 + A
    bounds = [(0, None)] * nonnegative_count
    bounds += [(None, None)] * (len(sc) + len(rc))
    return names, local, gap, A_ub, b_ub, bounds, nonnegative_count


def exact_certificate(s, rho):
    names, local, gap, A_ub, b_ub, bounds, nn = build_envelope_system(s, rho)
    res = linprog(np.zeros(len(names)), A_ub=A_ub, b_ub=b_ub,
                  bounds=bounds, method='highs')
    if not res.success:
        return None

    for denominator in (10_000, 100_000, 1_000_000, 10_000_000):
        X = []
        for j, value in enumerate(res.x):
            z = int(round(float(value) * denominator))
            X.append(max(0, z) if j < nn else z)

        # Each local envelope row has exactly one ell/sigma coefficient +1.
        # Lowering that variable repairs the row and cannot damage another local
        # row except via the final strict-gap test, which is rechecked exactly.
        repairs = {}
        for row, rhs, repair_var in local:
            lhs = sum(coef * X[j] for j, coef in row.items())
            target = rhs * denominator
            if lhs > target:
                repairs[repair_var] = max(repairs.get(repair_var, 0), lhs - target)
        for j, amount in repairs.items():
            X[j] -= int(amount)

        if any(X[j] < 0 for j in range(nn)):
            continue
        good = True
        for row, rhs, _ in local:
            if sum(coef * X[j] for j, coef in row.items()) > rhs * denominator:
                good = False
                break
        if not good:
            continue
        gap_numerator = sum(coef * X[j] for j, coef in gap.items())
        if gap_numerator < 0:
            return {
                'denominator': denominator,
                'gap_numerator': int(gap_numerator),
                'repair_count': len(repairs),
                'repair_total': int(sum(repairs.values())),
            }
    raise RuntimeError('floating feasible state failed exact integer acceptance')


def load_frontier(path):
    rows = []
    with path.open() as f:
        for row in csv.reader(f):
            if not row:
                continue
            q = int(row[0])
            s = tuple(map(int, row[1:]))
            assert len(s) == A and 19 <= q <= 23
            rows.append((q, s))
    assert len(rows) == 381
    assert Counter(q for q, _ in rows) == Counter({19:206,20:104,21:50,22:18,23:3})
    return rows


def expand(frontier):
    positive = []
    zero = []
    impossible = []
    for q, s in frontier:
        rho0, monotone_extra = min_rho_closure(s)
        slack = q - 19 - monotone_extra
        if slack < 0:
            impossible.append({'Q': q, 's': list(s), 'monotone_extra': monotone_extra,
                               'S': sum(s), 'r_min': sum(rho0)})
            continue
        for E in range(slack + 1):
            for rho in rho_variants(rho0, E):
                rec = {'Q': q, 's': list(s), 'rho': list(rho), 'E': E}
                (positive if min(s) > 0 else zero).append(rec)
    assert len(positive) == 1984
    assert len(zero) == 61
    assert len(impossible) == 1
    assert impossible[0]['s'] == [3] * 11 + [5] * 3
    return positive, zero, impossible


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--frontier', type=Path, required=True)
    ap.add_argument('--survivors', type=Path, required=True)
    ap.add_argument('--zero-states', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()

    frontier = load_frontier(args.frontier)
    positive, zero, impossible = expand(frontier)

    certified = []
    survivors = []
    for i, rec in enumerate(positive):
        cert = exact_certificate(tuple(rec['s']), tuple(rec['rho']))
        if cert is None:
            survivors.append({'state_id': i, **rec})
        else:
            certified.append({'state_id': i, **cert})

    assert len(certified) == 1369
    assert len(survivors) == 615
    assert all(x['denominator'] == 10000 for x in certified)

    args.survivors.parent.mkdir(parents=True, exist_ok=True)
    args.survivors.write_text(''.join(json.dumps(x, separators=(',',':'), sort_keys=True) + '\n'
                                      for x in survivors))
    args.zero_states.write_text(''.join(json.dumps({'state_id': i, **x}, separators=(',',':'), sort_keys=True) + '\n'
                                       for i, x in enumerate(zero)))

    gaps = [x['gap_numerator'] for x in certified]
    out = {
        'schema': 'n32-t1-lifted-potential-exact-v1',
        'status': 'PASS',
        'frontier_profiles': 381,
        'frontier_histogram': {'19':206,'20':104,'21':50,'22':18,'23':3},
        'positive_states': len(positive),
        'zero_states': len(zero),
        'monotone_tail_impossible_profiles': impossible,
        'exact_certificates': len(certified),
        'survivors': len(survivors),
        'denominator': 10000,
        'gap_numerator_min': min(gaps),
        'gap_numerator_max': max(gaps),
        'floating_point_is_proposal_only': True,
        'integer_arithmetic_is_acceptance': True,
        'potential_terms': 13,
        'interpretation': '1369 states are excluded by exact rational envelope certificates for the fixed lifted N30 potential; 615 are passed to the stronger RX/Hall replay.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
