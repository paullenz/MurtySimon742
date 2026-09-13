#!/usr/bin/env python3
"""Exact replay for ORIENTATION_FLOW_HALL.md.

Checks:
  * the committed Ferrers/prefix counterexample;
  * target-flow max-flow == capacitated Hall over all source subsets;
  * pair-choice max-flow == pair-node Hall over all source subsets;
  * a small exhaustive family of canonical-looking profiles.

All arithmetic is integral; no external solver is used.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, cap):
        a = [v, cap, None]
        b = [u, 0, a]
        a[2] = b
        self.g[u].append(a)
        self.g[v].append(b)

    def flow(self, s, t):
        ans = 0
        n = len(self.g)
        while True:
            lev = [-1] * n
            lev[s] = 0
            dq = deque([s])
            while dq:
                u = dq.popleft()
                for v, cap, rev in self.g[u]:
                    if cap and lev[v] < 0:
                        lev[v] = lev[u] + 1
                        dq.append(v)
            if lev[t] < 0:
                return ans
            it = [0] * n

            def dfs(u, f):
                if u == t:
                    return f
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    v, cap, rev = e
                    if cap and lev[v] == lev[u] + 1:
                        got = dfs(v, min(f, cap))
                        if got:
                            e[1] -= got
                            rev[1] += got
                            return got
                    it[u] += 1
                return 0

            while True:
                got = dfs(s, 10**9)
                if not got:
                    break
                ans += got


def dmat(q, rho):
    c = [x + r for x, r in zip(q, rho)]
    n = len(q)
    return [
        [
            i != j and q[i] <= c[j] + 1 and q[j] <= c[i]
            for j in range(n)
        ]
        for i in range(n)
    ]


def target_flow(q, rho, P):
    n = len(q)
    D = dmat(q, rho)
    s = 2 * n
    t = s + 1
    F = Dinic(t + 1)
    for i in range(n):
        F.add(s, i, q[i])
    for i in range(n):
        for j in range(n):
            if D[i][j]:
                F.add(i, n + j, 1)
    for j in range(n):
        F.add(n + j, t, P[j])
    return F.flow(s, t)


def target_hall(q, rho, P):
    n = len(q)
    D = dmat(q, rho)
    best = None
    for mask in range(1, 1 << n):
        W = [i for i in range(n) if mask >> i & 1]
        lhs = sum(q[i] for i in W)
        ds = [sum(1 for i in W if D[i][j]) for j in range(n)]
        rhs = sum(min(P[j], ds[j]) for j in range(n))
        rec = (lhs - rhs, W, lhs, rhs, ds)
        if best is None or rec[0] > best[0]:
            best = rec
    return best


def pair_flow(q, rho):
    n = len(q)
    D = dmat(q, rho)
    pairs = [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if D[i][j] or D[j][i]
    ]
    s = n + len(pairs)
    t = s + 1
    F = Dinic(t + 1)
    for i in range(n):
        F.add(s, i, q[i])
    for k, (i, j) in enumerate(pairs):
        node = n + k
        if D[i][j]:
            F.add(i, node, 1)
        if D[j][i]:
            F.add(j, node, 1)
        F.add(node, t, 1)
    return F.flow(s, t)


def pair_hall(q, rho):
    n = len(q)
    D = dmat(q, rho)
    pairs = [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if D[i][j] or D[j][i]
    ]
    best = None
    for mask in range(1, 1 << n):
        W = [i for i in range(n) if mask >> i & 1]
        lhs = sum(q[i] for i in W)
        reach = 0
        for i, j in pairs:
            if ((mask >> i) & 1 and D[i][j]) or ((mask >> j) & 1 and D[j][i]):
                reach += 1
        rec = (lhs - reach, W, lhs, reach)
        if best is None or rec[0] > best[0]:
            best = rec
    return best


def old_prefix_values(q, rho, P):
    c = [x + r for x, r in zip(q, rho)]
    Q = sum(q)
    out = []
    for k in range(0, max(c + [0]) + 1):
        val = sum(q[i] for i in range(len(q)) if q[i] <= k + 1)
        val += sum(P[j] for j in range(len(q)) if c[j] > k)
        out.append((k, val, val - Q))
    return out


def canonical_caps(a, b, q, rho):
    # Deliberately omit the new K_D degree cap here: this is the basic
    # canonical/simple incoming relaxation used by the counterexample.
    return [
        max(0, min(b - 1 - q[i], rho[i] + b - a - 1))
        for i in range(len(q))
    ]


def main():
    q = [0, 1, 3, 3, 0]
    rho = [1, 1, 1, 1, 3]
    P = [1, 1, 1, 1, 3]
    Q = sum(q)
    D = dmat(q, rho)
    pref = old_prefix_values(q, rho, P)

    assert all(v >= Q for _, v, _ in pref)
    assert all(sum(D[i]) >= q[i] for i in range(len(q)))

    tf = target_flow(q, rho, P)
    th = target_hall(q, rho, P)
    pf = pair_flow(q, rho)
    ph = pair_hall(q, rho)

    assert tf == Q - max(0, th[0]) == 6
    assert th[0] == 1 and th[1] == [2, 3] and th[2:4] == (6, 5)
    assert pf == Q - max(0, ph[0]) == 6
    assert ph[0] == 1 and ph[1] == [2, 3]

    # Exhaustive implementation cross-check on a small canonical-looking family:
    # b=4,a=3,rho in {1,2}, 0<=q<=a-rho, canonical/simple P.
    checked = 0
    target_bad = 0
    pair_bad = 0
    vals = [(qq, rr) for rr in (1, 2) for qq in range(0, 3 - rr + 1)]
    for qr in product(vals, repeat=4):
        qq = [x[0] for x in qr]
        rr = [x[1] for x in qr]
        PP = canonical_caps(3, 4, qq, rr)
        Q0 = sum(qq)

        tflow = target_flow(qq, rr, PP)
        thall = target_hall(qq, rr, PP)
        assert tflow == Q0 - max(0, thall[0])

        pflow = pair_flow(qq, rr)
        phall = pair_hall(qq, rr)
        assert pflow == Q0 - max(0, phall[0])

        checked += 1
        target_bad += tflow < Q0
        pair_bad += pflow < Q0

    report = {
        "schema": "orientation-flow-hall-verification-v1",
        "counterexample": {
            "a": 4,
            "b": 5,
            "q": q,
            "rho": rho,
            "c": [q[i] + rho[i] for i in range(5)],
            "P": P,
            "Q": Q,
            "old_prefix": [
                {"k": k, "capacity": v, "margin": m} for k, v, m in pref
            ],
            "active_source_local_target_counts": [sum(D[i]) for i in range(5)],
            "target_flow_value": tf,
            "target_hall_deficiency": {
                "deficiency": th[0],
                "W": th[1],
                "lhs": th[2],
                "rhs": th[3],
                "d_W": th[4],
            },
            "pair_flow_value": pf,
            "pair_hall_deficiency": {
                "deficiency": ph[0],
                "W": ph[1],
                "lhs": ph[2],
                "rhs": ph[3],
            },
        },
        "small_exhaustive_crosscheck": {
            "profiles_checked": checked,
            "target_flow_infeasible": target_bad,
            "pair_flow_infeasible": pair_bad,
            "assertion": (
                "max-flow value equals Q minus maximum Hall deficiency "
                "in every checked profile"
            ),
        },
        "external_review": "OPEN",
    }

    out = HERE / "ORIENTATION_FLOW_HALL_VERIFICATION.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
