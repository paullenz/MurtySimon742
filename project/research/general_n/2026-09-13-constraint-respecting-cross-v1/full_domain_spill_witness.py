#!/usr/bin/env python3
"""Construct and directly verify spill-surviving witnesses for every combined survivor.

This is an exact positive-witness test, not an infeasibility search.  For each
of the 4,584 combined compatible-routing survivors it seeks one exact-demand
selected pattern S (therefore x_i=s_i), derives q, constructs a p vector that
satisfies the previous selected-balance/transport tails, and checks the new
receiver-containment spill inequalities.  A successful witness proves only
that these necessary conditions do not by themselves exclude the state.

No solver is used.  The search is deterministic from the recorded seed rule;
every saved witness is then rechecked independently by check_witness().
"""
from collections import defaultdict
from pathlib import Path
import hashlib
import json
import random
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import records, read_bytes  # noqa: E402


def combined_survivors():
    rows = json.loads(read_bytes("survivors.json"))
    out = [r for r in rows if r["combined_survives"]]
    assert len(rows) == 4588
    assert len(out) == 4584
    assert sum(r["layer"] == "n34-m289" for r in out) == 4506
    assert sum(r["layer"] == "n35-m306" for r in out) == 78
    return out


def selected_pattern(rec, rng, mode):
    """Construct x=s with distinct labels at each source.

    Labels are processed hardest-first.  The score modes deliberately generate
    different q geometries while respecting rho_u>=s_i and q_u<=a-rho_u.
    """
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    S = [set() for _ in range(b)]
    order = sorted(range(a), key=lambda i: (-s[i], i))
    for i in order:
        need = s[i]
        eligible = [u for u in range(b) if rho[u] >= s[i] and len(S[u]) < a - rho[u]]
        if len(eligible) < need:
            return None
        scored = []
        for u in eligible:
            q = len(S[u])
            cap = a - rho[u]
            if mode == 0:       # balanced q
                score = (q, rng.random())
            elif mode == 1:     # balanced relative to available selected capacity
                score = ((q + 0.25) / (cap + 0.25), rng.random())
            elif mode == 2:     # favour larger rho among similarly loaded sources
                score = (q, -rho[u], rng.random())
            elif mode == 3:     # favour smaller rho among similarly loaded sources
                score = (q, rho[u], rng.random())
            else:               # noisy but still mildly balanced
                score = (q + 2.0 * rng.random(), rng.random())
            scored.append((score, u))
        for _, u in sorted(scored)[:need]:
            S[u].add(i)
    return S


def greedy_p(rec, q):
    """Maximise every nested receiving tail by filling highest rho+q first."""
    a, b, rho = rec["a"], rec["b"], rec["rho"]
    Q = sum(q)
    cap = [min(rho[u] + b - a - 1, b - 1 - q[u]) for u in range(b)]
    if min(cap, default=0) < 0 or sum(cap) < Q:
        return None
    p = [0] * b
    left = Q
    for u in sorted(range(b), key=lambda u: (-(rho[u] + q[u]), -cap[u], u)):
        take = min(cap[u], left)
        p[u] = take
        left -= take
    if left:
        return None
    # These are the previous all-transport inequalities.  Because the receiver
    # sets {rho+q>=k} are nested, the high-(rho+q) greedy allocation maximises
    # every right-hand tail simultaneously for this fixed q.
    for k in range(a + 2):
        lhs = sum(q[u] for u in range(b) if q[u] > k)
        rhs = sum(p[u] for u in range(b) if rho[u] + q[u] >= k)
        if lhs > rhs:
            return None
    return p


def spill_details(rec, q):
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    Q = sum(q)
    S_total = sum(s)
    eligibility = [sum(rho[v] >= s[i] for v in range(b)) for i in range(a)]
    prefix_s = [0]
    for x in sorted(s, reverse=True):
        prefix_s.append(prefix_s[-1] + x)
    prefix_e = [0]
    for x in sorted(eligibility, reverse=True):
        prefix_e.append(prefix_e[-1] + x)
    out = []
    for u in range(b):
        nu = q[u] + rho[u]
        assert 0 <= nu <= a
        candidates = [
            v for v in range(b)
            if v != u
            and q[v] + rho[v] >= q[u] - 1
            and q[v] <= nu
            and rho[v] + b - a - 1 >= 1
        ]
        if len(candidates) < q[u]:
            return False, {"source": u, "reason": "candidate_count", "q": q[u], "candidates": len(candidates)}
        h = a - nu
        g = [min(q[v], h) for v in range(b) if v != u]
        cg = sorted(min(q[v], h) for v in candidates)
        G = sum(g) - sum(cg[:q[u]])
        lam = max(0, S_total - prefix_s[nu], Q - prefix_e[nu])
        if lam > G:
            return False, {"source": u, "reason": "spill", "q": q[u], "n": nu, "lambda": lam, "G": G}
        out.append({"source": u, "q": q[u], "n": nu, "candidates": len(candidates), "lambda": lam, "G": G})
    return True, out


