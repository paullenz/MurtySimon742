#!/usr/bin/env python3
"""Independent graph-level regression for source-tuple premises.

This checker reconstructs rooted objects from actual D2C graphs and rejects any
fixture that fails D2C before examining source-premise semantics.  It deliberately
does not import the abstract source-tuple implementation.

The previous revision contained provisional alleged raw-P2 fixtures which failed
this exact validation; they have been removed and the failure is documented in
SOURCE_PREMISE_GRAPH_AUDIT.md.
"""
from collections import defaultdict
import itertools
import networkx as nx


def is_d2c(G):
    if G.number_of_nodes() < 3 or not nx.is_connected(G):
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
    """Raw tight-antipode definition at root v."""
    if u not in G[v] or w not in G[v] or G.has_edge(u, w):
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
        raise AssertionError("tight antipodes failed matching property")
    U = B - set(flat)
    return A, B, U, pairs


def oriented_beta_certificates(G, v):
    """Low-level candidate certificates (x,i,y,q,mate).

    This implements only the raw unique-common-neighbour geometry used in the
    source audit.  It has not been declared equivalent to every later selected
    beta object; that interface remains under audit.
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


def premise_collisions(G, v):
    certs = oriented_beta_certificates(G, v)
    by_xy = defaultdict(set)
    by_yi = defaultdict(set)
    for x, i, y, q, mate in certs:
        by_xy[(x, y)].add(i)
        by_yi[(y, i)].add(x)
    p1 = [(x, y, sorted(I)) for (x, y), I in by_xy.items() if len(I) > 1]
    raw_p2 = [(y, i, sorted(X)) for (y, i), X in by_yi.items() if len(X) > 1]
    return p1, raw_p2, certs


def atlas_regression():
    classes = roots = cert_count = 0
    p1_fail = []
    raw_p2_fail = []
    for G0 in nx.graph_atlas_g():
        if G0.number_of_nodes() < 3:
            continue
        G = nx.convert_node_labels_to_integers(G0)
        if not is_d2c(G):
            continue
        classes += 1
        for v in G.nodes():
            roots += 1
            p1, p2, certs = premise_collisions(G, v)
            cert_count += len(certs)
            if p1:
                p1_fail.append((classes, v, p1))
            if p2:
                raw_p2_fail.append((classes, v, p2))
    return classes, roots, cert_count, p1_fail, raw_p2_fail


def main():
    classes, roots, cert_count, p1, p2 = atlas_regression()
    assert classes == 21, classes
    assert not p1, p1
    assert not p2, p2
    print("D2C atlas classes through order 7:", classes)
    print("roots checked:", roots)
    print("raw beta-candidate certificates:", cert_count)
    print("P1 collisions:", len(p1))
    print("raw P2 collisions:", len(p2))
    print("PASS: atlas regression; P1/P2 remain unproved graph-level premises")


if __name__ == "__main__":
    main()
