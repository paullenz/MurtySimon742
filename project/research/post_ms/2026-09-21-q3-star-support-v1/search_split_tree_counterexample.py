#!/usr/bin/env python3
"""Construct an actual D2C graph with two tree components in H_x."""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/workspace/scratch/a4369cb67676/deps")
from pysat.solvers import Solver

from check_star_support import d2c, graph
from maxsat_fixed_codes import encode


def main():
    k = 4
    codes = ["C00", "C01", "C10", "C11", "C20", "C21"]
    codes += sum(([s] * k for s in ("S0", "S3", "S5", "S6")), [])
    codes += ["P0"] * k + ["P1"] * k
    offset = 6 + 4 * k
    x = 6
    R = list(range(offset, offset + k))
    T = list(range(offset + k, offset + 2 * k))
    rs, ts = R[:2], T[:2]
    cnf, avars, _ = encode(codes)

    def var(i, j):
        return avars[tuple(sorted((9 + i, 9 + j)))]

    # x has exactly the selected two neighbours on each parity side.
    for y in rs + ts:
        cnf.append([var(x, y)])
    for y in R[2:] + T[2:]:
        cnf.append([-var(x, y)])

    # Two diagonal missing pairs have x as unique common A-neighbour.
    for r, t in zip(rs, ts):
        cnf.append([-var(r, t)])
        for y in range(len(codes)):
            if y not in (r, t, x):
                cnf.append([-var(r, y), -var(t, y)])

    # The cross pairs are present, so H_x consists of two disjoint edges.
    cnf.append([var(rs[0], ts[1])])
    cnf.append([var(rs[1], ts[0])])

    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        assert solver.solve()
        model = solver.get_model()
    positive = {v for v in model if v > 0}
    A_edges = [
        (u - 9, v - 9) for (u, v), variable in avars.items()
        if variable in positive
    ]
    adjacency = graph(codes, A_edges)
    assert d2c(adjacency)
    edges = {tuple(sorted(e)) for e in A_edges}

    def adjacent(i, j):
        return tuple(sorted((i, j))) in edges

    S = [i for i, code in enumerate(codes) if code.startswith("S")]
    H_data = []
    h = 0
    L = 0
    for star in S:
        bridge_degree = sum(adjacent(star, t) for t in T)
        bridge_degree += sum(
            adjacent(star, y) and codes[y] != codes[star] for y in S
        )
        if bridge_degree == 1:
            L += sum(adjacent(star, t) for t in T)
        if bridge_degree < 2:
            continue
        H_edges = [
            (r, t) for r in R for t in T
            if adjacent(r, star) and adjacent(t, star) and not adjacent(r, t)
            and {
                y for y in range(len(codes))
                if adjacent(r, y) and adjacent(t, y)
            } == {star}
        ]
        if not H_edges:
            continue
        local = {v: set() for edge in H_edges for v in edge}
        for a, b in H_edges:
            local[a].add(b)
            local[b].add(a)
        seen = set()
        components = []
        for start in local:
            if start in seen:
                continue
            stack = [start]
            seen.add(start)
            vertices = []
            while stack:
                u = stack.pop()
                vertices.append(u)
                for v in local[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            edge_count = sum(len(local[u]) for u in vertices) // 2
            is_tree = edge_count == len(vertices) - 1
            h += int(is_tree)
            components.append({
                "vertices": vertices,
                "edges": edge_count,
                "tree": is_tree,
            })
        H_data.append({
            "star": star,
            "code": codes[star],
            "bridge_degree": bridge_degree,
            "H_edges": H_edges,
            "components": components,
        })

    star_edges = sum(
        adjacent(a, b) for i, a in enumerate(S) for b in S[i + 1 :]
    )
    L += star_edges
    cross = sum(adjacent(r, t) for r in R for t in T)
    I = sum(
        adjacent(a, b)
        for side in (R, T)
        for i, a in enumerate(side) for b in side[i + 1 :]
    )
    M = len(R) * len(T) - cross
    hard = 0
    for star in S:
        bridge_degree = sum(adjacent(star, t) for t in T)
        bridge_degree += sum(
            adjacent(star, y) and codes[y] != codes[star] for y in S
        )
        hard += sum(adjacent(star, r) for r in R)
        if bridge_degree >= 2:
            hard += sum(adjacent(star, t) for t in T)
    nu = hard - h
    g = (M - I) - nu
    parity_star = sum(
        adjacent(p, s) for p in R + T for s in S
    )
    n = len(adjacency)
    m = sum(map(len, adjacency)) // 2
    out = {
        "status": "actual D2C counterexample to matching-one, one-tree-component, and h+L<=s",
        "codes": codes,
        "A_edges": A_edges,
        "n": n,
        "m": m,
        "M_n": (n - 1) ** 2 // 4 + 1,
        "deficit_from_M": (n - 1) ** 2 // 4 + 1 - m,
        "R": R,
        "T": T,
        "forced_star": x,
        "H_data": H_data,
        "h": h,
        "L": L,
        "s": len(S),
        "h_plus_L": h + L,
        "hard_obligations": hard,
        "nu": nu,
        "M": M,
        "I": I,
        "g_equals_M_minus_I_minus_nu": g,
        "corrected_condition_left": h + L,
        "corrected_condition_right": len(S) + g,
        "block_edges": cross + I + parity_star + star_edges,
        "rq_plus_s": len(R) * len(T) + len(S),
        "direct_D2C_replay": True,
    }
    assert h + L > len(S)
    assert h + L <= len(S) + g
    assert out["block_edges"] <= out["rq_plus_s"]
    path = Path(__file__).with_name("PARITY_STAR_SPLIT_TREE_COUNTEREXAMPLE.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(
        f"PASS: n={n}, m={m}, h+L={h+L}>s={len(S)}, "
        f"but h+L<={len(S)+g}=s+g and block={out['block_edges']}<=rq+s={out['rq_plus_s']}"
    )


if __name__ == "__main__":
    main()
