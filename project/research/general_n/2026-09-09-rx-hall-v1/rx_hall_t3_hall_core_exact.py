#!/usr/bin/env python3
"""Exact proof-producing t=3 RX-Hall Hall-core reduction.

This model is a deliberately much weaker necessary-condition system than the
previous RX-Hall LP.  It removes:
  * all source/supplement P variables;
  * all residual-label R variables and the residual budget;
  * all selected-incidence Z variables;
  * RX2;
  * source-label grouped cap inequalities;
  * cumulative tails and unordered-pair aggregate capacity.

It retains only source-type distributions, an elementary RX1 source-degree
cap, nested transport threshold cuts, label extra-load distributions, total
selected incidence, and Hall cuts for unions of at most two compatibility
rectangles.  Floating point proposes Farkas multipliers; exact integer
arithmetic accepts them.
"""
from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("rx_hall_exact", HERE / "rx_hall_exact.py")
if spec is None or spec.loader is None:
    raise SystemExit("cannot load rx_hall_exact.py")
ex = module_from_spec(spec)
spec.loader.exec_module(ex)
rx = ex.rx


def groups(vals):
    return sorted(Counter(vals).items())


def build_hall_core(a, b, dmax, s, rho):
    assert len(s) == a and len(rho) == b and min(s) > 0
    SG = groups(rho)
    LG = groups(s)
    m = rx.LP()
    source_types = defaultdict(list)
    source_attrs = []

    # RX1 plus simplicity gives the pointwise cap
    # q_u <= #{i : s_i <= rho_u}.
    for k, (rh, nk) in enumerate(SG):
        nlabels = sum(1 for si in s if si <= rh)
        norm = {}
        qmax = min(a - rh, nlabels)
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

    # Every selected missing pair has one source and one supplement.
    balance = {}
    for k, (rh, nk) in enumerate(SG):
        for q, p, h, w in source_types[k]:
            balance[w] = nk * (q - p)
    m.equal(balance, 0)

    # Nested transport Hall cuts.  If q_u >= k+1, every one of u's q_u
    # outgoing source/supplement arcs must land at a target w with
    # rho_w+q_w >= k.  Allowing self-targets only weakens the system.
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

    # RX3 and R_i <= dmax-s_i imply, for y_i=x_i-s_i,
    # y_i >= q_u+p_u-dmax on every selected source-label incidence.
    # We retain only y and x=s+y; R disappears entirely.
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

    # Total selected source degree equals total selected label degree.
    total = {}
    for k, (rh, nk) in enumerate(SG):
        for q, p, h, w in source_types[k]:
            total[w] = total.get(w, 0) + nk * q
    for g, (sg, ng) in enumerate(LG):
        for y, x, lvar in label_types[g]:
            total[lvar] = total.get(lvar, 0) - ng * x
    m.equal(total, 0)

    # A source type (rho,h) can use only the compatibility rectangle
    # N(rho,h)={(s,y): s<=rho, y>=h}.  For any union D of one or two such
    # rectangles, every source type whose whole neighborhood is contained in
    # D must send all q of its incidences into labels in D.  This gives an
    # ordinary Hall capacity inequality.  Pair-unions are a strict subset of
    # all possible staircase Hall cuts, hence this remains a relaxation.
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

    # Deterministic ordering makes model/certificate replay stable.
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

    ex.add_unit_density_bounds(m)
    m.hall_core_metadata = {
        "source_attribute_pairs": len(attr_pairs),
        "one_or_two_rectangle_domains": len(domains),
    }
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
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()

    hard = load_hard(a.demands_json, a.rows, a.t)
    records = []
    unresolved = []
    domain_counts = []
    for hard_position, (position, did, total, s, rho) in enumerate(hard):
        model = build_hall_core(a.a, a.b, a.dmax, s, rho)
        cert = ex.exact_certificate(model)
        if cert is None:
            unresolved.append({
                "hard_position": hard_position,
                "position": position,
                "demand_id": did,
                "s": s,
                "rho": rho,
            })
        domain_counts.append(model.hall_core_metadata["one_or_two_rectangle_domains"])
        records.append({
            "hard_position": hard_position,
            "position": position,
            "demand_id": did,
            "total": total,
            "s": s,
            "rho": rho,
            "hall_core_metadata": model.hall_core_metadata,
            "certificate": cert,
        })

    raw = (json.dumps(records, separators=(",", ":"), sort_keys=True) + "\n").encode()
    gz = gzip.compress(raw, mtime=0)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_bytes(gz)
    rhs = [r["certificate"]["rhs"] for r in records if r["certificate"] is not None]
    report = {
        "schema": "general-rx-hall-t3-hall-core-exact-v1",
        "scope": {"a": a.a, "b": a.b, "dmax": a.dmax, "t": a.t},
        "hard_rows": len(hard),
        "exact_integer_farkas_rejections": len(hard) - len(unresolved),
        "unresolved": unresolved,
        "hall_domains_min": min(domain_counts) if domain_counts else None,
        "hall_domains_max": max(domain_counts) if domain_counts else None,
        "rhs_min": min(rhs) if rhs else None,
        "rhs_max": max(rhs) if rhs else None,
        "removes_P_transport_variables": True,
        "removes_R_residual_variables_and_budget": True,
        "removes_Z_incidence_variables": True,
        "uses_rx2": False,
        "uses_rx1_pointwise_q_cap": True,
        "uses_rx3_load_consequence": True,
        "uses_nested_transport_threshold_cuts": True,
        "uses_hall_unions_of_at_most_two_rectangles": True,
        "uses_all_staircase_hall_cuts": False,
        "uses_unordered_pair_aggregate_capacity": False,
        "uses_cumulative_tail_variables": False,
        "floating_point_is_proposal_only": True,
        "integer_farkas_is_acceptance": True,
        "json_sha256": hashlib.sha256(raw).hexdigest(),
        "gzip_sha256": hashlib.sha256(gz).hexdigest(),
    }
    rp = a.output.with_suffix(a.output.suffix + ".report.json")
    rp.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "unresolved"}, sort_keys=True))
    if unresolved:
        raise SystemExit(f"{len(unresolved)} Hall-core rows lack exact certificates")


if __name__ == "__main__":
    main()
