#!/usr/bin/env python3
"""Independent, standard-library Hall closure checks. No network or services.

Uses bitset digraphs, sorted-pair rearrangement, all subset minima, a separate
Edmonds-Karp flow implementation, and every reachable neutral-deletion branch.
Run: python verify_closure.py --output CLOSURE_VERIFICATION.json
Finite checks are not a proof and not external independent mathematical review.
"""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import random


def digraphs(n):
    pairs = [(u, v) for u in range(n) for v in range(n) if u != v]
    for code in range(1 << len(pairs)):
        rows = [0] * n
        for j, (u, v) in enumerate(pairs):
            if code >> j & 1:
                rows[u] |= 1 << v
        yield tuple(rows)


def dominance(P, rows, blocks, mode='weak', omit=()):
    n = len(P)
    full = (1 << n) - 1
    incoming = tuple(sum((1 << u) for u in range(n) if rows[u] >> w & 1)
                     for w in range(n))
    for block in blocks:
        for x in block:
            for y in block:
                if P[x] >= P[y]:
                    continue
                xy, yx = rows[x] >> y & 1, rows[y] >> x & 1
                if 'pair' not in omit:
                    if mode == 'strict' and not (xy and yx):
                        return False
                    if mode == 'weak' and yx and not xy:
                        return False
                outside = full ^ ((1 << x) | (1 << y))
                if 'incoming' not in omit and incoming[x] & ~incoming[y] & outside:
                    return False
                if 'outgoing' not in omit and rows[x] & ~rows[y] & outside:
                    return False
    return True


def antitone(P, d, blocks):
    return all(P[x] >= P[y] or d[x] >= d[y]
               for B in blocks for x in B for y in B)


def tables(P, rows, blocks):
    n = len(P)
    incoming = tuple(sum((1 << u) for u in range(n) if rows[u] >> w & 1)
                     for w in range(n))
    psorted = [sorted(P[w] for w in B) for B in blocks]
    ys, hs, us = [], [], []
    for S in range(1 << n):
        y = tuple((S & incoming[w]).bit_count() for w in range(n))
        H = sum(min(P[w], y[w]) for w in range(n))
        # Independent of the original checker: no threshold-count formula here.
        U = sum(sum(min(a, b) for a, b in zip(psorted[i], sorted(y[w] for w in B)))
                for i, B in enumerate(blocks))
        assert U >= H
        ys.append(y); hs.append(H); us.append(U)
    return ys, hs, us


def margins(hs, us, d):
    ds = [sum(d[u] for u in range(len(d)) if S >> u & 1)
          for S in range(len(hs))]
    fs = [h - v for h, v in zip(hs, ds)]
    gs = [u - v for u, v in zip(us, ds)]
    gamma = min(fs)
    minima = [S for S, f in enumerate(fs) if f == gamma]
    maximal = 0
    for S in minima:
        maximal |= S
    assert fs[maximal] == gamma
    return fs, gs, gamma, maximal


def crossings(P, y, blocks):
    # A layer-cake gap is equivalent to an integer m in this interval.
    return [(x, z, max(P[x] + 1, y[z] + 1))
            for B in blocks for x in B for z in B
            if max(P[x] + 1, y[z] + 1) <= min(P[z], y[x])]


def all_deletions(P, rows, blocks, d, ys, hs, us, fs, gamma, maximal):
    """Checks EVERY possible crossing choice along every reachable branch."""
    pending, seen, terminals, edges = [maximal], set(), [], []
    while pending:
        S = pending.pop()
        if S in seen:
            continue
        seen.add(S)
        assert fs[S] == gamma
        cs = crossings(P, ys[S], blocks)
        assert bool(cs) == (us[S] > hs[S])
        if not cs:
            terminals.append(S)
            continue
        for x, z, m in cs:
            assert not S >> x & 1 and S >> z & 1
            assert not maximal >> x & 1
            assert ys[S][x] == m and ys[S][z] == m - 1
            assert rows[x] >> z & 1 and rows[z] >> x & 1
            Z = sum(1 << w for w in range(len(P)) if ys[S][w] < P[w])
            T = sum(1 << w for w in range(len(P)) if ys[S][w] <= P[w])
            A, B = rows[x] & Z, rows[z] & T
            assert A & (1 << z)
            assert (A & ~(1 << z)) & ~B == 0
            assert A.bit_count() >= d[x] + 1
            assert B.bit_count() <= d[z]
            assert A.bit_count() == d[x] + 1 == d[z] + 1 == B.bit_count() + 1
            nxt = S ^ (1 << z)
            assert fs[nxt] == gamma
            assert ys[S][z] < P[z]
            edges.append((S, x, z, m, nxt))
            pending.append(nxt)
    terminals = sorted(set(terminals))
    # New canonical-witness claim: every branch has the same terminal, and it
    # is the greatest exact minimum with pointwise rearrangement equality.
    tight_minima = [T for T in range(len(hs)) if fs[T] == gamma and hs[T] == us[T]]
    canonical = 0
    for T in tight_minima:
        canonical |= T
    assert terminals == [canonical]
    for A in tight_minima:
        for B in tight_minima:
            assert fs[A | B] == gamma and hs[A | B] == us[A | B]
    for S in seen:
        assert canonical & ~S == 0
    return seen, edges, terminals


