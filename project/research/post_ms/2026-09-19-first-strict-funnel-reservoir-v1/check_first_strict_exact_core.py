#!/usr/bin/env python3
"""Exact-core audit for the first-strict funnel resource cone.

Abstract integer diagnostic only; NOT a D2C graph enumerator.

This supersedes the physical-v1 survivor counts in
check_first_strict_funnel_reservoir.py by restoring an already-proved upstream
identity that the interrupted checkpoint accidentally weakened:

  E_core = k(p+k-1) + H_core,

and, in the weakest chi=1 unique-hole route,

  H_core >= k-1.

A W0--Uo missing edge is charged once at its core endpoint here and once at its
outside-witness endpoint in E_W; this is correct because it contributes one
unit of degree slack to each endpoint.
"""
import math
from collections import Counter


def phi(g): return g*(g-1) if g>=3 else 0

def C0(p,u,l):
    H=((l+1)**2)//4
    return (l+3)*p+(l+2)*u-2*H-4

def D(p,u,l): return 5*p+5*u-3*l-2

def Rcode(S,p,u,l):
    d=D(p,u,l)
    return (d+math.isqrt(d*d+12*S))//3

def ceildiv(a,b): return (a+b-1)//b

def ccap(S,p,u,l,g,x,y):
    R=Rcode(S,p,u,l); L=l+1
    return R*(g*L+2*S)>=2*x*y*L

def sigma_exact(p,u,l,x,y,g,k,m):
    cap=C0(p,u,l)
    Ecore=k*(p+k-1)+(k-1)  # exact core + weakest forced H_core
    P0=Ecore+(p-g+1)+y*(p-g+1+m)
    lo=max(P0,y*max(0,3*y-D(p,u,l)))
    if lo>cap: return None
    hi=cap; ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap(mid,p,u,l,g,x,y): ans=mid; hi=mid-1
        else: lo=mid+1
    return ans

def row_status(p,u,l,x,y,g):
    k=x-g; N=x-1; cap=C0(p,u,l); g0=p-y
    RA=Rcode(cap,p,u,l)//2
    if RA<=0: return False,False
    uo=u-k-1
    cache={}; pair=final=False
    for F in range(N+1):
      Rn=N-F
      hfmin=ceildiv(F,RA) if F else 0
      hrmin=ceildiv(Rn,RA) if Rn else 0
      if hfmin+hrmin>p: continue
      for hF in range(hfmin,F+1 if F else 1):
       for hR in range(hrmin,Rn+1 if Rn else 1):
        if hF+hR>p: continue
        s=max(1,hF)
        if s>p-hR or s>p-1: continue
        for mF in range(hF,F+1 if F else 1):
         m=hR+mF
         if m<=0 or m>uo: continue
         if m not in cache: cache[m]=sigma_exact(p,u,l,x,y,g,k,m)
         sig=cache[m]
         if sig is None: continue
         epsa=max(0,g0+1-F)
         EW=max(0,N+(k-1)+mF-m*(x-p))
         if sig+EW+epsa>cap: continue
         pair=True
         LY=y*(p-g+1+m)
         EUmax=cap-max(phi(g),LY+epsa)
         if EUmax<0: continue
         qmax=math.comb(u,2)-math.comb(k+1,2)-(k-1)
         if qmax<0: continue
         rlow=x+y*(s+ceildiv(F*(p-1-s),x))
         rupper=(p-l)*(p+u)+qmax+EUmax
         if rupper>=rlow: return True,True
    return pair,final

def main():
    st=Counter()
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
          # Keep the historical broad baseline for direct comparison.
          if phi(g)+k*(p+k-2)+(p-g+1)>cap: continue
          st['coarse']+=1
          pa,fi=row_status(p,u,l,x,y,g)
          st['exact_core_pair']+=pa
          st['exact_core_final']+=fi
    st['exact_core_pair_rejected']=st['coarse']-st['exact_core_pair']
    st['exact_core_residual_rejected']=st['exact_core_pair']-st['exact_core_final']
    exp={'coarse':248798,'exact_core_pair':208684,'exact_core_final':174769,
         'exact_core_pair_rejected':40114,'exact_core_residual_rejected':33915}
    bad={k:(v,st[k]) for k,v in exp.items() if st[k]!=v}
    print({'counts':dict(st),'mismatches':bad,'failures':len(bad),
           'trust':('abstract exact-core diagnostic only; no D2C graph-realizability claim; '
                    'supersedes 179735 physical-v1 final survivors')})
if __name__=='__main__': main()
