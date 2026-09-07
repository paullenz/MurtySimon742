#!/usr/bin/env python3
"""Generalized second arithmetic implementation, derived from the frozen second verifier.
Imports no code from the primary verifier. Both share the proposed generalized lemmas.

Domains use multiplicity vectors and residual excess; assignment bounds use
augmenting-path bipartite matching, not sorted greedy matching. Column vectors
use weak compositions of excess. Comparison with the first run occurs only
after this entire computation has finished. Both implementations share the
stated mathematical lemmas, so agreement does not constitute external review.
"""
from __future__ import annotations

A, B, GAP, LEDGER = 10, 14, 3, 42
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys


def reject(condition: bool, message: str) -> None:
    if condition:
        raise RuntimeError(message)


@lru_cache(None)
def histograms(value: int, slots: int, weight: int) -> tuple:
    """Counts of values 0,...,value; exact number of slots and exact weight."""
    if value == 0:
        return ((slots,),) if weight == 0 else ()
    result = []
    for count in range(min(slots, weight // value) + 1):
        for rest in histograms(value - 1, slots - count, weight - count * value):
            result.append(rest + (count,))
    return tuple(result)


def expand(counts: tuple, shift: int = 0) -> tuple:
    return tuple(v + shift for v, n in enumerate(counts) for _ in range(n))


@lru_cache(None)
def matching_number(labels: tuple, supplies: tuple) -> int:
    """Maximum cardinality matching, with distinct copies of repeated degrees."""
    owner = [-1] * len(supplies)
    def extend(label: int, visited: set) -> bool:
        for supplier, capacity in enumerate(supplies):
            if supplier in visited or labels[label] > capacity:
                continue
            visited.add(supplier)
            if owner[supplier] < 0 or extend(owner[supplier], visited):
                owner[supplier] = label
                return True
        return False
    count = 0
    for label in range(len(labels)):
        if extend(label, set()):
            count += 1
    return count


def neighbours_bound(ds: tuple, rs: tuple, columns: tuple | None) -> list:
    by_type = {}
    for rb in set(rs):
        others = list(rs)
        others.remove(rb)
        supplies = tuple(rb + other for other in others)
        admissible = [0]
        for size in range(1, A + 1 - rb):
            labels = tuple(ds[a] for a in range(A)
                           if ds[a] < rb + size and
                           (columns is None or ds[a] - columns[a] <= rb))
            if matching_number(labels, supplies) >= size:
                admissible.append(size)
        by_type[rb] = max(admissible)
    return [by_type[rb] for rb in rs]


def high_threshold_reject(ds: tuple, rs: tuple, bounds: list | None) -> bool:
    for cut in range(1, max(ds) + 1):
        highs = tuple(d for d in ds if d >= cut)
        required = sum(highs) - sum(min(len(highs), rb) for rb in rs)
        if bounds is None:
            available = 0
            for b in range(B):
                for w in range(b):
                    available += rs[b] + rs[w] >= cut
        else:
            available = 0
            for b in range(B):
                supplies = tuple(rs[b] + rs[w] for w in range(B) if w != b)
                candidates = tuple(d for d in highs if d < rs[b] + bounds[b])
                available += min(bounds[b], matching_number(candidates, supplies))
        if available < required:
            return True
    return False


def weak_compositions(amount: int, slots: int):
    if slots == 1:
        yield (amount,)
    else:
        for last in range(amount + 1):
            for first in weak_compositions(amount - last, slots - 1):
                yield first + (last,)


def analyse(ds: tuple, rs: tuple, r: int) -> tuple[str, list]:
    if high_threshold_reject(ds, rs, None):
        return 'pair_threshold', []
    bounds = neighbours_bound(ds, rs, None)
    if sum(bounds) < r + 2 * GAP:
        return 'source_total', []
    if high_threshold_reject(ds, rs, bounds):
        return 'source_threshold', []
    descending = tuple(reversed(rs))
    square = sum(descending[j - 1] >= j for j in range(1, B + 1))
    minimum = tuple(max(0, degree - square) for degree in ds)
    slack = r - sum(minimum)
    if slack < 0:
        return 'column_lower_bound', []
    all_columns = []
    passed = False
    for excess in weak_compositions(slack, A):
        columns = tuple(base + more for base, more in zip(minimum, excess))
        if max(columns) > B:
            continue
        required = sum(max(0, ds[a] - columns[a]) for a in range(A))
        first_bounds = neighbours_bound(ds, rs, columns)
        second_bounds = first_bounds.copy()
        if sum(first_bounds) >= required:
            for b in range(B):
                sizes = []
                for q in range(first_bounds[b] + 1):
                    supplier_count = len([w for w in range(B) if w != b
                                          and rs[w] + first_bounds[w] >= q - 1])
                    if supplier_count >= q:
                        sizes.append(q)
                second_bounds[b] = max(sizes)
        all_columns.append([list(columns), required, first_bounds, second_bounds])
        if sum(second_bounds) >= required:
            passed = True
    reject(not all_columns, 'Column domain unexpectedly empty')
    return ('survives' if passed else 'all_columns'), all_columns


def fingerprint(lines: list[str]) -> str:
    return hashlib.sha256(('\n'.join(sorted(lines)) + '\n').encode('ascii')).hexdigest()


def run(output: Path, reference: Path | None, degree_a: int, original_edges: int, ks: list[int], order: int = 27) -> dict:
    global A, B, GAP, LEDGER
    A = degree_a; B = order - 1 - A
    LEDGER = order*(order-1)//2 - original_edges - A - B*(B-1)//2
    GAP = A*(A-1)//2 - LEDGER
    output.mkdir(parents=True, exist_ok=True)
    keys, rows, columns = [], [], []
    for k in ks:
        D = A - 1 - k
        for r in range(B, LEDGER - (A*k+1)//2 + 1):
            counts = Counter()
            for hd in histograms(D, A, 2 * r + 2 * GAP):
                if hd[-1] == 0:
                    continue
                ds = expand(hd)
                # rho = 1 + excess, excess in 0..9, and total excess r-14.
                for hr in histograms(A - 1, B, r - B):
                    rs = expand(hr, shift=1)
                    key = json.dumps([k, r, ds, rs], separators=(',', ':'))
                    kind, evidence = analyse(ds, rs, r)
                    keys.append(key)
                    counts[kind] += 1
                    if evidence:
                        for c in evidence:
                            columns.append(json.dumps([key] + c, separators=(',', ':')))
            record = dict(k=k, D=D, r=r, states=sum(counts.values()),
                          dispositions=dict(sorted(counts.items())))
            rows.append(record)
            print(json.dumps(record, sort_keys=True), flush=True)
    reject(len(keys) != len(set(keys)), 'Duplicate state generated')
    summary = dict(schema=1, implementation='independent', imports_primary=False,
                   independent_mathematical_audit=False,
                   state_count=len(keys), state_key_sha256=fingerprint(keys), rows=rows,
                   survivors=sum(row['dispositions'].get('survives', 0) for row in rows),
                   column_vectors=len(columns), column_comparison_sha256=fingerprint(columns))
    summary['scope'] = dict(n=order, edges_G=original_edges, degree_A=A, delta_G=B, gap=GAP, ledger=LEDGER, ks=ks)
    if reference is not None:
        first = json.loads((reference / 'primary_summary.json').read_text())
        for name in ('state_count', 'state_key_sha256', 'rows', 'survivors', 'column_vectors'):
            reject(first[name] != summary[name], f'Independent comparison mismatch: {name}')
        old_columns = []
        for state in json.loads((reference / 'primary_column_cases.json').read_text()):
            for c in state['witness']['columns']:
                old_columns.append(json.dumps([state['key'], c['columns'], c['required'],
                                               c['caps'], c['refined_caps']], separators=(',', ':')))
        reject(fingerprint(old_columns) != fingerprint(columns), 'Column/capacity comparison mismatch')
        summary['comparison'] = 'ALL_STATE_KEYS_COUNTS_DISPOSITIONS_AND_COLUMN_CAPS_MATCH'
    else:
        summary['comparison'] = 'NOT_REQUESTED'
    (output / 'independent_summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
    return summary


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, default=Path('results'))
    p.add_argument('--reference', type=Path, default=None)
    p.add_argument('--n',type=int,default=27)
    p.add_argument('--a', type=int, required=True)
    p.add_argument('--edges', type=int, required=True)
    p.add_argument('--ks', type=int, nargs='+', required=True)
    a = p.parse_args()
    try:
        print(json.dumps(run(a.output, a.reference, a.a, a.edges, a.ks, a.n), sort_keys=True))
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        raise SystemExit(1)
