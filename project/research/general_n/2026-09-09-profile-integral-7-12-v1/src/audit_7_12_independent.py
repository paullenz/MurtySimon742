#!/usr/bin/env python3
"""Independently structured exact audit of the 7/12 candidate.

No imports from check_7_12.py. The script reconstructs the scalar rational
margins, small-a exception set, threshold certificates and degree regression
using separate functions/data flow.
"""
from fractions import Fraction
from math import isqrt
import json

F=Fraction

def ck(x,msg):
    if not x: raise AssertionError(msg)

def ceilq(n,d): return (n+d-1)//d if n>=0 else n//d

def poly_mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z

def poly_sub(a,b):
    n=max(len(a),len(b));z=[F(0)]*n
    for i in range(n):z[i]=(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
    return z

def evalp(a,x):
    v=F(0)
    for c in reversed(a):v=v*x+c
    return v

def scalar_audit():
    B=[F(1),-F(1,2),-F(1,8),-F(3,32)]
    gap=poly_sub([F(1),-F(1)],poly_mul(B,B))
    target=[F(0),F(0),F(0),F(1,16),-F(7,64),-F(3,128),-F(9,1024)]
    ck(gap==target,('independent square gap coefficients',gap))
    ck(evalp(B,F(1,2))==F(181,256),'B half')
    core=lambda u:F(64)-112*u-24*u*u-9*u*u*u
    ck(core(F(1,2))==F(7,8),'core half')

    q=F(7,20)
    Q=lambda z:F(4)-12*z+F(10,3)*z**3+F(7,10)*z**5+F(27,56)*z**7
    ck(Q(q)==-F(1631127391,30720000000),'Q rational')
    # Q' is increasing in each positive power; use q^2<=1/2 on the full high interval.
    qprime_cap=-F(12)+10*F(1,2)+F(7,2)*F(1,4)+F(27,8)*F(1,8)
    ck(qprime_cap==-F(365,64),'Qprime cap')
    tail=F(2,3)*q**5+F(1,10)*q**7+F(3,56)*q**9
    ck(tail<F(1,250),'tail below 1/250')
    ck(F(2,27)+F(1,250)<F(5,64),'middle interval bound')
    return {'gap_coefficients':[str(x) for x in gap],'B_half':str(evalp(B,F(1,2))),
            'core_half':str(core(F(1,2))),'Q_7_20':str(Q(q)),
            'Qprime_cap':str(qprime_cap),'tail_7_20':str(tail),
            'margin':str(F(5,64)-(F(2,27)+F(1,250)))}

def least(W,h,H):
    # Independently compute the minimum z by integer discriminant, then verify neighbours.
    rhs=2*W-h*(h+1)
    if H*(H-1)>=rhs:z=H
    else:
        D=1+4*rhs
        z=max(H,(1+isqrt(D))//2)
        while z*(z-1)<rhs:z+=1
    ck(z>=H and z*z-z+h*(h+1)>=2*W,('least feasible',W,h,H,z))
    if z>H: ck((z-1)*(z-2)+h*(h+1)<2*W,('least minimal',W,h,H,z))
    return z

def cap_for_a(a):
    overall=0; witness=None; pairs=levels=0
    for H in range(1,a):
        for S in range(H,a*H+1):
            pairs+=1; R=0
            for h in range(1,H+1):
                den=H-h+1
                K=max(1,-(-(S-a*(h-1))//den))
                ck(1<=K<=a,('K',a,H,S,h,K))
                W=max(H,h*K,S-(a-K)*(h-1))
                R+=least(W,h,H);levels+=1
            v=S-R
            if v>overall:overall=v;witness=(H,S)
    return max(0,overall),witness,pairs,levels

def assembly_audit():
    # Reconstruct all small-a failures of the direct strict bound.
    bad=[]
    for a in range(2,53):
        b=-(-(7*(a+1))//5)
        T=(b-a-1)**2//4
        if 128*T<5*a*a+16*a: bad.append((a,b,T))
    expected=[4,6,9,11,14,19,24,29,34,39,44]
    ck([x[0] for x in bad]==expected,('bad list',bad))
    rows=[]
    expected_caps={4:1,6:2,9:5,11:8,14:13,19:26,24:43,29:64,34:90,39:121,44:155}
    for a,b,T in bad:
        cap,wit,pairs,levels=cap_for_a(a)
        ck(cap==expected_caps[a],('cap',a,cap,expected_caps[a]))
        ck(cap<2*T,('does not close',a,b,T,cap))
        rows.append({'a':a,'least_b':b,'required_t':T,'cap_S_minus_r':cap,
                     'witness_HS':wit,'HS_cases':pairs,'threshold_cases':levels})
    D53=F(54*54,25)-F(1,4)-F(5*53*53,128)-F(53,8)
    forward=F(55*55-54*54,25)-F(5*(54*54-53*53),128)-F(1,8)
    ck(D53==F(123,3200)>0,'D53')
    ck(forward==F(177,3200)>0,'forward')
    return {'exceptions':rows,'D53':str(D53),'forward_53':str(forward)}

def degree_regression(caps,max_n=3000):
    checked=0
    for n in range(6,max_n+1):
        bmin=-(-(7*n)//12)
        for b in range(bmin,n):
            a=n-1-b;T=n*n//4-b*(n-b)
            ck(T==(b-a-1)**2//4,('identity',n,b,a,T))
            if a==0: ck(n-1<n*n//4,('star',n))
            elif a==1: ck(T>0,('a1',n,b))
            elif a in caps: ck(caps[a]<2*T,('finite',n,b,a,T,caps[a]))
            else: ck(128*T>=5*a*a+16*a,('direct',n,b,a,T))
            checked+=1
    return checked

def main():
    scalar=scalar_audit();assembly=assembly_audit()
    caps={r['a']:r['cap_S_minus_r'] for r in assembly['exceptions']}
    out={'schema':'profile-integral-7-12-independent-audit-v1','scalar':scalar,
         'assembly':assembly,'degree_pairs_regressed':degree_regression(caps)}
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
