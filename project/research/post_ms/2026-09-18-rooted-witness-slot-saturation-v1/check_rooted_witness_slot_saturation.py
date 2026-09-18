#!/usr/bin/env python3
import networkx as nx
import json
from collections import Counter

def is_d2c(G):
    if not nx.is_connected(G) or nx.diameter(G) != 2:
        return False
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            return False
    return True

def audit_root(G, v):
    B = set(G.neighbors(v))
    A = set(G.nodes()) - B - {v}
    bedges = list(G.subgraph(B).edges())
    omega = [(x,z) for x in B for z in A if not G.has_edge(x,z)]

    chosen = []
    for x,y in bedges:
        candidates = []
        for z in A:
            if not G.has_edge(x,z) and set(nx.common_neighbors(G,x,z)) == {y}:
                candidates.append((x,z))
            if not G.has_edge(y,z) and set(nx.common_neighbors(G,y,z)) == {x}:
                candidates.append((y,z))
        assert candidates, ("no A-witness for rooted B-edge", v, x, y)
        chosen.append(candidates[0])

    assert len(chosen) == len(set(chosen))
    unused = set(omega) - set(chosen)
    Q = len(bedges)
    r = len(omega) - Q

    # Exact B-edge Hamming / unused B-collision identity.
    H_B = 0
    for x,y in bedges:
        H_B += sum(G.has_edge(x,z) != G.has_edge(y,z) for z in A)
    C_B = sum(len(set(nx.common_neighbors(G,x,z)) & B) for x,z in unused)
    assert H_B - Q == C_B

    # Exact A-edge B-neighborhood asymmetry / unused A-collision identity.
    H_A = 0
    for y,z in G.subgraph(A).edges():
        Ny = set(G.neighbors(y)) & B
        Nz = set(G.neighbors(z)) & B
        H_A += len(Ny ^ Nz)
    C_A = sum(len(set(nx.common_neighbors(G,x,z)) & A) for x,z in unused)
    assert H_A == C_A

    # Saturation consequences.
    if r == 0:
        assert G.subgraph(A).number_of_edges() == 0
        assert nx.is_bipartite(G.subgraph(B))
        for x,y in bedges:
            assert sum(G.has_edge(x,z) != G.has_edge(y,z) for z in A) == 1
        for x,z in omega:
            common = set(nx.common_neighbors(G,x,z))
            assert len(common) == 1
            assert common <= B

    return {
        "Q": Q,
        "omega": len(omega),
        "r": r,
        "H_B": H_B,
        "H_A": H_A,
        "unused": len(unused),
    }

def make_x3():
    G = nx.Graph()
    root = "r"
    cube = [format(i, "03b") for i in range(8)]
    A = ["a0", "a1", "a2"]
    G.add_nodes_from([root] + cube + A)
    for s in cube:
        for j in range(3):
            t = list(s)
            t[j] = "1" if s[j] == "0" else "0"
            t = "".join(t)
            if s < t:
                G.add_edge(s,t)
    for s in cube:
        G.add_edge(root,s)
    for j,a in enumerate(A):
        for s in cube:
            if s[j] == "0":
                G.add_edge(a,s)
    return G

def main():
    atlas_d2c = []
    for G in nx.graph_atlas_g():
        if G.number_of_nodes() < 3 or G.number_of_nodes() > 7:
            continue
        if not nx.is_connected(G):
            continue
        if is_d2c(G):
            atlas_d2c.append(G.copy())

    totals = Counter()
    for G in atlas_d2c:
        Delta = max(dict(G.degree()).values())
        for v,d in G.degree():
            if d != Delta:
                continue
            out = audit_root(G,v)
            totals["maximum_degree_roots"] += 1
            totals["rooted_B_edges"] += out["Q"]
            totals["BA_nonedge_slots"] += out["omega"]
            totals["unused_slots"] += out["r"]
            totals["saturated_roots"] += int(out["r"] == 0)

    X = make_x3()
    assert is_d2c(X)
    xout = audit_root(X, "r")
    assert X.number_of_nodes() == 12
    assert X.number_of_edges() == 32
    assert xout == {"Q":12, "omega":12, "r":0, "H_B":12, "H_A":0, "unused":0}

    summary = {
        "atlas_D2C_classes_through_order_7": len(atlas_d2c),
        **dict(totals),
        "X3": xout,
        "failures": 0,
        "trust_boundary": "finite audit only; promoted results are hand proofs",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
