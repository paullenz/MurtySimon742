#!/usr/bin/env python3
"""Finite regression for TWO_DEFECT_ISOLATED_STAR_SWITCHING_EXCLUSION.md.

Evidence only; the universal statements in the note are hand proofs.
Uses only the Python standard library.
"""

from collections import Counter, defaultdict, deque
from math import comb
import json


def omega_edges(k):
    # Gauge: a=0 isolated, b=1 centre, D=2,...,k-1 leaves adjacent to b.
    sigma = [[0] * k for _ in range(k)]
    for d in range(2, k):
        sigma[1][d] = sigma[d][1] = 1

    out = []
    for i in range(k):
        for j in range(i + 1, k):
            sgm = sigma[i][j]
            for s in (0, 1):
                u = 0
                for h in range(k):
                    if h == j:
                        val = 1 - s
                    elif h == i:
                        val = s ^ sgm
                    else:
                        val = 1 ^ s ^ sigma[j][h]
                    u |= val << h

                t = s ^ sgm
                v = 0
                for h in range(k):
                    if h == i:
                        val = 1 - t
                    elif h == j:
                        val = s
                    else:
                        val = 1 ^ t ^ sigma[i][h]
                    v |= val << h
                out.append((u, v, (i, j, s)))
    return out


def component_signatures(k):
    edges = omega_edges(k)
    adj = defaultdict(set)
    mult = Counter()
    for u, v, _ in edges:
        adj[u].add(v)
        adj[v].add(u)
        mult[tuple(sorted((u, v)))] += 1

    seen = set()
    sigs = []
    for root in list(adj):
        if root in seen:
            continue
        q = deque([root])
        seen.add(root)
        comp = []
        while q:
            x = q.popleft()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        cset = set(comp)
        simple_edges = [e for e in mult if e[0] in cset and e[1] in cset]
        physical = sum(mult[e] for e in simple_edges)
        degs = sorted(sum(1 for y in adj[x] if y in cset) for x in comp)
        sigs.append((len(comp), len(simple_edges), physical, tuple(degs)))
    return sorted(sigs)


def expected_signatures(k):
    clique = (k - 2, comb(k - 2, 2), comb(k - 2, 2), tuple([k - 3] * (k - 2)))
    star = (k - 1, k - 2, k - 2, tuple([1] * (k - 2) + [k - 2]))
    doubled_edge = (2, 1, 2, (1, 1))
    return sorted([clique, clique, star, star, star, star, doubled_edge])


def M(n):
    return ((n - 1) * (n - 1)) // 4 + 1


def arithmetic_record(k, lam):
    a = 2 * k - lam - 1
    r = k * (k - lam)
    h = r // (k - 1)
    exceptional = 5 - 2 * lam
    f_bound = (h * h) // 4 + exceptional * k
    delta_bound = r - f_bound
    n = 1 + 2 * k + a
    base = 2 * k * (n - 2 * k)
    need = base - M(n)
    return {
        "k": k,
        "lambda": lam,
        "a": a,
        "r": r,
        "h_bound": h,
        "exceptional_bound": exceptional,
        "f_bound": f_bound,
        "delta_bound": delta_bound,
        "needed_delta": need,
        "closed": delta_bound >= need,
    }


def main():
    checked = 0
    for k in range(5, 101):
        got = component_signatures(k)
        exp = expected_signatures(k)
        assert got == exp, (k, got, exp)
        assert len(omega_edges(k)) == k * (k - 1)
        tau = 2 * (k - 3) + 4 + 1
        assert tau == 2 * k - 1
        checked += 1

    first = {}
    for lam in (0, -1):
        records = [arithmetic_record(k, lam) for k in range(5, 5001)]
        threshold = None
        for rec in records:
            k = rec["k"]
            if rec["closed"] and all(r["closed"] for r in records[k - 5 :]):
                threshold = k
                break
        first[str(lam)] = threshold

    assert first["0"] == 10
    assert first["-1"] == 12

    summary = {
        "status": "PASS_TWO_DEFECT_ISOLATED_STAR_SWITCHING_EXCLUSION",
        "component_replay_k_range": [5, 100],
        "component_instances": checked,
        "exact_orientation_code_decomposition": "2 K_{k-2} + 4 K_{1,k-2} + one doubled K2",
        "exact_tau": "2k-1",
        "arithmetic_replay_k_range": [5, 5000],
        "closure_thresholds": {"lambda_0": 10, "lambda_minus_1": 12},
        "eventual_uniform_threshold": 12,
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
        "scope": "finite regression evidence only; universal structural claims are hand proofs",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
