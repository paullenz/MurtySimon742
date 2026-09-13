#!/usr/bin/env python3
"""Assemble an exact-demand spill/transport witness for all 4,584 survivors.

The first pass already stores 4,484 exact-demand witnesses.  The deeper search
recovers 98 of the remaining 100.  The two search-hard boundary profiles share
a directly verified nonuniform q construction, recorded here deterministically.
Thus every final witness has x_i=s_i exactly; no extra selected incidence is
needed to survive the spill inequality.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "2026-09-12-compatible-routing-catalogue-v1"
sys.path.insert(0, str(CAT))
from evidence_io import read_bytes  # noqa: E402
sys.path.insert(0, str(HERE))
from complete_spill_witness import combined_survivors, deeper_exact, selected_flow_for_q, validate_general  # noqa: E402
from full_domain_spill_witness import greedy_p, spill_details  # noqa: E402


def boundary_exact(rec):
    """Deterministic exact-demand witness for the two search-hard boundary states.

    Both have s=(4,4,5^13), one rho=4 source and eleven rho=5 sources; all
    lower-rho sources have q=0.  The displayed multiset sums to 73=sum(s).
    """
    if rec["s"] != [4, 4] + [5] * 13:
        return None
    i4 = [u for u, r in enumerate(rec["rho"]) if r == 4]
    i5 = [u for u, r in enumerate(rec["rho"]) if r == 5]
    if len(i4) != 1 or len(i5) != 11:
        return None
    vals = [4, 4, 5, 5, 5, 5, 5, 10, 10, 10, 10]
    q = [0] * rec["b"]
    # q=0 at the rho=4 source; the 11 rho=5 sources take the common multiset.
    for u, value in zip(i5, vals):
        q[u] = value
    assert sum(q) == sum(rec["s"]) == 73
    p = greedy_p(rec, q)
    if p is None:
        return None
    ok, _ = spill_details(rec, q)
    if not ok:
        return None
    realization = selected_flow_for_q(rec, q)
    if realization is None:
        return None
    selected, x = realization
    if x != rec["s"]:
        return None
    w = {
        "stage": "deterministic_boundary_exact",
        "selected": [sorted(z) for z in selected],
        "q": q,
        "p": p,
    }
    w["check"] = validate_general(rec, w)
    assert w["check"]["extra_selected"] == 0
    return w


def main():
    rows = combined_survivors(); bykey = {(r["layer"], r["state_id"]): r for r in rows}
    first = json.loads((HERE / "FULL_DOMAIN_SPILL_WITNESSES.json").read_text())
    assert first["summary"]["witnessed"] == 4484 and first["summary"]["unresolved"] == 100
    witnesses = {}; stages = Counter()

    for old in first["witnesses"]:
        key = old["layer"], old["state_id"]; rec = bykey[key]
        w = {k: v for k, v in old.items() if k not in ("layer", "state_id", "check")}
        w["stage"] = "pass1_exact"
        w["check"] = validate_general(rec, w)
        assert w["check"]["extra_selected"] == 0 and w["check"]["x"] == rec["s"]
        witnesses[key] = w; stages[w["stage"]] += 1

    unresolved = [(x["layer"], x["state_id"]) for x in first["unresolved"]]
    for index, key in enumerate(unresolved):
        rec = bykey[key]
        w = deeper_exact(rec, index)
        if w is None:
            w = boundary_exact(rec)
        if w is None:
            raise RuntimeError(f"OPEN exact-demand state: {key}")
        w["check"] = validate_general(rec, w)
        assert w["check"]["extra_selected"] == 0 and w["check"]["x"] == rec["s"]
        witnesses[key] = w; stages[w["stage"]] += 1
        print(index + 1, "/100", key, w["stage"], flush=True)

    assert len(witnesses) == 4584 and set(witnesses) == set(bykey)
    ordered = []
    for key in sorted(witnesses):
        rec = bykey[key]; w = witnesses[key]
        again = validate_general(rec, w)
        assert again == w["check"] and again["extra_selected"] == 0 and again["x"] == rec["s"]
        ordered.append({"layer": key[0], "state_id": key[1], **w})

    payload = {
        "schema": "full-domain-spill-exact-demand-positive-witness-v1",
        "date": "2026-09-13",
        "input": {
            "survivors_sha256": hashlib.sha256(read_bytes("survivors.json")).hexdigest(),
            "pool_sha256": hashlib.sha256(read_bytes("pool_inputs.jsonl")).hexdigest(),
            "combined_survivors": 4584,
        },
        "scope": (
            "For every combined compatible-routing survivor, one directly verified pattern has "
            "x_i=s_i exactly and satisfies source eligibility/capacity, selected balance, all "
            "transport tails and the receiver-containment spill inequality.  Hence the spill "
            "inequality adds zero whole-state exclusions even on this exact-demand slice.  "
            "Residual-set placement, exact destinations, heavy-H catalogue data and Hall "
            "routing remain outside this witness statement."
        ),
        "summary": {
            "witnessed": 4584,
            "unresolved": 0,
            "whole_state_exclusions_added": 0,
            "all_exact_demand": True,
            "stage_counts": dict(sorted(stages.items())),
            "minimum_candidate_margin": min(w["check"]["min_candidate_margin"] for w in ordered),
            "minimum_spill_slack": min(w["check"]["min_spill_slack"] for w in ordered),
        },
        "witnesses": ordered,
    }
    (HERE / "FULL_DOMAIN_SPILL_EXACT.json").write_text(json.dumps(payload, separators=(",", ":")) + "\n")
    print(json.dumps(payload["summary"], indent=2))


if __name__ == "__main__":
    main()
