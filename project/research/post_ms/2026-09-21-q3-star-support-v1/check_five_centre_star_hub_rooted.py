#!/usr/bin/env python3
"""No-positive-rigid-root audit for the improved five-centre family."""
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "2026-09-19-rigid-graph-regression-v1"))
import networkx as nx
import check_rigid_graph_level as hall

from check_five_centre_star_hub_family import build, TYPES, COORDINATES, LEAVES


def nx_graph(mult):
    codes, _, adjacency = build(mult)
    G = nx.Graph()
    G.add_nodes_from(range(len(adjacency)))
    G.add_edges_from((x, y) for x, ns in enumerate(adjacency) for y in ns if x < y)
    return codes, G


def main():
    seed = {kind: 1 for kind in TYPES}
    seed["P1"] = 2
    codes, G = nx_graph(seed)
    seed_rows = []
    for v in G:
        pairs = hall.rooted_partition(G, v)[3]
        kind = "original_root" if v == 8 else (f"cube_{v}" if v < 8 else codes[v - 9])
        seed_rows.append({"root": v, "kind": kind, "degree": G.degree(v), "p": len(pairs)})
        if v == 8:
            assert len(pairs) == 4
        else:
            assert not pairs
    assert max(dict(G.degree()).values()) > G.degree(8)

    random.seed(744)
    rows = []
    maximum_root_checks = 0
    for trial in range(1000):
        mult = {kind: 1 for kind in TYPES}
        for kind in COORDINATES + ["P0", "P1"] + LEAVES:
            mult[kind] = random.randint(1, 12)
        mult["S7"] = 1
        _, H = nx_graph(mult)
        Delta = max(dict(H.degree()).values())
        roots = [v for v in H if H.degree(v) == Delta]
        for v in roots:
            assert not hall.rooted_partition(H, v)[3]
            maximum_root_checks += 1
        rows.append({"trial": trial, "maximum_degree": Delta,
                     "maximum_root_count": len(roots), "all_p_zero": True})

    X3 = hall.cube_face_graph(3)
    assert len(X3) == 12 and X3.number_of_edges() == 32 and hall.M(12) == 31
    out = {
        "finite_type_seed": seed_rows,
        "seed_conclusion": "Only the original Q3 root has p>0; its degree 8 is below the P1 hub degree.",
        "random_combined_fixtures": 1000,
        "maximum_root_checks": maximum_root_checks,
        "rows": rows,
        "X3_negative_control": {"n": 12, "m": 32, "M": 31},
        "conclusion": "Every maximum root in the arbitrary clone-closed family has p=0 by seed-type monotonicity; random replay is diagnostic confirmation.",
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_STAR_HUB_ROOTED_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print(f"PASS: seed types closed; {maximum_root_checks} random maximum roots all p=0; X3 retained")


if __name__ == "__main__":
    main()
