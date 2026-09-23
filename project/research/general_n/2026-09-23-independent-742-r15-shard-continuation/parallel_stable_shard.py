import itertools
import json
import multiprocessing as mp
import sys

from screen_demand_15_16 import partitions, f
from witness_deficit_milp import solve_aggregated


def enumerate_stable(n, Delta, start, stop):
    rho = 2 * Delta - n
    Dmax = n * rho // 2 - 2 if n % 2 == 0 else (n * rho - 3) // 2
    a = n - 1 - Delta
    scalar = 0
    out = []
    for total in (15, 16):
        for p in partitions(total):
            if len(p) > a or (total == 16 and min(p) < 2):
                continue
            ranges = [range(d, (Delta - 1 + d) // 2 + 1) for d in p]
            for xs in itertools.product(*ranges):
                if any(p[j] == p[j - 1] and xs[j] > xs[j - 1]
                       for j in range(1, len(p))):
                    continue
                hs = [2 * x - d for x, d in zip(xs, p)]
                if any(x > (Delta - h) * (Delta - 2)
                       for x, h in zip(xs, hs)):
                    continue
                if max(hs) * Dmax < sum(f(x, rho) for x in xs):
                    continue
                if sum(xs) > Delta * (Delta - 1) // 2:
                    continue
                scalar += 1
                if scalar < start:
                    continue
                if scalar > stop:
                    return rho, Dmax, out, scalar - 1
                out.append((scalar, total, tuple(p), tuple(xs)))
    return rho, Dmax, out, scalar


def worker(args):
    idx, total, p, xs, n, Delta, rho, Dmax = args
    r = solve_aggregated(list(p), list(xs), rho, Delta, 10)
    md = r.get("minimum_deficit")
    return {
        "idx": idx,
        "total": total,
        "demands": list(p),
        "x": list(xs),
        "h": r.get("h"),
        "minimum_deficit": md,
        "gap_vs_Dmax": None if md is None else md - Dmax,
        "status": r.get("status"),
        "message": r.get("message"),
    }


def main():
    n, Delta, start, stop, workers = map(int, sys.argv[1:6])
    rho, Dmax, items, last = enumerate_stable(n, Delta, start, stop)
    args = [(idx, total, p, xs, n, Delta, rho, Dmax)
            for idx, total, p, xs in items]
    with mp.Pool(workers) as pool:
        rows = pool.map(worker, args)
    survivors = [
        r for r in rows
        if r["minimum_deficit"] is not None and r["gap_vs_Dmax"] <= 0
        and not (r["demands"] == [5, 5, 5] and r["x"] == [5, 5, 5])
    ]
    excluded = [
        r for r in rows
        if r["demands"] == [5, 5, 5] and r["x"] == [5, 5, 5]
        and r["minimum_deficit"] is not None and r["gap_vs_Dmax"] <= 0
    ]
    closest = min(
        (r for r in rows if r["minimum_deficit"] is not None),
        key=lambda r: r["gap_vs_Dmax"],
        default=None,
    )
    print(json.dumps({
        "n": n,
        "Delta": Delta,
        "rho": rho,
        "Dmax": Dmax,
        "range_start": start,
        "range_stop": stop,
        "enumerated": len(items),
        "stable_last_seen": last,
        "range_complete": len(items) == stop - start + 1,
        "abstract_survivors": survivors,
        "known_graph_excluded_survivors": excluded,
        "closest": closest,
        "rows": rows,
    }, indent=2))


if __name__ == "__main__":
    main()
