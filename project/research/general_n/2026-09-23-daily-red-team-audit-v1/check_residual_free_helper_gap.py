#!/usr/bin/env python3
"""Hostile replay of r=11 supplement forcing with residual-free helpers.

The r=8 equality checker permits a supplement source with zero residual mass.
The later r=11 checkers omitted those helper types.  This bounded audit asks
whether the single source-population witness stored for each of the 27 surviving
r=11 kernels becomes supplement-feasible when the earlier, more permissive
semantics is restored.  A survivor refutes the claimed exclusion; no survivor
would not prove the full screen sound because only one population per kernel is
tested here.
"""
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "2026-09-22-r11-quotient-v1"


def rows():
    for name in (
        "r11_support8_sources_case2.json",
        "r11_support9_sources_case1.json",
        "r11_support10_sources.json",
    ):
        data = json.loads((ROOT / name).read_text())
        for row in data["feasible_rows"]:
            yield name, row


def test(name, row):
    residual = tuple(row["R"])
    edges = [tuple(edge) for edge in row["edges"]]
    k = len(residual)
    neighbours = [set() for _ in residual]
    degrees = [0] * k
    for i, j in edges:
        neighbours[i].add(j)
        neighbours[j].add(i)
        degrees[i] += 1
        degrees[j] += 1
    positive = {i for i in range(k) if degrees[i] > residual[i]}

    # Same residual-free helper semantics as check_r8_equality_supplements.py.
    free = []
    for state in itertools.product(range(2), repeat=k):
        left = {i for i, value in enumerate(state) if value == 1}
        if left & positive:
            continue
        if any(not neighbours[i] <= left for i in left):
            continue
        free.append(state)

    population = []
    for source in row["population"]:
        population.extend([tuple(source["state"])] * source["count"])

    def forced(su, u, sw, w):
        left_u = {i for i, value in enumerate(su) if value == 1}
        left_w = {i for i, value in enumerate(sw) if value == 1}
        return ({(u, i) for i in left_u if sw[i] == 0}
                | {(w, j) for j in left_w if su[j] == 0})

    failures = []
    free_witnesses = []
    for u, su in enumerate(population):
        for i, value in enumerate(su):
            if value != 1:
                continue
            if any(w != u and forced(su, u, sw, w) == {(u, i)}
                   for w, sw in enumerate(population)):
                continue
            witness = next((q for q, sw in enumerate(free)
                            if forced(su, u, sw, ("free", q)) == {(u, i)}), None)
            if witness is None:
                failures.append((u, i))
            else:
                free_witnesses.append((u, i, witness))
    return {
        "file": name,
        "key": [row.get("mask"), row.get("unit_mask"), row.get("heavy_neighbours")],
        "support": k,
        "residual_free_types": len(free),
        "population_size": len(population),
        "supplement_feasible_with_free_helpers": not failures,
        "unmet_obligations": failures,
        "free_helper_obligations": free_witnesses,
    }


out = [test(name, row) for name, row in rows()]
print(json.dumps({
    "kernels_tested": len(out),
    "reopened_witness_populations": sum(
        row["supplement_feasible_with_free_helpers"] for row in out),
    "rows": out,
    "disposition": (
        "Any reopened witness population invalidates the zero-survivor r=11 "
        "supplement conclusion under the earlier residual-free helper semantics."
    ),
}, indent=2))
