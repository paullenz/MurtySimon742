#!/usr/bin/env python3
"""Independent graph-level regression for source-tuple premises.

This checker reconstructs rooted objects from actual D2C graphs and rejects any
fixture that fails D2C before examining source-premise semantics.  It
intentionally distinguishes the two orientations of a physical P--U edge:

  alpha / matched-source:
      x~y, x!~q, N(x) cap N(q)={y}

  beta / unmatched-source:
      x!~y, x~q, N(x) cap N(y)={q}.

The previous revision incorrectly labelled the alpha family as beta.  That
mistake is preserved in SOURCE_PREMISE_REPAIR.md; this file contains the
corrected implementation.

Selected P2 is a selection convention (one chosen representative per physical
source-coordinate obligation), not a claim that all raw beta witnesses are
unique.  Raw P2 multiplicity is therefore reported diagnostically rather than
used as a theorem premise.
"""
from collections import defaultdict
import itertools
import math
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


def _selected_endpoint(G, y, pair):
    r, s = pair
    yr = G.has_edge(y, r)
    ys = G.has_edge(y, s)
    if yr == ys:
        raise AssertionError("unmatched vertex failed tight-fibre transversal rule")
    return (r, s) if yr else (s, r)


def raw_beta_certificates(G, v):
    """Raw beta candidates (x,i,y,q,mate).

    For physical P--U edge yq, beta orientation is from unmatched source y.
    In G this means x is a non-neighbour of y, a neighbour of q, and
    N_G(x) cap N_G(y)={q}.
    """
    A, B, U, pairs = rooted_objects(G, v)
    out = []
    for i, pair in enumerate(pairs):
        for y in U:
            q, mate = _selected_endpoint(G, y, pair)
            for x in A:
                if G.has_edge(x, y):
                    continue
                if not G.has_edge(x, q):
                    continue
                if G.has_edge(x, mate):
                    continue
                if set(nx.common_neighbors(G, x, y)) == {q}:
                    out.append((x, i, y, q, mate))
    return out


def raw_alpha_certificates(G, v):
    """Raw alpha candidates (x,i,y,q,mate).

    For physical P--U edge yq, alpha orientation is from matched source q.
    In G this means x~y, x!~q, and N_G(x) cap N_G(q)={y}.
    """
    A, B, U, pairs = rooted_objects(G, v)
    out = []
    for i, pair in enumerate(pairs):
        for y in U:
            q, mate = _selected_endpoint(G, y, pair)
            for x in A:
                if not G.has_edge(x, y):
                    continue
                if G.has_edge(x, q):
                    continue
                if not G.has_edge(x, mate):
                    continue
                if set(nx.common_neighbors(G, x, q)) == {y}:
                    out.append((x, i, y, q, mate))
    return out


def premise_collisions(G, v):
    beta = raw_beta_certificates(G, v)

    # P1 would fail if one physical x,y pair appeared at two target fibres.
    by_xy = defaultdict(set)
    # Raw P2 multiplicity is diagnostic only; selected P2 chooses one rep.
    by_yi = defaultdict(set)
    for x, i, y, q, mate in beta:
        by_xy[(x, y)].add(i)
        by_yi[(y, i)].add(x)

    p1 = [(x, y, sorted(I)) for (x, y), I in by_xy.items() if len(I) > 1]
    raw_p2 = [(y, i, sorted(X)) for (y, i), X in by_yi.items() if len(X) > 1]
    return p1, raw_p2, beta



def canonical_selected_system(G, v):
    """Choose one canonical criticality representative for every rooted B-edge.

    In G-language, a selected orientation source->exception with A-label x has
    source!~x, x~exception, and N(source) cap N(x)={exception}.
    Lexicographic choice is only to make the regression deterministic.
    """
    A, B, U, pairs = rooted_objects(G, v)
    selected = []

    for u, w in G.subgraph(B).edges():
        candidates = []
        for source, exception in ((u, w), (w, u)):
            for x in A:
                if G.has_edge(source, x):
                    continue
                if not G.has_edge(x, exception):
                    continue
                if set(nx.common_neighbors(G, source, x)) == {exception}:
                    candidates.append(
                        (repr(source), repr(x), repr(exception), source, x, exception)
                    )

        if not candidates:
            raise AssertionError(
                ("rooted B-edge has no canonical selected representative", v, u, w)
            )

        candidates.sort(key=lambda t: t[:3])
        _, _, _, source, x, exception = candidates[0]
        selected.append((source, x, exception))

    source_label = [(source, x) for source, x, exception in selected]
    if len(source_label) != len(set(source_label)):
        raise AssertionError("selected source-label incidence graph is not simple")

    return selected


