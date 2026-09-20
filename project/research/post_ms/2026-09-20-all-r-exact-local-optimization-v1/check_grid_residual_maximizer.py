#!/usr/bin/env python3
"""Exhaustive integer check of GRID_RESIDUAL_MAXIMIZER.md.

This checks only the discrete maximizer-location algebra, not graph realizability.
"""
import math


def qpart(T,d):
    return -d-math.comb(T-d,2)


def rval(T,d,A,phi):
    return qpart(T,d)-max(phi,A-d)


def candidates(T,lo,A,phi):
    th=A-phi
    raw={math.floor(th),math.floor(th)+1,T-2,T-1,lo,T}
    return sorted(d for d in raw if lo<=d<=T)


def main():
    bad=[]
    tested=0
    for T in range(0,60):
      for lo in range(0,T+1):
       for A in range(-10,100):
        for ph in range(0,50):
            tested+=1
            true=max(rval(T,d,A,ph) for d in range(lo,T+1))
            cand=max(rval(T,d,A,ph) for d in candidates(T,lo,A,ph))
            if cand!=true:
                bad.append((T,lo,A,ph,true,cand,candidates(T,lo,A,ph)))
                print({'tested':tested,'failures':len(bad),'first':bad[0]})
                return
    print({'tested':tested,'failures':0,
           'trust':'integer algebra check only; not a D2C graph check'})

if __name__=='__main__':
    main()
