"""Stable-index row screen using the exact-small-star v4 witness model."""
import itertools
import json
import sys

sys.path.insert(0, "project/research/general_n/2026-09-24-demand15-source-union-v1")
from screen_demand_15_16 import partitions, f
from witness_deficit_exact_star_milp import solve_aggregated


def main(n, Delta, resume_scalar=0, stop_scalar=None):
    rho = 2 * Delta - n
    Dmax = n * rho // 2 - 2 if n % 2 == 0 else (n * rho - 3) // 2
    a = n - 1 - Delta
    tested = scalar_pass = 0
    survivors = []
    best = None
    for total in (15, 16):
        for demand in partitions(total):
            if len(demand) > a or (total == 16 and min(demand) < 2):
                continue
            ranges = [range(d, (Delta - 1 + d) // 2 + 1) for d in demand]
            for xs in itertools.product(*ranges):
                if any(demand[j] == demand[j-1] and xs[j] > xs[j-1]
                       for j in range(1, len(demand))):
                    continue
                tested += 1
                hs = [2*x-d for x, d in zip(xs, demand)]
                if any(x > (Delta-h)*(Delta-2) for x, h in zip(xs, hs)):
                    continue
                if max(hs) * Dmax < sum(f(x, rho) for x in xs):
                    continue
                if sum(xs) > Delta * (Delta - 1) // 2:
                    continue
                scalar_pass += 1
                if scalar_pass <= resume_scalar:
                    continue
                if stop_scalar is not None and scalar_pass > stop_scalar:
                    print("FINAL " + json.dumps({
                        "model": "exact-small-star-v4", "n": n,
                        "Delta": Delta, "rho": rho, "Dmax": Dmax,
                        "patterns_tested": tested, "scalar_pass": scalar_pass-1,
                        "range": [resume_scalar+1, stop_scalar],
                        "survivor_count": len(survivors), "survivors": survivors,
                        "closest": best}), flush=True)
                    return
                out = solve_aggregated(list(demand), list(xs), rho, Delta, 10)
                out["total_demand"] = total
                out["stable_index"] = scalar_pass
                if out["minimum_deficit"] is not None:
                    out["gap_vs_Dmax"] = out["minimum_deficit"] - Dmax
                    if out["gap_vs_Dmax"] <= 0:
                        survivors.append(out)
                        print("SURVIVOR " + json.dumps(out), flush=True)
                    if best is None or out["gap_vs_Dmax"] < best["gap_vs_Dmax"]:
                        best = out
                if scalar_pass % 100 == 0:
                    print(json.dumps({"scalar_pass": scalar_pass,
                                      "survivors": len(survivors),
                                      "best_gap": (None if best is None
                                                   else best["gap_vs_Dmax"])}),
                          flush=True)
    print("FINAL " + json.dumps({
        "model": "exact-small-star-v4", "n": n, "Delta": Delta,
        "rho": rho, "Dmax": Dmax, "patterns_tested": tested,
        "scalar_pass": scalar_pass, "range": [resume_scalar+1, scalar_pass],
        "survivor_count": len(survivors), "survivors": survivors,
        "closest": best}), flush=True)


if __name__ == "__main__":
    resume = int(sys.argv[sys.argv.index("--resume-scalar")+1])
    stop = int(sys.argv[sys.argv.index("--stop-scalar")+1])
    main(int(sys.argv[1]), int(sys.argv[2]), resume, stop)
