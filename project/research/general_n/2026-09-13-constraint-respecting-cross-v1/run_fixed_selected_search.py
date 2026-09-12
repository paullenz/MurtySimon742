#!/usr/bin/env python3
"""Exploratory fixed-selected-pattern residual/compatibility search.

A solver-reported infeasible fixed-S model is recorded as a negative experiment,
not a proof certificate. Positive patterns are decoded for direct checking.
"""
from pathlib import Path
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix
import argparse
import json
import random
import time

HERE = Path(__file__).resolve().parent
PARENT_INPUTS = HERE.parent / "2026-09-12-arc-realisation-pilot-v1" / "pilot_inputs.json"


class Model:
    def __init__(self):
        self.ub = []
        self.rows = []
        self.lo = []
        self.hi = []

    def var(self, upper=1):
        k = len(self.ub)
        self.ub.append(upper)
        return k

    def row(self, terms, lo=float("-inf"), hi=float("inf")):
        d = {}
        for j, c in terms:
            d[j] = d.get(j, 0) + c
        self.rows.append([(j, c) for j, c in d.items() if c])
        self.lo.append(lo)
        self.hi.append(hi)

    def solve(self, seconds):
        rr, cc, dd = [], [], []
        for i, row in enumerate(self.rows):
            for j, c in row:
                rr.append(i)
                cc.append(j)
                dd.append(c)
        A = coo_matrix(
            (dd, (rr, cc)), shape=(len(self.rows), len(self.ub))
        ).tocsr()
        return milp(
            [0.0] * len(self.ub),
            integrality=[1] * len(self.ub),
            bounds=Bounds([0] * len(self.ub), self.ub),
            constraints=LinearConstraint(A, self.lo, self.hi),
            options={"time_limit": seconds, "presolve": True},
        )


def random_selected(rec, rng, extra):
    """Randomized load-balanced selected pattern respecting source eligibility.

    `extra` is the maximum random number of incidences above s_i for each label.
    Failure here only means the randomized request overfilled source capacity.
    """
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    S = [set() for _ in range(b)]
    for i in sorted(range(a), key=lambda i: (-s[i], i)):
        need = s[i] + (rng.randint(0, extra) if extra else 0)
        eligible = [
            u
            for u in range(b)
            if rho[u] >= s[i] and len(S[u]) < a - rho[u]
        ]
        if len(eligible) < need:
            return None
        scored = [
            (len(S[u]) + 2.5 * rng.random() - 0.05 * rho[u], u)
            for u in eligible
        ]
        for _, u in sorted(scored)[:need]:
            S[u].add(i)
    return S


def fixed_selected_model(rec, S):
    """Choose residual sets after fixing S, with prior compatibility checks.

    This deliberately does not perform the final Hall routing. It asks whether
    the fixed S can be completed so that every selected incidence has at least
    one exact compatible destination and passes the minimum endpoint load.
    """
    a, b, rho = rec["a"], rec["b"], rec["rho"]
    m = Model()
    r = {
        (u, i): m.var(int(i not in S[u]))
        for u in range(b)
        for i in range(a)
    }
    w = {
        (u, i, v): m.var()
        for u in range(b)
        for i in S[u]
        for v in range(b)
        if v != u
    }
    X = [sum(i in S[u] for u in range(b)) for i in range(a)]
    q = list(map(len, S))

    for u in range(b):
        m.row([(r[u, i], 1) for i in range(a)], rho[u], rho[u])

    for u in range(b):
        for i in S[u]:
            # Minimum endpoint load before incoming selected pairs are known:
            # R_i + x_i >= q_u.
            m.row([(r[v, i], 1) for v in range(b)], lo=q[u] - X[i])

            # At least one exact compatible destination for this obligation.
            m.row([(w[u, i, v], 1) for v in range(b) if v != u], lo=1)
            for v in range(b):
                if v == u:
                    continue
                W = w[u, i, v]

                # S_u \ N_v = {i}: i is absent at v.
                if i in S[v]:
                    m.row([(W, 1)], hi=0)
                else:
                    m.row([(r[v, i], 1), (W, 1)], hi=1)

                # S_u \ {i} is contained in N_v.
                for j in S[u] - {i}:
                    if j not in S[v]:
                        m.row([(r[v, j], 1), (W, -1)], lo=0)

                # S_v is contained in N_u.
                for j in S[v]:
                    if j not in S[u]:
                        m.row([(r[u, j], 1), (W, -1)], lo=0)

    return m, r


