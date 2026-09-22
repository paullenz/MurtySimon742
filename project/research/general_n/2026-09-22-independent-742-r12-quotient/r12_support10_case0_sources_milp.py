#!/usr/bin/env python3
"""Physical-source MILP screen for r=12 support-ten partition (3,1^9)."""
import json
import multiprocessing as mp

from r11_support10_sources_milp import one


if __name__ == "__main__":
    lines = open("r12_support10_case0_masks.txt").read().splitlines()
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(one, lines, chunksize=1))
    feasible = [row for row in rows if row.get("population")]
    unknown = [row for row in rows if row["status"] not in (0, 2)]
    print(json.dumps({
        "partition": [3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "strict_core_orbits": len(lines),
        "source_feasible": len(feasible),
        "solver_unknown": len(unknown),
        "feasible_rows": feasible,
        "unknown_rows": unknown,
        "scope": "Integer physical-source necessary condition encoded as MILP; internal computer-assisted result, not graph realization.",
    }, indent=2, sort_keys=True))

