#!/usr/bin/env python3
"""Fresh full replay of the saved r=12 support-ten source MILP stage.

This driver deliberately recomputes every kernel from the compressed orbit
ledger.  It reuses the committed per-kernel mathematical encoding, but does not
trust or read the eight saved result shards when producing its replay count.
"""

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


def main():
    with gzip.open(PACKAGE / "r12_support10_case1_masks.txt.gz", "rt") as source:
        lines = source.read().splitlines()
    assert len(lines) == 6386

    feasible = []
    unknown = []
    processed = 0
    with mp.Pool(16) as pool:
        for row in pool.imap_unordered(one, lines, chunksize=1):
            processed += 1
            if row.get("population"):
                feasible.append(row)
            if row["status"] not in (0, 2):
                unknown.append(row)
            if processed % 400 == 0:
                print(f"PROGRESS {processed}/6386 feasible={len(feasible)} unknown={len(unknown)}", flush=True)

    ids = sorted(identity(row) for row in feasible)
    digest = hashlib.sha256(
        "\n".join(" ".join(map(str, item)) for item in ids).encode()
    ).hexdigest()
    print("RESULT_BEGIN")
    print(json.dumps({
        "strict_kernels_replayed": len(lines),
        "source_feasible_total": len(feasible),
        "solver_unknown_total": len(unknown),
        "distinct_kernel_identities": len(set(ids)),
        "feasible_identity_sha256": digest,
        "feasible_identities": ids,
        "scope": "Fresh execution of all 6,386 committed per-kernel source MILPs; reuses the committed mathematical encoding and is not an independent reimplementation of that encoding.",
    }, indent=2, sort_keys=True))
    print("RESULT_END")


if __name__ == "__main__":
    main()
