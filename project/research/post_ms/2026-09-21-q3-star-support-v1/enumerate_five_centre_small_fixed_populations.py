#!/usr/bin/env python3
"""Exact A-graph enumeration for the one-copy five-centre small orders."""
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
from pysat.solvers import Solver

from maxsat_fixed_codes import encode

HALFCODES = ["C00", "C01", "C10", "C11", "C20", "C21", "P0", "P1"]
STARS = ["S0", "S1", "S2", "S4", "S7"]


def enumerate_a_graphs(codes):
    cnf, avars, _ = encode(codes)
    variables = list(avars.values())
    rows = []
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        while solver.solve():
            positive = {x for x in solver.get_model() if x > 0}
            edges = sorted(
                (codes[u - 9], codes[v - 9])
                for (u, v), variable in avars.items()
                if variable in positive
            )
            rows.append(edges)
            solver.add_clause([-x if x in positive else x for x in variables])
    return rows


def main():
    subsets = []
    for size in range(9):
        for subset in itertools.combinations(HALFCODES, size):
            rows = enumerate_a_graphs(list(subset) + STARS)
            if rows:
                subsets.append({"halfcodes": list(subset), "A_graphs": rows})
        if subsets:
            break
    assert size == 7 and len(subsets) == 1
    assert subsets[0]["halfcodes"] == HALFCODES[:6] + ["P1"]
    assert len(subsets[0]["A_graphs"]) == 3
    assert {len(edges) for edges in subsets[0]["A_graphs"]} == {9}

    full_rows = enumerate_a_graphs(HALFCODES + STARS)
    distribution = {}
    for edges in full_rows:
        distribution[str(len(edges))] = distribution.get(str(len(edges)), 0) + 1
    assert distribution == {"11": 1, "10": 6}

    minimum_codes = HALFCODES[:6] + ["P1"] + STARS
    one_extra = []
    for extra in ["P0"] + minimum_codes:
        rows = enumerate_a_graphs(minimum_codes + [extra])
        distribution_extra = {}
        for edges in rows:
            distribution_extra[str(len(edges))] = distribution_extra.get(str(len(edges)), 0) + 1
        one_extra.append({
            "extra_type": extra,
            "labeled_A_graph_count": len(rows),
            "A_edge_distribution": distribution_extra,
            "maximum_edge_count": 72 + max(map(len, rows)) if rows else None,
        })
    maxima = [row["extra_type"] for row in one_extra if row["maximum_edge_count"] == 83]
    assert maxima == ["P0", "S7"]

    out = {
        "scope": "one physical copy of every selected code; fixed star support {0,1,2,4,7}",
        "minimum_halfcode_count": 7,
        "order_21": {
            "feasible_halfcode_subsets": subsets,
            "labeled_A_graph_count": 3,
            "isomorphism_note": "the three star paths are related by permutations of cube coordinates",
            "edge_count": 77,
        },
        "order_22_full_halfcodes": {
            "labeled_A_graph_count": len(full_rows),
            "A_edge_distribution": distribution,
            "unique_maximum_A_graph": [row for row in full_rows if len(row) == 11][0],
            "maximum_edge_count": 83,
        },
        "order_22_one_extra_from_minimum_population": {
            "rows": one_extra,
            "83_edge_extra_types": maxima,
        },
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_SMALL_FIXED_POPULATION_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print("PASS: order 21 has three labeled/one symmetric model; order 22 has unique 83-edge maximum")


if __name__ == "__main__":
    main()
