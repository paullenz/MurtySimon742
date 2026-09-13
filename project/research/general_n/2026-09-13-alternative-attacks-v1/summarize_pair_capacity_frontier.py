#!/usr/bin/env python3
"""Summarize canonical pair-capacity frontier scan output."""
from pathlib import Path
import argparse
import csv
import hashlib
import json
from collections import Counter


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--output", default="PAIR_CAPACITY_FRONTIER_SUMMARY.json")
    args = ap.parse_args()
    path = Path(args.input)
    with path.open() as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    excluded = [r for r in rows if r["status"] == "PAIR_CAPACITY_EXCLUDED"]
    survived = [r for r in rows if r["status"] == "SURVIVES_PAIR_CAPACITY"]
    excluded.sort(key=lambda r: (int(r["layer"]), int(r["state_id"])))

    layer_counts = Counter(int(r["layer"]) for r in rows)
    excluded_layers = Counter(int(r["layer"]) for r in excluded)
    witness_e = Counter(int(r["witness_E"]) for r in survived)

    hardest = sorted(
        rows,
        key=lambda r: (float(r["seconds"]), int(r["profiles_tested"])),
        reverse=True,
    )[:50]
    closest_excluded = sorted(
        excluded,
        key=lambda r: int(r["best_pair_margin"]),
        reverse=True,
    )[:100]

    report = {
        "schema": "pair-capacity-frontier-summary-v1",
        "input_tsv_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "states": len(rows),
        "input_layer_counts": {str(k): v for k, v in sorted(layer_counts.items())},
        "pair_capacity_excluded": len(excluded),
        "survives_pair_capacity": len(survived),
        "excluded_by_layer": {str(k): v for k, v in sorted(excluded_layers.items())},
        "excluded_keys": [
            {
                "layer": int(r["layer"]),
                "state_id": int(r["state_id"]),
                "S": int(r["S"]),
                "Emax": int(r["Emax"]),
                "profiles_tested": int(r["profiles_tested"]),
                "pre_pair_passes": int(r["pre_pair_passes"]),
                "best_pre_margin": int(r["best_pre_margin"]),
                "best_pair_margin": int(r["best_pair_margin"]),
                "seconds": float(r["seconds"]),
            }
            for r in excluded
        ],
        "survivor_witness_E_histogram": {
            str(k): v for k, v in sorted(witness_e.items())
        },
        "profiles_tested": sum(int(r["profiles_tested"]) for r in rows),
        "total_reported_seconds": sum(float(r["seconds"]) for r in rows),
        "closest_excluded": [
            {
                "layer": int(r["layer"]),
                "state_id": int(r["state_id"]),
                "best_pair_margin": int(r["best_pair_margin"]),
                "best_pre_margin": int(r["best_pre_margin"]),
                "profiles_tested": int(r["profiles_tested"]),
            }
            for r in closest_excluded
        ],
        "hardest_states": [
            {
                "layer": int(r["layer"]),
                "state_id": int(r["state_id"]),
                "status": r["status"],
                "profiles_tested": int(r["profiles_tested"]),
                "seconds": float(r["seconds"]),
                "witness_E": int(r["witness_E"]),
            }
            for r in hardest
        ],
        "proof_scope": (
            "PAIR_CAPACITY_EXCLUDED means every q multiset in the deliberately enlarged "
            "universe defined by the universal source-degree bounds fails the combined "
            "incoming and potential-pair degree capacities at every admissible total excess E. "
            "Each such row is therefore a candidate whole-scalar-state exclusion under the "
            "canonical bridge lemmas, pending independent replay before ledger promotion."
        ),
        "survival_scope": (
            "SURVIVES_PAIR_CAPACITY means one enlarged-universe q profile passes this cheap "
            "relaxation. It does not assert selected-incidence feasibility or graph feasibility."
        ),
        "external_review": "OPEN",
    }
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
