#!/usr/bin/env python3
"""Independently aggregate the eight saved r=12 support-ten source shards."""

import glob
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "2026-09-22-independent-742-r12-quotient"


def main():
    files = sorted(PACKAGE.glob("r12_support10_case1_source_chunk[0-7].json"))
    assert len(files) == 8, len(files)
    expected_lo = 0
    rows = []
    shard_counts = []
    unknown = 0
    for index, path in enumerate(files):
        data = json.loads(path.read_text())
        assert data["chunk"] == index
        lo, hi = data["range"]
        assert lo == expected_lo, (path, lo, expected_lo)
        assert hi - lo == data["strict_core_orbits"]
        assert data["source_feasible"] == len(data["feasible_rows"])
        assert data["solver_unknown"] == len(data["unknown_rows"])
        expected_lo = hi
        rows.extend(data["feasible_rows"])
        unknown += data["solver_unknown"]
        shard_counts.append(data["source_feasible"])

    identities = {
        (row["unit_graph"], row["heavy_edge"], row["a_mask"], row["b_mask"])
        for row in rows
    }
    assert expected_lo == 6386
    assert len(rows) == len(identities)
    assert unknown == 0
    assert {tuple(row["R"]) for row in rows} == {(2, 2, 1, 1, 1, 1, 1, 1, 1, 1)}
    assert {row["t_upper"] for row in rows} == {1}

    result = {
        "strict_kernels": expected_lo,
        "source_feasible_by_shard": shard_counts,
        "source_feasible_total": len(rows),
        "distinct_kernel_identities": len(identities),
        "solver_unknown_total": unknown,
        "saved_audit_claim": 42,
        "claim_matches_saved_shards": len(rows) == 42,
        "status": "COUNT_MISMATCH_FREEZE" if len(rows) != 42 else "PASS",
        "scope": "Saved-shard aggregate only; does not independently rerun the source MILPs.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
