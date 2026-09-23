#!/usr/bin/env python3
"""Shardable fresh physical-source replay for r=12 support-seven cores.

This restates the saved recursive exact-cover screen as an integer feasibility
problem.  It reads the source masks but not the saved source-result JSON until
the final identity comparison.
"""
import argparse
import hashlib
import itertools
import json
import multiprocessing as mp
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix

ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "project/research/general_n/2026-09-22-r12-quotient-v1"
PAIRS = list(itertools.combinations(range(7), 2))


def identity(row):
    return (row["case"], row["mask"], tuple(row["R"]))


def digest(rows):
    payload = json.dumps(sorted(identity(row) for row in rows), separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def one(line):
    fields = list(map(int, line.split()))
    case, mask, t_upper = fields[:3]
    residual = tuple(fields[3:10])
    edges = [PAIRS[q] for q in range(21) if mask >> q & 1]
    neighbours = [set() for _ in residual]
    degree = [0] * 7
    for i, j in edges:
        neighbours[i].add(j); neighbours[j].add(i)
        degree[i] += 1; degree[j] += 1
    need = tuple(max(0, degree[i] - residual[i]) for i in range(7))
    patterns = []
    for state in itertools.product(range(3), repeat=7):
        left = {i for i, value in enumerate(state) if value == 1}
        zero = {i for i, value in enumerate(state) if value == 2}
        if not zero or any(not neighbours[i] <= left | zero or
                           len(neighbours[i] & left) > residual[i] for i in left):
            continue
        patterns.append((
            tuple(int(i in zero) for i in range(7)),
            tuple(int(i in left) for i in range(7)), state))
    matrix = np.array(
        [[p[0][i] for p in patterns] for i in range(7)] +
        [[p[1][i] for p in patterns] for i in range(7)], dtype=float)
    result = milp(
        np.zeros(len(patterns)), integrality=np.ones(len(patterns)),
        bounds=Bounds(np.zeros(len(patterns)), np.full(len(patterns), np.inf)),
        constraints=LinearConstraint(
            csc_matrix(matrix), np.array(residual + need, dtype=float),
            np.array(residual + (10**9,) * 7, dtype=float)),
        options={"time_limit": 120.0})
    row = {
        "case": case, "mask": mask, "R": residual, "t_upper": t_upper,
        "status": int(result.status), "message": result.message,
        "patterns": len(patterns), "degrees": degree, "need": need,
    }
    if result.success:
        row["population"] = [
            {"state": patterns[q][2], "count": int(round(value))}
            for q, value in enumerate(result.x) if value > 0.5]
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard", type=int, required=True)
    parser.add_argument("--shards", type=int, default=16)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    assert 0 <= args.shard < args.shards
    lines = (PACKAGE / "r12_support7_masks.txt").read_text().splitlines()
    lo = len(lines) * args.shard // args.shards
    hi = len(lines) * (args.shard + 1) // args.shards
    with mp.Pool(args.workers) as pool:
        rows = list(pool.imap_unordered(one, lines[lo:hi], chunksize=1))
    feasible = [row for row in rows if row.get("population")]
    unknown = [row for row in rows if row["status"] not in (0, 2)]
    saved = json.loads((PACKAGE / "r12_support7_sources.json").read_text())["rows"]
    saved_subset = [row for row in saved if any(
        identity(row) == identity(candidate) for candidate in feasible)]
    result = {
        "partition": [1] * 7, "shard": args.shard, "shards": args.shards,
        "range": [lo, hi], "strict_core_orbits": hi - lo,
        "source_feasible": len(feasible), "solver_unknown": len(unknown),
        "feasible_identity_sha256": digest(feasible),
        "saved_matching_identity_sha256": digest(saved_subset),
        "identity_match_for_fresh_feasible": digest(feasible) == digest(saved_subset),
        "feasible_rows": feasible, "unknown_rows": unknown,
        "scope": "Fresh integer replay of the exact physical-source necessary condition; not graph realization.",
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: result[key] for key in (
        "shard", "range", "strict_core_orbits", "source_feasible",
        "solver_unknown", "identity_match_for_fresh_feasible")}, sort_keys=True))


if __name__ == "__main__":
    main()
