#!/usr/bin/env python3
"""Physical-source MILP screen for r=11 support-ten strict cores."""
import itertools
import json
import multiprocessing as mp

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix

unit_pairs = list(itertools.combinations(range(9), 2))


def one(line):
    fields = list(map(int, line.split()))
    unit_mask, heavy_neighbours, t_upper = fields[:3]
    residual = tuple(fields[3:13])
    edges = [(i + 1, j + 1) for q, (i, j) in enumerate(unit_pairs)
             if unit_mask >> q & 1]
    edges += [(0, i + 1) for i in range(9) if heavy_neighbours >> i & 1]
    k = 10
    neigh = [set() for _ in residual]
    degree = [0] * k
    for i, j in edges:
        neigh[i].add(j); neigh[j].add(i)
        degree[i] += 1; degree[j] += 1
    need = tuple(max(0, degree[i] - residual[i]) for i in range(k))
    patterns = []
    for state in itertools.product(range(3), repeat=k):
        left = {i for i, s in enumerate(state) if s == 1}
        zero = {i for i, s in enumerate(state) if s == 2}
        if not zero or any(not neigh[i] <= left | zero or
                           len(neigh[i] & left) > residual[i] for i in left):
            continue
        patterns.append((
            tuple(int(i in zero) for i in range(k)),
            tuple(int(i in left) for i in range(k)), state))
    if not patterns:
        return {"unit_mask": unit_mask, "heavy_neighbours": heavy_neighbours,
                "status": 2}
    matrix = np.array([[p[0][i] for p in patterns] for i in range(k)] +
                      [[p[1][i] for p in patterns] for i in range(k)], dtype=float)
    result = milp(
        np.zeros(len(patterns)), integrality=np.ones(len(patterns)),
        bounds=Bounds(np.zeros(len(patterns)), np.full(len(patterns), np.inf)),
        constraints=LinearConstraint(
            csc_matrix(matrix), np.array(residual + need, dtype=float),
            np.array(residual + (10**9,) * k, dtype=float)),
        options={"time_limit": 120.0})
    row = {"unit_mask": unit_mask, "heavy_neighbours": heavy_neighbours,
           "R": residual, "t_upper": t_upper, "edges": edges, "degrees": degree,
           "need": need, "patterns": len(patterns), "status": int(result.status),
           "message": result.message}
    if result.success:
        row["population"] = [
            {"state": patterns[q][2], "count": int(round(value))}
            for q, value in enumerate(result.x) if value > 0.5]
    return row


if __name__ == "__main__":
    lines = open("r11_support10_masks.txt").read().splitlines()
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(one, lines, chunksize=1))
    feasible = [row for row in rows if row.get("population")]
    unknown = [row for row in rows if row["status"] not in (0, 2)]
    print(json.dumps({
        "partition": (2,1,1,1,1,1,1,1,1,1),
        "strict_core_orbits": len(lines),
        "source_feasible": len(feasible),
        "solver_unknown": len(unknown),
        "feasible_rows": feasible,
        "unknown_rows": unknown,
        "scope": "Integer physical-source necessary condition encoded as MILP; internal computer-assisted result, not graph realization.",
    }, indent=2, sort_keys=True))
