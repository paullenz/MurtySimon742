#!/usr/bin/env python3
"""Exact source-priced selected-incidence envelope. Standard library only.

Prices are integer numerators with one positive denominator (scale). Output
upper_scaled/scale is a rigorous upper bound for the stated projection only.
The maximising label choices need not form a common incidence matrix.
"""
from __future__ import annotations
from itertools import product
import argparse
import json
from pathlib import Path


def envelope(q, rho, s, D, E, alpha, prices, scale=1, xi=0, fixed_prefix=None):
    b, a = len(q), len(s)
    if any(type(v) is not int for arr in (q, rho, s, D, alpha, prices, [E, scale, xi]) for v in arr):
        raise ValueError('exact integer data and price numerators required')
    if not all(len(v) == b for v in (rho, D, alpha, prices)):
        raise ValueError('source-array length mismatch')
    if scale <= 0 or E < 0 or xi < 0 or s != sorted(s):
        raise ValueError('invalid scale, excess, threshold or label order')
    if any(v < 0 for arr in (q, s, D, alpha) for v in arr) or any(r < 1 for r in rho):
        raise ValueError('invalid nonnegative data or rho')
    if sum(q) != sum(s) + E:
        raise ValueError('row/column total mismatch')
    if fixed_prefix is not None:
        k, value = fixed_prefix
        if not 0 <= k <= a or not 0 <= value <= E:
            raise ValueError('invalid fixed-prefix branch')
        if k == 0 and value != 0:
            return None
    cache = {}
    for demand in set(s):
        eligible = [u for u in range(b) if q[u] > 0 and rho[u] >= demand]
        options = []
        for excess in range(min(E, len(eligible) - demand) + 1):
            values = [(scale * alpha[u] * min(excess, D[u])
                       if demand > xi else 0) - prices[u] for u in eligible]
            ranked = sorted(zip(values, eligible), key=lambda pair: (-pair[0], pair[1]))
            chosen = ranked[:demand + excess]
            options.append((sum(value for value, _ in chosen), [u for _, u in chosen]))
        cache[demand] = options
    # Exact forced selections in each labelled prefix give safe excess floors.
    floors = []
    for j in range(1, a + 1):
        forced = sum(max(0, q[u] - sum(v <= rho[u] for v in s[j:])) for u in range(b))
        floors.append(max(0, forced - sum(s[:j])))
    dp = [None] * (E + 1)
    dp[0] = 0
    back = []
    for j, demand in enumerate(s, 1):
        nxt = [None] * (E + 1)
        chosen_excess = [None] * (E + 1)
        for used, value in enumerate(dp):
            if value is None:
                continue
            for excess, (score, _) in enumerate(cache[demand]):
                total = used + excess
                if total > E:
                    break
                if total < floors[j - 1]:
                    continue
                if fixed_prefix is not None and j == fixed_prefix[0] and total != fixed_prefix[1]:
                    continue
                candidate = value + score
                if nxt[total] is None or candidate > nxt[total]:
                    nxt[total], chosen_excess[total] = candidate, excess
        dp = nxt
        back.append(chosen_excess)
    if dp[E] is None:
        return None
    allocation, used = [0] * a, E
    for j in range(a - 1, -1, -1):
        allocation[j] = back[j][used]
        used -= allocation[j]
    counts = [0] * b
    for demand, excess in zip(s, allocation):
        for u in cache[demand][excess][1]:
            counts[u] += 1
    return {'upper_scaled': dp[E] + sum(p * k for p, k in zip(prices, q)),
            'scale': scale, 'allocation': allocation, 'relaxed_source_counts': counts}


