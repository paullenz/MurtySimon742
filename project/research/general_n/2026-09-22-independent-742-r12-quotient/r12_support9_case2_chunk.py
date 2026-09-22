#!/usr/bin/env python3
"""Chunked exact source MILP for r=12 support-nine partition (2,2,2,1^6)."""
import json
import multiprocessing as mp
import sys

from r11_support9_sources_milp import one


if __name__ == "__main__":
    chunk = int(sys.argv[1])
    chunks = int(sys.argv[2])
    all_lines = [
        line for line in open("r12_support9_masks.txt")
        if int(line.split()[0]) == 2
    ]
    lo = len(all_lines) * chunk // chunks
    hi = len(all_lines) * (chunk + 1) // chunks
    lines = all_lines[lo:hi]
    with mp.Pool(8) as pool:
        rows = list(pool.imap_unordered(one, lines, chunksize=2))
    feasible = [row for row in rows if row.get("population")]
    unknown = [row for row in rows if row["status"] not in (0, 2)]
    print(json.dumps({
        "case": 2,
        "partition": [2, 2, 2, 1, 1, 1, 1, 1, 1],
        "chunk": chunk,
        "chunks": chunks,
        "range": [lo, hi],
        "strict_core_orbits": len(lines),
        "source_feasible": len(feasible),
        "solver_unknown": len(unknown),
        "feasible_rows": feasible,
        "unknown_rows": unknown,
        "scope": "Integer physical-source necessary condition encoded as MILP; internal computer-assisted result, not graph realization.",
    }, indent=2, sort_keys=True))

