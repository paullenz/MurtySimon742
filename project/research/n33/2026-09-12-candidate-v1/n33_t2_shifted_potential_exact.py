#!/usr/bin/env python3
"""Exact finite verifier for the N33 (a,b,t)=(14,18,2) equality frontier.

The 21 frozen demand rows expand to 29 conservative (s,rho) states after
monotone residual-tail closure and every allowed slack increment.

A fixed nine-term monotone BC potential -- the one-step b=18 lift of the N32
t=2 potential -- is tested on every state.  Floating LP is proposal only.
Accepted exclusions are rechecked after integer rounding and one-sided envelope
repair; the strict contradiction gap must remain negative in integer arithmetic.

Expected result: 25 exact exclusions and four named hand states.
"""
from collections import Counter
from pathlib import Path
import csv
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

HERE = Path(__file__).resolve().parent
FRONTIER = HERE / "N33_T2_FRONTIER.csv"
A = 14
B = 18
DMAX = 12

# Same graph-level h cutoffs as the N32 nine-rectangle potential.
PAT = {
    (2, 0): 4,
    (2, 7): 2,
    (2, 9): 1,
    (2, 11): 1,
    (2, 14): 1,
    (2, 15): 1,
    (3, 10): 1,
    (3, 12): 1,
    (3, 13): 1,
}

HAND = {
    ((3, 4) + (5,) * 12, (1,) * 6 + (3, 4) + (5,) * 10),
    ((3,) + (5,) * 13, (1,) * 6 + (3,) + (5,) * 11),
    ((4, 4) + (5,) * 12, (1,) * 6 + (4, 4) + (5,) * 10),
    ((4,) + (5,) * 13, (1,) * 6 + (4,) + (5,) * 11),
}


def cap(h, z):
    return (z * (z - 1) + h * (h + 1)) // 2


def gamma(h, W):
    if W <= 0:
        return 0
    z = h
    while W > cap(h, z):
        z += 1
    return z


def minimal_rho(s):
    raw = {}
    for h in range(2, A):
        vals = [x for x in s if x >= h]
        raw[h] = gamma(h, sum(vals)) if vals else 0

    # Residual tails must be nonincreasing: z_h >= z_{h+1}.
    z = {}
    running = 0
    for h in range(A - 1, 1, -1):
        running = max(running, raw[h])
        z[h] = running

    closure_extra = sum(z[h] - raw[h] for h in range(2, A))
    zz = {1: B, **z, A: 0}
    rho = []
    for k in range(1, A):
        count = zz[k] - zz[k + 1]
        assert count >= 0
        rho.extend([k] * count)
    assert len(rho) == B
    return tuple(rho), closure_extra


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


def load_states():
    demand_rows = []
    with FRONTIER.open() as f:
        for row in csv.reader(f):
            if not row:
                continue
            Q = int(row[0])
            s = tuple(map(int, row[1:]))
            assert len(s) == A and min(s) > 0 and Q in (22, 23)
            demand_rows.append((Q, s))

    assert len(demand_rows) == 21
    assert Counter(Q for Q, _ in demand_rows) == Counter({22: 18, 23: 3})

    states = []
    impossible = []
    for Q, s in demand_rows:
        rho0, closure_extra = minimal_rho(s)
        available = Q - 22 - closure_extra
        if available < 0:
            impossible.append((Q, s))
            continue
        variants = set()
        for E in range(available + 1):
            variants |= rho_variants(rho0, E)
        for rho in sorted(variants):
            states.append((Q, s, rho))

    assert not impossible
    assert len(states) == 29
    assert Counter(Q for Q, _, _ in states) == Counter({22: 18, 23: 11})
    return states


def potential(d, h):
    v = B - h
    return sum(w for (D, V), w in PAT.items() if d >= D and v >= V)


def tterm(rho, q, p, j):
    return (q if q >= j + 1 else 0) - (p if rho + q >= j else 0)


