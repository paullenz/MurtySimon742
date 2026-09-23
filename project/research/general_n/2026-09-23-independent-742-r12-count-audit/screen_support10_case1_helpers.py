#!/usr/bin/env python3
"""Helper-aware source/supplement MILP for saved r=12 support-ten survivors.

Residual-free helper types are admitted under the same optimistic semantics as
the 23 September hostile r=11 audit.  Therefore infeasibility is useful exact
evidence for the abstract necessary-condition system; feasibility is only a
survivor and is not graph realizability.
"""

import itertools
import json
import multiprocessing as mp
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent / "2026-09-22-independent-742-r12-quotient"


def inputs():
    rows = []
    for shard in range(8):
        data = json.loads((PACKAGE / f"r12_support10_case1_source_chunk{shard}.json").read_text())
        for row in data["feasible_rows"]:
            row = dict(row)
            row["shard"] = shard
            rows.append(row)
    return rows


def solve(item):
    index, row = item
    residual = tuple(row["R"])
    edges = [tuple(edge) for edge in row["edges"]]
    k = len(residual)
    neighbours = [set() for _ in residual]
    degrees = [0] * k
    for i, j in edges:
        neighbours[i].add(j)
        neighbours[j].add(i)
        degrees[i] += 1
        degrees[j] += 1
    need = tuple(max(0, degrees[i] - residual[i]) for i in range(k))
    positive = {i for i, value in enumerate(need) if value > 0}

    patterns = []
    free = []
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

    m = len(patterns)
    nvar = 2 * m
    constraints = []
    lower = []
    upper = []
    for i in range(k):
        vector = np.zeros(nvar)
        for p, (_, _, zero) in enumerate(patterns):
            vector[p] = i in zero
        constraints.append(vector)
        lower.append(residual[i])
        upper.append(residual[i])
    for i in range(k):
        vector = np.zeros(nvar)
        for p, (_, left, _) in enumerate(patterns):
            vector[p] = i in left
        constraints.append(vector)
        lower.append(need[i])
        upper.append(np.inf)
    for p in range(m):
        vector = np.zeros(nvar)
        vector[p] = 1
        vector[m + p] = -1
        constraints.append(vector)
        lower.append(0)
        upper.append(np.inf)
        vector = np.zeros(nvar)
        vector[p] = 1
        vector[m + p] = -12
        constraints.append(vector)
        lower.append(-np.inf)
        upper.append(0)

    helper_constraints = 0
    free_discharges = 0
    for p, (state_p, left_p, _) in enumerate(patterns):
        if len(left_p) == 1:
            continue
        for i in left_p:
            def helps(state_q, left_q):
                return (state_q[i] == 0 and
                        all(state_q[j] != 0 for j in left_p if j != i) and
                        all(state_p[j] != 0 for j in left_q))

            if any(helps(state_q, left_q) for state_q, left_q in free):
                free_discharges += 1
                continue
            helpers = [q for q, (state_q, left_q, _) in enumerate(patterns)
                       if q != p and helps(state_q, left_q)]
            vector = np.zeros(nvar)
            vector[m + p] = 1
            for q in helpers:
                vector[m + q] -= 1
            constraints.append(vector)
            lower.append(-np.inf)
            upper.append(0)
            helper_constraints += 1

    result = milp(
        np.zeros(nvar),
        integrality=np.ones(nvar),
        bounds=Bounds(np.zeros(nvar), np.r_[np.full(m, 12.0), np.ones(m)]),
        constraints=LinearConstraint(
            csc_matrix(np.vstack(constraints)), np.array(lower), np.array(upper)),
        options={"time_limit": 180.0},
    )
    return {
        "index": index,
        "shard": row["shard"],
        "identity": [row["unit_graph"], row["heavy_edge"], row["a_mask"], row["b_mask"]],
        "patterns": m,
        "residual_free_types": len(free),
        "free_discharges": free_discharges,
        "helper_constraints": helper_constraints,
        "status": int(result.status),
        "success": bool(result.success),
        "message": result.message,
    }


def main():
    rows = inputs()
    with mp.Pool(9) as pool:
        results = []
        for result in pool.imap_unordered(solve, enumerate(rows)):
            results.append(result)
            print(f"PROGRESS {len(results)}/{len(rows)} success={sum(r['success'] for r in results)}", flush=True)
    results.sort(key=lambda row: row["index"])
    print("RESULT_BEGIN")
    print(json.dumps({
        "kernels": len(results),
        "feasible": sum(row["success"] for row in results),
        "infeasible": sum(row["status"] == 2 for row in results),
        "unknown": sum(row["status"] not in (0, 2) for row in results),
        "rows": results,
        "scope": "Helper-aware abstract necessary-condition MILP with optimistic residual-free helpers; infeasibility excludes a kernel at this profile layer, feasibility is not graph realizability.",
    }, indent=2, sort_keys=True))
    print("RESULT_END")


if __name__ == "__main__":
    main()
