#!/usr/bin/env python3
from pathlib import Path
import argparse
import csv
import hashlib
import json

FIELDS = [
    "layer", "state_id", "S", "Emax", "profiles_tested",
    "paircap_fail", "paircap_pass", "incidence_fail", "incidence_pass",
    "pairhall_fail", "pairhall_pass", "targethall_fail", "targethall_pass",
    "cost_fail", "status", "witness_E", "witness_cost", "witness_envelope",
]


def rows(path):
    with Path(path).open(newline="") as f:
        out = list(csv.DictReader(f, delimiter="\t"))
    if not out:
        raise SystemExit("empty scan output: " + path)
    return {r["state_id"]: r for r in out}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("primary")
    ap.add_argument("independent")
    ap.add_argument("--output", default="POST_PAIR_RELATIONAL_COMPARE.json")
    args = ap.parse_args()

    a = rows(args.primary)
    b = rows(args.independent)
    if set(a) != set(b):
        raise SystemExit("state sets differ")

    differences = []
    for state in sorted(a, key=int):
        for field in FIELDS:
            if a[state][field] != b[state][field]:
                differences.append({
                    "state_id": int(state),
                    "field": field,
                    "primary": a[state][field],
                    "independent": b[state][field],
                })
        if a[state]["status"] != "RELATIONAL_EXCLUDED":
            differences.append({
                "state_id": int(state),
                "field": "required_status",
                "primary": a[state]["status"],
                "independent": b[state]["status"],
            })

    report = {
        "schema": "post-pair-relational-compare-v1",
        "primary_sha256": digest(args.primary),
        "independent_sha256": digest(args.independent),
        "state_ids": [int(x) for x in sorted(a, key=int)],
        "exact_fields": FIELDS,
        "difference_count": len(differences),
        "differences": differences,
        "result": "PASS" if not differences else "FAIL",
        "external_review": "OPEN",
    }
    Path(args.output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    if differences:
        raise SystemExit("relational implementations disagree")


if __name__ == "__main__":
    main()
