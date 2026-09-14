#!/usr/bin/env python3
"""Exact original-sample verifier for the singleton-destination and cardinality arc-slot traps."""
from __future__ import annotations
import argparse,json
from collections import deque
from itertools import combinations
from pathlib import Path

SOURCE_SHA='157db7e1f48261626eac8cb99bf875f4aec3b707d4c024f62989dd1bcec38572'
ROWS=[160,338,347,471,586]


def arc_allowed(a,q,rho,u,w):
    if u==w:return False
    lo=max(0,q[u]+q[w]-a,q[u]-rho[w]-1,q[w]-rho[u])
    hi=min(q[u],q[w],q[u]-1)
    return lo<=hi


def singleton_trap(p):
    q,rho=p['q'],p['rho']
    T=[u for u,(qq,r) in enumerate(zip(q,rho)) if qq==1 and r==1]
    L=[w for w,qq in enumerate(q) if qq<=1]
    slots=sorted({tuple(sorted((u,w))) for u in T for w in L if u!=w})
    adj={u:[s for s in slots if u in s] for u in T}
    match={}
    def dfs(u,seen):
        for s in adj[u]:
            if s in seen:continue
            seen.add(s)
            if s not in match or dfs(match[s],seen):
                match[s]=u;return True
        return False
    for u in T:dfs(u,set())
    hall=None
    for r in range(1,len(T)+1):
        for sub in combinations(T,r):
            neigh=sorted({s for u in sub for s in adj[u]})
            deficit=len(sub)-len(neigh)
            if deficit<=0:continue
            cand=(deficit,len(sub),sub,neigh)
            if hall is None or (-cand[0],cand[1],cand[2])<(-hall[0],hall[1],hall[2]):hall=cand
    return dict(trap_sources=T,low_q_destinations=L,pair_slots=[list(s) for s in slots],
                matching_size=len(match),required=len(T),rejected=len(match)<len(T),
                hall_witness=None if hall is None else dict(sources=list(hall[2]),
                    neighbor_pair_slots=[list(s) for s in hall[3]],deficit=hall[0]))


def cardinality_flow(p):
    a,q,rho=p['a'],p['q'],p['rho'];n=len(q)
    slots=[];adj={u:[] for u in range(n)}
    for u in range(n):
        for w in range(u+1,n):
            dirs=[]
            if arc_allowed(a,q,rho,u,w):dirs.append(u)
            if arc_allowed(a,q,rho,w,u):dirs.append(w)
            if dirs:
                j=len(slots);slots.append((u,w,tuple(dirs)))
                for d in dirs:adj[d].append(j)
    S=0;so=1;po=1+n;T=po+len(slots);N=T+1
    g=[[] for _ in range(N)]
    def add(u,v,c):
        g[u].append([v,c,len(g[v])]);g[v].append([u,0,len(g[u])-1])
    total=sum(q)
    for u,qq in enumerate(q):add(S,so+u,qq)
    for j,(_,_,dirs) in enumerate(slots):
        add(po+j,T,1)
        for u in dirs:add(so+u,po+j,1)
    flow=0
    while True:
        level=[-1]*N;level[S]=0;dq=deque([S])
        while dq:
            v=dq.popleft()
            for to,c,_ in g[v]:
                if c and level[to]<0:level[to]=level[v]+1;dq.append(to)
        if level[T]<0:break
        it=[0]*N
        def dfs(v,f):
            if v==T:return f
            while it[v]<len(g[v]):
                e=g[v][it[v]];to,c,rev=e
                if c and level[to]==level[v]+1:
                    z=dfs(to,min(f,c))
                    if z:e[1]-=z;g[to][rev][1]+=z;return z
                it[v]+=1
            return 0
        while True:
            z=dfs(S,10**9)
            if not z:break
            flow+=z
    vis=[False]*N;vis[S]=True;dq=deque([S])
    while dq:
        v=dq.popleft()
        for to,c,_ in g[v]:
            if c and not vis[to]:vis[to]=True;dq.append(to)
    deficient=[u for u in range(n) if vis[so+u]]
    neighbors=sorted({j for u in deficient for j in adj[u]})
    return dict(required_out_arcs=total,max_compatible_pair_flow=flow,
                compatible_pair_slots=len(slots),rejected=flow<total,
                deficient_source_subset=deficient,
                deficient_demand=sum(q[u] for u in deficient),
                deficient_neighbor_slots=len(neighbors))


def verify(data):
    assert data['source_sha256']==SOURCE_SHA
    rows={p['row']:p for p in data['rows']}
    assert all(r in rows for r in ROWS)
    out=dict(schema='singleton-destination-and-cardinality-arc-slot-original-v1',
             scope='necessary selected-label/destination cardinality coupling plus simple orientation; original synthetic namespace only',
             profiles={},newly_excluded=[],remaining=[],
             original_sample=dict(rejected=711,total=713,not_rejected=[160,338]))
    for row in ROWS:
        p=rows[row]
        singleton=singleton_trap(p);card=cardinality_flow(p)
        out['profiles'][str(row)]=dict(a=p['a'],singleton_trap=singleton,cardinality_arc_slot=card)
        (out['newly_excluded'] if singleton['rejected'] else out['remaining']).append(row)
    assert out['newly_excluded']==[347,471,586]
    assert out['remaining']==[160,338]
    assert [out['profiles'][str(r)]['cardinality_arc_slot']['max_compatible_pair_flow'] for r in ROWS]==[81,101,127,95,108]
    assert [out['profiles'][str(r)]['cardinality_arc_slot']['required_out_arcs'] for r in ROWS]==[81,101,129,96,109]
    assert not out['profiles']['160']['cardinality_arc_slot']['rejected']
    assert not out['profiles']['338']['cardinality_arc_slot']['rejected']
    return out


def main():
    if not __debug__:raise SystemExit('Assertions disabled: do not run with -O')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--remainder',type=Path,required=True);args=ap.parse_args()
    print(json.dumps(verify(json.loads(args.remainder.read_text())),sort_keys=True,indent=2))

if __name__=='__main__':main()
