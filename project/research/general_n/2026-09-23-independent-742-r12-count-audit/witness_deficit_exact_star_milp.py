"""Source-union/right-budget witness MILP with audited exact star slack.

This is a forward model, kept separate from the historical v3 solver.  The
only change is the star-slack table: labelled graph/set-cover enumeration
gives the exact minima for x=3,...,7; the previously audited x=8 lower bound
is retained only in the (Delta,rho)=(10,2) row where it was proved.
"""
import numpy as np
from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix


EXACT_SMALL_STAR_SLACK = {3: 4, 4: 8, 5: 14, 6: 21, 7: 30}


def star_slack(x, rho, Delta):
    if x in EXACT_SMALL_STAR_SLACK:
        return EXACT_SMALL_STAR_SLACK[x]
    if (Delta, rho, x) == (10, 2, 8):
        return 35
    return x * (x - 1) // 2 + (1 if x >= 3 else 0)


def solve_aggregated(demands, xs, rho, Delta, time_limit=20):
    k = len(xs)
    h = [2 * xs[i] - demands[i] for i in range(k)]
    patterns = []
    for r in range(1, k + 1):
        for J in combinations(range(k), r):
            if r <= min(h[i] for i in J):
                patterns.append(J)
    levels = range(Delta + 1)
    a_keys = [(i, c) for i in range(k) for c in levels]
    n_keys = [(p, z) for p in range(len(patterns)) for z in levels]
    a_idx = {key: j for j, key in enumerate(a_keys)}
    n_idx = {key: len(a_keys) + j for j, key in enumerate(n_keys)}
    nvar = len(a_keys) + len(n_keys)
    rows, lows, highs = [], [], []

    def add(items, lo=-np.inf, hi=np.inf):
        rows.append(items)
        lows.append(lo)
        highs.append(hi)

    for i in range(k):
        add([(a_idx[i, c], 1) for c in levels], 1, 1)
    for i in range(k):
        add([(n_idx[p, z], 1) for p, J in enumerate(patterns)
             if i in J for z in levels], xs[i], xs[i])
    add([(n_idx[p, z], 1) for p in range(len(patterns)) for z in levels],
        hi=Delta)
    max_count = max(xs)
    for p, J in enumerate(patterns):
        for z in levels:
            threshold = max(0, rho + 1 - z)
            if threshold <= 0:
                continue
            for i in J:
                allowed = [(a_idx[i, c], max_count)
                           for c in levels if c >= threshold]
                add([(n_idx[p, z], 1)] + [(j, -v) for j, v in allowed], hi=0)
    for i in range(k):
        rhs = xs[i] * (rho + 1) + star_slack(xs[i], rho, Delta)
        items = [(a_idx[i, c], xs[i] * c) for c in levels]
        items += [(n_idx[p, z], z) for p, J in enumerate(patterns)
                  if i in J for z in levels]
        add(items, lo=rhs)

    A = lil_matrix((len(rows), nvar), dtype=float)
    for r, items in enumerate(rows):
        for j, value in items:
            A[r, j] += value
    lower = np.zeros(nvar)
    upper = np.ones(nvar)
    for i in range(k):
        for c in levels:
            if c > h[i]:
                upper[a_idx[i, c]] = 0
    upper[len(a_keys):] = max_count
    source_union_floors = []
    for p, J in enumerate(patterns):
        floor = max(0, rho + len(J) - min(h[i] for i in J))
        source_union_floors.append(floor)
        for z in range(floor):
            upper[n_idx[p, z]] = 0
    integrality = np.ones(nvar, dtype=int)
    objective = np.zeros(nvar)
    for i, c in a_keys:
        objective[a_idx[i, c]] = c
    for p, z in n_keys:
        objective[n_idx[p, z]] = z
    result = milp(
        objective, integrality=integrality, bounds=Bounds(lower, upper),
        constraints=LinearConstraint(A.tocsr(), np.array(lows), np.array(highs)),
        options={"time_limit": time_limit, "presolve": True},
    )
    payload = {
        "model": "source-union-right-budget-exact-small-star-v4",
        "demands": demands, "x": xs, "h": h, "rho": rho,
        "Delta": Delta, "star_slack": [star_slack(x, rho, Delta) for x in xs],
        "status": int(result.status), "message": result.message,
        "minimum_deficit": None if result.fun is None else round(result.fun),
    }
    if result.x is not None:
        payload["centre_deficits"] = [
            sum(c * round(result.x[a_idx[i, c]]) for c in levels)
            for i in range(k)]
        payload["right_types"] = [
            {"labels": list(patterns[p]), "deficit": z,
             "source_union_floor": source_union_floors[p],
             "multiplicity": round(result.x[n_idx[p, z]])}
            for p, z in n_keys if result.x[n_idx[p, z]] > .5]
    return payload
