#!/usr/bin/env python3
"""Certificate audit for the clone-closed five-centre family."""
import json
import random
from pathlib import Path

from check_star_support import CODES, d2c, graph
from check_five_centre_two_parameter_family import labels, lost_pairs

COORDINATES = ["C00", "C01", "C10", "C11", "C20", "C21"]
TYPES = COORDINATES + ["P0", "P1", "S0", "S1", "S2", "S4", "S7"]


def build(multiplicity):
    codes = []
    indices = {}
    for kind in TYPES:
        count = multiplicity[kind]
        indices[kind] = list(range(len(codes), len(codes) + count))
        codes += [kind] * count
    edges = [(x, y) for x in indices["P0"] for y in indices["P1"]]
    hub = indices["P1"][0]
    edges += [(x, hub) for kind in COORDINATES for x in indices[kind]]
    edges += [(x, y) for x in indices["S0"] for y in indices["S7"]]
    edges += [(x, y) for kind in ("S1", "S2")
              for x in indices[kind] for y in indices["S4"]]
    return codes, edges, graph(codes, edges)


def formula(multiplicity):
    C = sum(multiplicity[kind] for kind in COORDINATES)
    r, q = multiplicity["P0"], multiplicity["P1"]
    a, b = multiplicity["S0"], multiplicity["S7"]
    c, d = multiplicity["S1"], multiplicity["S2"]
    n = 10 + C + r + q + a + b + c + d
    m = 24 + 5 * C + 4 * (r + q + a + b) + 5 * (c + d) + r * q + a * b
    return n, m


def main():
    base = {kind: 1 for kind in TYPES}
    codes, _, adjacency = build(base)
    names = labels(codes)
    vertex = {name: 9 + i for i, name in enumerate(codes)}
    hub = vertex["P1"]
    hazards = {kind: set(CODES[kind]) | {hub} for kind in COORDINATES}
    hazards["P0"] = set(CODES["P0"]) | {hub}
    hazards["P1_nonhub"] = set(CODES["P1"]) | {vertex["P0"]}
    for kind, other in (("S0", "S7"), ("S7", "S0"),
                        ("S1", "S4"), ("S2", "S4")):
        hazards[kind] = set(CODES[kind]) | {vertex[other]}

    certificates = []
    for x in range(len(adjacency)):
        for y in sorted(adjacency[x]):
            if x >= y:
                continue
            safe = [
                pair for pair in lost_pairs(adjacency, (x, y))
                if all(not (set(pair) <= neighbourhood) for neighbourhood in hazards.values())
            ]
            assert safe, (names[x], names[y])
            a, b = safe[0]
            certificates.append({"edge": [names[x], names[y]],
                                 "all_clone_safe_witness": [names[a], names[b]]})
    assert len(certificates) == 82

    random.seed(742)
    rows = []
    cloneable = COORDINATES + ["P0", "P1", "S0", "S1", "S2", "S7"]
    for trial in range(200):
        mult = base.copy()
        for kind in cloneable:
            mult[kind] = random.randint(1, 6)
        mult["S4"] = 1
        _, _, G = build(mult)
        n, m = formula(mult)
        assert len(G) == n and sum(map(len, G)) // 2 == m and d2c(G)
        rows.append({"trial": trial, "multiplicity": mult, "n": n, "m": m})

    out = {
        "base_edges_with_all_clone_safe_witness": len(certificates),
        "cloneable_types": cloneable,
        "fixed_singleton_type": "S4",
        "certificates": certificates,
        "random_combined_direct_replays": rows,
        "formula": {
            "n": "10+C+r+q+a+b+c+d",
            "m": "24+5C+4(r+q+a+b)+5(c+d)+rq+ab",
        },
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_CLONE_CLOSED_FAMILY_RESULTS.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print("PASS: 82 universally clone-safe base witnesses; 200 combined blowups")


if __name__ == "__main__":
    main()
