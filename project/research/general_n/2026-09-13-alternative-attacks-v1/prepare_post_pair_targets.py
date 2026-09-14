#!/usr/bin/env python3
"""Prepare specific ledger-current states for post-pair relational auditing.

Transport only: this applies no theorem. It decodes the frozen compatible-
routing survivor catalogue, removes every currently promoted N34/N35 closure
from the corresponding canonical whole-state ledgers, and emits exactly the
requested active state IDs in the input format consumed by the relational
scanners.
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

LEDGERS = {
    "n34-m289": HERE / "WHOLE_STATE_LEDGER.tsv",
    "n35-m306": HERE / "WHOLE_STATE_LEDGER_N35.tsv",
}
LAYERS = {"n34-m289": 0, "n35-m306": 1}


def parse_ids(text: str) -> list[int]:
    ids = [int(x) for x in text.split(",") if x.strip()]
    if not ids:
        raise SystemExit("--ids must contain at least one state id")
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate id in --ids")
    return ids


def ledger_closed(path: Path) -> set[int]:
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = [int(r["state"]) for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"duplicate state in {path.name}")
    return set(ids)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", required=True, help="comma-separated active state ids")
    ap.add_argument("--output", default="POST_PAIR_TARGET_INPUT.txt")
    args = ap.parse_args()

    requested = parse_ids(args.ids)
    closed = {layer: ledger_closed(path) for layer, path in LEDGERS.items()}
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    if len(combined) != 4584:
        raise SystemExit(f"unexpected frozen combined survivor count: {len(combined)}")

    active = [
        r for r in combined
        if int(r["state_id"]) not in closed[r["layer"]]
    ]
    expected_active = 4584 - sum(len(ids) for ids in closed.values())
    if len(active) != expected_active:
        raise SystemExit(("active-count mismatch", len(active), expected_active))

    by_id: dict[int, list[dict]] = {}
    for row in active:
        by_id.setdefault(int(row["state_id"]), []).append(row)

    missing = [state for state in requested if state not in by_id]
    ambiguous = [state for state in requested if len(by_id.get(state, [])) != 1]
    if missing:
        raise SystemExit(f"requested states not active in ledger-current frontier: {missing}")
    if ambiguous:
        raise SystemExit(f"requested state id is not unique across active layers: {ambiguous}")

    selected = [by_id[state][0] for state in requested]
    out = Path(args.output)
    lines = [str(len(selected))]
    for row in selected:
        vals = [
            LAYERS[row["layer"]], row["state_id"], row["a"], row["b"], row["t"],
            len(row["s"]), *row["s"], len(row["rho"]), *row["rho"],
        ]
        lines.append(" ".join(map(str, vals)))
    out.write_text("\n".join(lines) + "\n")

    report = {
        "schema": "post-pair-target-input-v2",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "ledger_sha256": {
            layer: hashlib.sha256(path.read_bytes()).hexdigest()
            for layer, path in LEDGERS.items()
        },
        "ledger_closure_count": {layer: len(ids) for layer, ids in closed.items()},
        "canonical_active": len(active),
        "requested_ids": requested,
        "selected": [
            {
                "layer": row["layer"],
                "state_id": row["state_id"],
                "a": row["a"],
                "b": row["b"],
                "t": row["t"],
                "S": sum(row["s"]),
            }
            for row in selected
        ],
        "output": str(out),
        "output_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
        "note": "Transport only; no relational exclusion is claimed here.",
        "external_review": "OPEN",
    }
    Path(out.stem + "_VERIFICATION.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
