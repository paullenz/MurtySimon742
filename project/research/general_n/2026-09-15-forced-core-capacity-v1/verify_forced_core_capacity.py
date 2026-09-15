#!/usr/bin/env python3
"""Exact verifier for the forced-core receiver-capacity partition obstruction."""
from __future__ import annotations
import argparse
import itertools
import json
from itertools import combinations
from pathlib import Path

SOURCE_SHA = "157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572"
ROWS = [160, 338]
R0 = 1


def best_partition(capacities, bins, target):
    """Assign each indivisible receiver capacity to one label bin or leave it unused."""
    best_min = -1
    best_sums = None
    for assignment in itertools.product(range(bins + 1), repeat=len(capacities)):
        sums = [0] * bins
        for cap, bucket in zip(capacities, assignment):
            if bucket < bins:
                sums[bucket] += cap
        m = min(sums) if bins else 0
        if m > best_min:
            best_min = m
            best_sums = sums
    return best_min, best_sums, best_min >= target


def tiny_challenge():
    """Exhaustively sanity-check the structural destination consequences on tiny set systems."""
    patterns = 0
    eligible_cases = 0
    for h in range(1, 4):
        universe = set(range(h + 2))
        core = set(range(h))
        source_neighbourhood = core | {h}
        for qv in range(h + 3):
            for Sv_t in combinations(universe, qv):
                Sv = set(Sv_t)
                remaining = universe - Sv
                for rhov in range(3):
                    if rhov > len(remaining):
                        continue
                    for Rv_t in combinations(remaining, rhov):
                        Rv = set(Rv_t)
                        Nv = Sv | Rv
                        patterns += 1
                        for i in core:
                            if core - Nv == {i} and Sv <= source_neighbourhood:
                                eligible_cases += 1
                                assert qv <= h
                                assert qv + rhov >= h - 1
                                assert Sv != core
    assert patterns == 290
    assert eligible_cases == 82
    return {"enumerated_cross_patterns": patterns, "eligible_obligation_cases": eligible_cases}


def analyze_profile(p):
    a, b = p["a"], p["b"]
    s, q, rho = p["s"], p["q"], p["rho"]
    assert len(s) == a and len(q) == b and len(rho) == b

    core = [i for i, si in enumerate(s) if si <= R0]
    h = len(core)
    forced = [u for u, (qu, ru) in enumerate(zip(q, rho)) if ru == R0 and qu == h]
    target = len(forced)

    # Necessary relaxed destination superset for an obligation from a forced-core source.
    capacity = [ru + b - a - 1 for ru in rho]
    candidates = [
        v for v in range(b)
        if v not in forced
        and q[v] <= h
        and q[v] + rho[v] >= h - 1
        and capacity[v] > 0
    ]
    caps = [capacity[v] for v in candidates]

    best_min, best_sums, feasible = best_partition(caps, h, target)
    return {
        "row": p["row"],
        "core_labels": core,
        "core_size": h,
        "forced_sources": forced,
        "forced_source_count": target,
        "candidate_destinations": candidates,
        "destination_capacities": {str(v): capacity[v] for v in candidates},
        "capacity_multiset": caps,
        "required_per_core_label": target,
        "best_achievable_min_label_capacity": best_min,
        "best_capacity_bin_sums": best_sums,
        "partition_feasible": feasible,
        "rejected": not feasible,
    }


def verify(data):
    assert data["source_sha256"] == SOURCE_SHA
    by_row = {p["row"]: p for p in data["rows"]}
    assert all(r in by_row for r in ROWS)

    profiles = {str(r): analyze_profile(by_row[r]) for r in ROWS}

    assert profiles["160"]["core_labels"] == [0, 1, 2]
    assert profiles["160"]["forced_sources"] == [0, 1, 2, 3, 13, 16, 17, 19, 25, 26]
    assert profiles["160"]["candidate_destinations"] == [4, 9, 10, 14, 15, 18, 22]
    assert profiles["160"]["capacity_multiset"] == [5, 5, 5, 4, 4, 4, 4]
    assert profiles["160"]["best_achievable_min_label_capacity"] == 9
    assert profiles["160"]["required_per_core_label"] == 10
    assert profiles["160"]["rejected"]

    assert profiles["338"]["core_labels"] == [0, 1]
    assert profiles["338"]["forced_sources"] == [6, 7, 9, 10, 11, 14, 15, 22, 26, 27]
    assert profiles["338"]["candidate_destinations"] == [0, 1, 3]
    assert profiles["338"]["capacity_multiset"] == [6, 6, 5]
    assert sum(profiles["338"]["capacity_multiset"]) == 17
    assert profiles["338"]["forced_source_count"] * profiles["338"]["core_size"] == 20
    assert profiles["338"]["best_achievable_min_label_capacity"] == 6
    assert profiles["338"]["rejected"]

    return {
        "schema": "forced-core-receiver-capacity-partition-v1",
        "scope": "original synthetic rows160 and338; necessary canonical selected/residual routing conditions only",
        "source_sha256": SOURCE_SHA,
        "r0": R0,
        "profiles": profiles,
        "newly_excluded": ROWS,
        "original_sample": {"rejected": 713, "total": 713, "not_rejected": []},
        "canonical_finite_frontier": {
            "exclusions": 4626,
            "survivors": 952,
            "whole_state_closures": 3632,
            "changed": False,
        },
        "tiny_challenge": tiny_challenge(),
    }


def main():
    if not __debug__:
        raise SystemExit("Assertions disabled: do not run with -O")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--remainder", type=Path, required=True)
    args = ap.parse_args()
    out = verify(json.loads(args.remainder.read_text()))
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
