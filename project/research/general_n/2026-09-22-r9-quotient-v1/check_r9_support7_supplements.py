2026-09-22T15:14:02+01:00
#!/usr/bin/env python3
"""Exact source populations and supplement forcing for two r=9 kernels."""
import itertools, json

R=(2,2,1,1,1,1,1)
CASES={
  120436:[(0,3),(0,5),(0,6),(1,2),(1,5),(1,6),(2,4),(2,6),(3,4),(3,5)],
  378090:[(0,2),(0,4),(0,6),(1,2),(1,3),(1,6),(2,6),(3,4),(3,5),(4,5)],
}

def run(edges):
    k=len(R);neighbors=[set() for _ in R];deg=[0]*k
    for i,j in edges:
        neighbors[i].add(j);neighbors[j].add(i);deg[i]+=1;deg[j]+=1
    need=tuple(deg[i]-R[i] for i in range(k))
    assert all(x>0 for x in need)
    patterns=[]
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1}
        Z={i for i,s in enumerate(state) if s==2}
        if any(not neighbors[i]<=L|Z or len(neighbors[i]&L)>R[i] for i in L):
            continue
        if not Z:
            assert not L
            continue
        patterns.append((tuple(int(i in Z) for i in range(k)),
                         tuple(int(i in L) for i in range(k)),state))
    pops=[]
    def search(start,rem,x,chosen):
        if not any(rem):
            if all(x[i]>=need[i] for i in range(k)):pops.append(tuple(chosen))
            return
        for q in range(start,len(patterns)):
            z,l,state=patterns[q]
            if all(z[i]<=rem[i] for i in range(k)):
                search(q,tuple(rem[i]-z[i] for i in range(k)),
                       tuple(x[i]+l[i] for i in range(k)),chosen+[state])
    search(0,R,(0,)*k,[])
    def supplement_ok(pop):
        L=[{i for i,s in enumerate(st) if s==1} for st in pop]
        for u in range(len(pop)):
            for i in L[u]:
                possible=len(L[u])==1
                for w in range(len(pop)):
                    if w==u:continue
                    forced={(u,j) for j in L[u] if pop[w][j]==0}
                    forced|={(w,j) for j in L[w] if pop[u][j]==0}
                    possible |= forced=={(u,i)}
                if not possible:return False
        return True
    survivors=[p for p in pops if supplement_ok(p)]
    return {'R':R,'edges':edges,'degrees':deg,'selected_lower_bounds':need,
            'single_source_patterns':len(patterns),'source_multisets':len(pops),
            'supplement_feasible':len(survivors),
            'source_examples':pops[:5],'supplement_examples':survivors[:5],
            'scope':'Exact necessary C-source and B-edge forcing kernel; not graph realization.'}

print(json.dumps({str(mask):run(edges) for mask,edges in CASES.items()},indent=2))
