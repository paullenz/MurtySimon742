#!/usr/bin/env python3
"""Exact full RX/Hall replay for the 615 N32 t=1 lifted-potential survivors.

This imports the preserved generic positive-demand RX/Hall model and its exact
integer Farkas layer. A row is counted as rejected only when the integer
certificate verifier passes. A row with no certificate is re-solved as a primal
feasibility problem and reported, never silently reclassified.

Run in shards for practical review. Across all shards the expected result is:
  input states       615
  exact rejections   614
  primal survivors     1
  unresolved           0
The unique survivor is s=1^2 2^12, rho=1^10 2^7 and is closed separately by hand.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from scipy.optimize import linprog

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parents[1]
EXACT_PATH = RESEARCH / 'general_n' / '2026-09-09-rx-hall-v1' / 'rx_hall_exact.py'
spec = spec_from_file_location('rx_exact_generic', EXACT_PATH)
if spec is None or spec.loader is None:
    raise SystemExit(f'cannot load {EXACT_PATH}')
ex = module_from_spec(spec)
spec.loader.exec_module(ex)

A = 14
B = 17
DMAX = 12


def load_jsonl(path):
    out = []
    for line in path.read_text().splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def primal_status(model):
    A_ub, b_ub, A_eq, b_eq = ex.arrays(model)
    res = linprog(
        np.zeros(len(model.names)),
        A_ub=A_ub, b_ub=b_ub,
        A_eq=A_eq, b_eq=b_eq,
        bounds=(0, None), method='highs'
    )
    if res.status == 4:
        res = linprog(
            np.zeros(len(model.names)),
            A_ub=A_ub, b_ub=b_ub,
            A_eq=A_eq, b_eq=b_eq,
            bounds=(0, None), method='highs-ipm'
        )
    return res


def cert_digest(cert):
    raw = (json.dumps(cert, separators=(',', ':'), sort_keys=True) + '\n').encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--survivors', type=Path, required=True)
    ap.add_argument('--shard', type=int, default=0)
    ap.add_argument('--shards', type=int, default=1)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if not (0 <= args.shard < args.shards):
        raise SystemExit('bad shard')

    states = load_jsonl(args.survivors)
    assert len(states) == 615
    selected = [x for i, x in enumerate(states) if i % args.shards == args.shard]

    exact = []
    feasible = []
    unresolved = []
    for rec in selected:
        s = tuple(rec['s'])
        rho = tuple(rec['rho'])
        assert min(s) > 0
        model = ex.rx.build_rx_hall(A, B, DMAX, s, rho)
        ex.add_unit_density_bounds(model)
        cert = ex.exact_certificate(model)
        if cert is not None:
            # exact_certificate already calls verify_certificate; call again so
            # this driver visibly treats verification as acceptance.
            rhs = ex.verify_certificate(model, cert)
            exact.append({
                'state_id': rec['state_id'],
                'rhs': rhs,
                'certificate_sha256': cert_digest(cert),
                'variables': cert['variables'],
                'inequalities': cert['inequalities'],
                'equalities': cert['equalities'],
            })
            continue

        res = primal_status(model)
        if res.success:
            feasible.append(rec)
        elif res.status == 2:
            unresolved.append({
                'state_id': rec['state_id'],
                'reason': 'numerically infeasible but no exact certificate',
            })
        else:
            unresolved.append({
                'state_id': rec['state_id'],
                'reason': f'solver status {res.status}: {res.message}',
            })

    out = {
        'schema': 'n32-t1-full-rx-exact-shard-v1',
        'status': 'PASS' if not unresolved else 'FAIL_UNRESOLVED',
        'scope': {'n':32,'Delta':17,'m':256,'a':A,'b':B,'t':1,'dmax':DMAX},
        'shard': args.shard,
        'shards': args.shards,
        'input_states_total': len(states),
        'rows_in_shard': len(selected),
        'exact_rejections': len(exact),
        'primal_survivors': feasible,
        'unresolved': unresolved,
        'certificate_records': exact,
        'floating_point_is_proposal_only': True,
        'integer_farkas_is_acceptance': True,
        'uses_generic_preserved_rx_hall_model': True,
        'interpretation': 'Aggregate all shards: expected 614 exact rejections, one primal survivor, zero unresolved. The survivor is handled by HAND_EXCEPTION.md.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'certificate_records'}, indent=2, sort_keys=True))
    if unresolved:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
