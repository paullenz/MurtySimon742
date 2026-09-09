#!/usr/bin/env python3
"""Standard-library verifier for RX-Hall integer Farkas certificates.

This file deliberately imports neither SciPy nor the certificate generator nor
the reconnaissance scanner.  It independently reconstructs the integer model
and verifies coverage plus every saved certificate by integer arithmetic.
"""
from collections import defaultdict
from pathlib import Path
import argparse
import gzip
import json


def groups(vals):
    d = {}
    for x in vals:
        d[x] = d.get(x, 0) + 1
    return sorted(d.items())


class ExactModel:
    def __init__(self):
        self.names = []
        self.eq = []
        self.be = []
        self.ub = []
        self.bu = []
        self.bound_start = None

    def var(self, name):
        self.names.append(name)
        return len(self.names) - 1

    def equal(self, row, rhs=0):
        self.eq.append({j: c for j, c in row.items() if c})
        self.be.append(rhs)

    def le(self, row, rhs):
        self.ub.append({j: c for j, c in row.items() if c})
        self.bu.append(rhs)


def build_model(a, b, dmax, s, rho):
    assert len(s) == a and len(rho) == b and min(s) > 0
    r = sum(rho)
    LG = groups(s)
    SG = groups(rho)
    m = ExactModel()

    source_types = defaultdict(list)
    for k, (rh, nk) in enumerate(SG):
        norm = {}
        for q in range(a - rh + 1):
            pmax = min(rh + b - a - 1, b - 1 - q)
            for p in range(pmax + 1):
                w = m.var(("W", k, q, p))
                source_types[k].append((q, p, w))
                norm[w] = 1
        m.equal(norm, 1)

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

    label_types = defaultdict(list)
    for g, (sg, ng) in enumerate(LG):
        norm = {}
        for R in range(dmax - sg + 1):
            for x in range(sg, b - R + 1):
                z = m.var(("L", g, R, x))
                label_types[g].append((R, x, z))
                norm[z] = 1
        m.equal(norm, 1)

    residual = {}
    for g, (sg, ng) in enumerate(LG):
        for R, x, z in label_types[g]:
            residual[z] = residual.get(z, 0) + ng * R
    m.equal(residual, r)

    by_source = defaultdict(list)
    by_label = defaultdict(list)
    for k, (rh, nk) in enumerate(SG):
        for g, (sg, ng) in enumerate(LG):
            if sg > rh:
                continue
            for q, p, w in source_types[k]:
                if q == 0:
                    continue
                for R, x, lvar in label_types[g]:
                    if R + sg > rh + q - 1:
                        continue
                    if R + x < q + p:
                        continue
                    z = m.var(("Z", k, g, q, p, R, x))
                    by_source[k, q, p, g].append(z)
                    by_label[g, R, x].append((k, z))

    for k, (rh, nk) in enumerate(SG):
        for q, p, w in source_types[k]:
            total = {w: -q}
            for g, (sg, ng) in enumerate(LG):
                cap = {w: -1}
                for z in by_source[k, q, p, g]:
                    cap[z] = cap.get(z, 0) + 1
                    total[z] = total.get(z, 0) + ng
                m.le(cap, 0)
            m.equal(total, 0)

    for g, (sg, ng) in enumerate(LG):
        for R, x, lvar in label_types[g]:
            row = {lvar: -x}
            for k, z in by_label[g, R, x]:
                row[z] = row.get(z, 0) + SG[k][1]
            m.equal(row, 0)

    m.bound_start = len(m.ub)
    for j in range(len(m.names)):
        m.le({j: 1}, 1)
    return m


def strict_int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def verify_certificate(model, cert):
    assert strict_int(cert["variables"]) and cert["variables"] == len(model.names)
    assert strict_int(cert["inequalities"]) and cert["inequalities"] == len(model.ub)
    assert strict_int(cert["equalities"]) and cert["equalities"] == len(model.eq)
    assert strict_int(cert["rhs"]) and cert["rhs"] < 0

    coef = [0] * len(model.names)
    rhs = 0

    seen = set()
    for pair in cert["ub"]:
        assert isinstance(pair, list) and len(pair) == 2
        i, w = pair
        assert strict_int(i) and strict_int(w)
        assert 0 <= i < len(model.ub) and i not in seen and w > 0
        seen.add(i)
        rhs += w * model.bu[i]
        for j, c in model.ub[i].items():
            coef[j] += w * c

    seen = set()
    for pair in cert["eq"]:
        assert isinstance(pair, list) and len(pair) == 2
        i, w = pair
        assert strict_int(i) and strict_int(w)
        assert 0 <= i < len(model.eq) and i not in seen and w != 0
        seen.add(i)
        rhs += w * model.be[i]
        for j, c in model.eq[i].items():
            coef[j] += w * c

    assert min(coef, default=0) >= 0
    assert rhs == cert["rhs"]
    return rhs


def expected_records(demands_path, rows_path, t, shard, shards):
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
    selected = [x for hp, x in enumerate(hard) if hp % shards == shard]
    return len(hard), selected


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--demands-json", type=Path, required=True)
    p.add_argument("--rows", type=Path, required=True)
    p.add_argument("--certificates", type=Path, required=True)
    p.add_argument("--a", type=int, required=True)
    p.add_argument("--b", type=int, required=True)
    p.add_argument("--dmax", type=int, required=True)
    p.add_argument("--t", type=int, required=True)
    p.add_argument("--shard", type=int, default=0)
    p.add_argument("--shards", type=int, default=1)
    a = p.parse_args()
    assert 0 <= a.shard < a.shards

    hard_total, expected = expected_records(
        a.demands_json, a.rows, a.t, a.shard, a.shards
    )
    records = json.loads(gzip.decompress(a.certificates.read_bytes()))
    assert isinstance(records, list) and len(records) == len(expected)

    rhs_values = []
    for rec, exp in zip(records, expected):
        position, did, total, s, rho = exp
        assert rec["position"] == position
        assert rec["demand_id"] == did
        assert rec["total"] == total
        assert rec["s"] == s
        assert rec["rho"] == rho
        assert len(s) == a.a and len(rho) == a.b and min(s) > 0
        assert sum(s) == sum(rho) + 2 * a.t
        cert = rec["certificate"]
        assert isinstance(cert, dict)
        model = build_model(a.a, a.b, a.dmax, s, rho)
        rhs_values.append(verify_certificate(model, cert))

    out = {
        "schema": "general-rx-hall-independent-exact-check-v1",
        "status": "PASS",
        "scope": {"a": a.a, "b": a.b, "dmax": a.dmax, "t": a.t},
        "shard": a.shard,
        "shards": a.shards,
        "hard_rows_total": hard_total,
        "records_checked": len(records),
        "rhs_min": min(rhs_values) if rhs_values else None,
        "rhs_max": max(rhs_values) if rhs_values else None,
        "standard_library_only": True,
        "imports_generator": False,
        "imports_scipy": False,
        "uses_unordered_pair_aggregate_capacity": False,
        "uses_cumulative_tail_variables": False,
    }
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
