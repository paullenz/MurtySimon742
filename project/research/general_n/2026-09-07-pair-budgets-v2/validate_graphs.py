#!/usr/bin/env python3
"""Actual-graph falsification checks. No universal-proof claim."""
from itertools import combinations,product
import random,json,math,platform
from pathlib import Path


def diam2(adj):
    return all(((adj[u]>>v)&1) or (adj[u]&adj[v]) for u in range(len(adj)) for v in range(u+1,len(adj)))


def critical(adj):
    n=len(adj)
    if n<3 or sum(x.bit_count() for x in adj)==n*(n-1) or not diam2(adj):return False
    for u,v in combinations(range(n),2):
        if not ((adj[u]>>v)&1):continue
        adj[u]^=1<<v;adj[v]^=1<<u
        redundant=diam2(adj)
        adj[u]^=1<<v;adj[v]^=1<<u
        if redundant:return False
    return True


def bipartite(adj):
    col={}
    for root in range(len(adj)):
        if root in col:continue
        col[root]=0;todo=[root]
        for u in todo:
            for v in range(len(adj)):
                if not ((adj[u]>>v)&1):continue
                if v in col:
                    if col[v]==col[u]:return False
                else:col[v]=1-col[u];todo.append(v)
    return True


def adjacency(n,edges):
    a=[0]*n
    for u,v in edges:a[u]|=1<<v;a[v]|=1<<u
    return a


def check(adj,cnt,rng,all_choices):
    n=len(adj);full=(1<<n)-1
    H=[full^(1<<u)^adj[u] for u in range(n)]
    a=min(x.bit_count() for x in H)
    assert a>0
    for v in range(n):
        if H[v].bit_count()!=a:continue
        A=[i for i in range(n) if (H[v]>>i)&1]
        B=[u for u in range(n) if u!=v and not ((H[v]>>u)&1)]
        b=len(B);ell=b-a-1;choices=[]
        for u,w in combinations(B,2):
            if (H[u]>>w)&1:continue
            opts=[]
            for uu,ww in [(u,w),(w,u)]:
                for i in A:
                    if ((H[uu]>>i)&1) and H[uu]|H[i]==full^(1<<ww):opts.append((i,uu,ww))
            assert opts;choices.append(opts)
        count=math.prod(map(len,choices));cnt['root_instances']+=1
        cnt['largest_selection_product']=max(cnt['largest_selection_product'],count)
        if all_choices:
            selections=product(*choices)
        else:
            selections=[tuple(rng.choice(opts) for opts in choices) for _ in range(min(count,5))]
        for selected in selections:
            cnt['selected_systems']+=1
            sel={(u,i) for i,u,w in selected};assert len(sel)==len(selected)
            residual={(u,i) for u in B for i in A if (H[u]>>i)&1 and (u,i) not in sel}
            rho={u:sum((u,i) in residual for i in A) for u in B}
            R={i:sum((u,i) in residual for u in B) for i in A}
            q={u:sum(uu==u for i,uu,w in selected) for u in B}
            p={u:sum(w==u for i,uu,w in selected) for u in B}
            x={i:sum(j==i for j,u,w in selected) for i in A}
            d={i:sum(i!=j and not ((H[i]>>j)&1) for j in A) for i in A}
            Q=len(selected);r=len(residual);t=sum(row.bit_count() for row in adj)//2-b*(n-b)
            assert sum(d.values())==2*(r+t)
            s={i:max(0,d[i]-R[i]) for i in A}
            assert all(x[i]>=s[i] for i in A)
            Qmin=sum(s.values());E=Q-Qmin
            assert E>=0
            D0=max(max(d[i],R[i]) for i in A)
            for u in B:
                assert H[u].bit_count()==b-1+rho[u]-p[u]
                assert p[u]<=rho[u]+ell
                sigma=q[u]+p[u]
                assert sigma==sum(not ((H[u]>>w)&1) for w in B if w!=u)
                assert max(0,sigma-(rho[u]+ell))*max(0,sigma-D0)<=E
                cnt['vertex_checks']+=1
            for i,u,w in selected:
                assert R[i]+x[i]>=q[u]+p[u]
                cnt['selected_edge_checks']+=1
            W={w for i,u,w in selected}
            assert Q<=sum(rho[w]+ell for w in W)
            assert sum(rho[u] for u in B if u not in W)+2*t<=ell*len(W)
            if t>0:cnt['positive_surplus_systems']+=1


def main():
    import networkx as nx
    root=Path(__file__).resolve().parent;rng=random.Random(20260907)
    cnt=dict(atlas_graphs=0,atlas_critical=0,atlas_nonbipartite_critical=0,
        random_attempts=0,random_nonbipartite_critical=0,root_instances=0,selected_systems=0,
        largest_selection_product=0,vertex_checks=0,selected_edge_checks=0,positive_surplus_systems=0)
    saved=[]
    for g in nx.graph_atlas_g():
        cnt['atlas_graphs']+=1
        adj=adjacency(len(g),list(g.edges()))
        if not critical(adj):continue
        cnt['atlas_critical']+=1
        if bipartite(adj):continue
        cnt['atlas_nonbipartite_critical']+=1
        saved.append(dict(origin='atlas',n=len(g),edges=[list(e) for e in g.edges()]))
        check(adj,cnt,rng,True)
    for n in [8,10,14,20,28,32,44]:
        for rep in range(12):
            cnt['random_attempts']+=1
            edges=[(u,v) for u,v in combinations(range(n),2) if rng.random()<0.5]
            adj=adjacency(n,edges)
            if not diam2(adj):continue
            rng.shuffle(edges)
            for u,v in edges:
                adj[u]^=1<<v;adj[v]^=1<<u
                if not diam2(adj):adj[u]^=1<<v;adj[v]^=1<<u
            assert critical(adj)
            if bipartite(adj):continue
            cnt['random_nonbipartite_critical']+=1
            saved.append(dict(origin='seeded_greedy_minimisation',n=n,
                edges=[[u,v] for u,v in combinations(range(n),2) if (adj[u]>>v)&1]))
            check(adj,cnt,rng,False)
    out=dict(status='PASS',counts=cnt,seed=20260907,networkx_version=nx.__version__,
      python=platform.python_version(),scope='All Graph Atlas entries; every quasi-edge choice on its nonbipartite critical graphs. Seeded larger examples use at most five selections per minimum-degree complement root.',
      limits='No positive-surplus actual graph occurred. These are falsification tests, not universal proofs or independent expert review. Catalogue coverage is an imported dependency.')
    (root/'GRAPH_TESTS.json').write_text(json.dumps(out,indent=2)+'\n')
    (root/'TESTED_GRAPHS.json').write_text(json.dumps(saved,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
