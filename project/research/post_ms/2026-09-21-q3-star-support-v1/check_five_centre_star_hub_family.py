#!/usr/bin/env python3
"""Uniform-certificate and density audit for the stronger S7-hub family."""
import json
import itertools
import random
from pathlib import Path

from check_star_support import CODES, d2c, graph
from check_five_centre_two_parameter_family import labels, lost_pairs
from maxsat_fixed_codes import maximize

COORDINATES = ["C00", "C01", "C10", "C11", "C20", "C21"]
LEAVES = ["S0", "S1", "S2", "S4"]
TYPES = COORDINATES + ["P0", "P1"] + LEAVES + ["S7"]


def build(mult):
    codes, indices = [], {}
    for kind in TYPES:
        indices[kind] = list(range(len(codes), len(codes) + mult[kind]))
        codes += [kind] * mult[kind]
    hub = indices["P1"][0]
    centre = indices["S7"][0]
    edges = [(x, y) for x in indices["P0"] for y in indices["P1"]]
    edges += [(x, hub) for kind in COORDINATES for x in indices[kind]]
    edges += [(x, centre) for kind in LEAVES for x in indices[kind]]
    return codes, edges, graph(codes, edges)


def formula(mult):
    C = sum(mult[x] for x in COORDINATES)
    A = sum(mult[x] for x in LEAVES)
    r, q = mult["P0"], mult["P1"]
    return 10 + C + A + r + q, 24 + 5 * (C + A) + 4 * (r + q) + r * q


def main():
    base = {kind: 1 for kind in TYPES}
    codes, _, adjacency = build(base)
    assert d2c(adjacency) and len(adjacency) == 22
    assert sum(map(len, adjacency)) // 2 == 83
    names = labels(codes)
    V = {kind: 9 + i for i, kind in enumerate(codes)}
    hazards = {kind: set(CODES[kind]) | {V["P1"]} for kind in COORDINATES}
    hazards["P0"] = set(CODES["P0"]) | {V["P1"]}
    hazards["P1_nonhub"] = set(CODES["P1"]) | {V["P0"]}
    for kind in LEAVES:
        hazards[kind] = set(CODES[kind]) | {V["S7"]}

    certs = []
    for x in range(len(adjacency)):
        for y in sorted(adjacency[x]):
            if x >= y:
                continue
            safe = [pair for pair in lost_pairs(adjacency, (x, y))
                    if all(not (set(pair) <= H) for H in hazards.values())]
            assert safe, (names[x], names[y])
            a, b = safe[0]
            certs.append({"edge": [names[x], names[y]],
                          "all_clone_safe_witness": [names[a], names[b]]})
    assert len(certs) == 83

    fixed_codes = COORDINATES + ["P0", "P1"] + LEAVES + ["S7"]
    maxsat = maximize(fixed_codes)
    assert maxsat["max_A_edges"] == 11

    random.seed(743)
    rows = []
    for trial in range(200):
        mult = base.copy()
        for kind in COORDINATES + ["P0", "P1"] + LEAVES:
            mult[kind] = random.randint(1, 6)
        mult["S7"] = 1
        _, _, G = build(mult)
        n, m = formula(mult)
        assert len(G) == n and sum(map(len, G)) // 2 == m and d2c(G)
        rows.append({"trial": trial, "multiplicity": mult, "n": n, "m": m})

    binary_count = 0
    cloneable = COORDINATES + ["P0", "P1"] + LEAVES
    for values in itertools.product((1, 2), repeat=len(cloneable)):
        mult = base.copy()
        mult.update(dict(zip(cloneable, values)))
        mult["S7"] = 1
        _, _, G = build(mult)
        n, m = formula(mult)
        assert len(G) == n and sum(map(len, G)) // 2 == m and d2c(G)
        binary_count += 1
    assert binary_count == 4096

    out = {
        "base": {"n": 22, "m": 83, "universal_safe_edges": len(certs)},
        "base_fixed_multiset_maxsat": maxsat,
        "certificates": certs,
        "random_combined_direct_replays": rows,
        "exhaustive_one_two_multiplicity_cube": binary_count,
        "formula": {"n": "10+C+A+r+q", "m": "24+5(C+A)+4(r+q)+rq"},
        "internal_extremum": "4n-6+floor((n-20)^2/4)",
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_STAR_HUB_FAMILY_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print("PASS: 83 universal witnesses; exact base A-maximum 11; 4096 binary and 200 random blowups")


if __name__ == "__main__":
    main()
