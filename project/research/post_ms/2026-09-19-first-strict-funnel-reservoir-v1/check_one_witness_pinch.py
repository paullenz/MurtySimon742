#!/usr/bin/env python3
"""Diagnostic for the audited m=1 all-R equality pinch.

This is an abstract parameter diagnostic, not a D2C graph enumerator. It keeps
only the unique one-witness geometry that can avoid the +y rooted-slot
surcharge: s=1, I=I0, all X one code at Hamming distance one from d.
"""
import math
from collections import Counter


def phi(g):
    return g*(g-1) if g>=3 else 0


def C0(p,u,l):
    H=((l+1)**2)//4
    return (l+3)*p+(l+2)*u-2*H-4


def D_code(p,u,l):
    return 5*p+5*u-3*l-2


def R_code(S,p,u,l):
    D=D_code(p,u,l)
    return (D+math.isqrt(D*D+12*S))//3


def ccap_ok(S,p,u,l,g,x,y):
    R=R_code(S,p,u,l)
    L=l+1
    return R*(g*L+2*S)>=2*x*y*L


def sigma_one_witness(p,u,l,x,y,g,k):
    cap=C0(p,u,l)
    # m=1 in the audited first-strict pair floor.
    P0=k*(p+k-2)+(p-g+1)+y*(p-g+2)
    lo=max(P0,y*max(0,3*y-D_code(p,u,l)))
    if lo>cap:
        return None
    hi=cap
    ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap_ok(mid,p,u,l,g,x,y):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    return ans


def main():
    st=Counter()
    for p in range(3,19):
        for u in range(1,19):
            b=2*p+u
            for l in range(0,b-3):
                a=b-l-1
                if a<4:
                    continue
                cap=C0(p,u,l)
                if cap<0:
                    continue
                for x in range(3,a):
                    y=a-x
                    if p-y<1:
                        continue
                    for g in range(0,p):
                        k=x-g
                        if k<=0 or k+1>u:
                            continue
                        if phi(g)+k*(p+k-2)+(p-g+1)>cap:
                            continue
                        st['coarse']+=1

                        # One physical outside witness must actually fit in U_o.
                        if u-k-1<1:
                            continue

                        # In the equality pinch a0 is in the same code class as
                        # all x-1 buffer heads, so the FULL class has size x.
                        R_A=R_code(cap,p,u,l)//2
                        if x>R_A:
                            continue

                        sig=sigma_one_witness(p,u,l,x,y,g,k)
                        if sig is None:
                            continue

                        # all-R m=1: F=0, m_F=0, weakest chi=1.
                        eps_a0=p-y+1
                        E_W=p+k-2
                        if sig+E_W+eps_a0>cap:
                            continue
                        st['pinch_pair']+=1

                        L_Y=y*(p-g+2)
                        E_U_max=cap-max(phi(g),L_Y+eps_a0)
                        if E_U_max<0:
                            continue
                        q_max=math.comb(u,2)-math.comb(k+1,2)-(k-1)
                        if q_max<0:
                            continue

                        r_upper=(p-l)*(p+u)+q_max+E_U_max
                        # Equality pinch has only the baseline r>=a.
                        if r_upper>=a:
                            st['pinch_final']+=1

    expected={'coarse':248798,'pinch_pair':212324,'pinch_final':178572}
    bad={k:(expected[k],st[k]) for k in expected if expected[k]!=st[k]}
    print({'counts':dict(st),'mismatches':bad,'failures':len(bad),
           'trust':('abstract diagnostic of the audited one-witness equality pinch only; '
                    'no graph-realizability claim')})


if __name__=='__main__':
    main()
