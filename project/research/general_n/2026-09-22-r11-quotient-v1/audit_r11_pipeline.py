#!/usr/bin/env python3
"""Independent cross-file replay of the complete r=11 finite pipeline."""
import itertools
import json
from pathlib import Path


def strict_value(edges, residual, degrees):
    k = len(residual)
    neigh = [set() for _ in range(k)]
    for i, j in edges:
        neigh[i].add(j); neigh[j].add(i)
    positive = [degrees[i] > residual[i] for i in range(k)]
    capacity_ok = all(
        not positive[i] or
        (degrees[i] - residual[i]) ** 2 <= sum(residual[j] for j in neigh[i])
        for i in range(k)
    )
    e_pos = sum(positive[i] and positive[j] for i, j in edges)
    e_non = sum(not positive[i] and not positive[j] for i, j in edges)
    demand_pos = sum(residual[i] for i in range(k) if positive[i])
    slack = sum(residual[i] == 1 and degrees[i] == 0
                for i in range(k) if not positive[i])
    return capacity_ok, e_pos - e_non - demand_pos - slack


def parse_support(path, k):
    pairs = list(itertools.combinations(range(k), 2))
    rows = []
    for line in Path(path).read_text().splitlines():
        fields = list(map(int, line.split()))
        case, mask, claimed = fields[:3]
        residual = tuple(fields[3:3+k])
        degrees = tuple(fields[3+k:3+2*k])
        edges = [pair for q, pair in enumerate(pairs) if mask >> q & 1]
        recomputed = [0] * k
        for i, j in edges:
            recomputed[i] += 1; recomputed[j] += 1
        cap, value = strict_value(edges, residual, tuple(recomputed))
        assert tuple(recomputed) == degrees
        assert cap and value == claimed and value > 0
        rows.append((case, mask, residual, claimed))
    assert len(rows) == len(set(rows))
    return rows


def parse_support10(path):
    pairs = list(itertools.combinations(range(9), 2))
    rows = []
    for line in Path(path).read_text().splitlines():
        fields = list(map(int, line.split()))
        unit_mask, heavy_neighbours, claimed = fields[:3]
        residual = tuple(fields[3:13]); degrees = tuple(fields[13:23])
        edges = [(i+1, j+1) for q, (i, j) in enumerate(pairs)
                 if unit_mask >> q & 1]
        edges += [(0, i+1) for i in range(9) if heavy_neighbours >> i & 1]
        recomputed = [0] * 10
        for i, j in edges:
            recomputed[i] += 1; recomputed[j] += 1
        cap, value = strict_value(edges, residual, tuple(recomputed))
        assert tuple(recomputed) == degrees
        assert cap and value == claimed and value > 0
        assert max(degrees[1:]) <= 3 and max(
            sum(1 for j in range(1, 10) if
                tuple(sorted((i, j))) in {tuple(sorted(e)) for e in edges})
            for i in range(1, 10)) <= 2
        rows.append((unit_mask, heavy_neighbours, residual, claimed))
    assert len(rows) == len(set(rows))
    return rows


s8 = parse_support("r11_support8_masks.txt", 8)
s9 = parse_support("r11_support9_masks.txt", 9)
s10 = parse_support10("r11_support10_masks.txt")
assert [sum(r[0] == c for r in s8) for c in range(3)] == [26, 800, 1670]
assert [sum(r[0] == c for r in s9) for c in range(2)] == [125, 3148]
assert len(s10) == 280

s8_sources = [json.load(open(f"r11_support8_sources_case{i}.json")) for i in range(3)]
s9_sources = [json.load(open(f"r11_support9_sources_case{i}.json")) for i in range(2)]
s10_sources = json.load(open("r11_support10_sources.json"))
assert [(x["strict_core_orbits"], x["source_feasible"], x["solver_unknown"])
        for x in s8_sources] == [(26, 0, 0), (800, 0, 0), (1670, 16, 0)]
assert [(x["strict_core_orbits"], x["source_feasible"], x["solver_unknown"])
        for x in s9_sources] == [(125, 0, 0), (3148, 8, 0)]
assert (s10_sources["strict_core_orbits"], s10_sources["source_feasible"],
        s10_sources["solver_unknown"]) == (280, 3, 0)

s8_keys = {(r[1], r[2]) for r in s8 if r[0] == 2}
assert {(r["mask"], tuple(r["R"])) for r in s8_sources[2]["feasible_rows"]} <= s8_keys
s9_keys = {(r[1], r[2]) for r in s9 if r[0] == 1}
assert {(r["mask"], tuple(r["R"])) for r in s9_sources[1]["feasible_rows"]} <= s9_keys
s10_keys = {(r[0], r[1]) for r in s10}
assert {(r["unit_mask"], r["heavy_neighbours"])
        for r in s10_sources["feasible_rows"]} <= s10_keys

e8 = json.load(open("r11_support8_earlyexit.json"))
e9 = json.load(open("r11_support9_earlyexit.json"))
e10 = json.load(open("r11_support10_earlyexit.json"))
assert (e8["kernels"], e8["found"], e8["exhausted"], e8["truncated"]) == (16, 0, 16, 0)
assert (e9["kernels"], e9["found"], e9["exhausted"]) == (8, 0, 8)
assert (e10["kernels"], e10["found"], e10["exhausted"]) == (3, 0, 3)

print(json.dumps({
    "status": "PASS",
    "strict_rows": {"support8": len(s8), "support9": len(s9), "support10": len(s10)},
    "source_survivors": {"support8": 16, "support9": 8, "support10": 3},
    "supplement_survivors": {"support8": 0, "support9": 0, "support10": 0},
    "checks": [
        "every strict row has independently recomputed degrees",
        "every strict row satisfies local capacity and has matching positive strict value",
        "all source survivors belong to their raw strict census",
        "all source and supplement aggregates agree across files",
        "support-ten unit-induced maximum degree is at most two",
    ],
    "scope": "Independent cross-file/formula replay; it does not independently reimplement orbit isomorphism reduction or the source/supplement algorithms.",
}, indent=2))
