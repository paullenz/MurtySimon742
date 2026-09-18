#!/usr/bin/env python3
"""Independent finite audit of the generic D2C edge-criticality trichotomy.

This is audit support only.  It does not prove the near-full Boolean-code
lemmas used in GLOBAL_A_EDGE_TRANSFER_AND_WITNESS_CHANNELS.md.
"""

import json
import networkx as nx


def is_d2c(G):
    if G.number_of_nodes() < 2 or not nx.is_connected(G):
        return False
    if nx.diameter(G) != 2:
        return False
    for x, y in list(G.edges()):
        H = G.copy()
        H.remove_edge(x, y)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True


def audit():
    classes = 0
    edge_checks = 0
    direct = 0
    externally_certified = 0
    witness_orientations = 0
    failures = []

    for G0 in nx.graph_atlas_g():
        n = G0.number_of_nodes()
        if n < 2 or n > 7 or not is_d2c(G0):
            continue
        classes += 1
        G = G0
        V = set(G.nodes())

        for x, y in list(G.edges()):
            edge_checks += 1
            common = set(G.neighbors(x)) & set(G.neighbors(y))
            if not common:
                direct += 1
                continue

            certs = []
            for source, head in ((x, y), (y, x)):
                for w in V - {source, head}:
                    if G.has_edge(source, w):
                        continue
                    cn = set(G.neighbors(source)) & set(G.neighbors(w))
                    if cn == {head}:
                        certs.append((source, head, w))

            if certs:
                externally_certified += 1
                witness_orientations += len(certs)
            else:
                failures.append(
                    {
                        "n": n,
                        "edge": [x, y],
                        "edges": sorted([list(e) for e in G.edges()]),
                    }
                )

    out = {
        "d2c_isomorphism_classes_through_order_7": classes,
        "edge_checks": edge_checks,
        "direct_edges": direct,
        "non_direct_externally_certified_edges": externally_certified,
        "total_witness_orientations": witness_orientations,
        "failures": len(failures),
        "failure_examples": failures[:10],
        "scope": "audit support for generic D2C critical-edge trichotomy only",
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    assert not failures
    return out


if __name__ == "__main__":
    audit()
