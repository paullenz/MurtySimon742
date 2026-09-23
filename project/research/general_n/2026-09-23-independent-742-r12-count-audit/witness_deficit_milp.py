import json
import sys
import numpy as np
from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix


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

    # Choose one integral centre-deficit level.
    for i in range(k):
        add([(a_idx[i,c], 1) for c in levels], 1, 1)
    # Exact left degrees.
    for i in range(k):
        add([(n_idx[p,z], 1) for p,J in enumerate(patterns)
             if i in J for z in levels], xs[i], xs[i])
    max_count = max(xs)
    # An endpoint at level z can use pattern J only if every incident centre
    # has deficit at least rho+1-z.
    for p, J in enumerate(patterns):
        for z in levels:
            threshold = max(0, rho + 1 - z)
            if threshold <= 0:
                continue
            for i in J:
                allowed = [(a_idx[i,c], max_count)
                           for c in levels if c >= threshold]
                add([(n_idx[p,z], 1)] + [(j,-v) for j,v in allowed], hi=0)
    # Full quadratic star inequalities.
    for i in range(k):
        rhs = xs[i]*(rho+1) + xs[i]*(xs[i]-1)//2
        items = [(a_idx[i,c], xs[i]*c) for c in levels]
        items += [(n_idx[p,z], z) for p,J in enumerate(patterns)
                  if i in J for z in levels]
        add(items, lo=rhs)

    A = lil_matrix((len(rows), nvar), dtype=float)
    for r, items in enumerate(rows):
        for j, v in items:
            A[r,j] += v
    lower = np.zeros(nvar)
    upper = np.ones(nvar)
    upper[len(a_keys):] = max_count
    integrality = np.ones(nvar, dtype=int)
    obj = np.zeros(nvar)
    for i,c in a_keys:
        obj[a_idx[i,c]] = c
    for p,z in n_keys:
        obj[n_idx[p,z]] = z
    result = milp(
        obj, integrality=integrality, bounds=Bounds(lower, upper),
        constraints=LinearConstraint(A.tocsr(), np.array(lows), np.array(highs)),
        options={"time_limit": time_limit, "presolve": True},
    )
    payload = {
        "model": "aggregated-incidence-pattern-v1",
        "demands": demands, "x": xs, "h": h, "rho": rho,
        "Delta": Delta, "status": int(result.status),
        "message": result.message,
        "minimum_deficit": None if result.fun is None else round(result.fun),
    }
    if result.x is not None:
        payload["centre_deficits"] = [
            sum(c*round(result.x[a_idx[i,c]]) for c in levels) for i in range(k)
        ]
        payload["right_types"] = [
            {"labels": list(patterns[p]), "deficit": z,
             "multiplicity": round(result.x[n_idx[p,z]])}
            for p,z in n_keys if result.x[n_idx[p,z]] > .5
        ]
    return payload


def solve(demands, xs, rho, Delta, time_limit=20):
    k = len(xs)
    R = sum(xs)  # enough named right vertices; unused columns are allowed
    n_y = k * R
    off_c = n_y
    off_z = off_c + k
    off_w = off_z + R
    nvar = off_w + n_y

    def Y(i, t): return i * R + t
    def C(i): return off_c + i
    def Z(t): return off_z + t
    def W(i, t): return off_w + i * R + t

    h = [2 * xs[i] - demands[i] for i in range(k)]
    M = Delta
    rows, lows, highs = [], [], []

    def add(items, lo=-np.inf, hi=np.inf):
        rows.append(items); lows.append(lo); highs.append(hi)

    for i in range(k):
        add([(Y(i,t),1) for t in range(R)], xs[i], xs[i])
    for i in range(k):
        for t in range(R):
            # right degree <= h_i when i is incident
            add([(Y(j,t),1) for j in range(k)] + [(Y(i,t),M)],
                hi=h[i]+M)
            # pair deficit
            add([(C(i),1),(Z(t),1),(Y(i,t),-M)],
                lo=rho+1-M)
            # w = y*z linearization
            add([(W(i,t),1),(Z(t),-1)], hi=0)
            add([(W(i,t),1),(Y(i,t),-M)], hi=0)
            add([(W(i,t),1),(Z(t),-1),(Y(i,t),-M)], lo=-M)
    for i in range(k):
        rhs = xs[i]*(rho+1) + xs[i]*(xs[i]-1)//2
        add([(C(i),xs[i])] + [(W(i,t),1) for t in range(R)], lo=rhs)

    A = lil_matrix((len(rows), nvar), dtype=float)
    for r, items in enumerate(rows):
        for j, v in items:
            A[r,j] += v
    lower = np.zeros(nvar)
    upper = np.full(nvar, Delta, dtype=float)
    upper[:n_y] = 1
    # Deficit carried by an unused right vertex is never useful.
    for t in range(R):
        # z_t <= Delta * sum_i y_it
        addrow = len(rows)
    integrality = np.ones(nvar, dtype=int)
    obj = np.zeros(nvar)
    for i in range(k): obj[C(i)] = 1
    for t in range(R): obj[Z(t)] = 1
    result = milp(
        obj, integrality=integrality, bounds=Bounds(lower, upper),
        constraints=LinearConstraint(A.tocsr(), np.array(lows), np.array(highs)),
        options={"time_limit": time_limit, "presolve": True},
    )
    payload = {
        "demands": demands, "x": xs, "h": h, "rho": rho,
        "Delta": Delta, "status": int(result.status),
        "message": result.message, "minimum_deficit": None if result.fun is None else round(result.fun),
    }
    if result.x is not None:
        payload["centre_deficits"] = [round(result.x[C(i)]) for i in range(k)]
        used = []
        for t in range(R):
            labels = [i for i in range(k) if result.x[Y(i,t)] > .5]
            if labels:
                used.append({"labels": labels, "deficit": round(result.x[Z(t)])})
        payload["right_vertices"] = used
    return payload


if __name__ == "__main__":
    d = list(map(int, sys.argv[1].split(",")))
    x = list(map(int, sys.argv[2].split(",")))
    solver = solve_aggregated if len(sys.argv) < 6 or sys.argv[5] != "expanded" else solve
    print(json.dumps(solver(d, x, int(sys.argv[3]), int(sys.argv[4])), indent=2))
