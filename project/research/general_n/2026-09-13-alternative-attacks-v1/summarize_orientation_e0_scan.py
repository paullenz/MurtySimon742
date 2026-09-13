#!/usr/bin/env python3
"""Summarize exact E=0 frontier scanner TSV output."""
from pathlib import Path
import argparse
import csv
import hashlib
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--output", default="ORIENTATION_E0_SCAN_SUMMARY.json")
    args = ap.parse_args()
    path = Path(args.input)
    with path.open() as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    excluded = [r for r in rows if r["status"] == "E0_EXCLUDED"]
    survived = [r for r in rows if r["status"] == "SURVIVES_RELAXATION"]
    stages = {
        k: sum(int(r[k]) for r in rows)
        for k in ["incidence_fail", "cap_fail", "prefix_fail", "pair_fail", "target_fail"]
    }
    hardest = sorted(rows, key=lambda r: (float(r["seconds"]), int(r["profiles_tested"])), reverse=True)[:20]
    report = {
        "schema": "orientation-e0-scan-summary-v1",
        "input_tsv_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "states": len(rows),
        "e0_excluded": len(excluded),
        "survives_relaxation": len(survived),
        "e0_excluded_state_ids": [int(r["state_id"]) for r in excluded],
        "surviving_state_ids": [int(r["state_id"]) for r in survived],
        "stage_failure_profile_counts": stages,
        "profiles_tested": sum(int(r["profiles_tested"]) for r in rows),
        "total_reported_seconds": sum(float(r["seconds"]) for r in rows),
        "hardest_states": [
            {
                "state_id": int(r["state_id"]),
                "status": r["status"],
                "profiles_tested": int(r["profiles_tested"]),
                "seconds": float(r["seconds"]),
                "best_inc_def": int(r["best_inc_def"]),
                "best_pair_def": int(r["best_pair_def"]),
                "best_target_def": int(r["best_target_def"]),
            }
            for r in hardest
        ],
        "proof_scope": (
            "For a row marked E0_EXCLUDED, every q profile up to equal-rho permutation "
            "failed at least one exact necessary condition retained by the scanner, so only "
            "that state's x=s (E=0) layer is excluded. This is not a whole-state closure."
        ),
        "survival_scope": (
            "SURVIVES_RELAXATION means one q profile passed the retained necessary conditions; "
            "it does not assert graph feasibility."
        ),
        "external_review": "OPEN",
    }
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
