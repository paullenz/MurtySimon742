import json
D=json.load(open('project/research/post_ms/2026-09-21-q3-star-support-v1/PARITY_STAR_MAXSAT_GRID.json'));base=D['base_codes']
for z in D['rows']:
 r,q=z['r'],z['q'];codes=base+['P0']*r+['P1']*q;E={tuple(sorted(e)) for e in z['A_edges']}
 R=[i for i,c in enumerate(codes) if c=='P0'];T=[i for i,c in enumerate(codes) if c=='P1'];S=[i for i,c in enumerate(codes) if c.startswith('S')]
 def adj(i,j):return tuple(sorted((i,j))) in E
 obligations=[]; targets=[]; B={}
 for x in S:
  bridge=sum(adj(x,t) for t in T)+sum(adj(x,y) and codes[y]!=codes[x] for y in S)
  for rr in R:
   if adj(rr,x):obligations.append(('R',rr,x))
  for t in T:
   if adj(t,x):
    if bridge==1: targets.append(('slot',x))
    else: obligations.append(('T',t,x))
 missing=[(rr,t) for rr in R for t in T if not adj(rr,t)]
 targets += [('pair',rr,t) for rr,t in missing]
 for o in obligations:B[('o',o)]=[]
 for tar in targets:B.setdefault(('x',tar),[])
 for o in obligations:
  typ,v,x=o
  if typ=='R':
   for t in T:
    if adj(t,x) and not adj(v,t) and {y for y in range(len(codes)) if adj(v,y) and adj(t,y)}=={x}:B[('o',o)].append(('x',('pair',v,t)))
  else:
   for rr in R:
    if adj(rr,x) and not adj(rr,v) and {y for y in range(len(codes)) if adj(rr,y) and adj(v,y)}=={x}:B[('o',o)].append(('x',('pair',rr,v)))
 # eligible bucket assignment by reclassifying T edge
 for o in obligations:
  typ,v,x=o
  if typ=='T':
   bridge=sum(adj(x,t) for t in T)+sum(adj(x,y) and codes[y]!=codes[x] for y in S)
   if bridge==1:B[('o',o)].append(('x',('slot',x)))
 mt={}
 def aug(u,seen):
  for v in B[u]:
   if v in seen:continue
   seen.add(v)
   if v not in mt or aug(mt[v],seen): mt[v]=u;return True
  return False
 matched=sum(aug(('o',o),set()) for o in obligations)
 
 low=sum(1 for x in S for t in T if adj(x,t) and (sum(adj(x,u) for u in T)+sum(adj(x,y) and codes[y]!=codes[x] for y in S)==1))
 es=sum(1 for i,x in enumerate(S) for y in S[i+1:] if adj(x,y))
 L=low+es; h=len(obligations)-matched
 print(r,q,'ob',len(obligations),'matched',matched,'h',h,'L',L,'slack',len(S)-L,'condition',h<=len(S)-L)
