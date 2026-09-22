#!/usr/bin/env python3
"""Optimistic equality-core screen at r=6; candidates are not graphs."""
import itertools,json

def parts(n,hi=None):
    if n==0:yield ();return
    hi=min(n,hi or n)
    for x in range(hi,0,-1):
        for tail in parts(n-x,x):yield (x,)+tail

def canonical(R,edges,h):
    groups={}
    for i,x in enumerate(R):groups.setdefault(x,[]).append(i)
    forms=[]
    for choices in itertools.product(*(list(itertools.permutations(g)) for g in groups.values())):
        mp={}
        for g,p in zip(groups.values(),choices):
            for old,new in zip(g,p):mp[old]=new
        ee=tuple(sorted(tuple(sorted((mp[i],mp[j]))) for i,j in edges))
        hh=tuple(h[mp.index(i)] if False else 0 for i in range(len(R)))
        # Transform old-index h to new indices.
        ht=[0]*len(R)
        for old,new in mp.items():ht[new]=h[old]
        forms.append((ee,tuple(ht)))
    return min(forms)

out={}
for R in parts(6):
    k=len(R);pairs=list(itertools.combinations(range(k),2));classes={};labelled=0
    for mask in range(1<<len(pairs)):
        edges=[pairs[q] for q in range(len(pairs)) if mask>>q&1]
        deg=[0]*k;neigh=[[] for _ in R]
        for i,j in edges:deg[i]+=1;deg[j]+=1;neigh[i].append(j);neigh[j].append(i)
        if any(R[i]+R[j]<2 for i,j in edges):continue
        P=[i for i in range(k) if deg[i]>R[i]];N=[i for i in range(k) if i not in P]
        if any((deg[i]-R[i])**2>sum(R[j] for j in neigh[i]) for i in P):continue
        eP=sum(i in P and j in P for i,j in edges);eN=sum(i in N and j in N for i,j in edges)
        base=eP-eN-sum(R[i] for i in P)
        ranges=[]
        for i in range(k):
            if i in P:ranges.append((0,))
            elif R[i]==1:ranges.append((R[i]-deg[i],))
            else:ranges.append(tuple(range(R[i]-deg[i]+1)))
        for h in itertools.product(*ranges):
            if sum(h)!=base:continue
            # All-unit equality is already rigorously excluded.
            if all(x==1 for x in R):continue
            labelled+=1;key=canonical(R,edges,h)
            if key not in classes:
                classes[key]={'representative':{'edges':edges,'core_degrees':deg,'P':P,'N':N,'h':h,
                  'actual_degrees':[R[i]-h[i] if i in N else deg[i] for i in range(k)],
                  'selected_lower_bounds':[max(0,deg[i]-R[i]) for i in range(k)]},'labelled_count':0}
            classes[key]['labelled_count']+=1
    out[str(R)]={'labelled_equality_candidates':labelled,'candidate_orbits':len(classes),
      'orbit_representatives':list(classes.values())}
print(json.dumps(out,indent=2))
