#!/usr/bin/env python3
"""Diagnostic for the corrected maximal-m=2, p>=3, x>=4 F/R normal form.

This is an abstract necessary-condition scan, NOT a D2C graph enumerator and not
a realizability proof.  It starts from the historical broad first-strict box and
then imposes only formulas documented in MAXIMAL_SELECTION_MATCHING_AND_M1_CLOSURE.md,
M2_BULK_BLOCK_SCOPE_CORRECTION.md, and M2_FR_RESERVOIR.md.
"""
import math
from collections import Counter


def phi(g): return g*(g-1) if g >= 3 else 0

def C0(p,u,l):
    H=((l+1)**2)//4
    return (l+3)*p+(l+2)*u-2*H-4

def D(p,u,l): return 5*p+5*u-3*l-2

def Rcode(S,p,u,l):
    d=D(p,u,l)
    return (d+math.isqrt(d*d+12*S))//3

def ceildiv(a,b): return (a+b-1)//b

def ccap_ok(S,p,u,l,g,x,y):
    R=Rcode(S,p,u,l); L=l+1
    return R*(g*L+2*S) >= 2*x*y*L

def sigma_phys(p,u,l,x,y,g,k,omega):
    """Exact pair-local threshold with physical Y-reservoir price."""
    cap=C0(p,u,l)
    Ecore=k*(p+k-1)+(k-1)
    P0=Ecore+(p-g+1)+y*(p-g+1+omega)
    lo=max(P0, y*max(0,3*y-D(p,u,l)))
    if lo>cap: return None
    hi=cap; ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap_ok(mid,p,u,l,g,x,y): ans=mid; hi=mid-1
        else: lo=mid+1
    return ans


def main():
    st=Counter()
    examples=[]
    for p in range(3,19):
      for u in range(1,19):
       b=2*p+u
       for l in range(0,b-3):
        a=b-l-1
        if a<4: continue
        cap=C0(p,u,l)
        if cap<0: continue
        for x in range(4,a):
         y=a-x
         if p-y<1: continue
         for g in range(0,p):
          k=x-g
          if k<=0 or k+1>u: continue
          # Historical coarse first-strict baseline, retained for comparability.
          if phi(g)+k*(p+k-2)+(p-g+1)>cap: continue
          st['coarse_x4']+=1

          omega=u-k-1
          if omega<2: continue
          key='omega2' if omega==2 else 'omega_gt2'
          st[key+'_base']+=1

          sig=sigma_phys(p,u,l,x,y,g,k,omega)
          if sig is None: continue
          st[key+'_pair']+=1

          N=x-1
          # Corrected F/R normal form.  When omega>2 the F component has
          # multiple physical witnesses and hence exactly one F head.
          Fvals=range(1,N) if omega==2 else (1,)
          good_score=good_res=False
          for F in Fvals:
            eps_a0=max(0,p-y+1-F)
            E_ZF=(omega-1)*max(0,p-x+omega) if omega>2 else 0
            if sig+eps_a0+E_ZF>cap: continue
            good_score=True

            LY=y*(p-g+1+omega)
            EUmax=cap-max(phi(g),LY+eps_a0)
            if EUmax<0: continue

            qmax=math.comb(u,2)-math.comb(k+1,2)-(k-1)
            if omega>2:
                qmax-=math.comb(omega-1,2)
            if qmax<0: continue

            rlow=x+y*(1+ceildiv(F*(p-2),x))
            rupper=(p-l)*(p+u)+qmax+EUmax
            if rupper>=rlow:
                good_res=True
                if len(examples)<8:
                    examples.append((p,u,l,x,y,g,k,omega,F))
          st[key+'_score']+=int(good_score)
          st[key+'_residual']+=int(good_res)

    expected={
      'coarse_x4':241502,
      'omega2_base':21237,'omega2_pair':16203,
      'omega2_score':16187,'omega2_residual':13454,
      'omega_gt2_base':182396,'omega_gt2_pair':171981,
      'omega_gt2_score':151736,'omega_gt2_residual':110759,
    }
    bad={k:(v,st[k]) for k,v in expected.items() if st[k]!=v}
    print({'counts':dict(st),'mismatches':bad,'failures':len(bad),
           'example_survivors':examples,
           'trust':'abstract necessary-condition diagnostic only; not graph counts'})

if __name__=='__main__': main()
