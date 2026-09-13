#!/usr/bin/env python3
"""Prepare the broader N34 low-demand Hall/flow family.

This is transport/triage infrastructure only. It decodes the hash-verified
compatible-routing survivor catalogue, removes the nine quantified whole-state
closures now proved later, and expands the old adjacent-family filter by
removing only the ad hoc count limits on demand-two labels and rho-two sources.

No theorem is applied by this script.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

CLOSED = {227, 230, 279, 282, 382, 385, 519, 526, 588}


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


def in_family(r):
    return (
        r["layer"] == "n34-m289"
        and r["a"] == 15
        and r["b"] == 18
        and r["t"] == 1
        and len(r["s"]) == 15
        and len(r["rho"]) == 18
        and set(r["s"]) <= {2, 3}
        and set(r["rho"]) <= {1, 2, 3}
    )


def main():
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584

    closed_keys = {("n34-m289", x) for x in CLOSED}
    bykey = {key(r): r for r in combined}
    assert closed_keys <= set(bykey)

    family = [r for r in combined if in_family(r)]
    active = [r for r in family if key(r) not in closed_keys]

    profiles = defaultdict(list)
    for r in active:
        profiles[profile(r)].append(r["state_id"])

    profile_rows = []
    for p, ids in sorted(profiles.items()):
        profile_rows.append({
            "n2": p[0], "n3": p[1],
            "r1": p[2], "r2": p[3], "r3": p[4],
            "records": len(ids),
            "state_ids": sorted(ids),
        })

    # Rank profiles first by distance from the already-closed adjacent band,
    # then by number of records. This is triage only, not a proof score.
    def ring_distance(row):
        return max(0, row["n2"] - 4) + max(0, row["r2"] - 3)

    ranked = sorted(
        profile_rows,
        key=lambda z: (ring_distance(z), z["records"], z["n2"], z["r2"], z["r1"]),
    )
    for j, row in enumerate(ranked, 1):
        row["ring_rank"] = j
        row["distance_from_old_count_box"] = ring_distance(row)

    old_box_active = [
        r for r in active
        if r["s"].count(2) <= 4 and r["rho"].count(2) <= 3
    ]
    assert not old_box_active, (
        "The old adjacent-family count box should now be wholly closed; "
        f"unexpected active IDs: {[r['state_id'] for r in old_box_active]}"
    )

    report = {
        "schema": "low-demand-flow-family-v1",
        "source": "compatible-routing survivors.json (hash-verified decode)",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "frozen_survivors_before_whole_state_closures": len(combined),
        "closed_whole_states": sorted(CLOSED),
        "family_filter": {
            "layer": "n34-m289",
            "a": 15,
            "b": 18,
            "t": 1,
            "s_values": [2, 3],
            "rho_values": [1, 2, 3],
            "old_count_limits_removed": True,
        },
        "family_records_including_closed": len(family),
        "active_family_records": len(active),
        "active_state_ids": sorted(r["state_id"] for r in active),
        "distinct_active_profiles": len(profile_rows),
        "old_adjacent_count_box_active_records": len(old_box_active),
        "profiles_ranked_by_nearest_count_ring": ranked,
        "external_review": "OPEN",
        "note": "Triage only. No Hall/flow theorem has yet been applied to these active records.",
    }

    out = HERE / "LOW_DEMAND_FLOW_FAMILY_INPUT.json"
    out.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n")

    # Also produce a compact exact input for subsequent integer scanners.
    inp = HERE / "low_demand_flow_family_input.txt"
    lines = [str(len(active))]
    for r in sorted(active, key=lambda x: x["state_id"]):
        vals = [
            r["state_id"], r["a"], r["b"], r["t"],
            len(r["s"]), *r["s"],
            len(r["rho"]), *r["rho"],
        ]
        lines.append(" ".join(map(str, vals)))
    inp.write_text("\n".join(lines) + "\n")

    print(json.dumps(report, indent=2, sort_keys=False))
    print("INPUT_SHA256", hashlib.sha256(inp.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