def build_envelope(s, rho):
    sc = Counter(s)
    rc = Counter(rho)
    r = sum(rho)
    names, bounds, rows, rhs, kinds = [], [], [], [], []

    def var(name, bound):
        j = len(names)
        names.append(name)
        bounds.append(bound)
        return j

    lam = var("lambda", (0, None))
    c = var("c", (0, None))
    mu_plus = var("mu+", (0, None))
    mu_minus = var("mu-", (0, None))
    tau = {j: var(("tau", j), (0, None)) for j in range(1, A + 1)}
    ell = {sv: var(("ell", sv), (None, None)) for sv in sc}
    sig = {rv: var(("sig", rv), (None, None)) for rv in rc}

    def le(co, b, kind):
        rows.append(co)
        rhs.append(b)
        kinds.append(kind)

    # Label envelopes.
    for sv in sc:
        for R in range(DMAX - sv + 1):
            for x in range(sv, B - R + 1):
                le(
                    {ell[sv]: 1, lam: -R, c: -x},
                    x * potential(R + sv, R + x),
                    ("ell", ell[sv]),
                )

    # Source envelopes.
    for rv in rc:
        qmax = min(A - rv, sum(si <= rv for si in s))
        for q in range(qmax + 1):
            pmax = min(rv + B - A - 1, B - 1 - q)
            for p in range(pmax + 1):
                co = {
                    sig[rv]: 1,
                    mu_plus: -(q - p),
                    mu_minus: (q - p),
                    c: q,
                }
                for j in range(1, A + 1):
                    tv = tterm(rv, q, p, j)
                    if tv:
                        co[tau[j]] = co.get(tau[j], 0) - tv
                le(
                    co,
                    -q * potential(rv + q - 1, q + p),
                    ("sig", sig[rv]),
                )

    # Strict scalar gap, normalized numerically to <= -1.
    co = {lam: r}
    for sv, n in sc.items():
        co[ell[sv]] = co.get(ell[sv], 0) - n
    for rv, n in rc.items():
        co[sig[rv]] = co.get(sig[rv], 0) - n
    le(co, -1, ("gap", None))

    M = lil_matrix((len(rows), len(names)))
    for i, co in enumerate(rows):
        for j, value in co.items():
            M[i, j] = value

    res = linprog(
        np.zeros(len(names)),
        A_ub=M.tocsr(),
        b_ub=np.array(rhs, float),
        bounds=bounds,
        method="highs",
    )
    if res.status == 4:
        res = linprog(
            np.zeros(len(names)),
            A_ub=M.tocsr(),
            b_ub=np.array(rhs, float),
            bounds=bounds,
            method="highs-ipm",
        )
    return names, bounds, rows, rhs, kinds, res


def exactify(model):
    names, bounds, rows, rhs, kinds, res = model
    if not res.success:
        return None

    for denom in (10_000, 100_000, 1_000_000, 10_000_000):
        X = [int(round(float(v) * denom)) for v in res.x]
        for j, (lo, _hi) in enumerate(bounds):
            if lo == 0 and X[j] < 0:
                X[j] = 0

        # Repair only the one-sided envelope variables.  Lowering ell/sigma
        # can only improve their local envelope rows; the final strict gap is
        # then checked again from scratch.
        repairs = {}
        for co, b, kind in zip(rows, rhs, kinds):
            if kind[0] == "gap":
                continue
            lhs = sum(int(a) * X[j] for j, a in co.items())
            target = int(b * denom)
            if lhs > target:
                j = kind[1]
                repairs[j] = max(repairs.get(j, 0), lhs - target)
        for j, delta in repairs.items():
            X[j] -= delta

        local_violations = 0
        bound_violations = 0
        gap = None
        for co, b, kind in zip(rows, rhs, kinds):
            lhs = sum(int(a) * X[j] for j, a in co.items())
            if kind[0] == "gap":
                gap = lhs
            elif lhs > int(b * denom):
                local_violations += 1

        for j, (lo, hi) in enumerate(bounds):
            if lo is not None and X[j] < int(lo * denom):
                bound_violations += 1
            if hi is not None and X[j] > int(hi * denom):
                bound_violations += 1

        if (
            local_violations == 0
            and bound_violations == 0
            and gap is not None
            and gap < 0
        ):
            return {
                "denominator": denom,
                "gap_numerator": gap,
                "repair_count": len(repairs),
                "repair_total": sum(repairs.values()),
            }
    return None


def main():
    states = load_states()
    exact = []
    hand = []
    failures = []

    for position, (Q, s, rho) in enumerate(states):
        model = build_envelope(s, rho)
        res = model[-1]
        key = (s, rho)
        if not res.success:
            if key in HAND:
                hand.append({"position": position, "Q": Q, "s": s, "rho": rho})
            else:
                failures.append({"position": position, "Q": Q, "s": s, "rho": rho})
            continue
        cert = exactify(model)
        if cert is None:
            failures.append({"position": position, "Q": Q, "s": s, "rho": rho})
        else:
            exact.append({"position": position, "Q": Q, "s": s, "rho": rho, **cert})

    assert len(exact) == 25, len(exact)
    assert len(hand) == 4, len(hand)
    assert not failures, failures
    assert {(tuple(x["s"]), tuple(x["rho"])) for x in hand} == HAND

    result = {
        "schema": "n33-t2-shifted-nine-rectangle-exact-v1",
        "status": "PASS",
        "scope": {"n": 33, "Delta": 18, "a": 14, "b": 18, "m": 272, "t": 2},
        "demand_profiles": 21,
        "expanded_states": 29,
        "Q_histogram_states": {"22": 18, "23": 11},
        "exact_potential_exclusions": 25,
        "hand_states": 4,
        "failures": 0,
        "potential": [
            {"D": D, "V": V, "weight": w}
            for (D, V), w in sorted(PAT.items())
        ],
        "denominator_histogram": dict(Counter(x["denominator"] for x in exact)),
        "worst_gap_numerator": max(x["gap_numerator"] for x in exact),
        "best_gap_numerator": min(x["gap_numerator"] for x in exact),
        "repair_count_total": sum(x["repair_count"] for x in exact),
        "floating_point_is_proposal_only": True,
        "integer_arithmetic_is_acceptance": True,
        "hand_profiles": hand,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
