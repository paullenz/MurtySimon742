import itertools
import json
import sys
from screen_demand_15_16 import partitions, f
from witness_deficit_milp import solve_aggregated


def main(n, Delta):
    rho = 2 * Delta - n
    Dmax = n * rho // 2 - 2 if n % 2 == 0 else (n * rho - 3) // 2
    a = n - 1 - Delta
    tested = scalar_pass = 0
    abstract_survivors = []
    best_excluded = None
    for total in (15, 16):
        for p in partitions(total):
            if len(p) > a or (total == 16 and min(p) < 2):
                continue
            ranges = [range(d, (Delta + d) // 2 + 1) for d in p]
            for xs in itertools.product(*ranges):
                if any(p[j] == p[j-1] and xs[j] > xs[j-1]
                       for j in range(1, len(p))):
                    continue
                tested += 1
                hs = [2*x-d for x,d in zip(xs,p)]
                rhs = sum(f(x, rho) for x in xs)
                if max(hs) * Dmax < rhs:
                    continue
                if sum(xs) > Delta * (Delta - 1) // 2:
                    continue
                scalar_pass += 1
                out = solve_aggregated(list(p), list(xs), rho, Delta, 10)
                out["total_demand"] = total
                if out["minimum_deficit"] is not None:
                    gap = out["minimum_deficit"] - Dmax
                    out["gap_vs_Dmax"] = gap
                    if gap <= 0:
                        abstract_survivors.append(out)
                    if best_excluded is None or gap < best_excluded["gap_vs_Dmax"]:
                        best_excluded = out
                if scalar_pass % 50 == 0:
                    print(json.dumps({
                        "scalar_pass_tested": scalar_pass,
                        "all_patterns_tested": tested,
                        "abstract_survivors": len(abstract_survivors),
                        "best_gap": None if best_excluded is None else best_excluded["gap_vs_Dmax"],
                    }), flush=True)
    result = {
        "n": n, "Delta": Delta, "rho": rho, "Dmax": Dmax, "a": a,
        "patterns_tested": tested, "scalar_pass": scalar_pass,
        "abstract_survivor_count": len(abstract_survivors),
        "abstract_survivors": abstract_survivors,
        "closest_result": best_excluded,
    }
    print("FINAL "+json.dumps(result))


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))
