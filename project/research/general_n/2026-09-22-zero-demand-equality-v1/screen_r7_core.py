#!/usr/bin/env python3
"""Optimistic exact residual-core screen at r=7; survivors are not graphs."""
import itertools,json

def parts(n,hi=None):
    if n==0:yield ();return
    hi=min(n,hi or n)
    for x in range(hi,0,-1):
        for tail in parts(n-x,x):yield (x,)+tail

def canonical(R,edges):
    groups={}
    for i,x in enumerate(R):groups.setdefault(x,[]).append(i)
    forms=[]
    for choices in itertools.product(*(list(itertools.permutations(g)) for g in groups.values())):
        mp={}
        for g,p in zip(groups.values(),choices):
            for old,new in zip(g,p):mp[old]=new
        forms.append(tuple(sorted(tuple(sorted((mp[i],mp[j]))) for i,j in edges)))
    return min(forms)

out={}
for R in parts(7):
    k=len(R)
    if all(x==1 for x in R):
        out[str(R)]={'excluded_by':'unit-column theorem','strict_survivor_orbits':0};continue
    pairs=list(itertools.combinations(range(k),2));survivors=[];checked=0
    for mask in range(1<<len(pairs)):
        edges=[pairs[q] for q in range(len(pairs)) if mask>>q&1]
        deg=[0]*k;neigh=[[] for _ in R]
        for i,j in edges:deg[i]+=1;deg[j]+=1;neigh[i].append(j);neigh[j].append(i)
        if any(R[i]+R[j]<2 for i,j in edges):continue
        P=[i for i in range(k) if deg[i]>R[i]];N=[i for i in range(k) if i not in P]
        if any((deg[i]-R[i])**2>sum(R[j] for j in neigh[i]) for i in P):continue
        eP=sum(i in P and j in P for i,j in edges);eN=sum(i in N and j in N for i,j in edges)
        slack=sum(1 for i in N if R[i]==1 and deg[i]==0)
        t_upper=eP-eN-sum(R[i] for i in P)-slack;checked+=1
        if t_upper>0:
            survivors.append({'edges':edges,'degrees':deg,'P':P,'N':N,'t_upper':t_upper,
              'selected_lower_bounds':[max(0,deg[i]-R[i]) for i in range(k)]})
    classes={}
    for s in survivors:
        key=canonical(R,s['edges'])
        if key not in classes:classes[key]={'representative':s,'labelled_count':0}
        classes[key]['labelled_count']+=1
    out[str(R)]={'support':k,'core_graphs_checked_after_local_filters':checked,
      'strict_survivors_labelled':len(survivors),'strict_survivor_orbits':len(classes),
      'orbit_representatives':list(classes.values())}
print(json.dumps(out,indent=2))
