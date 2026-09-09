#!/usr/bin/env python3
"""Exact t=3 ablations of the stripped RX-Hall model.

Variants:
  stripped  - delete residual-column budget and source-label cap inequalities;
              retain RX1, RX2, RX3 and source/supplement transport.
  no-rx2    - additionally delete RX2 from selected source-label compatibility.

Floating LP is used only to propose exact Farkas certificates.  Numerical
feasibility is recorded as a survivor, not as a theorem.
"""
from collections import defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent

# Reuse only generic LP/certificate machinery; this file reconstructs the
# ablated graph-derived model itself.
spec = spec_from_file_location("rx_hall_exact", HERE / "rx_hall_exact.py")
if spec is None or spec.loader is None:
    raise SystemExit("cannot load rx_hall_exact.py")
ex = module_from_spec(spec)
spec.loader.exec_module(ex)
rx = ex.rx


def build_variant(a, b, dmax, s, rho, variant):
    assert variant in {"stripped", "no-rx2"}
    assert len(s) == a and len(rho) == b and min(s) > 0
    LG = rx.groups(s)
    SG = rx.groups(rho)
    m = rx.LP()
    source_types = defaultdict(list)

    # Source-type distributions.
    for k, (rh, nk) in enumerate(SG):
        norm = {}
        for q in range(a - rh + 1):
            pmax = min(rh + b - a - 1, b - 1 - q)
            for p in range(pmax + 1):
                w = m.var(("W", k, q, p))
                source_types[k].append((q, p, w))
                norm[w] = 1
        m.equal(norm, 1)

    # Source -> supplement transport, with the original compatibility rule.
    Pout = defaultdict(list)
    Pin = defaultdict(list)
    for k, (rhk, nk) in enumerate(SG):
        qks = sorted({q for q, p, w in source_types[k] if q > 0})
        for l, (rhl, nl) in enumerate(SG):
            if k == l and nk < 2:
                continue
            qls = sorted({q for q, p, w in source_types[l]})
            for q in qks:
                for q2 in qls:
                    if rhl + q2 < q - 1:
                        continue
                    z = m.var(("P", k, l, q, q2))
                    Pout[k, q].append((l, z))
                    Pin[l, q2].append((k, z))

    for k, (rh, nk) in enumerate(SG):
        for q in sorted({qq for qq, p, w in source_types[k] if qq > 0}):
            row = {}
            for qq, p, w in source_types[k]:
                if qq == q:
                    row[w] = row.get(w, 0) - q
            for l, z in Pout[k, q]:
                row[z] = row.get(z, 0) + SG[l][1] - (k == l)
            m.equal(row, 0)

    for l, (rh, nl) in enumerate(SG):
        for q2 in sorted({qq for qq, p, w in source_types[l]}):
            row = {}
            for qq, p, w in source_types[l]:
                if qq == q2:
                    row[w] = row.get(w, 0) - p
            for k, z in Pin[l, q2]:
                row[z] = row.get(z, 0) + SG[k][1] - (k == l)
            m.equal(row, 0)

    # Label (R,x) distributions.  Deliberately NO residual-column budget.
    label_types = defaultdict(list)
    for g, (sg, ng) in enumerate(LG):
        norm = {}
        for R in range(dmax - sg + 1):
            for x in range(sg, b - R + 1):
                z = m.var(("L", g, R, x))
                label_types[g].append((R, x, z))
                norm[z] = 1
        m.equal(norm, 1)

    # Selected source-label incidence. RX1 and RX3 are retained. RX2 is
    # retained only in the stripped variant.
    by_source = defaultdict(list)
    by_label = defaultdict(list)
    for k, (rh, nk) in enumerate(SG):
        for g, (sg, ng) in enumerate(LG):
            if sg > rh:                         # RX1
                continue
            for q, p, w in source_types[k]:
                if q == 0:
                    continue
                for R, x, lvar in label_types[g]:
                    if variant == "stripped" and R + sg > rh + q - 1:  # RX2
                        continue
                    if R + x < q + p:           # RX3
                        continue
                    z = m.var(("Z", k, g, q, p, R, x))
                    by_source[k, q, p, g].append(z)
                    by_label[g, R, x].append((k, z))

    # Source selected-degree totals. Deliberately NO per-demand-group
    # source-label cap inequality.
    for k, (rh, nk) in enumerate(SG):
        for q, p, w in source_types[k]:
            total = {w: -q}
            for g, (sg, ng) in enumerate(LG):
                for z in by_source[k, q, p, g]:
                    total[z] = total.get(z, 0) + ng
            m.equal(total, 0)

    # Label selected-degree totals.
    for g, (sg, ng) in enumerate(LG):
        for R, x, lvar in label_types[g]:
            row = {lvar: -x}
            for k, z in by_label[g, R, x]:
                row[z] = row.get(z, 0) + SG[k][1]
            m.equal(row, 0)

    ex.add_unit_density_bounds(m)
    return m


