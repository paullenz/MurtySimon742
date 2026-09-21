#!/usr/bin/env python3
"""Audit the exact local certificate-graph obstruction on saved D2C models."""
import json
from pathlib import Path
here=Path(__file__).parent

def audit(base,z):
 r,q=z['r'],z['q'];codes=base+['P0']*r+['P1']*q
 E={tuple(sorted(e)) for e in z['A_edges']}; ad=lambda i,j:tuple(sorted((i,j))) in E
 R=[i for i,c in enumerate(codes) if c=='P0'];T=[i for i,c in enumerate(codes) if c=='P1'];S=[i for i,c in enumerate(codes) if c.startswith('S')]
 rows=[]
 for x in S:
  bd=sum(ad(x,t) for t in T)+sum(ad(x,y) and codes[y]!=codes[x] for y in S)
  if bd<2:continue
  V=[i for i in R+T if ad(i,x)]; H={v:set() for v in V}
  for rr in R:
   for t in T:
    if rr in H and t in H and not ad(rr,t) and {y for y in range(len(codes)) if ad(rr,y) and ad(t,y)}=={x}:
     H[rr].add(t);H[t].add(rr)
  assert all(H[v] for v in V)
  seen=set();tree=0;comps=0
  for v in V:
   if v in seen:continue
   stack=[v];seen.add(v);vs=[]
   while stack:
    u=stack.pop();vs.append(u)
    for w in H[u]:
     if w not in seen:seen.add(w);stack.append(w)
   ee=sum(len(H[u]) for u in vs)//2;comps+=1;tree+=(ee==len(vs)-1)
  rows.append({'star_index':x,'bridge_degree':bd,'certificate_components':comps,'tree_components':tree})
 return {'r':r,'q':q,'high_bridge_stars':rows,'local_condition':all(x['tree_components']<=1 for x in rows)}
sets=[]
for fn in ['PARITY_STAR_MAXSAT_GRID.json','PARITY_STAR_PARAMETER_GRID.json']:
 d=json.loads((here/fn).read_text());rows=[audit(d['base_codes'],z) for z in d['rows']]
 sets.append({'source':fn,'models':len(rows),'violations':[x for x in rows if not x['local_condition']],'rows':rows})
out={'scope':'saved exact optima plus saved satisfiable parameter models','sets':sets}
(here/'PARITY_STAR_LOCAL_COMPONENT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
assert all(not x['violations'] for x in sets)
print('PASS:',sum(x['models'] for x in sets),'models; every high-bridge star has at most one tree component')
