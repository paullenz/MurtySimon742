#!/usr/bin/env python3
"""Diagnostic for CROSS_EDGE_RESERVOIR_SHARPENING.md.

Necessary abstract parameter test only; not graph enumeration.
"""
import math
from collections import Counter


def phi(g): return g*(g-1) if g>=3 else 0

def C0(p,u,l):
    H=((l+1)**2)//4
    return (l+3)*p+(l+2)*u-2*H-4

def D_code(p,u,l): return 5*p+5*u-3*l-2

def R_code(S,p,u,l):
    D=D_code(p,u,l)
    return (D+math.isqrt(D*D+12*S))//3

def ccap_ok(S,p,u,l,g,x,y):
    R=R_code(S,p,u,l); L=l+1
    return R*(g*L+2*S)>=2*x*y*L

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

def pint(e,m,x,p): return max(e-m*(x-p-2),0)

def feasible(p,u,l,x,y,g,k,sig,cap):
    if g<1: return False,None
    uo=u-k-1; N=x-1; h=x-2; a=x+y
    Ecore=k*(p+k); epsb=p-g+1; LY=y*(p-g+2)
    Z0=(k+1)*(a-1)+y+1; ZX0=(k+1)*N+1
    Rcross=g*y if y>=2 else 0
    M=max(x,y); F=max(0,x-p+1)
    smin=(Rcross+M-1)//M if Rcross else 0

    for d in range(uo):
        J=uo-1-d
        epsz=p+k-1+d
        E0=Ecore+epsb+epsz+J*p
        B=x*(p-y)+(ZX0+N*J)-cap+E0

        for m in range(d+1):
            evals=(0,) if m==0 else range(m,min(N*(N-1)//2,m*h)+1)
            for s in range(smin,d-m+1):
                if Rcross>s*M: continue
                Pcross=max(Rcross-s*F,0)
                epsa=p+u-y-d+m+s-1
                if sig+epsz+epsa>cap: continue
                EUmax=cap-max(phi(g),LY+epsa)
                if EUmax<0: continue
                qmax=(math.comb(u,2)-math.comb(k+1,2)-k-d
                      -math.comb(J,2))
                if qmax<0: continue

                for e in evals:
                    P=pint(e,m,x,p) if m else 0
                    if E0+P+Pcross>EUmax: continue
                    if e < B+m+P+Pcross: continue
                    Zmin=Z0+N*J+m*(y+1)+e+Rcross
                    if 2*qmax+EUmax < Zmin-u*(p-l): continue
                    if (p-l)*(p+u)+qmax+EUmax<a: continue
                    return True,(d,m,s,e)
    return False,None

def main():
    st=Counter(); shape=Counter()
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
          st['coarse']+=1
          if u-k-1<1: continue
          if x>R_code(cap,p,u,l)//2: continue
          sig0=sigma_old(p,u,l,x,y,g,k)
          if sig0 is None or sig0+(p+k-2)+(p-y+1)>cap: continue
          LY=y*(p-g+2)
          EU0=cap-max(phi(g),LY+(p-y+1))
          q0=math.comb(u,2)-math.comb(k+1,2)-(k-1)
          if EU0<0 or q0<0: continue
          if (p-l)*(p+u)+q0+EU0<a: continue
          st['predecessor_final']+=1

          sig=sigma_strong(p,u,l,x,y,g,k)
          if sig is None:
              st['new_reject']+=1
              continue
          ok,info=feasible(p,u,l,x,y,g,k,sig,cap)
          if ok:
              st['new_final']+=1
              d,m,s,e=info
              shape[(e==0,y==1)]+=1
          else:
              st['new_reject']+=1

    expected={
        'coarse':248798,
        'predecessor_final':173347,
        'new_final':71996,
        'new_reject':101351,
    }
    bad={k:(expected[k],st[k]) for k in expected if st[k]!=expected[k]}
    print({
        'counts':dict(st),
        'expected':expected,
        'mismatches':bad,
        'failures':len(bad),
        'first_feasible_shape':{str(k):v for k,v in sorted(shape.items())},
        'trust':'abstract necessary-condition diagnostic only; not graph enumeration',
    })

if __name__=='__main__':
    main()
