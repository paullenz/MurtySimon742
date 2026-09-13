#!/usr/bin/env python3
"""Assemble and directly verify one spill/transport witness for every combined survivor.

Stages:
  1. reuse the 4,484 direct witnesses from FULL_DOMAIN_SPILL_WITNESSES.json;
  2. rerun the deeper exact-demand search on its 100 unresolved states;
  3. if exact demand still fails to yield a witness, allow the canonical freedom
     x_i>s_i and construct a selected-label realization by exact lower-bound flow.

The output is positive evidence only.  It proves that the new spill inequality,
combined with the explicit necessary conditions checked here, adds zero whole-
state exclusions among the 4,584 combined survivors.  It does not assert that
any witness extends to residual sets, exact destinations, heavy-H data or a D2C
graph.
"""
from collections import deque, Counter
from pathlib import Path
import hashlib
import json
import random
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

sys.path.insert(0, str(HERE))
from full_domain_spill_witness import greedy_p, spill_details  # noqa: E402
from refine_spill_witness import parameter_selected, local_improve, try_witness  # noqa: E402


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, cap):
        a = [v, cap, len(self.g[v]), cap]
        b = [u, 0, len(self.g[u]), 0]
        self.g[u].append(a); self.g[v].append(b)
        return u, len(self.g[u]) - 1

    def maxflow(self, s, t):
        total = 0
        while True:
            level = [-1] * len(self.g); level[s] = 0; q = deque([s])
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e[1] and level[e[0]] < 0:
                        level[e[0]] = level[u] + 1; q.append(e[0])
            if level[t] < 0:
                return total
            it = [0] * len(self.g)
            def dfs(u, f):
                if u == t: return f
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    if e[1] and level[e[0]] == level[u] + 1:
                        z = dfs(e[0], min(f, e[1]))
                        if z:
                            e[1] -= z; self.g[e[0]][e[2]][1] += z
                            return z
                    it[u] += 1
                return 0
            while True:
                z = dfs(s, 10**9)
                if not z: break
                total += z


def combined_survivors():
    rows = json.loads(read_bytes("survivors.json"))
    out = [r for r in rows if r["combined_survives"]]
    assert len(out) == 4584
    return out


def q_caps(rec):
    return [
        min(rec["a"] - r, sum(si <= r for si in rec["s"]))
        for r in rec["rho"]
    ]


def selected_flow_for_q(rec, q):
    """Exact lower-bound circulation realizing row degrees q and x_i>=s_i."""
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    Q = sum(q)
    root = 0; b0 = 1; l0 = 1 + b; sink = 1 + b + a; ss = sink + 1; tt = sink + 2
    d = Dinic(tt + 1); bal = [0] * (tt + 1); refs = {}

    def add_lb(u, v, lo, hi, key=None):
        assert 0 <= lo <= hi
        ref = d.add(u, v, hi - lo)
        bal[u] -= lo; bal[v] += lo
        if key is not None: refs[key] = (ref, lo)

    for u in range(b):
        add_lb(root, b0 + u, q[u], q[u])
    for u in range(b):
        for i in range(a):
            if rho[u] >= s[i]:
                add_lb(b0 + u, l0 + i, 0, 1, (u, i))
    eligibility = [sum(r >= s[i] for r in rho) for i in range(a)]
    for i in range(a):
        add_lb(l0 + i, sink, s[i], eligibility[i])
    add_lb(sink, root, Q, Q)

    need = 0
    for v, x in enumerate(bal):
        if x > 0:
            d.add(ss, v, x); need += x
        elif x < 0:
            d.add(v, tt, -x)
    if d.maxflow(ss, tt) != need:
        return None

    selected = [set() for _ in range(b)]
    for (u, i), ((uu, idx), lo) in refs.items():
        e = d.g[uu][idx]
        used = e[3] - e[1] + lo
        if used:
            assert used == 1
            selected[u].add(i)
    if [len(z) for z in selected] != q:
        return None
    x = [sum(i in selected[u] for u in range(b)) for i in range(a)]
    if any(x[i] < s[i] for i in range(a)):
        return None
    return selected, x


