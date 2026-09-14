#!/usr/bin/env python3
"""Independent finite audit of canonical-witness compatible-copy exactness.

This verifier does not import the earlier Hall/band verifiers.  It reconstructs
complete-type Hall margins, the maximal minimizer M+, sharp staircase bands,
the compatible-copy all-band margin, and labelled/refined max flows.
"""
from collections import Counter, deque
from itertools import combinations_with_replacement
import json
import random
from pathlib import Path

SEED = 742091401
OUT = Path(__file__).resolve().parent / "CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS_VERIFICATION.json"


def compat(x, y):
    qx, cx, _ = x
    qy, cy, _ = y
    return qx <= cy + 1 and qy <= cx


def dominates(x, y):
    qx, cx, px = x
    qy, cy, py = y
    return cx <= cy and (qx > qy or (qx == qy and px >= py))


def grouped(profile):
    ct = Counter(profile)
    types = tuple(sorted(ct))
    counts = tuple(ct[t] for t in types)
    return types, counts


def hall_margin(types, counts, mask):
    demand = sum(counts[t] * types[t][0] for t in range(len(types)) if (mask >> t) & 1)
    cap = 0
    for s, sigma in enumerate(types):
        incoming = 0
        for t, tau in enumerate(types):
            if ((mask >> t) & 1) and compat(tau, sigma):
                incoming += counts[t]
        if (mask >> s) & 1:
            incoming -= 1
        if incoming < 0:
            raise AssertionError(("negative incoming", types, counts, mask, s))
        cap += counts[s] * min(sigma[2], incoming)
    return cap - demand


def maximal_minimizer(types, counts):
    vals = []
    best = None
    for mask in range(1 << len(types)):
        f = hall_margin(types, counts, mask)
        vals.append(f)
        best = f if best is None else min(best, f)
    mplus = 0
    for mask, f in enumerate(vals):
        if f == best:
            mplus |= mask
    if hall_margin(types, counts, mplus) != best:
        raise AssertionError(("union of minimizers not minimizer", types, counts, best, mplus))
    return best, mplus


def is_upset(types, mask):
    for y in range(len(types)):
        if not ((mask >> y) & 1):
            continue
        for x in range(len(types)):
            if x != y and dominates(types[x], types[y]) and not ((mask >> x) & 1):
                return False
    return True


def generators(types, mask):
    gens = []
    for i in range(len(types)):
        if not ((mask >> i) & 1):
            continue
        if any(
            j != i and ((mask >> j) & 1) and dominates(types[i], types[j])
            for j in range(len(types))
        ):
            continue
        gens.append(i)
    gens.sort(key=lambda i: types[i][1])
    return gens


def bands(types, counts, mask):
    gens = generators(types, mask)
    if not gens:
        if mask != 0:
            raise AssertionError(("nonempty upset without generators", types, counts, mask))
        return gens, [], {}, []
    qg = [types[g][0] for g in gens]
    cg = [types[g][1] for g in gens]
    if any(cg[i] >= cg[i + 1] for i in range(len(cg) - 1)):
        raise AssertionError(("generator c not strict", types, gens))
    if any(qg[i] > qg[i + 1] for i in range(len(qg) - 1)):
        raise AssertionError(("generator q decreases", types, gens))

    bt = [[] for _ in gens]
    bof = {}
    for t in range(len(types)):
        if not ((mask >> t) & 1):
            continue
        c = types[t][1]
        choices = [i for i, g in enumerate(gens) if c <= types[g][1]]
        if not choices:
            raise AssertionError(("band assignment missing", types, gens, t))
        i = choices[0]
        if not dominates(types[t], types[gens[i]]):
            raise AssertionError(("band member does not dominate generator", types, gens, t, i))
        bof[t] = i
        bt[i].append(t)
    demand = [sum(counts[t] * types[t][0] for t in bt[i]) for i in range(len(gens))]
    return gens, bt, bof, demand


def all_band_margin(types, counts, mask):
    gens, bt, bof, demand = bands(types, counts, mask)
    if not gens:
        return 0, 0, (gens, bt, bof, demand)
    cap = 0
    for s, sigma in enumerate(types):
        total = 0
        for i in range(len(gens)):
            c = sum(counts[t] for t in bt[i] if compat(types[t], sigma))
            if s in bof and bof[s] == i:
                c -= 1
            if c < 0:
                raise AssertionError(("negative refined count", types, counts, mask, i, s))
            total += c
        cap += counts[s] * min(sigma[2], total)
    d = sum(demand)
    return cap - d, d, (gens, bt, bof, demand)


class Flow:
    def __init__(self, n):
        self.n = n
        self.cap = [[0] * n for _ in range(n)]

    def add(self, u, v, c):
        if c < 0:
            raise AssertionError(("negative capacity", u, v, c))
        self.cap[u][v] += c

    def maxflow(self, s, t):
        r = [row[:] for row in self.cap]
        out = 0
        while True:
            par = [-1] * self.n
            par[s] = s
            q = deque([s])
            while q and par[t] < 0:
                u = q.popleft()
                for v, c in enumerate(r[u]):
                    if c > 0 and par[v] < 0:
                        par[v] = u
                        q.append(v)
                        if v == t:
                            break
            if par[t] < 0:
                return out
            aug = 10**18
            v = t
            while v != s:
                u = par[v]
                aug = min(aug, r[u][v])
                v = u
            v = t
            while v != s:
                u = par[v]
                r[u][v] -= aug
                r[v][u] += aug
                v = u
            out += aug