def maximal_cut(P, rows, d):
    """Integral max flow and the MAXIMAL source-side minimum cut, not minimal."""
    n = len(P); size = 2 * n + 2; source = 2 * n; sink = source + 1
    cap = [[0] * size for _ in range(size)]
    for u in range(n):
        cap[source][u] = d[u]
        cap[n + u][sink] = P[u]
        for w in range(n):
            if rows[u] >> w & 1:
                cap[u][n + w] = 1
    residual = [row[:] for row in cap]
    value = 0
    while True:
        parent = [-1] * size; parent[source] = source
        q = deque([source])
        while q and parent[sink] == -1:
            u = q.popleft()
            for v in range(size):
                if residual[u][v] > 0 and parent[v] == -1:
                    parent[v] = u; q.append(v)
        if parent[sink] == -1:
            break
        delta = None; v = sink
        while v != source:
            u = parent[v]
            delta = residual[u][v] if delta is None else min(delta, residual[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]; residual[u][v] -= delta; residual[v][u] += delta; v = u
        value += delta
    # Nodes from which the sink is reachable, computed by reverse traversal.
    reaches_sink = {sink}; q = deque([sink])
    while q:
        v = q.popleft()
        for u in range(size):
            if residual[u][v] > 0 and u not in reaches_sink:
                reaches_sink.add(u); q.append(u)
    side = set(range(size)) - reaches_sink
    assert source in side and sink not in side
    cut = sum(cap[u][v] for u in side for v in range(size) if v not in side)
    assert cut == value
    flow = [[cap[u][v] - residual[u][v] for v in range(size)] for u in range(size)]
    for u in range(size):
        balance = sum(flow[u])
        assert balance == (value if u == source else -value if u == sink else 0)
        for v in range(size):
            assert flow[u][v] == -flow[v][u]
            if cap[u][v]:
                assert 0 <= flow[u][v] <= cap[u][v]
    M = sum(1 << u for u in range(n) if u in side)
    return value, M


def instance(P, rows, blocks, d, flow=True):
    ys, hs, us = tables(P, rows, blocks)
    fs, gs, gamma, M = margins(hs, us, d)
    assert min(gs) == gamma
    seen, edges, terminals = all_deletions(P, rows, blocks, d, ys, hs, us, fs, gamma, M)
    if flow:
        value, flow_M = maximal_cut(P, rows, d)
        assert value == sum(d) + gamma and flow_M == M
    return {'P': P, 'rows': rows, 'blocks': blocks, 'd': d, 'gamma': gamma,
            'Mplus': M, 'H_Mplus': hs[M], 'U_Mplus': us[M],
            'states': sorted(seen), 'deletion_edges': edges, 'terminals': terminals}


def scan(n, blocks, capacities, layer_demands=None, unequal=False, mode='strict'):
    demand_list = tuple(tuple(d) for d in (layer_demands or ()))
    cases, profiles, gaps, gap_sets, start_gap, transitions, states = 0, 0, 0, 0, 0, 0, 0
    weak_only, unequal_cases, max_depth = 0, 0, 0
    stream = sha256(); examples = {}; rows_all = list(digraphs(n))
    for P in product(capacities, repeat=n):
        if unequal:
            ds = [d for d in product((0, 1, 2), repeat=n) if antitone(P, d, blocks)]
        else:
            ds = [tuple(next(d[i] for i, B in enumerate(blocks) if u in B) for u in range(n))
                  for d in demand_list]
        for rows in rows_all:
            if not dominance(P, rows, blocks, mode):
                continue
            profiles += 1
            ys, hs, us = tables(P, rows, blocks)
            point_gaps = sum(u > h for u, h in zip(us, hs))
            is_weak_only = not dominance(P, rows, blocks, 'strict')
            for d in ds:
                cases += 1
                gaps += bool(point_gaps); gap_sets += point_gaps
                weak_only += is_weak_only
                unequal_here = any(len({d[u] for u in B}) > 1 for B in blocks)
                unequal_cases += unequal_here
                fs, gs, gamma, M = margins(hs, us, d)
                assert min(gs) == gamma, (P, rows, blocks, d, gamma, min(gs))
                seen, edges, terminals = all_deletions(P, rows, blocks, d, ys, hs, us, fs, gamma, M)
                value, flow_M = maximal_cut(P, rows, d)
                assert value == sum(d) + gamma and flow_M == M
                states += len(seen); transitions += len(edges)
                start_gap += us[M] > hs[M]
                depth = max(M.bit_count() - t.bit_count() for t in terminals)
                max_depth = max(max_depth, depth)
                record = [P, rows, d, gamma, M, terminals, len(edges)]
                stream.update((json.dumps(record, separators=(',', ':')) + '\n').encode())
                keys = []
                if us[M] > hs[M]: keys.append('maximal_minimizer_gap')
                if len(terminals) > 1: keys.append('order_dependence')
                if depth >= 2: keys.append('multiple_deletions')
                if point_gaps and 'pointwise_gap' not in examples: keys.append('pointwise_gap')
                if is_weak_only and unequal_here and point_gaps:
                    keys.append('strict_extension_with_gap')
                for key in keys:
                    if key not in examples:
                        examples[key] = instance(P, rows, blocks, d, flow=False)
    if not unequal:
        assert cases == profiles * len(demand_list)
    return {'n': n, 'blocks': blocks, 'capacities': capacities, 'mode': mode,
            'unequal_antitone_demands': unequal, 'valid_profiles': profiles,
            'demand_instances': cases, 'pointwise_gap_instances': gaps,
            'pointwise_gap_source_sets': gap_sets, 'maximal_minimizer_gap_instances': start_gap,
            'all_branch_states': states, 'all_branch_transitions': transitions,
            'max_deletion_depth': max_depth, 'weak_not_strict_instances': weak_only,
            'unequal_within_block_instances': unequal_cases,
            'flow_and_maximal_cut_checks': cases, 'minimum_mismatches': 0,
            'stream_sha256': stream.hexdigest(), 'examples': examples}


def witness(P, rows, blocks, d):
    ys, hs, us = tables(P, rows, blocks)
    fs, gs, gamma, M = margins(hs, us, d)
    return {'P': P, 'rows': rows, 'blocks': blocks, 'd': d,
            'exact_min': gamma, 'rearranged_min': min(gs),
            'subsets': [{'S': S, 'y': ys[S], 'H': hs[S], 'U': us[S],
                         'F': fs[S], 'U_minus_D': gs[S]} for S in range(len(hs))]}


def find_axiom_counterexample(omitted, mode='weak'):
    for n in range(2, 5):
        # Two vertices in the crossing block; other vertices have independent demands.
        partitions = [tuple([tuple(range(n))])]
        if n > 2:
            partitions.append(tuple([(0, 1)] + [(i,) for i in range(2, n)]))
        for blocks in partitions:
            for P in product((0, 1, 2), repeat=n):
                for rows in digraphs(n):
                    if not dominance(P, rows, blocks, mode, omit=(omitted,)):
                        continue
                    if dominance(P, rows, blocks, mode):
                        continue
                    ys, hs, us = tables(P, rows, blocks)
                    if hs == us:
                        continue
                    for ld in product((0, 1, 2), repeat=len(blocks)):
                        d = tuple(next(ld[i] for i, B in enumerate(blocks) if u in B)
                                  for u in range(n))
                        fs, gs, gamma, M = margins(hs, us, d)
                        if gamma != min(gs):
                            return witness(P, rows, blocks, d)
    return None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', default='CLOSURE_VERIFICATION.json')
    ap.add_argument('--regime', choices=['one', 'two', 'weak', 'adversarial', 'random', 'all'], default='all')
    args = ap.parse_args(); out = {'result': 'PASS', 'regime': args.regime}
    if args.regime in ('one', 'all'):
        out['original_one_layer_independent'] = scan(4, ((0, 1, 2, 3),), (0, 1, 2), ((0,), (1,), (2,)))
    if args.regime in ('two', 'all'):
        out['original_two_layer_independent'] = scan(4, ((0, 1), (2, 3)), (0, 1), tuple(product((0, 1, 2), repeat=2)))
    if args.regime in ('weak', 'all'):
        out['weakened_unequal_one_layer'] = scan(3, ((0, 1, 2),), (0, 1, 2), unequal=True, mode='weak')
        out['weakened_unequal_two_layer'] = scan(4, ((0, 1), (2, 3)), (0, 1), unequal=True, mode='weak')
    if args.regime in ('adversarial', 'all'):
        out['dropped_axioms'] = {k: find_axiom_counterexample(k) for k in ('pair', 'incoming', 'outgoing')}
        out['strict_dropped_axioms'] = {k: find_axiom_counterexample(k, 'strict') for k in ('pair', 'incoming', 'outgoing')}
        out['real_demands_fail'] = witness((0, 1), (2, 1), ((0, 1),), (Fraction(1, 2),) * 2)
        out['demand_order_fails'] = witness((0, 1), (2, 1), ((0, 1),), (0, 1))
        for v in list(out['dropped_axioms'].values()) + list(out['strict_dropped_axioms'].values()) + [out['real_demands_fail'], out['demand_order_fails']]:
            assert v is not None and v['exact_min'] < v['rearranged_min']
        out['U_not_submodular'] = witness((0, 0, 2), (4, 4, 3), ((0, 1, 2),), (1, 1, 1))
        u = [r['U'] for r in out['U_not_submodular']['subsets']]
        assert u[5] + u[6] < u[7] + u[4]
        out['tight_minima_not_intersection_closed'] = witness((0, 2, 0), (2, 1, 2), ((0, 1), (2,)), (1, 1, 1))
        t = out['tight_minima_not_intersection_closed']['subsets']
        assert t[3]['F'] == t[6]['F'] == t[2]['F'] == -1
        assert t[3]['H'] == t[3]['U'] and t[6]['H'] == t[6]['U'] and t[2]['H'] < t[2]['U']
    if args.regime in ('random', 'all'):
        rng = random.Random(74220260927); accepted = 0; examined = 0; stream = sha256()
        examples = {}; sizes = {}; max_depth = 0
        # Directed block-threshold construction; not uniform random digraphs.
        while accepted < 1500:
            examined += 1; n = rng.randint(5, 9)
            labels = [rng.randrange(3) for _ in range(n)]
            blocks = tuple(tuple(u for u in range(n) if labels[u] == j)
                           for j in sorted(set(labels)))
            scores = [rng.randrange(5) for _ in range(n)]
            threshold = [[rng.randrange(1, 13) for _ in range(3)] for _ in range(3)]
            rows = tuple(sum(1 << w for w in range(n) if u != w
                             and scores[u] + 2 * scores[w] >= threshold[labels[u]][labels[w]])
                         for u in range(n))
            P = tuple(scores)
            base = [rng.randrange(n + 1) for _ in range(3)]
            if accepted % 2:
                d = tuple(base[labels[u]] for u in range(n))
            else:
                d = tuple(max(0, base[labels[u]] - scores[u] // 2) for u in range(n))
            assert dominance(P, rows, blocks, 'weak') and antitone(P, d, blocks)
            rec = instance(P, rows, blocks, d)
            accepted += 1; sizes[n] = sizes.get(n, 0) + 1
            depth = max(rec['Mplus'].bit_count() - t.bit_count() for t in rec['terminals'])
            max_depth = max(max_depth, depth)
            if depth and 'deletions' not in examples:
                examples['deletions'] = rec
            stream.update((json.dumps(rec, separators=(',', ':')) + '\n').encode())
        out['structured_random'] = {'seed': 74220260927, 'cases': accepted, 'sizes': sizes,
                                    'max_depth': max_depth, 'stream_sha256': stream.hexdigest(),
                                    'qualification': 'Structured directed block-threshold family, not uniform over WCD systems.',
                                    'examples': examples}
        n = 13
        P = tuple([0, 1] * 6 + [0])
        rows = tuple([(1 << (u ^ 1)) for u in range(12)] + [0])
        blocks = tuple([(2*j, 2*j+1) for j in range(6)] + [(12,)])
        d = tuple([0] * 12 + [1])
        out['six_deletion_diamond'] = instance(P, rows, blocks, d)
        assert out['six_deletion_diamond']['gamma'] == -1
        assert len(out['six_deletion_diamond']['states']) == 64
        assert len(out['six_deletion_diamond']['deletion_edges']) == 192
        assert out['six_deletion_diamond']['terminals'] == [1 << 12]
    out['source_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    def serial(x):
        if isinstance(x, Fraction): return str(x)
        raise TypeError(type(x).__name__)
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True, default=serial) + '\n')
    print(json.dumps({'result': out['result'], 'regime': args.regime, 'output': args.output}))


if __name__ == '__main__':
    main()
