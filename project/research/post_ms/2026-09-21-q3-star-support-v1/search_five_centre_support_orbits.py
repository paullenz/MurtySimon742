#!/usr/bin/env python3
"""Orbit census and exact single-copy scan for five Q3 star centres."""
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
from pysat.solvers import Solver

from check_star_support import d2c, graph
from maxsat_fixed_codes import encode


def cube_automorphisms():
    out = []
    for permutation in itertools.permutations(range(3)):
        for translation in range(8):
            image = []
            for x in range(8):
                y = sum(((x >> j) & 1) << i for i, j in enumerate(permutation))
                image.append(y ^ translation)
            out.append(tuple(image))
    return out


AUTOMORPHISMS = cube_automorphisms()


def canonical(support):
    return min(
        tuple(sorted(automorphism[x] for x in support))
        for automorphism in AUTOMORPHISMS
    )


def solve(codes):
    cnf, avars, _ = encode(codes)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        if not solver.solve():
            return None
        model = solver.get_model()
    positive = {v for v in model if v > 0}
    A_edges = [
        (u - 9, v - 9)
        for (u, v), variable in avars.items()
        if variable in positive
    ]
    adjacency = graph(codes, A_edges)
    assert d2c(adjacency)
    n = len(adjacency)
    m = sum(map(len, adjacency)) // 2
    return {
        "codes": codes,
        "A_edges": A_edges,
        "n": n,
        "m": m,
        "M_n": (n - 1) ** 2 // 4 + 1,
        "deficit_from_M": (n - 1) ** 2 // 4 + 1 - m,
        "direct_D2C_replay": True,
    }


def main():
    halfcodes = ["C00", "C01", "C10", "C11", "C20", "C21", "P0", "P1"]
    representatives = sorted(
        {canonical(support) for support in itertools.combinations(range(8), 5)}
    )
    rows = []
    for support in representatives:
        solutions = []
        tested = 0
        for size in range(9):
            for subset in itertools.combinations(halfcodes, size):
                tested += 1
                codes = list(subset) + [f"S{x}" for x in support]
                model = solve(codes)
                if model is not None:
                    solutions.append({"halfcodes": list(subset), **model})
            if solutions:
                break
        rows.append({
            "star_support": list(support),
            "complement": sorted(set(range(8)) - set(support)),
            "tested_halfcode_subsets": tested,
            "minimum_halfcode_count": len(solutions[0]["halfcodes"]) if solutions else None,
            "minimum_models": solutions,
        })
    out = {
        "cube_automorphism_count": len(AUTOMORPHISMS),
        "five_centre_orbit_count": len(representatives),
        "scope": "one physical vertex per star centre; arbitrary subset of the eight nonstar antipodal-transversal codes",
        "rows": rows,
    }
    path = Path(__file__).with_name("FIVE_CENTRE_SINGLE_COPY_ORBIT_RESULTS.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    for row in rows:
        print(row["star_support"], row["minimum_halfcode_count"], len(row["minimum_models"]))


if __name__ == "__main__":
    main()
