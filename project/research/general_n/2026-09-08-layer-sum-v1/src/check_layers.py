#!/usr/bin/env python3
"""Fresh bit-set audit of the selected/residual construction and layer bound.
Python standard library only. Small graphs and all their selections are exhaustive;
larger graphs are deterministic greedy samples, not exhaustive graph evidence.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
import argparse
import json
from pathlib import Path


# Saved inputs from the locally installed NetworkX 3.6.1 atlas, generated this session.
# Replay below imports no NetworkX and independently checks each graph's criticality.
ATLAS7 = [{'atlas_id': 270, 'n': 7, 'adjacency_bitmasks': [64, 64, 64, 64, 64, 64, 63]}, {'atlas_id': 558, 'n': 7, 'adjacency_bitmasks': [36, 36, 27, 68, 36, 83, 40]}, {'atlas_id': 571, 'n': 7, 'adjacency_bitmasks': [102, 17, 9, 84, 42, 17, 9]}, {'atlas_id': 580, 'n': 7, 'adjacency_bitmasks': [18, 69, 10, 52, 41, 88, 34]}, {'atlas_id': 670, 'n': 7, 'adjacency_bitmasks': [124, 124, 3, 3, 3, 3, 3]}, {'atlas_id': 676, 'n': 7, 'adjacency_bitmasks': [6, 69, 59, 20, 108, 20, 18]}, {'atlas_id': 680, 'n': 7, 'adjacency_bitmasks': [54, 5, 75, 20, 105, 17, 20]}, {'atlas_id': 685, 'n': 7, 'adjacency_bitmasks': [50, 69, 42, 36, 33, 93, 34]}, {'atlas_id': 730, 'n': 7, 'adjacency_bitmasks': [98, 21, 42, 84, 42, 21, 9]}, {'atlas_id': 1007, 'n': 7, 'adjacency_bitmasks': [54, 73, 73, 54, 73, 73, 54]}]

def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def bits(mask: int):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask ^= b


def at_most_two(adj: list[int]) -> bool:
    allv = (1 << len(adj)) - 1
    return all(adj[u] & adj[w] for u in range(len(adj))
               for w in bits(allv & ~(adj[u] | (1 << u))))


def witness_critical(adj: list[int]) -> bool:
    """Direct unique-common-neighbour criterion; no edge deletions."""
    n = len(adj)
    if n < 3 or all(x.bit_count() == n-1 for x in adj) or not at_most_two(adj):
        return False
    for u, v in combinations(range(n), 2):
        if not (adj[u] >> v) & 1:
            continue
        if not (adj[u] & adj[v]):
            continue
        if any(adj[u] & adj[w] == 1 << v
               for w in bits(adj[v] & ~(adj[u] | (1 << u)))):
            continue
        if any(adj[v] & adj[w] == 1 << u
               for w in bits(adj[u] & ~(adj[v] | (1 << v)))):
            continue
        return False
    return True


def bfs_diameter_two(adj: list[int]) -> bool:
    """Separate set-based two-round breadth-first reachability implementation."""
    n = len(adj)
    if n < 3 or sum(x.bit_count() for x in adj) == n*(n-1):
        return False
    for u in range(n):
        seen = {u}
        frontier = {u}
        for _ in range(2):
            nxt = {w for v in frontier for w in range(n)
                   if (adj[v] >> w) & 1} - seen
            seen |= nxt
            frontier = nxt
        if len(seen) != n:
            return False
    return True


def deletion_critical(adj: list[int]) -> bool:
    if not bfs_diameter_two(adj):
        return False
    for u, v in combinations(range(len(adj)), 2):
        if (adj[u] >> v) & 1:
            changed = adj.copy()
            changed[u] ^= 1 << v
            changed[v] ^= 1 << u
            if bfs_diameter_two(changed):
                return False
    return True


def graph_from_mask(n: int, mask: int) -> list[int]:
    adj = [0] * n
    for k, (u, v) in enumerate(combinations(range(n), 2)):
        if (mask >> k) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def greedy(n: int, seed: int) -> list[int]:
    adj = [((1 << n)-1) ^ (1 << u) for u in range(n)]
    edges = list(combinations(range(n), 2))
    edges.sort(key=lambda e: sha256(f'layers-v1:{n}:{seed}:{e[0]}:{e[1]}'.encode()).digest())
    for u, v in edges:
        adj[u] ^= 1 << v
        adj[v] ^= 1 << u
        if not at_most_two(adj):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    require(witness_critical(adj) and deletion_critical(adj), 'greedy criticality')
    return adj


def options(adj: list[int], v: int):
    n = len(adj)
    allv = (1 << n)-1
    H = [allv ^ ((1 << u) | adj[u]) for u in range(n)]
    A, B = list(bits(H[v])), list(bits(adj[v]))
    choices = []
    for u, w in combinations(B, 2):
        if not ((adj[u] >> w) & 1):
            continue
        candidates = []
        for p, q in [(u, w), (w, u)]:
            for i in A:
                if (H[p] >> i) & 1 and (H[p] | H[i]) == allv ^ (1 << q):
                    candidates.append((p, i, q))
        require(bool(candidates), 'quasi-edge existence')
        choices.append(candidates)
    return H, A, B, choices


def check_system(adj: list[int], v: int, selected, H, A, B) -> dict:
    n, a, b = len(adj), len(A), len(B)
    allv = (1 << n)-1
    expected = {tuple(sorted((u, w))) for u, w in combinations(B, 2)
                if (adj[u] >> w) & 1}
    require(all(u in B and w in B and i in A and u != w
                for u, i, w in selected), 'selected endpoints')
    require(len(selected) == len(expected), 'selection count')
    require({tuple(sorted((u, w))) for u, i, w in selected} == expected,
            'one selection for each missing pair')
    require(len({(u, i) for u, i, w in selected}) == len(selected), 'distinct selected edges')
    for u, i, w in selected:
        require((H[u] >> i) & 1 and (H[u] | H[i]) == allv ^ (1 << w), 'unique exception')
    chosen = {(u, i) for u, i, w in selected}
    residual = {(u, i) for u in B for i in A if (H[u] >> i) & 1} - chosen
    rho = {u: sum((u, i) in residual for i in A) for u in B}
    R = {i: sum((u, i) in residual for u in B) for i in A}
    x = {i: sum((u, i) in chosen for u in B) for i in A}
    q = {u: sum((u, i) in chosen for i in A) for u in B}
    d = {i: sum((adj[i] >> j) & 1 for j in A) for i in A}
    s = {i: max(0, d[i]-R[i]) for i in A}
    r, S = sum(rho.values()), sum(s.values())
    m = sum(t.bit_count() for t in adj)//2
    t = m-b*(n-b)
    require(sum(d.values()) == 2*(r+t), 'edge ledger')
    require(sum(R.values()) == r, 'residual ledger')
    require(S >= r+2*t, 'demand ledger')
    require(all(x[i] >= s[i] for i in A), 'minimum-degree demand')
    require(all(rho[u]+q[u] <= a for u in B), 'source capacity')
    for u, i, w in selected:
        # Explicitly rebuild the injection proving s_i <= rho_u.
        forced = []
        for j in A:
            if not ((adj[i] >> j) & 1):
                continue
            require((H[u] >> j) & 1, 'F-neighbour adjacency')
            if (u, j) in chosen:
                wj = next(ww for uu, jj, ww in selected if uu == u and jj == j)
                require(wj != w and (wj, i) in residual, 'residual injection target')
                forced.append(wj)
        require(len(forced) == len(set(forced)), 'residual injection injectivity')
        require(d[i] <= rho[u]+R[i] and s[i] <= rho[u], 'source lower bound')
        require(d[i] <= rho[u]+rho[w], 'supplement lower bound')
        require(all((H[w] >> j) & 1 for uu, j, ww in selected if uu == u and j != i),
                'supplement neighbours other selected labels')
    if a:
        require(all(0 <= s[i] < a for i in A), 'demand range')
        require(F(r) >= sum((F(s[i]*s[i], a-s[i]) for i in A), F(0)), 'old charging')
    tails, nonempty = [], 0
    for h in range(1, a+1):
        I = {i for i in A if s[i] >= h}
        Z = {u for u in B if rho[u] >= h}
        z, W = len(Z), sum(s[i] for i in I)
        ell = {u: sum((u, i) in chosen for i in I) for u in B}
        require(all(not ell[u] for u in B if u not in Z), 'heavy source confinement')
        busy = {u for u in Z if ell[u] > h}
        arcs = [(u, w) for u, i, w in selected if u in busy and i in I]
        require(all(w in Z for u, w in arcs), 'heavy supplement confinement')
        j = len(busy)
        require(len(arcs) <= j*z-j*(j+1)//2, 'unordered busy pair capacity')
        X = sum(ell.values())
        require(W <= X <= (z-j)*h+j*z-j*(j+1)//2, 'exact j capacity')
        require(not W or z >= h, 'heavy-label source count')
        if z >= h:
            require(W <= h*z+(z-h)*(z-h-1)//2, 'threshold capacity')
        else:
            require(W == 0, 'empty low-source tail')
        require(W <= z*z, 'square tail bound')
        tails.append((h, W, z))
        nonempty += bool(W)
    require(sum(W for h, W, z in tails) == sum(si*si for si in s.values()), 'demand layer cake')
    require(sum(z for h, W, z in tails) == r, 'residual layer cake')
    require(S**3 <= a*a*r*r, 'simple layer-sum bound')
    require(3*S**3 <= a*a*r*(2*r+1), 'weighted layer-sum moment inequality')
    require(648*t < 32*a*a+81, 'new quadratic coefficient and additive term')
    Hmax = max(s.values(), default=0)
    if Hmax:
        partial_r = sum(z for h, W, z in tails if h <= Hmax)
        cost = sum((F(2*W,z) for h, W,z in tails if h <= Hmax), F(0))
        require(all(z >= Hmax for h,W,z in tails if h <= Hmax), 'max-demand confinement')
        require(Hmax*Hmax <= r, 'max-demand residual cost')
        require(cost <= F(partial_r) + F(Hmax*Hmax+2,3), 'weighted summation')
        require(3*partial_r*cost <= 4*r*r+2*r, 'weighted Cauchy upper bound')
    # Exact rational threshold. The strict assertion deliberately starts at n=6.
    premise = 22*b >= 13*n
    require(not (n >= 6 and premise) or m < n*n//4, 'new degree consequence')
    return {'S': S, 'r': r, 't': t, 'a': a, 'nonempty_tails': nonempty,
            'tail_checks': len(tails), 'premise': premise, 'selected': list(selected)}


def exact_algebra() -> dict:
    count = 0
    for a in range(1, 8):
        # All demand multisets in this finite arithmetic domain; no graph claim.
        from itertools import combinations_with_replacement
        for s in combinations_with_replacement(range(a), a):
            S = sum(s)
            W = [sum(si for si in s if si >= h) for h in range(1, a)]
            lower_z = []
            for h, w in enumerate(W, 1):
                z = 0 if not w else h
                while w and h*z+(z-h)*(z-h-1)//2 < w:
                    z += 1
                lower_z.append(z)
            # True source tails are nonincreasing, so close the necessary lower bounds.
            for k in range(len(lower_z)-2, -1, -1):
                lower_z[k] = max(lower_z[k], lower_z[k+1])
            rlower = sum(lower_z)
            require(S**3 <= a*a*rlower*rlower, 'multiset cubic consequence')
            require(3*S**3 <= a*a*rlower*(2*rlower+1), 'multiset weighted moment')
            require(324*(S-rlower) < 32*a*a+81, 'multiset coefficient consequence')
            count += 1
    # Rational identity establishes the scalar maximum; finite regression of it.
    ids = 0
    for denom in range(1, 101):
        for numer in range(0, 2*denom+1):
            y = F(numer, denom)
            require(F(4,27)-y*y+y**3 == (y-F(2,3))**2*(y+F(1,3)), 'scalar identity')
            ids += 1
    require(F(4,81)*9 > F(3,8), 'all a>=4 rounding margin')
    require(F(4,81)*4+F(1,8) < 1, 'a=2 rounding case')
    require(F(4,81)*9+F(1,8) < 1, 'a=3 rounding case')
    require((F(13,22)-F(1,2))/(1-F(13,22)) == F(2,9), 'rational degree threshold')
    require(F(2,1)/(27*F(3,2)) == F(4,81), 'scalar coefficient')
    return {'demand_multisets': count, 'scalar_identity_cases': ids,
            'coefficient': '4/81', 'additive_term': '1/8',
            'cubic': '3 S^3 <= a^2 r(2r+1)', 'degree_threshold': '13/22 for n>=6',
            'formal_proof': False}



def run() -> dict:
    report = {'small_graph_masks': {}, 'small_graph_domain': 'all labelled simple graphs 3<=n<=6',
              'small_selection_scope': 'all max-degree roots, all quasi-edge choices',
              'generated_graphs': [], 'atlas7_input': ATLAS7, 'counts': {'graphs_considered': 0, 'critical_graphs': 0,
              'criticality_crosschecks': 0, 'small_systems': 0, 'sample_systems': 0, 'atlas7_systems': 0,
              'nonzero_demand_systems': 0, 'positive_surplus_systems': 0,
              'tail_checks': 0, 'nonempty_tail_checks': 0, 'degree_premise_systems': 0},
              'actual_graph_status': 'regression, not proof by extrapolation'}
    digest = sha256()
    control = None
    def consume(adj, exhaustive, key, kind=None):
        nonlocal control
        for v, row in enumerate(adj):
            if row.bit_count() != max(x.bit_count() for x in adj):
                continue
            H, A, B, choices = options(adj, v)
            if exhaustive:
                selections = product(*choices)
            else:
                sels = [tuple(opt[0] for opt in choices), tuple(opt[-1] for opt in choices)]
                selections = list(dict.fromkeys(sels))
            for selected in selections:
                out = check_system(adj, v, selected, H, A, B)
                digest.update((json.dumps([key, v, out], sort_keys=True, separators=(',', ':'))+'\n').encode())
                c = report['counts']
                c[kind or ('small_systems' if exhaustive else 'sample_systems')] += 1
                c['nonzero_demand_systems'] += out['S'] > 0
                c['positive_surplus_systems'] += out['t'] > 0
                c['tail_checks'] += out['tail_checks']
                c['nonempty_tail_checks'] += out['nonempty_tails']
                c['degree_premise_systems'] += out['premise']
                if selected and control is None:
                    control = (adj, v, selected, H, A, B)
    for n in range(3, 7):
        report['small_graph_masks'][str(n)] = []
        for mask in range(1 << (n*(n-1)//2)):
            adj = graph_from_mask(n, mask)
            fast = witness_critical(adj)
            require(fast == deletion_critical(adj), 'criticality implementation agreement')
            report['counts']['criticality_crosschecks'] += 1
            report['counts']['graphs_considered'] += 1
            if not fast:
                continue
            report['small_graph_masks'][str(n)].append(mask)
            report['counts']['critical_graphs'] += 1
            consume(adj, True, [n, mask])
    for record in ATLAS7:
        adj = record['adjacency_bitmasks']
        require(witness_critical(adj) and deletion_critical(adj), 'saved atlas criticality')
        consume(adj, True, ['atlas7', record['atlas_id']], 'atlas7_systems')
    for n in [8, 10, 12, 16, 20]:
        for seed in range(8):
            adj = greedy(n, seed)
            report['generated_graphs'].append({'n': n, 'seed': seed, 'adjacency_bitmasks': adj})
            consume(adj, False, ['greedy', n, seed])
    require(control is not None, 'nonvacuous selection negative controls')
    adj, v, selected, H, A, B = control
    bad = [selected[:-1], selected+(selected[0],),
           ((selected[0][0], selected[0][1], selected[0][0]),)+selected[1:]]
    rejected = []
    for label, case in zip(['missing_selection', 'duplicate_selection', 'self_supplement'], bad):
        try:
            check_system(adj, v, case, H, A, B)
        except AssertionError as exc:
            rejected.append({'control': label, 'reason': str(exc)})
        else:
            raise AssertionError('negative control unexpectedly passed: '+label)
    report['negative_controls'] = rejected
    report['system_sha256'] = digest.hexdigest()
    # K(2,3) is a mandatory boundary counterexample to n>=4 strictness.
    k23 = [28,28,3,3,3]
    require(witness_critical(k23) and deletion_critical(k23), 'K23 critical')
    require(22*3 >= 13*5 and sum(v.bit_count() for v in k23)//2 == 25//4,
            'K23 violates an overbroad strict n>=4 statement')
    report['small_order_boundary_control'] = 'K(2,3) confirms n>=6 scope is necessary'
    report['algebra'] = exact_algebra()
    report['status'] = 'PASS'
    report['independent_external_review'] = 'OPEN'
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        if args.output.exists():
            raise FileExistsError(args.output)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end='')

if __name__ == '__main__':
    main()
