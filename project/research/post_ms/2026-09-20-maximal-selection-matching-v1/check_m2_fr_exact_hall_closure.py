#!/usr/bin/env python3
"""Independent diagnostic for M2_FR_EXACT_HALL_CLOSURE.md.

This is an abstract necessary-condition replay, not a graph enumerator and not a
substitute for the analytic proof.  It deliberately uses only the coarse
historical first-strict baseline plus the new exact X-slack, physical U_o bill,
and rooted residual inequalities; it does not need pair-capacity to obtain the
zero residual count.
"""
import math
from collections import Counter


def phi(g):
    return g*(g-1) if g >= 3 else 0


def C0(p,u,l):
    H=((l+1)**2)//4
    return (l+3)*p+(l+2)*u-2*H-4


def main():
    st=Counter()
    closest={'>2':(-10**9,None),'=2':(-10**9,None)}

    for p in range(3,19):
      for u in range(1,19):
        b=2*p+u
        for l in range(0,b-3):
          a=b-l-1
          if a<4:
            continue
          cap=C0(p,u,l)
          if cap<0:
            continue
          for x in range(4,a):
            y=a-x
            if p-y < 1:
              continue
            for g in range(0,p):
              k=x-g
              if k<=0 or k+1>u:
                continue
              # Same deliberately weak coarse predecessor baseline.
              if phi(g)+k*(p+k-2)+(p-g+1)>cap:
                continue

              omega=u-k-1
              if omega<2:
                continue
              branch='>2' if omega>2 else '=2'
              st[branch+'_base'] += 1

              # Exact consequence of G[X]=empty and the physical X--U pattern.
              Lx=x*(p+k+omega-y)-k
              Ly=y*(p-g+1+omega)

              # Disjoint physical U-side lower bounds.
              Ecore=k*(p+k)-1
              ebuf=p-g+1
              Eout=omega*omega+(p-1)*omega-1
              if Lx+Ly+Ecore+ebuf+Eout > cap:
                continue
              st[branch+'_score'] += 1

              # Exact physical q ceiling after U_- and U_o independence and the
              # weakest preserved k-1 core-separation holes.
              qmax=k*omega-k+omega+1
              EUmax=cap-Lx-Ly
              rupper=(p-l)*(p+u)+qmax+EUmax

              # Conservative local Hamming floor.  One F head already pays p-1;
              # each other X head pays >=1; every Y head pays >=2 for p>=3.
              rlow=x+p-2+2*y
              margin=rupper-rlow
              if margin>closest[branch][0]:
                closest[branch]=(margin,(p,u,l,x,y,g,k,omega))
              if margin>=0:
                st[branch+'_resid'] += 1

    expected={
      '>2_base':182396,
      '>2_score':402,
      '>2_resid':0,
      '=2_base':21237,
      '=2_score':375,
      '=2_resid':0,
    }
    bad={k:(v,st[k]) for k,v in expected.items() if st[k]!=v}
    print({
      'counts':dict(st),
      'closest_residual_margin':closest,
      'mismatches':bad,
      'failures':len(bad),
      'trust':'abstract necessary-condition diagnostic only; analytic theorem is the proof',
    })


if __name__=='__main__':
    main()
