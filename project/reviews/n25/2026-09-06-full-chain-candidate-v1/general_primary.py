#!/usr/bin/env python3
"""Generalized exact necessary-condition scan derived from the frozen Delta=14 primary verifier.
New work: A/B sizes, edge ledger and surplus parameter vary; all-active is an external lemma premise.

This is an arithmetic verifier, NOT a machine check of the graph-theoretic
lemmas in PROOF.md. No SAT solver, floating point, or graph catalogue is used.
It over-enumerates non-graphical degree multisets and residual column vectors.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import gzip
import hashlib
import json
import sys

A, B, GAP, LEDGER = 10, 14, 3, 42


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


@lru_cache(None)
def multisets(length: int, total: int, least: int, largest: int) -> tuple:
    if length == 0:
        return ((),) if total == 0 else ()
    result = []
    for first in range(least, largest + 1):
        if first * length > total:
            break
        if first + largest * (length - 1) < total:
            continue
        for suffix in multisets(length - 1, total - first, first, largest):
            result.append((first,) + suffix)
    return tuple(result)


def state_key(k: int, r: int, degrees: tuple, residual: tuple) -> str:
    return json.dumps([k, r, degrees, residual], separators=(',', ':'))


def matches(easiest_labels: list, strongest_suppliers: list) -> bool:
    return all(d <= c for d, c in zip(reversed(easiest_labels), strongest_suppliers))


def source_caps(degrees: tuple, residual: tuple, columns: tuple | None = None) -> list:
    result = []
    for b, rb in enumerate(residual):
        suppliers = sorted((rb + rw for w, rw in enumerate(residual) if w != b), reverse=True)
        best = 0
        for q in range(1, A - rb + 1):
            eligible = [d for a, d in enumerate(degrees)
                        if d <= rb + q - 1 and (columns is None or d <= columns[a] + rb)]
            if len(eligible) >= q and matches(eligible[:q], suppliers[:q]):
                best = q
        result.append(best)
    return result


def pair_failure(degrees: tuple, residual: tuple) -> dict | None:
    for threshold in range(1, max(degrees) + 1):
        labels = [d for d in degrees if d >= threshold]
        lower = sum(labels) - sum(min(rb, len(labels)) for rb in residual)
        upper = sum(rb + rw >= threshold for rb, rw in combinations(residual, 2))
        if lower > upper:
            return dict(threshold=threshold, lower=lower, upper=upper)
    return None


def source_threshold_failure(degrees: tuple, residual: tuple, caps: list) -> dict | None:
    for threshold in range(1, max(degrees) + 1):
        labels = [d for d in degrees if d >= threshold]
        lower = sum(labels) - sum(min(rb, len(labels)) for rb in residual)
        upper_by_source = []
        for b, rb in enumerate(residual):
            eligible = [d for d in labels if d <= rb + caps[b] - 1]
            suppliers = sorted((rb + rw for w, rw in enumerate(residual) if w != b), reverse=True)
            best = 0
            for number in range(1, min(caps[b], len(eligible)) + 1):
                if matches(eligible[:number], suppliers[:number]):
                    best = number
            upper_by_source.append(best)
        if sum(upper_by_source) < lower:
            return dict(threshold=threshold, lower=lower,
                        upper=sum(upper_by_source), source_caps=upper_by_source)
    return None


def column_vectors(lower: tuple, total: int):
    """Every labelled A-side residual vector; equal-degree labels NOT identified."""
    suffix_sums = [sum(lower[i:]) for i in range(A + 1)]
    def visit(i: int, left: int, prefix: tuple):
        if i == A:
            if left == 0:
                yield prefix
            return
        for value in range(lower[i], min(B, left - suffix_sums[i + 1]) + 1):
            yield from visit(i + 1, left - value, prefix + (value,))
    yield from visit(0, total, ())


def neighbourhood_caps(residual: tuple, caps: list) -> list:
    """One sound refinement: q supplements each need q-1 other A-neighbours."""
    answer = []
    for b, old in enumerate(caps):
        possible = [q for q in range(old + 1)
                    if sum(w != b and residual[w] + caps[w] >= q - 1
                           for w in range(B)) >= q]
        answer.append(max(possible))
    return answer


def classify(degrees: tuple, residual: tuple, r: int) -> tuple[str, dict]:
    failure = pair_failure(degrees, residual)
    if failure is not None:
        return 'pair_threshold', failure
    caps = source_caps(degrees, residual)
    if sum(caps) < r + 2 * GAP:
        return 'source_total', dict(lower=r + 2 * GAP, upper=sum(caps), caps=caps)
    failure = source_threshold_failure(degrees, residual, caps)
    if failure is not None:
        return 'source_threshold', failure
    h = max(j for j in range(A + 1) if sum(rb >= j for rb in residual) >= j)
    lower_columns = tuple(max(0, d - h) for d in degrees)
    if sum(lower_columns) > r:
        return 'column_lower_bound', dict(h=h, lower=sum(lower_columns), budget=r,
                                          lower_columns=lower_columns)
    column_records = []
    survivors = []
    for columns in column_vectors(lower_columns, r):
        qmin = sum(max(0, d - ra) for d, ra in zip(degrees, columns))
        local_caps = source_caps(degrees, residual, columns)
        improved = local_caps if sum(local_caps) < qmin else neighbourhood_caps(residual, local_caps)
        rec = dict(columns=columns, required=qmin, caps=local_caps,
                   refined_caps=improved, upper=sum(improved))
        column_records.append(rec)
        if sum(improved) >= qmin:
            survivors.append(rec)
    need(bool(column_records), 'Unexpected empty column domain')
    return ('survives' if survivors else 'all_columns'), dict(h=h,
        lower_columns=lower_columns, column_count=len(column_records), columns=column_records,
        survivors=survivors)


def stable_bytes(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(',', ':')) + '\n').encode('ascii')


def run(output: Path, degree_a: int, original_edges: int, ks: list[int]) -> dict:
    global A, B, GAP, LEDGER
    A=degree_a; B=24-A
    LEDGER=300-original_edges-A-B*(B-1)//2
    GAP=A*(A-1)//2-LEDGER
    output.mkdir(parents=True, exist_ok=True)
    summaries, ledger, keys, column_cases = [], [], [], []
    for k in ks:
        D = A - 1 - k
        for r in range(B, LEDGER - (A*k+1)//2 + 1):
            counts = Counter()
            for d in multisets(A, 2 * (r + GAP), 0, D):
                if d[-1] != D:
                    continue
                for rho in multisets(B, r, 1, A):
                    key = state_key(k, r, d, rho)
                    kind, witness = classify(d, rho, r)
                    counts[kind] += 1
                    keys.append(key)
                    row = dict(key=key, kind=kind, witness=witness)
                    ledger.append(stable_bytes(row))
                    if kind in ('all_columns', 'survives'):
                        column_cases.append(row)
            row = dict(k=k, D=D, r=r, states=sum(counts.values()),
                       dispositions=dict(sorted(counts.items())))
            summaries.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    need(len(keys) == len(set(keys)), 'Duplicate state')
    summary = dict(schema=1, implementation='primary',
        scope=dict(n=25,edges_G=original_edges,delta_G=B,degree_A=A,gap=GAP,ledger=LEDGER,ks=ks),
        uses_graph_catalogue=False, uses_sat_solver=False, independent_mathematical_audit=False,
        state_count=len(keys), state_key_sha256=hashlib.sha256(
            ('\n'.join(sorted(keys)) + '\n').encode('ascii')).hexdigest(),
        survivors=sum(x['dispositions'].get('survives', 0) for x in summaries), rows=summaries,
        column_degree_states=len(column_cases),
        column_vectors=sum(x['witness']['column_count'] for x in column_cases))
    raw = b''.join(ledger)
    with (output / 'primary_ledger.jsonl.gz').open('wb') as stream:
        with gzip.GzipFile(filename='', mode='wb', fileobj=stream, mtime=0) as z:
            z.write(raw)
    summary['uncompressed_ledger_sha256'] = hashlib.sha256(raw).hexdigest()
    (output / 'primary_summary.json').write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
    (output / 'primary_column_cases.json').write_text(json.dumps(column_cases, indent=2, sort_keys=True) + '\n')
    # Numerical survivors are explicitly retained; no theorem is inferred from them.
    return summary


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, default=Path('results'))
    p.add_argument('--a',type=int,required=True)
    p.add_argument('--edges',type=int,required=True)
    p.add_argument('--ks',type=int,nargs='+',required=True)
    args = p.parse_args()
    try:
        print(json.dumps(run(args.output,args.a,args.edges,args.ks), sort_keys=True))
    except (OSError, ValueError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        raise SystemExit(1)
