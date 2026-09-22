#!/usr/bin/env python3
"""Independent Burnside and canonical replay of the r=10 support-nine core census."""
import itertools,json,math
perms=list(itertools.permutations(range(8)))
pairs=list(itertools.combinations(range(8),2));pidx={e:q for q,e in enumerate(pairs)}
def orbit_count(perm,objects,action):
 seen=set();c=0
 for x in objects:
  if x in seen:continue
  c+=1;y=x
  while y not in seen:
   seen.add(y);y=action(y,perm)
 return c
vertex_orbits=[];edge_orbits=[]
for p in perms:
 vertex_orbits.append(orbit_count(p,range(8),lambda i,p:p[i]))
 edge_orbits.append(orbit_count(p,pairs,lambda e,p:tuple(sorted((p[e[0]],p[e[1]])))))
unlabelled_graphs=sum(1<<e for e in edge_orbits)//math.factorial(8)
rooted_coloured=sum(1<<(v+e) for v,e in zip(vertex_orbits,edge_orbits))//math.factorial(8)
def transform(ug,hs,p):
 eu=0
 for q,(i,j) in enumerate(pairs):
  if ug>>q&1:
   a,b=sorted((p[i],p[j]));eu|=1<<pidx[(a,b)]
 eh=sum(1<<p[i] for i in range(8) if hs>>i&1)
 return (eu<<8)|eh
rows=[]
for line in open('r10_211111111_masks.txt'):
 f=list(map(int,line.split()));ug,hs,t=f[:3];stored=f[3:]
 edges=[(i+1,j+1) for q,(i,j) in enumerate(pairs) if ug>>q&1]+[(0,i+1) for i in range(8) if hs>>i&1]
 R=(2,1,1,1,1,1,1,1,1);deg=[0]*9;adjR=[0]*9
 for i,j in edges:deg[i]+=1;deg[j]+=1;adjR[i]+=R[j];adjR[j]+=R[i]
 P=[deg[i]>R[i] for i in range(9)]
 assert all(not P[i] or (deg[i]-R[i])**2<=adjR[i] for i in range(9))
 eP=sum(P[i] and P[j] for i,j in edges);eN=sum(not P[i] and not P[j] for i,j in edges)
 slack=sum(i>0 and not P[i] and deg[i]==0 for i in range(9))
 tt=eP-eN-sum(R[i] for i in range(9) if P[i])-slack
 assert tt==t and deg==stored and t>0
 rows.append((ug,hs))
canonical=[min(transform(ug,hs,p) for p in perms) for ug,hs in rows]
assert len(set(canonical))==len(rows)==146
out={'burnside_unlabelled_graphs_n8':unlabelled_graphs,
     'burnside_rooted_coloured_orbits':rooted_coloured,
     'strict_rows_replayed':len(rows),'strict_canonical_forms_unique':len(set(canonical)),
     'expected':{'unlabelled_graphs_n8':12346,'rooted_coloured_orbits':2208612,'strict_rows':146},
     'pass':unlabelled_graphs==12346 and rooted_coloured==2208612 and len(set(canonical))==146}
print(json.dumps(out,indent=2))
