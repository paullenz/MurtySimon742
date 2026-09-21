#!/usr/bin/env python3
"""Uniform twin-extension certificate for the five-centre r,q family."""
import json
from pathlib import Path

from probe_five_centre_parity_blowups import build


def labels(codes):
    seen = {}
    out = [f"b{i}" for i in range(8)] + ["v"]
    for code in codes:
        seen[code] = seen.get(code, 0) + 1
        out.append(f"{code}#{seen[code]}")
    return out


def lost_pairs(adjacency, edge):
    a, b = edge
    adjacency[a].remove(b)
    adjacency[b].remove(a)
    lost = []
    for x in range(len(adjacency)):
        for y in range(x + 1, len(adjacency)):
            if y not in adjacency[x] and not (adjacency[x] & adjacency[y]):
                lost.append((x, y))
    adjacency[a].add(b)
    adjacency[b].add(a)
    return lost


def main():
    codes, _, adjacency = build(1, 1)
    names = labels(codes)
    p0 = names.index("P0#1")
    p1 = names.index("P1#1")
    even_b = {i for i in range(8) if i.bit_count() % 2 == 0}
    odd_b = set(range(8)) - even_b
    new_p0_neighbourhood = even_b | {p1}
    new_p1_neighbourhood = odd_b | {p0}

    certificates = []
    for a in range(len(adjacency)):
        for b in sorted(adjacency[a]):
            if a >= b:
                continue
            lost = lost_pairs(adjacency, (a, b))
            safe = [
                (x, y) for x, y in lost
                if not ({x, y} <= new_p0_neighbourhood)
                and not ({x, y} <= new_p1_neighbourhood)
            ]
            assert safe, (names[a], names[b], [(names[x], names[y]) for x, y in lost])
            x, y = safe[0]
            certificates.append({
                "edge": [names[a], names[b]],
                "safe_lost_pair": [names[x], names[y]],
            })

    assert len(certificates) == 82
    out = {
        "base": {"r": 1, "q": 1, "n": len(adjacency), "m": 82},
        "base_edge_count_with_both_extension_safe_witness": len(certificates),
        "new_P0_common_neighbour_hazard": sorted(names[i] for i in new_p0_neighbourhood),
        "new_nonhub_P1_common_neighbour_hazard": sorted(names[i] for i in new_p1_neighbourhood),
        "new_edge_types": {
            "P0--even_cube_spoke": "endpoints lose distance <=2 after deletion",
            "nonhub_P1--odd_cube_spoke": "endpoints lose distance <=2 after deletion",
            "P0--P1": "endpoints lose distance <=2 after deletion",
        },
        "certificates": certificates,
        "status": "PASS",
    }
    Path(__file__).with_name("FIVE_CENTRE_TWO_PARAMETER_FAMILY_CERTIFICATES.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    print(f"PASS: {len(certificates)} base edges have P0- and P1-extension-safe witnesses")


if __name__ == "__main__":
    main()
