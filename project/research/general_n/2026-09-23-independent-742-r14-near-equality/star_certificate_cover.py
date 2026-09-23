import itertools
import json
import sys

import numpy as np
import networkx as nx
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


def edge_list(x):
    return list(itertools.combinations(range(x), 2))


def certificate_mask(x, graph_mask, subset_mask, edges):
    # z with S=N(z) cap T certifies tu only when one endpoint is outside S,
    # the other lies in S, and the outside endpoint has exactly one
    # neighbour in S.
    neighbours = [0] * x
    for k, (u, v) in enumerate(edges):
        if graph_mask >> k & 1:
            neighbours[u] |= 1 << v
            neighbours[v] |= 1 << u
    out = 0
    for k, (u, v) in enumerate(edges):
        if not (graph_mask >> k & 1):
            continue
        if (subset_mask >> u & 1) and not (subset_mask >> v & 1):
            if (neighbours[v] & subset_mask).bit_count() == 1:
                out |= 1 << k
        elif (subset_mask >> v & 1) and not (subset_mask >> u & 1):
            if (neighbours[u] & subset_mask).bit_count() == 1:
                out |= 1 << k
    return out


def cover_cost(x, graph_mask, max_certificates):
    edges = edge_list(x)
    graph_edges = [k for k in range(len(edges)) if graph_mask >> k & 1]
    types = []
    for s in range(1, (1 << x) - 1):
        mask = certificate_mask(x, graph_mask, s, edges)
        if mask:
            types.append((s, x - s.bit_count(), mask))
    if not graph_edges:
        return 0, []
    n = len(types)
    A = lil_matrix((len(graph_edges) + 1, n), dtype=float)
    for row, edge in enumerate(graph_edges):
        for j, (_, _, mask) in enumerate(types):
            if mask >> edge & 1:
                A[row, j] = 1
    A[-1, :] = 1
    lo = np.r_[np.ones(len(graph_edges)), -np.inf]
    hi = np.r_[np.full(len(graph_edges), np.inf), max_certificates]
    result = milp(
        np.array([cost for _, cost, _ in types], dtype=float),
        integrality=np.ones(n, dtype=int),
        bounds=Bounds(np.zeros(n), np.ones(n)),
        constraints=LinearConstraint(A.tocsr(), lo, hi),
        options={"presolve": True},
    )
    if result.fun is None:
        return None, []
    chosen = [
        {"S": [u for u in range(x) if s >> u & 1], "cost": cost}
        for value, (s, cost, _) in zip(result.x, types) if value > .5
    ]
    return round(result.fun), chosen


def screen(x=7, max_missing=3, max_certificates=6):
    edges = edge_list(x)
    complete = (1 << len(edges)) - 1
    best = None
    rows = []
    for missing_count in range(max_missing + 1):
        for missing in itertools.combinations(range(len(edges)), missing_count):
            missing_mask = sum(1 << k for k in missing)
            graph = complete ^ missing_mask
            beta, chosen = cover_cost(x, graph, max_certificates)
            if beta is None:
                continue
            slack = 2 * missing_count + beta
            row = {
                "missing_edges": [edges[k] for k in missing],
                "certificate_cost": beta,
                "star_slack": slack,
                "certificates": chosen,
            }
            rows.append(row)
            if best is None or slack < best["star_slack"]:
                best = row
    return {
        "x": x,
        "max_missing": max_missing,
        "max_certificates": max_certificates,
        "graphs_tested": sum(
            len(list(itertools.combinations(edges, q)))
            for q in range(max_missing + 1)
        ),
        "feasible_certificate_graphs": len(rows),
        "minimum": best,
    }


def screen_atlas(x=7, max_certificates=6):
    edges = edge_list(x)
    atlas = [g for g in nx.graph_atlas_g() if len(g) == x]
    best = None
    rows = []
    for g in atlas:
        graph = 0
        for k, (u, v) in enumerate(edges):
            if g.has_edge(u, v):
                graph |= 1 << k
        beta, chosen = cover_cost(x, graph, max_certificates)
        if beta is None:
            continue
        missing_count = len(edges) - g.number_of_edges()
        slack = 2 * missing_count + beta
        row = {
            "edges": g.number_of_edges(),
            "missing_edges": missing_count,
            "certificate_cost": beta,
            "star_slack": slack,
            "certificates": chosen,
            "graph6": nx.to_graph6_bytes(g, header=False).decode().strip(),
        }
        rows.append(row)
        if best is None or slack < best["star_slack"]:
            best = row
    return {
        "x": x,
        "max_certificates": max_certificates,
        "unlabelled_graphs_tested": len(atlas),
        "feasible_certificate_graphs": len(rows),
        "minimum": best,
    }


if __name__ == "__main__":
    x = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    missing = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    certs = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    if len(sys.argv) > 4 and sys.argv[4] == "atlas":
        print(json.dumps(screen_atlas(x, certs), indent=2))
    else:
        print(json.dumps(screen(x, missing, certs), indent=2))
