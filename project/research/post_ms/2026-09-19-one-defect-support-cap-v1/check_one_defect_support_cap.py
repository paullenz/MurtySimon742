#!/usr/bin/env python3
"""Diagnostic replay for ONE_DEFECT_SUPPORT_CAP_RESIDUAL_PINCH.md.

Abstract integer parameter scan only. This is not a D2C graph enumerator and
makes no graph-realizability claim.
"""
import math, runpy
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
PREV=HERE.parent / "2026-09-19-one-defect-witness-intersection-v1" / "check_one_defect_witness_intersection.py"
W=runpy.run_path(str(PREV))

C0=W["C0"]; predecessor_floor=W["predecessor_floor"]
repaired_floor=W["repaired_floor"]; preceding_mg1_score=W["preceding_mg1_score"]
hmin_closed=W["hmin_closed"]; sigma_pair=W["sigma_pair"]
rows_for_state=W["rows_for_state"]; sphere_survives=W["sphere_survives"]
support_sizes=W["support_sizes"]; E1_slot_floor=W["E1_slot_floor"]
RN_range=W["RN_range"]


def support_cap(k,d):
    if k>1:
        assert d in (0,1)
        return (k+1)*d, 4+(k-1)*d
    assert 0<=d<=2
    return 2*d, 4


def refined_pair_lhs(p,g,k,M,d,D):
    c,J0=support_cap(k,d)
    return p*(g+1)+k+M+max(D-c,-J0)


def verify_min_formula():
    checks=0
    for k in range(1,10):
        ds=(0,1,2) if k==1 else (0,1)
        for d in ds:
            c,J0=support_cap(k,d)
            for D in range(-30,31):
                brute=min(max(0,D+2*Delta)-min(c+2*Delta,J0) for Delta in range(50))
                closed=max(D-c,-J0)
                assert brute==closed,(k,d,D,brute,closed)
                checks+=1
    return checks


def main():
    c=Counter(); by_t=Counter(); qefail=[]
    min_checks=verify_min_formula()

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

              old_e1=False; new_e1=False; e2=False
              old_rows=0; new_rows=0

              for A,M,D,H,Emin,nu,rupper in rows:
                  d=g-A
                  if support_sizes(p,g,k,1) and ((k>1 and d in (0,1)) or (k==1 and 0<=d<=2)):
                      old_lhs=p*(g+1)+k+M-(k+1)*d+D
                      r1=E1_slot_floor(x,y,g,k,A,Emin)
                      if old_lhs<=cap-sig and rupper>=r1:
                          old_e1=True; old_rows+=1
                          new_lhs=refined_pair_lhs(p,g,k,M,d,D)
                          if new_lhs<=cap-sig:
                              new_e1=True; new_rows+=1

                              # Pointwise exact rooted q/E_U lower/upper intersection.
                              qmax=math.comb(u,2)-math.comb(k+1,2)-k-M
                              EUmax=cap-Y0-max(0,D)
                              Zplus=k*a+y*(g+2)+g
                              R0=Zplus+k*N-u*(p-lam)-Ebase
                              qelb=Ebase+M+math.ceil(max(0,R0-(k+1)*M)/2)
                              qeub=qmax+EUmax
                              c["new_E1_rows_qe_checked"]+=1
                              if qelb>qeub:
                                  qefail.append((p,u,lam,x,y,g,k,A,M,D,qelb,qeub))

                  r2,_=RN_range(p,x,y,g,k,Emin,2)
                  if r2 is not None and rupper>=r2:e2=True

              if old_e1:
                  c["old_E1_states"]+=1
                  c["old_E1_rows"]+=old_rows
                  if t==1:
                      c["t1_old_E1_states"]+=1
                      c["t1_old_E1_rows"]+=old_rows
              if new_e1:
                  c["new_E1_states"]+=1
                  c["new_E1_rows"]+=new_rows
                  if t==1:
                      c["t1_new_E1_states"]+=1
                      c["t1_new_E1_rows"]+=new_rows
              if old_e1 and not new_e1:
                  c["E1_state_closures"]+=1
                  by_t[t]+=1

              old_union=old_e1 or e2 or sphere
              new_union=new_e1 or e2 or sphere
              if old_union:c["old_union"]+=1
              if new_union:c["new_union"]+=1
              if old_union and not new_union:c["new_union_rejections"]+=1
              if t==1 and old_union:c["t1_old_union"]+=1
              if t==1 and new_union:c["t1_new_union"]+=1

    expected={
      "old_E1_states":53435,
      "new_E1_states":48674,
      "E1_state_closures":4761,
      "old_E1_rows":1212749,
      "new_E1_rows":1093262,
      "new_E1_rows_qe_checked":1093262,
      "t1_old_E1_states":5164,
      "t1_new_E1_states":4471,
      "t1_old_E1_rows":128750,
      "t1_new_E1_rows":111046,
      "old_union":64457,
      "new_union":64457,
      "new_union_rejections":0,
      "t1_old_union":5404,
      "t1_new_union":5404,
    }
    bad={key:(want,c[key]) for key,want in expected.items() if c[key]!=want}
    assert not qefail, qefail[:5]
    assert by_t==Counter({1:693,2:674,3:644,4:596,5:541,6:442,7:365,8:290,9:195,10:138,11:82,12:56,13:27,14:12,15:6}),by_t

    print({
      "min_formula_checks":min_checks,
      "counts":dict(c),
      "E1_state_closures_by_t":dict(sorted(by_t.items())),
      "rooted_qe_failures":len(qefail),
      "expected_mismatches":bad,
      "failures":len(bad),
      "trust":"abstract integer/arithmetic diagnostic only; no graph-realizability claim",
    })
    if bad:raise SystemExit(1)

if __name__=="__main__":main()
