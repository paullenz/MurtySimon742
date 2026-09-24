"""Stable-index v4 screen with explicit unresolved cases and per-case evidence.

All conclusions are internal numerical MILP conclusions conditional on the
model. Unknowns are never exclusions and prevent a successful final verdict.
"""
import argparse
import collections
import hashlib
import itertools
import json
import sys
from pathlib import Path
from screen_demand_15_16 import partitions, f
from witness_deficit_exact_star_milp import solve_aggregated


def profiles(n, Delta):
    rho = 2*Delta-n
    Dmax = n*rho//2-2 if n % 2 == 0 else (n*rho-3)//2
    a = n-1-Delta
    index = 0
    for total in (15, 16):
        for demand in partitions(total):
            if len(demand) > a or (total == 16 and min(demand) < 2):
                continue
            ranges = [range(d, (Delta-1+d)//2+1) for d in demand]
            for xs in itertools.product(*ranges):
                if any(demand[j] == demand[j-1] and xs[j] > xs[j-1]
                       for j in range(1, len(demand))):
                    continue
                hs = [2*x-d for x, d in zip(xs, demand)]
                if any(x > (Delta-h)*(Delta-2) for x, h in zip(xs, hs)):
                    continue
                if max(hs)*Dmax < sum(f(x, rho) for x in xs):
                    continue
                if sum(xs) > Delta*(Delta-1)//2:
                    continue
                index += 1
                yield index, total, demand, xs


def main(n, Delta, resume_scalar=0, stop_scalar=None, time_limit=10, record_path=None):
    if not (n >= 4 and 0 < Delta < n and resume_scalar >= 0 and time_limit > 0):
        raise ValueError('invalid row, resume index or time limit')
    if stop_scalar is not None and stop_scalar <= resume_scalar:
        raise ValueError('stop must exceed resume index')
    rho = 2*Delta-n
    Dmax = n*rho//2-2 if n % 2 == 0 else (n*rho-3)//2
    survivors, unresolved = [], []
    counts = collections.Counter()
    best = None
    completed = 0
    last = resume_scalar
    exhausted = True
    stream = Path(record_path).open('w') if record_path else None
    record_hash = hashlib.sha256()
    try:
        for index, total, demand, xs in profiles(n, Delta):
            if index <= resume_scalar:
                continue
            if stop_scalar is not None and index > stop_scalar:
                exhausted = False
                break
            last = index
            try:
                row = solve_aggregated(list(demand), list(xs), rho, Delta, time_limit)
                row.update(stable_index=index, total_demand=total)
                if row['status'] not in (0, 2):
                    raise RuntimeError('unresolved solver status')
                if row['status'] == 0 and row['minimum_deficit'] is None:
                    raise RuntimeError('optimal result has no validated objective')
                counts[str(row['status'])] += 1
                completed += 1
                if row['minimum_deficit'] is not None:
                    row['gap_vs_Dmax'] = row['minimum_deficit']-Dmax
                    if row['gap_vs_Dmax'] <= 0:
                        survivors.append(row)
                        print('SURVIVOR '+json.dumps(row), flush=True)
                    if best is None or row['gap_vs_Dmax'] < best['gap_vs_Dmax']:
                        best = row
            except RuntimeError as exc:
                row = dict(stable_index=index, total_demand=total,
                           demands=list(demand), x=list(xs), status='UNRESOLVED',
                           error=str(exc), minimum_deficit=None)
                unresolved.append(row)
                counts['UNRESOLVED'] += 1
                print('UNRESOLVED '+json.dumps(row), flush=True)
            encoded = (json.dumps(row, sort_keys=True, separators=(',', ':'))+'\n').encode()
            record_hash.update(encoded)
            if stream:
                stream.write(encoded.decode());stream.flush()
        if last == resume_scalar and exhausted:
            # No claim to have processed requested out-of-domain indices.
            last = min(resume_scalar, sum(1 for _ in profiles(n, Delta)))
    finally:
        if stream:
            stream.close()
    result = dict(model='exact-small-star-v4-status-safe', n=n, Delta=Delta,
                  rho=rho, Dmax=Dmax, range=[resume_scalar+1,last],
                  cases_resolved=completed, solver_status_counts=dict(counts),
                  unresolved_count=len(unresolved), unresolved=unresolved,
                  survivor_count=len(survivors), survivors=survivors, closest=best,
                  enumeration_exhausted=exhausted, range_complete=not unresolved,
                  case_records_sha256=record_hash.hexdigest(),
                  abstract_full_row_excluded=(resume_scalar == 0 and exhausted
                                             and completed > 0 and not unresolved and not survivors),
                  scope='Numerical solver status plus exact primal checks; not rational infeasibility certificates or graph realizability')
    print('FINAL '+json.dumps(result), flush=True)
    return 2 if unresolved else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('n',type=int);parser.add_argument('Delta',type=int)
    parser.add_argument('--resume-scalar',type=int,default=0)
    parser.add_argument('--stop-scalar',type=int)
    parser.add_argument('--case-time-limit',type=float,default=10)
    parser.add_argument('--records-jsonl')
    a=parser.parse_args()
    raise SystemExit(main(a.n,a.Delta,a.resume_scalar,a.stop_scalar,a.case_time_limit,a.records_jsonl))
