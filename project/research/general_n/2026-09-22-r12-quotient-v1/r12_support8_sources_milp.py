#!/usr/bin/env python3
"""Partition-sharded source MILP for r=12 support-eight strict cores."""
import json
import multiprocessing as mp
import sys
from r11_support8_sources_milp import one

PARTITIONS = [
    (5,1,1,1,1,1,1,1),
    (4,2,1,1,1,1,1,1),
    (3,3,1,1,1,1,1,1),
    (3,2,2,1,1,1,1,1),
    (2,2,2,2,1,1,1,1),
]

if __name__ == "__main__":
    case = int(sys.argv[1])
    lines = [line for line in open("r12_support8_masks.txt")
             if int(line.split()[0]) == case]
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(one, lines, chunksize=2))
    feasible = [row for row in rows if row.get("population")]
    unknown = [row for row in rows if row["status"] not in (0, 2)]
    print(json.dumps({
        "case": case, "partition": PARTITIONS[case],
        "strict_core_orbits": len(lines),
        "source_feasible": len(feasible), "solver_unknown": len(unknown),
        "feasible_rows": feasible, "unknown_rows": unknown,
        "scope": "Integer physical-source necessary condition encoded as MILP; internal computer-assisted result, not graph realization.",
    }, indent=2, sort_keys=True))
