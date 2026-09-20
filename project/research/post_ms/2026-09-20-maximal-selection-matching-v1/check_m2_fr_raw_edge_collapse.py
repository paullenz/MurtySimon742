#!/usr/bin/env python3
"""Diagnostic for the maximal-m=2, p>=3, x>=4, omega>2 F/R raw-edge collapse.

This is an abstract necessary-condition scan, NOT a D2C graph enumerator or a
realizability proof. It supplements check_m2_fr_reservoir.py with the physical
U_o-independence / outside-slack bill from M2_FR_RAW_EDGE_COLLAPSE.md.
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
    st=Counter(); examples=[]
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
          if phi(g)+k*(p+k-2)+(p-g+1)>cap: continue
          omega=u-k-1
          if omega<=2: continue
          st['omega_gt2_base']+=1
          sig=sigma_phys(p,u,l,x,y,g,k,omega)
          if sig is None: continue
          st['omega_gt2_pair']+=1

          # Full physical outside reservoir bill:
          # z_R pays >= p+omega-2 and each of omega-1 F-star leaves pays
          # >= p+omega-1 after U_o-independence and A-anticompleteness.
          Eout=omega*omega+(p-1)*omega-1
          if sig+Eout>cap: continue
          st['omega_gt2_score']+=1

          # Conservative rooted residual use of the full U_o-independent q loss.
          qmax=(math.comb(u,2)-math.comb(k+1,2)
                -math.comb(omega,2)-(k-1))
          if qmax<0: continue
          LY=y*(p-g+1+omega)
          EUmax=cap-max(phi(g),LY)
          # F=1 in omega>2. This keeps the audited local Hamming slot floor;
          # the stronger theorem e(X)=0 is deliberately NOT converted into an
          # extra scalar inequality here.
          rlow=x+y*(1+ceildiv(p-2,x))
          rupper=(p-l)*(p+u)+qmax+EUmax
          if rupper>=rlow:
              st['omega_gt2_residual']+=1
              if len(examples)<8:
                  examples.append((p,u,l,x,y,g,k,omega))

    expected={
      'omega_gt2_base':182396,
      'omega_gt2_pair':171981,
      'omega_gt2_score':103860,
      'omega_gt2_residual':73663,
    }
    bad={k:(v,st[k]) for k,v in expected.items() if st[k]!=v}
    print({'counts':dict(st),'mismatches':bad,'failures':len(bad),
           'example_survivors':examples,
           'trust':'abstract necessary-condition diagnostic only; not graph counts'})

if __name__=='__main__': main()
