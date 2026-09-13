#!/usr/bin/env python3
"""Exact finite checks for POTENTIAL_PAIR_CAPACITY.md.

The proof is elementary; this verifier protects the implemented closed-form
potential degree against sign/boundary mistakes. It exhausts small q,rho
profiles and checks:

  * D(u,w) or D(w,u) equals the symmetric criterion;
  * the closed-form d_KD(u) equals direct pair enumeration;
  * the threshold upper bound in (8) dominates d_KD(u).
"""
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def direct_pair(q, rho, u, w):
    if u == w:
        return False
    c = [q[i] + rho[i] for i in range(len(q))]
    d_uw = q[u] <= c[w] + 1 and q[w] <= c[u]
    d_wu = q[w] <= c[u] + 1 and q[u] <= c[w]
    return d_uw or d_wu


def symmetric_pair(q, rho, u, w):
    if u == w:
        return False
    c = [q[i] + rho[i] for i in range(len(q))]
    weak = c[w] >= q[u] - 1 and q[w] <= c[u] + 1
    forbidden = c[w] == q[u] - 1 and q[w] == c[u] + 1
    return weak and not forbidden


def closed_degree(q, rho, u):
    c = [q[i] + rho[i] for i in range(len(q))]
    weak = sum(c[w] >= q[u] - 1 and q[w] <= c[u] + 1 for w in range(len(q)))
    boundary = sum(
        w != u and c[w] == q[u] - 1 and q[w] == c[u] + 1
        for w in range(len(q))
    )
    return weak - 1 - boundary


def main():
    profiles = 0
    ordered_pairs = 0
    vertex_checks = 0
    # rho>=1 matches the live positive-surplus setting used for the -1 self
    # deletion in the closed degree formula.
    for n in range(2, 6):
        vals = [(q, rho) for q in range(4) for rho in range(1, 4)]
        # Exhaust all n-tuples for n<=4; use a deterministic dense subbox at 5
        # to keep CI compact while still covering boundary interactions.
        tuples = product(vals, repeat=n)
        limit = None if n <= 4 else 100000
        for idx, qr in enumerate(tuples):
            if limit is not None and idx >= limit:
                break
            q = [x[0] for x in qr]
            rho = [x[1] for x in qr]
            profiles += 1
            for u in range(n):
                direct_deg = 0
                for w in range(n):
                    if u == w:
                        continue
                    a = direct_pair(q, rho, u, w)
                    b = symmetric_pair(q, rho, u, w)
                    assert a == b, (q, rho, u, w, a, b)
                    direct_deg += a
                    ordered_pairs += 1
                cd = closed_degree(q, rho, u)
                assert cd == direct_deg, (q, rho, u, cd, direct_deg)
                c = [q[i] + rho[i] for i in range(n)]
                threshold = min(
                    sum(c[w] >= q[u] - 1 for w in range(n)),
                    sum(q[w] <= c[u] + 1 for w in range(n)),
                ) - 1
                assert direct_deg <= threshold
                vertex_checks += 1

    report = {
        "schema": "potential-pair-capacity-verification-v1",
        "profiles_checked": profiles,
        "ordered_pair_checks": ordered_pairs,
        "vertex_degree_checks": vertex_checks,
        "result": "PASS",
        "external_review": "OPEN",
    }
    (HERE / "POTENTIAL_PAIR_CAPACITY_VERIFICATION.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
