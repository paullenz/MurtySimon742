#!/usr/bin/env python3
"""Independent replay of the edge-criticality characterization used by Z3."""

import json
import networkx as nx


def direct_edge_critical(G, x, y):
    H = G.copy()
    H.remove_edge(x, y)
    return not nx.is_connected(H) or nx.diameter(H) > 2


def unique_common(G, a, z, w):
    return (not G.has_edge(a, z)
            and G.has_edge(a, w)
            and G.has_edge(z, w)
            and (set(G[a]) & set(G[z])) == {w})


def characterized_edge_critical(G, x, y):
    if not (set(G[x]) & set(G[y])):
        return True
    for z in G:
        if z in (x, y):
            continue
        if unique_common(G, x, z, y) or unique_common(G, y, z, x):
            return True
    return False


def main():
    graphs = edges = mismatches = d2c = 0
    for G in nx.graph_atlas_g():
        if len(G) < 2 or not nx.is_connected(G) or nx.diameter(G) > 2:
            continue
        graphs += 1
        all_critical = True
        for x, y in G.edges():
            edges += 1
            direct = direct_edge_critical(G, x, y)
            formula = characterized_edge_critical(G, x, y)
            if direct != formula:
                mismatches += 1
            all_critical &= direct
        d2c += int(all_critical)
    print(json.dumps({
        "diameter_two_graphs": graphs,
        "edges_checked": edges,
        "d2c_graphs": d2c,
        "characterization_mismatches": mismatches,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
