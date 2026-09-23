#!/usr/bin/env python3
"""Hostile residual-free-helper screen for saved r=12 support 8/9 survivors.

This reuses the optimistic helper-aware MILP from the audited support-ten
screen.  It closes a semantic gap in the legacy supplement outputs; it does
not independently reimplement the source screens or establish realizability.
"""

import json
import multiprocessing as mp
from pathlib import Path

from screen_support10_case1_helpers import solve


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent / "2026-09-22-independent-742-r12-quotient"


def inputs():
    rows = []
    files = sorted(path.name for path in PACKAGE.glob("r12_support8_sources_case*.json"))
    files += sorted(path.name for path in PACKAGE.glob("r12_support9_sources_case*.json"))
    for name in files:
        data = json.loads((PACKAGE / name).read_text())
        support = 8 if "support8" in name else 9
        for source_index, original in enumerate(data["feasible_rows"]):
            row = dict(original)
            # The imported solver uses only R and edges mathematically.  These
            # compatibility fields make its diagnostic identity explicit.
            row["shard"] = name
            row["unit_graph"] = row["mask"]
            row["heavy_edge"] = support
            row["a_mask"] = source_index
            row["b_mask"] = 0
            rows.append(row)
    return rows


def main():
    rows = inputs()
    with mp.Pool(9) as pool:
        results = list(pool.imap_unordered(solve, enumerate(rows)))
    results.sort(key=lambda row: row["index"])
    print("RESULT_BEGIN")
    print(json.dumps({
        "kernels": len(results),
        "support8_kernels": sum(row["identity"][1] == 8 for row in results),
        "support9_kernels": sum(row["identity"][1] == 9 for row in results),
        "feasible": sum(row["success"] for row in results),
        "infeasible": sum(row["status"] == 2 for row in results),
        "unknown": sum(row["status"] not in (0, 2) for row in results),
        "free_types_min": min(row["residual_free_types"] for row in results),
        "free_types_max": max(row["residual_free_types"] for row in results),
        "free_discharges_total": sum(row["free_discharges"] for row in results),
        "rows": results,
        "scope": "Optimistic residual-free-helper necessary-condition MILP over all saved r=12 support-8/9 source survivors; not an independent source reimplementation or graph realization.",
    }, indent=2, sort_keys=True))
    print("RESULT_END")


if __name__ == "__main__":
    main()
