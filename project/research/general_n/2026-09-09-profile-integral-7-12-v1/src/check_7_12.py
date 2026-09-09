#!/usr/bin/env python3
"""Exact standard-library checker for the 7/12 profile-integral strengthening.

This checker verifies algebraic/rational certificates and finite small-a degree
assembly. It does not search graphs and is not a substitute for review of the
shared graph-to-demand/profile-integral lemmas.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt
import json


def require(c, d):
    if not c: raise AssertionError(d)


def ceil_div(n,d):
    require(d>0,('den',d)); return -((-n)//d)


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def add(p,q):
    r=[Q(0)]*max(len(p),len(q))
    for i,x in enumerate(p):r[i]+=x
    for i,x in enumerate(q):r[i]+=x
    return trim(r)
def scale(p,c):return trim([c*x for x in p])
def mul(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return trim(r)

def value(p,x):
    r=Q(0)
    for c in reversed(p):r=r*x+c
    return r


def scalar_certificate():
    # B(u)=1-u/2-u^2/8-3u^3/32.
    B=[Q(1),-Q(1,2),-Q(1,8),-Q(3,32)]
    one_minus_u=[Q(1),Q(-1)]
    gap=add(one_minus_u,scale(mul(B,B),Q(-1)))
    expected=scale(mul([Q(0),Q(0),Q(0),Q(1)],
                       [Q(64),Q(-112),Q(-24),Q(-9)]),Q(1,1024))
    require(gap==expected,('sqrt minorant square gap',gap,expected))
    require(value(B,Q(1,2))==Q(181,256)>0,'B endpoint')
    core=[Q(64),Q(-112),Q(-24),Q(-9)]
    require(value(core,Q(1,2))==Q(7,8)>0,'core endpoint')
    # B' and core' have strictly negative coefficients on u>=0, so both
    # functions are decreasing; endpoint positivity proves B>=0 and gap>=0
    # throughout [0,1/2].

    # After x=2q^2, x-Phi(x) is bounded above by
    # P(q)=2q^2-4q^3+(2/3)q^5+(1/10)q^7+(3/56)q^9.
    P=[Q(0),Q(0),Q(2),Q(-4),Q(0),Q(2,3),Q(0),Q(1,10),Q(0),Q(3,56)]
    # P'(q)=q Qpoly(q), Qpoly=4-12q+(10/3)q^3+(7/10)q^5+(27/56)q^7.
    Qpoly=[Q(4),Q(-12),Q(0),Q(10,3),Q(0),Q(7,10),Q(0),Q(27,56)]
    q0=Q(7,20)
    require(value(Qpoly,q0)==Q(-1631127391,30720000000)<0,'Q(7/20)')
    # On [7/20,1/sqrt(2)], Qpoly' <= -12+10/2+(7/2)/4+(27/8)/8.
    derivative_upper=-Q(12)+Q(10,2)+Q(7,8)+Q(27,64)
    require(derivative_upper==Q(-365,64)<0,'Q derivative upper')
    # On [1/3,7/20], 2q^2-4q^3 is decreasing, so <=2/27;
    # the positive tail is increasing and is <1/250 at 7/20.
    tail=Q(2,3)*q0**5+Q(1,10)*q0**7+Q(3,56)*q0**9
    require(tail==Q(43868404489,12288000000000)<Q(1,250),'tail bound')
    middle_upper=Q(2,27)+Q(1,250)
    require(Q(5,64)-middle_upper==Q(11,216000)>0,'5/64 margin')
    # On [0,1/3], Qpoly>=4-12q>=0, so P increases to the middle interval.
    return {
        'sqrt_minorant_B_at_half':str(value(B,Q(1,2))),
        'sqrt_minorant_core_at_half':str(value(core,Q(1,2))),
        'Q_at_7_over_20':str(value(Qpoly,q0)),
        'Qprime_uniform_upper':str(derivative_upper),
        'tail_at_7_over_20':str(tail),
        'scalar_upper':'5/64',
        'middle_margin':str(Q(5,64)-middle_upper),
        'consequence':'t < 5*a^2/128 + a/8',
    }


@lru_cache(maxsize=None)
def least_z(W,h,H):
    require(1<=h<=H and W>=H,('least_z domain',W,h,H))
    z=H
    if z*z-z+h*(h+1)<2*W:
        D=1+8*W-4*h*(h+1)
        require(D>0,('disc',D))
        z=max(H,(1+isqrt(D))//2)
        if z*z-z+h*(h+1)<2*W:z+=1
    require(z*z-z+h*(h+1)>=2*W,'least_z feasible')
    require(z==H or (z-1)*(z-2)+h*(h+1)<2*W,'least_z minimal')
    return z


def small_certificate(a):
    best=0; best_HS=None; cases=levels=0
    rows=[]
    for H in range(1,a):
        rowbest=-10**9; rowS=None
        for S in range(H,a*H+1):
            cases+=1; R=0
            for h in range(1,H+1):
                K=max(1,ceil_div(S-a*(h-1),H-h+1))
                require(K<=a,('K',a,H,S,h,K))
                W=max(H,h*K,S-(a-K)*(h-1))
                R+=least_z(W,h,H); levels+=1
            u=S-R
            if u>rowbest:rowbest,rowS=u,S
            if u>best:best,best_HS=u,(H,S)
        rows.append({'H':H,'max_S_minus_R_lower':rowbest,'first_maximising_S':rowS})
    return {'a':a,'upper_S_minus_r':max(0,best),'first_maximising_HS':best_HS,
            'HS_cases':cases,'threshold_cases':levels,'rows':rows}


def degree_assembly():
    # b >= 7n/12 iff 5b >= 7(a+1), so least b is ceil(7(a+1)/5).
    # For a>=53, the continuous lower t bound exceeds the new strict upper.
    D53=Q(54*54,25)-Q(1,4)-Q(5*53*53,128)-Q(53,8)
    step53=Q(6*53-141,3200)
    require(D53==Q(123,3200)>0,('D53',D53))
    require(step53==Q(177,3200)>0,('step53',step53))
    exceptions=[]; ordinary=[]
    expected=[4,6,9,11,14,19,24,29,34,39,44]
    for a in range(2,53):
        b=ceil_div(7*(a+1),5)
        T=(b-a-1)**2//4
        if 128*T>=5*a*a+16*a:
            ordinary.append({'a':a,'least_b':b,'required_t':T})
        else:
            exceptions.append((a,b,T))
    require([a for a,_,_ in exceptions]==expected,('exceptions',exceptions))
    finite=[]
    for a,b,T in exceptions:
        c=small_certificate(a)
        require(c['upper_S_minus_r']<2*T,
                ('finite exception not closed',a,b,T,c['upper_S_minus_r']))
        finite.append({'a':a,'least_b':b,'required_t':T,
                       'upper_S_minus_r':c['upper_S_minus_r'],
                       'first_maximising_HS':c['first_maximising_HS'],
                       'HS_cases':c['HS_cases'],'threshold_cases':c['threshold_cases']})
    return {'large_a_start':53,'D53':str(D53),'first_forward_difference':str(step53),
            'ordinary_small_a_count':len(ordinary),'exception_count':len(finite),
            'exceptions':finite}


def regression(max_n=5000):
    checked=0
    finite_caps={x['a']:x['upper_S_minus_r'] for x in degree_assembly()['exceptions']}
    for n in range(6,max_n+1):
        for b in range(ceil_div(7*n,12),n):
            a=n-1-b
            T=n*n//4-b*(n-b)
            require(T==(b-a-1)**2//4,('parity',n,b,a,T))
            if a==0:
                require(n-1<n*n//4,('star',n))
            elif a==1:
                require(T>0,('a1',n,b))
            elif a in finite_caps:
                require(finite_caps[a]<2*T,('finite regression',n,b,a,T))
            else:
                require(128*T>=5*a*a+16*a,('profile regression',n,b,a,T))
            checked+=1
    return {'max_n':max_n,'eligible_degree_pairs_checked':checked}


def main():
    out={'schema':'profile-integral-7-12-exact-check-v1',
         'scalar':scalar_certificate(),
         'degree_assembly':degree_assembly(),
         'regression':regression()}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
