#!/usr/bin/env python3
"""Exact strengthened replay for the 61 zero-demand N32 t=1 states.

Positive-demand compression d=R+s is invalid when s=0. This model therefore
keeps d and R separately, enforces s=max(0,d-R), the exact residual budget
sum R=r, and the exact degree-mass identity sum d=2(r+t). The cap d<=12 is
justified by the isolated-C lemma: at (a,b,t)=(14,17,1), an isolated C-vertex
would force b<=a-1-t, i.e. 17<=12.

The source/supplement and grouped selected-incidence layers are the same safe
necessary conditions as in the preserved RX/Hall model. Acceptance is only by
the preserved exact integer Farkas verifier.

Expected aggregate result over all shards: 61/61 exact rejections, zero unresolved.
"""
from collections import defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parents[1]
SCAN_PATH = RESEARCH / 'general_n' / '2026-09-09-rx-hall-v1' / 'rx_hall_scan.py'
EXACT_PATH = RESEARCH / 'general_n' / '2026-09-09-rx-hall-v1' / 'rx_hall_exact.py'

sp = spec_from_file_location('rx_scan_generic', SCAN_PATH)
if sp is None or sp.loader is None:
    raise SystemExit(f'cannot load {SCAN_PATH}')
rx = module_from_spec(sp)
sp.loader.exec_module(rx)

ep = spec_from_file_location('rx_exact_generic', EXACT_PATH)
if ep is None or ep.loader is None:
    raise SystemExit(f'cannot load {EXACT_PATH}')
ex = module_from_spec(ep)
ep.loader.exec_module(ex)

A = 14
B = 17
DMAX = 12
T = 1


def build_zero_model(s, rho):
    assert len(s) == A and len(rho) == B and min(s) == 0
    r = sum(rho)
    LG = rx.groups(s)
    SG = rx.groups(rho)
    m = rx.LP()
    source_types = defaultdict(list)

    # Source distributions.
    for k, (rh, nk) in enumerate(SG):
        norm = {}
        for q in range(A - rh + 1):
            pmax = min(rh + B - A - 1, B - 1 - q)
            for p in range(pmax + 1):
                w = m.var(('W', k, q, p))
                source_types[k].append((q, p, w))
                norm[w] = 1
        m.equal(norm, 1)

    # Exact grouped source -> supplement transport, as in the generic model.
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
                    z = m.var(('P', k, l, q, q2))
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

    # Label states retain d and R separately. The fixed demand class is exactly
    # s=max(0,d-R). x>=s and R+x<=b are elementary cross-degree conditions.
    label_types = defaultdict(list)
    for g, (sg, ng) in enumerate(LG):
        norm = {}
        for d in range(DMAX + 1):
            for R in range(B + 1):
                if max(0, d - R) != sg:
                    continue
                for x in range(sg, B - R + 1):
                    z = m.var(('L', g, d, R, x))
                    label_types[g].append((d, R, x, z))
                    norm[z] = 1
        if not norm:
            raise RuntimeError(('empty label group', sg))
        m.equal(norm, 1)

    residual = {}
    degree_mass = {}
    for g, (sg, ng) in enumerate(LG):
        for d, R, x, z in label_types[g]:
            residual[z] = residual.get(z, 0) + ng * R
            degree_mass[z] = degree_mass.get(z, 0) + ng * d
    m.equal(residual, r)
    m.equal(degree_mass, 2 * (r + T))

    # Selected source-label incidence. Necessary compatibility is
    # s<=rho, d<=rho+q-1, R+x>=q+p.
    by_source = defaultdict(list)
    by_label = defaultdict(list)
    for k, (rh, nk) in enumerate(SG):
        for g, (sg, ng) in enumerate(LG):
            if sg > rh:
                continue
            for q, p, w in source_types[k]:
                if q == 0:
                    continue
                for d, R, x, lvar in label_types[g]:
                    if d > rh + q - 1:
                        continue
                    if R + x < q + p:
                        continue
                    z = m.var(('Z', k, g, q, p, d, R, x))
                    by_source[k, q, p, g].append(z)
                    by_label[g, d, R, x].append((k, z))

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
        for d, R, x, lvar in label_types[g]:
            row = {lvar: -x}
            for k, z in by_label[g, d, R, x]:
                row[z] = row.get(z, 0) + SG[k][1]
            m.equal(row, 0)

    return m


def load_jsonl(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]


def digest(cert):
    raw = (json.dumps(cert, separators=(',', ':'), sort_keys=True) + '\n').encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--zero-states', type=Path, required=True)
    ap.add_argument('--shard', type=int, default=0)
    ap.add_argument('--shards', type=int, default=1)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if not (0 <= args.shard < args.shards):
        raise SystemExit('bad shard')

    states = load_jsonl(args.zero_states)
    assert len(states) == 61
    selected = [x for i, x in enumerate(states) if i % args.shards == args.shard]

    records = []
    unresolved = []
    for rec in selected:
        model = build_zero_model(tuple(rec['s']), tuple(rec['rho']))
        ex.add_unit_density_bounds(model)
        cert = ex.exact_certificate(model)
        if cert is None:
            unresolved.append({'state_id': rec['state_id'], 'reason': 'no exact Farkas certificate'})
            continue
        rhs = ex.verify_certificate(model, cert)
        records.append({
            'state_id': rec['state_id'],
            'rhs': rhs,
            'certificate_sha256': digest(cert),
            'variables': cert['variables'],
            'inequalities': cert['inequalities'],
            'equalities': cert['equalities'],
        })

    out = {
        'schema': 'n32-t1-zero-demand-exact-shard-v1',
        'status': 'PASS' if not unresolved else 'FAIL_UNRESOLVED',
        'scope': {'n':32,'Delta':17,'m':256,'a':A,'b':B,'t':T,'dmax':DMAX},
        'shard': args.shard,
        'shards': args.shards,
        'input_states_total': len(states),
        'rows_in_shard': len(selected),
        'exact_rejections': len(records),
        'unresolved': unresolved,
        'certificate_records': records,
        'exact_degree_mass_enforced': True,
        'd_and_R_kept_separate': True,
        'integer_farkas_is_acceptance': True,
        'interpretation': 'Aggregate all shards: expected 61 exact rejections and zero unresolved.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'certificate_records'}, indent=2, sort_keys=True))
    if unresolved:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