def decode_positive(rec, S, rvars, x):
    a, b = rec["a"], rec["b"]
    R = [
        {i for i in range(a) if x[rvars[u, i]] > 0.5}
        for u in range(b)
    ]
    N = [S[u] | R[u] for u in range(b)]
    X = [sum(i in S[u] for u in range(b)) for i in range(a)]
    Ri = [sum(i in R[u] for u in range(b)) for i in range(a)]
    q = list(map(len, S))

    for u in range(b):
        assert len(R[u]) == rec["rho"][u]
        assert not S[u] & R[u]
        for i in S[u]:
            assert Ri[i] + X[i] >= q[u]
            D = [
                v
                for v in range(b)
                if v != u and S[u] - N[v] == {i} and S[v] <= N[u]
            ]
            assert D

    return {
        "selected": [sorted(z) for z in S],
        "residual": [sorted(z) for z in R],
    }


def run_trial(rec, S, seconds):
    if S is None:
        return {"classification": "generator_failed_capacity"}
    m, rvars = fixed_selected_model(rec, S)
    res = m.solve(seconds)
    out = {
        "selected_total": sum(map(len, S)),
        "source_q": list(map(len, S)),
        "solver_status": int(res.status),
        "solver_message": res.message,
        "variables": len(m.ub),
        "rows": len(m.rows),
    }
    if res.x is not None:
        out["classification"] = "positive_pattern"
        out["pattern"] = decode_positive(rec, S, rvars, res.x)
    elif res.status == 2:
        out["classification"] = "solver_reported_infeasible"
    elif res.status == 1:
        out["classification"] = "open_time_limit_no_incumbent"
    else:
        out["classification"] = "open_solver_outcome"
    return out


def default_specs():
    return [
        dict(record=0, extra=0, trials=1000, seed=742123, seconds=0.25),
        dict(record=1, extra=0, trials=100, seed=99001, seconds=0.25),
        dict(record=2, extra=0, trials=100, seed=99002, seconds=0.25),
        dict(record=3, extra=0, trials=100, seed=99003, seconds=0.25),
        dict(record=4, extra=0, trials=100, seed=99004, seconds=0.25),
        dict(record=5, extra=0, trials=100, seed=99005, seconds=0.25),
        dict(record=0, extra=1, trials=500, seed=742201, seconds=0.25),
        dict(record=0, extra=2, trials=300, seed=88302, seconds=0.25),
        dict(record=0, extra=3, trials=200, seed=88303, seconds=0.25),
    ]


def quick_specs():
    return [dict(record=i, extra=0, trials=5, seed=120000 + i, seconds=0.25) for i in range(6)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="five deterministic trials per state")
    parser.add_argument("--output", default="SAMPLE_RESULTS.json")
    args = parser.parse_args()

    parent = json.loads(PARENT_INPUTS.read_text())
    records = parent["sample"]
    specs = quick_specs() if args.quick else default_specs()
    results = []
    started = time.time()

    for spec in specs:
        rec = records[spec["record"]]
        rng = random.Random(spec["seed"])
        counts = {}
        first_positive = None
        selected_totals = []
        for k in range(spec["trials"]):
            S = random_selected(rec, rng, spec["extra"])
            result = run_trial(rec, S, spec["seconds"])
            counts[result["classification"]] = counts.get(result["classification"], 0) + 1
            if S is not None:
                selected_totals.append(sum(map(len, S)))
            if result["classification"] == "positive_pattern":
                first_positive = {"trial": k, "result": result}
                break
        results.append(
            {
                "record_index": spec["record"],
                "layer": rec["layer"],
                "state_id": rec["state_id"],
                "extra_max_per_label": spec["extra"],
                "planned_trials": spec["trials"],
                "executed_trials": sum(counts.values()),
                "seed": spec["seed"],
                "time_limit_seconds": spec["seconds"],
                "classification_counts": counts,
                "selected_total_range": (
                    [min(selected_totals), max(selected_totals)] if selected_totals else None
                ),
                "first_positive": first_positive,
            }
        )
        print(json.dumps(results[-1]), flush=True)

    report = {
        "schema": "constraint-respecting-cross-pilot-results-v1",
        "date": "2026-09-13",
        "quick": args.quick,
        "results": results,
        "elapsed_seconds": time.time() - started,
        "interpretation": (
            "Solver-reported infeasibility is exploratory evidence only and is not a proof "
            "certificate or whole-state exclusion. Positive patterns are directly decoded "
            "and checked by the script."
        ),
    }
    (HERE / args.output).write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
