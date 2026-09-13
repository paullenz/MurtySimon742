#!/usr/bin/env python3
"""Extract the frozen 4,584 generalisation survivors with their scalar records.

This is a transport/replay utility only.  It does not apply any new theorem.
It hash-verifies the compressed compatible-catalogue evidence through the
existing evidence_io helper and intersects it with the complete spill-witness
key set used by the later pair-overlap/shared-budget continuations.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
CROSS = HERE.parent / "2026-09-13-constraint-respecting-cross-v1"
sys.path.insert(0, str(CAT))
from evidence_io import records  # noqa: E402


def main(out_path):
    pool = {(r["layer"], r["state_id"]): r for r in records("pool_inputs.jsonl")}
    full = json.loads((CROSS / "FULL_DOMAIN_SPILL_EXACT.json").read_text())
    assert full["summary"]["witnessed"] == 4584
    keys = [(w["layer"], w["state_id"]) for w in full["witnesses"]]
    assert len(keys) == len(set(keys)) == 4584
    extracted = [pool[k] for k in keys]
    assert len(extracted) == 4584

    out = Path(out_path)
    out.write_text("\n".join(json.dumps(r, sort_keys=True) for r in extracted) + "\n")
    summary = {
        "schema": "frozen-survivor-extract-v1",
        "records": len(extracted),
        "layers": {},
        "fields": sorted(extracted[0].keys()),
    }
    for r in extracted:
        summary["layers"][r["layer"]] = summary["layers"].get(r["layer"], 0) + 1
    out.with_suffix(".summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: extract_frozen_survivors.py OUTPUT.jsonl")
    main(sys.argv[1])
