#!/usr/bin/env python3
from collections import Counter, defaultdict


def sigma_nonstar(k):
    s = [[0] * k for _ in range(k)]
    for d in range(3, k):
        s[0][d] = s[d][0] = 1
    s[1][2] = s[2][1] = 1
    return s


def orient_code(s, source, target, source_bit):
    k = len(s)
    target_bit = source_bit ^ s[source][target]
    c = [0] * k
    c[source] = 1 - source_bit
    c[target] = target_bit
    for h in range(k):
        if h not in (source, target):
            c[h] = 1 - source_bit ^ s[source][h]
    return tuple(c)


def omega_edges(k):
    s = sigma_nonstar(k)
    out = []
    for i in range(k):
        for j in range(i + 1, k):
            for bit_j in (0, 1):
                bit_i = bit_j ^ s[i][j]
                out.append((orient_code(s, j, i, bit_j),
                            orient_code(s, i, j, bit_i),
                            (i, j, bit_j)))
    return out


def components(adj):
    seen = set()
    out = []
    for start in adj:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        comp = set()
        while stack:
            u = stack.pop()
            comp.add(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        out.append(comp)
    return out


def check_decomposition(k):
    edges = omega_edges(k)
    adj = defaultdict(set)
    multiplicity = Counter()
    for u, v, _ in edges:
        assert u != v
        adj[u].add(v)
        adj[v].add(u)
        multiplicity[tuple(sorted((u, v)))] += 1

    comps = components(adj)
    sizes = sorted(map(len, comps))
    assert sizes == sorted([k - 3, k - 3, 2 * k - 4, 2 * k - 4, 2 * k - 4])

    cliques = double_stars = 0
    for comp in comps:
        degs = sorted((len(adj[u] & comp) for u in comp), reverse=True)
        if len(comp) == k - 3 and degs == [k - 4] * (k - 3):
            cliques += 1
        elif (len(comp) == 2 * k - 4 and
              degs == [k - 2, k - 2] + [1] * (2 * k - 6)):
            double_stars += 1
        else:
            raise AssertionError((k, len(comp), degs))

    assert (cliques, double_stars) == (2, 3)
    md = Counter(multiplicity.values())
    assert md[2] == 3
    assert set(md) <= {1, 2}
    assert len(edges) == k * (k - 1)

    tau = 2 * (k - 4) + 3 * 2
    assert tau == 2 * k - 2
    return {
        "nodes": len(adj),
        "simple_edges": sum(map(len, adj.values())) // 2,
        "physical_edges": len(edges),
        "component_sizes": sizes,
        "tau": tau,
    }


def defect_lb(k, lam):
    r = k * (k - lam)
    h = {1: k, 0: k + 1, -1: k + 2}[lam]
    exceptional_bound = 8 - 2 * lam
    return r - (h * h // 4) - exceptional_bound * k


def required_defect(k, lam):
    return {1: 2 * k - 2, 0: 2 * k - 1, -1: 2 * k - 1}[lam]


def main():
    first = last = None
    for k in range(5, 101):
        rec = check_decomposition(k)
        if first is None:
            first = rec
        last = rec

    thresholds = {}
    for lam in (1, 0, -1):
        failures = [k for k in range(8, 5001)
                    if defect_lb(k, lam) < required_defect(k, lam)]
        threshold = max(failures) + 1 if failures else 8
        thresholds[lam] = threshold
        for k in range(threshold, 5001):
            assert defect_lb(k, lam) >= required_defect(k, lam)

    assert thresholds == {1: 12, 0: 14, -1: 16}
    print("PASS_NONSTAR_ONE_DEFECT_SWITCHING_EXCLUSION")
    print("decomposition k=5..100; first=", first, "last=", last)
    print("defect thresholds through k=5000:", thresholds)


if __name__ == "__main__":
    main()
