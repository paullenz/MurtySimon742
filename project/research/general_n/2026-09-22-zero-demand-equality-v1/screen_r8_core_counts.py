#!/usr/bin/env python3
"""Exact labelled/core-signature first pass for optimistic r=8 strict surplus."""
import itertools,json

def parts(n,hi=None):
    if n==0:yield ();return
    hi=min(n,hi or n)
    for x in range(hi,0,-1):
        for tail in parts(n-x,x):yield (x,)+tail

out={}
for R in parts(8):
    k=len(R)
    if all(x==1 for x in R):
        out[str(R)]={'excluded_by':'unit-column theorem','strict_survivors_labelled':0};continue
    pairs=list(itertools.combinations(range(k),2));checked=0;survivors=0;signatures={};examples=[]
    for mask in range(1<<len(pairs)):
        edges=[pairs[q] for q in range(len(pairs)) if mask>>q&1]
        deg=[0]*k;neigh=[[] for _ in R]
        for i,j in edges:deg[i]+=1;deg[j]+=1;neigh[i].append(j);neigh[j].append(i)
        if any(R[i]+R[j]<2 for i,j in edges):continue
        P=[i for i in range(k) if deg[i]>R[i]];N=[i for i in range(k) if i not in P]
        if any((deg[i]-R[i])**2>sum(R[j] for j in neigh[i]) for i in P):continue
        eP=sum(i in P and j in P for i,j in edges);eN=sum(i in N and j in N for i,j in edges)
        slack=sum(1 for i in N if R[i]==1 and deg[i]==0)
        t=eP-eN-sum(R[i] for i in P)-slack;checked+=1
        if t<=0:continue
        survivors+=1
        groups=[]
        for value in sorted(set(R),reverse=True):
            groups.append((value,tuple(sorted((deg[i],int(i in P)) for i,x in enumerate(R) if x==value))))
        sig=str((t,tuple(groups)));signatures[sig]=signatures.get(sig,0)+1
        if len(examples)<8:examples.append({'edges':edges,'degrees':deg,'P':P,'N':N,'t_upper':t,'selected_lower_bounds':[max(0,deg[i]-R[i]) for i in range(k)]})
    out[str(R)]={'support':k,'core_graphs_checked_after_local_filters':checked,
      'strict_survivors_labelled':survivors,'degree_P_signature_counts':signatures,
      'first_examples':examples,'scope':'Labelled necessary relaxation; signatures are not graph-isomorphism orbits.'}
print(json.dumps(out,indent=2))
