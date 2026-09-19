#!/usr/bin/env python3
"""Arithmetic audit for ZERO_BUFFER_CORE_OUTSIDE_SEPARATION_AND_LAMBDA7_FRONTIER.md.

This is diagnostic support only. It does not prove the raw D2C criticality
or Boolean-support premises used by the hand theorem.
"""

def Hlam(lam):
    return ((lam + 1) ** 2) // 4

def c0(p,k,rho,lam):
    u=k+rho
    return (lam+3)*p + (lam+2)*u - 2*Hlam(lam) - 4

def strong_floor(p,k,rho,lam):
    s=rho-p
    u=k+rho
    uo=rho-1
    x=p+k
    y=p+rho-lam-1
    M=max(x,uo)
    LY=rho*y
    EU=k*(p+u-2)+uo*(rho-2)+M
    R=s-2
    LXraw=x*(lam+1-rho)+k*(x-1)+M-2*k*R
    LX=max(0,LXraw)
    return LY+EU+LX, LY, EU, LX, LXraw

def scan(lam, limit=100):
    out=[]
    for p in range(4,limit+1):
        for rho in range(p+2,limit+1):
            y=p+rho-lam-1
            if y<=0: continue
            for k in range(1,limit+1):
                sf,*rest=strong_floor(p,k,rho,lam)
                if sf<=c0(p,k,rho,lam):
                    out.append((p,rho,k,sf,c0(p,k,rho,lam),*rest))
    return out

def main():
    assert scan(6)==[]
    s7=scan(7)
    assert [(r[0],r[1],r[2]) for r in s7]==[(4,6,1)]
    p,rho,k=4,6,1
    assert c0(p,k,rho,7)==67
    # exact state: S=55+2J, J>=5
    possibilities=[(J,55+2*J,J-9) for J in range(5,20) if 55+2*J<=67]
    assert possibilities==[(5,65,-4),(6,67,-3)]
    print({"lambda6_survivors":0,"lambda7_frontier":[(4,6,1)],"lambda7_exact_J_delta":[(5,-4),(6,-3)],"failures":0})

if __name__ == "__main__":
    main()
