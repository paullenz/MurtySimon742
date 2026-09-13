#!/usr/bin/env python3
"""Summarize targeted excess-budget orientation scan TSV."""
from pathlib import Path
import argparse
import csv
import hashlib
import json
from collections import defaultdict, Counter


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--output", default="EXCESS_BUDGET_ORIENTATION_SUMMARY.json")
    args = ap.parse_args()
    p = Path(args.input)
    with p.open() as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    by = defaultdict(list)
    for r in rows:
        by[(int(r["layer"]), int(r["state_id"]))].append(r)

    states = []
    for (layer, sid), rr in sorted(by.items()):
        excluded = [r for r in rr if r["status"] == "LAYER_EXCLUDED"]
        survived = [r for r in rr if r["status"] == "SURVIVES_RELAXATION"]
        stages = {
            k: sum(int(r[k]) for r in rr)
            for k in [
                "incidence_fail", "cap_fail", "prefix_fail", "cheap_cost_fail",
                "pair_fail", "target_fail", "cost_fail",
            ]
        }
        states.append({
            "layer": layer,
            "state_id": sid,
            "layers_scanned": len(rr),
            "excluded_E": [int(r["E"]) for r in excluded],
            "surviving_E": [int(r["E"]) for r in survived],
            "whole_state_excluded_by_relaxation": len(survived) == 0,
            "profiles_tested": sum(int(r["profiles_tested"]) for r in rr),
            "stage_failure_profile_counts": stages,
            "total_reported_seconds": sum(float(r["seconds"]) for r in rr),
            "surviving_witnesses": [
                {
                    "E": int(r["E"]),
                    "Q": int(r["Q"]),
                    "envelope": int(r["envelope"]),
                    "witness_cost": int(r["witness_cost"]),
                    "rho": r["witness_rho"],
                    "q": r["witness_q"],
                }
                for r in survived
            ],
        })

    report = {
        "schema": "excess-budget-orientation-summary-v1",
        "input_tsv_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "rows": len(rows),
        "states": states,
        "whole_state_excluded_count": sum(s["whole_state_excluded_by_relaxation"] for s in states),
        "surviving_excess_histogram": dict(sorted(Counter(
            e for s in states for e in s["surviving_E"]
        ).items())),
        "proof_scope": (
            "A LAYER_EXCLUDED row means every equal-rho-symmetry q profile for that E "
            "failed at least one retained exact necessary condition. A state is a candidate "
            "whole-scalar closure only if every admissible E row is excluded; independent "
            "replay is still required before updating the canonical closure ledger."
        ),
        "external_review": "OPEN",
    }
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
