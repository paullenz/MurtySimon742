#!/usr/bin/env python3
"""Exact hostile replay of the four r=10 supplement kernels with free helpers."""
import itertools
import json

CASES = {
    "3515": ((2,2,2,2,1,1), [(0,1),(0,2),(0,4),(0,5),(1,2),(1,4),(1,5),(2,4),(2,5)]),
    "401020": ((2,2,2,1,1,1,1), [(0,3),(0,4),(0,5),(0,6),(1,2),(1,5),(1,6),(2,3),(2,4),(3,6),(4,5)]),
    "15402149": ((2,2,1,1,1,1,1,1), [(0,1),(0,3),(0,6),(1,2),(1,5),(2,6),(2,7),(3,5),(3,7),(4,5),(4,6)]),
    "48374421": ((2,2,1,1,1,1,1,1), [(0,1),(0,3),(0,5),(1,2),(1,4),(2,3),(2,7),(3,7),(4,5),(4,6),(5,6)]),
}

def run(R, edges):
    k=len(R); neigh=[set() for _ in R]; deg=[0]*k
    for i,j in edges: neigh[i].add(j); neigh[j].add(i); deg[i]+=1; deg[j]+=1
    P={i for i in range(k) if deg[i]>R[i]}; need=tuple(max(0,deg[i]-R[i]) for i in range(k))
    patterns=[]; free=[]
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1}; Z={i for i,s in enumerate(state) if s==2}
        if any(not neigh[i]<=L|Z or len(neigh[i]&L)>R[i] for i in L): continue
        if not Z:
            if not (L&P): free.append(state)
            continue
        patterns.append((tuple(int(i in Z) for i in range(k)),tuple(int(i in L) for i in range(k)),state))
    pops=[]
    def search(start,rem,x,chosen):
        if not any(rem):
            if all(x[i]>=need[i] for i in range(k)): pops.append(tuple(chosen))
            return
        for q in range(start,len(patterns)):
            z,l,state=patterns[q]
            if all(z[i]<=rem[i] for i in range(k)):
                search(q,tuple(rem[i]-z[i] for i in range(k)),tuple(x[i]+l[i] for i in range(k)),chosen+[state])
    search(0,R,(0,)*k,[])
    def forced(su,u,sw,w):
        Lu={i for i,s in enumerate(su) if s==1}; Lw={i for i,s in enumerate(sw) if s==1}
        return {(u,i) for i in Lu if sw[i]==0}|{(w,j) for j in Lw if su[j]==0}
    def ok(pop):
        for u,su in enumerate(pop):
            for i,s in enumerate(su):
                if s!=1: continue
                if any(w!=u and forced(su,u,sw,w)=={(u,i)} for w,sw in enumerate(pop)): continue
                if any(forced(su,u,sw,("free",q))=={(u,i)} for q,sw in enumerate(free)): continue
                return False
        return True
    survivors=[p for p in pops if ok(p)]
    return {"source_multisets":len(pops),"residual_free_types":len(free),"supplement_feasible":len(survivors),"examples":survivors[:2]}

print(json.dumps({name:run(*case) for name,case in CASES.items()},indent=2))
