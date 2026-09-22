#!/usr/bin/env python3
"""Exact optimistic equality-core screen at r=8; candidates are not graphs."""
import itertools,json

def parts(n,hi=None):
    if n==0: yield (); return
    hi=min(n,hi or n)
    for x in range(hi,0,-1):
        for z in parts(n-x,x): yield (x,)+z

def canonical(R,edges,h):
    groups=[]
    for x in sorted(set(R),reverse=True): groups.append(tuple(i for i,y in enumerate(R) if y==x))
    best=None
    for choices in itertools.product(*(itertools.permutations(g) for g in groups)):
        p=list(range(len(R)))
        for g,im in zip(groups,choices):
            for old,new in zip(g,im): p[old]=new
        ee=tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in edges))
        hh=[0]*len(R)
        for old,new in enumerate(p): hh[new]=h[old]
        form=(ee,tuple(hh))
        if best is None or form<best: best=form
    return best

out={}
for R in parts(8):
    k=len(R); classes={}; labelled=0
    if all(x==1 for x in R):
        out[str(R)]={'labelled_equality_candidates':0,'candidate_orbits':0,'orbit_representatives':[],
                     'excluded_by':'all-unit equality theorem'}
        continue
    pairs=list(itertools.combinations(range(k),2))
    for mask in range(1<<len(pairs)):
        edges=[pairs[q] for q in range(len(pairs)) if mask>>q&1]
        if not edges: continue
        deg=[0]*k; neigh=[[] for _ in R]; adj=[set() for _ in R]
        for i,j in edges: deg[i]+=1;deg[j]+=1;neigh[i].append(j);neigh[j].append(i);adj[i].add(j);adj[j].add(i)
        seen=set(); bad=False
        for root in range(k):
            if root in seen: continue
            stack=[root]; comp={root};seen.add(root)
            while stack:
                i=stack.pop()
                for j in adj[i]-seen: seen.add(j);comp.add(j);stack.append(j)
            if len(comp)>=3 and all(R[i]==1 and len(adj[i])==2 for i in comp): bad=True
        if bad: continue
        P=[i for i in range(k) if deg[i]>R[i]]; N=[i for i in range(k) if i not in P]
        if any((deg[i]-R[i])**2>sum(R[j] for j in neigh[i]) for i in P): continue
        base=sum(i in P and j in P for i,j in edges)-sum(i in N and j in N for i,j in edges)-sum(R[i] for i in P)
        ranges=[]
        for i in range(k):
            if i in P: ranges.append((0,))
            elif R[i]==1: ranges.append((R[i]-deg[i],))
            else: ranges.append(tuple(range(max(0,R[i]-deg[i])+1)))
        for h in itertools.product(*ranges):
            if sum(h)!=base: continue
            labelled+=1; key=canonical(R,edges,h)
            if key in classes: classes[key]['labelled_count']+=1; continue
            ce,ch=key; cedges=[list(e) for e in ce]
            cdeg=[0]*k; cn=[[] for _ in R]
            for i,j in ce: cdeg[i]+=1;cdeg[j]+=1;cn[i].append(j);cn[j].append(i)
            cP=[i for i in range(k) if cdeg[i]>R[i]]; cN=[i for i in range(k) if i not in cP]
            classes[key]={'representative':{'edges':cedges,'core_degrees':cdeg,'P':cP,'N':cN,'h':list(ch),
              'actual_degrees':[R[i]-ch[i] if i in cN else cdeg[i] for i in range(k)],
              'selected_lower_bounds':[max(0,cdeg[i]-R[i]) for i in range(k)]},'labelled_count':1}
    out[str(R)]={'labelled_equality_candidates':labelled,'candidate_orbits':len(classes),'orbit_representatives':list(classes.values())}
print(json.dumps(out,indent=2))
