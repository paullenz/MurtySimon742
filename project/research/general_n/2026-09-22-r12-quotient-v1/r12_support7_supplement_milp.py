#!/usr/bin/env python3
"""Combined source/supplement MILP for the two r=12 support-seven kernels."""
import json
import multiprocessing as mp
from r12_support6_supplement_milp import solve

SOURCE = json.load(open("r12_support7_sources.json"))
ROWS = [(str(tuple(row["R"])), row) for row in SOURCE["rows"]]

if __name__ == "__main__":
    with mp.Pool(2) as pool:
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
