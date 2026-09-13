#!/usr/bin/env python3
"""Independent small-instance checks for the strengthened all-excess machinery.

This verifier does two logically separate checks:

1. Compare the lower-bound selected-incidence circulation criterion with brute
   enumeration of every allowed 0/1 source-label incidence matrix on small
   instances.
2. Brute-force the TOTAL_EXCESS_SOURCE_CAP.md inequality over small demand,
   excess and selected-label configurations.

It is intentionally independent of the C++ scanner implementation.
"""
from itertools import combinations, product
import json
from collections import deque
from pathlib import Path

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
            q = deque([s])
            while q:
                u = q.popleft()
                for v, cap, rev in self.g[u]:
                    if cap and lev[v] < 0:
                        lev[v] = lev[u] + 1
                        q.append(v)
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
                        z = dfs(v, min(f, cap))
                        if z:
                            e[1] -= z
                            rev[1] += z
                            return z
                    it[u] += 1
                return 0

            while True:
                z = dfs(s, 10**9)
                if not z:
                    break
                ans += z


def circulation_feasible(s, rho, qdeg):
    n, m = len(rho), len(s)
    S0, T0, SS, TT = n + m, n + m + 1, n + m + 2, n + m + 3
    F = Dinic(TT + 1)
    bal = [0] * (TT + 1)

    def lowedge(u, v, lo, hi):
        if lo > hi:
            return False
        F.add(u, v, hi - lo)
        bal[u] -= lo
        bal[v] += lo
        return True

    Q = sum(qdeg)
    for u in range(n):
        if not lowedge(S0, u, qdeg[u], qdeg[u]):
            return False
    for u in range(n):
        for i in range(m):
            if s[i] <= rho[u]:
                lowedge(u, n + i, 0, 1)
    for i in range(m):
        up = sum(s[i] <= rho[u] for u in range(n))
        if not lowedge(n + i, T0, s[i], up):
            return False
    lowedge(T0, S0, 0, Q)

    need = 0
    for v in range(T0 + 1):
        if bal[v] > 0:
            F.add(SS, v, bal[v])
            need += bal[v]
        elif bal[v] < 0:
            F.add(v, TT, -bal[v])
    return F.flow(SS, TT) == need


def brute_incidence(s, rho, qdeg):
    n, m = len(rho), len(s)
    allowed = [(u, i) for u in range(n) for i in range(m) if s[i] <= rho[u]]
    Q = sum(qdeg)
    if Q > len(allowed):
        return False
    for chosen in combinations(allowed, Q):
        rows = [0] * n
        cols = [0] * m
        ok = True
        seen = set()
        for u, i in chosen:
            if (u, i) in seen:
                ok = False
                break
            seen.add((u, i))
            rows[u] += 1
            cols[i] += 1
        if ok and rows == list(qdeg) and all(cols[i] >= s[i] for i in range(m)):
            return True
    return False


def check_incidence():
    checked = 0
    mismatches = []
    # Keep brute enumeration deliberately tiny but exhaustive inside this box.
    for n in (1, 2, 3):
        for m in (1, 2, 3):
            for rho in product((1, 2), repeat=n):
                for s in product((0, 1, 2), repeat=m):
                    for qdeg in product(range(m + 1), repeat=n):
                        if sum(qdeg) > 7:
                            continue
                        allowed_count = sum(s[i] <= rho[u] for u in range(n) for i in range(m))
                        if allowed_count > 9:
                            continue
                        a = circulation_feasible(s, rho, qdeg)
                        b = brute_incidence(s, rho, qdeg)
                        checked += 1
                        if a != b:
                            mismatches.append({"s": s, "rho": rho, "q": qdeg, "flow": a, "brute": b})
                            if len(mismatches) >= 10:
                                return checked, mismatches
    return checked, mismatches


def total_excess_cap(rho, q, E, z):
    if q <= 0:
        return None
    kstar = min(z, q, E)
    if q <= kstar:
        return None
    return rho + (E - kstar) // (q - kstar) - 1


def check_total_excess_cap():
    checked = 0
    violations = []
    for m in range(1, 5):
        for s in product((0, 1, 2), repeat=m):
            z = sum(x == 0 for x in s)
            for e in product((0, 1, 2), repeat=m):
                E = sum(e)
                x = [s[i] + e[i] for i in range(m)]
                usable = [i for i in range(m) if x[i] > 0]
                for q in range(1, len(usable) + 1):
                    for sel in combinations(usable, q):
                        # A selected zero-demand label must indeed have e_i>=1;
                        # x_i>0 above guarantees exactly that.
                        for rho in (1, 2, 3):
                            for p in range(0, 7):
                                valid = all(
                                    s[i] == 0 or p - rho + 1 <= e[i]
                                    for i in sel
                                )
                                if not valid:
                                    continue
                                cap = total_excess_cap(rho, q, E, z)
                                checked += 1
                                if cap is not None and p > cap:
                                    violations.append({
                                        "s": s, "e": e, "E": E, "sel": sel,
                                        "rho": rho, "p": p, "q": q, "z": z,
                                        "cap": cap,
                                    })
                                    if len(violations) >= 10:
                                        return checked, violations
    return checked, violations


def main():
    inc_checked, inc_bad = check_incidence()
    cap_checked, cap_bad = check_total_excess_cap()
    assert not inc_bad, inc_bad
    assert not cap_bad, cap_bad

    report = {
        "schema": "total-excess-machinery-verification-v1",
        "incidence_circulation": {
            "small_instances_checked": inc_checked,
            "mismatches": len(inc_bad),
            "result": "PASS",
        },
        "total_excess_source_cap": {
            "valid_selected_source_configurations_checked": cap_checked,
            "violations": len(cap_bad),
            "result": "PASS",
        },
        "external_review": "OPEN",
    }
    (HERE / "TOTAL_EXCESS_MACHINERY_VERIFICATION.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
