#!/usr/bin/env python3
"""Merge and verify exact E=0 scan shards."""
from pathlib import Path
import argparse
import csv
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directory")
    ap.add_argument("--shards", type=int, default=16)
    ap.add_argument("--output", default="ORIENTATION_E0_FULL.tsv")
    args = ap.parse_args()
    root = Path(args.directory)
    all_rows = []
    header = None
    selected_total = 0
    seen_rems = set()
    for rem in range(args.shards):
        tsv = root / f"ORIENTATION_E0_SHARD_{rem}.tsv"
        ver = root / f"ORIENTATION_E0_SHARD_{rem}_INPUT_VERIFICATION.json"
        assert tsv.is_file(), tsv
        assert ver.is_file(), ver
        meta = json.loads(ver.read_text())
        assert meta["canonical_active"] == 4568
        assert meta["filter"] == {"max_s": None, "mod": args.shards, "rem": rem}
        selected_total += meta["selected"]
        seen_rems.add(rem)
        with tsv.open() as f:
            reader = csv.DictReader(f, delimiter="\t")
            if header is None:
                header = reader.fieldnames
            else:
                assert reader.fieldnames == header
            all_rows.extend(reader)
    assert seen_rems == set(range(args.shards))
    assert selected_total == 4568
    assert len(all_rows) == 4568
    keys = {(int(r["layer"]), int(r["state_id"])) for r in all_rows}
    assert len(keys) == 4568
    all_rows.sort(key=lambda r: (int(r["layer"]), int(r["state_id"])))
    out = Path(args.output)
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(all_rows)
    print(json.dumps({
        "status": "PASS",
        "shards": args.shards,
        "selected_total": selected_total,
        "rows": len(all_rows),
        "unique_state_keys": len(keys),
        "output": str(out),
    }, indent=2))


if __name__ == "__main__":
    main()