def validate_general(rec, w):
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    selected = [set(z) for z in w["selected"]]
    q = list(w["q"]); p = list(w["p"])
    assert len(selected) == len(q) == len(p) == b
    assert [len(z) for z in selected] == q
    assert all(len(selected[u]) <= a - rho[u] for u in range(b))
    assert all(all(rho[u] >= s[i] for i in selected[u]) for u in range(b))
    x = [sum(i in selected[u] for u in range(b)) for i in range(a)]
    assert all(x[i] >= s[i] for i in range(a))
    Q = sum(q)
    assert Q == sum(x) == sum(p)
    for u in range(b):
        assert 0 <= p[u] <= min(rho[u] + b - a - 1, b - 1 - q[u])
    for k in range(a + 2):
        assert sum(q[u] for u in range(b) if q[u] > k) <= sum(
            p[u] for u in range(b) if rho[u] + q[u] >= k
        )
    ok, details = spill_details(rec, q); assert ok
    return {
        "Q": Q,
        "selected_degree_sum": sum(x),
        "demand_sum": sum(s),
        "extra_selected": Q - sum(s),
        "x": x,
        "min_candidate_margin": min(d["candidates"] - d["q"] for d in details),
        "min_spill_slack": min(d["G"] - d["lambda"] for d in details),
    }


def deeper_exact(rec, index):
    seed = 913000000 + index * 100003 + rec["state_id"]
    rng = random.Random(seed); best = None; best_tuple = None
    for attempt in range(20000):
        S = parameter_selected(rec, rng)
        if S is None: continue
        # Cheap positive test first.
        w = try_witness(rec, S)
        if w is not None:
            return {"stage": "deep_exact", "seed": seed, "attempt": attempt, **w}
        # Periodic local improvement uses the scorer in the imported refinement.
        if attempt in (499, 1999, 7999):
            from refine_spill_witness import score
            sc, _ = score(rec, S)
            if best_tuple is None or sc < best_tuple:
                best_tuple = sc; best = [set(z) for z in S]
            if best is not None:
                improved, isc = local_improve(rec, best, rng, steps=600)
                if isc < best_tuple:
                    best_tuple = isc; best = improved
                w = try_witness(rec, best)
                if w is not None:
                    return {"stage": "deep_exact_local", "seed": seed, "attempt": attempt, **w}
    if best is not None:
        improved, _ = local_improve(rec, best, rng, steps=3000)
        w = try_witness(rec, improved)
        if w is not None:
            return {"stage": "deep_exact_final_local", "seed": seed, "attempt": 20000, **w}
    return None


def random_extra_q(rec, rng, Q):
    caps = q_caps(rec); b = rec["b"]
    if Q > sum(caps): return None
    q = [rng.randrange(c + 1) if c else 0 for c in caps]
    diff = Q - sum(q)
    while diff > 0:
        cand = [u for u in range(b) if q[u] < caps[u]]
        if not cand: return None
        u = rng.choice(cand); q[u] += 1; diff -= 1
    while diff < 0:
        cand = [u for u in range(b) if q[u] > 0]
        if not cand: return None
        u = rng.choice(cand); q[u] -= 1; diff += 1
    return q


