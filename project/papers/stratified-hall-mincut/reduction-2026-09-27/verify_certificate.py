#!/usr/bin/env python3
"""Verify a Hall/rearrangement saddle certificate without a solver or Theorem A.

The input must contain the complete labelled instance, a feasible integral flow,
and a source cut attaining its value with H=U. Standard library only; no network.
Verification is instance-specific, not verification of a universal theorem.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integers(value: Any, name: str, n: int | None = None) -> list[int]:
    require(isinstance(value, list), f'{name}: expected a list')
    require(all(type(x) is int and x >= 0 for x in value),
            f'{name}: expected nonnegative integers, not booleans')
    require(n is None or len(value) == n, f'{name}: length mismatch')
    return value


def edge_set(value: Any, n: int, name: str) -> set[tuple[int, int]]:
    require(isinstance(value, list), f'{name}: expected a list')
    edges: set[tuple[int, int]] = set()
    for entry in value:
        pair = integers(entry, name, 2)
        u, w = pair
        require(u < n and w < n, f'{name}: index out of range')
        require(u != w, f'{name}: loop not permitted')
        require((u, w) not in edges, f'{name}: duplicate edge')
        edges.add((u, w))
    return edges


def verify(cert: dict[str, Any]) -> dict[str, int | str]:
    require(isinstance(cert, dict), 'expected an object')
    require(set(cert) == {'schema', 'P', 'd', 'layers', 'arcs', 'flow',
                          'source_set', 'claimed_flow_value'}, 'wrong certificate fields')
    require(cert['schema'] == 'hall-saddle-v1', 'unsupported schema')
    P = integers(cert['P'], 'P'); n = len(P)
    d = integers(cert['d'], 'd', n)
    layers = integers(cert['layers'], 'layers', n)
    arcs = edge_set(cert['arcs'], n, 'arcs')
    flow = edge_set(cert['flow'], n, 'flow')
    require(flow <= arcs, 'flow uses a forbidden arc')
    row = [0] * n; col = [0] * n
    for u, w in flow:
        row[u] += 1; col[w] += 1
    require(all(a <= b for a, b in zip(row, d)), 'source demand exceeded')
    require(all(a <= b for a, b in zip(col, P)), 'receiver capacity exceeded')
    selected = integers(cert['source_set'], 'source_set')
    require(len(set(selected)) == len(selected), 'duplicate source label')
    require(all(u < n for u in selected), 'source label out of range')
    S = set(selected); y = [0] * n
    for u, w in arcs:
        if u in S:
            y[w] += 1
    H = sum(min(P[w], y[w]) for w in range(n))
    # Threshold counting deliberately differs from the producer's sorting formula.
    U = 0
    for layer in sorted(set(layers)):
        ids = [w for w in range(n) if layers[w] == layer]
        for k in range(1, n + 1):
            U += min(sum(P[w] >= k for w in ids), sum(y[w] >= k for w in ids))
    value = len(flow)
    require(type(cert['claimed_flow_value']) is int, 'noninteger claimed flow')
    require(cert['claimed_flow_value'] == value, 'wrong claimed flow value')
    cut = sum(d[u] for u in range(n) if u not in S) + H
    require(value == cut, 'flow and cut do not match')
    require(H == U, 'cut has a rearrangement gap')
    return {'status': 'PASS', 'flow_value': value, 'minimum_margin': value - sum(d),
            'H': H, 'U': U, 'cut_size': len(S),
            'scope': 'this labelled instance and its within-layer capacity permutations'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    try:
        result = verify(json.loads(args.certificate.read_text(encoding='utf-8')))
    except (OSError, json.JSONDecodeError, ValueError, TypeError, KeyError) as error:
        parser.exit(1, f'FAIL: {error}\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
