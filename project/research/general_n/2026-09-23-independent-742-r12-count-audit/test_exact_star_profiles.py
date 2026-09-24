"""Replay the five audited leading n=18 profiles with exact small-star slack."""
import json
from witness_deficit_exact_star_milp import solve_aggregated


PROFILES = [
    ([8, 7], [8, 7]),
    ([8, 7], [8, 8]),
    ([8, 6, 1], [8, 6, 1]),
    ([8, 5, 2], [8, 5, 2]),
    ([5, 5, 5], [5, 5, 5]),
]

rows = []
for demands, xs in PROFILES:
    out = solve_aggregated(demands, xs, 2, 10, 60)
    out["Dmax"] = 16
    out["gap_vs_Dmax"] = (None if out["minimum_deficit"] is None
                           else out["minimum_deficit"] - 16)
    rows.append(out)
print(json.dumps({"n": 18, "Delta": 10, "rho": 2, "rows": rows}, indent=2))
