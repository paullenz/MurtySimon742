#!/usr/bin/env python3
"""Exact finite boundary verifier for A14_HIGH_B_SURPLUS_THEOREM.md.

New boundary scopes checked here:
  b=19,t=2 : 3 states, all exact shifted-potential exclusions
  b=20,t=1 : 29 states, 23 exact shifted-potential exclusions + 6 hand states
  b=21,t=1 : 3 states, all exact shifted-potential exclusions

The b=17 and b=18 boundary scopes are preserved separately in the N32/N33
packages and are cited by the theorem note. Floating LP is proposal only;
accepted exclusions are rechecked by the imported integer exactifier.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import csv
import json

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parents[1]
N33 = RESEARCH / "n33" / "2026-09-12-candidate-v1"
SOURCE = N33 / "n33_t2_shifted_potential_exact.py"
FRONTIER = N33 / "N33_T2_FRONTIER.csv"

spec = spec_from_file_location("n33shift", SOURCE)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot load {SOURCE}")
rx = module_from_spec(spec)
spec.loader.exec_module(rx)

A = 14

HAND20 = {
    ((3, 4) + (5,) * 12, (1,) * 8 + (3, 4) + (5,) * 10),
    ((3,) + (5,) * 13, (1,) * 8 + (3,) + (5,) * 11),
    ((4,) * 9 + (5,) * 5, (1,) * 8 + (2,) + (4,) * 6 + (5,) * 5),
    ((4, 4) + (5,) * 12, (1,) * 8 + (4, 4) + (5,) * 10),
    ((4,) + (5,) * 13, (1,) * 8 + (4,) + (5,) * 11),
    ((5,) * 14, (1,) * 7 + (2, 4) + (5,) * 11),
}


def pattern(b):
    """Same graph-level h cutoffs for every b; convert to v=b-h."""
    return {
        (2, 0): 4,
        (2, b - 11): 2,
        (2, b - 9): 1,
        (2, b - 7): 1,
        (2, b - 4): 1,
        (2, b - 3): 1,
        (3, b - 8): 1,
        (3, b - 6): 1,
        (3, b - 5): 1,
    }


def demand_rows():
    out = []
    with FRONTIER.open() as f:
        for row in csv.reader(f):
            if not row:
                continue
            z = list(map(int, row))
            out.append((z[0], tuple(z[1:])))
    assert len(out) == 21
    assert Counter(q for q, _ in out) == Counter({22: 18, 23: 3})
    return out


def rho_variants(rho0, increments):
    cur = {tuple(rho0)}
    for _ in range(increments):
        nxt = set()
        for rho in cur:
            for i, x in enumerate(rho):
                if x >= A:
                    continue
                y = list(rho)
                y[i] += 1
                y.sort()
                nxt.add(tuple(y))
        cur = nxt
    return cur


def states_for(b, t):
    rx.B = b
    threshold = b + 2 * t
    states = []
    for Q, s in demand_rows():
        if Q < threshold:
            continue
        rho0, closure_extra = rx.minimal_rho(s)
        available = Q - threshold - closure_extra
        assert available >= 0
        variants = set()
        for E in range(available + 1):
            variants |= rho_variants(rho0, E)
        for rho in sorted(variants):
            states.append((Q, s, rho))
    return states


def run_scope(b, t, hand):
    rx.B = b
    rx.PAT = pattern(b)
    states = states_for(b, t)
    exact = []
    hands = []
    failures = []

    for pos, (Q, s, rho) in enumerate(states):
        model = rx.build_envelope(s, rho)
        res = model[-1]
        key = (s, rho)
        if not res.success:
            if key in hand:
                hands.append((pos, Q, s, rho))
            else:
                failures.append((pos, Q, s, rho, "no-envelope"))
            continue
        cert = rx.exactify(model)
        if cert is None:
            failures.append((pos, Q, s, rho, "exactify-failed"))
        else:
            exact.append((pos, Q, s, rho, cert))

    assert {(s, rho) for _, _, s, rho in hands} == hand
    return {
        "b": b,
        "t": t,
        "states": len(states),
        "exact": len(exact),
        "hand": len(hands),
        "failures": len(failures),
        "denominators": dict(Counter(x[4]["denominator"] for x in exact)),
        "worst_gap": max((x[4]["gap_numerator"] for x in exact), default=None),
        "best_gap": min((x[4]["gap_numerator"] for x in exact), default=None),
    }, failures


def main():
    results = []
    all_failures = []

    for b, t, hand in [
        (19, 2, set()),
        (20, 1, HAND20),
        (21, 1, set()),
    ]:
        report, failures = run_scope(b, t, hand)
        results.append(report)
        all_failures.extend(failures)

    assert results[0]["states"] == 3 and results[0]["exact"] == 3
    assert results[1]["states"] == 29 and results[1]["exact"] == 23 and results[1]["hand"] == 6
    assert results[2]["states"] == 3 and results[2]["exact"] == 3
    assert not all_failures

    out = {
        "schema": "a14-high-b-boundary-exact-v1",
        "status": "PASS",
        "new_boundary_states": sum(r["states"] for r in results),
        "new_exact_potential_exclusions": sum(r["exact"] for r in results),
        "new_hand_states": sum(r["hand"] for r in results),
        "failures": 0,
        "scopes": results,
        "floating_point_is_proposal_only": True,
        "integer_arithmetic_is_acceptance": True,
        "interpretation": (
            "Together with the already preserved b=17 and b=18 scopes, these "
            "boundary checks complete the finite base cases in the a=14 high-b theorem."
        ),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