def check_witness(rec, witness):
    a, b, s, rho = rec["a"], rec["b"], rec["s"], rec["rho"]
    S = [set(x) for x in witness["selected"]]
    q = witness["q"]
    p = witness["p"]
    assert len(S) == len(q) == len(p) == b
    assert [len(x) for x in S] == q
    assert all(len(S[u]) <= a - rho[u] for u in range(b))
    assert all(all(0 <= i < a and rho[u] >= s[i] for i in S[u]) for u in range(b))
    x = [sum(i in S[u] for u in range(b)) for i in range(a)]
    assert x == s
    Q = sum(q)
    assert Q == sum(s) == sum(p)
    for u in range(b):
        assert 0 <= p[u] <= min(rho[u] + b - a - 1, b - 1 - q[u])
    for k in range(a + 2):
        assert sum(q[u] for u in range(b) if q[u] > k) <= sum(
            p[u] for u in range(b) if rho[u] + q[u] >= k
        )
    ok, details = spill_details(rec, q)
    assert ok
    return {
        "Q": Q,
        "min_candidate_margin": min((d["candidates"] - d["q"] for d in details), default=0),
        "min_spill_slack": min((d["G"] - d["lambda"] for d in details), default=0),
    }


def find_witness(rec, index, max_attempts=256):
    # Different deterministic modes first, then seeded noisy-balanced samples.
    base = 742000000 + 1009 * index + rec["state_id"]
    for attempt in range(max_attempts):
        mode = attempt if attempt < 5 else 4
        rng = random.Random(base + 104729 * attempt)
        S = selected_pattern(rec, rng, mode)
        if S is None:
            continue
        q = [len(z) for z in S]
        p = greedy_p(rec, q)
        if p is None:
            continue
        ok, _ = spill_details(rec, q)
        if not ok:
            continue
        witness = {
            "attempt": attempt,
            "selected": [sorted(z) for z in S],
            "q": q,
            "p": p,
        }
        witness["check"] = check_witness(rec, witness)
        return witness
    return None


def main():
    survivors = combined_survivors()
    output = []
    unresolved = []
    attempts_hist = defaultdict(int)
    layer_counts = defaultdict(int)
    min_spill = None
    min_candidate = None
    for idx, rec in enumerate(survivors):
        w = find_witness(rec, idx)
        key = {"layer": rec["layer"], "state_id": rec["state_id"]}
        if w is None:
            unresolved.append(key)
        else:
            check = check_witness(rec, w)
            assert check == w["check"]
            attempts_hist[w["attempt"]] += 1
            layer_counts[rec["layer"]] += 1
            min_spill = check["min_spill_slack"] if min_spill is None else min(min_spill, check["min_spill_slack"])
            min_candidate = check["min_candidate_margin"] if min_candidate is None else min(min_candidate, check["min_candidate_margin"])
            output.append({**key, **w})
        if (idx + 1) % 250 == 0:
            print(f"processed {idx+1}/{len(survivors)} unresolved={len(unresolved)}", flush=True)

    payload = {
        "schema": "full-domain-spill-positive-witness-v1",
        "date": "2026-09-13",
        "scope": (
            "Direct positive witnesses for the exact-demand selected-degree, selected-balance, "
            "all-transport and receiver-containment-spill necessary conditions.  This is a "
            "relaxed domain: it does not include the heavy-H catalogue inequalities, residual "
            "placement, exact destination sets or final Hall routing."
        ),
        "input": {
            "catalogue_survivors_sha256": hashlib.sha256(read_bytes("survivors.json")).hexdigest(),
            "catalogue_pool_sha256": hashlib.sha256(read_bytes("pool_inputs.jsonl")).hexdigest(),
            "combined_survivors": len(survivors),
        },
        "summary": {
            "witnessed": len(output),
            "unresolved": len(unresolved),
            "by_layer": dict(sorted(layer_counts.items())),
            "minimum_spill_slack": min_spill,
            "minimum_candidate_margin": min_candidate,
            "attempt_histogram": {str(k): v for k, v in sorted(attempts_hist.items())},
            "whole_state_exclusions_proved": 0,
        },
        "unresolved": unresolved,
        "witnesses": output,
    }
    path = HERE / "FULL_DOMAIN_SPILL_WITNESSES.json"
    path.write_text(json.dumps(payload, separators=(",", ":")) + "\n")
    print(json.dumps({"status": "PASS" if not unresolved else "PARTIAL", **payload["summary"]}, indent=2))
    if unresolved:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