def selected_pu_ledger(G, v):
    """Classify selected P--U obligations as alpha or beta.

    Returns (physical_pu, alpha_count, beta_count, beta_records), where each
    beta record is (x,i,y).  This is the graph-level selected system needed by
    the source-tuple interface.
    """
    A, B, U, pairs = rooted_objects(G, v)
    selected = canonical_selected_system(G, v)
    by_pair = {
        frozenset((source, exception)): (source, x, exception)
        for source, x, exception in selected
    }

    alpha = beta = 0
    beta_records = []

    for i, pair in enumerate(pairs):
        for y in U:
            q, mate = _selected_endpoint(G, y, pair)
            key = frozenset((y, q))
            if key not in by_pair:
                raise AssertionError("P--U physical edge missing from selected system")

            source, x, exception = by_pair[key]
            if source == y and exception == q:
                beta += 1
                beta_records.append((x, i, y))
            elif source == q and exception == y:
                alpha += 1
            else:
                raise AssertionError("selected P--U orientation does not match physical edge")

    physical = len(pairs) * len(U)
    if alpha + beta != physical:
        raise AssertionError("selected P--U ledger does not partition physical obligations")

    # Selected P2: one physical (y,i) obligation can appear at most once.
    yi = [(y, i) for x, i, y in beta_records]
    if len(yi) != len(set(yi)):
        raise AssertionError("selected source-coordinate uniqueness failed")

    # Selected P1, now also backed by the direct raw-criticality proof.
    by_xy = defaultdict(set)
    for x, i, y in beta_records:
        by_xy[(x, y)].add(i)
    bad = [(key, I) for key, I in by_xy.items() if len(I) > 1]
    if bad:
        raise AssertionError(("selected distinct-physical-source premise failed", bad))

    return physical, alpha, beta, beta_records

def make_x3():
    """Programmatic published 12/32 cube-face negative control."""
    G = nx.Graph()
    cube = [format(i, "03b") for i in range(8)]
    G.add_nodes_from(["r", "a1", "a2", "a3"] + cube)

    for s in cube:
        for j in range(3):
            t = s[:j] + ("1" if s[j] == "0" else "0") + s[j + 1 :]
            G.add_edge(s, t)

    for s in cube:
        G.add_edge("r", s)

    for j, a in enumerate(["a1", "a2", "a3"]):
        for s in cube:
            if s[j] == "0":
                G.add_edge(a, s)

    return G


def x3_regression():
    G = make_x3()
    assert G.number_of_nodes() == 12
    assert G.number_of_edges() == 32
    M12 = math.floor((12 - 1) ** 2 / 4) + 1
    assert M12 == 31
    assert G.number_of_edges() > M12
    assert is_d2c(G)

    A, B, U, pairs = rooted_objects(G, "r")
    assert len(A) == 3
    assert len(B) == 8
    assert len(U) == 0
    assert len(pairs) == 4
    assert not raw_beta_certificates(G, "r")
    return len(A), len(B), len(U), len(pairs)


def atlas_regression():
    classes = roots = beta_count = alpha_count = 0
    selected_edges = physical_pu = selected_alpha = selected_beta = 0
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
            p1, p2, beta = premise_collisions(G, v)
            beta_count += len(beta)
            alpha_count += len(raw_alpha_certificates(G, v))
            selected_edges += len(canonical_selected_system(G, v))
            pu, sa, sb, selected_beta_records = selected_pu_ledger(G, v)
            physical_pu += pu
            selected_alpha += sa
            selected_beta += sb
            if p1:
                p1_fail.append((classes, v, p1))
            if p2:
                raw_p2_fail.append((classes, v, p2))

    return (
        classes,
        roots,
        beta_count,
        alpha_count,
        selected_edges,
        physical_pu,
        selected_alpha,
        selected_beta,
        p1_fail,
        raw_p2_fail,
    )


def main():
    (
        classes,
        roots,
        beta_count,
        alpha_count,
        selected_edges,
        physical_pu,
        selected_alpha,
        selected_beta,
        p1,
        raw_p2,
    ) = atlas_regression()

    assert classes == 21, classes
    # P1 now has a direct hand proof; any graph-level collision is a blocker.
    assert not p1, p1

    a, b, u, p = x3_regression()

    print("D2C atlas classes through order 7:", classes)
    print("roots checked:", roots)
    print("raw beta candidate certificates:", beta_count)
    print("raw alpha candidate certificates:", alpha_count)
    print("canonical selected rooted B-edges:", selected_edges)
    print("physical P--U obligations:", physical_pu)
    print("selected alpha P--U obligations:", selected_alpha)
    print("selected beta P--U obligations:", selected_beta)
    print("P1 collisions:", len(p1))
    print("raw P2 collisions (diagnostic only):", len(raw_p2))
    print("X3 canonical root (a,b,u,p):", (a, b, u, p))
    print("X3: n=12 m=32 M(12)=31 D2C PASS")
    print("PASS: corrected beta orientation, selected P--U ledger, and mandatory X3 control")


if __name__ == "__main__":
    main()
