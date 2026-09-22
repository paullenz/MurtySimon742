#!/usr/bin/env python3
"""Independent SciPy/HiGHS MILP replay of r=10 support-nine source infeasibility."""
import itertools,json,multiprocessing as mp
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csc_matrix
R=(2,1,1,1,1,1,1,1,1);k=9
upairs=list(itertools.combinations(range(1,9),2))
def one(line):
 f=list(map(int,line.split()));ug,hs,t=f[:3]
 edges=[upairs[q] for q in range(28) if ug>>q&1]+[(0,i+1) for i in range(8) if hs>>i&1]
 neigh=[set() for _ in R];deg=[0]*k
 for i,j in edges:neigh[i].add(j);neigh[j].add(i);deg[i]+=1;deg[j]+=1
 need=np.array([max(0,deg[i]-R[i]) for i in range(k)],dtype=float)
 cols=[]
 for state in itertools.product(range(3),repeat=k):
  L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
  if not Z or any(not neigh[i]<=L|Z or len(neigh[i]&L)>R[i] for i in L):continue
  cols.append([int(i in Z) for i in range(k)]+[int(i in L) for i in range(k)])
 A=csc_matrix(np.array(cols,dtype=float).T)
 lb=np.r_[np.array(R,dtype=float),need];ub=np.r_[np.array(R,dtype=float),np.full(k,np.inf)]
 res=milp(np.zeros(len(cols)),integrality=np.ones(len(cols)),bounds=Bounds(0,np.inf),
          constraints=LinearConstraint(A,lb,ub),options={'time_limit':120})
 return {'unit_mask':ug,'heavy_neighbour_mask':hs,'patterns':len(cols),
         'status':int(res.status),'success':bool(res.success),'message':str(res.message)}
if __name__=='__main__':
 lines=open('r10_211111111_masks.txt').read().splitlines()
 with mp.Pool(6) as pool: rows=list(pool.imap_unordered(one,lines))
 counts={str(s):sum(r['status']==s for r in rows) for s in sorted(set(r['status'] for r in rows))}
 assert all(not r['success'] and r['status']==2 for r in rows),counts
 print(json.dumps({'cases':len(rows),'status_counts':counts,'feasible':sum(r['success'] for r in rows),
  'rows':sorted(rows,key=lambda x:(x['unit_mask'],x['heavy_neighbour_mask'])),
  'scope':'Independent integer linear feasibility replay using SciPy/HiGHS.'},indent=2))
