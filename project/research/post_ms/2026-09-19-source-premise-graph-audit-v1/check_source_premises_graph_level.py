#!/usr/bin/env python3
"""Independent graph-level regression for source-tuple premises.

This checker intentionally reconstructs the rooted objects from actual D2C graphs.
It does not import the abstract source-tuple implementation.

Requires networkx.  The two explicit counterexamples in main() are dependency-light
regression fixtures for raw P2 failure.
"""
from collections import defaultdict
import itertools
import networkx as nx


def is_d2c(G):
    if not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def tight_pair(G, v, u, w):
    if G.has_edge(u, w):
        return False
    if set(nx.common_neighbors(G, u, w)) != {v}:
        return False
    for z in G.nodes():
        if z in (v, u, w):
            continue
        if int(G.has_edge(z, u)) + int(G.has_edge(z, w)) != 1:
            return False
    return True


def rooted_objects(G, v):
    B = set(G.neighbors(v))
    A = set(G.nodes()) - {v} - B
    pairs = []
    for u, w in itertools.combinations(sorted(B), 2):
        if tight_pair(G, v, u, w):
            pairs.append((u, w))
    flat = [z for e in pairs for z in e]
    if len(flat) != len(set(flat)):
        raise AssertionError("tight antipode pairs do not form a matching")
    U = B - set(flat)
    return A, B, U, pairs


def oriented_beta_certificates(G, v):
    """Return raw certificates (x,i,y,q,mate).

    Each tight pair is tried in both orientations.  A raw certificate records
    a graph realization; it has NOT been deduplicated by physical (y,i).
    """
    A, B, U, pairs = rooted_objects(G, v)
    out = []
    for i, (r, s) in enumerate(pairs):
        for q, mate in ((r, s), (s, r)):
            for x in A:
                if G.has_edge(x, q) or not G.has_edge(x, mate):
                    continue
                for y in U:
                    if not G.has_edge(x, y) or not G.has_edge(y, q):
                        continue
                    if set(nx.common_neighbors(G, x, q)) == {y}:
                        out.append((x, i, y, q, mate))
    return out


def premise_violations(G, v):
    certs = oriented_beta_certificates(G, v)
    # P1: one fixed x reuses physical y on two distinct target fibres.
    by_xy = defaultdict(set)
    for x, i, y, q, mate in certs:
        by_xy[(x, y)].add(i)
    p1 = [(x, y, sorted(I)) for (x, y), I in by_xy.items() if len(I) > 1]

    # Raw P2: one fixed physical (y,i) has multiple A-witness realizations.
    by_yi = defaultdict(set)
    for x, i, y, q, mate in certs:
        by_yi[(y, i)].add(x)
    p2 = [(y, i, sorted(X)) for (y, i), X in by_yi.items() if len(X) > 1]
    return p1, p2, certs


def make_graph(n, edges):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)
    return G


def check_fixture(n, edges, root, expected_yi, expected_xs):
    G = make_graph(n, edges)
    assert is_d2c(G)
    p1, p2, certs = premise_violations(G, root)
    assert not p1
    found = {(y, i): set(xs) for y, i, xs in p2}
    assert found[expected_yi] == set(expected_xs), (found, certs)
    return certs


def atlas_regression():
    count = 0
    p1_fail = []
    p2_fail = []
    for G0 in nx.graph_atlas_g():
        if G0.number_of_nodes() < 3:
            continue
        G = nx.convert_node_labels_to_integers(G0)
        if not is_d2c(G):
            continue
        count += 1
        for v in G.nodes():
            p1, p2, certs = premise_violations(G, v)
            if p1:
                p1_fail.append((count, v, p1))
            if p2:
                p2_fail.append((count, v, p2))
    return count, p1_fail, p2_fail


def main():
    e9 = [(0,1),(0,2),(1,3),(2,8),(3,8),(4,6),(4,7),(5,6),(5,7)]
    c9 = check_fixture(9, e9, 4, (7, 0), {2, 3})

    e10 = [(0,6),(0,8),(1,3),(1,8),(2,4),(2,8),(3,9),(4,5),(5,7),(6,7)]
    c10 = check_fixture(10, e10, 1, (8, 0), {0, 2})

    count, p1, p2 = atlas_regression()
    assert count == 21, count
    assert not p1, p1
    print("fixture n=9 raw certificates:", c9)
    print("fixture n=10 raw certificates:", c10)
    print("D2C atlas classes through order 7:", count)
    print("atlas P1 violations:", len(p1))
    print("atlas raw P2 violations:", len(p2))
    print("PASS: explicit realizable D2C fixtures refute raw P2")


if __name__ == "__main__":
    main()
