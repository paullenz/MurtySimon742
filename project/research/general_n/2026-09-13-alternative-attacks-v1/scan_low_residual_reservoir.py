#!/usr/bin/env python3
"""Scan the ledger-current frontier with LOW_RESIDUAL_RESERVOIR_BOUND.md.

For each current scalar survivor, compute the explicit selection-free upper
bound on Q from the guaranteed low-c reservoir supplied by vertices below the
minimum positive demand. Since every legal branch has Q>=S, a state is
excluded whenever S exceeds this upper bound.

This scan performs no q enumeration and uses only integer arithmetic.
"""
from pathlib import Path
import csv
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

LEDGER = HERE / "WHOLE_STATE_LEDGER.tsv"


def closed_ids():
    with LEDGER.open(newline="") as f:
        return {int(r["state"]) for r in csv.DictReader(f, delimiter="\t")}


def bound_for(row):
    s = list(row["s"])
    rho = list(row["rho"])
    a, b = row["a"], row["b"]
    positives = [x for x in s if x > 0]
    if not positives:
        return None
    z = sum(x == 0 for x in s)
    h = min(positives)
    ell = sum(r < h for r in rho)
    if ell == 0:
        return None
    R = z + h - 1
    d = a - R - 2  # = a-z-h-1
    if d < 0:
        return None
    C = b * (b - 1) // 2
    num = ell * b * (R + 1) + d * C
    den = ell + d
    assert den > 0
    upper = num // den
    S = sum(s)
    return {
        "z": z,
        "h": h,
        "ell": ell,
        "R": R,
        "d": d,
        "S": S,
        "Q_upper": upper,
        "gap": upper - S,
        "excluded": S > upper,
    }


def main():
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    closed = closed_ids()
    active = [
        r for r in rows
        if r.get("combined_survives")
        and not (r["layer"] == "n34-m289" and r["state_id"] in closed)
    ]
    active.sort(key=lambda r: (r["layer"], r["state_id"]))
    assert len(active) == 3623, len(active)

    results = []
    for r in active:
        rec = bound_for(r)
        results.append({
            "layer": r["layer"],
            "state_id": r["state_id"],
            "a": r["a"], "b": r["b"], "t": r["t"],
            "bound": rec,
        })

    applicable = [r for r in results if r["bound"] is not None]
    excluded = [r for r in applicable if r["bound"]["excluded"]]
    survivors = [r for r in applicable if not r["bound"]["excluded"]]
    closest = sorted(survivors, key=lambda r: r["bound"]["gap"])[:100]

    summary = {
        "schema": "low-residual-reservoir-scan-v1",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "ledger_closed_count": len(closed),
        "current_frontier": len(active),
        "applicable": len(applicable),
        "not_applicable": len(active) - len(applicable),
        "excluded": len(excluded),
        "excluded_keys": [
            {
                "layer": r["layer"],
                "state_id": r["state_id"],
                **r["bound"],
            }
            for r in excluded
        ],
        "closest_survivors": [
            {
                "layer": r["layer"],
                "state_id": r["state_id"],
                **r["bound"],
            }
            for r in closest
        ],
        "proof_scope": (
            "excluded means the scalar base demand S already exceeds the explicit "
            "Q upper bound in LOW_RESIDUAL_RESERVOIR_BOUND.md; since every legal "
            "branch has Q>=S, this is a candidate whole-state exclusion under the "
            "canonical bridge and potential-pair theorem."
        ),
        "external_review": "OPEN",
    }
    (HERE / "LOW_RESIDUAL_RESERVOIR_SCAN.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
