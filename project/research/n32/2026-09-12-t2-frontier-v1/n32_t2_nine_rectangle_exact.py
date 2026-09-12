#!/usr/bin/env python3
"""Exactify the common nine-rectangle potential for N32, Delta=17, m=257.

The floating solve proposes only the profile-specific envelope coefficients.
Acceptance is integer arithmetic: every homogeneous row must be <=0, every
contradiction row must be strictly negative, and every bound/pin must hold.

The global potential is fixed by hand at

  4 B(2,0) + 2 B(2,6)
  + B(2,8)+B(2,10)+B(2,13)+B(2,14)
  + B(3,9)+B(3,11)+B(3,12).

The script reads the committed 71-profile score frontier, expands every allowed
positive-demand residual-tail slack state, and checks all 154 states at once.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse
import csv
import hashlib
import json

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parents[1]
RD_PATH = RESEARCH / "general_n" / "2026-09-09-rx-hall-v1" / "n29_t2_rectdiag_sparse_scan.py"
spec = spec_from_file_location("rd", RD_PATH)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot load {RD_PATH}")
rd = module_from_spec(spec)
spec.loader.exec_module(rd)

A = 14
B = 17
DMAX = 12
PAT = {
    (2, 0): 4,
    (2, 6): 2,
    (2, 8): 1,
    (2, 10): 1,
    (2, 13): 1,
    (2, 14): 1,
    (3, 9): 1,
    (3, 11): 1,
    (3, 12): 1,
}


def C(h, z):
    return (z * (z - 1) + h * (h + 1)) // 2


def gamma(h, W):
    if W <= 0:
        return 0
    z = h
    while W > C(h, z):
        z += 1
    return z


def minimal_rho(s):
    z = {1: B, A: 0}
    for h in range(2, A):
        vals = [x for x in s if x >= h]
        z[h] = gamma(h, sum(vals)) if vals else 0
    out = []
    for k in range(1, A):
        out.extend([k] * (z[k] - z[k + 1]))
    assert len(out) == B
    return tuple(out)


def rho_variants(rho0, E):
    cur = {tuple(rho0)}
    for _ in range(E):
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
    return sorted(cur)


def load_states(frontier):
    profiles = []
    with frontier.open() as f:
        for row in csv.reader(f):
            if not row:
                continue
            q = int(row[0])
            s = tuple(map(int, row[1:]))
            assert len(s) == A and 21 <= q <= 23
            profiles.append((q, s))
    assert len(profiles) == 71
    assert Counter(q for q, _ in profiles) == Counter({21: 50, 22: 18, 23: 3})

    states = []
    zero = []
    for q, s in profiles:
        if min(s) == 0:
            zero.append((q, s))
            continue
        r0 = minimal_rho(s)
        for E in range(q - 21 + 1):
            for rho in rho_variants(r0, E):
                states.append({"s": list(s), "rho": list(rho), "Q": q, "E": E})
    assert len(zero) == 1 and zero[0][1] == (0,) + (3,) * 13
    assert len(states) == 154
    return profiles, zero, states


def exact_attempt(M, res, denom, pinned, expected_margins):
    X = [int(round(float(v) * denom)) for v in res.x]
    for j, val in pinned.items():
        X[j] = int(val * denom)

    # One-sided repair: ell/sigma occur with coefficient +1 in their local
    # envelope rows. Lowering them cannot damage a previously satisfied row.
    repairs = {}
    for i, (row, rhs) in enumerate(zip(M.rows, M.rhs)):
        if rhs != 0:
            continue
        lhs = sum(int(c) * X[j] for j, c in row.items())
        if lhs <= 0:
            continue
        cand = [
            j for j, c in row.items()
            if c == 1 and isinstance(M.names[j], tuple)
            and M.names[j][0] in ("ell", "sig")
        ]
        if len(cand) != 1:
            return None, {"repair_failure": [i, lhs, [str(M.names[j]) for j in cand]]}
        j = cand[0]
        repairs[j] = max(repairs.get(j, 0), lhs)
    for j, d in repairs.items():
        X[j] -= d

    zero_viol = []
    margins = []
    bound_viol = []
    zero_max = None
    for i, (row, rhs) in enumerate(zip(M.rows, M.rhs)):
        lhs = sum(int(c) * X[j] for j, c in row.items())
        if rhs == 0:
            zero_max = lhs if zero_max is None else max(zero_max, lhs)
            if lhs > 0:
                zero_viol.append([i, lhs])
        else:
            margins.append([i, lhs])

    for j, (lo, hi) in enumerate(M.bounds):
        if j in pinned:
            target = int(pinned[j] * denom)
            if X[j] != target:
                bound_viol.append([j, "pin", X[j], target])
            continue
        if lo is not None and X[j] < int(round(lo * denom)):
            bound_viol.append([j, "lo", X[j], int(round(lo * denom))])
        if hi is not None and X[j] > int(round(hi * denom)):
            bound_viol.append([j, "hi", X[j], int(round(hi * denom))])

    nonnegative = [x for x in margins if x[1] >= 0]
    ok = (
        not zero_viol
        and not bound_viol
        and len(margins) == expected_margins
        and not nonnegative
    )
    meta = {
        "repair_count": len(repairs),
        "repair_total": sum(repairs.values()),
        "repair_max": max(repairs.values()) if repairs else 0,
        "zero_rhs_max_lhs": zero_max,
        "zero_row_violation_count": len(zero_viol),
        "bound_violation_count": len(bound_viol),
        "margin_count": len(margins),
        "nonnegative_margin_count": len(nonnegative),
        "worst_margin_numerator": max((x[1] for x in margins), default=None),
    }
    return (X if ok else None), meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frontier", type=Path, default=HERE / "N32_T2_FRONTIER.csv")
    ap.add_argument("--output", type=Path, required=True)
    z = ap.parse_args()

    profiles, zero, states = load_states(z.frontier)
    P = [{"s": x["s"], "rho": x["rho"]} for x in states]

    # Build the established rectangle-potential finite system with no diagonal
    # correction. Pin every rectangle not in PAT to zero.
    M, rect, diag = rd.build(P, A, B, DMAX, False)
    assert diag is None
    pinned = {}
    for D, V, w in rect:
        val = PAT.get((D, V), 0)
        M.bounds[w] = (val, val)
        pinned[w] = val

    res = M.solve()
    if not res.success:
        raise SystemExit(f"fixed nine-rectangle potential is not numerically feasible: {res.message}")

    accepted = None
    attempts = []
    for denom in (10**5, 10**6, 10**7, 10**8):
        X, meta = exact_attempt(M, res, denom, pinned, len(states))
        attempts.append({"denominator_scale": denom, **meta})
        if X is not None:
            accepted = (denom, X, meta)
            break
    if accepted is None:
        raise SystemExit("no exact integer acceptance")

    denom, X, meta = accepted
    nums = {str(name): int(X[i]) for i, name in enumerate(M.names)}
    raw_nums = (json.dumps(nums, separators=(",", ":"), sort_keys=True) + "\n").encode()
    out = {
        "schema": "n32-t2-nine-rectangle-exact-v1",
        "status": "PASS",
        "scope": {"n": 32, "a": A, "b": B, "m": 257, "t": 2, "dmax": DMAX},
        "frontier_profiles": len(profiles),
        "positive_profiles": 70,
        "zero_demand_profiles": 1,
        "positive_states": len(states),
        "Q_histogram": {"21": 50, "22": 18, "23": 3},
        "potential": [
            {"D": D, "V": V, "weight": w}
            for (D, V), w in sorted(PAT.items())
        ],
        "generator_count": len(PAT),
        "diagonal_generators": 0,
        "accepted_denominator_scale": denom,
        "attempts": attempts,
        "variables": len(M.names),
        "rows": len(M.rows),
        "integer_arithmetic_only_acceptance": True,
        "floating_point_is_discovery_only": True,
        "numerator_map_sha256": hashlib.sha256(raw_nums).hexdigest(),
        "scaled_integer_numerators": nums,
        "interpretation": (
            "PASS exactly verifies the profile-specific envelope coefficients for the fixed "
            "nine-term integer rectangle potential on all 154 positive-demand N32 t=2 states. "
            "The sole zero-demand frontier profile is handled separately by hand."
        ),
    }
    z.output.parent.mkdir(parents=True, exist_ok=True)
    z.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    summary = {k: v for k, v in out.items() if k != "scaled_integer_numerators"}
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
