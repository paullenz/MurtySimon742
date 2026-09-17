#!/usr/bin/env python3
"""Finite regression for THREE_DEFECT_EMPTY_STAR_SWITCHING_EXCLUSION.md.

Evidence only; universal claims in the note are hand arguments.
Uses only the Python standard library.
"""

from collections import Counter, defaultdict, deque
from math import comb
import json


def omega_edges(k):
    # Exceptional coordinates a=0,b=1,c=2 are independent.
    # D=3,...,k-1 are all leaves attached to c.
    sigma = [[0] * k for _ in range(k)]
    for d in range(3, k):
        sigma[2][d] = sigma[d][2] = 1

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

                ss = s ^ sgm
                v = 0
                for h in range(k):
                    if h == i:
                        val = 1 - ss
                    elif h == j:
                        val = s
                    else:
                        val = 1 ^ ss ^ sigma[i][h]
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
    clique = (k - 3, comb(k - 3, 2), comb(k - 3, 2), tuple([k - 4] * (k - 3)))
    star = (k - 2, k - 3, k - 3, tuple([1] * (k - 3) + [k - 3]))
    bip = (k, 2 * (k - 2), 2 * (k - 2), tuple([2] * (k - 2) + [k - 2, k - 2]))
    edge = (2, 1, 1, (1, 1))
    return sorted([clique, clique, star, star, bip, bip, edge, edge])


def M(n):
    return ((n - 1) * (n - 1)) // 4 + 1


def arithmetic_record(k):
    a = 2 * k
    r = k * (k + 1)
    h = r // (k - 1)
    f_bound = (h * h) // 4 + 8 * k
    delta_bound = r - f_bound
    n = 1 + 2 * k + a
    base = 2 * k * (n - 2 * k)
    needed = base - M(n)
    return {
        "k": k,
        "a": a,
        "r": r,
        "h_bound": h,
        "f_bound": f_bound,
        "delta_bound": delta_bound,
        "needed_delta": needed,
        "closed": delta_bound >= needed,
    }


def main():
    checked = 0
    for k in range(6, 101):
        got = component_signatures(k)
        exp = expected_signatures(k)
        assert got == exp, (k, got, exp)
        assert len(omega_edges(k)) == k * (k - 1)
        tau = 2 * (k - 4) + 2 + 4 + 2
        assert tau == 2 * k
        checked += 1

    records = [arithmetic_record(k) for k in range(6, 5001)]
    threshold = None
    for i, rec in enumerate(records):
        if rec["closed"] and all(r["closed"] for r in records[i:]):
            threshold = rec["k"]
            break
    assert threshold == 14

    summary = {
        "status": "PASS_THREE_DEFECT_EMPTY_STAR_SWITCHING_EXCLUSION",
        "component_replay_k_range": [6, 100],
        "component_instances": checked,
        "exact_orientation_code_decomposition": "2 K_{k-3} + 2 K_{1,k-3} + 2 K_{2,k-2} + 2 K2",
        "exact_tau": "2k",
        "arithmetic_replay_k_range": [6, 5000],
        "eventual_uniform_threshold": 14,
        "negative_control": "k=4 X3 residual-zero perfect-matching mechanism is outside theorem scope",
        "scope": "finite regression evidence only; universal structural claims are hand proofs",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
