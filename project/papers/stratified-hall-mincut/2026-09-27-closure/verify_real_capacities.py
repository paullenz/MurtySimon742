#!/usr/bin/env python3
"""Exact-Fraction check of the natural real-receiver-capacity extension.
U is sorted-pair rearrangement, NOT the old discrete threshold sum.
Imports the independently written integer verifier; no network or services.
"""
from __future__ import annotations
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import argparse
from verify_closure import digraphs, dominance, antitone, tables, margins, maximal_cut


def closure(P, rows, blocks, d, ys, hs, us, fs, gamma, M):
    todo, seen, edges, terminals = [M], set(), [], []
    while todo:
        S = todo.pop()
        if S in seen: continue
        seen.add(S)
        assert fs[S] == gamma
        crosses = [(x, y) for B in blocks for x in B for y in B
                   if max(P[x], ys[S][y]) < min(P[y], ys[S][x])]
        assert bool(crosses) == (us[S] > hs[S])
        if not crosses:
            terminals.append(S); continue
        for x, y in crosses:
            assert not M >> x & 1 and S >> y & 1
            assert ys[S][x] == ys[S][y] + 1
            assert rows[x] >> y & 1 and rows[y] >> x & 1
            gain = hs[S | (1 << x)] - hs[S]
            nxt = S ^ (1 << y)
            loss = hs[S] - hs[nxt]
            Z = sum(1 << w for w in range(len(P)) if ys[S][w] < P[w])
            T = sum(1 << w for w in range(len(P)) if ys[S][w] <= P[w])
            A, B = rows[x] & Z, rows[y] & T
            assert gain > d[x] and gain <= A.bit_count()
            assert A.bit_count() >= d[x] + 1
            assert A & (1 << y) and (A & ~(1 << y)) & ~B == 0
            assert B.bit_count() <= loss <= d[y] <= d[x]
            assert A.bit_count() == B.bit_count() + 1 == d[x] + 1
            assert d[x] == d[y] == loss and fs[nxt] == gamma
            assert ys[S][y] < P[y]
            # The partially saturated low receiver cannot secretly lose capacity.
            lx = min(P[x], ys[S][x]) - min(P[x], ys[S][x] - 1)
            assert lx == 0
            edges.append((S, x, y, nxt, gain, loss))
            todo.append(nxt)
    tight = [S for S in range(len(hs)) if fs[S] == gamma and hs[S] == us[S]]
    C = 0
    for S in tight: C |= S
    assert sorted(set(terminals)) == [C]
    for S in seen: assert C & ~S == 0
    for A in tight:
        for B in tight:
            assert fs[A | B] == gamma and hs[A | B] == us[A | B]
    return C, seen, edges


def inspect(P, rows, blocks, d):
    assert all(isinstance(x, int) and x >= 0 for x in d)
    assert dominance(P, rows, blocks, 'weak') and antitone(P, d, blocks)
    ys, hs, us = tables(P, rows, blocks)
    fs, gs, gamma, M = margins(hs, us, d)
    assert min(gs) == gamma
    C, seen, edges = closure(P, rows, blocks, d, ys, hs, us, fs, gamma, M)
    value, flow_M = maximal_cut(P, rows, d)
    assert value == sum(d) + gamma and flow_M == M
    return {'P': P, 'rows': rows, 'blocks': blocks, 'd': d, 'gamma': gamma,
            'Mplus': M, 'canonical': C, 'states': sorted(seen), 'edges': edges}


def scan(n, blocks, capacities, unequal=False):
    rows_all = list(digraphs(n)); profiles = cases = starts = edges_count = states = 0
    fractional_margins = 0; stream = sha256(); example = None
    for P in product(capacities, repeat=n):
        if unequal:
            ds = [d for d in product((0, 1, 2), repeat=n) if antitone(P, d, blocks)]
        else:
            ds = [tuple(next(ld[i] for i, B in enumerate(blocks) if u in B)
                        for u in range(n)) for ld in product((0, 1, 2), repeat=len(blocks))]
        for rows in rows_all:
            if not dominance(P, rows, blocks, 'weak'): continue
            profiles += 1
            ys, hs, us = tables(P, rows, blocks)
            for d in ds:
                cases += 1
                fs, gs, gamma, M = margins(hs, us, d)
                assert min(gs) == gamma
                C, seen, edges = closure(P, rows, blocks, d, ys, hs, us, fs, gamma, M)
                value, flow_M = maximal_cut(P, rows, d)
                assert value == sum(d) + gamma and flow_M == M
                starts += us[M] > hs[M]
                fractional_margins += Q(gamma).denominator != 1
                edges_count += len(edges); states += len(seen)
                if edges and example is None: example = inspect(P, rows, blocks, d)
                line = [P, rows, d, gamma, M, C, len(edges)]
                stream.update((json.dumps(line, separators=(',', ':'), default=str) + '\n').encode())
    return {'n': n, 'blocks': blocks, 'capacities': capacities, 'unequal_antitone_demands': unequal,
            'profiles': profiles, 'demand_instances': cases, 'flow_checks': cases,
            'fractional_minimum_instances': fractional_margins,
            'maximal_minimizer_gap_instances': starts, 'all_branch_states': states,
            'all_branch_transitions': edges_count, 'stream_sha256': stream.hexdigest(),
            'minimum_or_canonical_mismatches': 0, 'example': example}


def main():
    p = argparse.ArgumentParser(); p.add_argument('--regime', choices=['one', 'two', 'unit'], required=True)
    p.add_argument('--output', required=True); args = p.parse_args()
    out = {'result': 'PASS', 'regime': args.regime}
    if args.regime == 'one':
        out['half_integer_one_block'] = scan(3, ((0, 1, 2),), tuple(Q(i, 2) for i in range(5)), unequal=True)
    if args.regime == 'two':
        out['half_integer_two_blocks'] = scan(4, ((0, 1), (2, 3)), (Q(1, 2), Q(3, 2)))
    if args.regime == 'unit':
        out['positive_integer_demand_fractional_addition'] = inspect(
            (Q(0), Q(1, 2), Q(2), Q(0)), (6, 5, 0, 0), ((0, 1), (2,), (3,)), (1, 1, 0, 1))
        e = out['positive_integer_demand_fractional_addition']
        assert e['gamma'] == -1 and e['Mplus'] == 14 and e['canonical'] == 12
        assert e['edges'][0][4:] == (Q(3, 2), Q(1))
        # The original fully integral counterpart also has a nonzero-demand deletion.
        out['positive_integer_demand_integral_capacity'] = inspect(
            (Q(0), Q(1), Q(2), Q(0)), (6, 5, 0, 0), ((0, 1), (2,), (3,)), (1, 1, 0, 1))
        out['empty_instance'] = inspect((), (), (), ())
        out['singleton_instances'] = [inspect((Q(p, 2),), (0,), ((0,),), (d,))
                                      for p in range(5) for d in range(3)]
    out['source_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    out['dependency_sha256'] = sha256(Path('verify_closure.py').read_bytes()).hexdigest()
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True, default=str) + '\n')
    print(args.regime, 'PASS', args.output)

if __name__ == '__main__': main()
