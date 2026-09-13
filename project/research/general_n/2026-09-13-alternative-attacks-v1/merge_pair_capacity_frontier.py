#!/usr/bin/env python3
"""Merge and verify sharded pair-capacity frontier scans."""
from pathlib import Path
import argparse
import csv
import hashlib
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directory")
    ap.add_argument("--shards", type=int, default=32)
    ap.add_argument("--output", default="PAIR_CAPACITY_FRONTIER_FULL.tsv")
    args = ap.parse_args()

    root = Path(args.directory)
    header = None
    rows = []
    selected_total = 0
    canonical_active = None
    ledger_ids = None

    for rem in range(args.shards):
        tsv = root / f"PAIR_CAPACITY_SHARD_{rem}.tsv"
        ver = root / f"PAIR_CAPACITY_SHARD_{rem}_INPUT_VERIFICATION.json"
        assert tsv.is_file(), tsv
        assert ver.is_file(), ver
        meta = json.loads(ver.read_text())
        assert meta["filter"] == {"mod": args.shards, "rem": rem}
        selected_total += meta["selected"]
        if canonical_active is None:
            canonical_active = meta["canonical_active"]
            ledger_ids = meta["ledger_closed_n34"]
        else:
            assert meta["canonical_active"] == canonical_active
            assert meta["ledger_closed_n34"] == ledger_ids

        with tsv.open() as f:
            reader = csv.DictReader(f, delimiter="\t")
            if header is None:
                header = reader.fieldnames
            else:
                assert reader.fieldnames == header
            rows.extend(reader)

    assert canonical_active is not None
    assert selected_total == canonical_active
    assert len(rows) == canonical_active
    keys = {(int(r["layer"]), int(r["state_id"])) for r in rows}
    assert len(keys) == canonical_active

    rows.sort(key=lambda r: (int(r["layer"]), int(r["state_id"])))
    out = Path(args.output)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    report = {
        "schema": "pair-capacity-frontier-merge-v1",
        "status": "PASS",
        "shards": args.shards,
        "canonical_active": canonical_active,
        "selected_total": selected_total,
        "rows": len(rows),
        "unique_state_keys": len(keys),
        "ledger_closed_n34": ledger_ids,
        "output": str(out),
        "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
    }
    Path(out.stem + "_MERGE_VERIFICATION.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