def brute_envelope(q, rho, s, D, E, alpha, prices, scale=1, xi=0):
    """Independent Cartesian enumeration, used only on small test inputs."""
    b = len(q)
    best = None
    for ex in product(range(E + 1), repeat=len(s)):
        if sum(ex) != E:
            continue
        feasible = True
        score = sum(prices[u] * q[u] for u in range(b))
        for j, (demand, excess) in enumerate(zip(s, ex), 1):
            eligible = [u for u in range(b) if q[u] and rho[u] >= demand]
            if demand + excess > len(eligible):
                feasible = False
                break
            need = sum(max(0, q[u] - sum(v <= rho[u] for v in s[j:])) for u in range(b))
            if sum(s[:j]) + sum(ex[:j]) < need:
                feasible = False
                break
            weights = [(scale * alpha[u] * min(excess, D[u]) if demand > xi else 0)
                       - prices[u] for u in eligible]
            weights.sort(reverse=True)
            score += sum(weights[:demand + excess])
        if feasible and (best is None or score > best):
            best = score
    return best


def pressure_lower(row, alpha):
    """Safe full-incoming lower bound; zeros handled by at most z selections."""
    q, rho, P = row['q'], row['rho'], row['P']
    need = max(0, sum(q) - sum(min(p, r - 1) for p, r in zip(P, rho)))
    z = row['s'].count(0)
    units = sorted(alpha[u] * max(0, q[u] - z)
                   for u in range(len(q)) for _ in range(max(0, P[u] - rho[u] + 1)))
    return None if need > len(units) else sum(units[:need])


def explore(row, iterations=48):
    q, rho, s, E = row['q'], row['rho'], row['s'], row['Esel']
    D = [max(0, p - r + 1) for p, r in zip(row['P'], rho)]
    results = []
    for name, alpha in [('unit', [1] * len(q)),
                        ('low-q-weight', [1 if k <= 2 else 3 for k in q])]:
        prices, best, trace = [0] * len(q), None, []
        lower = pressure_lower(row, alpha)
        for iteration in range(iterations):
            result = envelope(q, rho, s, D, E, alpha, prices, scale=2)
            if result is None:
                raise RuntimeError('unexpected empty label projection; inspect separately')
            upper = result['upper_scaled']
            trace.append(upper)
            if best is None or upper < best['upper_scaled']:
                best = dict(result, prices=prices[:], iteration=iteration)
            step = 4 if iteration < 12 else 2 if iteration < 24 else 1
            prices = [p + step * (used - wanted)
                      for p, used, wanted in zip(prices, result['relaxed_source_counts'], q)]
        # Replay the selected certificate without relying on the exploratory trace.
        replay = envelope(q, rho, s, D, E, alpha, best['prices'], scale=2)
        assert replay['upper_scaled'] == best['upper_scaled']
        results.append({'coefficients': name, 'alpha': alpha, 'lower': lower,
                        'initial_upper_scaled': trace[0], 'best': best,
                        'trace_upper_scaled': trace,
                        'strict_contradiction': lower is not None and 2 * lower > best['upper_scaled']})
    return {'row': row['row'], 'results': results,
            'excluded_by_this_test': any(r['strict_contradiction'] for r in results)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', type=Path)
    parser.add_argument('--iterations', type=int, default=48)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.iterations < 1:
        parser.error('--iterations must be positive')
    path = args.profiles or Path(__file__).parent.parent / '2026-09-14-block-pressure-v1/REMAINDER_12.json'
    original = json.loads(path.read_text())
    wanted = {108, 160, 338, 347, 471, 586}
    rows = [row for row in original['rows'] if row['row'] in wanted]
    if len(rows) != len(wanted) or {row['row'] for row in rows} != wanted:
        raise ValueError('original six-profile input coverage mismatch')
    result = {'schema': 'source-price-original-six-v1', 'iterations_per_weight': args.iterations,
              'scope': 'Original six synthetic profiles; not fresh seed, graph realization or whole-state coverage.',
              'profiles': [explore(row, args.iterations) for row in rows]}
    result['new_profile_exclusions'] = sum(row['excluded_by_this_test'] for row in result['profiles'])
    text = json.dumps(result, sort_keys=True, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
