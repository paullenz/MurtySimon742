#!/usr/bin/env python3
"""Exact standard-library verifier for the fresh forced-core/high-squeeze closure."""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

EXPECTED_SEED = 74220260919
EXPECTED_SOURCE_SHA = "f0e32e99a66d51027d1ad89d9f3874a8d50b3d4d215e8e1dd0d816786504dc2e"
EXPECTED_ROWS = [20, 91, 391, 490, 528, 562, 677]
R0 = 1


def best_partition(capacities, bins, target):
    best_min = -1
    best_sums = None
    feasible = False
    for assignment in itertools.product(range(bins + 1), repeat=len(capacities)):
        sums = [0] * bins
        for cap, bucket in zip(capacities, assignment):
            if bucket < bins:
                sums[bucket] += cap
        m = min(sums) if bins else 0
        if m > best_min:
            best_min = m
            best_sums = sums
        if m >= target:
            feasible = True
    return best_min, best_sums, feasible


def analyze_core(profile, r=R0):
    a, b = profile["a"], profile["b"]
    s, q, rho = profile["s"], profile["q"], profile["rho"]
    assert len(s) == a and len(q) == b and len(rho) == b

    core = [i for i, si in enumerate(s) if si <= r]
    h = len(core)
    forced = [u for u, (qu, ru) in enumerate(zip(q, rho)) if ru == r and qu == h]
    assert h >= 1 and forced

    # Exact incoming-capacity upper from the canonical bridge.
    capacity = [ru + b - a - 1 for ru in rho]

    # Deliberately relaxed destination superset.  For a forced source u,
    # S_u=A_r.  If (u,i) is routed to v then S_u\N_v={i} and S_v subset N_u.
    # Hence |S_v|<=h+r-1 and |N_v|>=h-1; another forced peer is impossible.
    candidates = [
        v for v in range(b)
        if v not in forced
        and q[v] <= h + r - 1
        and q[v] + rho[v] >= h - 1
        and capacity[v] > 0
    ]
    caps = [capacity[v] for v in candidates]
    required = h * len(forced)
    total = sum(caps)
    maxcap = max(caps) if caps else 0
    min_per_label = math.ceil(len(forced) / maxcap) if maxcap else None
    min_total = h * min_per_label if min_per_label is not None else None

    # The fresh remainder has at most six candidates, so full receiver-to-label
    # partition enumeration is tiny and provides an independent exact check.
    best_min, best_sums, feasible = best_partition(caps, h, len(forced))

    return {
        "row": profile["row"],
        "core_labels": core,
        "core_size": h,
        "forced_sources": forced,
        "forced_source_count": len(forced),
        "candidate_destinations": candidates,
        "capacity_multiset": caps,
        "candidate_capacity_total": total,
        "required_obligations": required,
        "total_capacity_deficit": total < required,
        "max_receiver_capacity": maxcap,
        "minimum_receivers_per_label": min_per_label,
        "minimum_receivers_total": min_total,
        "best_partition_min": best_min,
        "best_partition_sums": best_sums,
        "partition_feasible": feasible,
    }


def high_squeeze(profile, core):
    """Search the exact higher-demand squeeze once every candidate is forced used."""
    r = R0
    s, q, rho = profile["s"], profile["q"], profile["rho"]
    candidates = core["candidate_destinations"]
    assert core["minimum_receivers_total"] == len(candidates)
    assert all(core["max_receiver_capacity"] < core["forced_source_count"] for _ in [0])

    certificates = []
    for tau in range(r + 1, max(s) + 1):
        required = sum(si for si in s if si >= tau)
        raw = sum(qu for qu, ru in zip(q, rho) if ru >= tau)
        adjusted = raw
        adjustments = {}
        for v in candidates:
            if rho[v] >= tau:
                # A used receiver satisfies S_v subset A_r union R_u for at
                # least one forced source u.  |R_u|=r, so at most r selected
                # labels of v can lie outside A_r.  Every tau-heavy label lies
                # outside A_r because tau>r.
                allowed = min(q[v], r)
                loss = q[v] - allowed
                adjusted -= loss
                adjustments[str(v)] = {
                    "q": q[v],
                    "rho": rho[v],
                    "high_selected_upper": allowed,
                    "lost_high_slots": loss,
                }
        certificates.append({
            "threshold": tau,
            "required_high_selected": required,
            "raw_high_source_capacity": raw,
            "all_candidate_receivers_forced_used": True,
            "used_receivers": candidates,
            "high_eligible_used_receiver_adjustments": adjustments,
            "adjusted_high_selected_upper": adjusted,
            "deficit": required - adjusted,
            "rejected": adjusted < required,
        })
    rejects = [c for c in certificates if c["rejected"]]
    assert rejects
    return rejects[0]


def verify(data):
    assert data["schema"] == "fresh-shared-slack-reconnaissance-v1"
    assert data["seed"] == EXPECTED_SEED
    assert data["source_sha256"] == EXPECTED_SOURCE_SHA
    assert data["counts"]["profiles"] == 715
    assert data["counts"]["unrejected"] == 7

    by_row = {p["row"]: p for p in data["unrejected"]}
    assert sorted(by_row) == EXPECTED_ROWS
    profiles = {str(row): analyze_core(by_row[row]) for row in EXPECTED_ROWS}

    capacity_excluded = [
        row for row in EXPECTED_ROWS if profiles[str(row)]["total_capacity_deficit"]
    ]
    assert capacity_excluded == [20, 91, 391, 528, 562, 677]

    r490 = profiles["490"]
    assert r490["core_labels"] == [0, 1, 2]
    assert r490["forced_sources"] == [1, 4, 5, 11, 12, 13, 19, 21, 22, 26, 28]
    assert r490["candidate_destinations"] == [3, 7, 10, 17, 23, 27]
    assert r490["capacity_multiset"] == [8, 6, 6, 9, 8, 7]
    assert r490["partition_feasible"]
    assert r490["minimum_receivers_total"] == 6 == len(r490["candidate_destinations"])

    squeeze = high_squeeze(by_row[490], r490)
    assert squeeze["threshold"] == 3
    assert squeeze["required_high_selected"] == 45
    assert squeeze["raw_high_source_capacity"] == 46
    assert squeeze["adjusted_high_selected_upper"] == 43
    assert squeeze["deficit"] == 2

    # Do not retain a witness-style best partition in the frozen theorem surface;
    # only the exact best minimum is needed there.
    for rec in profiles.values():
        rec.pop("best_partition_sums")

    return {
        "schema": "fresh-forced-core-high-squeeze-v1",
        "scope": "fresh seed 74220260919, seven previously unrejected synthetic profiles; necessary canonical fixed-neighbourhood routing conditions only",
        "input": {
            "seed": EXPECTED_SEED,
            "embedded_source_sha256": EXPECTED_SOURCE_SHA,
            "previous_counts": {"profiles": 715, "unrejected": 7},
        },
        "r0": R0,
        "profiles": profiles,
        "capacity_deficit_exclusions": capacity_excluded,
        "row490_high_squeeze": squeeze,
        "newly_excluded": EXPECTED_ROWS,
        "fresh_sample": {"rejected": 715, "total": 715, "not_rejected": []},
        "original_sample": {"rejected": 713, "total": 713, "not_rejected": []},
        "canonical_finite_frontier": {
            "exclusions": 4626,
            "survivors": 952,
            "whole_state_closures": 3632,
            "changed": False,
        },
    }


def main():
    if not __debug__:
        raise SystemExit("Assertions disabled: do not run with -O")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, required=True)
    args = ap.parse_args()
    result = verify(json.loads(args.input.read_text()))
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
