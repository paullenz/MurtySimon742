#!/usr/bin/env python3
"""Exact joint lower-tail clipping, with a reconstructible minimizer.

Independent implementation of the integer capacity inverse.  For a labels,
maximum M and exactly k occurrences of M, minimize the TOTAL gamma drop
over all compatible lower-demand counts, rather than each level separately.
Standard library only. No graph sufficiency or all-order theorem is inferred.
"""
import argparse
from functools import lru_cache
from itertools import combinations_with_replacement
import json
from math import isqrt


def gamma(h, weight):
    if weight == 0:
        return 0
    assert weight > 0
    z = max(h, (1 + isqrt(max(0, 1 + 8 * weight - 4 * h * (h + 1)))) // 2)
    while z * (z - 1) + h * (h + 1) < 2 * weight:
        z += 1
    return z


def D(demands):
    return sum(
        len(tail) - gamma(h, sum(tail))
        for h in range(2, max(demands, default=0) + 1)
        if (tail := [s for s in demands if s >= h])
    )


def independent_gain(a, M, k):
    lo = M * k
    hi = lo + (M - 1) * (a - k)
    return sum(min(gamma(h, w) - gamma(h, w-k) for w in range(lo, hi+1))
               for h in range(2, M))


def joint_gain(a, M, k):
    """DP state: next level, available lower labels, already fixed tail mass."""
    @lru_cache(None)
    def solve(h, slots, mass):
        if h < 2:
            return 0
        return min(gamma(h, mass+h*c) - gamma(h, mass+h*c-k)
                   + solve(h-1, slots-c, mass+h*c)
                   for c in range(slots+1))

    h, slots, mass = M-1, a-k, M*k
    best = solve(h, slots, mass)
    demands = [M]*k
    while h >= 2:
        optimum = solve(h, slots, mass)
        for c in range(slots+1):
            nxt = mass+h*c
            if gamma(h,nxt)-gamma(h,nxt-k)+solve(h-1,slots-c,nxt) == optimum:
                demands.extend([h]*c)
                mass, slots = nxt, slots-c
                break
        h -= 1
    demands.extend([0]*slots)
    demands.sort()
    loss = k-gamma(M,M*k)
    clipped = [min(s,M-1) for s in demands]
    assert D(clipped)-D(demands) == best-loss
    return best, demands, solve.cache_info().currsize


def row(a, M, k):
    loss = k-gamma(M,M*k)
    safe = independent_gain(a,M,k)
    gain, witness, states = joint_gain(a,M,k)
    assert gain >= safe
    return dict(a=a,M=M,k=k,loss=loss,independent_gain=safe,
                joint_gain=gain,net_gain=gain-loss,minimizer=witness,dp_states=states)


def verify_small():
    checks = 0
    for a in range(3,9):
        for M in range(2,min(a,6)):
            for k in range(1,a+1):
                exact = min(D([min(s,M-1) for s in lower+(M,)*k])-D(lower+(M,)*k)
                            for lower in combinations_with_replacement(range(M),a-k))
                r = row(a,M,k)
                assert r['net_gain'] == exact, r
                checks += 1
    return checks


def terminal(a, cap):
    """Counts of labels >=2; zero/one labels do not contribute to D."""
    best, extremizers, count = -10**9, [], 0
    def visit(h, remaining, demands):
        nonlocal best, extremizers, count
        if h < 2:
            count += 1
            vector = [1]*remaining + demands
            score = D(vector)
            if score > best:
                best, extremizers = score, [sorted(vector)]
            elif score == best:
                extremizers.append(sorted(vector))
            return
        for c in range(remaining+1):
            visit(h-1, remaining-c, [h]*c+demands)
    visit(cap,a,[])
    return dict(a=a,cap=cap,states=count,Dmax=best,Qmax=a+best,
                terminal_Q_equality=extremizers)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--min-a',type=int,default=17)
    ap.add_argument('--max-a',type=int,default=23)
    ap.add_argument('--output')
    ap.add_argument('--small-check',action='store_true')
    args = ap.parse_args()
    results = {'method':'exact compatible lower-count dynamic programming','rows':[],'terminal':[]}
    if args.small_check:
        results['small_exhaustive_comparisons'] = verify_small()
    for a in range(args.min_a,args.max_a+1):
        all_ok = True
        for M in range(a-1,5,-1):
            for k in range(1,a+1):
                loss=k-gamma(M,M*k)
                if loss <= 0:
                    continue
                safe=independent_gain(a,M,k)
                if safe >= loss:
                    continue
                r=row(a,M,k)
                results['rows'].append(r)
                if r['net_gain'] < 0:
                    all_ok=False
                print(json.dumps(r),flush=True)
        result=terminal(a,5)
        result['clipping_to_five_verified']=all_ok
        results['terminal'].append(result)
        print(json.dumps(result),flush=True)
    if args.output:
        with open(args.output,'w') as f:
            json.dump(results,f,indent=2)
            f.write('\n')


if __name__ == '__main__':
    main()
