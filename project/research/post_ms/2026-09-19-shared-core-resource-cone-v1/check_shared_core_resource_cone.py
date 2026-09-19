#!/usr/bin/env python3
"""Arithmetic audit for SHARED_CORE_RESOURCE_CONE.md.

This checker verifies exact algebraic identities and integer minimizations inside
the conditional t=1,E=2,k>=3 shared-core branch. It is NOT a D2C graph
enumerator and makes no graph-realizability claim.
"""
import math


def C0(p,u,lam):
    H=((lam+1)**2)//4
    return (lam+3)*p+(lam+2)*u-2*H-4


def data(p,k,N,y):
    u=N+k+2
    lam=N+p+2-y
    g=p-1
    x=p+k-1
    a=x+y
    T0=a-p
    Q=x*(x-T0)+k*(x-1)+x-g*(g-1)+k*N
    D0=Q-(2*k-1)*g
    Emax=math.comb(g,2)+k*g
    R0=D0+2*Emax
    P0=k*(p+k)+1+y*(p+2)
    B0=C0(p,u,lam)-P0-p*p
    eps=lam&1
    B02=(N*N+2*N*k+2*N*p+6*N-eps-2*k*k-2*k*y+8*k
         -p*p-2*p*y+8*p-y*y-2*y-2)
    Aroot=(2*N*k+2*N*y+N-eps+2*k*p+2*k+p*p+2*p-y*y-2*y-8)
    return u,lam,R0,B0,B02,Aroot,Emax


def W(R0,k,M,e):
    return M+e+max(0,R0-k*M-2*e)


def wstar_closed(R0,k,N):
    if R0<=0:
        return 0
    if R0<=k*N:
        return (R0+k-1)//k
    if R0<=k*N+2*k:
        return N+(R0-k*N+1)//2
    return N+R0-k*N-k


def quartic(a):
    return 3*a**4+12*a**3+8*a**2-8*a-16


def alpha0_bisect():
    lo,hi=1.0,1.1
    for _ in range(100):
        mid=(lo+hi)/2
        if quartic(mid)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def main():
    # Fixed target counts make the independent arithmetic coverage stable as
    # surrounding diagnostics evolve.
    coord_target=13176
    root_target=45300
    w_target=28350
    coord_checks=root_checks=w_checks=0

    done=False
    for p in range(3,20):
        if done: break
        for k in range(3,11):
            if done: break
            for N in range(p-1,p+15):
                if done: break
                for y in range(1,min(N+p+2,20)):
                    u,lam,R0,B0,B02,Aroot,Emax=data(p,k,N,y)
                    if lam<0:
                        continue
                    assert 2*B0==B02,(p,k,N,y,2*B0,B02)
                    coord_checks+=1
                    if coord_checks>=coord_target:
                        done=True
                        break

    done=False
    for p in range(3,20):
        if done: break
        for k in range(3,11):
            if done: break
            for N in range(p-1,p+15):
                if done: break
                for y in range(1,min(N+p+2,20)):
                    u,lam,R0,B0,B02,Aroot,Emax=data(p,k,N,y)
                    if lam<0:
                        continue
                    cap=C0(p,u,lam)
                    Y0=y*(p+2)
                    base=(p-lam)*(p+u)
                    for M in (0,N//2,N):
                        if done: break
                        for e in (0,k//2,k):
                            LX=max(0,R0-k*M-2*e)
                            qmax=math.comb(u,2)-math.comb(k+1,2)-k-M
                            EUmax=cap-Y0-LX
                            rupper=base+qmax+EUmax
                            rlower=(p+k-1+y)+y+2+e+(1 if e>0 else 0)
                            rhs=Aroot-2*(W(R0,k,M,e)+(1 if e>0 else 0))
                            assert (rupper>=rlower)==(rhs>=0),(
                                p,k,N,y,M,e,rupper,rlower,rhs)
                            root_checks+=1
                            if root_checks>=root_target:
                                done=True
                                break

    done=False
    for k in range(3,15):
        if done: break
        for N in range(0,20):
            if done: break
            for R0 in range(-25,k*N+2*k+55):
                brute=min(W(R0,k,M,e) for M in range(N+1) for e in range(k+1))
                closed=wstar_closed(R0,k,N)
                assert brute==closed,(k,N,R0,brute,closed)
                w_checks+=1
                if w_checks>=w_target:
                    done=True
                    break

    assert coord_checks==coord_target
    assert root_checks==root_target
    assert w_checks==w_target

    # Deep-arm equality triangle ceiling.
    for k in range(3,12):
        for N in range(0,30):
            u=N+k+2
            q1=math.comb(u,2)-math.comb(k+1,2)-k-N
            q2=(N*N+2*N*k+N+2)//2
            assert q1==q2,(N,k,q1,q2)

    # Fixed/sublinear-k asymptotic pinch.
    a0=alpha0_bisect()
    assert abs(a0-1.017515183827867)<1e-12,a0
    beta0=a0+1-math.sqrt(a0*a0+2*a0)
    lam0=a0+1-beta0

    # Finite weak pair/root diagnostic near the predicted pinch for k=3.
    finite=[]
    for p in (100,200,500,1000):
        k=3
        best=None
        for N in range(p-5,int(1.08*p)+8):
            for y in range(1,int(.36*p)+8):
                u,lam,R0,B0,B02,Aroot,Emax=data(p,k,N,y)
                if lam<0:
                    continue
                ws=wstar_closed(R0,k,N)
                if ws<=B0 and 2*ws<=Aroot:
                    cand=(N,y)
                    if best is None or cand<best:
                        best=cand
        assert best is not None,p
        finite.append((p,best[0],best[0]/p,best[1]))

    print({
        "coordinate_parity_checks":coord_checks,
        "root_same_currency_checks":root_checks,
        "W_star_bruteforce_checks":w_checks,
        "alpha0":a0,
        "beta0":beta0,
        "lambda_ratio_at_pinch":lam0,
        "finite_k3_weak_pair_root_minima":finite,
        "trust":"exact arithmetic audit of conditional shared-core inequalities only; no D2C graph-realizability claim",
    })


if __name__=="__main__":
    main()
