"""Independent exhaustive labelled replay of small-star certificate slack.

For every labelled graph on x<=5 witnesses, compute the minimum total
T--Z missing-incidence cost of certificate neighbourhoods covering all
present T-edges, then add twice the missing T-edge count.
"""
from itertools import combinations
import json
import sys


def solve(x):
    edges = list(combinations(range(x), 2))
    edge_count = len(edges)
    best = None
    minimizers = 0
    feasible_graphs = 0
    for graph in range(1 << edge_count):
        neighbours = [0] * x
        for k, (u, v) in enumerate(edges):
            if (graph >> k) & 1:
                neighbours[u] |= 1 << v
                neighbours[v] |= 1 << u

        certificate_types = []
        for subset in range(1, (1 << x) - 1):
            covered = 0
            for k, (u, v) in enumerate(edges):
                if not ((graph >> k) & 1):
                    continue
                if ((subset >> u) & 1) and not ((subset >> v) & 1):
                    if (neighbours[v] & subset).bit_count() == 1:
                        covered |= 1 << k
                elif ((subset >> v) & 1) and not ((subset >> u) & 1):
                    if (neighbours[u] & subset).bit_count() == 1:
                        covered |= 1 << k
            if covered:
                certificate_types.append((covered,
                                          x - subset.bit_count()))

        # Exact weighted set-cover DP over the present T-edges.  Repeating a
        # certificate neighbourhood never improves a cover, so one copy of
        # each subset type suffices even when Z has repeated neighbourhoods.
        dp = {0: 0}
        for covered, cost in certificate_types:
            new = dict(dp)
            for mask, value in dp.items():
                target = mask | covered
                new[target] = min(new.get(target, 10**9), value + cost)
            dp = new
        beta = dp.get(graph)
        if beta is None:
            continue
        feasible_graphs += 1
        slack = 2 * (edge_count - graph.bit_count()) + beta
        if best is None or slack < best:
            best = slack
            minimizers = 1
        elif slack == best:
            minimizers += 1
    return {
        "x": x,
        "labelled_graphs": 1 << edge_count,
        "certificate_cover_feasible_graphs": feasible_graphs,
        "minimum_star_slack": best,
        "minimizer_count": minimizers,
    }


def main():
    xmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(json.dumps({"method": "independent labelled graph and set-cover DP",
                      "rows": [solve(x) for x in range(3, xmax + 1)]},
                     indent=2))


if __name__ == "__main__":
    main()
