#!/usr/bin/env python3
"""Prepare deterministic E=0 input from the canonical frozen frontier.

Transport only. This script applies no new theorem. It hash-verifies the frozen
compatible-routing survivor stream, removes the 16 canonical whole-state N34
closures, and writes the selected shard in a compact text format for the exact
orientation/selected-incidence scanner.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

CLOSED_N34 = {227, 279, 588, 526, 382, 519, 230, 282, 385, 153, 122, 283, 154, 231, 77, 60}
LAYERS = {"n34-m289": 0, "n35-m306": 1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-s", type=int, default=None)
    ap.add_argument("--mod", type=int, default=1)
    ap.add_argument("--rem", type=int, default=0)
    ap.add_argument("--output", default="ORIENTATION_E0_FRONTIER_INPUT.txt")
    args = ap.parse_args()
    assert args.mod >= 1 and 0 <= args.rem < args.mod

    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584
    active = [
        r for r in combined
        if not (r["layer"] == "n34-m289" and r["state_id"] in CLOSED_N34)
    ]
    assert len(active) == 4568
    active.sort(key=lambda r: (r["layer"], r["state_id"]))

    selected = []
    for idx, r in enumerate(active):
        if args.max_s is not None and max(r["s"]) > args.max_s:
            continue
        if idx % args.mod != args.rem:
            continue
        selected.append(r)

    out = Path(args.output)
    lines = [str(len(selected))]
    for r in selected:
        assert r["layer"] in LAYERS
        vals = [
            LAYERS[r["layer"]], r["state_id"], r["a"], r["b"], r["t"],
            len(r["s"]), *r["s"], len(r["rho"]), *r["rho"],
        ]
        lines.append(" ".join(map(str, vals)))
    out.write_text("\n".join(lines) + "\n")

    report = {
        "schema": "orientation-e0-frontier-input-v1",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_active": len(active),
        "selected": len(selected),
        "filter": {"max_s": args.max_s, "mod": args.mod, "rem": args.rem},
        "selected_layers": {
            layer: sum(r["layer"] == layer for r in selected) for layer in LAYERS
        },
        "output": str(out),
        "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
        "note": "Transport only; no E=0 exclusion is claimed by this preparation step.",
        "external_review": "OPEN",
    }
    Path(out.stem + "_VERIFICATION.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
