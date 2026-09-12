#!/usr/bin/env python3
"""Aggregate exact N32 t=1 replay shards and assert the published ledger."""
from pathlib import Path
import argparse
import glob
import json


def load(path):
    return json.loads(Path(path).read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lifted', type=Path, required=True)
    ap.add_argument('--rx-glob', required=True)
    ap.add_argument('--zero-glob', required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()

    lifted = load(args.lifted)
    assert lifted['status'] == 'PASS'
    assert lifted['frontier_profiles'] == 381
    assert lifted['positive_states'] == 1984
    assert lifted['zero_states'] == 61
    assert lifted['exact_certificates'] == 1369
    assert lifted['survivors'] == 615
    assert len(lifted['monotone_tail_impossible_profiles']) == 1

    rx_files = sorted(glob.glob(args.rx_glob))
    zero_files = sorted(glob.glob(args.zero_glob))
    if not rx_files or not zero_files:
        raise SystemExit('missing shard reports')

    rx_rows = rx_exact = rx_feasible = rx_unresolved = 0
    feasible_states = []
    for p in rx_files:
        z = load(p)
        assert z['status'] == 'PASS'
        rx_rows += z['rows_in_shard']
        rx_exact += z['exact_rejections']
        rx_feasible += len(z['primal_survivors'])
        rx_unresolved += len(z['unresolved'])
        feasible_states.extend(z['primal_survivors'])

    zero_rows = zero_exact = zero_unresolved = 0
    for p in zero_files:
        z = load(p)
        assert z['status'] == 'PASS'
        zero_rows += z['rows_in_shard']
        zero_exact += z['exact_rejections']
        zero_unresolved += len(z['unresolved'])

    assert rx_rows == 615
    assert rx_exact == 614
    assert rx_feasible == 1
    assert rx_unresolved == 0
    assert len(feasible_states) == 1
    survivor = feasible_states[0]
    assert survivor['s'] == [1,1] + [2]*12
    assert survivor['rho'] == [1]*10 + [2]*7

    assert zero_rows == 61
    assert zero_exact == 61
    assert zero_unresolved == 0

    out = {
        'schema': 'n32-t1-equality-aggregate-v1',
        'status': 'PASS',
        'frontier_profiles': 381,
        'monotone_tail_impossible_profiles': 1,
        'positive_states': 1984,
        'lifted_potential_exact_rejections': 1369,
        'full_rx_input_states': 615,
        'full_rx_exact_rejections': 614,
        'full_rx_primal_survivors': 1,
        'full_rx_unresolved': 0,
        'hand_survivor': survivor,
        'zero_demand_states': 61,
        'zero_demand_exact_rejections': 61,
        'zero_demand_unresolved': 0,
        'interpretation': 'All t=1 arithmetic states are accounted for exactly except the one displayed full-RX survivor, which is excluded by HAND_EXCEPTION.md.'
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
