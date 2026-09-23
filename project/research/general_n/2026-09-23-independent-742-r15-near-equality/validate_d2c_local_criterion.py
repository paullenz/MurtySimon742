"""Independent checks for the local edge-criticality criterion used by Z3."""
import json
import subprocess
import networkx as nx


def edge_local_critical(G, i, j):
    common = set(G[i]) & set(G[j])
    if not common:
        return True
    for x in set(G[i]) - {j}:
        if x not in G[j] and (set(G[x]) & set(G[j])) == {i}:
            return True
    for x in set(G[j]) - {i}:
        if x not in G[i] and (set(G[x]) & set(G[i])) == {j}:
            return True
    return False


def edge_brute_critical(G, i, j):
    H = G.copy()
    H.remove_edge(i, j)
    return (not nx.is_connected(H)) or nx.diameter(H) > 2


checked_graphs = checked_edges = mismatches = 0
for G in nx.graph_atlas_g():
    if len(G) < 2 or not nx.is_connected(G) or nx.diameter(G) > 2:
        continue
    checked_graphs += 1
    for i, j in G.edges():
        checked_edges += 1
        if edge_local_critical(G, i, j) != edge_brute_critical(G, i, j):
            mismatches += 1

# Independently replay a satisfiable diameter-stage model.
raw = subprocess.check_output(
    ["python", "check_n18_555_d2c_z3.py", "--mode", "diameter"], text=True)
row = json.loads(raw)
H = nx.Graph()
H.add_nodes_from(range(18))
H.add_edges_from(map(tuple, row["edges"]))
degrees = [H.degree(v) for v in range(18)]
expected = [5, 5, 5, 10, 10, 10, 10, 9] + [10] * 10
fixed_ok = all(H.has_edge(i, c) for i in range(3) for c in range(8, 13))
fixed_ok &= all(not H.has_edge(i, v) for i in range(3)
                for v in list(range(3)) + list(range(3, 8)) + list(range(13, 18))
                if v != i)
fixed_ok &= all(H.has_edge(t, c) == (t - 3 == c - 8)
                for t in range(3, 8) for c in range(8, 13))

out = {
    "atlas_diameter2_graphs_checked": checked_graphs,
    "atlas_edges_checked": checked_edges,
    "criterion_mismatches": mismatches,
    "diameter_stage": {
        "degree_sequence_ok": degrees == expected,
        "fixed_geometry_ok": fixed_ok,
        "connected": nx.is_connected(H),
        "diameter": nx.diameter(H),
        "edge_count": H.number_of_edges(),
        "d2c": all(edge_brute_critical(H, i, j) for i, j in H.edges()),
        "noncritical_edge_count": sum(
            not edge_brute_critical(H, i, j) for i, j in H.edges()),
    },
}
print(json.dumps(out, indent=2))
assert mismatches == 0
assert degrees == expected and fixed_ok and nx.diameter(H) == 2
