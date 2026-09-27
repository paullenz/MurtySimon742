#!/usr/bin/env python3
"""Exact-rational checks for the sharp local condition d_y <= floor(d_x).
Uses shared bitset, rearrangement and flow code, but separately implements the
rounded-demand squeeze and exhaustive deletion/canonical checks.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from math import floor
from pathlib import Path
import json
from verify_closure import digraphs, dominance, tables, margins, maximal_cut


def demand_order(P, d, blocks):
    return all(P[x] >= P[y] or d[y] <= floor(d[x])
               for B in blocks for x in B for y in B)


def check(P, rows, blocks, d):
    assert dominance(P, rows, blocks, 'weak') and demand_order(P, d, blocks)
    ys, hs, us = tables(P, rows, blocks)
    fs, gs, gamma, M = margins(hs, us, d)
    assert gamma == min(gs)
    fv, fm = maximal_cut(P, rows, d)
    assert fv == sum(d) + gamma and fm == M
    todo, seen, terminals, transitions = [M], set(), [], []
    while todo:
        S = todo.pop()
        if S in seen: continue
        seen.add(S)
        assert fs[S] == gamma
        pairs = [(x, y) for B in blocks for x in B for y in B
                 if max(P[x], ys[S][y]) < min(P[y], ys[S][x])]
        assert bool(pairs) == (us[S] > hs[S])
        if not pairs: terminals.append(S)
        for x, y in pairs:
            assert not M >> x & 1 and S >> y & 1
            assert ys[S][x] == ys[S][y] + 1
            nxt = S ^ (1 << y)
            gain, loss = hs[S | (1 << x)] - hs[S], hs[S] - hs[nxt]
            Z = sum(1 << w for w in range(len(P)) if ys[S][w] < P[w])
            T = sum(1 << w for w in range(len(P)) if ys[S][w] <= P[w])
            A, B = rows[x] & Z, rows[y] & T
            k = floor(d[x])
            assert gain > d[x] and gain <= A.bit_count()
            assert A.bit_count() >= k + 1
            assert A & (1 << y) and (A & ~(1 << y)) & ~B == 0
            assert k + 1 <= A.bit_count() <= B.bit_count() + 1 <= loss + 1 <= d[y] + 1 <= k + 1
            assert loss == d[y] == k and fs[nxt] == gamma
            transitions.append((S, x, y, nxt)); todo.append(nxt)
    tight = [S for S in range(len(hs)) if fs[S] == gamma and hs[S] == us[S]]
    C = 0
    for S in tight: C |= S
    assert sorted(set(terminals)) == [C]
    for A in tight:
        for B in tight:
            assert fs[A | B] == gamma and hs[A | B] == us[A | B]
    return [P, rows, d, gamma, M, C, len(seen), len(transitions)]


def sharp_family(a, b):
    k = floor(a); assert b > k
    n = k + 2; aux = sum(1 << w for w in range(2, n))
    rows = tuple([2 | aux, 1 | aux] + [0] * k)
    P = tuple([0, 1] + [2] * k)
    d = tuple([a, b] + [0] * k)
    blocks = tuple([(0, 1)] + [(w,) for w in range(2, n)])
    assert dominance(P, rows, blocks, 'strict')
    ys, hs, us = tables(P, rows, blocks)
    fs, gs, gamma, M = margins(hs, us, d)
    expected = min(Q(0), k + 1 - a, k + 1 - b, 2*k + 1 - a - b)
    assert gamma == k - b and min(gs) == expected and expected > gamma
    return [a, b, k, gamma, expected]


def main():
    caps = (Q(0), Q(1, 2), Q(3, 2)); values = tuple(Q(i, 2) for i in range(5))
    blocks = ((0, 1, 2),); rows_all = list(digraphs(3))
    stream = sha256(); cases = profiles = fractional_demands = with_deletions = 0
    for P in product(caps, repeat=3):
        ds = [d for d in product(values, repeat=3) if demand_order(P, d, blocks)]
        for rows in rows_all:
            if not dominance(P, rows, blocks, 'weak'): continue
            profiles += 1
            for d in ds:
                rec = check(P, rows, blocks, d); cases += 1
                fractional_demands += any(x.denominator != 1 for x in d)
                with_deletions += rec[-1] > 0
                stream.update((json.dumps(rec, separators=(',', ':'), default=str) + '\n').encode())
    family = [sharp_family(Q(a, 2), Q(b, 2)) for a in range(7) for b in range(7)
              if Q(b, 2) > floor(Q(a, 2))]
    fractional_example = check((Q(0), Q(3, 4)), (2, 1), ((0, 1),), (Q(1, 2), Q(0)))
    assert fractional_example[3:6] == [0, 2, 0]
    out = {'result': 'PASS', 'scope': 'Real capacities and rounded-order real demands',
           'profiles': profiles, 'demand_instances': cases, 'fractional_demand_instances': fractional_demands,
           'instances_with_deletions': with_deletions, 'flow_and_canonical_checks': cases,
           'stream_sha256': stream.hexdigest(), 'sharp_family_checks': family,
           'fractional_demand_positive_example': fractional_example,
           'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
           'dependency_sha256': sha256(Path('verify_closure.py').read_bytes()).hexdigest()}
    Path('ROUNDED_DEMANDS.json').write_text(json.dumps(out, indent=2, sort_keys=True, default=str) + '\n')
    print('PASS',cases,'instances;',len(family),'sharp-family cases')

if __name__ == '__main__': main()
