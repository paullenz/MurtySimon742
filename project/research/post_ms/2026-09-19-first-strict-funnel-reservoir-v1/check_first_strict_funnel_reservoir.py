#!/usr/bin/env python3
"""Independent reconstruction/audit of the interrupted first-strict funnel diagnostic.

This is an abstract integer diagnostic, NOT a D2C graph enumerator. It has two
modes evaluated in one pass:

* legacy: reconstructs the arithmetic implicit in the interrupted theorem note,
  including the reported counts;
* corrected: additionally enforces the physical requirement that the m distinct
  selected outside witnesses actually fit in U_o, i.e. m <= |U_o|=u-k-1,
  and refuses a negative physical q ceiling.

The corrected mode is the one future work should use.
"""
import math
from collections import Counter


def phi(g):
    return g*(g-1) if g >= 3 else 0


def C0(p,u,lam):
    H=((lam+1)**2)//4
    return (lam+3)*p+(lam+2)*u-2*H-4


def D_code(p,u,lam):
    return 5*p+5*u-3*lam-2


def R_code(S,p,u,lam):
    if S < 0:
        return -1
    D=D_code(p,u,lam)
    return (D+math.isqrt(D*D+12*S))//3


def ceildiv(a,b):
    return (a+b-1)//b


def ccap_ok(S,p,u,lam,g,x,y):
    R=R_code(S,p,u,lam)
    L=lam+1
    return R*(g*L+2*S) >= 2*x*y*L


def sigma_P(p,u,lam,x,y,g,k,m):
    cap=C0(p,u,lam)
    D=D_code(p,u,lam)
    P0=k*(p+k-2)+(p-g+1)+y*(p-g+1+m)
    lo=max(P0, y*max(0,3*y-D))
    if lo>cap:
        return None
    hi=cap
    ans=None
    while lo<=hi:
        mid=(lo+hi)//2
        if ccap_ok(mid,p,u,lam,g,x,y):
            ans=mid
            hi=mid-1
        else:
            lo=mid+1
    return ans


def row_status(p,u,lam,x,y,g):
    """Return legacy/corrected pair and final feasibility for one coarse row."""
    k=x-g
    N=x-1
    cap=C0(p,u,lam)
    g0=p-y
    RA=R_code(cap,p,u,lam)//2
    if RA<=0:
        return False,False,False,False
    uo=u-k-1
    sigcache={}
    legacy_pair=legacy_final=corrected_pair=corrected_final=False

    for F in range(N+1):
        Rn=N-F
        hfmin=ceildiv(F,RA) if F else 0
        hrmin=ceildiv(Rn,RA) if Rn else 0
        if hfmin+hrmin>p:
            continue
        for hF in range(hfmin, F+1 if F else 1):
            for hR in range(hrmin, Rn+1 if Rn else 1):
                if hF+hR>p:
                    continue
                s=max(1,hF)
                if s>p-hR or s>p-1:
                    continue
                for mF in range(hF, F+1 if F else 1):
                    m=hR+mF
                    if m<=0:
                        continue
                    sig=sigcache.get(m)
                    if m not in sigcache:
                        sig=sigma_P(p,u,lam,x,y,g,k,m)
                        sigcache[m]=sig
                    if sig is None:
                        continue
                    epsa=max(0,g0+1-F)
                    # weakest legitimate chi=1 choice in the theorem note
                    EW=max(0, N+k-1+mF-m*(x-p))
                    if sig+EW+epsa>cap:
                        continue
                    legacy_pair=True
                    physical=(m<=uo)
                    if physical:
                        corrected_pair=True

                    LY=y*(p-g+1+m)
                    EUmax=cap-max(phi(g),LY+epsa)
                    if EUmax<0:
                        continue
                    qmax=math.comb(u,2)-math.comb(k+1,2)-(k-1)
                    rlow=x+y*(s+ceildiv(F*(p-1-s),x))
                    rupper=(p-lam)*(p+u)+qmax+EUmax

                    # This deliberately reconstructs the interrupted count even
                    # when qmax<0; that is an algebraic replay, not a physical one.
                    if rupper>=rlow:
                        legacy_final=True

                    # A physical q=e(G[U]) must be nonnegative, and all selected
                    # witnesses must be actual distinct vertices of U_o.
                    if physical and qmax>=0 and rupper>=rlow:
                        corrected_final=True

                    if legacy_pair and legacy_final and corrected_pair and corrected_final:
                        return True,True,True,True
    return legacy_pair,legacy_final,corrected_pair,corrected_final


def main():
    st=Counter()
    for p in range(3,19):
        for u in range(1,19):
            b=2*p+u
            for lam in range(0,b-3):
                a=b-lam-1
                if a<4:
                    continue
                cap=C0(p,u,lam)
                if cap<0:
                    continue
                for x in range(3,a):
                    y=a-x
                    if p-y<1:  # principal g0=p-y>=1 slice
                        continue
                    for g in range(0,p):
                        k=x-g
                        if k<=0 or k+1>u:
                            continue
                        if phi(g)+k*(p+k-2)+(p-g+1)>cap:
                            continue
                        st['coarse']+=1
                        lp,lf,cp,cf=row_status(p,u,lam,x,y,g)
                        st['legacy_pair_survivors']+=lp
                        st['legacy_final_survivors']+=lf
                        st['corrected_pair_survivors']+=cp
                        st['corrected_final_survivors']+=cf
                        if lp and not cp:
                            st['pair_rows_removed_by_physical_Uo_capacity']+=1
                        if lf and not cf:
                            st['legacy_final_rows_removed_by_physical_correction']+=1

    st['legacy_pair_rejected']=st['coarse']-st['legacy_pair_survivors']
    st['legacy_residual_rejected']=st['legacy_pair_survivors']-st['legacy_final_survivors']
    st['corrected_pair_rejected']=st['coarse']-st['corrected_pair_survivors']
    st['corrected_residual_rejected']=st['corrected_pair_survivors']-st['corrected_final_survivors']

    legacy_expected={
        'coarse':248798,
        'legacy_pair_survivors':225152,
        'legacy_pair_rejected':23646,
        'legacy_final_survivors':188912,
        'legacy_residual_rejected':36240,
    }
    legacy_bad={k:(v,st[k]) for k,v in legacy_expected.items() if st[k]!=v}

    corrected_expected={
        'corrected_pair_survivors':213840,
        'corrected_pair_rejected':34958,
        'corrected_final_survivors':179735,
        'corrected_residual_rejected':34105,
    }
    corrected_bad={k:(v,st[k]) for k,v in corrected_expected.items() if st[k]!=v}

    print({
        'counts':dict(st),
        'legacy_mismatches':legacy_bad,
        'corrected_mismatches':corrected_bad,
        'failures':len(legacy_bad)+len(corrected_bad),
        'trust':('legacy counts reproduce the interrupted arithmetic only; corrected counts '
                 'add mandatory physical U_o witness capacity and q>=0; neither is a graph-realizability count'),
    })


if __name__=='__main__':
    main()
