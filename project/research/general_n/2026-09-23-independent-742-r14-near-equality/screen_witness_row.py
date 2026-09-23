import itertools
import json
import sys
from screen_demand_15_16 import partitions, f
from witness_deficit_milp import solve_aggregated


def main(n, Delta, stop_first=False, skip_tuples=None,
         resume_scalar=0, stop_scalar=None):
    skip_tuples = set() if skip_tuples is None else set(skip_tuples)
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
            # Every assigned witness needs a source in N_B(i), so h_i<Delta.
            ranges = [range(d, (Delta - 1 + d) // 2 + 1) for d in p]
            for xs in itertools.product(*ranges):
                if any(p[j] == p[j-1] and xs[j] > xs[j-1]
                       for j in range(1, len(p))):
                    continue
                if (tuple(p), tuple(xs)) in skip_tuples:
                    continue
                tested += 1
                hs = [2*x-d for x,d in zip(xs,p)]
                if any(x > (Delta-h)*(Delta-2) for x,h in zip(xs,hs)):
                    continue
                rhs = sum(f(x, rho) for x in xs)
                if max(hs) * Dmax < rhs:
                    continue
                if sum(xs) > Delta * (Delta - 1) // 2:
                    continue
                scalar_pass += 1
                if scalar_pass <= resume_scalar:
                    if scalar_pass % 500 == 0:
                        print(json.dumps({
                            "resume_scalar_scanned": scalar_pass,
                            "all_patterns_tested": tested,
                            "resume_target": resume_scalar,
                        }), flush=True)
                    continue
                if stop_scalar is not None and scalar_pass > stop_scalar:
                    result = {
                        "n": n, "Delta": Delta, "rho": rho,
                        "Dmax": Dmax, "a": a,
                        "patterns_tested": tested,
                        "scalar_pass": scalar_pass - 1,
                        "range_start": resume_scalar + 1,
                        "range_stop": stop_scalar,
                        "range_complete": True,
                        "abstract_survivor_count": len(abstract_survivors),
                        "abstract_survivors": abstract_survivors,
                        "closest_result": best_excluded,
                    }
                    print("FINAL "+json.dumps(result), flush=True)
                    return
                out = solve_aggregated(list(p), list(xs), rho, Delta, 10)
                out["total_demand"] = total
                if out["minimum_deficit"] is not None:
                    gap = out["minimum_deficit"] - Dmax
                    out["gap_vs_Dmax"] = gap
                    if gap <= 0:
                        abstract_survivors.append(out)
                        print("SURVIVOR "+json.dumps(out), flush=True)
                        if stop_first:
                            result = {
                                "n": n, "Delta": Delta, "rho": rho,
                                "Dmax": Dmax, "a": a,
                                "patterns_tested": tested,
                                "scalar_pass": scalar_pass,
                                "abstract_survivor_count": 1,
                                "abstract_survivors": abstract_survivors,
                                "closest_result": out,
                                "stopped_after_first_survivor": True,
                            }
                            print("FINAL "+json.dumps(result))
                            return
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
    skip = set()
    if "--skip-8,7:8,7" in sys.argv:
        skip.add(((8, 7), (8, 7)))
    if "--skip-known-n18" in sys.argv:
        skip.update({
            ((8, 7), (8, 7)),
            ((8, 7), (8, 8)),
            ((8, 6, 1), (8, 6, 1)),
            ((8, 5, 2), (8, 5, 2)),
        })
    resume_scalar = 0
    if "--resume-scalar" in sys.argv:
        resume_scalar = int(sys.argv[sys.argv.index("--resume-scalar") + 1])
    stop_scalar = None
    if "--stop-scalar" in sys.argv:
        stop_scalar = int(sys.argv[sys.argv.index("--stop-scalar") + 1])
    main(int(sys.argv[1]), int(sys.argv[2]),
         "--stop-first" in sys.argv, skip, resume_scalar, stop_scalar)
