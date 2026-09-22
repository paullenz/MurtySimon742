#!/usr/bin/env python3
"""Partition-sharded physical-source MILP screen for r=11 support nine."""
import itertools
import json
import multiprocessing as mp
import sys

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix

pairs = list(itertools.combinations(range(9), 2))


def one(line):
    fields = list(map(int, line.split()))
    case, mask, t_upper = fields[:3]
    residual = tuple(fields[3:12])
    edges = [pairs[q] for q in range(36) if mask >> q & 1]
    neigh = [set() for _ in residual]
    degree = [0] * 9
    for i, j in edges:
        neigh[i].add(j)
        neigh[j].add(i)
        degree[i] += 1
        degree[j] += 1
    need = tuple(max(0, degree[i] - residual[i]) for i in range(9))
    patterns = []
    for state in itertools.product(range(3), repeat=9):
        left = {i for i, s in enumerate(state) if s == 1}
        zero = {i for i, s in enumerate(state) if s == 2}
        if not zero:
            continue
        if any(not neigh[i] <= left | zero or len(neigh[i] & left) > residual[i]
               for i in left):
            continue
        patterns.append((
            tuple(int(i in zero) for i in range(9)),
            tuple(int(i in left) for i in range(9)),
            state,
        ))
    if not patterns:
        return {"case": case, "mask": mask, "status": 2}
    matrix = np.array([[p[0][i] for p in patterns] for i in range(9)] +
                      [[p[1][i] for p in patterns] for i in range(9)], dtype=float)
    result = milp(
        np.zeros(len(patterns)),
        integrality=np.ones(len(patterns)),
        bounds=Bounds(np.zeros(len(patterns)), np.full(len(patterns), np.inf)),
        constraints=LinearConstraint(
            csc_matrix(matrix),
            np.array(residual + need, dtype=float),
            np.array(residual + (10**9,) * 9, dtype=float),
        ),
        options={"time_limit": 120.0},
    )
    row = {
        "case": case, "mask": mask, "R": residual, "t_upper": t_upper,
        "edges": edges, "degrees": degree, "need": need,
        "patterns": len(patterns), "status": int(result.status),
        "message": result.message,
    }
    if result.success:
        row["population"] = [
            {"state": patterns[q][2], "count": int(round(value))}
            for q, value in enumerate(result.x) if value > 0.5
        ]
    return row


if __name__ == "__main__":
    case = int(sys.argv[1])
    lines = [
        line for line in open("r11_support9_masks.txt")
        if int(line.split()[0]) == case
    ]
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(one, lines, chunksize=2))
    feasible = [row for row in rows if row.get("population")]
    unknown = [row for row in rows if row["status"] not in (0, 2)]
    print(json.dumps({
        "case": case,
        "partition": [(3,1,1,1,1,1,1,1,1), (2,2,1,1,1,1,1,1,1)][case],
        "strict_core_orbits": len(lines),
        "source_feasible": len(feasible),
        "solver_unknown": len(unknown),
        "feasible_rows": feasible,
        "unknown_rows": unknown,
        "scope": "Integer physical-source necessary condition encoded as MILP; internal computer-assisted result, not graph realization.",
    }, indent=2, sort_keys=True))
