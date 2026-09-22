#!/usr/bin/env python3
"""Replay the inherited one-supplement test on the MILP witness populations."""
import json

data = json.load(open("r11_support8_sources_case2.json"))


def supplement_ok(population):
    left_sets = [
        {i for i, state in enumerate(source) if state == 1}
        for source in population
    ]
    for u in range(len(population)):
        for i in left_sets[u]:
            possible = len(left_sets[u]) == 1
            for w in range(len(population)):
                if w == u:
                    continue
                forced = {
                    (u, j) for j in left_sets[u] if population[w][j] == 0
                } | {
                    (w, j) for j in left_sets[w] if population[u][j] == 0
                }
                possible |= forced == {(u, i)}
            if not possible:
                return False
    return True


rows = []
for row in data["feasible_rows"]:
    population = []
    for source in row["population"]:
        population += [tuple(source["state"])] * source["count"]
    rows.append({
        "mask": row["mask"],
        "R": row["R"],
        "source_count": len(population),
        "milp_witness_supplement_feasible": supplement_ok(population),
    })
print(json.dumps({
    "kernels": len(rows),
    "witness_supplement_feasible": sum(
        row["milp_witness_supplement_feasible"] for row in rows
    ),
    "rows": rows,
    "scope": "Checks one MILP witness per kernel only; failure does not prove that every source population fails.",
}, indent=2))
