#!/usr/bin/env python3
"""Combined source/supplement MILP for the three r=12 support-six kernels."""
import itertools, json, multiprocessing as mp
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix

ROWS=[]
for partition,data in json.load(open("r12_support6.json")).items():
    for row in data["feasible"]:
        ROWS.append((partition,row))

def solve(item):
    index,(partition,row)=item;R=tuple(eval(partition));edges=[tuple(e) for e in row["edges"]]
    k=len(R);neigh=[set() for _ in R];deg=[0]*k
    for i,j in edges:neigh[i].add(j);neigh[j].add(i);deg[i]+=1;deg[j]+=1
    need=tuple(max(0,deg[i]-R[i]) for i in range(k));patterns=[]
    for state in itertools.product(range(3),repeat=k):
        L={i for i,s in enumerate(state) if s==1};Z={i for i,s in enumerate(state) if s==2}
        if not Z or any(not neigh[i]<=L|Z or len(neigh[i]&L)>R[i] for i in L):continue
        patterns.append((state,L,Z))
    m=len(patterns);nvar=2*m;A=[];lo=[];hi=[]
    for i in range(k):
        a=np.zeros(nvar)
        for p,(_,_,Z) in enumerate(patterns):a[p]=i in Z
        A.append(a);lo.append(R[i]);hi.append(R[i])
    for i in range(k):
        a=np.zeros(nvar)
        for p,(_,L,_) in enumerate(patterns):a[p]=i in L
        A.append(a);lo.append(need[i]);hi.append(np.inf)
    for p in range(m):
        a=np.zeros(nvar);a[p]=1;a[m+p]=-1;A.append(a);lo.append(0);hi.append(np.inf)
        a=np.zeros(nvar);a[p]=1;a[m+p]=-12;A.append(a);lo.append(-np.inf);hi.append(0)
    helper_constraints=0
    for p,(sp,Lp,_) in enumerate(patterns):
        if len(Lp)==1:continue
        for i in Lp:
            helpers=[]
            for q,(sq,Lq,_) in enumerate(patterns):
                if q==p or sq[i]!=0:continue
                if any(sq[j]==0 for j in Lp if j!=i):continue
                if any(sp[j]==0 for j in Lq):continue
                helpers.append(q)
            a=np.zeros(nvar);a[m+p]=1
            for q in helpers:a[m+q]-=1
            A.append(a);lo.append(-np.inf);hi.append(0);helper_constraints+=1
    result=milp(np.zeros(nvar),integrality=np.ones(nvar),
        bounds=Bounds(np.zeros(nvar),np.concatenate([np.full(m,12.0),np.ones(m)])),
        constraints=LinearConstraint(csc_matrix(np.vstack(A)),np.array(lo),np.array(hi)),
        options={"time_limit":300.0})
    return {"index":index,"partition":partition,"mask":row["mask"],"patterns":m,
            "helper_constraints":helper_constraints,"status":int(result.status),
            "success":bool(result.success),"message":result.message}

if __name__=="__main__":
    with mp.Pool(3) as pool:rows=list(pool.imap_unordered(solve,enumerate(ROWS)))
    rows.sort(key=lambda r:r["index"])
    print(json.dumps({"kernels":len(rows),"feasible":sum(r["success"] for r in rows),
      "infeasible":sum(r["status"]==2 for r in rows),
      "unknown":sum(r["status"] not in (0,2) for r in rows),"rows":rows,
      "scope":"Combined integer source/supplement MILP; internal computer-assisted evidence, not graph realization."},indent=2))
