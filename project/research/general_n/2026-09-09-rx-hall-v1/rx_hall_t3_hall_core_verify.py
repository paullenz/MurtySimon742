#!/usr/bin/env python3
"""Standard-library verifier for t=3 Hall-core Farkas certificates.

No SciPy and no import of the generator/model builder.  This file independently
reconstructs the tiny Hall-core integer system and checks every saved Farkas
certificate by exact integer arithmetic.
"""
from collections import Counter, defaultdict
from pathlib import Path
import argparse
import gzip
import json


def groups(vals):
    return sorted(Counter(vals).items())


class Model:
    def __init__(self):
        self.names = []
        self.eq = []
        self.be = []
        self.ub = []
        self.bu = []

    def var(self, name):
        self.names.append(name)
        return len(self.names) - 1

    def equal(self, row, rhs=0):
        self.eq.append({j: c for j, c in row.items() if c})
        self.be.append(rhs)

    def le(self, row, rhs=0):
        self.ub.append({j: c for j, c in row.items() if c})
        self.bu.append(rhs)


def build(a, b, dmax, s, rho):
    SG = groups(rho)
    LG = groups(s)
    m = Model()
    source_types = defaultdict(list)
    source_attrs = []

    for k, (rh, nk) in enumerate(SG):
        nlabels = sum(1 for si in s if si <= rh)
        qmax = min(a - rh, nlabels)
        norm = {}
        for q in range(qmax + 1):
            pmax = min(rh + b - a - 1, b - 1 - q)
            for p in range(pmax + 1):
                h = max(0, q + p - dmax)
                w = m.var(("W", k, q, p))
                source_types[k].append((q, p, h, w))
                norm[w] = 1
                if q > 0:
                    source_attrs.append((w, rh, h, nk, q))
        m.equal(norm, 1)

    row = {}
    for k, (rh, nk) in enumerate(SG):
        for q, p, h, w in source_types[k]:
            row[w] = nk * (q - p)
    m.equal(row, 0)

    for threshold in range(1, a + 1):
        row = {}
        for k, (rh, nk) in enumerate(SG):
            for q, p, h, w in source_types[k]:
                c = 0
                if q >= threshold + 1:
                    c += nk * q
                if rh + q >= threshold:
                    c -= nk * p
                if c:
                    row[w] = c
        m.le(row, 0)

    label_types = defaultdict(list)
    label_attrs = []
    for g, (sg, ng) in enumerate(LG):
        norm = {}
        for y in range(b - sg + 1):
            x = sg + y
            lvar = m.var(("L", g, y))
            label_types[g].append((y, x, lvar))
            label_attrs.append((lvar, sg, y, ng, x))
            norm[lvar] = 1
        m.equal(norm, 1)

    row = {}
    for k, (rh, nk) in enumerate(SG):
        for q, p, h, w in source_types[k]:
            row[w] = row.get(w, 0) + nk * q
    for g, (sg, ng) in enumerate(LG):
        for y, x, lvar in label_types[g]:
            row[lvar] = row.get(lvar, 0) - ng * x
    m.equal(row, 0)

    def neighborhood(rh, h):
        return frozenset(
            i for i, (_, sg, y, _, _) in enumerate(label_attrs)
            if sg <= rh and y >= h
        )

    attr_pairs = sorted(set((rh, h) for _, rh, h, _, _ in source_attrs))
    masks = {key: neighborhood(*key) for key in attr_pairs}
    domains = set(masks.values())
    for i, u in enumerate(attr_pairs):
        for v in attr_pairs[i:]:
            domains.add(masks[u] | masks[v])
    domains = sorted(domains, key=lambda D: (len(D), tuple(sorted(D))))

    for D in domains:
        row = {}
        has_source = False
        for w, rh, h, nk, q in source_attrs:
            if masks[(rh, h)] <= D:
                row[w] = row.get(w, 0) + nk * q
                has_source = True
        if not has_source:
            continue
        for i in D:
            lvar, sg, y, ng, x = label_attrs[i]
            row[lvar] = row.get(lvar, 0) - ng * x
        m.le(row, 0)

    for j in range(len(m.names)):
        m.le({j: 1}, 1)

    return m, len(domains)


def strict_int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def verify_cert(m, cert):
    assert strict_int(cert["variables"]) and cert["variables"] == len(m.names)
    assert strict_int(cert["inequalities"]) and cert["inequalities"] == len(m.ub)
    assert strict_int(cert["equalities"]) and cert["equalities"] == len(m.eq)
    assert strict_int(cert["rhs"]) and cert["rhs"] < 0
    coef = [0] * len(m.names)
    rhs = 0

    seen = set()
    for pair in cert["ub"]:
        assert isinstance(pair, list) and len(pair) == 2
        i, w = pair
        assert strict_int(i) and strict_int(w) and w > 0
        assert 0 <= i < len(m.ub) and i not in seen
        seen.add(i)
        rhs += w * m.bu[i]
        for j, c in m.ub[i].items():
            coef[j] += w * c

    seen = set()
    for pair in cert["eq"]:
        assert isinstance(pair, list) and len(pair) == 2
        i, w = pair
        assert strict_int(i) and strict_int(w) and w != 0
        assert 0 <= i < len(m.eq) and i not in seen
        seen.add(i)
        rhs += w * m.be[i]
        for j, c in m.eq[i].items():
            coef[j] += w * c

    assert min(coef, default=0) >= 0
    assert rhs == cert["rhs"]
    return rhs


def hard_rows(demands_path, rows_path, t):
    demands = json.loads(Path(demands_path).read_text())
    out = []
    for position, line in enumerate(Path(rows_path).read_text().splitlines()):
        if not line.strip():
            continue
        z = list(map(int, line.split()))
        did, total, rho = z[0], z[1], z[2:]
        s = demands[did]["s"]
        if min(s) > 0 and sum(s) == sum(rho) + 2 * t:
            out.append((position, did, total, s, rho))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--demands-json", type=Path, required=True)
    p.add_argument("--rows", type=Path, required=True)
    p.add_argument("--certificates", type=Path, required=True)
    p.add_argument("--a", type=int, default=12)
    p.add_argument("--b", type=int, default=16)
    p.add_argument("--dmax", type=int, default=10)
    p.add_argument("--t", type=int, default=3)
    a = p.parse_args()

    expected = hard_rows(a.demands_json, a.rows, a.t)
    records = json.loads(gzip.decompress(a.certificates.read_bytes()))
    assert len(records) == len(expected)
    rhs_values = []
    domains = []
    for hp, (rec, exp) in enumerate(zip(records, expected)):
        position, did, total, s, rho = exp
        assert rec["hard_position"] == hp
        assert rec["position"] == position
        assert rec["demand_id"] == did
        assert rec["total"] == total
        assert rec["s"] == s
        assert rec["rho"] == rho
        assert isinstance(rec["certificate"], dict)
        model, nd = build(a.a, a.b, a.dmax, s, rho)
        assert rec["hall_core_metadata"]["one_or_two_rectangle_domains"] == nd
        rhs_values.append(verify_cert(model, rec["certificate"]))
        domains.append(nd)

    report = {
        "schema": "general-rx-hall-t3-hall-core-independent-check-v1",
        "status": "PASS",
        "records_checked": len(records),
        "rhs_min": min(rhs_values),
        "rhs_max": max(rhs_values),
        "hall_domains_min": min(domains),
        "hall_domains_max": max(domains),
        "standard_library_only": True,
        "imports_generator": False,
        "imports_scipy": False,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
