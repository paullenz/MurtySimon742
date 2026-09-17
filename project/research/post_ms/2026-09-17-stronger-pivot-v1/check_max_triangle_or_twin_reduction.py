#!/usr/bin/env python3
"""
Regression checks for MAX_TRIANGLE_OR_TWIN_REDUCTION.md.

These finite checks support, but do not replace, the hand proofs:
  * exact D2C graph-atlas regression through order 7;
  * direct false-twin peeling checks;
  * arithmetic checks through n=5000;
  * the X_3 12-vertex/32-edge hostile control;
  * expanded-C5 equality controls through n=30.

Requires NetworkX (the repository already uses it for atlas diagnostics).
"""
from __future__ import annotations
import itertools
import math
import networkx as nx


def is_d2c(G: nx.Graph) -> bool:
    if len(G) < 2 or not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for u, v in list(G.edges()):
        H = G.copy()
        H.remove_edge(u, v)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def M(n: int) -> int:
    return ((n - 1) * (n - 1)) // 4 + 1


def rooted_data(G: nx.Graph, v):
    B = set(G.neighbors(v))
    A = set(G.nodes()) - B - {v}
    b = len(B)
    F = G.subgraph(A).copy()
    f = F.number_of_edges()
    Q = G.subgraph(B).number_of_edges()
    delta = b * (len(G) - b) - G.number_of_edges()
    rows = []
    if Q == 0:
        for x in A:
            dx = F.degree(x)
            Rx = b - sum(1 for u in B if G.has_edge(x, u))
            ex = Rx - dx
            assert ex == b - G.degree(x)
            assert ex >= 0
            rows.append((x, dx, Rx, ex))
        assert delta == f + sum(row[3] for row in rows)
    return A, B, F, f, Q, delta, rows


def triangle_vertices(G: nx.Graph) -> set:
    out = set()
    for tri in nx.enumerate_all_cliques(G):
        if len(tri) == 3:
            out.update(tri)
        elif len(tri) > 3:
            break
    return out


def has_triangle_edge(G: nx.Graph, x, y) -> bool:
    return bool(set(G.neighbors(x)) & set(G.neighbors(y)))


def check_atlas():
    total = 0
    triangle_bearing = 0
    q0_roots = 0
    triangle_free_F_edge_records = 0
    peel_records = 0

    for G in nx.graph_atlas_g():
        n = len(G)
        if n < 3 or n > 7 or not is_d2c(G):
            continue
        total += 1
        Tverts = triangle_vertices(G)
        if Tverts:
            triangle_bearing += 1
        Delta = max(dict(G.degree()).values())
        maxroots = [v for v in G if G.degree(v) == Delta]

        # The finite diagnostic used in DEFECT_TRIANGLE_ROOT.md:
        # every triangle-bearing atlas D2C graph has at least one maximum
        # vertex in a triangle. We do not promote this to a theorem.
        if Tverts:
            assert any(v in Tverts for v in maxroots)

        for v in maxroots:
            A, B, F, f, Q, delta, rows = rooted_data(G, v)
            if Q != 0:
                continue
            q0_roots += 1

            # Triangle-free F-edge payment: delta >= b-1.
            b = len(B)
            for x, y in F.edges():
                if not has_triangle_edge(G, x, y):
                    triangle_free_F_edge_records += 1
                    assert delta >= b - 1

            # Identify false twins of the root with independent common B.
            if G.subgraph(B).number_of_edges() != 0:
                continue
            W = [x for x in G if x != v and set(G.neighbors(x)) == B]
            # Directly check every legal one-step peel in the atlas.
            for y in W:
                H = G.copy()
                H.remove_node(y)
                if len(H) >= 2 and not nx.is_complete_graph(H):
                    peel_records += 1
                    assert is_d2c(H)

    return {
        "atlas_d2c": total,
        "atlas_triangle_bearing": triangle_bearing,
        "atlas_q0_max_roots": q0_roots,
        "atlas_triangle_free_F_edge_records": triangle_free_F_edge_records,
        "atlas_false_twin_peels": peel_records,
    }


