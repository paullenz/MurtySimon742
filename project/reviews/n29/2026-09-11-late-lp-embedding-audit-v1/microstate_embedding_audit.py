#!/usr/bin/env python3
"""Independent graph-level microstate -> grouped late-LP regression for n=29.

This script is deliberately written outside the production late-model builder.  It
constructs explicit selected/residual microstates, averages them into the Y/T/W/P/Z
variables from first principles using exact Fraction arithmetic, and then evaluates
every row of the production corrected-v2 model.  As a sensitivity control the same
assignment is also evaluated against the quarantined v1 model and MUST fail there.

The fixtures are not asserted to be diameter-two-critical graphs.  They are explicit
finite microstates satisfying the local hypotheses used by the late averaging layer.
Their purpose is to test the *embedding/normalisation algebra*, not graph existence.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
PROD = HERE.parents[2] / "2026-09-08-redteam-restart-v1"
sys.path.insert(0, str(PROD))

import independent_threshold_model_v2 as v2  # noqa: E402
import independent_threshold_model as v1      # noqa: E402

A = 12
B = 16


def balanced_edges(rowdeg, avoid=frozenset(), offset=0):
    """Simple bipartite row-degree realisation, balancing column degrees."""
    col = [0] * A
    edges = []
    for u, deg in enumerate(rowdeg):
        cand = [i for i in range(A) if (u, i) not in avoid]
        cand.sort(key=lambda i: (col[i], (i - u - offset) % A))
        if len(cand) < deg:
            raise AssertionError("insufficient simple bipartite capacity")
        for i in cand[:deg]:
            col[i] += 1
            edges.append((u, i))
    assert len(edges) == len(set(edges))
    return edges


def make_fixture(kind):
    """Return a locally bridge-compatible explicit microstate."""
    if kind == "uniform":
        rho = [4] * B
        q_target = [4] * B
        s = [1] * A
    elif kind == "mixed":
        rho = [3] * 8 + [4] * 8
        q_target = [4] * 8 + [3] * 8
        s = [1] * 6 + [0] * 6
    else:
        raise ValueError(kind)

    # Oriented selected missing-B pairs.  Forward cyclic distances <=4 ensure
    # that no unordered pair is used in both orientations.
    pair_arcs = []
    seen = set()
    for u, qq in enumerate(q_target):
        for step in range(1, qq + 1):
            w = (u + step) % B
            assert u != w and (w, u) not in seen and (u, w) not in seen
            seen.add((u, w))
            pair_arcs.append((u, w))

    q = [0] * B
    p = [0] * B
    for u, w in pair_arcs:
        q[u] += 1
        p[w] += 1
    assert q == q_target

    # One selected A-B edge per outgoing selected B-pair.  The particular
    # association to the supplement is irrelevant to the grouped late LP.
    selected = balanced_edges(q, offset=0)
    assert Counter(u for u, _ in selected) == Counter({u: q[u] for u in range(B)})

    # Residual A-B edges are disjoint from selected A-B edges and realise rho.
    residual = balanced_edges(rho, avoid=frozenset(selected), offset=5)
    assert not (set(selected) & set(residual))
    assert Counter(u for u, _ in residual) == Counter({u: rho[u] for u in range(B)})

    x = [0] * A
    R = [0] * A
    for u, i in selected:
        x[i] += 1
    for u, i in residual:
        R[i] += 1

    # Choose F-degrees so s_i=max(0,d_i-R_i) is exactly the prescribed demand.
    d = [R[i] + s[i] for i in range(A)]
    assert all(0 <= di <= 10 for di in d)
    assert all(0 <= Ri <= B for Ri in R)
    assert all(x[i] <= B - R[i] for i in range(A))

    # This t simply makes the exact global degree ledger true for the fixture.
    assert sum(d) % 2 == 0
    r = sum(rho)
    t = sum(d) // 2 - r
    assert sum(R) == r
    assert sum(d) == 2 * (r + t)

    # Local hypotheses used by Z and P construction.
    for u, w in pair_arcs:
        assert rho[w] + q[w] >= q[u] - 1
    for u in range(B):
        assert q[u] + rho[u] <= A
        assert p[u] <= rho[u] + 3
        assert q[u] + p[u] <= B - 1
    for u, i in selected:
        assert s[i] <= rho[u]
        assert d[i] <= rho[u] + R[i]
        assert d[i] <= rho[u] + q[u] - 1
        assert R[i] + x[i] >= q[u] + p[u]

    return {
        "kind": kind,
        "rho": rho,
        "q": q,
        "p": p,
        "s": s,
        "R": R,
        "x": x,
        "d": d,
        "selected": selected,
        "residual": residual,
        "pair_arcs": pair_arcs,
        "t": t,
    }


def group_data(vals):
    counts = Counter(vals)
    ordered = sorted(counts)
    idx = {value: j for j, value in enumerate(ordered)}
    mult = {j: counts[value] for value, j in idx.items()}
    return idx, mult


def aggregate(fix):
    """Map an explicit microstate to exact Y/T/W/P/Z grouped variables."""
    s, rho = fix["s"], fix["rho"]
    d, R, x = fix["d"], fix["R"], fix["x"]
    q, p = fix["q"], fix["p"]
    g_of, ng = group_data(s)
    k_of, nk = group_data(rho)

    val = defaultdict(Fraction)

    # Y and T: fractions within one demand group.
    for i in range(A):
        g = g_of[s[i]]
        val[("Y", g, d[i], R[i])] += Fraction(1, ng[g])
        U = B - R[i]
        for h in range(1, U + 1):
            if x[i] >= h:
                val[("T", g, d[i], R[i], h)] += Fraction(1, ng[g])

    # W: fractions within one residual-degree source group.
    for u in range(B):
        k = k_of[rho[u]]
        val[("W", k, q[u], p[u])] += Fraction(1, nk[k])

    # P: density among ordered source/target vertex pairs.  The denominator
    # excludes the diagonal for a same-rho group.
    for u, w in fix["pair_arcs"]:
        k, l = k_of[rho[u]], k_of[rho[w]]
        den = nk[k] * (nk[l] - (k == l))
        assert den > 0
        val[("P", k, l, q[u], q[w])] += Fraction(1, den)

    # Z: density among all source vertices in k and labels in g.
    for u, i in fix["selected"]:
        k, g = k_of[rho[u]], g_of[s[i]]
        den = nk[k] * ng[g]
        val[("Z", k, g, q[u], p[u], d[i], R[i])] += Fraction(1, den)

    return dict(val)


def evaluate(model, assignment):
    """Evaluate every production LP row with exact rational arithmetic."""
    by_index = []
    missing_nonzero = []
    names = set(model.names)
    for name, value in assignment.items():
        if value and name not in names:
            missing_nonzero.append((name, str(value)))
    if missing_nonzero:
        return {"missing_nonzero_variables": missing_nonzero, "eq_bad": [], "ub_bad": []}

    for name in model.names:
        value = assignment.get(name, Fraction(0))
        assert 0 <= value <= 1, (name, value)
        by_index.append(value)

    eq_bad = []
    for idx, (row, rhs) in enumerate(model.eq):
        lhs = sum(Fraction(c) * by_index[j] for j, c in row.items())
        if lhs != rhs:
            eq_bad.append((idx, str(lhs), str(rhs)))

    ub_bad = []
    for idx, (row, rhs) in enumerate(model.ub):
        lhs = sum(Fraction(c) * by_index[j] for j, c in row.items())
        if lhs > rhs:
            ub_bad.append((idx, str(lhs), str(rhs)))

    return {
        "missing_nonzero_variables": [],
        "eq_bad": eq_bad,
        "ub_bad": ub_bad,
        "variables": len(model.names),
        "equalities": len(model.eq),
        "inequalities": len(model.ub),
    }


def run_fixture(kind):
    fix = make_fixture(kind)
    assignment = aggregate(fix)

    corrected = v2.build(fix["s"], fix["rho"], fix["t"])
    old = v1.build(fix["s"], fix["rho"], fix["t"])
    c = evaluate(corrected, assignment)
    o = evaluate(old, assignment)

    assert not c["missing_nonzero_variables"], c
    assert not c["eq_bad"], c
    assert not c["ub_bad"], c

    # Sensitivity control: the same exact graph-level assignment must expose
    # the historical v1 label-group multiplicity error.
    old_failures = len(o["eq_bad"]) + len(o["ub_bad"]) + len(o["missing_nonzero_variables"])
    assert old_failures > 0, "audit fixture failed to distinguish quarantined v1 from corrected v2"

    return {
        "fixture": kind,
        "t": fix["t"],
        "demand_groups": sorted(Counter(fix["s"]).items()),
        "residual_groups": sorted(Counter(fix["rho"]).items()),
        "selected_pair_arcs": len(fix["pair_arcs"]),
        "selected_cross_edges": len(fix["selected"]),
        "residual_cross_edges": len(fix["residual"]),
        "corrected_v2": {
            "variables": c["variables"],
            "equalities": c["equalities"],
            "inequalities": c["inequalities"],
            "violations": 0,
        },
        "quarantined_v1_failures": {
            "equalities": len(o["eq_bad"]),
            "inequalities": len(o["ub_bad"]),
            "missing_nonzero_variables": len(o["missing_nonzero_variables"]),
            "total": old_failures,
        },
    }


def main():
    results = [run_fixture("uniform"), run_fixture("mixed")]
    report = {
        "schema": "n29-late-lp-microstate-embedding-audit-v1",
        "status": "PASS",
        "purpose": "exact rational regression of graph-level averaging into corrected production late LP",
        "fixtures": results,
        "corrected_v2_all_rows_satisfied": True,
        "historical_v1_detectably_fails": True,
        "external_independence": False,
        "note": "Fixtures test averaging/normalisation algebra, not existence of diameter-two-critical graphs.",
    }
    out = HERE / "MICROSTATE_AUDIT_REPORT.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