def load_hard(demands_path, rows_path, t):
    demands = json.loads(Path(demands_path).read_text())
    hard = []
    for position, line in enumerate(Path(rows_path).read_text().splitlines()):
        if not line.strip():
            continue
        z = list(map(int, line.split()))
        did, total, rho = z[0], z[1], z[2:]
        s = demands[did]["s"]
        if min(s) > 0 and sum(s) == sum(rho) + 2 * t:
            hard.append((position, did, total, s, rho))
    return hard


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--demands-json", type=Path, required=True)
    p.add_argument("--rows", type=Path, required=True)
    p.add_argument("--a", type=int, default=12)
    p.add_argument("--b", type=int, default=16)
    p.add_argument("--dmax", type=int, default=10)
    p.add_argument("--t", type=int, default=3)
    p.add_argument("--variant", choices=["stripped", "no-rx2"], required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()

    hard = load_hard(a.demands_json, a.rows, a.t)
    records = []
    exact_rejections = 0
    numerical_survivors = []
    unresolved = []

    for hard_position, (position, did, total, s, rho) in enumerate(hard):
        model = build_variant(a.a, a.b, a.dmax, s, rho, a.variant)
        cert = ex.exact_certificate(model)
        if cert is not None:
            exact_rejections += 1
            status = "EXACT_INFEASIBLE"
        else:
            # This second solve is diagnostic only. A success is retained as a
            # numerical survivor; any other status is unresolved.
            res = model.solve()
            if res.status == 4:
                n = len(model.names)
                U = model._mat(model.ub, n)
                E = model._mat(model.eq, n)
                import numpy as np
                res = rx.linprog(
                    np.zeros(n), A_ub=U, b_ub=np.array(model.bu, float),
                    A_eq=E, b_eq=np.array(model.be, float), bounds=(0, None),
                    method="highs-ipm"
                )
            if res.success:
                status = "NUMERICAL_FEASIBLE"
                numerical_survivors.append({
                    "hard_position": hard_position,
                    "position": position,
                    "demand_id": did,
                    "total": total,
                    "s": s,
                    "rho": rho,
                })
            else:
                status = "UNRESOLVED"
                unresolved.append({
                    "hard_position": hard_position,
                    "position": position,
                    "demand_id": did,
                    "solver_status": int(res.status),
                    "s": s,
                    "rho": rho,
                })
        records.append({
            "hard_position": hard_position,
            "position": position,
            "demand_id": did,
            "total": total,
            "s": s,
            "rho": rho,
            "status": status,
            "certificate": cert,
        })

    raw = (json.dumps(records, separators=(",", ":"), sort_keys=True) + "\n").encode()
    gz = gzip.compress(raw, mtime=0)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_bytes(gz)
    report = {
        "schema": "general-rx-hall-t3-ablation-exact-v1",
        "variant": a.variant,
        "scope": {"a": a.a, "b": a.b, "dmax": a.dmax, "t": a.t},
        "hard_rows": len(hard),
        "exact_integer_farkas_rejections": exact_rejections,
        "numerical_survivors": numerical_survivors,
        "unresolved": unresolved,
        "deletes_residual_budget": True,
        "deletes_source_label_caps": True,
        "retains_rx1": True,
        "retains_rx2": a.variant == "stripped",
        "retains_rx3": True,
        "retains_source_supplement_transport": True,
        "uses_unordered_pair_aggregate_capacity": False,
        "uses_cumulative_tail_variables": False,
        "unit_density_bounds": True,
        "floating_point_is_proposal_only_for_rejections": True,
        "json_sha256": hashlib.sha256(raw).hexdigest(),
        "gzip_sha256": hashlib.sha256(gz).hexdigest(),
    }
    rp = a.output.with_suffix(a.output.suffix + ".report.json")
    rp.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in {"numerical_survivors", "unresolved"}}, sort_keys=True))


if __name__ == "__main__":
    main()
