#!/usr/bin/env python3
"""Direct replay and uniform-witness audit for the five-centre P1-twin family."""
import json
from pathlib import Path

from check_star_support import d2c, graph


def build(q):
    codes = ["C00", "C01", "C10", "C11", "C20", "C21"]
    codes += ["P1"] * q + ["S0", "S1", "S2", "S4", "S7"]
    hub = 6
    star = 6 + q
    A_edges = [(i, hub) for i in range(6)]
    A_edges += [(star, star + 4), (star + 1, star + 3), (star + 2, star + 3)]
    return codes, A_edges, graph(codes, A_edges)


def base_witness_audit(adjacency):
    n = len(adjacency)

    def within_two(a, b):
        return b in adjacency[a] or bool(adjacency[a] & adjacency[b])

    checked = 0
    for a in range(n):
        for b in sorted(adjacency[a]):
            if a >= b:
                continue
            adjacency[a].remove(b)
            adjacency[b].remove(a)
            lost = [
                (x, y)
                for x in range(n)
                for y in range(x + 1, n)
                if not within_two(x, y)
            ]
            safe = [
                (x, y)
                for x, y in lost
                if not (
                    x < 8 and y < 8
                    and x.bit_count() % 2 == 1
                    and y.bit_count() % 2 == 1
                )
            ]
            adjacency[a].add(b)
            adjacency[b].add(a)
            assert safe, (a, b, lost)
            checked += 1
    return checked


def main():
    rows = []
    for q in range(1, 21):
        codes, A_edges, adjacency = build(q)
        assert d2c(adjacency)
        n = len(adjacency)
        m = sum(map(len, adjacency)) // 2
        assert n == 20 + q and m == 4 * n - 7
        rows.append({"q": q, "n": n, "m": m, "direct_D2C_replay": True})
    _, _, base = build(1)
    witness_count = base_witness_audit(base)
    assert witness_count == 77
    out = {
        "family": "six coordinate codes, q P1 vertices, centres {0,1,2,4,7}",
        "formula": {"n": "20+q", "m": "4n-7"},
        "base_edges_with_twin_safe_witness": witness_count,
        "direct_replay_rows": rows,
        "status": "PASS",
    }
    path = Path(__file__).with_name("FIVE_CENTRE_FAMILY_RESULTS.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"PASS: {len(rows)} D2C members; {witness_count} twin-safe base witnesses")


if __name__ == "__main__":
    main()
