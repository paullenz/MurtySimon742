#!/usr/bin/env python3
"""Chunked physical-source MILP for r=12 support-ten partition (2,2,1^8)."""
import itertools
import json
import multiprocessing as mp
import sys

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix

UNIT_PAIRS = list(itertools.combinations(range(8), 2))


def one(line):
    fields = list(map(int, line.split()))
    unit_graph, heavy_edge, a_mask, b_mask, t_upper = fields[:5]
    residual = tuple(fields[5:15])
    edges = [(i + 2, j + 2) for q, (i, j) in enumerate(UNIT_PAIRS)
             if unit_graph >> q & 1]
    if heavy_edge:
        edges.append((0, 1))
    edges += [(0, i + 2) for i in range(8) if a_mask >> i & 1]
    edges += [(1, i + 2) for i in range(8) if b_mask >> i & 1]
    neigh = [set() for _ in residual]
    degree = [0] * 10
    for i, j in edges:
        neigh[i].add(j); neigh[j].add(i)
        degree[i] += 1; degree[j] += 1
    need = tuple(max(0, degree[i] - residual[i]) for i in range(10))
    patterns = []
    for state in itertools.product(range(3), repeat=10):
        left = {i for i, s in enumerate(state) if s == 1}
        zero = {i for i, s in enumerate(state) if s == 2}
        if not zero or any(not neigh[i] <= left | zero or
                           len(neigh[i] & left) > residual[i] for i in left):
            continue
        patterns.append((
            tuple(int(i in zero) for i in range(10)),
            tuple(int(i in left) for i in range(10)), state))
    if not patterns:
        return {"unit_graph": unit_graph, "heavy_edge": heavy_edge,
                "a_mask": a_mask, "b_mask": b_mask, "status": 2}
    matrix = np.array([[p[0][i] for p in patterns] for i in range(10)] +
                      [[p[1][i] for p in patterns] for i in range(10)], dtype=float)
    result = milp(
        np.zeros(len(patterns)), integrality=np.ones(len(patterns)),
        bounds=Bounds(np.zeros(len(patterns)), np.full(len(patterns), np.inf)),
        constraints=LinearConstraint(
            csc_matrix(matrix), np.array(residual + need, dtype=float),
            np.array(residual + (10**9,) * 10, dtype=float)),
        options={"time_limit": 120.0})
    row = {"unit_graph": unit_graph, "heavy_edge": heavy_edge,
           "a_mask": a_mask, "b_mask": b_mask, "R": residual,
           "t_upper": t_upper, "edges": edges, "degrees": degree, "need": need,
           "patterns": len(patterns), "status": int(result.status),
           "message": result.message}
    if result.success:
        row["population"] = [
            {"state": patterns[q][2], "count": int(round(value))}
            for q, value in enumerate(result.x) if value > 0.5]
    return row


if __name__ == "__main__":
    chunk, chunks = map(int, sys.argv[1:3])
    all_lines = open("r12_support10_case1_masks.txt").read().splitlines()
    lo = len(all_lines) * chunk // chunks
    hi = len(all_lines) * (chunk + 1) // chunks
    lines = all_lines[lo:hi]
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(one, lines, chunksize=1))
    feasible = [row for row in rows if row.get("population")]
    unknown = [row for row in rows if row["status"] not in (0, 2)]
    print(json.dumps({
        "partition": [2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        "chunk": chunk, "chunks": chunks, "range": [lo, hi],
        "strict_core_orbits": len(lines),
        "source_feasible": len(feasible), "solver_unknown": len(unknown),
        "feasible_rows": feasible, "unknown_rows": unknown,
        "scope": "Integer physical-source necessary condition encoded as MILP; internal computer-assisted result, not graph realization.",
    }, indent=2, sort_keys=True))

