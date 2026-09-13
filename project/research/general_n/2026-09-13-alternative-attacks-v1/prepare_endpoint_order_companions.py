#!/usr/bin/env python3
"""Prepare the current adjacent companion states for endpoint-order scanning.

This is transport only.  It reconstructs the frozen compatible-routing
survivor catalogue, removes the six whole-state closures now established in
the quantified programme, and emits the three remaining narrow-family
companions 230, 282 and 385 plus state 519 as a regression/reference row.
"""
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

CLOSED = {227, 279, 382, 519, 526, 588}
TARGET = {230, 282, 385, 519}


def key(r):
    return (r["layer"], r["state_id"])


def in_narrow_family(r):
    return (
        r["layer"] == "n34-m289"
        and r["a"] == 15
        and r["b"] == 18
        and r["t"] == 1
        and len(r["s"]) == 15
        and len(r["rho"]) == 18
        and set(r["s"]) <= {2, 3}
        and set(r["rho"]) <= {1, 2, 3}
        and r["s"].count(2) <= 4
        and r["rho"].count(2) <= 3
    )


def main():
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584

    bykey = {key(r): r for r in combined}
    closed_keys = {("n34-m289", x) for x in CLOSED}
    assert closed_keys <= set(bykey)
    active = [r for r in combined if key(r) not in closed_keys]
    assert len(active) == 4578

    family = [r for r in combined if in_narrow_family(r)]
    active_family = [r for r in family if key(r) not in closed_keys]
    assert {r["state_id"] for r in active_family} == {230, 282, 385}

    chosen = [r for r in family if r["state_id"] in TARGET]
    assert {r["state_id"] for r in chosen} == TARGET

    out = HERE / "endpoint_order_companions_input.txt"
    lines = [str(len(chosen))]
    for r in sorted(chosen, key=lambda x: x["state_id"]):
        vals = [
            r["state_id"],
            1 if r["state_id"] in CLOSED else 0,
            r["a"], r["b"], r["t"],
            len(r["s"]), *r["s"],
            len(r["rho"]), *r["rho"],
        ]
        lines.append(" ".join(map(str, vals)))
    out.write_text("\n".join(lines) + "\n")

    report = {
        "schema": "endpoint-order-adjacent-companions-input-v1",
        "source": "compatible-routing survivors.json (hash-verified decode)",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "frozen_survivors_before_whole_state_closures": 4584,
        "closed_whole_states": sorted(CLOSED),
        "active_survivors": len(active),
        "active_narrow_family": sorted(r["state_id"] for r in active_family),
        "scan_rows": sorted(r["state_id"] for r in chosen),
        "state519_role": "closed regression/reference",
        "input_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
        "external_review": "OPEN",
    }
    (HERE / "ENDPOINT_ORDER_COMPANIONS_INPUT.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
