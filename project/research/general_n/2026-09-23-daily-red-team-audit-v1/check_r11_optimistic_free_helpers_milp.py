#!/usr/bin/env python3
"""Optimistic r=11 MILP replay allowing every residual-free helper type.

If this relaxation is infeasible, the old exclusion survives the omitted helper
class.  A feasible result reopens the kernel and blocks the r=11/S<=13 claim
until an exact helper-aware enumeration is completed.
"""
import itertools, json, multiprocessing as mp
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix

ROOT=Path(__file__).resolve().parents[1]/"2026-09-22-r11-quotient-v1"
def inputs():
 for support,name in [(8,"r11_support8_sources_case2.json"),(9,"r11_support9_sources_case1.json"),(10,"r11_support10_sources.json")]:
  for row in json.loads((ROOT/name).read_text())["feasible_rows"]: yield support,name,row

def solve(item):
 idx,(support,name,row)=item; R=tuple(row["R"]); edges=[tuple(e) for e in row["edges"]]; k=len(R)
 neigh=[set() for _ in R]; deg=[0]*k
 for i,j in edges: neigh[i].add(j);neigh[j].add(i);deg[i]+=1;deg[j]+=1
 need=tuple(max(0,deg[i]-R[i]) for i in range(k));P={i for i in range(k) if need[i]>0};patterns=[];free=[]
 for state in itertools.product(range(3),repeat=k):
  L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
  if any(not neigh[i]<=L|Z or len(neigh[i]&L)>R[i] for i in L):continue
  if not Z:
   if not(L&P):free.append((state,L))
   continue
  patterns.append((state,L,Z))
 m=len(patterns);n=2*m;A=[];lo=[];hi=[]
 for i in range(k):
  a=np.zeros(n)
  for p,(_,_,Z) in enumerate(patterns):a[p]=i in Z
  A.append(a);lo.append(R[i]);hi.append(R[i])
 for i in range(k):
  a=np.zeros(n)
  for p,(_,L,_) in enumerate(patterns):a[p]=i in L
  A.append(a);lo.append(need[i]);hi.append(np.inf)
 for p in range(m):
  a=np.zeros(n);a[p]=1;a[m+p]=-1;A.append(a);lo.append(0);hi.append(np.inf)
  a=np.zeros(n);a[p]=1;a[m+p]=-11;A.append(a);lo.append(-np.inf);hi.append(0)
 helper_constraints=0;free_discharges=0
 for p,(sp,Lp,_) in enumerate(patterns):
  if len(Lp)==1:continue
  for i in Lp:
   def helps(sq,Lq):
    return sq[i]==0 and all(sq[j]!=0 for j in Lp if j!=i) and all(sp[j]!=0 for j in Lq)
   if any(helps(sq,Lq) for sq,Lq in free):free_discharges+=1;continue
   helpers=[q for q,(sq,Lq,_) in enumerate(patterns) if q!=p and helps(sq,Lq)]
   a=np.zeros(n);a[m+p]=1
   for q in helpers:a[m+q]-=1
   A.append(a);lo.append(-np.inf);hi.append(0);helper_constraints+=1
 res=milp(np.zeros(n),integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.r_[np.full(m,11.),np.ones(m)]),constraints=LinearConstraint(csc_matrix(np.vstack(A)),np.array(lo),np.array(hi)),options={"time_limit":120.})
 return {"index":idx,"support":support,"file":name,"key":[row.get("mask"),row.get("unit_mask"),row.get("heavy_neighbours")],"status":int(res.status),"success":bool(res.success),"free_types":len(free),"free_discharges":free_discharges,"helper_constraints":helper_constraints,"message":res.message}

if __name__=="__main__":
 data=list(inputs())
 with mp.Pool(8) as pool:rows=list(pool.imap_unordered(solve,enumerate(data)))
 rows.sort(key=lambda x:x["index"])
 print(json.dumps({"kernels":len(rows),"feasible":sum(r["success"] for r in rows),"infeasible":sum(r["status"]==2 for r in rows),"unknown":sum(r["status"] not in (0,2) for r in rows),"rows":rows},indent=2))
