#!/usr/bin/env python3
"""Integer augmenting paths and fixed-neighbourhood B-side routing."""
from collections import deque

def max_flow(vertices,edges,source,sink):
    capacity=[[0]*vertices for _ in range(vertices)]
    for u,v,c in edges:
        assert type(c) is int and c>=0
        capacity[u][v]+=c
    remaining=[r[:] for r in capacity];value=0
    while True:
        parent=[-1]*vertices;parent[source]=source;queue=deque([source])
        while queue and parent[sink]<0:
            u=queue.popleft()
            for v,c in enumerate(remaining[u]):
                if c>0 and parent[v]<0:parent[v]=u;queue.append(v)
        if parent[sink]<0:break
        v=sink;amount=None
        while v!=source:
            u=parent[v];amount=remaining[u][v] if amount is None else min(amount,remaining[u][v]);v=u
        v=sink
        while v!=source:
            u=parent[v];remaining[u][v]-=amount;remaining[v][u]+=amount;v=u
        value+=amount
    reachable={source};queue=deque([source])
    while queue:
        u=queue.popleft()
        for v,c in enumerate(remaining[u]):
            if c>0 and v not in reachable:reachable.add(v);queue.append(v)
    assert sink not in reachable
    cut=sum(c for u,v,c in edges if u in reachable and v not in reachable)
    assert cut==value
    flows={(u,v):capacity[u][v]-remaining[u][v] for u,v,c in edges}
    return value,flows,reachable

def eligible(selected,residual,b):
    S=[{i for w,i in selected if w==u} for u in range(b)]
    N=[{i for w,i in set(selected)|set(residual) if w==u} for u in range(b)]
    return {(u,i):[v for v in range(b) if v!=u and S[u]-N[v]=={i} and S[v]<=N[u]] for u,i in sorted(selected)}

def solve(a,b,selected,residual,capacities):
    assert len(capacities)==b and min(capacities)>=0
    destinations=eligible(selected,residual,b);obligations=sorted(destinations);Q=len(obligations)
    src=Q+b;sink=src+1;edges=[]
    for k,key in enumerate(obligations):
        edges.append((src,k,1))
        for v in destinations[key]:edges.append((k,Q+v,Q+1))
    for v,c in enumerate(capacities):edges.append((Q+v,sink,c))
    value,flows,reached=max_flow(sink+1,edges,src,sink)
    report=dict(required=Q,flow=value,empty_eligibility_obligations=[list(o) for o in obligations if not destinations[o]],
        eligible_pair_count=sum(map(len,destinations.values())))
    if value==Q:
        report.update(status='ROUTING',arcs=[[u,i,v] for k,(u,i) in enumerate(obligations) for v in destinations[u,i] if flows[k,Q+v]==1])
    else:
        T=[o for k,o in enumerate(obligations) if k in reached]
        U=sorted({v for o in T for v in destinations[o]});total=sum(capacities[v] for v in U)
        assert len(T)>total
        report.update(status='FIXED_PATTERN_HALL_OBSTRUCTION',obligations=[list(o) for o in T],destinations=U,
            destination_capacity=total,deficit=len(T)-total)
    return report

def selected_pattern(rec):
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho'];source=a+b;sink=source+1;edges=[]
    for i,demand in enumerate(s):
        edges.append((source,i,demand))
        for u in range(b):
            if rho[u]>=demand:edges.append((i,a+u,1))
    for u in range(b):edges.append((a+u,sink,a-rho[u]))
    value,flows,reached=max_flow(sink+1,edges,source,sink)
    assert value==sum(s),'Selected-incidence construction failed; preserve and examine before continuation.'
    return {(u,i) for i in range(a) for u in range(b) if flows.get((i,a+u),0)==1}
