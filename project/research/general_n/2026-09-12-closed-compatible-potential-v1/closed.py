#!/usr/bin/env python3
"""Exact compatible-potential maxima from at most 59 candidates per sender class."""

def potential(h,k,j,rho,H,q,p):
    e=int(H>h)
    return (H*(h+max(0,4*h-max(h,q+p)))+H-2*e*H
            +(2*min(p,j-e) if rho>=h else 0)
            -(4*q if q>k else 0)+(4*p if rho+q>=k else 0))

def one_class(a,b,h,k,j,rho,hi,lo,e):
    assert a>=2 and b>=a and h>=2 and k>=0 and j>=0 and 1<=rho<=a
    assert hi>=0 and lo>=0 and hi+lo<=a and e in (0,1)
    C=min(a-rho,hi);left=0 if e==0 else h+1;right=min(C,h) if e==0 else C
    if left>right or e>j:return dict(value=None,witness=None,pieces=0,candidates=0)
    R=rho+b-a-1;B=b-1;J=j-e;D=k-rho
    best=None;witness=None;pieces=0;tested=0
    def accept(H,q,p,value):
        nonlocal best,witness,tested
        tested+=1
        assert left<=H<=right and H<=q and q-H<=lo and q+rho<=a and q+p<b and 0<=p<=R
        assert value==potential(h,k,j,rho,H,q,p)
        point=(H,q,p)
        if best is None or value>best or value==best and point<witness:best=value;witness=point
    # q=H. Each p candidate is c+dH; split P=min(R,B-H).
    branches=sorted({(0,0),(R,0),(J,0),(B,-1),(h,-1),(4*h,-1)})
    for c,d in branches:
        L,U=left,right
        if d==0:
            if c<0 or c>R:continue
            U=min(U,B-c)
        else:
            if c>B:continue
            L=max(L,c-R);U=min(U,c)
        if L>U:continue
        cuts={L,U+1}
        boundaries=[k+1,D]
        if d==0:boundaries.extend([h-c+1,4*h-c])
        else:boundaries.append(c-J)
        cuts.update(x for x in boundaries if L<x<=U)
        cuts=sorted(cuts)
        for l,stop in zip(cuts,cuts[1:]):
            u=stop-1;pieces+=1;p=c+d*l
            if l+p<=h:A,F0=0,3*h
            elif l+p>=4*h:A,F0=0,0
            else:A,F0=-(1+d),4*h-c
            coef=h+F0+1-2*e-4*int(l>k);constant=0
            if rho>=h:
                if p<=J:coef+=2*d;constant+=2*c
                else:constant+=2*J
            if l>=D:coef+=4*d;constant+=4*c
            assert A in (-1,0)
            if A==0:points={u if coef>0 else l}
            else:points={max(l,min(u,x)) for x in [coef//2,coef//2+1]}
            for H in sorted(points):accept(H,H,c+d*H,A*H*H+coef*H+constant)
    # q=D=k-rho. Within a sender class the potential increases with H.
    L=max(left,D-lo);U=min(right,D);P=min(R,B-D)
    if 0<=D<=a-rho and L<=U and P>=0:
        H=U
        points={0,P}|{p for p in [h-D,4*h-D,J] if 0<=p<=P}
        for p in sorted(points):accept(H,D,p,potential(h,k,j,rho,H,D,p))
    assert best is not None and pieces<=27 and tested<=59
    return dict(value=best,witness=witness,pieces=pieces,candidates=tested)

def maxima(a,b,h,k,j,rho,hi,lo):
    return tuple(one_class(a,b,h,k,j,rho,hi,lo,e) for e in (0,1))
