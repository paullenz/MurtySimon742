#!/usr/bin/env python3
"""Independent arithmetic replay for the noncheap R_N and E=1 theorem.

This scans abstract integer parameter states only. It is NOT a D2C graph
enumerator and makes no graph-realizability claim.
"""
import math, runpy
from collections import Counter
from functools import lru_cache
from pathlib import Path

HERE=Path(__file__).resolve().parent
PAIR=HERE.parent / "2026-09-19-minimal-reservoir-pair-hall-v1" / "check_minimal_reservoir_pair_hall.py"
SPHERE=HERE.parent / "2026-09-19-minimal-reservoir-slot-sphere-v1" / "check_minimal_reservoir_slot_sphere.py"
P=runpy.run_path(str(PAIR))
S=runpy.run_path(str(SPHERE))

phi=P["phi"]; C0=P["C0"]; predecessor_floor=P["predecessor_floor"]
repaired_floor=P["repaired_floor"]; preceding_mg1_score=P["preceding_mg1_score"]
hmin_closed=P["hmin_closed"]; sigma_pair=P["sigma_pair"]
rows_for_state=S["rows_for_state"]; nu_min=S["nu_min"]

@lru_cache(None)
def mu(j):
    if j<=0:return 0
    q=max(0,(1+math.isqrt(1+8*j))//2)
    while q*(q-1)//2<j:q+=1
    while q>0 and (q-1)*(q-2)//2>=j:q-=1
    return q

@lru_cache(None)
def eta(j):
    if j<=0:return 0
    q=max(0,(math.isqrt(1+8*j)-1)//2)
    while q*(q+1)//2<j:q+=1
    while q>0 and (q-1)*q//2>=j:q-=1
    return q

@lru_cache(None)
def support_sizes(p,g,k,E):
    q=p-2
    out=set()
    if q<=0:return tuple()
    if E<=g*q and E>0:
        for ell in range((E+q-1)//q,min(E,g)+1):out.add(ell)
    for estar in range(1,q+1):
        R=E-k*estar
        if R<0 or R>g*q:continue
        if R==0:
            out.add(k)
        else:
            for ell in range((R+q-1)//q,min(R,g)+1):out.add(k+ell)
    return tuple(sorted(out))

@lru_cache(None)
def Cx(x,E):
    m=min(E,x)
    if 2*m>=x:return x*x//4
    return m*(x-m)

@lru_cache(None)
def gamma_floor(p,g,k,x,E,e):
    ss=support_sizes(p,g,k,E)
    if not ss:return None
    bx=math.comb(x,2)
    return min(s+mu(max(0,e-bx+math.comb(x-s,2))) for s in ss)

@lru_cache(None)
def RN_range(p,x,y,g,k,e,Elo):
    """Independent replay of R_N, optionally restricted to E>=2."""
    a=x+y; best=None; bestE=[]
    for E in range(Elo,x*(p-2)+1):
        G=gamma_floor(p,g,k,x,E,e)
        if G is None:continue
        parity=(y*E+2*max(0,e-Cx(x,E))+(a-2))//(a-1)
        val=a+y*((E+x-1)//x)+max(G,parity)
        if best is None or val<best:
            best=val; bestE=[E]
        elif val==best:
            bestE.append(E)
    return best,tuple(bestE)

def cheap_zero_rho_cap(x,g,k,A):
    if A==0:
        return min(x-1,max(0,min(2,g-1)))
    return min(x-1,k+(1 if g>=2 else 0))

def E1_slot_floor(x,y,g,k,A,e):
    c=cheap_zero_rho_cap(x,g,k,A)
    return x+y+y+1+eta(max(0,e-c))

def sphere_survives(p,u,lam,x,y,g,k,cap,Q,N,Y0,sig):
    a=x+y; T0=a-p; base=(p-lam)*(p+u)
    for M in range(N+1):
        A=g
        D=Q-(2*k-1)*A-k*M
        sphere_out=p*(g+1)+k+M
        if sphere_out+max(0,D)>cap-sig:continue
        LXmax=cap-sig-sphere_out
        ZX=k*(x-1)+x+A+k*(N-M)
        Emin=max(0,math.ceil((x*(x-T0)+ZX-LXmax)/2))
        Emax=math.comb(g,2)+k*A
        if Emin>Emax:continue
        nu=nu_min(Emin,g,A,k)
        if nu is None:continue
        qmax=math.comb(u,2)-math.comb(k+1,2)-k-M
        EUmax=cap-Y0-max(0,D)
        if base+qmax+EUmax>=a+nu:return True
    return False

def main():
    c=Counter(); by_t=Counter(); opt=Counter()

    for p in range(3,19):
      for u in range(1,19):
        b=2*p+u
        for lam in range(0,b-3):
          a=b-lam-1
          if a<4:continue
          cap=C0(p,u,lam)
          if cap<0:continue
          for x in range(3,a):
            y=a-x
            for g in range(0,p):
              k=x-g; t=p-g
              if k<=0 or k+1>u:continue
              if predecessor_floor(p,x,y,g)>cap:continue
              if u<x+2:continue
              if repaired_floor(p,u,lam,x,y,g)>cap:continue
              old=preceding_mg1_score(p,u,lam,x,y,g)
              if old is None or old>cap:continue

              T0=a-p; N=u-k-2; s1=max(0,t-k+1)
              Y0=y*(p+2)
              Q=x*(x-T0)+k*(x-1)+x-g*(g-1)+k*N
              Ebase=k*(p+k)+2*t+k+g*s1
              if Ebase+Y0+hmin_closed(Q,k,g,N)>cap:continue

              P0=k*(p+k)+t+Y0
              O0=t+k+g*s1
              sig=sigma_pair(p,u,lam,x,y,g,P0,cap)
              if sig is None:continue
              BP=cap-O0-sig
              if hmin_closed(Q,k,g,N)>BP:continue

              rows=rows_for_state(p,u,lam,x,y,g,k,cap,Q,N,BP,Y0)
              sphere=sphere_survives(p,u,lam,x,y,g,k,cap,Q,N,Y0,sig)

              old_noncheap=any(rupper>=a+y for A,M,D,H,Emin,nu,rupper in rows)
              if not (old_noncheap or sphere):continue
              c["old_dichotomy_survive"]+=1

              rn_alive=False
              final_alive=False
              best_candidates=[]

              for A,M,D,H,Emin,nu,rupper in rows:
                  rn,_=RN_range(p,x,y,g,k,Emin,1)
                  if rn is not None and rupper>=rn:
                      rn_alive=True

                  # E=1 structural branch.
                  e1=False; r1=None
                  d=g-A
                  if support_sizes(p,g,k,1):
                      if (k>1 and 0<=d<=1) or (k==1 and 0<=d<=2):
                          pair_lhs=p*(g+1)+k+M-(k+1)*d+D
                          if pair_lhs<=cap-sig:
                              r1=E1_slot_floor(x,y,g,k,A,Emin)
                              if rupper>=r1:e1=True

                  # E>=2 retains the independent R_N replay.
                  r2,Es=RN_range(p,x,y,g,k,Emin,2)
                  e2=(r2 is not None and rupper>=r2)

                  if e1 or e2:
                      final_alive=True
                      if e1:best_candidates.append((r1,"E1"))
                      if e2:best_candidates.append((r2,"E2+"))

              rn_union=rn_alive or sphere
              final_union=final_alive or sphere
              if rn_union:
                  c["RN_union_survive"]+=1; by_t[("rn",t)]+=1
              else:
                  c["RN_union_reject"]+=1
              if final_union:
                  c["final_union_survive"]+=1; by_t[("final",t)]+=1
              else:
                  c["final_union_reject"]+=1; by_t[("final_reject",t)]+=1
              if rn_alive and not final_alive:
                  c["one_defect_noncheap_closures"]+=1

              if final_alive:
                  best=min(v for v,_ in best_candidates)
                  types={typ for v,typ in best_candidates if v==best}
                  opt["E1" if "E1" in types else "E2+"]+=1
                  if t==1:
                      opt["t1_E1" if "E1" in types else "t1_E2+"]+=1

    expected={
      "old_dichotomy_survive":64557,
      "RN_union_survive":64461,
      "RN_union_reject":96,
      "final_union_survive":64457,
      "final_union_reject":100,
      "one_defect_noncheap_closures":6,
    }
    bad={k:(v,c[k]) for k,v in expected.items() if c[k]!=v}
    assert by_t[("rn",1)]==5404
    assert by_t[("final",1)]==5404
    assert opt["t1_E1"]==4762
    assert opt["t1_E2+"]==642

    print({
      "counts":dict(c),
      "optimizer":dict(opt),
      "new_union_rejections_by_t":{t:by_t[("final_reject",t)] for t in range(1,19) if by_t[("final_reject",t)]},
      "expected_mismatches":bad,
      "failures":len(bad),
      "trust":"abstract integer/arithmetic diagnostic only; no graph-realizability claim",
    })
    if bad:raise SystemExit(1)

if __name__=="__main__":main()