def extra_witness(rec, index, attempts=50000):
    seed = 20260913 + rec["state_id"] + 1000003 * index
    rng = random.Random(seed); base = sum(rec["s"]); maxq = sum(q_caps(rec))
    extra_cap = min(25, maxq - base)
    for attempt in range(attempts):
        if extra_cap <= 0: break
        # Cycle the first few extra totals, then randomise them.
        extra = 1 + (attempt % extra_cap if attempt < extra_cap else rng.randrange(extra_cap))
        Q = base + extra
        q = random_extra_q(rec, rng, Q)
        if q is None: continue
        p = greedy_p(rec, q)
        if p is None: continue
        ok, _ = spill_details(rec, q)
        if not ok: continue
        realization = selected_flow_for_q(rec, q)
        if realization is None: continue
        selected, x = realization
        w = {"stage": "extra_selected", "seed": seed, "attempt": attempt,
             "selected": [sorted(z) for z in selected], "q": q, "p": p}
        check = validate_general(rec, w)
        assert check["x"] == x and check["extra_selected"] > 0
        w["check"] = check
        return w
    return None


def main():
    rows = combined_survivors(); bykey = {(r["layer"], r["state_id"]): r for r in rows}
    first = json.loads((HERE / "FULL_DOMAIN_SPILL_WITNESSES.json").read_text())
    assert first["summary"]["witnessed"] == 4484 and first["summary"]["unresolved"] == 100
    witnesses = {}
    stage_counts = Counter()

    for old in first["witnesses"]:
        key = old["layer"], old["state_id"]; rec = bykey[key]
        w = {k: v for k, v in old.items() if k not in ("layer", "state_id", "check")}
        w["stage"] = "pass1_exact"
        w["check"] = validate_general(rec, w)
        assert w["check"]["extra_selected"] == 0
        witnesses[key] = w; stage_counts[w["stage"]] += 1

    unresolved = [(x["layer"], x["state_id"]) for x in first["unresolved"]]
    for index, key in enumerate(unresolved):
        rec = bykey[key]
        w = deeper_exact(rec, index)
        if w is None:
            w = extra_witness(rec, index)
        if w is None:
            raise RuntimeError(f"OPEN: no positive witness found for {key}")
        w["check"] = validate_general(rec, w)
        witnesses[key] = w; stage_counts[w["stage"]] += 1
        print(index + 1, "/", len(unresolved), key, w["stage"], "Q", w["check"]["Q"], flush=True)

    assert len(witnesses) == 4584 and set(witnesses) == set(bykey)
    ordered = []
    for key in sorted(witnesses):
        rec = bykey[key]; w = witnesses[key]
        again = validate_general(rec, w); assert again == w["check"]
        ordered.append({"layer": key[0], "state_id": key[1], **w})

    extras = [w for w in ordered if w["check"]["extra_selected"]]
    payload = {
        "schema": "full-domain-spill-complete-positive-witness-v1",
        "date": "2026-09-13",
        "input": {
            "survivors_sha256": hashlib.sha256(read_bytes("survivors.json")).hexdigest(),
            "pool_sha256": hashlib.sha256(read_bytes("pool_inputs.jsonl")).hexdigest(),
            "combined_survivors": 4584,
        },
        "scope": (
            "For every combined compatible-routing survivor, one directly verified selected "
            "pattern satisfies x_i>=s_i, source eligibility/capacity, selected balance, all "
            "transport tails and the receiver-containment spill inequality.  This proves zero "
            "whole-state exclusions from this conjunction only.  Residual-set placement, exact "
            "destination compatibility, heavy-H catalogue data and final Hall routing are not "
            "constructed here."
        ),
        "summary": {
            "witnessed": 4584,
            "unresolved": 0,
            "whole_state_exclusions_added": 0,
            "stage_counts": dict(sorted(stage_counts.items())),
            "witnesses_with_extra_selected": len(extras),
            "extra_witness_ids": [[w["layer"], w["state_id"]] for w in extras],
            "minimum_candidate_margin": min(w["check"]["min_candidate_margin"] for w in ordered),
            "minimum_spill_slack": min(w["check"]["min_spill_slack"] for w in ordered),
        },
        "witnesses": ordered,
    }
    (HERE / "FULL_DOMAIN_SPILL_COMPLETE.json").write_text(json.dumps(payload, separators=(",", ":")) + "\n")
    print(json.dumps(payload["summary"], indent=2))


if __name__ == "__main__":
    main()
