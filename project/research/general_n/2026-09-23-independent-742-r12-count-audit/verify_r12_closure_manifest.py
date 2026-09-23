#!/usr/bin/env python3
"""Verify the saved-count and helper-screen manifest behind r=12 promotion."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "2026-09-22-r12-quotient-v1"
NEW = HERE.parent / "2026-09-22-independent-742-r12-quotient"


def load(path):
    return json.loads(path.read_text())


def subset_digest(path, cases):
    rows = [line for line in path.read_text().splitlines()
            if int(line.split()[0]) in cases]
    return hashlib.sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def source_count(path, field="feasible_rows"):
    return len(load(path)[field])


def main():
    le5 = load(OLD / "r12_support_le5.json")
    assert sum(row["source_feasible"] for row in le5.values()) == 0
    support6 = load(OLD / "r12_support6.json")
    count6 = sum(len(row["feasible"]) for row in support6.values())
    count7 = len(load(OLD / "r12_support7_sources.json")["rows"])
    assert subset_digest(OLD / "r12_support8_masks.txt", {0, 1}) == subset_digest(
        NEW / "r12_support8_masks.txt", {0, 1})
    count8 = sum(source_count(path) for path in [
        OLD / "r12_support8_sources_case0.json",
        OLD / "r12_support8_sources_case1.json",
        NEW / "r12_support8_sources_case2.json",
        NEW / "r12_support8_sources_case3.json",
        NEW / "r12_support8_sources_case4.json",
    ])
    count9 = sum(source_count(path) for path in [
        NEW / "r12_support9_sources_case0.json",
        NEW / "r12_support9_sources_case1.json",
        *(NEW / f"r12_support9_sources_case2_chunk{i}.json" for i in range(4)),
    ])
    count10 = source_count(NEW / "r12_support10_case0_sources.json") + sum(
        source_count(NEW / f"r12_support10_case1_source_chunk{i}.json")
        for i in range(8))
    counts = {6: count6, 7: count7, 8: count8, 9: count9, 10: count10}
    assert counts == {6: 3, 7: 2, 8: 8, 9: 36, 10: 32}
    helper67 = load(HERE / "R12_SUPPORT67_HELPER_AUDIT_RESULT.json")
    helper89 = load(HERE / "R12_SUPPORT89_HELPER_AUDIT_RESULT.json")
    helper10 = load(HERE / "R12_SUPPORT10_HELPER_SCREEN_RESULT.json")["helper_screen"]
    assert (helper67["feasible"], helper67["infeasible"], helper67["unknown"]) == (0, 5, 0)
    assert (helper89["feasible"], helper89["infeasible"], helper89["unknown"]) == (0, 44, 0)
    assert (helper10["feasible"], helper10["infeasible"], helper10["unknown"]) == (0, 32, 0)
    report = {
        "status": "PASS",
        "source_survivors_by_support": counts,
        "source_survivors_total": sum(counts.values()),
        "helper_feasible": 0,
        "helper_infeasible": 81,
        "helper_unknown": 0,
        "support8_cases01_subset_sha256": subset_digest(
            NEW / "r12_support8_masks.txt", {0, 1}),
        "logical_consequence": "internal strict closure through r=12; edge bound through S<=14",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
