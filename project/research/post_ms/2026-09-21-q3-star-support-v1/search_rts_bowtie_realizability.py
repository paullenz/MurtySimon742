#!/usr/bin/env python3
"""Build actual D2C controls containing the locally saturated RTS bow-tie."""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
from pysat.solvers import Solver

from check_star_support import d2c, graph
from maxsat_fixed_codes import encode


def feasible(star_multiplicity, r, q):
    codes = ["C00", "C01", "C10", "C11", "C20", "C21"]
    codes += sum(
        ([name] * star_multiplicity for name in ("S0", "S3", "S5", "S6")),
        [],
    )
    codes += ["P0"] * r + ["P1"] * q
    x = 6
    offset = 6 + 4 * star_multiplicity
    R = list(range(offset, offset + r))
    T = list(range(offset + r, offset + r + q))
    r0, r1 = R[:2]
    t0, t1 = T[:2]
    cnf, avars, _ = encode(codes)

    def var(i, j):
        return avars[tuple(sorted((9 + i, 9 + j)))]

    for a, b in ((x, r0), (x, r1), (x, t0), (x, t1), (r0, t0)):
        cnf.append([var(a, b)])
    for a, b in ((r0, t1), (r1, t0)):
        cnf.append([-var(a, b)])
        for y in range(len(codes)):
            if y not in (a, b, x):
                cnf.append([-var(a, y), -var(b, y)])
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        return solver.solve()


def solve(r, q, fourth_present):
    codes = ["C00", "C01", "C10", "C11", "C20", "C21"]
    codes += sum(([name] * 3 for name in ("S0", "S3", "S5", "S6")), [])
    codes += ["P0"] * r + ["P1"] * q
    x = 6
    offset = 18
    R = list(range(offset, offset + r))
    T = list(range(offset + r, offset + r + q))
    r0, r1 = R[:2]
    t0, t1 = T[:2]
    cnf, avars, _ = encode(codes)

    def var(i, j):
        return avars[tuple(sorted((9 + i, 9 + j)))]

    # RTS triangle and its forced four-arm expansion.
    for a, b in ((x, r0), (x, r1), (x, t0), (x, t1), (r0, t0)):
        cnf.append([var(a, b)])
    for a, b in ((r0, t1), (r1, t0)):
        cnf.append([-var(a, b)])
        for y in range(len(codes)):
            if y not in (a, b, x):
                cnf.append([-var(a, y), -var(b, y)])
    cnf.append([var(r1, t1) if fourth_present else -var(r1, t1)])

    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        assert solver.solve()
        model = solver.get_model()
    positive = {v for v in model if v > 0}
    A_edges = [
        (u - 9, v - 9)
        for (u, v), variable in avars.items()
        if variable in positive
    ]
    adjacency = graph(codes, A_edges)
    assert d2c(adjacency)
    edge_set = {tuple(sorted(edge)) for edge in A_edges}

    def common(a, b):
        return [
            y for y in range(len(codes))
            if tuple(sorted((a, y))) in edge_set
            and tuple(sorted((b, y))) in edge_set
        ]

    assert common(r0, t1) == [x]
    assert common(r1, t0) == [x]
    assert (tuple(sorted((r1, t1))) in edge_set) == fourth_present
    n = len(adjacency)
    m = sum(map(len, adjacency)) // 2
    return {
        "codes": codes,
        "A_edges": A_edges,
        "n": n,
        "m": m,
        "M_n": (n - 1) ** 2 // 4 + 1,
        "deficit_from_M": (n - 1) ** 2 // 4 + 1 - m,
        "r": r,
        "q": q,
        "star_multiplicity_each": 3,
        "forced_star": x,
        "r0_r1_t0_t1": [r0, r1, t0, t1],
        "fourth_pair_present": fourth_present,
        "crossed_pair_common_neighbours": {
            "r0_t1": common(r0, t1),
            "r1_t0": common(r1, t0),
        },
        "direct_D2C_replay": True,
    }


def main():
    grid = {}
    for k in (1, 2, 3):
        grid[str(k)] = [
            [r, q]
            for r in range(2, 9)
            for q in range(2, 9)
            if feasible(k, r, q)
        ]
    out = {
        "scope": "six coordinate codes; three copies of each even star code",
        "status": "actual D2C RTS-bow-tie controls with both fourth-pair statuses",
        "bounded_uniform_grid": {
            "star_multiplicities": [1, 2, 3],
            "r_range": [2, 8],
            "q_range": [2, 8],
            "satisfiable_r_q_by_star_multiplicity": grid,
        },
        "fourth_present_control": solve(4, 2, True),
        "fourth_missing_control": solve(5, 2, False),
    }
    path = Path(__file__).with_name("RTS_BOWTIE_REALIZABILITY_RESULTS.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    for key in ("fourth_present_control", "fourth_missing_control"):
        row = out[key]
        print(key, row["n"], row["m"], row["fourth_pair_present"])


if __name__ == "__main__":
    main()
