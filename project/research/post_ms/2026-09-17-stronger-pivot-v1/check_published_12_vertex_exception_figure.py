#!/usr/bin/env python3
"""Exact consistency check for PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md.

This script does not extract edges from the figure. It takes the explicit edge
tracing written in the companion note and verifies that it is exactly the
programmatic X_3 construction, has 32 edges, has the stated unique dominating
edge, and is diameter-2-critical.
"""

from collections import Counter, deque
from itertools import combinations, product

NAMES = ["A", "B", "C", "D", "E", "r", "G", "H", "I", "J", "K", "L"]
IDX = {x: i for i, x in enumerate(NAMES)}


def edge(u, v):
    return tuple(sorted((IDX[u], IDX[v])))


def figure_edges():
    e = set()

    # Visible Q3 edges in the published drawing.
    for u, v in [
        ("B", "C"), ("D", "E"), ("G", "H"), ("I", "J"),
        ("B", "D"), ("C", "E"), ("G", "I"), ("H", "J"),
        ("B", "G"), ("D", "I"), ("C", "H"), ("E", "J"),
    ]:
        e.add(edge(u, v))

    # Central root to all eight cube vertices.
    for x in ["B", "C", "D", "E", "G", "H", "I", "J"]:
        e.add(edge("r", x))

    # The three coordinate-zero face vertices.
    for x in ["B", "C", "G", "H"]:
        e.add(edge("A", x))
    for x in ["G", "H", "I", "J"]:
        e.add(edge("K", x))
    for x in ["C", "E", "H", "J"]:
        e.add(edge("L", x))

    return e


CUBE_COORD = {
    "H": (0, 0, 0),
    "G": (0, 0, 1),
    "C": (0, 1, 0),
    "J": (1, 0, 0),
    "B": (0, 1, 1),
    "I": (1, 0, 1),
    "E": (1, 1, 0),
    "D": (1, 1, 1),
}


def x3_edges():
    e = set()
    by_coord = {bits: name for name, bits in CUBE_COORD.items()}

    # Cube edges.
    coords = list(by_coord)
    for x, y in combinations(coords, 2):
        if sum(a != b for a, b in zip(x, y)) == 1:
            e.add(edge(by_coord[x], by_coord[y]))

    # Universal root on Q3.
    for name in CUBE_COORD:
        e.add(edge("r", name))

    # a_i adjacent to coordinate-zero face i.
    for name, bits in CUBE_COORD.items():
        if bits[0] == 0:
            e.add(edge("A", name))
        if bits[1] == 0:
            e.add(edge("K", name))
        if bits[2] == 0:
            e.add(edge("L", name))
    return e


def adjacency(edges):
    adj = [set() for _ in NAMES]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def diameter(edges):
    adj = adjacency(edges)
    worst = 0
    for s in range(len(NAMES)):
        dist = [-1] * len(NAMES)
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    q.append(v)
        if -1 in dist:
            return float("inf")
        worst = max(worst, max(dist))
    return worst


def is_dominating_edge(edges, uv):
    adj = adjacency(edges)
    u, v = uv
    return all(x in (u, v) or x in adj[u] or x in adj[v] for x in range(len(NAMES)))


def main():
    fig = figure_edges()
    x3 = x3_edges()
    assert fig == x3
    assert len(fig) == 32

    # Inner graph is exactly Q3 and outer face sets are coordinate halfcubes.
    cube_names = set(CUBE_COORD)
    cube_idx = {IDX[x] for x in cube_names}
    cube_edges = {e for e in fig if e[0] in cube_idx and e[1] in cube_idx}
    assert len(cube_edges) == 12
    for x, y in combinations(CUBE_COORD, 2):
        expect = sum(a != b for a, b in zip(CUBE_COORD[x], CUBE_COORD[y])) == 1
        assert (edge(x, y) in fig) == expect

    adj = adjacency(fig)
    degrees = sorted((len(nbrs) for nbrs in adj), reverse=True)
    assert degrees == [8, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4]

    dashed = edge("r", "H")
    dominating = sorted(e for e in fig if is_dominating_edge(fig, e))
    assert dominating == [dashed]

    assert diameter(fig) == 2
    for e in fig:
        reduced = set(fig)
        reduced.remove(e)
        assert diameter(reduced) > 2, (e, diameter(reduced))

    print({
        "status": "PASS_PUBLISHED_FIGURE_IS_X3",
        "vertices": len(NAMES),
        "edges": len(fig),
        "degree_sequence": degrees,
        "unique_dominating_edge": (NAMES[dashed[0]], NAMES[dashed[1]]),
        "diameter": 2,
        "every_edge_critical": True,
        "cube_coordinate_map": CUBE_COORD,
    })


if __name__ == "__main__":
    main()
