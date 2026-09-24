#!/usr/bin/env python3
"""Replay the 13 unresolved r=12 support-ten helper rows as continuous LPs.

This is deliberately separate from the historical integer-MILP driver.  It
rebuilds the pattern and helper matrices and calls scipy.optimize.linprog.
"""

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix, vstack


ROOT = Path(__file__).resolve().parent / "repo06"
PACKAGE = ROOT / "project/research/general_n/2026-09-22-independent-742-r12-quotient"
TARGETS = {362, 363, 437, 438, 451, 455, 1494, 3755, 3758, 4663, 4664, 4665, 4682}
SOURCE_INDICES = [355, 359, 362, 363, 434, 437, 438, 451, 452, 455,
                  1196, 1202, 1208, 1209, 1390, 1393, 1396, 1397, 1493,
                  1494, 1497, 3753, 3755, 3758, 3759, 3790, 3791, 4663,
                  4664, 4665, 4682, 4683]


def input_rows():
    rows = []
    for shard in range(8):
        path = PACKAGE / f"r12_support10_case1_source_chunk{shard}.json"
        for row in json.loads(path.read_text())["feasible_rows"]:
            rows.append(dict(row, shard=shard))
    assert len(rows) == len(SOURCE_INDICES)
    return {index: row for index, row in zip(SOURCE_INDICES, rows)}


def build(row):
    residual = tuple(row["R"])
    edges = [tuple(e) for e in row["edges"]]
    k = len(residual)
    neighbours = [set() for _ in residual]
    degrees = [0] * k
    for i, j in edges:
        neighbours[i].add(j); neighbours[j].add(i)
        degrees[i] += 1; degrees[j] += 1
    need = tuple(max(0, degrees[i] - residual[i]) for i in range(k))
    positive = {i for i, value in enumerate(need) if value > 0}

    patterns, free = [], []
    for state in itertools.product(range(3), repeat=k):
        left = {i for i, value in enumerate(state) if value == 1}
        zero = {i for i, value in enumerate(state) if value == 2}
        if any(not neighbours[i] <= left | zero or
               len(neighbours[i] & left) > residual[i] for i in left):
            continue
        if not zero:
            if not (left & positive):
                free.append((state, left))
            continue
        patterns.append((state, left, zero))

    m = len(patterns); nvar = 2 * m
    eq_rows, eq_rhs, ub_rows, ub_rhs = [], [], [], []
    for i in range(k):
        a = np.zeros(nvar)
        for p, (_, _, zero) in enumerate(patterns): a[p] = i in zero
        eq_rows.append(csc_matrix(a)); eq_rhs.append(residual[i])
    for i in range(k):
        a = np.zeros(nvar)
        for p, (_, left, _) in enumerate(patterns): a[p] = -(i in left)
        ub_rows.append(csc_matrix(a)); ub_rhs.append(-need[i])
    for p in range(m):
        a = np.zeros(nvar); a[p] = -1; a[m+p] = 1
        ub_rows.append(csc_matrix(a)); ub_rhs.append(0)
        a = np.zeros(nvar); a[p] = 1; a[m+p] = -12
        ub_rows.append(csc_matrix(a)); ub_rhs.append(0)

    helper_constraints = free_discharges = 0
    for p, (state_p, left_p, _) in enumerate(patterns):
        if len(left_p) == 1: continue
        for i in left_p:
            def helps(state_q, left_q):
                return (state_q[i] == 0 and
                        all(state_q[j] != 0 for j in left_p if j != i) and
                        all(state_p[j] != 0 for j in left_q))
            if any(helps(sq, lq) for sq, lq in free):
                free_discharges += 1; continue
            a = np.zeros(nvar); a[m+p] = 1
            for q, (sq, lq, _) in enumerate(patterns):
                if q != p and helps(sq, lq): a[m+q] -= 1
            ub_rows.append(csc_matrix(a)); ub_rhs.append(0)
            helper_constraints += 1
    return {
        "c": np.zeros(nvar),
        "A_eq": vstack(eq_rows, format="csc"), "b_eq": np.asarray(eq_rhs),
        "A_ub": vstack(ub_rows, format="csc"), "b_ub": np.asarray(ub_rhs),
        "bounds": [(0, 12)] * m + [(0, 1)] * m,
        "patterns": m, "free": len(free), "free_discharges": free_discharges,
        "helper_constraints": helper_constraints,
    }


def solve(index, row, method, time_limit):
    model = build(row)
    result = linprog(model["c"], A_ub=model["A_ub"], b_ub=model["b_ub"],
                     A_eq=model["A_eq"], b_eq=model["b_eq"],
                     bounds=model["bounds"], method=method,
                     options={"time_limit": time_limit})
    return {
        "index": index,
        "identity": [row["unit_graph"], row["heavy_edge"], row["a_mask"], row["b_mask"]],
        "patterns": model["patterns"], "free": model["free"],
        "free_discharges": model["free_discharges"],
        "helper_constraints": model["helper_constraints"],
        "status": int(result.status), "success": bool(result.success),
        "message": result.message,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indices", default=",".join(map(str, sorted(TARGETS))))
    parser.add_argument("--method", default="highs-ipm")
    parser.add_argument("--time-limit", type=float, default=120.0)
    args = parser.parse_args()
    wanted = [int(x) for x in args.indices.split(",") if x]
    rows = input_rows()
    output = []
    for index in wanted:
        result = solve(index, rows[index], args.method, args.time_limit)
        output.append(result); print(json.dumps(result), flush=True)
    print("FINAL " + json.dumps({"method": args.method, "rows": output,
          "infeasible": sum(r["status"] == 2 for r in output),
          "unknown": sum(r["status"] not in (0, 2) for r in output)}))


if __name__ == "__main__": main()
