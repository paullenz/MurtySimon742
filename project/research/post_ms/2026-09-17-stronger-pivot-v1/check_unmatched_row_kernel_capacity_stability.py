#!/usr/bin/env python3
"""Finite regression for UNMATCHED_ROW_KERNEL_CAPACITY_STABILITY.md.

This checker is evidence only.  The universal statements in the note are
proved by hand.  It independently checks:

* exact tau(Psi(K)) on every unlabelled graph of orders 3..7;
* the row-kernel/twin consequence for an exact minimum cover;
* the complete tau<=2 structural classification;
* the maximum-code-degree lower bound;
* the alpha/beta translation and matched-antipode eligibility identities
  for every signing and every row code at p=3,4,5;
* the projective-alpha multiplicity = maximum switched true-twin class
  identity for every signing at p=3,4,5;
* the beta-pool Hamming intersection formula for p=3..8.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter

import networkx as nx


def psi(K: nx.Graph):
    p = K.number_of_nodes()
    edges = []
    vertices = set()
    for i in range(p):
        A = frozenset(j for j in range(p) if j != i and not K.has_edge(i, j))
        S = frozenset((i,))
        edges.append((A, S))
        vertices.add(A)
        vertices.add(S)
    return sorted(vertices, key=lambda x: (len(x), tuple(x))), edges


def exact_tau(K: nx.Graph):
    vertices, edges = psi(K)
    for r in range(len(vertices) + 1):
        for comb in itertools.combinations(vertices, r):
            C = set(comb)
            if all(a in C or b in C for a, b in edges):
                return r, C
    raise AssertionError("no cover")


def complete_bipartite_allow_empty(L: nx.Graph) -> bool:
    if L.number_of_edges() == 0:
        return True
    if not nx.is_bipartite(L):
        return False
    colour = nx.bipartite.color(L)
    A = [v for v in L if colour[v] == 0]
    B = [v for v in L if colour[v] == 1]
    return L.number_of_edges() == len(A) * len(B)


def star_plus_isolates(L: nx.Graph) -> bool:
    if L.number_of_edges() == 0:
        return True
    V = list(L.nodes())
    for x in V:
        if all(not L.has_edge(a, b)
               for a, b in itertools.combinations([v for v in V if v != x], 2)):
            return True
    return False


def two_centre_form(L: nx.Graph) -> bool:
    V = list(L.nodes())
    for x, y in itertools.combinations(V, 2):
        good = True
        for z in V:
            if z in (x, y):
                continue
            if set(L.neighbors(z)) not in ({x}, {y}):
                good = False
                break
        if good:
            return True
    return False


def tau_le_two_form(L: nx.Graph) -> bool:
    return (complete_bipartite_allow_empty(L)
            or star_plus_isolates(L)
            or two_centre_form(L))


def bits(mask: int, p: int):
    return tuple((mask >> i) & 1 for i in range(p))


def complement(code):
    return tuple(1 - x for x in code)


def all_signings(p: int):
    pairs = [(i, j) for i in range(p) for j in range(i + 1, p)]
    for mask in range(1 << len(pairs)):
        sigma = [[0] * p for _ in range(p)]
        for bitpos, (i, j) in enumerate(pairs):
            z = (mask >> bitpos) & 1
            sigma[i][j] = sigma[j][i] = z
        yield sigma


def alpha(sigma, i: int, endpoint_bit: int):
    p = len(sigma)
    return tuple((1 - endpoint_bit) ^ (sigma[i][j] if j != i else 0)
                 for j in range(p))


def beta(code, i: int):
    return tuple(code[j] if j == i else 1 - code[j] for j in range(len(code)))


def switched_graph(sigma, code):
    p = len(code)
    K = nx.Graph()
    K.add_nodes_from(range(p))
    for i in range(p):
        for j in range(i + 1, p):
            if code[j] == (code[i] ^ sigma[i][j]):
                K.add_edge(i, j)
    return K


def symmetric_difference_code(a, b):
    return frozenset(i for i, (x, y) in enumerate(zip(a, b)) if x != y)


def max_true_twin_class(K: nx.Graph) -> int:
    sigs = Counter()
    for i in K:
        sigs[frozenset({i} | set(K.neighbors(i)))] += 1
    return max(sigs.values(), default=0)


def main():
    tau_distributions = {}
    atlas_graphs = 0
    tau2_mismatches = 0
    kernel_violations = 0
    degree_bound_violations = 0

    for p in range(3, 8):
        graphs = [g for g in nx.graph_atlas_g() if g.number_of_nodes() == p]
        dist = Counter()
        for K in graphs:
            tau, cover = exact_tau(K)
            dist[tau] += 1
            L = nx.complement(K)
            if (tau <= 2) != tau_le_two_form(L):
                tau2_mismatches += 1

            A = [frozenset(j for j in range(p) if j != i and not K.has_edge(i, j))
                 for i in range(p)]
            mult = Counter(A)
            D = max(
                [mult[C] + (1 if len(C) == 1 else 0) for C in mult]
                + [1 + mult.get(frozenset((j,)), 0) for j in range(p)]
            )
            if tau < math.ceil(p / D):
                degree_bound_violations += 1

            X = {next(iter(C)) for C in cover if len(C) == 1}
            if len({A[i] for i in range(p) if i not in X}) > tau:
                kernel_violations += 1
            for i, j in itertools.combinations([x for x in range(p) if x not in X], 2):
                if A[i] == A[j]:
                    Ni = frozenset({i} | set(K.neighbors(i)))
                    Nj = frozenset({j} | set(K.neighbors(j)))
                    if Ni != Nj:
                        kernel_violations += 1

        tau_distributions[str(p)] = {str(k): v for k, v in sorted(dist.items())}
        atlas_graphs += len(graphs)

    signing_instances = 0
    coordinate_identity_checks = 0
    mu_twin_violations = 0
    coordinate_identity_violations = 0

    for p in range(3, 6):
        for sigma in all_signings(p):
            signing_instances += 1
            rows = [tuple(sigma[i][j] if j != i else 0 for j in range(p))
                    for i in range(p)]
            alpha_mult = Counter()
            for i in range(p):
                for s in (0, 1):
                    alpha_mult[alpha(sigma, i, s)] += 1
            mu_alpha = max(alpha_mult.values())
            projective = Counter(min(r, complement(r)) for r in rows)
            if mu_alpha != max(projective.values()):
                mu_twin_violations += 1

            max_twins = 0
            for mask in range(1 << p):
                c = bits(mask, p)
                max_twins = max(max_twins, max_true_twin_class(switched_graph(sigma, c)))
            if mu_alpha != max_twins:
                mu_twin_violations += 1

            for mask in range(1 << p):
                c = bits(mask, p)
                bar_c = complement(c)
                K = switched_graph(sigma, c)
                for i in range(p):
                    A_i = frozenset(j for j in range(p)
                                    if j != i and not K.has_edge(i, j))
                    if symmetric_difference_code(alpha(sigma, i, c[i]), bar_c) != A_i:
                        coordinate_identity_violations += 1
                    if symmetric_difference_code(beta(c, i), bar_c) != frozenset((i,)):
                        coordinate_identity_violations += 1
                    eligible = alpha(sigma, i, 1 - c[i]) == c
                    universal = all(K.has_edge(i, j) for j in range(p) if j != i)
                    if eligible != universal:
                        coordinate_identity_violations += 1
                    coordinate_identity_checks += 1

    beta_pair_checks = 0
    beta_overlap_violations = 0
    for p in range(3, 9):
        pools = {}
        for mask in range(1 << p):
            c = bits(mask, p)
            pools[c] = {beta(c, i) for i in range(p)}
        codes = list(pools)
        for a_idx, c in enumerate(codes):
            for d in codes[a_idx:]:
                dist = sum(x != y for x, y in zip(c, d))
                observed = len(pools[c] & pools[d])
                expected = p if dist == 0 else (2 if dist == 2 else 0)
                if observed != expected:
                    beta_overlap_violations += 1
                beta_pair_checks += 1

    summary = {
        "atlas_graphs_orders_3_to_7": atlas_graphs,
        "tau_distributions": tau_distributions,
        "tau_le_2_classifier_mismatches": tau2_mismatches,
        "row_kernel_violations": kernel_violations,
        "degree_lower_bound_violations": degree_bound_violations,
        "exhaustive_signings_orders_3_to_5": signing_instances,
        "coordinate_identity_checks": coordinate_identity_checks,
        "coordinate_identity_violations": coordinate_identity_violations,
        "projective_alpha_vs_switched_true_twin_violations": mu_twin_violations,
        "beta_pool_pair_checks_orders_3_to_8": beta_pair_checks,
        "beta_pool_overlap_violations": beta_overlap_violations,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

    assert tau2_mismatches == 0
    assert kernel_violations == 0
    assert degree_bound_violations == 0
    assert coordinate_identity_violations == 0
    assert mu_twin_violations == 0
    assert beta_overlap_violations == 0


if __name__ == "__main__":
    main()
