#!/usr/bin/env python3
"""Exact SAT existence search for fixed Q3 code multisets, with every A-edge free."""
from pathlib import Path
import json,sys,time
sys.path.insert(0,'/workspace/scratch/a4369cb67676/deps')
from pysat.formula import CNF,IDPool
from pysat.solvers import Solver
from check_star_support import CODES,graph,d2c

def solve(codes):
 n=9+len(codes);fixed=set()
 def add(u,v):fixed.add(tuple(sorted((u,v))))
 for b in range(8):add(8,b)
 for b in range(8):
  for i in range(3):add(b,b^(1<<i))
 for i,c in enumerate(codes):
  for b in CODES[c]:add(9+i,b)
 vp=IDPool();cnf=CNF(); avars={}
 for i in range(len(codes)):
  for j in range(i+1,len(codes)):avars[(9+i,9+j)]=vp.id(('e',i,j))
 def edge(u,v,deleted=None):
  e=tuple(sorted((u,v)))
  if e==deleted:return False
  if e in fixed:return True
  return avars.get(e,False)
 # diameter <=2
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
 # Every present edge has a pair beyond distance 2 after deletion.
 for de in sorted(fixed|set(avars)):
  ev=edge(*de); selectors=[]
  candidates={tuple(sorted((x,w))) for x in de for w in range(n) if w!=x}
  for u,v in sorted(candidates):
   sel=vp.id(('wit',de,u,v));selectors.append(sel)
   if ev is not True:cnf.append([-sel,ev])
   direct=edge(u,v,de)
   if direct is True:cnf.append([-sel]);continue
   if direct is not False:cnf.append([-sel,-direct])
   impossible=False
   for z in range(n):
    if z in (u,v):continue
    a,b=edge(u,z,de),edge(z,v,de)
    if a is False or b is False:continue
    if a is True and b is True:impossible=True;break
    if a is True:cnf.append([-sel,-b])
    elif b is True:cnf.append([-sel,-a])
    else:cnf.append([-sel,-a,-b])
   if impossible:cnf.append([-sel])
  cnf.append(selectors if ev is True else [-ev]+selectors)
 start=time.monotonic()
 with Solver(name='cadical195',bootstrap_with=cnf) as s:
  sat=s.solve();model=set(x for x in s.get_model() if x>0) if sat else set()
 ae=[(u-9,v-9) for (u,v),x in avars.items() if x in model]
 if sat:assert d2c(graph(codes,ae))
 return {'sat':sat,'n':n,'variables':vp.top,'clauses':len(cnf.clauses),'seconds':time.monotonic()-start,'A_edges':ae}

def main():
 base=['C00','C10','C11','C20','C21','P0','P1','S0','S1','S6','S7']
 rows=[]
 for extra in ([],['S0'],['S6'],['S0','S6'],['C10'],['C21']):
  codes=base+extra;r=solve(codes);r['codes']=codes;rows.append(r);print(len(codes),extra,r,flush=True)
 Path(__file__).with_name('OPPOSITE_EDGE_CORE_SAT_RESULTS.json').write_text(json.dumps({'scope':'Exact over every A-edge for listed fixed physical code multisets; UNSAT applies only to that multiset, never arbitrary multiplicity.','rows':rows},indent=2)+'\n')
if __name__=='__main__':main()
