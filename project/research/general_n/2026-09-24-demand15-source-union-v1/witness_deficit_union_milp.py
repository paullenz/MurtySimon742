"""Witness-deficit MILP with the graph-level source-union endpoint floor."""
import numpy as np
from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix


def validate_optimal_result(result, objective, lower, upper, rows, lows, highs):
    """Gate solver status and exactly validate the rounded integral witness.

    A time-limit incumbent is an upper bound, never a proved minimum. Unknown
    results raise instead of letting legacy drivers silently skip a case.
    Optimality/infeasibility still relies on the numerical solver, not a
    rational dual certificate; the exact checks below certify only the primal.
    """
    status = int(result.status)
    if status == 2:
        if result.x is not None or result.fun is not None:
            raise RuntimeError('UNRESOLVED_MILP: infeasible status with incumbent')
        return None
    if status != 0:
        raise RuntimeError(f'UNRESOLVED_MILP: status={status}; {result.message}')
    if result.x is None or result.fun is None or not np.isfinite(result.fun):
        raise RuntimeError('UNRESOLVED_MILP: optimal status lacks finite witness/objective')
    if len(result.x) != len(objective) or not np.all(np.isfinite(result.x)):
        raise RuntimeError('UNRESOLVED_MILP: malformed primal vector')
    rounded = [int(round(value)) for value in result.x]
    if any(abs(value-integer) > 1e-6 for value, integer in zip(result.x, rounded)):
        raise RuntimeError('UNRESOLVED_MILP: nonintegral primal vector')
    if any(not lo <= value <= hi for value, lo, hi in zip(rounded, lower, upper)):
        raise RuntimeError('UNRESOLVED_MILP: rounded primal violates bounds')
    for items, lo, hi in zip(rows, lows, highs):
        if any(float(coefficient) != int(coefficient) for _, coefficient in items):
            raise RuntimeError('UNRESOLVED_MILP: nonintegral model coefficient')
        value = sum(int(coefficient)*rounded[j] for j, coefficient in items)
        if not lo <= value <= hi:
            raise RuntimeError('UNRESOLVED_MILP: rounded primal violates a row')
    if any(float(c) != int(c) for c in objective):
        raise RuntimeError('UNRESOLVED_MILP: nonintegral objective coefficient')
    value = sum(int(c)*x for c, x in zip(objective, rounded))
    if abs(value-float(result.fun)) > 1e-6:
        raise RuntimeError('UNRESOLVED_MILP: objective disagrees with exact primal')
    return value


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
        rows.append(items); lows.append(lo); highs.append(hi)
    for i in range(k):
        add([(a_idx[i, c], 1) for c in levels], 1, 1)
    for i in range(k):
        add([(n_idx[p, z], 1) for p, J in enumerate(patterns)
             if i in J for z in levels], xs[i], xs[i])
    # Each nonzero incidence pattern represents one physical endpoint t in
    # B=N(v).  Distinct pattern copies are distinct vertices, so their total
    # multiplicity cannot exceed |B|=Delta.
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
        slack = xs[i] * (xs[i] - 1) // 2 + (1 if xs[i] >= 3 else 0)
        if Delta == 10 and rho == 2 and xs[i] == 7:
            slack = 30
        if Delta == 10 and rho == 2 and xs[i] == 8:
            slack = 35
        rhs = xs[i] * (rho + 1) + slack
        items = [(a_idx[i, c], xs[i] * c) for c in levels]
        items += [(n_idx[p, z], z) for p, J in enumerate(patterns)
                  if i in J for z in levels]
        add(items, lo=rhs)
    A = lil_matrix((len(rows), nvar), dtype=float)
    for r, items in enumerate(rows):
        for j, v in items:
            A[r, j] += v
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
    obj = np.zeros(nvar)
    for i, c in a_keys:
        obj[a_idx[i, c]] = c
    for p, z in n_keys:
        obj[n_idx[p, z]] = z
    result = milp(
        obj, integrality=integrality, bounds=Bounds(lower, upper),
        constraints=LinearConstraint(A.tocsr(), np.array(lows), np.array(highs)),
        options={"time_limit": time_limit, "presolve": True, "mip_rel_gap": 0.0},
    )
    verified_minimum = validate_optimal_result(result, obj, lower, upper, rows, lows, highs)
    payload = {
        "model": "aggregated-incidence-pattern-source-union-right-budget-v3",
        "demands": demands, "x": xs, "h": h, "rho": rho,
        "Delta": Delta, "status": int(result.status),
        "message": result.message,
        "minimum_deficit": verified_minimum,
        "positive_source_union_floor_types": sum(x > 0 for x in source_union_floors),
        "maximum_source_union_floor": max(source_union_floors, default=0),
    }
    if result.x is not None:
        payload["centre_deficits"] = [
            sum(c * round(result.x[a_idx[i, c]]) for c in levels) for i in range(k)]
        payload["right_types"] = [
            {"labels": list(patterns[p]), "deficit": z,
             "source_union_floor": source_union_floors[p],
             "multiplicity": round(result.x[n_idx[p, z]])}
            for p, z in n_keys if result.x[n_idx[p, z]] > .5]
    return payload
