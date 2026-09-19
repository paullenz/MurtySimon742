#!/usr/bin/env python3
"""Abstract diagnostic for ALL_R_PINCH_LOCAL_FEEDBACK.md.

NOT a D2C graph enumerator.  It reproduces the predecessor corrected
one-witness pinch counts and then applies only necessary inequalities from the
new hand package.
"""
import math
from collections import Counter

def phi(g):
    return g*(g-1) if g>=3 else 0

def C0(p,u,l):
    H=((l+1)**2)//4
    return (l+3)*p+(l+2)*u-2*H-4

def D_code(p,u,l):
    return 5*p+5*u-3*l-2

def R_code(S,p,u,l):
    D=D_code(p,u,l)
    return (D+math.isqrt(D*D+12*S))//3

def ccap_ok(S,p,u,l,g,x,y):
    R=R_code(S,p,u,l)
    L=l+1
    return R*(g*L+2*S)>=2*x*y*L

def sigma_old(p,u,l,x,y,g,k):
    """Predecessor exact-core one-witness threshold."""
    cap=C0(p,u,l)
    Ecore=k*(p+k-1)+(k-1)
    P0=Ecore+(p-g+1)+y*(p-g+2)
    lo=max(P0,y*max(0,3*y-D_code(p,u,l)))
    if lo>cap:
        return None
    hi=cap
    ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap_ok(mid,p,u,l,g,x,y):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    return ans

def sigma_strong(p,u,l,x,y,g,k):
    """New pair-local threshold using H_core>=k."""
    cap=C0(p,u,l)
    Ecore=k*(p+k)
    P0=Ecore+(p-g+1)+y*(p-g+2)
    lo=max(P0,y*max(0,3*y-D_code(p,u,l)))
    if lo>cap:
        return None
    hi=cap
    ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap_ok(mid,p,u,l,g,x,y):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    return ans

def main():
    st=Counter()
    d_choice=Counter()
    t_choice=Counter()

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

        for x in range(3,a):
         y=a-x
         if p-y<1:
            continue

         for g in range(0,p):
          k=x-g
          if k<=0 or k+1>u:
            continue

          # Historical broad baseline, retained only so the new checker can
          # reproduce the predecessor checkpoint exactly.
          if phi(g)+k*(p+k-2)+(p-g+1)>cap:
            continue
          st['coarse']+=1

          if u-k-1<1:
            continue

          RA=R_code(cap,p,u,l)//2
          if x>RA:
            continue

          # Reproduce predecessor corrected equality-pinch gate.
          sig0=sigma_old(p,u,l,x,y,g,k)
          if sig0 is None:
            continue
          epsa0_old=p-y+1
          epsz_old=p+k-2
          if sig0+epsz_old+epsa0_old>cap:
            continue

          LY=y*(p-g+2)
          EUmax_old=cap-max(phi(g),LY+epsa0_old)
          qmax_old=math.comb(u,2)-math.comb(k+1,2)-(k-1)
          if EUmax_old<0 or qmax_old<0:
            continue
          if (p-l)*(p+u)+qmax_old+EUmax_old<a:
            continue
          st['predecessor_final']+=1

          # New literal-pinch theorems.
          sig=sigma_strong(p,u,l,x,y,g,k)
          if sig is None:
            st['new_reject']+=1
            continue

          uo=u-k-1
          N=x-1
          epsa=p-y+k+1
          Amin=max(phi(g),LY+epsa)
          EUmax=cap-Amin
          if EUmax<0:
            st['new_reject']+=1
            continue

          Ecore=k*(p+k)
          epsb=p-g+1
          g1=max(0,p-y-1)
          Z0=(k+1)*(a-1)+y+1
          ZX0=(k+1)*N+1

          feasible=False
          chosen=None

          # d counts the z--(U_o\{z}) nonedges.
          for d in range(uo):
            J=uo-1-d
            epsz=p+k-1+d

            # Keep exact pair score local before using the total cap.
            if sig+epsz+epsa>cap:
                continue

            qmax=math.comb(u,2)-math.comb(k+1,2)-k-d
            if qmax<0:
                continue

            # Physical A--U rectangle and exact Z identity.
            Zmin=Z0+N*J
            if 2*qmax+EUmax < Zmin-u*(p-l):
                continue

            # Equality-pinch local rooted-slot requirement r>=a.
            if (p-l)*(p+u)+qmax+EUmax<a:
                continue

            # Eliminate the internal edge variable.  If t additional bar-C
            # witnesses exist, e(X)<=min(C(N,2),N t).  Hall exactness forces a
            # lower bound on the same e(X).
            for t in range(uo):
                adj_bar=max(0,t-d)
                Ebase=(Ecore+epsb+epsz+J*g1
                       +(p-g1)*adj_bar)
                if Ebase>EUmax:
                    continue

                emax=min(N*(N-1)//2,N*t)
                hall_rhs=(x*(p-y)+(ZX0+N*J)-cap+Ebase)
                if 2*emax < hall_rhs:
                    continue

                feasible=True
                chosen=(d,t)
                break

            if feasible:
                break

          if feasible:
            st['new_final']+=1
            d_choice[chosen[0]]+=1
            t_choice[chosen[1]]+=1
          else:
            st['new_reject']+=1

    expected={
        'coarse':248798,
        'predecessor_final':173347,
        'new_final':134077,
        'new_reject':39270,
    }
    bad={k:(expected[k],st[k]) for k in expected if st[k]!=expected[k]}
    print({
        'counts':dict(st),
        'expected':expected,
        'mismatches':bad,
        'failures':len(bad),
        'minimizing_d_distribution':dict(sorted(d_choice.items())),
        'minimizing_t_distribution':dict(sorted(t_choice.items())),
        'trust':('abstract necessary-condition diagnostic only; '
                 'not graph enumeration or realizability evidence'),
    })

if __name__=='__main__':
    main()
