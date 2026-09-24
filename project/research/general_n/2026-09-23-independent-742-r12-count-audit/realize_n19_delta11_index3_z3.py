#!/usr/bin/env python3
"""Exact graph-realizability test for n=19, Delta=11 stable index 3.

The fixed profile is d=(9,6), x=(9,8), h=(9,10).  This model retains the
actual graph, distinct one-use physical source edges, diameter two, and
edge-by-edge diameter-two criticality.  SAT models are independently replayed
in NetworkX before being reported.  UNSAT is profile-specific, not a general
theorem.
"""

import json
import networkx as nx
from z3 import And, Bool, If, Implies, Not, Or, PbEq, PbLe, Solver, Sum, sat

N = 19
DELTA = 11
ROOT = 0
B = tuple(range(1, 12))
L0, L1 = 12, 13
A = tuple(range(12, 19))


def key(u, v):
    return (u, v) if u < v else (v, u)


E = {(u, v): Bool(f"e_{u}_{v}") for u in range(N) for v in range(u + 1, N)}


def edge(u, v):
    if u == v:
        return False
    return E[key(u, v)]


def unique_common(a, z, w):
    others = [Not(And(edge(a, q), edge(z, q)))
              for q in range(N) if q not in (a, z, w)]
    return And(Not(edge(a, z)), edge(a, w), edge(z, w), *others)


def build():
    s = Solver()
    s.set(timeout=300_000)

    # Maximum-degree root and strict-counterexample deficit budget.
    for b in B:
        s.add(edge(ROOT, b))
    for a in A:
        s.add(Not(edge(ROOT, a)))
    degrees = []
    for u in range(N):
        du = Sum([If(edge(u, v), 1, 0) for v in range(N) if v != u])
        degrees.append(du)
        s.add(du <= DELTA)
    s.add(Sum([DELTA - du for du in degrees]) <= 27)

    # Symmetry-normalized B-neighbour sets: |C0|=2, |C1|=1.  The private-
    # source lemma forces these sets disjoint; B symmetry permits this choice.
    C0, C1 = {1, 2}, {3}
    for b in B:
        s.add(edge(L0, b) if b in C0 else Not(edge(L0, b)))
        s.add(edge(L1, b) if b in C1 else Not(edge(L1, b)))

    # Label 0 is saturated: all nine B non-neighbours are assigned endpoints.
    assign = {}
    for t in B:
        assign[L0, t] = (t not in C0)
    # Label 1 selects eight of its ten B non-neighbours.
    a1 = {t: Bool(f"a1_{t}") for t in B}
    for t in B:
        if t in C1:
            s.add(Not(a1[t]))
    s.add(PbEq([(a1[t], 1) for t in B], 8))
    for t in B:
        assign[L1, t] = a1[t]

    # Every assigned incidence has exactly one common neighbour, lying in B.
    for i in (L0, L1):
        for t in B:
            ai = assign[i, t]
            if ai is False:
                continue
            commons_b = [And(edge(i, u), edge(t, u)) for u in B if u != t]
            s.add(Implies(ai, PbEq([(x, 1) for x in commons_b], 1)))
            for z in range(N):
                if z not in B and z not in (i, t):
                    s.add(Implies(ai, Not(And(edge(i, z), edge(t, z)))))
            s.add(Implies(ai, Not(edge(i, t))))

    # One physical B-edge can be the source edge for at most one incidence.
    for u in B:
        for t in B:
            if u >= t:
                continue
            uses = []
            for i in (L0, L1):
                ai_t = assign[i, t]
                ai_u = assign[i, u]
                if ai_t is not False:
                    uses.append(And(ai_t, edge(i, u), edge(t, u)))
                if ai_u is not False:
                    uses.append(And(ai_u, edge(i, t), edge(u, t)))
            if uses:
                s.add(PbLe([(x, 1) for x in uses], 1))

    # Diameter at most two.
    for u in range(N):
        for v in range(u + 1, N):
            s.add(Or(edge(u, v), *[And(edge(u, w), edge(w, v))
                                  for w in range(N) if w not in (u, v)]))

    # Edge-criticality characterization: deleting xy must either separate x,y
    # beyond distance two, or destroy a unique two-path x-y-z / y-x-z.
    for x in range(N):
        for y in range(x + 1, N):
            no_other_common = And(*[Not(And(edge(x, w), edge(y, w)))
                                    for w in range(N) if w not in (x, y)])
            witnesses = [no_other_common]
            for z in range(N):
                if z not in (x, y):
                    witnesses.append(unique_common(x, z, y))
                    witnesses.append(unique_common(y, z, x))
            s.add(Implies(edge(x, y), Or(*witnesses)))
    return s, degrees, a1


def replay(model, degrees, a1):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for (u, v), var in E.items():
        if bool(model.eval(var)):
            G.add_edge(u, v)
    diameter_two = nx.is_connected(G) and nx.diameter(G) <= 2
    critical = True
    for uv in list(G.edges()):
        H = G.copy()
        H.remove_edge(*uv)
        if nx.is_connected(H) and nx.diameter(H) <= 2:
            critical = False
            break
    return {
        "edges": G.number_of_edges(),
        "degree_sequence": sorted((d for _, d in G.degree()), reverse=True),
        "deficit": N * DELTA - 2 * G.number_of_edges(),
        "selected_label1": [t for t in B if bool(model.eval(a1[t]))],
        "diameter_two": diameter_two,
        "edge_critical": critical,
        "edge_list": sorted([list(e) for e in G.edges()]),
    }


def main():
    solver, degrees, a1 = build()
    status = solver.check()
    out = {"profile": "n19-Delta11-stable-index-3", "status": str(status)}
    if status == sat:
        out["replay"] = replay(solver.model(), degrees, a1)
    elif str(status) == "unknown":
        out["reason_unknown"] = solver.reason_unknown()
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
