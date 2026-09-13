#!/usr/bin/env python3
"""Summarize the canonical 4,568-state frontier for orientation-flow rescanning.

Transport/triage only: this script applies no new theorem. It hash-verifies and
decodes the frozen compatible-routing survivor stream, removes the 16 canonical
whole-state closures, and records the structural distribution needed to size
later exact q/flow enumeration.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

CLOSED_N34 = {227, 279, 588, 526, 382, 519, 230, 282, 385, 153, 122, 283, 154, 231, 77, 60}


def main():
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    combined = [r for r in rows if r["combined_survives"]]
    assert len(combined) == 4584

    active = [
        r for r in combined
        if not (r["layer"] == "n34-m289" and r["state_id"] in CLOSED_N34)
    ]
    assert len(active) == 4568

    layers = Counter(r["layer"] for r in active)
    assert layers == Counter({"n34-m289": 4490, "n35-m306": 78})

    rho_profiles = Counter(tuple(r["rho"]) for r in active)
    s_profiles = Counter(tuple(r["s"]) for r in active)
    joint_profiles = Counter((tuple(r["s"]), tuple(r["rho"])) for r in active)

    max_s = Counter(max(r["s"]) for r in active)
    max_rho = Counter(max(r["rho"]) for r in active)
    distinct_rho = Counter(len(set(r["rho"])) for r in active)
    distinct_s = Counter(len(set(r["s"])) for r in active)

    def quantiles(vals):
        vals = sorted(vals)
        def q(p):
            if not vals:
                return None
            return vals[round((len(vals) - 1) * p)]
        return {"min": vals[0], "q25": q(.25), "median": q(.5), "q75": q(.75), "max": vals[-1]}

    Svals = [sum(r["s"]) for r in active]
    rvals = [sum(r["rho"]) for r in active]

    low23 = [
        r for r in active
        if set(r["s"]) <= {2, 3} and set(r["rho"]) <= {1, 2, 3}
    ]
    positive_all = [r for r in active if min(r["s"]) > 0]

    # At E=0 a source of residual degree rho can use only labels with s<=rho.
    # Record a cheap source-cap profile count without claiming feasibility.
    exact_demand_signature = Counter()
    for r in active:
        sc = Counter(r["s"])
        rc = Counter(r["rho"])
        sig = tuple(
            (rho, cnt, sum(1 for s in r["s"] if 0 < s <= rho))
            for rho, cnt in sorted(rc.items())
        )
        exact_demand_signature[(r["layer"], sig, sum(r["s"]))] += 1

    report = {
        "schema": "orientation-frontier-summary-v1",
        "source": "compatible-routing survivors.json (hash-verified decode)",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "pre_whole_state_survivors": len(combined),
        "canonical_closed_n34": sorted(CLOSED_N34),
        "active_survivors": len(active),
        "layers": dict(sorted(layers.items())),
        "unique_rho_profiles": len(rho_profiles),
        "unique_s_profiles": len(s_profiles),
        "unique_joint_s_rho_profiles": len(joint_profiles),
        "unique_exact_demand_signatures": len(exact_demand_signature),
        "max_s_histogram": {str(k): v for k, v in sorted(max_s.items())},
        "max_rho_histogram": {str(k): v for k, v in sorted(max_rho.items())},
        "distinct_s_values_histogram": {str(k): v for k, v in sorted(distinct_s.items())},
        "distinct_rho_values_histogram": {str(k): v for k, v in sorted(distinct_rho.items())},
        "sum_s": quantiles(Svals),
        "sum_rho": quantiles(rvals),
        "all_positive_demand": len(positive_all),
        "low_23_family": len(low23),
        "top_rho_profiles": [
            {"rho": list(k), "records": v} for k, v in rho_profiles.most_common(20)
        ],
        "top_s_profiles": [
            {"s": list(k), "records": v} for k, v in s_profiles.most_common(20)
        ],
        "note": "Triage only; no orientation-flow exclusion is claimed by this summary.",
        "external_review": "OPEN",
    }

    out = HERE / "ORIENTATION_FRONTIER_SUMMARY.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
