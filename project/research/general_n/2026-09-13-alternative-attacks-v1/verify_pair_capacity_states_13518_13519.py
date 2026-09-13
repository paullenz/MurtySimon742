#!/usr/bin/env python3
"""Independent superset replay for candidate closures 13518 and 13519.

This deliberately does NOT reuse the C++ q recursion, selected-incidence flow,
base-demand prefix constraints, orientation-prefix cuts, Hall flows or weighted
excess-cost machinery.

For each state and every Q=S+E allowed by the universal per-source selected
label count, it enumerates ALL q multisets inside equal-rho classes subject only
to

    0 <= q_u <= min(a-rho_u, #{i:s_i<=rho_u})
    sum q_u = Q.

This is a superset of every legal selected-incidence profile.  Each profile is
then tested only against:

  * universal incoming p<=rho+b-a-1;
  * simple missing degree p<=b-1-q;
  * TOTAL_EXCESS_SOURCE_CAP.md (all demands here are positive);
  * the orientation-independent potential-pair graph K_D from
    ORIENTATION_FLOW_HALL.md, giving p<=d_KD-q.

If even this larger q universe always has total incoming capacity < Q (or a
negative pointwise capacity), the scalar state is independently excluded under
those structural lemmas, without relying on the more elaborate C++ scanner.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, product
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402

TARGETS = {13518, 13519}


@lru_cache(maxsize=None)
def class_parts(count, qmax, total):
    return tuple(
        xs for xs in combinations_with_replacement(range(qmax + 1), count)
        if sum(xs) == total
    )


def directed_ok(q, rho, u, w):
    if u == w:
        return False
    cu = q[u] + rho[u]
    cw = q[w] + rho[w]
    return q[u] <= cw + 1 and q[w] <= cu


def caps_for_profile(*, a, b, E, q, rho):
    n = len(q)
    pairdeg = [0] * n
    for u in range(n):
        for w in range(u + 1, n):
            if directed_ok(q, rho, u, w) or directed_ok(q, rho, w, u):
                pairdeg[u] += 1
                pairdeg[w] += 1

    base = []
    pair = []
    for u in range(n):
        p0 = min(rho[u] + b - a - 1, b - 1 - q[u])
        if q[u] > 0:
            # z=0 for both target states.
            p0 = min(p0, rho[u] + E // q[u] - 1)
        base.append(p0)
        pair.append(min(p0, pairdeg[u] - q[u]))
    return base, pair, pairdeg


def enumerate_profiles(s, rho, a, Q):
    classes = []
    counts = Counter(rho)
    for r in sorted(counts):
        qmax = min(a - r, sum(d <= r for d in s))
        classes.append((r, counts[r], qmax))

    suffix = [0] * (len(classes) + 1)
    for i in range(len(classes) - 1, -1, -1):
        _, cnt, qmax = classes[i]
        suffix[i] = suffix[i + 1] + cnt * qmax

    def rec(i, used, qout, rout):
        if i == len(classes):
            if used == Q:
                yield tuple(qout), tuple(rout)
            return
        r, cnt, qmax = classes[i]
        lo = max(0, Q - used - suffix[i + 1])
        hi = min(cnt * qmax, Q - used)
        for sm in range(lo, hi + 1):
            for xs in class_parts(cnt, qmax, sm):
                yield from rec(
                    i + 1,
                    used + sm,
                    qout + list(xs),
                    rout + [r] * cnt,
                )

    yield from rec(0, 0, [], [])


def check_state(row):
    s = list(row["s"])
    rho0 = list(row["rho"])
    a, b = row["a"], row["b"]
    assert min(s) > 0
    S = sum(s)

    qmax_total = sum(min(a - r, sum(d <= r for d in s)) for r in rho0)
    Emax = qmax_total - S
    assert Emax >= 0

    layers = []
    total_profiles = 0
    for E in range(Emax + 1):
        Q = S + E
        profiles = 0
        base_capacity_pass = 0
        pair_capacity_pass = 0
        best_pair_margin = None
        best_base_margin = None
        best_q = None
        best_pairdeg = None
        best_pair_caps = None

        for q, rho in enumerate_profiles(s, rho0, a, Q):
            profiles += 1
            base, pair, pairdeg = caps_for_profile(a=a, b=b, E=E, q=q, rho=rho)

            base_ok = min(base) >= 0 and sum(base) >= Q
            if base_ok:
                base_capacity_pass += 1
            bm = sum(base) - Q if min(base) >= 0 else -10**9
            if best_base_margin is None or bm > best_base_margin:
                best_base_margin = bm

            pair_ok = min(pair) >= 0 and sum(pair) >= Q
            if pair_ok:
                pair_capacity_pass += 1
            pm = sum(pair) - Q if min(pair) >= 0 else -10**9
            if best_pair_margin is None or pm > best_pair_margin:
                best_pair_margin = pm
                best_q = q
                best_pairdeg = tuple(pairdeg)
                best_pair_caps = tuple(pair)

        total_profiles += profiles
        assert profiles > 0
        assert pair_capacity_pass == 0, (row["state_id"], E, best_pair_margin, best_q)
        layers.append({
            "E": E,
            "Q": Q,
            "profiles": profiles,
            "base_capacity_pass": base_capacity_pass,
            "pair_capacity_pass": pair_capacity_pass,
            "best_base_margin": best_base_margin,
            "best_pair_margin": best_pair_margin,
            "closest_q": list(best_q),
            "closest_pairdeg": list(best_pairdeg),
            "closest_pair_caps": list(best_pair_caps),
        })

    return {
        "state_id": row["state_id"],
        "a": a,
        "b": b,
        "t": row["t"],
        "s": s,
        "rho": rho0,
        "S": S,
        "Emax": Emax,
        "profiles_checked": total_profiles,
        "all_layers_pair_capacity_excluded": True,
        "layers": layers,
    }


def main():
    raw = read_bytes("survivors.json")
    rows = json.loads(raw)
    selected = [
        r for r in rows
        if r.get("combined_survives") and r["layer"] == "n34-m289" and r["state_id"] in TARGETS
    ]
    assert {r["state_id"] for r in selected} == TARGETS
    selected.sort(key=lambda r: r["state_id"])

    results = [check_state(r) for r in selected]
    report = {
        "schema": "pair-capacity-states-13518-13519-independent-v1",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "states": results,
        "assertion": (
            "Every q profile in the deliberately enlarged universe fails the sum-p=Q "
            "incoming capacity test after adding the orientation-independent potential-pair "
            "degree cap p_u<=d_KD(u)-q_u. No selected-incidence flow, q-prefix Hall, pair-flow, "
            "target-flow or weighted excess-budget theorem is used in this replay."
        ),
        "external_review": "OPEN",
    }
    out = HERE / "PAIR_CAPACITY_13518_13519_INDEPENDENT.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "schema": report["schema"],
        "source_sha256": report["source_sha256"],
        "states": [
            {
                "state_id": r["state_id"],
                "Emax": r["Emax"],
                "profiles_checked": r["profiles_checked"],
                "worst_best_pair_margin": max(x["best_pair_margin"] for x in r["layers"]),
                "layers": [
                    {
                        "E": x["E"],
                        "profiles": x["profiles"],
                        "base_capacity_pass": x["base_capacity_pass"],
                        "best_base_margin": x["best_base_margin"],
                        "best_pair_margin": x["best_pair_margin"],
                    }
                    for x in r["layers"]
                ],
            }
            for r in results
        ],
        "result": "PASS",
        "external_review": "OPEN",
    }, indent=2))


if __name__ == "__main__":
    main()