def check_threshold_arithmetic(limit: int = 5000):
    records = 0
    for n in range(4, limit + 1):
        mn = M(n)
        for b in range(1, n):
            records += 1
            # b(n-b)-(b-1) <= M(n)
            assert b * (n - b) - (b - 1) <= mn

            # At m >= M+1, the resulting defect is <= b-2 whenever
            # such an m fits below b(n-b).
            if mn + 1 <= b * (n - b):
                delta_max = b * (n - b) - (mn + 1)
                assert delta_max <= b - 2

                # If Q=0, triangle-bearing, and no max triangle vertex,
                # the derived twin class lower bound is at least 3.
                # Minimal f is 1.
                w_lower = n - b - delta_max + 1
                assert w_lower >= 3
    return records


def expanded_c5_graph(x1: int, x2: int, x3: int) -> nx.Graph:
    # Blow up three consecutive C5 vertices into independent twin classes;
    # leave the two remaining C5 vertices singleton.
    assert x1 >= 1 and x2 >= 1 and x3 >= 1
    G = nx.Graph()
    X1 = [(1, i) for i in range(x1)]
    X2 = [(2, i) for i in range(x2)]
    X3 = [(3, i) for i in range(x3)]
    s4, s5 = (4, 0), (5, 0)
    G.add_nodes_from(X1 + X2 + X3 + [s4, s5])
    joins = [(X1, X2), (X2, X3)]
    for L, R in joins:
        for u in L:
            for v in R:
                G.add_edge(u, v)
    for u in X3:
        G.add_edge(u, s4)
    G.add_edge(s4, s5)
    for u in X1:
        G.add_edge(s5, u)
    return G


def check_expanded_c5(max_n: int = 30):
    controls = 0
    for n in range(6, max_n + 1):
        allowed_x2 = {(n - 3) // 2, math.ceil((n - 3) / 2)}
        for x2 in sorted(allowed_x2):
            rem = n - 2 - x2
            for x1 in range(1, rem):
                x3 = rem - x1
                if x3 < 1:
                    continue
                controls += 1
                G = expanded_c5_graph(x1, x2, x3)
                assert len(G) == n
                assert is_d2c(G)
                assert G.number_of_edges() == M(n)
                Delta = max(dict(G.degree()).values())
                for v in [u for u in G if G.degree(u) == Delta]:
                    delta = Delta * (n - Delta) - G.number_of_edges()
                    assert delta == Delta - 1
    return controls


def X3_graph() -> nx.Graph:
    k = 3
    B = list(itertools.product((0, 1), repeat=k))
    root = ("r",)
    A = [("a", i) for i in range(k)]
    G = nx.Graph()
    G.add_nodes_from(B + [root] + A)
    for x in B:
        G.add_edge(root, x)
        for i in range(k):
            if x[i] == 0:
                G.add_edge(("a", i), x)
    for i in range(k):
        for x in B:
            y = list(x)
            y[i] ^= 1
            y = tuple(y)
            if x < y:
                G.add_edge(x, y)
    return G


def check_X3():
    G = X3_graph()
    assert is_d2c(G)
    n = len(G)
    m = G.number_of_edges()
    assert (n, m, M(n)) == (12, 32, 31)
    Delta = max(dict(G.degree()).values())
    roots = [v for v in G if G.degree(v) == Delta]
    assert roots == [("r",)]
    A, B, F, f, Q, delta, rows = rooted_data(G, roots[0])
    assert f == 0
    assert delta == 0
    assert Q == 12
    return {"n": n, "m": m, "M": M(n), "delta": delta, "Q": Q}


def main():
    summary = check_atlas()
    summary["arithmetic_records"] = check_threshold_arithmetic()
    summary["expanded_C5_controls"] = check_expanded_c5()
    summary["X3"] = check_X3()
    print("PASS_MAX_TRIANGLE_OR_TWIN_REDUCTION")
    print(summary)


if __name__ == "__main__":
    main()
