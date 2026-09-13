#!/usr/bin/env python3
"""Prepare the current canonical survivor frontier for pair-capacity scanning.

Transport only. This script applies no new theorem. It hash-verifies and decodes
the frozen compatible-routing survivor stream, then removes every N34 state
currently listed in WHOLE_STATE_LEDGER.tsv. This avoids hard-coding a stale
closure set as the canonical ledger grows.
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

LEDGER = HERE / "WHOLE_STATE_LEDGER.tsv"
LAYERS = {"n34-m289": 0, "n35-m306": 1}


def ledger_closed_n34():
    with LEDGER.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = {int(r["state"]) for r in rows}
    if len(ids) != len(rows):
        raise SystemExit("duplicate state in WHOLE_STATE_LEDGER.tsv")
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mod", type=int, default=1)
    ap.add_argument("--rem", type=int, default=0)
    ap.add_argument("--output", default="PAIR_CAPACITY_FRONTIER_INPUT.txt")
    args = ap.parse_args()
    assert args.mod >= 1 and 0 <= args.rem < args.mod

    closed = ledger_closed_n34()
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584

    active = [
        r for r in combined
        if not (r["layer"] == "n34-m289" and r["state_id"] in closed)
    ]
    expected = 4584 - len(closed)
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
        "schema": "pair-capacity-frontier-input-v1",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "ledger_closed_n34": sorted(closed),
        "ledger_closure_count": len(closed),
        "canonical_active": len(active),
        "selected": len(selected),
        "filter": {"mod": args.mod, "rem": args.rem},
        "selected_layers": {
            layer: sum(r["layer"] == layer for r in selected) for layer in LAYERS
        },
        "output": str(out),
        "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
        "note": "Transport only; no pair-capacity exclusion is claimed here.",
        "external_review": "OPEN",
    }
    Path(out.stem + "_VERIFICATION.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
