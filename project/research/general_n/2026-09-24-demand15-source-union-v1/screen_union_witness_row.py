"""Demand-15/16 row screen with the source-union endpoint floor."""
import itertools
import json
import sys
from screen_demand_15_16 import partitions, f
from witness_deficit_union_milp import solve_aggregated


def main(n, Delta, stop_first=False, resume_scalar=0, stop_scalar=None):
    rho = 2 * Delta - n
    Dmax = n * rho // 2 - 2 if n % 2 == 0 else (n * rho - 3) // 2
    a = n - 1 - Delta
    tested = scalar_pass = 0
    survivors = []
    best = None
    for total in (15, 16):
        for p in partitions(total):
            if len(p) > a or (total == 16 and min(p) < 2):
                continue
            ranges = [range(d, (Delta - 1 + d) // 2 + 1) for d in p]
            for xs in itertools.product(*ranges):
                if any(p[j] == p[j-1] and xs[j] > xs[j-1]
                       for j in range(1, len(p))):
                    continue
                tested += 1
                hs = [2*x-d for x, d in zip(xs, p)]
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
                        "n": n, "Delta": Delta, "rho": rho, "Dmax": Dmax,
                        "patterns_tested": tested, "scalar_pass": scalar_pass-1,
                        "range": [resume_scalar+1, stop_scalar],
                        "survivor_count": len(survivors), "survivors": survivors,
                        "closest": best}), flush=True)
                    return
                out = solve_aggregated(list(p), list(xs), rho, Delta, 10)
                out["total_demand"] = total
                if out["minimum_deficit"] is not None:
                    out["gap_vs_Dmax"] = out["minimum_deficit"] - Dmax
                    if out["gap_vs_Dmax"] <= 0:
                        survivors.append(out)
                        print("SURVIVOR " + json.dumps(out), flush=True)
                        if stop_first:
                            print("FINAL " + json.dumps({
                                "n": n, "Delta": Delta, "rho": rho,
                                "Dmax": Dmax, "patterns_tested": tested,
                                "scalar_pass": scalar_pass, "survivor_count": 1,
                                "survivors": survivors}), flush=True)
                            return
                    if best is None or out["gap_vs_Dmax"] < best["gap_vs_Dmax"]:
                        best = out
                if scalar_pass % 100 == 0:
                    print(json.dumps({"scalar_pass": scalar_pass,
                                      "survivors": len(survivors),
                                      "best_gap": None if best is None else best["gap_vs_Dmax"]}),
                          flush=True)
    print("FINAL " + json.dumps({
        "n": n, "Delta": Delta, "rho": rho, "Dmax": Dmax,
        "patterns_tested": tested, "scalar_pass": scalar_pass,
        "survivor_count": len(survivors), "survivors": survivors,
        "closest": best}), flush=True)


if __name__ == "__main__":
    resume = int(sys.argv[sys.argv.index("--resume-scalar")+1]) if "--resume-scalar" in sys.argv else 0
    stop = int(sys.argv[sys.argv.index("--stop-scalar")+1]) if "--stop-scalar" in sys.argv else None
    main(int(sys.argv[1]), int(sys.argv[2]), "--stop-first" in sys.argv, resume, stop)
