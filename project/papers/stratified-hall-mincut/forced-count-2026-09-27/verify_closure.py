#!/usr/bin/env python3
"""Exact, solver-free certificate verifier for a greatest tight Hall minimum.

Usage: python verify_closure.py CERTIFICATE.json
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
    require(type(c) is dict and type(c.get("version")) is int and c.get("version") == 4, "unsupported schema")
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
    adj = [set() for _ in rev]
    for v, predecessors in enumerate(rev):
        for u in predecessors:
            adj[u].add(v)
    return start, gamma, value, adj



def reachable(adj, start):
    seen, stack = {start}, [start]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def source_components(adj, n):
    reach = [reachable(adj, i) for i in range(n)]
    return {frozenset(j for j in range(n) if j in reach[i] and i in reach[j])
            for i in range(n)}


def checked_path(values, adj, a, b):
    require(type(values) is list and 1 <= len(values) <= len(adj), "invalid residual path")
    path = [index(i, len(adj)) for i in values]
    require(path[0] == a and path[-1] == b, "wrong residual path endpoints")
    require(len(set(path)) == len(path), "residual path is not simple")
    require(all(v in adj[u] for u,v in zip(path,path[1:])), "nonpositive/nonexistent residual edge")
    return path



def closure_network(instance, adj, S, a, x, y):
    n=instance[0];N=len(adj);sigma,tau=N,N+1;B=n+1
    cap=[[0]*(N+2) for _ in range(N+2)]
    for u in range(N):
        for w in adj[u]:cap[u][w]+=B
    cap[sigma][2*n]+=B;cap[sigma][a]+=B
    for u in {2*n+1}|(set(range(n))-S):cap[u][tau]+=B
    negative=0
    for u in range(n):
        c=int((u,x) in instance[4])-int((u,y) in instance[4])
        if c>0:cap[u][tau]+=c
        elif c<0:cap[sigma][u]-=c;negative-=c
    return cap,sigma,tau,negative


def feasible_aux_flow(records,cap,s,t):
    require(type(records) is list,"auxiliary flow list required")
    N=len(cap);balance=[0]*N;seen=set()
    for e in records:
        require(type(e) is list and len(e)==3,"invalid auxiliary flow record")
        u,w=index(e[0],N),index(e[1],N);f=e[2]
        require(type(f) is int and 0<f<=cap[u][w],"invalid auxiliary flow capacity/value")
        require((u,w) not in seen,"duplicate auxiliary flow arc")
        seen.add((u,w));balance[u]+=f;balance[w]-=f
    value=balance[s]
    require(value>=0 and balance[t]==-value and all(balance[u]==0 for u in range(N) if u not in (s,t)),
            "auxiliary flow conservation fails")
    return value


def closure_step(instance,S,gamma,adj,step):
    n,blocks,p,d,arcs=instance
    require(type(step) is dict,"step object required")
    a,x,y=(index(step.get(k),n) for k in ("anchor","x","y"))
    require(a in S,"anchor absent")
    core=reachable(adj,2*n)
    require(a not in core,"anchor is mandatory")
    require(any(x in b and y in b for b in blocks) and p[x]<p[y],"invalid receiver pair")
    forced=(core|reachable(adj,a))&set(range(n))
    q=sum((u,x) in arcs for u in forced)
    require(q>p[x],"least anchored minimum does not exceed low capacity")
    yy,_,_,f=quantities(*instance,S)
    require(f==gamma,"state is not an exact minimum")
    require(yy[y]<p[y],"high receiver has no strict slack")
    cap,s,t,negative=closure_network(instance,adj,S,a,x,y)
    val=feasible_aux_flow(step.get("difference_flow"),cap,s,t)
    require(val-negative>=1,"signed difference lower bound is not positive")
    removed={u for u in S if a in reachable(adj,u)}
    after=S-removed
    require(quantities(*instance,after)[3]==gamma,"predecessor removal is not neutral")
    return after,dict(anchor=a,x=x,y=y,forced_sources=sorted(forced),low_lower_bound=q,
                     high_upper_bound=yy[y],difference_lower_bound=val-negative,
                     auxiliary_flow_value=val,negative_weight=negative,
                     before=sorted(S),remove=sorted(removed),after=sorted(after))


def verify(c):
    instance=parse_instance(c);n=instance[0]
    S,gamma,value,adj=flow_start(c,instance);initial=sorted(S)
    require(type(c.get("deletions")) is list and len(c['deletions'])<=n,"invalid deletion sequence")
    trace=[]
    for step in c['deletions']:
        S,r=closure_step(instance,S,gamma,adj,step);trace.append(r)
    require(S==vertex_set(c.get('terminal'),n),"wrong claimed terminal")
    _,h,u,f=quantities(*instance,S)
    require(f==gamma and h==u,"terminal is not a tight exact minimum")
    return dict(status='ACCEPT',version=4,greatest_exact_minimum=initial,
                greatest_tight_minimum=sorted(S),margin=str(gamma),maximum_flow=str(value),
                steps=len(trace),trace=trace,
                scope='internal signed residual-closure instance certificate; no completeness/general proof claim')


def main():
    try:
        require(len(sys.argv)==2,'usage: verify_closure.py CERTIFICATE.json')
        print(json.dumps(verify(json.loads(Path(sys.argv[1]).read_text())),indent=2,sort_keys=True));return 0
    except (Invalid,OSError,json.JSONDecodeError) as e:
        print(json.dumps(dict(status='REJECT',reason=str(e)),sort_keys=True));return 1


if __name__=='__main__':sys.exit(main())
