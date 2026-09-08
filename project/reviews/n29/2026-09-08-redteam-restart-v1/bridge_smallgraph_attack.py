#!/usr/bin/env python3
"""Exhaustive labelled small-graph regression for the standalone bridge.

Enumerates every simple graph through n=6, keeps diameter-two edge-critical
ones, and checks the graph-to-selected/residual pointwise identities for every
minimum-complement-degree choice of v.  This is falsification evidence only:
there are no positive-surplus (t>0) examples in this small domain, so the
residual-activity/charging t>0 branch is not exercised by actual graphs here.
"""
import json
from collections import Counter


def graph_from_mask(n,mask):
    adj=[0]*n;k=0
    for i in range(n):
        for j in range(i+1,n):
            if (mask>>k)&1:
                adj[i]|=1<<j;adj[j]|=1<<i
            k+=1
    return adj


def d2(adj,n):
    allmask=(1<<n)-1
    for u in range(n):
        reach=(1<<u)|adj[u]
        bits=adj[u]
        while bits:
            bit=bits&-bits;bits-=bit;w=bit.bit_length()-1
            reach|=adj[w]
        if reach!=allmask:return False
    return True


def critical(adj,n):
    if not d2(adj,n):return False
    for u in range(n):
        bits=adj[u]&~((1<<(u+1))-1)
        while bits:
            bit=bits&-bits;bits-=bit;w=bit.bit_length()-1
            h=adj.copy();h[u]&=~(1<<w);h[w]&=~(1<<u)
            if d2(h,n):return False
    return True


def complement(adj,n):
    allmask=(1<<n)-1
    return [(allmask^(1<<u)^adj[u])&allmask for u in range(n)]


def quasi_options(H,n,A,u,w):
    full=(1<<n)-1;out=[]
    for src,exc in ((u,w),(w,u)):
        for i in A:
            if ((H[src]>>i)&1) and (H[src]|H[i])==(full^(1<<exc)):
                out.append((src,i,exc))
    return out


def check_view(G,H,n,v):
    A=[i for i in range(n) if (H[v]>>i)&1]
    B=[i for i in range(n) if i!=v and not ((H[v]>>i)&1)]
    a=len(A);b=len(B);m=sum(x.bit_count() for x in G)//2;t=m-b*(n-b)
    selected=set();oriented=[]
    for ii,u in enumerate(B):
        for w in B[ii+1:]:
            if (H[u]>>w)&1:continue
            opts=quasi_options(H,n,A,u,w)
            assert opts,('missing B-pair has no quasi-edge',n,v,u,w)
            # Through n=6 this happens to be unique.  The proof needs only one.
            src,i,exc=opts[0]
            assert (src,i) not in selected
            selected.add((src,i));oriented.append((src,i,exc))
    residual={(u,i) for u in B for i in A if ((H[u]>>i)&1) and (u,i) not in selected}
    rho={u:sum((u,i) in residual for i in A) for u in B}
    q={u:sum((u,i) in selected for i in A) for u in B}
    p={u:sum(exc==u for src,i,exc in oriented) for u in B}
    R={i:sum((u,i) in residual for u in B) for i in A}
    x={i:sum((u,i) in selected for u in B) for i in A}
    d={i:sum(j!=i and not ((H[i]>>j)&1) for j in A) for i in A}
    r=sum(rho.values());eF=sum(d.values())//2
    assert eF==r+t
    s={i:max(0,d[i]-R[i]) for i in A}
    for i in A:assert x[i]>=s[i]
    for u,i,w in oriented:
        assert d[i]<=rho[u]+R[i]
        assert s[i]<=rho[u]
        assert d[i]<=rho[u]+rho[w]
        assert rho[w]+q[w]>=q[u]-1
        assert d[i]<=rho[u]+q[u]-1
        assert R[i]+x[i]>=q[u]+p[u]
    for u in B:
        assert q[u]+rho[u]<=a
        assert q[u]+p[u]<=b-1
        assert p[u]<=rho[u]+b-a-1
    # Threshold capacity does not require t>0; source demand and pair injection suffice.
    Hmax=max([0]+list(s.values()))
    for h in range(1,Hmax+1):
        W=sum(si for si in s.values() if si>=h)
        z=sum(rho[u]>=h for u in B)
        if W:
            assert z>=h
            assert 2*W<=z*z-z+h*(h+1)
    return t


def main():
    counts=Counter();views=0;tpos=0
    for n in range(3,7):
        M=n*(n-1)//2
        for mask in range(1<<M):
            G=graph_from_mask(n,mask)
            if not critical(G,n):continue
            counts[str(n)]+=1
            H=complement(G,n);mind=min(x.bit_count() for x in H)
            for v in range(n):
                if H[v].bit_count()!=mind:continue
                views+=1
                if check_view(G,H,n,v)>0:tpos+=1
    expected={'3':3,'4':7,'5':27,'6':571}
    assert dict(counts)==expected
    assert views==920
    assert tpos==0
    print(json.dumps({'status':'PASS','critical_graphs':dict(counts),'minimum_degree_views':views,'positive_surplus_views':tpos},sort_keys=True))


if __name__=='__main__':main()