def labelled_selected_flow(profile, selected_type_set):
    types, counts = grouped(profile)
    type_index = {t: i for i, t in enumerate(types)}
    n = len(profile)
    S = 2 * n
    T = S + 1
    f = Flow(T + 1)
    demand = 0
    for u, tau in enumerate(profile):
        ti = type_index[tau]
        if (selected_type_set >> ti) & 1:
            f.add(S, u, tau[0])
            demand += tau[0]
            for w, sigma in enumerate(profile):
                if u != w and compat(tau, sigma):
                    f.add(u, n + w, 1)
    for w, sigma in enumerate(profile):
        f.add(n + w, T, sigma[2])
    return f.maxflow(S, T), demand


def refined_band_flow(types, counts, mask):
    gens, bt, bof, demand = bands(types, counts, mask)
    h = len(gens)
    if h == 0:
        return 0, 0
    k = len(types)
    S = h + k
    T = S + 1
    f = Flow(T + 1)
    for i in range(h):
        f.add(S, i, demand[i])
    for i in range(h):
        for s, sigma in enumerate(types):
            copies = sum(counts[t] for t in bt[i] if compat(types[t], sigma))
            if s in bof and bof[s] == i:
                copies -= 1
            f.add(i, h + s, counts[s] * copies)
    for s, sigma in enumerate(types):
        f.add(h + s, T, counts[s] * sigma[2])
    return f.maxflow(S, T), sum(demand)


def audit(profile, stats):
    types, counts = grouped(profile)
    m, mp = maximal_minimizer(types, counts)
    if not is_upset(types, mp):
        raise AssertionError(("M+ not sharp upset", profile, types, counts, m, mp))
    exact_margin = hall_margin(types, counts, mp)
    band_margin, d, _ = all_band_margin(types, counts, mp)
    if exact_margin != m or band_margin != m:
        raise AssertionError(("whole-staircase identity", profile, m, exact_margin, band_margin, mp))

    exact_flow, exact_demand = labelled_selected_flow(profile, mp)
    band_flow, band_demand = refined_band_flow(types, counts, mp)
    if exact_demand != d or band_demand != d:
        raise AssertionError(("demand mismatch", profile, d, exact_demand, band_demand))
    if exact_flow > band_flow:
        raise AssertionError(("aggregation flow order", profile, exact_flow, band_flow, d))

    original_feasible = m >= 0
    band_feasible = band_flow == d
    if original_feasible != band_feasible:
        raise AssertionError(("canonical feasibility equivalence", profile, m, band_flow, d, mp))
    if m < 0 and not (band_margin < 0 and band_flow < d):
        raise AssertionError(("deficient canonical witness not detected", profile, m, band_margin, band_flow, d))

    stats["profiles"] += 1
    stats["infeasible_profiles"] += int(m < 0)
    stats["feasible_profiles"] += int(m >= 0)
    stats["canonical_nonempty"] += int(mp != 0)
    stats["whole_staircase_identity_checks"] += 1
    stats["canonical_feasibility_equivalence_checks"] += 1
    stats["max_distinct_types"] = max(stats["max_distinct_types"], len(types))
    stats["max_vertices"] = max(stats["max_vertices"], len(profile))


def main():
    universe = [
        (0, 0, 0), (0, 1, 1),
        (1, 1, 0), (1, 2, 1), (1, 3, 2),
        (2, 2, 1), (2, 3, 2), (2, 4, 3),
    ]
    stats = {
        "profiles": 0,
        "infeasible_profiles": 0,
        "feasible_profiles": 0,
        "canonical_nonempty": 0,
        "whole_staircase_identity_checks": 0,
        "canonical_feasibility_equivalence_checks": 0,
        "max_distinct_types": 0,
        "max_vertices": 0,
    }
    exhaustive = 0
    for n in range(1, 6):
        for profile in combinations_with_replacement(universe, n):
            audit(profile, stats)
            exhaustive += 1

    rng = random.Random(SEED)
    random_profiles = 1200
    for _ in range(random_profiles):
        n = rng.randint(1, 7)
        p = []
        for __ in range(n):
            q = rng.randint(0, 4)
            rho = rng.randint(0, 4)
            cap = rng.randint(0, 5)
            p.append((q, q + rho, cap))
        audit(tuple(p), stats)

    report = {
        "schema": "canonical-witness-compatible-copy-exactness-verification-v1",
        "result": "PASS",
        "seed": SEED,
        "exhaustive_universe": [list(x) for x in universe],
        "exhaustive_max_order": 5,
        "exhaustive_profiles": exhaustive,
        "random_profiles": random_profiles,
        **stats,
        "claims_checked": [
            "the union of minimum complete-type Hall cuts remains a minimum cut",
            "the canonical maximal minimizer is a sharp-hardness up-set",
            "the compatible-copy all-bands margin equals the exact Hall margin of M+",
            "labelled selected-source flow is no larger than compatible-copy band flow",
            "the compatible-copy band network built from M+ is feasible iff original target Hall is feasible",
            "every deficient canonical M+ is rejected by its all-bands compatible-copy cut",
        ],
        "external_review": "OPEN",
        "note": "Independent finite arithmetic audit of the canonical-witness exactness corollary; not third-party review of the Murty-Simon bridge.",
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
