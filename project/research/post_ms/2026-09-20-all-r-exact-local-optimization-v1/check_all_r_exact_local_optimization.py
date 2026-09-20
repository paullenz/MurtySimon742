#!/usr/bin/env python3
"""Necessary-condition diagnostic for ALL_R_EXACT_LOCAL_OPTIMIZATION.md.

Not graph enumeration and not realizability evidence.
"""
import math
from collections import Counter


def phi(g): return g*(g-1) if g >= 3 else 0

def C0(p,u,l):
    H=((l+1)**2)//4
    return (l+3)*p+(l+2)*u-2*H-4

def D_code(p,u,l): return 5*p+5*u-3*l-2

def R_code(S,p,u,l):
    D=D_code(p,u,l)
    return (D+math.isqrt(D*D+12*S))//3

def ccap_ok(S,p,u,l,g,x,y):
    R=R_code(S,p,u,l); L=l+1
    return R*(g*L+2*S) >= 2*x*y*L

def sigma_old(p,u,l,x,y,g,k):
    cap=C0(p,u,l)
    Ecore=k*(p+k-1)+(k-1)
    P0=Ecore+(p-g+1)+y*(p-g+2)
    lo=max(P0,y*max(0,3*y-D_code(p,u,l)))
    if lo>cap: return None
    hi=cap; ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap_ok(mid,p,u,l,g,x,y): ans=mid; hi=mid-1
        else: lo=mid+1
    return ans

def sigma_strong(p,u,l,x,y,g,k):
    cap=C0(p,u,l)
    Ecore=k*(p+k)
    P0=Ecore+(p-g+1)+y*(p-g+2)
    lo=max(P0,y*max(0,3*y-D_code(p,u,l)))
    if lo>cap: return None
    hi=cap; ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap_ok(mid,p,u,l,g,x,y): ans=mid; hi=mid-1
        else: lo=mid+1
    return ans

def load_price(e,m,x,p):
    return max(e-m*(x-p-2),0)

def live_feasible(p,u,l,x,y,g,k,sig,cap):
    if g < 1: return False, None
    uo=u-k-1; N=x-1; h=x-2; a=x+y
    Ecore=k*(p+k); epsb=p-g+1; LY=y*(p-g+2)
    Z0=(k+1)*(a-1)+y+1; ZX0=(k+1)*N+1

    for d in range(uo):
        if y>=2 and d*max(x,y) < g*y:
            continue
        J=uo-1-d
        epsz=p+k-1+d
        E0=Ecore+epsb+epsz+J*p
        B=x*(p-y)+(ZX0+N*J)-cap+E0

        for m in range(d+1):
            epsa=p+u-y-d+m-1
            if sig+epsz+epsa > cap:
                continue
            EUmax=cap-max(phi(g),LY+epsa)
            if EUmax < 0:
                continue
            qmax=(math.comb(u,2)-math.comb(k+1,2)-k-d
                  -math.comb(J,2))
            if qmax < 0:
                continue

            if m==0:
                evals=(0,)
            else:
                elo=m
                ehi=min(N*(N-1)//2,m*h)
                if elo>ehi:
                    continue
                evals=range(elo,ehi+1)

            for e in evals:
                P=load_price(e,m,x,p) if m else 0
                if E0+P > EUmax:
                    continue
                if e < B+m+P:
                    continue
                Zmin=Z0+N*J+m*(y+1)+e
                if 2*qmax+EUmax < Zmin-u*(p-l):
                    continue
                if (p-l)*(p+u)+qmax+EUmax < a:
                    continue
                return True,(d,m,e)
    return False,None

def main():
    st=Counter(); choice=Counter()
    for p in range(3,19):
      for u in range(1,19):
       b=2*p+u
       for l in range(0,b-3):
        a=b-l-1
        if a<4: continue
        cap=C0(p,u,l)
        if cap<0: continue
        for x in range(3,a):
         y=a-x
         if p-y<1: continue
         for g in range(0,p):
          k=x-g
          if k<=0 or k+1>u: continue
          if phi(g)+k*(p+k-2)+(p-g+1)>cap: continue
          st['coarse'] += 1
          if u-k-1<1: continue
          if x > R_code(cap,p,u,l)//2: continue

          sig0=sigma_old(p,u,l,x,y,g,k)
          if sig0 is None: continue
          if sig0+(p+k-2)+(p-y+1)>cap: continue
          LY=y*(p-g+2)
          EU0=cap-max(phi(g),LY+(p-y+1))
          q0=math.comb(u,2)-math.comb(k+1,2)-(k-1)
          if EU0<0 or q0<0: continue
          if (p-l)*(p+u)+q0+EU0<a: continue
          st['predecessor_final'] += 1

          sig=sigma_strong(p,u,l,x,y,g,k)
          if sig is None:
              st['new_reject'] += 1
              continue
          ok,info=live_feasible(p,u,l,x,y,g,k,sig,cap)
          if ok:
              st['new_final'] += 1
              choice[info] += 1
          else:
              st['new_reject'] += 1

    expected={
        'coarse':248798,
        'predecessor_final':173347,
        'new_final':78582,
        'new_reject':94765,
    }
    bad={k:(expected[k],st[k]) for k in expected if st[k]!=expected[k]}
    print({
        'counts':dict(st),
        'expected':expected,
        'mismatches':bad,
        'failures':len(bad),
        'trust':'abstract necessary-condition diagnostic only; not graph enumeration',
    })

if __name__=='__main__':
    main()
