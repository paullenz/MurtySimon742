2026-09-22T15:29:10+01:00
#!/usr/bin/env python3
"""Exact r=10 optimistic core/source quotient for support at most seven.

Scratch computation only.  It mirrors the audited r=8 necessary conditions:
positive-core ledger, demand-square capacity, colour-preserving quotient, and
physical-source state feasibility.  Survivors are not graph realizations.
"""
import itertools, json
from functools import lru_cache

def parts(n, hi=None):
    if n == 0:
        yield ()
        return
    hi = min(n, hi or n)
    for x in range(hi, 0, -1):
        for tail in parts(n-x, x):
            yield (x,) + tail

def data_for(R, pairs, mask):
    k=len(R); deg=[0]*k; neigh=[set() for _ in R]; edges=[]
    for q,(i,j) in enumerate(pairs):
        if mask>>q&1:
            edges.append((i,j));deg[i]+=1;deg[j]+=1
            neigh[i].add(j);neigh[j].add(i)
    P=[i for i in range(k) if deg[i]>R[i]]
    N=[i for i in range(k) if i not in P]
    if any((deg[i]-R[i])**2>sum(R[j] for j in neigh[i]) for i in P):
        return None
    eP=sum(i in P and j in P for i,j in edges)
    eN=sum(i in N and j in N for i,j in edges)
    # Optimistic core-only relaxation used by the audited r=8 census.
    # Core degree need not equal total F-degree because N may meet T, so the
    # full apparent R-coredeg slack is not safely subtractable here.
    slack=sum(1 for i in N if R[i]==1 and deg[i]==0)
    t=eP-eN-sum(R[i] for i in P)-slack
    if t<=0:return None
    return edges,deg,neigh,P,N,t

def perms_for(R):
    groups=[tuple(i for i,x in enumerate(R) if x==v)
            for v in sorted(set(R),reverse=True)]
    for choices in itertools.product(*(itertools.permutations(g) for g in groups)):
        p=list(range(len(R)))
        for g,image in zip(groups,choices):
            for i,j in zip(g,image):p[i]=j
        yield tuple(p)

def canonical(mask,pairs,index,perms):
    best=None
    for p in perms:
        image=0
        for q,(i,j) in enumerate(pairs):
            if mask>>q&1:
                a,b=sorted((p[i],p[j]));image|=1<<index[(a,b)]
        best=image if best is None or image<best else best
    return best

def source_feasible(R,datum):
    edges,deg,neigh,P,N,t=datum;k=len(R);need=tuple(max(0,deg[i]-R[i]) for i in range(k))
    patterns=[]
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1}
        Z={i for i,s in enumerate(state) if s==2}
        if any(not neigh[i] <= L|Z or len(neigh[i]&L)>R[i] for i in L):continue
        if not Z:
            if L&set(P):continue
            continue
        patterns.append((tuple(int(i in Z) for i in range(k)),
                         tuple(int(i in L) for i in range(k)),state))
    @lru_cache(None)
    def solve(rem,x):
        if not any(rem):return () if all(x[i]>=need[i] for i in range(k)) else None
        for q,(z,l,state) in enumerate(patterns):
            if all(z[i]<=rem[i] for i in range(k)):
                tail=solve(tuple(rem[i]-z[i] for i in range(k)),
                           tuple(min(need[i],x[i]+l[i]) for i in range(k)))
                if tail is not None:return (q,)+tail
        return None
    w=solve(R,(0,)*k)
    return None if w is None else [patterns[q][2] for q in w]

out={}
for R in parts(10):
    k=len(R)
    if k>7 or all(x==1 for x in R):continue
    pairs=list(itertools.combinations(range(k),2));idx={e:q for q,e in enumerate(pairs)}
    perms=list(perms_for(R)); reps={};labelled=0
    for mask in range(1<<len(pairs)):
        d=data_for(R,pairs,mask)
        if d is None:continue
        labelled+=1;cm=canonical(mask,pairs,idx,perms)
        if cm not in reps:reps[cm]=data_for(R,pairs,cm)
    feasible=[]
    for cm,d in reps.items():
        w=source_feasible(R,d)
        if w is not None:feasible.append({'mask':cm,'edges':d[0],'degrees':d[1],
            'P':d[3],'t_upper':d[5],'witness':w})
    out[str(R)]={'support':k,'labelled':labelled,'orbits':len(reps),
                 'source_feasible':len(feasible),'feasible':feasible}
    print(R,labelled,len(reps),len(feasible),flush=True)
print(json.dumps(out,indent=2))
