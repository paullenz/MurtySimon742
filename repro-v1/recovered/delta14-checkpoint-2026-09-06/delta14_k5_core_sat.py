#!/usr/bin/env python3
"""Necessary-condition SAT encoder for Delta(G)=14, k=5 fixed cores.

The fixed graph F has ten vertices, e(F)=r+3 and maximum degree exactly four.
This is a conservative extension of the audited k=7 encoder.  It adds only two
project lemmas that were established after that package was frozen:

* an inactive source cannot meet a component P with 2e(P)>r;
* y(b,a,w) implies rho_b+rho_w >= d_F(a).

All encoded conditions are necessary.  Hence UNSAT excludes a fixed core,
whereas SAT only identifies a survivor of the relaxation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from itertools import combinations
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver


N_A = 10
N_B = 14


def decode_graph6(line: str) -> set[tuple[int, int]]:
    """Decode the ordinary (n<=62) graph6 representation used by geng."""
    line = line.strip()
    if not line or line.startswith(">>"):
        raise ValueError("not an ordinary graph6 record")
    n = ord(line[0]) - 63
    if n != N_A:
        raise ValueError(f"expected {N_A} vertices, found {n}")
    bits = []
    for char in line[1:]:
        value = ord(char) - 63
        if not 0 <= value < 64:
            raise ValueError("invalid graph6 byte")
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    edges: set[tuple[int, int]] = set()
    cursor = 0
    for upper in range(1, n):
        for lower in range(upper):
            if bits[cursor]:
                edges.add((lower, upper))
            cursor += 1
    return edges


def graph_data(edges: set[tuple[int, int]]):
    neighbors = [set() for _ in range(N_A)]
    for a, u in edges:
        if not (0 <= a < u < N_A):
            raise ValueError(f"non-canonical edge {(a, u)}")
        neighbors[a].add(u)
        neighbors[u].add(a)
    degrees = [len(row) for row in neighbors]

    unseen = set(range(N_A))
    components = []
    while unseen:
        root = min(unseen)
        stack = [root]
        vertices = set()
        unseen.remove(root)
        while stack:
            vertex = stack.pop()
            vertices.add(vertex)
            for other in neighbors[vertex]:
                if other in unseen:
                    unseen.remove(other)
                    stack.append(other)
        component_edges = {
            edge for edge in edges if edge[0] in vertices and edge[1] in vertices
        }
        components.append({
            "vertices": tuple(sorted(vertices)),
            "edges": tuple(sorted(component_edges)),
        })
    components.sort(key=lambda item: (len(item["vertices"]), item["vertices"]))
    component_of = {
        vertex: component
        for component in components
        for vertex in component["vertices"]
    }
    return neighbors, degrees, components, component_of


def add_exactly_one_pairwise(cnf: CNF, literals):
    literals = list(literals)
    cnf.append(literals)
    for first, second in combinations(literals, 2):
        cnf.append([-first, -second])


def extend_card(cnf: CNF, card):
    cnf.extend(card.clauses)


def build(edges: set[tuple[int, int]], r: int, *,
          expected_delta_f: int = 4,
          add_component_lemmas: bool = True,
          add_supplement_cost: bool = True,
          add_orientation_capacity: bool = True,
          add_direct_fixed_labels: bool = True,
          add_orientation_blocking: bool = True,
          add_active_first: bool = True,
          add_rho_ordering: bool = True,
          add_rho_selectors: bool = False,
          add_min_b: bool = True,
          add_dom_b: bool = True,
          rho_pattern=None,
          inactive_masks=None):
    neighbors, degrees, components, component_of = graph_data(edges)
    if len(edges) != r + 3:
        raise ValueError(f"expected {r+3} F-edges, found {len(edges)}")
    if max(degrees) != expected_delta_f:
        raise ValueError(
            f"expected Delta(F)={expected_delta_f}, found {max(degrees)}"
        )

    pool = IDPool()
    x = {(a, b): pool.id(("x", a, b)) for a in range(N_A) for b in range(N_B)}
    z = {(a, b): pool.id(("z", a, b)) for a in range(N_A) for b in range(N_B)}
    h = {(b, w): pool.id(("h", b, w))
         for b in range(N_B) for w in range(b + 1, N_B)}
    y = {(b, a, w): pool.id(("y", b, a, w))
         for b in range(N_B) for a in range(N_A)
         for w in range(N_B) if w != b}
    active = {b: pool.id(("active", b)) for b in range(N_B)}
    oriented = {(b, w): pool.id(("oriented", b, w))
                for b in range(N_B) for w in range(N_B) if w != b}

    def hv(b, w):
        return h[(b, w)] if b < w else h[(w, b)]

    cnf = CNF()
    family_counts = {}

    def finish(name, before):
        family_counts[name] = len(cnf.clauses) - before

    before = len(cnf.clauses)
    for a in range(N_A):
        for b in range(N_B):
            candidates = [z[(a, b)]] + [y[(b, a, w)] for w in range(N_B) if w != b]
            for literal in candidates:
                cnf.append([-literal, x[(a, b)]])
            cnf.append([-x[(a, b)]] + candidates)
            for first, second in combinations(candidates, 2):
                cnf.append([-first, -second])
    finish("cross_edge_partition", before)

    before = len(cnf.clauses)
    for b in range(N_B):
        residuals = [z[(a, b)] for a in range(N_A)]
        for literal in residuals:
            cnf.append([-literal, active[b]])
        cnf.append([-active[b]] + residuals)
        for w in range(N_B):
            if w == b:
                continue
            assignments = [y[(b, a, w)] for a in range(N_A)]
            for literal in assignments:
                cnf.append([-literal, oriented[(b, w)]])
            cnf.append([-oriented[(b, w)]] + assignments)
    if add_active_first:
        for b in range(N_B - 1):
            cnf.append([-active[b + 1], active[b]])
    if add_rho_ordering:
        # B is fully symmetric.  Relabel it so residual degrees are
        # nonincreasing.  The cardinal inequality is
        # rho_b + (10-rho_{b+1}) >= 10.
        for b in range(N_B - 1):
            ordered_literals = [z[(a, b)] for a in range(N_A)]
            ordered_literals += [-z[(a, b + 1)] for a in range(N_A)]
            extend_card(cnf, CardEnc.atleast(
                lits=ordered_literals, bound=N_A, vpool=pool,
                encoding=EncType.seqcounter
            ))
    finish("activity_orientation_definitions_and_symmetry", before)

    before = len(cnf.clauses)
    if rho_pattern is not None:
        if sum(rho_pattern) != r or any(value <= 0 for value in rho_pattern):
            raise ValueError("rho_pattern must be a positive partition of r")
        if tuple(rho_pattern) != tuple(sorted(rho_pattern, reverse=True)):
            raise ValueError("rho_pattern must be nonincreasing")
        if len(rho_pattern) > N_B:
            raise ValueError("too many residual-active vertices")
        for b in range(N_B):
            target = rho_pattern[b] if b < len(rho_pattern) else 0
            extend_card(cnf, CardEnc.equals(
                lits=[z[(a, b)] for a in range(N_A)], bound=target,
                vpool=pool, encoding=EncType.seqcounter
            ))
        if inactive_masks is not None:
            if len(inactive_masks) != N_B - len(rho_pattern):
                raise ValueError("one inactive mask is required per inactive vertex")
            for offset, mask in enumerate(inactive_masks):
                b = len(rho_pattern) + offset
                if not mask:
                    raise ValueError("inactive A-neighbourhood must be nonempty")
                selected_vertices = {
                    vertex for component_index in mask
                    for vertex in components[component_index]["vertices"]
                }
                for a in range(N_A):
                    cnf.append([x[(a, b)]] if a in selected_vertices
                               else [-x[(a, b)]])
    finish("fixed_residual_and_inactive_pattern", before)

    before = len(cnf.clauses)
    rho_selectors = {}
    if add_rho_selectors:
        for b in range(N_B):
            literals = [z[(a, b)] for a in range(N_A)]
            for value in range(N_A + 1):
                selector = pool.id(("rho_equals", b, value))
                rho_selectors[(b, value)] = selector
                equality = CardEnc.equals(
                    lits=literals, bound=value, vpool=pool,
                    encoding=EncType.seqcounter
                )
                for clause in equality.clauses:
                    cnf.append([-selector] + clause)
    finish("residual_degree_selectors", before)

    before = len(cnf.clauses)
    for b, w in combinations(range(N_B), 2):
        candidates = [h[(b, w)]]
        candidates += [y[(b, a, w)] for a in range(N_A)]
        candidates += [y[(w, a, b)] for a in range(N_A)]
        add_exactly_one_pairwise(cnf, candidates)
    finish("missing_B_pair_bijection", before)

    before = len(cnf.clauses)
    extend_card(cnf, CardEnc.equals(
        lits=list(z.values()), bound=r, vpool=pool, encoding=EncType.totalizer
    ))
    finish("residual_count", before)

    before = len(cnf.clauses)
    for a in range(N_A):
        extend_card(cnf, CardEnc.atleast(
            lits=[x[(a, b)] for b in range(N_B)], bound=degrees[a],
            vpool=pool, encoding=EncType.seqcounter
        ))
    for b in range(N_B):
        if add_min_b:
            degree_literals = [x[(a, b)] for a in range(N_A)]
            degree_literals += [hv(b, w) for w in range(N_B) if w != b]
            extend_card(cnf, CardEnc.atleast(
                lits=degree_literals, bound=10, vpool=pool,
                encoding=EncType.seqcounter
            ))
        cnf.append([x[(a, b)] for a in range(N_A)])
    finish("minimum_degree_and_v_distance_two", before)

    before = len(cnf.clauses)
    if add_orientation_capacity:
        # s_b <= 3+rho_b is equivalent to
        # s_b + (10-rho_b) <= 13.
        for b in range(N_B):
            incoming = [oriented[(w, b)] for w in range(N_B) if w != b]
            nonresidual_slots = [-z[(a, b)] for a in range(N_A)]
            extend_card(cnf, CardEnc.atmost(
                lits=incoming + nonresidual_slots, bound=13,
                vpool=pool, encoding=EncType.seqcounter
            ))
    finish("orientation_capacity", before)

    before = len(cnf.clauses)
    for b in range(N_B):
        for a in range(N_A):
            for w in range(N_B):
                if w == b:
                    continue
                yy = y[(b, a, w)]
                cnf.append([-yy, -x[(a, w)]])
                for u in neighbors[a]:
                    cnf.append([-yy, x[(u, b)]])
                if add_dom_b:
                    for c in range(N_B):
                        if c != b and c != w:
                            cnf.append([-yy, hv(b, c), x[(a, c)]])
    finish("quasi_edge_domination", before)

    before = len(cnf.clauses)
    if add_component_lemmas:
        for b in range(N_B):
            active_b = [z[(a, b)] for a in range(N_A)]
            for component in components:
                vertices = component["vertices"]
                inaccessible = len(vertices) > r or 2 * len(component["edges"]) > r
                if inaccessible:
                    for a in vertices:
                        cnf.append(active_b + [-x[(a, b)]])
                else:
                    anchor = vertices[0]
                    for a in vertices[1:]:
                        cnf.append(active_b + [-x[(anchor, b)], x[(a, b)]])
                        cnf.append(active_b + [x[(anchor, b)], -x[(a, b)]])

            for a in range(N_A):
                if len(component_of[a]["vertices"]) == 1:
                    continue
                for w in range(N_B):
                    if w != b:
                        active_w = [z[(u, w)] for u in range(N_A)]
                        cnf.append([-y[(b, a, w)]] + active_b + active_w)
    finish("component_and_residual_label_lemmas", before)

    before = len(cnf.clauses)
    if add_direct_fixed_labels:
        # If inactive b uses b-a with supplement w in a nontrivial component,
        # fixed labels force w adjacent to all other vertices of that component.
        # For F-neighbours u of a that forced edge w-u is residual.
        for b in range(N_B):
            active_b = [z[(u, b)] for u in range(N_A)]
            for a in range(N_A):
                component = component_of[a]
                if len(component["vertices"]) == 1:
                    continue
                for w in range(N_B):
                    if w == b:
                        continue
                    yy = y[(b, a, w)]
                    for u in component["vertices"]:
                        if u == a:
                            continue
                        cnf.append([-yy] + active_b + [x[(u, w)]])
                    for u in neighbors[a]:
                        cnf.append([-yy] + active_b + [z[(u, w)]])
    finish("direct_fixed_labels", before)

    before = len(cnf.clauses)
    if add_orientation_blocking:
        # Lemma 6.5.  If inactive b misses P and b->w, then w has no
        # selected edge into P.  `oriented` and `active` abbreviate the two
        # disjunctions but do not strengthen them.
        for b in range(N_B):
            for w in range(N_B):
                if w == b:
                    continue
                for component in components:
                    anchor = component["vertices"][0]
                    for u in component["vertices"]:
                        for c in range(N_B):
                            if c == w:
                                continue
                            cnf.append([
                                -oriented[(b, w)], active[b], x[(anchor, b)],
                                -y[(w, u, c)],
                            ])
    finish("orientation_blocking", before)

    before = len(cnf.clauses)
    if add_supplement_cost:
        # Safe later lemma: y(b,a,w) => rho_b + rho_w >= d_F(a).
        # Reuse one condition per unordered B-pair and threshold rather than
        # rebuilding the same cardinal network for every A-label.
        pair_ge = {}
        for b, w in combinations(range(N_B), 2):
            literals = [z[(u, b)] for u in range(N_A)]
            literals += [z[(u, w)] for u in range(N_A)]
            for bound in range(1, 5):
                indicator = pool.id(("pair_rho_ge", b, w, bound))
                pair_ge[(b, w, bound)] = indicator
                conditional = CardEnc.atleast(
                    lits=literals, bound=bound, vpool=pool,
                    encoding=EncType.seqcounter
                )
                for clause in conditional.clauses:
                    cnf.append([-indicator] + clause)
        for b in range(N_B):
            for a in range(N_A):
                bound = degrees[a]
                if bound == 0:
                    continue
                for w in range(N_B):
                    if w == b:
                        continue
                    pair = (b, w) if b < w else (w, b)
                    cnf.append([-y[(b, a, w)], pair_ge[pair + (bound,)]])
    finish("supplement_residual_cost", before)

    maps = {
        "x": x, "z": z, "h": h, "y": y, "active": active,
        "oriented": oriented, "pool": pool,
        "rho_selectors": rho_selectors,
        "degrees": degrees, "components": components,
        "family_counts": family_counts,
    }
    return cnf, maps


def solve_record(graph6: str, r: int, solver_name: str = "cadical195", *,
                 rho_pattern=None, inactive_masks=None, expected_delta_f=4):
    edges = decode_graph6(graph6)
    cnf, maps = build(
        edges, r, rho_pattern=rho_pattern, inactive_masks=inactive_masks,
        expected_delta_f=expected_delta_f,
    )
    started = time.time()
    with Solver(name=solver_name, bootstrap_with=cnf.clauses) as solver:
        sat = solver.solve()
        model = solver.get_model() if sat else None
        stats = solver.accum_stats()
    result = {
        "graph6": graph6.strip(),
        "r": r,
        "max_degree_f": expected_delta_f,
        "f_edges": len(edges),
        "f_degrees": maps["degrees"],
        "component_profile": [
            {"vertices": len(component["vertices"]),
             "edges": len(component["edges"])}
            for component in maps["components"]
        ],
        "status": "SAT-RELAXATION" if sat else "UNSAT",
        "variables": cnf.nv,
        "clauses": len(cnf.clauses),
        "seconds": time.time() - started,
        "stats": stats,
        "cnf_sha256": hashlib.sha256(cnf.to_dimacs().encode("ascii")).hexdigest(),
        "rho_pattern": rho_pattern,
        "inactive_masks": inactive_masks,
    }
    if sat:
        true = {literal for literal in model if literal > 0}
        z = maps["z"]
        result["rho"] = [
            sum(z[(a, b)] in true for a in range(N_A)) for b in range(N_B)
        ]
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, required=True, choices=range(3, 18))
    parser.add_argument("--graph6")
    parser.add_argument("--graph6-file")
    parser.add_argument("--index", type=int, default=0)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--max-degree", type=int, default=4, choices=(3, 4))
    parser.add_argument("--cnf-out")
    parser.add_argument("--result-out")
    parser.add_argument("--rho-pattern")
    parser.add_argument("--inactive-masks")
    args = parser.parse_args()
    if bool(args.graph6) == bool(args.graph6_file):
        parser.error("supply exactly one of --graph6 or --graph6-file")
    if args.graph6_file:
        lines = [line.strip() for line in Path(args.graph6_file).read_text().splitlines()
                 if line.strip() and not line.startswith(">>")]
        graph6 = lines[args.index]
    else:
        graph6 = args.graph6
    edges = decode_graph6(graph6)
    rho_pattern = None
    if args.rho_pattern:
        rho_pattern = tuple(int(item) for item in args.rho_pattern.split(",") if item)
    inactive_masks = None
    if args.inactive_masks is not None:
        inactive_masks = [
            tuple(int(item) for item in group.split(",") if item)
            for group in args.inactive_masks.split(";")
        ]
    cnf, _ = build(
        edges, args.r, rho_pattern=rho_pattern, inactive_masks=inactive_masks,
        expected_delta_f=args.max_degree,
    )
    if args.cnf_out:
        cnf.to_file(args.cnf_out)
    result = solve_record(
        graph6, args.r, args.solver,
        rho_pattern=rho_pattern, inactive_masks=inactive_masks,
        expected_delta_f=args.max_degree,
    )
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    if args.result_out:
        Path(args.result_out).write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    main()
