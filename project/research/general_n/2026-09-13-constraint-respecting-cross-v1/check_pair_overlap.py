#!/usr/bin/env python3
"""Exact standard-library replay of pair-trace and residual-cover tests.

Input selected patterns come from FULL_DOMAIN_SPILL_EXACT.json.  The checker:
1. evaluates the raw k=2 co-singleton moment;
2. deterministically repairs every failing selected pattern by degree-preserving
   two-source/two-label switches, without changing q or x=s;
3. verifies k=2,3,4 global moments on the repaired patterns;
4. evaluates the exact local residual-cover inequality (PAIR_OVERLAP.md, (6)).

A failure of the local residual-cover inequality excludes only that fixed
selected-set realization.  No whole-state exclusion is inferred here.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import math
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import records  # noqa: E402


def pool():
    return {(r["layer"], r["state_id"]): r for r in records("pool_inputs.jsonl")}


def selected_degrees(S, a):
    return [sum(i in S[u] for u in range(len(S))) for i in range(a)]


def moment(rec, S, k):
    q = list(map(len, S)); M = {}
    for u, Su in enumerate(S):
        value = q[u] - k + 1
        if value <= 0:
            continue
        for T in combinations(sorted(Su), k):
            if value > M.get(T, 0):
                M[T] = value
    lower = sum(M.values())
    capacity = sum(math.comb(q[u] + rec["rho"][u], k) for u in range(rec["b"]))
    return capacity - lower, lower, capacity


def greedy_pair_repair(rec, S):
    """Greedily maximise the k=2 moment slack using exact degree-preserving switches."""
    S = [set(x) for x in S]
    q0 = list(map(len, S)); x0 = selected_degrees(S, rec["a"])
    assert x0 == rec["s"]
    switches = []
    current = moment(rec, S, 2)[0]
    while current < 0:
        best_slack = current
        best_move = None
        for u in range(rec["b"]):
            for v in range(u + 1, rec["b"]):
                A = sorted(S[u] - S[v])
                B = sorted(S[v] - S[u])
                for i in A:
                    for j in B:
                        if rec["rho"][u] < rec["s"][j]:
                            continue
                        if rec["rho"][v] < rec["s"][i]:
                            continue
                        S[u].remove(i); S[u].add(j)
                        S[v].remove(j); S[v].add(i)
                        slack = moment(rec, S, 2)[0]
                        S[u].remove(j); S[u].add(i)
                        S[v].remove(i); S[v].add(j)
                        if slack > best_slack:
                            best_slack = slack
                            best_move = (u, v, i, j)
        if best_move is None:
            break
        u, v, i, j = best_move
        S[u].remove(i); S[u].add(j)
        S[v].remove(j); S[v].add(i)
        switches.append([u, v, i, j])
        current = best_slack
        if len(switches) > 50:
            raise AssertionError("unexpected repair length")
    assert list(map(len, S)) == q0
    assert selected_degrees(S, rec["a"]) == x0 == rec["s"]
    assert all(all(rec["rho"][u] >= rec["s"][i] for i in S[u]) for u in range(rec["b"]))
    return S, current, switches


def deficit_graph(rec, S):
    q = list(map(len, S)); M = {}; selected_pairs = Counter()
    for u, Su in enumerate(S):
        value = q[u] - 1
        for e in combinations(sorted(Su), 2):
            selected_pairs[e] += 1
            if value > M.get(e, 0):
                M[e] = value
    return {
        e: max(0, M[e] - selected_pairs[e])
        for e in M
        if M[e] > selected_pairs[e]
    }


def local_cover_max(rec, Su, rho, positive_edges):
    complement = [i for i in range(rec["a"]) if i not in Su]
    best = -1
    for Rt in combinations(complement, rho):
        R = set(Rt); N = Su | R
        covered = 0
        for i, j in positive_edges:
            if i in N and j in N and not (i in Su and j in Su):
                covered += 1
        if covered > best:
            best = covered
    return best


def residual_cover(rec, S):
    D = deficit_graph(rec, S)
    need = sum(D.values())
    positive_edges = list(D)
    caps = [
        local_cover_max(rec, set(S[u]), rec["rho"][u], positive_edges)
        for u in range(rec["b"])
    ]
    capacity = sum(caps)
    return capacity - need, need, capacity, len(D), caps


def main():
    P = pool()
    full = json.loads((HERE / "FULL_DOMAIN_SPILL_EXACT.json").read_text())
    assert full["summary"]["witnessed"] == 4584
    assert full["summary"]["all_exact_demand"] is True

    raw_pair_failures = []
    repairs = []
    repaired = {}
    moment_min = {2: None, 3: None, 4: None}

    for w in full["witnesses"]:
        key = (w["layer"], w["state_id"]); rec = P[key]
        S = [set(x) for x in w["selected"]]
        assert selected_degrees(S, rec["a"]) == rec["s"]
        before = moment(rec, S, 2)[0]
        if before < 0:
            raw_pair_failures.append({"layer": key[0], "state_id": key[1], "slack": before})
            S, after, switches = greedy_pair_repair(rec, S)
            assert after >= 0
            repairs.append({
                "layer": key[0], "state_id": key[1],
                "before_slack": before, "after_slack": after,
                "switches": switches,
            })
        repaired[key] = S
        for k in (2, 3, 4):
            slack = moment(rec, S, k)[0]
            assert slack >= 0
            moment_min[k] = slack if moment_min[k] is None else min(moment_min[k], slack)

    assert len(raw_pair_failures) == 23
    assert len(repairs) == 23
    assert max(len(r["switches"]) for r in repairs) <= 3
    assert moment_min == {2: 0, 3: 195, 4: 191}

    local_failures = []
    min_local = None
    for index, (key, S) in enumerate(repaired.items()):
        rec = P[key]
        slack, need, capacity, edge_count, _ = residual_cover(rec, S)
        min_local = slack if min_local is None else min(min_local, slack)
        if slack < 0:
            local_failures.append({
                "layer": key[0], "state_id": key[1],
                "slack": slack, "demand_units": need,
                "local_capacity": capacity, "deficit_edge_count": edge_count,
            })
        if (index + 1) % 500 == 0:
            print(f"checked {index+1}/4584 local-cover patterns", flush=True)

    assert len(local_failures) == 26
    assert min_local == -87

    out = {
        "schema": "pair-overlap-check-v1",
        "date": "2026-09-13",
        "input_patterns": 4584,
        "raw_pair_moment_failures": len(raw_pair_failures),
        "raw_pair_failures": raw_pair_failures,
        "pair_repairs": repairs,
        "all_pair_moments_repaired": True,
        "maximum_repair_switches": max(len(r["switches"]) for r in repairs),
        "minimum_repaired_moment_slack": {str(k): moment_min[k] for k in (2,3,4)},
        "local_residual_cover_failures_on_frozen_repaired_patterns": len(local_failures),
        "minimum_local_residual_cover_slack": min_local,
        "local_residual_cover_failures": local_failures,
        "whole_state_exclusions_claimed": 0,
        "scope": (
            "Pair-moment repairs are direct positive selected-set witnesses and show zero "
            "whole-state exclusions from the raw k=2 moment on this study. Local residual-cover "
            "failures exclude only the listed fixed selected-set realizations; alternative "
            "selected-set geometries are not quantified here."
        ),
    }
    (HERE / "PAIR_OVERLAP_CHECK.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS", "raw_pair_failures": len(raw_pair_failures),
        "pair_repairs": len(repairs), "local_pattern_failures": len(local_failures),
        "min_local_slack": min_local,
    }, indent=2))


if __name__ == "__main__":
    main()
