import json
import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix


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
    print(json.dumps(solve(d, x, int(sys.argv[3]), int(sys.argv[4])), indent=2))
