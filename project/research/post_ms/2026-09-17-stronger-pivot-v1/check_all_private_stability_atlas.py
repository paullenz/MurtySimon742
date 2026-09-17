#!/usr/bin/env python3
"""Graph-atlas regression for the all-private stability inequality."""

import json
import networkx as nx


def is_d2c(G):
    if G.number_of_nodes() < 3 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def main():
    out = {
        "result": "PASS",
        "atlas_max_order": 7,
        "d2c_isomorphism_classes": 0,
        "maximum_degree_triangle_roots": 0,
        "all_private_roots": 0,
        "apg_violations": 0,
        "delta_zero_all_private_roots": 0,
        "profiles": [],
    }

    for G0 in nx.graph_atlas_g():
        n = G0.number_of_nodes()
        if n < 3 or n > 7:
            continue
        G = nx.convert_node_labels_to_integers(G0)
        if not is_d2c(G):
            continue
        out["d2c_isomorphism_classes"] += 1
        Delta = max(dict(G.degree()).values())

        for v in [u for u, d in G.degree() if d == Delta]:
            B = set(G.neighbors(v))
            A = set(G.nodes()) - B - {v}
            Q = G.subgraph(B).number_of_edges()
            if Q == 0:
                continue
            out["maximum_degree_triangle_roots"] += 1
            T = {u for u in B if any(w in B for w in G.neighbors(u))}

            all_private = True
            for u in T:
                if not any((set(G.neighbors(x)) & B) == {u} for x in A):
                    all_private = False
                    break
            if not all_private:
                continue

            out["all_private_roots"] += 1
            b = len(B)
            t = len(T)
            delta = b * (n - b) - G.number_of_edges()
            lhs = t * (b - t)
            rhs = 2 * delta
            profile = {"n": n, "b": b, "t": t, "Q": Q, "delta": delta, "lhs": lhs, "rhs": rhs}
            out["profiles"].append(profile)
            if lhs > rhs:
                out["apg_violations"] += 1
                out["result"] = "FAIL"
            if delta == 0:
                out["delta_zero_all_private_roots"] += 1
                out["result"] = "FAIL"

    print(json.dumps(out, indent=2, sort_keys=True))
    if out["result"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
