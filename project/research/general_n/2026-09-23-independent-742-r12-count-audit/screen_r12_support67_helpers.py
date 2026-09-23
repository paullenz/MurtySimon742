#!/usr/bin/env python3
"""Hostile residual-free-helper screen for saved r=12 support 6/7 survivors."""

import ast
import json
import multiprocessing as mp
from pathlib import Path

from screen_support10_case1_helpers import solve


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent / "2026-09-22-r12-quotient-v1"


def normalize(row, residual, support, index, source):
    out = dict(row)
    out["R"] = list(residual)
    out["shard"] = source
    out["unit_graph"] = out["mask"]
    out["heavy_edge"] = support
    out["a_mask"] = index
    out["b_mask"] = 0
    return out


def inputs():
    rows = []
    support6 = json.loads((PACKAGE / "r12_support6.json").read_text())
    for partition, data in support6.items():
        residual = ast.literal_eval(partition)
        for index, row in enumerate(data["feasible"]):
            rows.append(normalize(row, residual, 6, index, partition))
    support7 = json.loads((PACKAGE / "r12_support7_sources.json").read_text())
    for index, row in enumerate(support7["rows"]):
        rows.append(normalize(row, row["R"], 7, index, "r12_support7_sources.json"))
    return rows


def main():
    rows = inputs()
    with mp.Pool(5) as pool:
        results = list(pool.imap_unordered(solve, enumerate(rows)))
    results.sort(key=lambda row: row["index"])
    print("RESULT_BEGIN")
    print(json.dumps({
        "kernels": len(results),
        "support6_kernels": sum(row["identity"][1] == 6 for row in results),
        "support7_kernels": sum(row["identity"][1] == 7 for row in results),
        "feasible": sum(row["success"] for row in results),
        "infeasible": sum(row["status"] == 2 for row in results),
        "unknown": sum(row["status"] not in (0, 2) for row in results),
        "free_types_min": min(row["residual_free_types"] for row in results),
        "free_types_max": max(row["residual_free_types"] for row in results),
        "free_discharges_total": sum(row["free_discharges"] for row in results),
        "rows": results,
        "scope": "Optimistic residual-free-helper necessary-condition MILP over all saved r=12 support-6/7 source survivors; not an independent source reimplementation or graph realization.",
    }, indent=2, sort_keys=True))
    print("RESULT_END")


if __name__ == "__main__":
    main()
