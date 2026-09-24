"""Compare old and source-union witness models on the audited n=18 profiles."""
import json
from witness_deficit_milp import solve_aggregated as old
from witness_deficit_union_milp import solve_aggregated as new

PROFILES = [
    ([8, 7], [8, 7]),
    ([8, 7], [8, 8]),
    ([8, 6, 1], [8, 6, 1]),
    ([8, 5, 2], [8, 5, 2]),
    ([5, 5, 5], [5, 5, 5]),
]

rows = []
for demands, xs in PROFILES:
    before = old(demands, xs, 2, 10, 30)
    after = new(demands, xs, 2, 10, 30)
    rows.append({
        "demands": demands, "x": xs,
        "old_minimum_deficit": before["minimum_deficit"],
        "new_minimum_deficit": after["minimum_deficit"],
        "new_status": after["status"],
        "positive_floor_types": after["positive_source_union_floor_types"],
        "maximum_floor": after["maximum_source_union_floor"],
        "new_centre_deficits": after.get("centre_deficits"),
        "new_right_types": after.get("right_types"),
    })
print(json.dumps({"n": 18, "Delta": 10, "rho": 2, "rows": rows}, indent=2))
