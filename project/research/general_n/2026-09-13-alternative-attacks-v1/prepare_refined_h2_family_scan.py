#!/usr/bin/env python3
"""Prepare an exact, hash-verified input for the adjacent refined-h2 family scan.

This is transport/triage infrastructure only.  It reconstructs the frozen
4,584-survivor catalogue from the compatible-routing evidence, marks the five
whole-state closures already proved later, and selects a deliberately narrow
N34 family structurally adjacent to those examples.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

CLOSED = {227, 279, 382, 526, 588}


def key(r):
    return (r["layer"], r["state_id"])


def profile(r):
    return (
        r["s"].count(2),
        r["s"].count(3),
        r["rho"].count(1),
        r["rho"].count(2),
        r["rho"].count(3),
    )


def in_adjacent_family(r):
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

    closed_keys = {("n34-m289", x) for x in CLOSED}
    bykey = {key(r): r for r in combined}
    assert closed_keys <= set(bykey)
    active = [r for r in combined if key(r) not in closed_keys]
    assert len(active) == 4579

    family = [r for r in combined if in_adjacent_family(r)]
    active_family = [r for r in family if key(r) not in closed_keys]
    assert all(x in {key(r) for r in family} for x in closed_keys)

    out = HERE / "refined_h2_family_input.txt"
    lines = [str(len(family))]
    for r in sorted(family, key=lambda x: x["state_id"]):
        vals = [
            r["state_id"],
            1 if r["state_id"] in CLOSED else 0,
            r["a"], r["b"], r["t"],
            len(r["s"]), *r["s"],
            len(r["rho"]), *r["rho"],
        ]
        lines.append(" ".join(map(str, vals)))
    out.write_text("\n".join(lines) + "\n")

    profiles = Counter(profile(r) for r in family)
    report = {
        "schema": "refined-h2-adjacent-family-input-v1",
        "source": "compatible-routing survivors.json (hash-verified decode)",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "frozen_survivors_before_whole_state_closures": len(combined),
        "closed_whole_states": sorted(CLOSED),
        "active_survivors": len(active),
        "family_filter": {
            "layer": "n34-m289",
            "a": 15,
            "b": 18,
            "t": 1,
            "s_values": [2, 3],
            "max_demand_two_labels": 4,
            "rho_values": [1, 2, 3],
            "max_rho_two_sources": 3,
        },
        "family_records_including_regressions": len(family),
        "active_family_records": len(active_family),
        "distinct_profiles": len(profiles),
        "profiles": [
            {
                "n2": p[0], "n3": p[1], "r1": p[2], "r2": p[3], "r3": p[4],
                "records": c,
            }
            for p, c in sorted(profiles.items())
        ],
        "input_sha256": hashlib.sha256(out.read_bytes()).hexdigest(),
        "external_review": "OPEN",
    }
    (HERE / "REFINED_H2_FAMILY_INPUT.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
