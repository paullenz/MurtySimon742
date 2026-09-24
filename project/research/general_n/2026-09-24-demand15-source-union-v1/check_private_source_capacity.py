"""Regression for the common-endpoint private-source capacity lemma."""
import itertools
import json
import sys

import screen_hall_envelope as hall
from check_source_union_charge import complete_bipartite, x3


def inspect_root(adj, root):
    n = len(adj)
    Delta = adj[root].bit_count()
    B = [u for u in range(n) if (adj[root] >> u) & 1]
    A = [i for i in range(n) if i != root and not ((adj[root] >> i) & 1)]
    C = {i: {u for u in B if (adj[i] >> u) & 1} for i in A}
    source = {}
    for i in A:
        for t in B:
            if (adj[i] >> t) & 1:
                continue
            common = adj[i] & adj[t]
            if common.bit_count() == 1:
                u = common.bit_length() - 1
                if u in C[i]:
                    source[i, t] = u
    out = {"label_subsets": 0, "nonempty_common_endpoint_families": 0,
           "common_endpoints": 0, "violations": 0,
           "containment_with_common_endpoint": 0,
           "degree_capacity_tight": 0, "coarse_capacity_tight": 0,
           "maximum_common_endpoints": 0, "minimum_degree_capacity_slack": None,
           "minimum_coarse_capacity_slack": None}
    for r in range(2, min(8, len(A)) + 1):
        for J in itertools.combinations(A, r):
            out["label_subsets"] += 1
            common_ts = []
            for t in B:
                if not all((i, t) in source for i in J):
                    continue
                sources = {source[i, t] for i in J}
                if len(sources) == r:
                    common_ts.append(t)
            if not common_ts:
                continue
            out["nonempty_common_endpoint_families"] += 1
            out["common_endpoints"] += len(common_ts)
            out["maximum_common_endpoints"] = max(out["maximum_common_endpoints"],
                                                   len(common_ts))
            private = {}
            for i in J:
                others = set().union(*(C[j] for j in J if j != i))
                private[i] = C[i] - others
            containment = any(not private[i] for i in J)
            out["containment_with_common_endpoint"] += containment
            degree_cap = min(sum(adj[u].bit_count() - 2 for u in private[i])
                             for i in J)
            coarse_cap = (Delta - 2) * min(len(private[i]) for i in J)
            ds = degree_cap - len(common_ts)
            cs = coarse_cap - len(common_ts)
            out["degree_capacity_tight"] += ds == 0
            out["coarse_capacity_tight"] += cs == 0
            out["minimum_degree_capacity_slack"] = (ds if out["minimum_degree_capacity_slack"] is None
                                                     else min(out["minimum_degree_capacity_slack"], ds))
            out["minimum_coarse_capacity_slack"] = (cs if out["minimum_coarse_capacity_slack"] is None
                                                     else min(out["minimum_coarse_capacity_slack"], cs))
            out["violations"] += containment or ds < 0 or cs < 0
    return out


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
    keys = ["label_subsets", "nonempty_common_endpoint_families", "common_endpoints",
            "violations", "containment_with_common_endpoint", "degree_capacity_tight",
            "coarse_capacity_tight"]
    totals = {key: 0 for key in keys}
    totals.update({"graphs": 0, "maximum_degree_roots": 0,
                   "maximum_common_endpoints": 0,
                   "minimum_degree_capacity_slack": None,
                   "minimum_coarse_capacity_slack": None})
    controls = {}
    for name, adj in corpus:
        assert hall.fully_certified(adj)
        totals["graphs"] += 1
        Delta = max(x.bit_count() for x in adj)
        rows = []
        for root, mask in enumerate(adj):
            if mask.bit_count() != Delta:
                continue
            row = inspect_root(adj, root)
            rows.append(row)
            totals["maximum_degree_roots"] += 1
            for key in keys:
                totals[key] += row[key]
            totals["maximum_common_endpoints"] = max(totals["maximum_common_endpoints"],
                                                       row["maximum_common_endpoints"])
            for key in ("minimum_degree_capacity_slack", "minimum_coarse_capacity_slack"):
                if row[key] is not None:
                    totals[key] = row[key] if totals[key] is None else min(totals[key], row[key])
        if name in {"K5,5", "K5,6", "K6,6", "K6,7", "X3"}:
            controls[name] = rows
    print(json.dumps({"seed_count": seeds, "generated_orders": [8, 26],
                      "subset_cap": 8, "totals": totals, "controls": controls}, indent=2))
    assert totals["violations"] == 0


if __name__ == "__main__":
    main()
