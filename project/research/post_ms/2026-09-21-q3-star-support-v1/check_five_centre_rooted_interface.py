#!/usr/bin/env python3
"""Maximum-root and rigid/Hall interface audit for the five-centre family."""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "2026-09-19-rigid-graph-regression-v1"))
import networkx as nx
import check_rigid_graph_level as hall

from probe_five_centre_parity_blowups import build


def nx_graph(r, q):
    _, _, adjacency = build(r, q)
    G = nx.Graph()
    G.add_nodes_from(range(len(adjacency)))
    G.add_edges_from((x, y) for x, ns in enumerate(adjacency) for y in ns if x < y)
    return G


def expected_roots(r, q):
    even_degree = 11 + r
    odd_degree = 9 + q
    if even_degree > odd_degree:
        return [0]
    if even_degree < odd_degree:
        return [1, 2, 4]
    return [0, 1, 2, 4]


def main():
    grid = []
    root_checks = 0
    for r in range(1, 21):
        for q in range(1, 21):
            G = nx_graph(r, q)
            degree = max(dict(G.degree()).values())
            roots = sorted(v for v in G if G.degree(v) == degree)
            assert roots == expected_roots(r, q)
            root_rows = []
            for v in roots:
                A, B, U, pairs = hall.rooted_partition(G, v)
                assert not pairs and U == B
                Q = G.subgraph(B).number_of_edges()
                assert Q == (17 if v == 0 else 16)
                delta = len(B) * (len(G) - len(B)) - G.number_of_edges()
                assert delta == 5 * r + 7 * q + 26
                lam = len(B) - len(A) - 1
                assert lam == (2 + r - q if v == 0 else q - r - 2)
                root_rows.append({
                    "root": v,
                    "a": len(A),
                    "b": len(B),
                    "p": 0,
                    "u": len(U),
                    "lambda": lam,
                    "Q": Q,
                    "delta": delta,
                })
                root_checks += 1
            grid.append({"r": r, "q": q, "maximum_degree": degree, "roots": root_rows})

    replay = []
    totals = Counter()
    for r, q in [(1, 1), (1, 3), (1, 4), (4, 1), (4, 4),
                 (8, 8), (4, 12), (12, 4), (20, 20)]:
        G = nx_graph(r, q)
        stats = Counter()
        for v in expected_roots(r, q):
            for policy in ("lex", "matched_first", "au_first"):
                stats.update(hall.verify_root(G, v, policy, True))
        totals.update(stats)
        replay.append({"r": r, "q": q, "stats": dict(stats)})

    X3 = hall.cube_face_graph(3)
    assert len(X3) == 12 and X3.number_of_edges() == 32 and hall.M(12) == 31
    x3_stats = Counter()
    for policy in ("lex", "matched_first", "au_first"):
        x3_stats.update(hall.verify_root(X3, "r", policy, True))

    out = {
        "grid_scope": "all 1<=r,q<=20; every maximum-degree root",
        "grid_fixture_count": len(grid),
        "maximum_root_checks": root_checks,
        "maximum_degree_formula": "max(11+r,9+q)",
        "root_switch": "root 0 if q<r+2; roots 1,2,4 if q>r+2; all four if q=r+2",
        "universal_root_defect": "delta=5r+7q+26",
        "grid": grid,
        "selected_full_interface_replay": replay,
        "selected_totals": dict(totals),
        "X3_negative_control": {"n": 12, "m": 32, "M": 31, "stats": dict(x3_stats)},
        "conclusion": "Every maximum-degree root has p=0; the family cannot exercise the positive rigid-cut interface.",
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_ROOTED_INTERFACE_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print(f"PASS: {len(grid)} fixtures, {root_checks} maximum roots, all p=0; X3 retained")


if __name__ == "__main__":
    main()
