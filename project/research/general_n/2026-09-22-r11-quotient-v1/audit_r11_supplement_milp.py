#!/usr/bin/env python3
"""Independent MILP replay combining source counts and supplement helpers."""
import itertools
import json
import multiprocessing as mp

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix


def survivors():
    rows = []
    for support, path in [
        (8, "r11_support8_sources_case2.json"),
        (9, "r11_support9_sources_case1.json"),
        (10, "r11_support10_sources.json"),
    ]:
        for row in json.load(open(path))["feasible_rows"]:
            rows.append((support, row))
    return rows


def solve(item):
    index, (support, row) = item
    residual = tuple(row["R"])
    edges = [tuple(edge) for edge in row["edges"]]
    k = len(residual)
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
        patterns.append((state, left, zero))
    m = len(patterns)
    # x_p is the integer multiplicity; y_p records whether pattern p is present.
    # This is deliberately different from the earlier multiset DFS.
    nvar = 2 * m
    rows_a = []; lower = []; upper = []
    for i in range(k):
        a = np.zeros(nvar)
        for p, (_, _, zero) in enumerate(patterns):
            a[p] = i in zero
        rows_a.append(a); lower.append(residual[i]); upper.append(residual[i])
    for i in range(k):
        a = np.zeros(nvar)
        for p, (_, left, _) in enumerate(patterns):
            a[p] = i in left
        rows_a.append(a); lower.append(need[i]); upper.append(np.inf)
    for p in range(m):
        # y_p <= x_p <= 11 y_p.
        a = np.zeros(nvar); a[p] = 1; a[m+p] = -1
        rows_a.append(a); lower.append(0); upper.append(np.inf)
        a = np.zeros(nvar); a[p] = 1; a[m+p] = -11
        rows_a.append(a); lower.append(-np.inf); upper.append(0)
    helper_constraints = 0
    for p, (state_p, left_p, _) in enumerate(patterns):
        if len(left_p) == 1:
            continue
        for i in left_p:
            helpers = []
            for q, (state_q, left_q, _) in enumerate(patterns):
                if q == p or state_q[i] != 0:
                    continue
                if any(state_q[j] == 0 for j in left_p if j != i):
                    continue
                if any(state_p[j] == 0 for j in left_q):
                    continue
                helpers.append(q)
            a = np.zeros(nvar); a[m+p] = 1
            for q in helpers:
                a[m+q] -= 1
            rows_a.append(a); lower.append(-np.inf); upper.append(0)
            helper_constraints += 1
    result = milp(
        np.zeros(nvar),
        integrality=np.ones(nvar),
        bounds=Bounds(np.zeros(nvar),
                      np.concatenate([np.full(m, 11.0), np.ones(m)])),
        constraints=LinearConstraint(csc_matrix(np.vstack(rows_a)),
                                    np.array(lower), np.array(upper)),
        options={"time_limit": 300.0},
    )
    key = (row.get("mask"), row.get("unit_mask"), row.get("heavy_neighbours"))
    answer = {
        "index": index, "support": support, "key": key,
        "patterns": m, "helper_constraints": helper_constraints,
        "status": int(result.status), "success": bool(result.success),
        "message": result.message,
    }
    if result.success:
        answer["population"] = [
            {"state": patterns[p][0], "count": int(round(result.x[p]))}
            for p in range(m) if result.x[p] > 0.5
        ]
    return answer


if __name__ == "__main__":
    source_rows = survivors()
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(solve, enumerate(source_rows), chunksize=1))
    rows.sort(key=lambda row: row["index"])
    print(json.dumps({
        "kernels": len(rows),
        "feasible": sum(row["success"] for row in rows),
        "infeasible": sum(row["status"] == 2 for row in rows),
        "unknown": sum(row["status"] not in (0, 2) for row in rows),
        "by_support": {
            str(s): {
                "kernels": sum(row["support"] == s for row in rows),
                "feasible": sum(row["support"] == s and row["success"] for row in rows),
            } for s in (8, 9, 10)
        },
        "rows": rows,
        "scope": "Independent combined source/supplement MILP replay; numerical MILP certificate status is internal computer-assisted evidence, not graph realization.",
    }, indent=2))
