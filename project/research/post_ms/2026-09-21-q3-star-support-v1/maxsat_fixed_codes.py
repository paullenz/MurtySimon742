#!/usr/bin/env python3
"""Exact maximum A-edge count for a fixed rooted code multiset."""
import sys,time
sys.path.insert(0,'/workspace/scratch/a4369cb67676/deps')
from pysat.formula import CNF,IDPool,WCNF
from pysat.examples.rc2 import RC2
from check_star_support import CODES,graph,d2c

def encode(codes):
 n=9+len(codes);fixed=set()
 def add(u,v):fixed.add(tuple(sorted((u,v))))
 for b in range(8):add(8,b)
 for b in range(8):
  for i in range(3):add(b,b^(1<<i))
 for i,c in enumerate(codes):
  for b in CODES[c]:add(9+i,b)
 vp=IDPool();cnf=CNF();avars={(9+i,9+j):vp.id(('e',i,j)) for i in range(len(codes)) for j in range(i+1,len(codes))}
 def edge(u,v,de=None):
  e=tuple(sorted((u,v)))
  if e==de:return False
  if e in fixed:return True
  return avars.get(e,False)
 for u in range(n):
  for v in range(u+1,n):
   direct=edge(u,v);lits=[] if direct is False else ([direct] if direct is not True else None)
   if lits is None:continue
   for z in range(n):
    if z in (u,v):continue
    a,b=edge(u,z),edge(z,v)
    if a is False or b is False:continue
    if a is True and b is True:lits=None;break
    if a is True:lits.append(b);continue
    if b is True:lits.append(a);continue
    q=vp.id(('path',u,v,z));cnf.extend([[-q,a],[-q,b],[-a,-b,q]]);lits.append(q)
   if lits is not None:cnf.append(lits)
 for de in sorted(fixed|set(avars)):
  ev=edge(*de);sels=[]
  candidates={tuple(sorted((x,w))) for x in de for w in range(n) if w!=x}
  for u,v in candidates:
   q=vp.id(('wit',de,u,v));sels.append(q)
   if ev is not True:cnf.append([-q,ev])
   direct=edge(u,v,de)
   if direct is True:cnf.append([-q]);continue
   if direct is not False:cnf.append([-q,-direct])
   impossible=False
   for z in range(n):
    if z in (u,v):continue
    a,b=edge(u,z,de),edge(z,v,de)
    if a is False or b is False:continue
    if a is True and b is True:impossible=True;break
    if a is True:cnf.append([-q,-b])
    elif b is True:cnf.append([-q,-a])
    else:cnf.append([-q,-a,-b])
   if impossible:cnf.append([-q])
  cnf.append(sels if ev is True else [-ev]+sels)
 return cnf,avars,vp.top

def maximize(codes):
 cnf,avars,nvars=encode(codes);w=WCNF()
 for c in cnf.clauses:w.append(c)
 for v in avars.values():w.append([v],weight=1)
 t=time.monotonic()
 with RC2(w,solver='cadical195') as rc:
  model=rc.compute();cost=rc.cost if model else None
 pos=set(x for x in (model or []) if x>0);ae=[(u-9,v-9) for (u,v),x in avars.items() if x in pos]
 if model:assert d2c(graph(codes,ae))
 return {'sat':model is not None,'max_A_edges':len(ae) if model else None,'A_edges':ae,'variables':nvars,'hard_clauses':len(cnf.clauses),'seconds':time.monotonic()-t}
