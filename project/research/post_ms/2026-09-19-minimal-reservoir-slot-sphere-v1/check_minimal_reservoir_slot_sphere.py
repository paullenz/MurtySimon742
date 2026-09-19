#!/usr/bin/env python3
"""Diagnostic replay for MINIMAL_RESERVOIR_SLOT_SPHERE_PINCH.md.

This scans abstract integer parameter states only. It is NOT a D2C graph
enumerator and makes no realizability claim.
"""
import math, runpy
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
PREV=HERE.parent / "2026-09-19-minimal-reservoir-pair-hall-v1" / "check_minimal_reservoir_pair_hall.py"
P=runpy.run_path(str(PREV))
phi=P["phi"]; C0=P["C0"]; predecessor_floor=P["predecessor_floor"]
repaired_floor=P["repaired_floor"]; preceding_mg1_score=P["preceding_mg1_score"]
hmin_closed=P["hmin_closed"]; sigma_pair=P["sigma_pair"]


def nu_min(e,g,A,k):
    if e<=0:return 0
    best=None
    for h in range(g+1):
        for c in range(k+1):
            if h*(h-1)//2+c*min(h,A)>=e:
                s=h+c
                if best is None or s<best: best=s
    return best


def rows_for_state(p,u,lam,x,y,g,k,cap,Q,N,BP,Y0):
    a=x+y; T0=a-p; base=(p-lam)*(p+u)
    out=[]
    for A in range(g+1):
        for M in range(N+1):
            D=Q-(2*k-1)*A-k*M
            H=A+M+max(0,D)
            if H>BP: continue
            qmax=math.comb(u,2)-math.comb(k+1,2)-k-M
            if qmax<0: continue
            EUmax=cap-Y0-max(0,D)
            LXmax=BP-A-M
            ZX=k*(x-1)+x+A+k*(N-M)
            Emin=max(0,math.ceil((x*(x-T0)+ZX-LXmax)/2))
            Emax=math.comb(g,2)+k*A
            if Emin>Emax: continue
            nu=nu_min(Emin,g,A,k)
            if nu is None: continue
            rupper=base+qmax+EUmax
            out.append((A,M,D,H,Emin,nu,rupper))
    return out


def main():
    c=Counter(); by_t=Counter()
    for p in range(3,19):
      for u in range(1,19):
        b=2*p+u
        for lam in range(0,b-3):
          a=b-lam-1
          if a<4: continue
          cap=C0(p,u,lam)
          if cap<0: continue
          for x in range(3,a):
            y=a-x
            for g in range(0,p):
              k=x-g; t=p-g
              if k<=0 or k+1>u: continue
              if predecessor_floor(p,x,y,g)>cap: continue
              if u<x+2: continue
              if repaired_floor(p,u,lam,x,y,g)>cap: continue
              old=preceding_mg1_score(p,u,lam,x,y,g)
              if old is None or old>cap: continue

              T0=a-p; N=u-k-2; s1=max(0,t-k+1)
              Ebase=k*(p+k)+2*t+k+g*s1
              Y0=y*(p+2)
              BX=x*(x-T0)+k*(x-1)+x-g*(g-1)
              Q=BX+k*N
              if Ebase+Y0+hmin_closed(Q,k,g,N)>cap: continue

              P0=k*(p+k)+t+Y0
              O0=t+k+g*s1
              sig=sigma_pair(p,u,lam,x,y,g,P0,cap)
              if sig is None: continue
              BP=cap-O0-sig
              if hmin_closed(Q,k,g,N)>BP: continue

              c["current"]+=1
              rows=rows_for_state(p,u,lam,x,y,g,k,cap,Q,N,BP,Y0)

              # Unit II: r>=a with physical q and E_U ceilings.
              plain=any(rupper>=a for A,M,D,H,Emin,nu,rupper in rows)
              if not plain: c["plain_slot_reject"]+=1

              # Branch N: any extra Hamming unit forces r>=a+y.
              noncheap=any(rupper>=a+y for A,M,D,H,Emin,nu,rupper in rows)

              # Branch S: all distances one. The criticality theorem forces A=g;
              # the selected sphere witnesses strengthen the outside-pair bill.
              sphere=False
              base=(p-lam)*(p+u)
              for M in range(N+1):
                  A=g
                  D=Q-(2*k-1)*A-k*M
                  # S-S_P contains sphere-witness slack plus L_X.
                  sphere_out=p*(g+1)+k+M
                  if sphere_out+max(0,D)>cap-sig: continue
                  LXmax=cap-sig-sphere_out
                  ZX=k*(x-1)+x+A+k*(N-M)
                  Emin=max(0,math.ceil((x*(x-T0)+ZX-LXmax)/2))
                  Emax=math.comb(g,2)+k*A
                  if Emin>Emax: continue
                  nu=nu_min(Emin,g,A,k)
                  if nu is None: continue
                  qmax=math.comb(u,2)-math.comb(k+1,2)-k-M
                  EUmax=cap-Y0-max(0,D)
                  rupper=base+qmax+EUmax
                  if rupper>=a+nu:
                      sphere=True; break

              if not sphere: c["sphere_branch_closed"]+=1
              if t==1 and not sphere: c["t1_sphere_branch_closed"]+=1
              if not (noncheap or sphere):
                  c["full_dichotomy_reject"]+=1; by_t[t]+=1
              else:
                  c["full_dichotomy_survive"]+=1

    expected={
      "current":110387,
      "plain_slot_reject":45401,
      "full_dichotomy_reject":45830,
      "full_dichotomy_survive":64557,
      "t1_sphere_branch_closed":1024,
    }
    bad={k:(v,c[k]) for k,v in expected.items() if c[k]!=v}
    print({"counts":dict(c),"dichotomy_rejections_by_t":dict(sorted(by_t.items())),
           "expected_mismatches":bad,"failures":len(bad),
           "trust":"abstract integer/arithmetic diagnostic only; no graph-realizability claim"})
    if bad: raise SystemExit(1)

if __name__=="__main__": main()
