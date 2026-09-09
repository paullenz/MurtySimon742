#!/usr/bin/env python3
"""Exact integer Farkas layer for the stripped RX-Hall model.

Floating-point LP is used only to propose a dual ray.  A row is rejected only
when the proposed multipliers are converted to integers and independently
checked against the integer coefficient dictionaries of the reconstructed
model.

The RX-Hall variables W, P, L and Z are fractions/densities of vertex, ordered
pair, label and incidence classes.  Hence every graph image has 0 <= x <= 1.
The exact model makes these elementary unit upper bounds explicit.  It still
omits the old unordered-pair aggregate capacity constraints and all cumulative
selected-degree tail variables.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from functools import reduce
from math import gcd
import argparse
import gzip
import hashlib
import json
import time

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, hstack, vstack


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rx_hall_scan.py"
spec = spec_from_file_location("rx_hall_scan_original", SOURCE)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot load {SOURCE}")
rx = module_from_spec(spec)
spec.loader.exec_module(rx)


def add_unit_density_bounds(model):
    """Add x<=1 for every fraction/density variable and remember their rows."""
    model.bound_start = len(model.ub)
    for j in range(len(model.names)):
        model.le({j: 1}, 1)
    return model


def arrays(model):
    n = len(model.names)
    A = model._mat(model.ub, n)
    E = model._mat(model.eq, n)
    b = np.array(model.bu, float)
    f = np.array(model.be, float)
    return A, b, E, f


def propose_farkas(model):
    """Return a nonnegative split-dual proposal or None."""
    A, b, E, f = arrays(model)
    n = len(model.names)
    nu = len(model.ub)
    ne = len(model.eq)

    # lambda >= 0 for A x <= b; mu = mu+ - mu- for E x = f.
    # Require lambda A + mu E >= 0 and lambda b + mu f <= -1.
    D = hstack([-A.T, -E.T, E.T], format="csr")
    D = vstack(
        [D, csr_matrix(np.r_[b, f, -f].reshape(1, -1))],
        format="csr",
    )
    rhs = np.r_[np.zeros(n), -1.0]
    objective = np.ones(nu + 2 * ne)
    res = linprog(objective, A_ub=D, b_ub=rhs, bounds=(0, None), method="highs")
    if not res.success:
        res = linprog(
            objective, A_ub=D, b_ub=rhs, bounds=(0, None), method="highs-ipm"
        )
    return res if res.success else None


def verify_certificate(model, cert):
    assert cert["variables"] == len(model.names)
    assert cert["inequalities"] == len(model.ub)
    assert cert["equalities"] == len(model.eq)
    coef = [0] * len(model.names)
    rhs = 0

    seen = set()
    for i, w in cert["ub"]:
        assert i not in seen and 0 <= i < len(model.ub)
        assert isinstance(w, int) and w >= 0
        seen.add(i)
        row = model.ub[i]
        rhs += w * model.bu[i]
        for j, a in row.items():
            coef[j] += w * a

    seen = set()
    for i, w in cert["eq"]:
        assert i not in seen and 0 <= i < len(model.eq)
        assert isinstance(w, int)
        seen.add(i)
        row = model.eq[i]
        rhs += w * model.be[i]
        for j, a in row.items():
            coef[j] += w * a

    assert min(coef) >= 0
    assert rhs == cert["rhs"] and rhs < 0
    return rhs


def exact_certificate(model):
    """Propose numerically, round, repair with valid x<=1 rows, verify exactly."""
    res = propose_farkas(model)
    if res is None:
        return None

    nu = len(model.ub)
    ne = len(model.eq)
    n = len(model.names)
    for scale in (1_000, 1_000_000, 1_000_000_000, 1_000_000_000_000):
        lam = [max(0, round(float(x) * scale)) for x in res.x[:nu]]
        mu = [
            round(float(x - y) * scale)
            for x, y in zip(res.x[nu : nu + ne], res.x[nu + ne :])
        ]

        coef = [0] * n
        rhs = 0
        for row, b, w in zip(model.ub, model.bu, lam):
            if not w:
                continue
            rhs += w * b
            for j, a in row.items():
                coef[j] += w * a
        for row, f, w in zip(model.eq, model.be, mu):
            if not w:
                continue
            rhs += w * f
            for j, a in row.items():
                coef[j] += w * a

        # Rounding may leave tiny negative variable coefficients.  Because the
        # unit density rows x_j<=1 are part of the exact necessary-condition
        # model, add the exact amount required to make each coefficient zero.
        for j, c in enumerate(coef):
            if c < 0:
                lam[model.bound_start + j] -= c
                rhs -= c
                coef[j] = 0

        if rhs < 0:
            factor = reduce(gcd, lam + [abs(x) for x in mu]) or 1
            cert = {
                "ub": [(i, w // factor) for i, w in enumerate(lam) if w],
                "eq": [(i, w // factor) for i, w in enumerate(mu) if w],
                "rhs": rhs // factor,
                "variables": n,
                "inequalities": nu,
                "equalities": ne,
                "rounding_scale": scale,
            }
            verify_certificate(model, cert)
            return cert
    return None


def load_hard_rows(demands_path, rows_path, t):
    demands = json.loads(Path(demands_path).read_text())
    rows = []
    hard = []
    for position, line in enumerate(Path(rows_path).read_text().splitlines()):
        if not line.strip():
            continue
        z = list(map(int, line.split()))
        did, total, rho = z[0], z[1], z[2:]
        s = demands[did]["s"]
        rows.append((position, did, total, s, rho))
        if min(s) > 0 and sum(s) == sum(rho) + 2 * t:
            hard.append((position, did, total, s, rho))
    return rows, hard


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--demands-json", type=Path, required=True)
    p.add_argument("--rows", type=Path, required=True)
    p.add_argument("--a", type=int, required=True)
    p.add_argument("--b", type=int, required=True)
    p.add_argument("--dmax", type=int, required=True)
    p.add_argument("--t", type=int, required=True)
    p.add_argument("--shard", type=int, default=0)
    p.add_argument("--shards", type=int, default=1)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    if not (0 <= a.shard < a.shards):
        raise SystemExit("bad shard")

    _, hard = load_hard_rows(a.demands_json, a.rows, a.t)
    selected = [x for hp, x in enumerate(hard) if hp % a.shards == a.shard]
    start = time.time()
    records = []
    unresolved = []

    for local, (position, did, total, s, rho) in enumerate(selected):
        model = rx.build_rx_hall(a.a, a.b, a.dmax, s, rho)
        add_unit_density_bounds(model)
        cert = exact_certificate(model)
        rec = {
            "position": position,
            "demand_id": did,
            "total": total,
            "s": s,
            "rho": rho,
            "certificate": cert,
        }
        records.append(rec)
        if cert is None:
            unresolved.append({k: rec[k] for k in ("position", "demand_id", "total", "s", "rho")})

    raw = (json.dumps(records, separators=(",", ":"), sort_keys=True) + "\n").encode()
    gz = gzip.compress(raw, mtime=0)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_bytes(gz)

    rhs = [r["certificate"]["rhs"] for r in records if r["certificate"] is not None]
    report = {
        "schema": "general-rx-hall-exact-shard-v1",
        "scope": {"a": a.a, "b": a.b, "dmax": a.dmax, "t": a.t},
        "shard": a.shard,
        "shards": a.shards,
        "hard_rows_total": len(hard),
        "rows_in_shard": len(selected),
        "exact_rejections": len(selected) - len(unresolved),
        "unresolved": unresolved,
        "rhs_min": min(rhs) if rhs else None,
        "rhs_max": max(rhs) if rhs else None,
        "json_sha256": hashlib.sha256(raw).hexdigest(),
        "gzip_sha256": hashlib.sha256(gz).hexdigest(),
        "seconds": time.time() - start,
        "unit_density_bounds": True,
        "uses_unordered_pair_aggregate_capacity": False,
        "uses_cumulative_tail_variables": False,
        "floating_point_is_proposal_only": True,
        "integer_farkas_is_acceptance": True,
    }
    rp = a.output.with_suffix(a.output.suffix + ".report.json")
    rp.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "unresolved"}, sort_keys=True))
    if unresolved:
        raise SystemExit(f"{len(unresolved)} rows lack exact certificates")


if __name__ == "__main__":
    main()
