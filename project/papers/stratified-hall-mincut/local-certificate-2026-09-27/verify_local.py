#!/usr/bin/env python3
"""Exact, solver-free certificate verifier for a greatest tight Hall minimum.

Usage: python verify_local.py CERTIFICATE.json
Only Python's standard library is needed. Numeric fields accept integers or exact
fraction strings (e.g. "3/4"), not floats or booleans. No untrusted code is run.
A rejection or absence of a certificate is NOT a mathematical counterexample.
"""
from __future__ import annotations
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


class Invalid(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Invalid(message)


def rational(value: object) -> Q:
    require(type(value) in (int, str), "exact rational required; float/bool disallowed")
    try:
        q = Q(value)
    except (ValueError, ZeroDivisionError, TypeError) as exc:
        raise Invalid("invalid rational") from exc
    require(q >= 0, "negative quantity")
    return q


def index(value: object, n: int) -> int:
    require(type(value) is int and 0 <= value < n, "invalid vertex index")
    return value


def vertex_set(values: object, n: int) -> set[int]:
    require(type(values) is list, "vertex list required")
    ans = {index(v, n) for v in values}
    require(len(ans) == len(values), "duplicate vertex")
    return ans


def parse_instance(c: dict) -> tuple:
    require(type(c) is dict and type(c.get("version")) is int and c.get("version") == 1, "unsupported schema")
    n = c.get("n")
    require(type(n) is int and n >= 1, "positive integer order required")
    bs = c.get("blocks")
    require(type(bs) is list and bs, "nonempty block partition required")
    blocks = [vertex_set(b, n) for b in bs]
    require(all(blocks), "empty block")
    require(sum(map(len, blocks)) == n and set.union(*blocks) == set(range(n)),
            "blocks are not a partition")
    for name in ("capacities", "demands"):
        require(type(c.get(name)) is list and len(c[name]) == n, "wrong quota length")
    p = [rational(v) for v in c["capacities"]]
    d = [rational(v) for v in c["demands"]]
    require(type(c.get("arcs")) is list, "arc list required")
    arcs: set[tuple[int, int]] = set()
    for a in c["arcs"]:
        require(type(a) is list and len(a) == 2, "invalid arc")
        u, w = (index(a[0], n), index(a[1], n))
        require(u != w, "loops are not supported")
        require((u, w) not in arcs, "duplicate arc")
        arcs.add((u, w))
    return n, blocks, p, d, arcs


def quantities(n: int, blocks: list, p: list, d: list,
               arcs: set, s: set[int]) -> tuple:
    counts = [sum((u, w) in arcs for u in s) for w in range(n)]
    h = sum((min(p[w], counts[w]) for w in range(n)), Q(0))
    u = sum((sum((min(a, b) for a, b in
                       zip(sorted(p[w] for w in block),
                           sorted(counts[w] for w in block))), Q(0))
             for block in blocks), Q(0))
    demand = sum((d[v] for v in s), Q(0))
    return counts, h, u, h-demand


def flow_start(c: dict, instance: tuple) -> tuple:
    """Check supplied flow, then derive greatest min-cut projection residually."""
    n, blocks, p, d, arcs = instance
    require(type(c.get("flow")) is list, "flow list required")
    f = {}
    outgoing, incoming = [Q(0)]*n, [Q(0)]*n
    for e in c["flow"]:
        require(type(e) is list and len(e) == 3, "invalid flow record")
        u, w = index(e[0], n), index(e[1], n)
        require((u, w) in arcs and (u, w) not in f, "unsupported/duplicate flow arc")
        value = rational(e[2])
        require(value <= 1, "flow exceeds unit arc capacity")
        f[u, w] = value
        outgoing[u] += value
        incoming[w] += value
    require(all(outgoing[u] <= d[u] for u in range(n)), "source overload")
    require(all(incoming[w] <= p[w] for w in range(n)), "receiver overload")
    source, sink = 2*n, 2*n+1
    rev: list[set[int]] = [set() for _ in range(2*n+2)]

    def edge(a: int, b: int, cap: Q, value: Q) -> None:
        if cap > value:
            rev[b].add(a)
        if value > 0:
            rev[a].add(b)

    for u in range(n):
        edge(source, u, d[u], outgoing[u])
    for u, w in arcs:
        edge(u, n+w, Q(1), f.get((u, w), Q(0)))
    for w in range(n):
        edge(n+w, sink, p[w], incoming[w])
    can_reach_sink, stack = {sink}, [sink]
    while stack:
        v = stack.pop()
        for a in rev[v]:
            if a not in can_reach_sink:
                can_reach_sink.add(a)
                stack.append(a)
    require(source not in can_reach_sink, "augmenting path: supplied flow not maximum")
    start = set(range(n))-can_reach_sink
    value = sum(outgoing, Q(0))
    gamma = quantities(*instance, start)[3]
    require(value == sum(d, Q(0))+gamma, "flow/cut mismatch")
    return start, gamma, value


def local_step(instance: tuple, s: set[int], x: int, y: int, gamma: Q, delete: int | None = None) -> tuple:
    n, blocks, p, d, arcs = instance
    a = y if delete is None else delete
    require(x != y and a in s, "wrong deletion endpoints")
    require(any(x in b and y in b for b in blocks), "endpoints in different blocks")
    require(p[x] < p[y] and (a, x) in arcs and (a, y) not in arcs,
            "missing distinguished incoming row")
    require(all((z, y) not in arcs or (z, x) in arcs for z in s-{a}),
            "selected high-incoming rows are not contained in low-incoming rows")
    counts, _, _, margin = quantities(*instance, s)
    require(margin == gamma, "state is not the certified minimum")
    require(max(p[x], counts[y]) < min(p[y], counts[x]), "not a positive crossing")
    after = s-{a}
    require(quantities(*instance, after)[3] == gamma, "deletion is not neutral")
    return after, {"x": x, "y": y, "delete": a, "before": sorted(s), "after": sorted(after),
                   "low_count": counts[x], "high_count": counts[y]}


def verify(c: dict) -> dict:
    instance = parse_instance(c)
    n = instance[0]
    s, gamma, value = flow_start(c, instance)
    initial = sorted(s)
    require(type(c.get("deletions")) is list and len(c["deletions"]) <= n,
            "invalid deletion sequence")
    trace = []
    for step in c["deletions"]:
        require(type(step) is dict and "x" in step and "y" in step, "invalid step")
        x, y = index(step["x"], n), index(step["y"], n)
        a = index(step.get("delete", y), n)
        s, record = local_step(instance, s, x, y, gamma, a)
        trace.append(record)
    require(s == vertex_set(c.get("terminal"), n), "wrong claimed terminal")
    counts, h, u, margin = quantities(*instance, s)
    require(margin == gamma and h == u, "terminal is not a tight exact minimum")
    return {"status": "ACCEPT", "greatest_exact_minimum": initial,
            "greatest_tight_minimum": sorted(s), "margin": str(gamma),
            "maximum_flow": str(value), "neutral_deletions": len(trace),
            "trace": trace,
            "scope": "instance certificate; no general theorem/novelty/external-review claim"}


def main() -> int:
    try:
        require(len(sys.argv) == 2, "usage: verify_local.py CERTIFICATE.json")
        c = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(json.dumps(verify(c), indent=2, sort_keys=True))
        return 0
    except (Invalid, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "REJECT", "reason": str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
