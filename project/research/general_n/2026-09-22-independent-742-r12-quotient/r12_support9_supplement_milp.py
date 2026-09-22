#!/usr/bin/env python3
"""Combined source/supplement MILP for r=12 support-nine source survivors."""
import json
import multiprocessing as mp

from r12_support6_supplement_milp import solve


ROWS = []
for case in (0, 1):
    data = json.load(open(f"r12_support9_sources_case{case}.json"))
    for row in data["feasible_rows"]:
        ROWS.append((str(tuple(row["R"])), row))
for chunk in range(4):
    data = json.load(open(f"r12_support9_sources_case2_chunk{chunk}.json"))
    for row in data["feasible_rows"]:
        ROWS.append((str(tuple(row["R"])), row))


if __name__ == "__main__":
    with mp.Pool(min(8, len(ROWS))) as pool:
        rows = list(pool.imap_unordered(solve, enumerate(ROWS)))
    rows.sort(key=lambda row: row["index"])
    print(json.dumps({
        "kernels": len(rows),
        "feasible": sum(row["success"] for row in rows),
        "infeasible": sum(row["status"] == 2 for row in rows),
        "unknown": sum(row["status"] not in (0, 2) for row in rows),
        "rows": rows,
        "scope": "Combined integer source/supplement MILP; internal computer-assisted evidence, not graph realization.",
    }, indent=2))

