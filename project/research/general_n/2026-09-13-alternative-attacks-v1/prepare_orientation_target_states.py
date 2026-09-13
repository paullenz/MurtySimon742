#!/usr/bin/env python3
"""Extract named canonical survivor states for exact orientation/excess scans.

Transport only. No theorem is applied. The source survivor stream is decoded
through the existing hash-verifying evidence reader.
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
    ap.add_argument("--state", type=int, action="append", required=True)
    ap.add_argument("--layer", choices=sorted(LAYERS), default="n34-m289")
    ap.add_argument("--output", default="ORIENTATION_TARGET_STATES_INPUT.txt")
    args = ap.parse_args()

    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584
    active = [
        r for r in combined
        if not (r["layer"] == "n34-m289" and r["state_id"] in CLOSED_N34)
    ]
    assert len(active) == 4568

    want = set(args.state)
    chosen = [r for r in active if r["layer"] == args.layer and r["state_id"] in want]
    chosen.sort(key=lambda r: r["state_id"])
    found = {r["state_id"] for r in chosen}
    missing = sorted(want - found)
    if missing:
        raise SystemExit(f"requested active states not found: {missing}")

    out = Path(args.output)
    lines = [str(len(chosen))]
    metadata = []
    for r in chosen:
        vals = [
            LAYERS[r["layer"]], r["state_id"], r["a"], r["b"], r["t"],
            len(r["s"]), *r["s"], len(r["rho"]), *r["rho"],
        ]
        lines.append(" ".join(map(str, vals)))
        metadata.append({
            "layer": r["layer"], "state_id": r["state_id"],
            "a": r["a"], "b": r["b"], "t": r["t"],
            "s": r["s"], "rho": r["rho"],
            "S": sum(r["s"]), "R": sum(r["rho"]),
        })
    out.write_text("\n".join(lines) + "\n")

    report = {
        "schema": "orientation-target-states-input-v1",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "requested": sorted(want),
        "selected": metadata,
        "output": str(out),
        "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
        "note": "Transport only; no exclusion is claimed by this preparation step.",
        "external_review": "OPEN",
    }
    Path(out.stem + "_VERIFICATION.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
