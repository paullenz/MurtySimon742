#!/usr/bin/env python3
"""Fresh full replay of the saved r=12 support-ten source MILP stage.

This driver deliberately recomputes every kernel from the compressed orbit
ledger.  It reuses the committed per-kernel mathematical encoding, but does not
trust or read the eight saved result shards when producing its replay count.
"""

import argparse
import gzip
import hashlib
import json
import multiprocessing as mp
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent / "2026-09-22-independent-742-r12-quotient"
sys.path.insert(0, str(PACKAGE))
from r12_support10_case1_source_chunk import one  # noqa: E402


def identity(row):
    return (row["unit_graph"], row["heavy_edge"], row["a_mask"], row["b_mask"])


def run_task(task):
    shard, line = task
    return shard, one(line)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shards", default="0,1,2,3,4,5,6,7")
    parser.add_argument("--workers", type=int, default=9)
    args = parser.parse_args()
    shards = sorted({int(value) for value in args.shards.split(",")})
    assert shards and all(0 <= shard < 8 for shard in shards)

    with gzip.open(PACKAGE / "r12_support10_case1_masks.txt.gz", "rt") as source:
        lines = source.read().splitlines()
    assert len(lines) == 6386

    tasks = []
    for shard in shards:
        lo = len(lines) * shard // 8
        hi = len(lines) * (shard + 1) // 8
        tasks.extend((shard, line) for line in lines[lo:hi])

    feasible = []
    unknown = []
    by_shard = {shard: 0 for shard in shards}
    processed = 0
    with mp.Pool(args.workers) as pool:
        for shard, row in pool.imap_unordered(run_task, tasks, chunksize=1):
            processed += 1
            if row.get("population"):
                feasible.append(row)
                by_shard[shard] += 1
            if row["status"] not in (0, 2):
                unknown.append(row)
            if processed % 400 == 0:
                print(f"PROGRESS {processed}/{len(tasks)} feasible={len(feasible)} unknown={len(unknown)}", flush=True)

    ids = sorted(identity(row) for row in feasible)
    digest = hashlib.sha256(
        "\n".join(" ".join(map(str, item)) for item in ids).encode()
    ).hexdigest()
    saved_ids = []
    for shard in shards:
        saved = json.loads((PACKAGE / f"r12_support10_case1_source_chunk{shard}.json").read_text())
        saved_ids.extend(identity(row) for row in saved["feasible_rows"])
    saved_ids.sort()
    print("RESULT_BEGIN")
    print(json.dumps({
        "selected_shards": shards,
        "strict_kernels_replayed": len(tasks),
        "source_feasible_by_shard": by_shard,
        "source_feasible_total": len(feasible),
        "solver_unknown_total": len(unknown),
        "distinct_kernel_identities": len(set(ids)),
        "feasible_identity_sha256": digest,
        "feasible_identities": ids,
        "matches_saved_feasible_identities": ids == saved_ids,
        "scope": "Fresh execution of all 6,386 committed per-kernel source MILPs; reuses the committed mathematical encoding and is not an independent reimplementation of that encoding.",
    }, indent=2, sort_keys=True))
    print("RESULT_END")


if __name__ == "__main__":
    main()
