#!/usr/bin/env python3
"""Diagnostic arithmetic for the m=g+1 minimal outside-reservoir layer.

Not a D2C graph enumerator.  The hand statements are in
MINIMAL_OUTSIDE_RESERVOIR_CORE_COLLAPSE.md.
"""
from collections import Counter


def phi(g):
    return g*(g-1) if g >= 3 else 0


def C0(p,u,lam):
    H=((lam+1)**2)//4
    return (lam+3)*p+(lam+2)*u-2*H-4


def predecessor_floor(p,x,y,g):
    k=x-g; t=p-g
    return k*(p+k-1)+t+max(phi(g),y*(t+1))


def repaired_floor(p,u,lam,x,y,g):
    k=x-g; t=p-g
    Ecore=k*(p+k)
    Eout=t+g*(t-k+1) if k<=t else 0
    LY=y*(p+2)
    S=Ecore+t+Eout+max(phi(g),LY)
    return S


def min_mg1_score(p,u,lam,x,y,g):
    k=x-g; t=p-g; a=x+y; T0=a-p
    uo=u-k-1
    N=uo-1
    assert N>=g
    s1=max(0,t-k+1)
    Ebase=k*(p+k)+2*t+k+g*s1
    LY=y*(p+2)
    Lcore=max(0,k*(k-T0))
    best=None
    arg=None
    for Astar in range(g+1):
        for Mstar in range(N+1):
            dstar=N-Mstar
            ZX=k*(x-1)+x+Astar+k*dstar
            eXmax=g*(g-1)//2+k*Astar
            LX=max(0,x*(x-T0)+ZX-2*eXmax)
            S=Ebase+Astar+Mstar+max(phi(g),LY,Lcore,LX)
            if best is None or S<best:
                best=S; arg=(Astar,Mstar,LX)
    return best,arg


def main():
    st=Counter()
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
                        st['predecessor_repaired_survivors']+=1
                        if t==1: st['t1_predecessor_repaired_survivors']+=1
                        best,_=min_mg1_score(p,u,lam,x,y,g)
                        if best>cap:
                            st['mg1_rejected']+=1
                            if t==1: st['t1_mg1_rejected']+=1
                        else:
                            st['mg1_survivors']+=1
                            if t==1: st['t1_mg1_survivors']+=1
    expected={
        'predecessor_repaired_survivors':133835,
        'mg1_rejected':10250,
        'mg1_survivors':123585,
        't1_predecessor_repaired_survivors':5815,
        't1_mg1_rejected':295,
        't1_mg1_survivors':5520,
    }
    bad={k:(expected[k],st[k]) for k in expected if expected[k]!=st[k]}
    print({'counts':dict(st),'mismatches':bad,'failures':len(bad),
           'trust':'abstract integer diagnostic only; no realizability claim'})


if __name__=='__main__':
    main()
