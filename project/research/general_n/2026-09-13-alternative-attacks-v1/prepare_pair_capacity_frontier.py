#!/usr/bin/env python3
"""Prepare the current canonical survivor frontier for pair-capacity scanning.

Transport only. This script applies no new theorem. It hash-verifies and decodes
the frozen compatible-routing survivor stream, then removes every N34 and N35
state currently listed in the layer-specific whole-state ledgers. This avoids
hard-coding a stale closure set as the canonical ledgers grow.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

N34_LEDGER = HERE / "WHOLE_STATE_LEDGER.tsv"
N35_LEDGER = HERE / "WHOLE_STATE_LEDGER_N35.tsv"
LAYERS = {"n34-m289": 0, "n35-m306": 1}


def ledger_closed(path):
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = {int(r["state"]) for r in rows}
    if len(ids) != len(rows):
        raise SystemExit(f"duplicate state in {path.name}")
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mod", type=int, default=1)
    ap.add_argument("--rem", type=int, default=0)
    ap.add_argument("--output", default="PAIR_CAPACITY_FRONTIER_INPUT.txt")
    args = ap.parse_args()
    assert args.mod >= 1 and 0 <= args.rem < args.mod

    closed_n34 = ledger_closed(N34_LEDGER)
    closed_n35 = ledger_closed(N35_LEDGER)
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584

    active = [
        r for r in combined
        if not (
            (r["layer"] == "n34-m289" and r["state_id"] in closed_n34)
            or (r["layer"] == "n35-m306" and r["state_id"] in closed_n35)
        )
    ]
    expected = 4584 - len(closed_n34) - len(closed_n35)
    assert len(active) == expected, (len(active), expected)
    active.sort(key=lambda r: (r["layer"], r["state_id"]))

    selected = [r for idx, r in enumerate(active) if idx % args.mod == args.rem]

    out = Path(args.output)
    lines = [str(len(selected))]
    for r in selected:
        vals = [
            LAYERS[r["layer"]], r["state_id"], r["a"], r["b"], r["t"],
            len(r["s"]), *r["s"], len(r["rho"]), *r["rho"],
        ]
        lines.append(" ".join(map(str, vals)))
    out.write_text("\n".join(lines) + "\n")

    report = {
        "schema": "pair-capacity-frontier-input-v2-layered-ledger",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "ledger_closed_n34": sorted(closed_n34),
        "ledger_closed_n35": sorted(closed_n35),
        "ledger_closure_count_n34": len(closed_n34),
        "ledger_closure_count_n35": len(closed_n35),
        "ledger_closure_count": len(closed_n34) + len(closed_n35),
        "canonical_active": len(active),
        "selected": len(selected),
        "filter": {"mod": args.mod, "rem": args.rem},
        "selected_layers": {
            layer: sum(r["layer"] == layer for r in selected) for layer in LAYERS
        },
        "output": str(out),
        "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
        "note": "Transport only; no pair-capacity or relational exclusion is claimed here.",
        "external_review": "OPEN",
    }
    Path(out.stem + "_VERIFICATION.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
