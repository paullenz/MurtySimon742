"""Graph-level regression for the assigned-witness source-union charge.

For a maximum-degree root v, B=N(v), and a potential certificate incidence
(i,t), record the unique B-source u with N(i) cap N(t)={u}.  At a fixed t,
an assigned set of incidences must use distinct physical edges ut, hence
distinct sources.  The checker exhausts every locally compatible subset of
size at most eight (the irreducible demand-16 label bound).
"""
import itertools
import json
import sys

import screen_hall_envelope as hall


def complete_bipartite(p, q):
    n = p + q
    adj = [0] * n
    for i in range(p):
        for j in range(p, n):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def x3():
    """Published 12-vertex X3 in its Q3-root construction."""
    # 0 is the root, 1..8 are bit strings 0..7, 9..11 are the three
    # coordinate-halfcube vertices with chosen side zero.
    n = 12
    adj = [0] * n
    def add(i, j):
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    for b in range(8):
        add(0, b + 1)
        for bit in range(3):
            c = b ^ (1 << bit)
            if b < c:
                add(b + 1, c + 1)
        for bit in range(3):
            if not ((b >> bit) & 1):
                add(9 + bit, b + 1)
    return adj


def root_subsets(adj, root):
    n = len(adj)
    Delta = adj[root].bit_count()
    a = n - 1 - Delta
    B = [u for u in range(n) if (adj[root] >> u) & 1]
    A = [i for i in range(n) if i != root and not ((adj[root] >> i) & 1)]
    C = {i: {u for u in B if (adj[i] >> u) & 1} for i in A}
    deficits = [Delta - adj[z].bit_count() for z in range(n)]
    tested = violations = source_private_failures = 0
    min_slack = None
    strict_over_pair = 0
    max_gain = None
    max_r = 0
    for t in B:
        incidences = []
        for i in A:
            if (adj[i] >> t) & 1:
                continue
            common = adj[i] & adj[t]
            if common.bit_count() != 1:
                continue
            u = common.bit_length() - 1
            if u in C[i]:
                incidences.append((i, u))
        for r in range(1, min(8, len(incidences)) + 1):
            for chosen in itertools.combinations(incidences, r):
                sources = {u for _, u in chosen}
                if len(sources) != r:
                    continue  # same physical B-edge cannot be assigned twice
                labels = [i for i, _ in chosen]
                union = set().union(*(C[i] for i in labels))
                # Every chosen source is private among these label B-neighbourhoods.
                private = all(u not in C[j]
                              for i, u in chosen for j in labels if j != i)
                source_private_failures += not private
                rhs = len(union) - a
                slack = deficits[t] - rhs
                pair_rhs = max(2 * Delta - n + 1 - deficits[i]
                               for i in labels)
                gain = rhs - pair_rhs
                tested += 1
                violations += slack < 0 or not private
                min_slack = slack if min_slack is None else min(min_slack, slack)
                strict_over_pair += gain > 0
                max_gain = gain if max_gain is None else max(max_gain, gain)
                max_r = max(max_r, r)
    return {
        "subsets": tested,
        "violations": violations,
        "source_private_failures": source_private_failures,
        "minimum_slack": min_slack,
        "strictly_stronger_than_best_pair_bound": strict_over_pair,
        "maximum_gain_over_best_pair_bound": max_gain,
        "maximum_right_degree_tested": max_r,
    }


def main():
    seeds = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    corpus = [("K5,5", complete_bipartite(5, 5)),
              ("K5,6", complete_bipartite(5, 6)),
              ("K6,6", complete_bipartite(6, 6)),
              ("K6,7", complete_bipartite(6, 7)),
              ("X3", x3())]
    for seed in range(seeds):
        for n in range(8, 27):
            corpus.append((f"greedy-{seed}-{n}", hall.greedy_d2c(n, seed)))
    totals = {
        "graphs": 0, "maximum_degree_roots": 0, "subsets": 0,
        "violations": 0, "source_private_failures": 0,
        "strictly_stronger_than_best_pair_bound": 0,
        "maximum_right_degree_tested": 0,
    }
    min_slack = max_gain = None
    controls = {}
    for name, adj in corpus:
        assert hall.fully_certified(adj)
        totals["graphs"] += 1
        D = max(x.bit_count() for x in adj)
        graph_rows = []
        for root, mask in enumerate(adj):
            if mask.bit_count() != D:
                continue
            row = root_subsets(adj, root)
            graph_rows.append(row)
            totals["maximum_degree_roots"] += 1
            for key in ("subsets", "violations", "source_private_failures",
                        "strictly_stronger_than_best_pair_bound"):
                totals[key] += row[key]
            totals["maximum_right_degree_tested"] = max(
                totals["maximum_right_degree_tested"], row["maximum_right_degree_tested"])
            if row["minimum_slack"] is not None:
                min_slack = (row["minimum_slack"] if min_slack is None else
                             min(min_slack, row["minimum_slack"]))
            if row["maximum_gain_over_best_pair_bound"] is not None:
                max_gain = (row["maximum_gain_over_best_pair_bound"] if max_gain is None else
                            max(max_gain, row["maximum_gain_over_best_pair_bound"]))
        if name in {"K5,5", "K5,6", "K6,6", "K6,7", "X3"}:
            controls[name] = graph_rows
    totals["minimum_slack"] = min_slack
    totals["maximum_gain_over_best_pair_bound"] = max_gain
    out = {
        "lemma": "for distinct-source incidences at t, sources are private and delta_t >= |union C_i|-a",
        "subset_cap": 8,
        "seed_count": seeds,
        "generated_orders": [8, 26],
        "totals": totals,
        "controls": controls,
    }
    print(json.dumps(out, indent=2))
    assert totals["violations"] == 0
    assert totals["source_private_failures"] == 0


if __name__ == "__main__":
    main()
