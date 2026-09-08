#!/usr/bin/env python3
"""Independent finite audit of the complement edge-insertion -> quasi-edge bridge.

This program deliberately does not import or call the layer-sum selected-system
constructor. It rebuilds every labelled simple graph on 3..6 vertices, tests
D2 edge-criticality directly by edge deletion, chooses every minimum-complement-
degree root, inserts every missing H[B] edge, enumerates every adjacent total-
dominating pair in H+uw, and verifies the structural characterization used by
the proof.
"""
from itertools import combinations
from hashlib import sha256
import json


def graph_from_mask(n, mask):
    adj = [0] * n
    for k, (u, v) in enumerate(combinations(range(n), 2)):
        if (mask >> k) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def diameter_at_most_two(adj):
    n = len(adj)
    allv = (1 << n) - 1
    for u in range(n):
        reach = (1 << u) | adj[u]
        for v in range(n):
            if (adj[u] >> v) & 1:
                reach |= adj[v]
        if reach != allv:
            return False
    return True


def critical(adj):
    if not diameter_at_most_two(adj):
        return False
    for u, v in combinations(range(len(adj)), 2):
        if not ((adj[u] >> v) & 1):
            continue
        changed = adj.copy()
        changed[u] ^= 1 << v
        changed[v] ^= 1 << u
        if diameter_at_most_two(changed):
            return False
    return True


def complement(adj):
    n = len(adj)
    allv = (1 << n) - 1
    return [allv ^ (1 << u) ^ adj[u] for u in range(n)]


def adjacent_total_dominates(H, x, y):
    return bool((H[x] >> y) & 1) and (H[x] | H[y]) == (1 << len(H)) - 1


def run():
    stats = {
        'graphs': 0,
        'critical_graphs': 0,
        'minimum_degree_roots': 0,
        'missing_B_pairs': 0,
        'new_adjacent_total_dominating_pairs': 0,
        'valid_quasi_edges': 0,
    }
    digest = sha256()
    for n in range(3, 7):
        for mask in range(1 << (n * (n - 1) // 2)):
            stats['graphs'] += 1
            G = graph_from_mask(n, mask)
            if not critical(G):
                continue
            stats['critical_graphs'] += 1
            H = complement(G)
            hdeg = [x.bit_count() for x in H]
            minimum = min(hdeg)
            roots = [v for v in range(n) if hdeg[v] == minimum]
            stats['minimum_degree_roots'] += len(roots)

            # Diameter <=2 in G means H has no adjacent total dominating pair.
            assert not any(adjacent_total_dominates(H, x, y)
                           for x, y in combinations(range(n), 2))

            for v in roots:
                A = [i for i in range(n) if (H[v] >> i) & 1]
                B = [u for u in range(n) if u != v and not ((H[v] >> u) & 1)]
                for u, w in combinations(B, 2):
                    if (H[u] >> w) & 1:
                        continue
                    stats['missing_B_pairs'] += 1
                    H2 = H.copy()
                    H2[u] |= 1 << w
                    H2[w] |= 1 << u
                    pairs = [(x, y) for x, y in combinations(range(n), 2)
                             if adjacent_total_dominates(H2, x, y)]
                    assert pairs
                    stats['new_adjacent_total_dominating_pairs'] += len(pairs)
                    records = []
                    for x, y in pairs:
                        # {u,w} itself misses the root v, so cannot be the pair.
                        assert {x, y} != {u, w}
                        incident = int(x in (u, w)) + int(y in (u, w))
                        assert incident == 1
                        source = x if x in (u, w) else y
                        label = y if x in (u, w) else x
                        supplement = w if source == u else u
                        # The auxiliary must dominate v, so lies in A.
                        assert label in A
                        # Its source-label edge already existed in H.
                        assert (H[source] >> label) & 1
                        # Before insertion the pair has exactly the opposite
                        # endpoint as its unique undominated vertex.
                        all_except = ((1 << n) - 1) ^ (1 << supplement)
                        assert (H[source] | H[label]) == all_except
                        stats['valid_quasi_edges'] += 1
                        records.append((source, label, supplement))
                    digest.update((json.dumps([n, mask, v, u, w, pairs, records],
                                              separators=(',', ':')) + '\n').encode())
    return {
        'status': 'PASS',
        'scope': ('all labelled simple graphs 3<=n<=6; every minimum-complement-'
                  'degree root; every missing pair in B; every adjacent total-'
                  'dominating pair created by insertion'),
        'stats': stats,
        'ordered_case_sha256': digest.hexdigest(),
        'expected_ordered_case_sha256':
            '1f2b1bb5bd91d54937f166abd0c26badd8ddd105441cd37a6d0150c557d46c5e',
        'independent_implementation_note':
            'Does not call the layer-sum selected-system constructor.',
        'formal_proof': False,
        'external_independence': False,
    }


if __name__ == '__main__':
    result = run()
    assert result['ordered_case_sha256'] == result['expected_ordered_case_sha256']
    print(json.dumps(result, indent=2))
