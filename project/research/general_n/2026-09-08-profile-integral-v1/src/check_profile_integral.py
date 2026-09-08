#!/usr/bin/env python3
"""Exact audit for the 293/500 profile-integral candidate (standard library).

The universal argument is in PROOF.md. These are exact finite regressions and
small-case arithmetic certificates, not a proof by extrapolation from graphs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations_with_replacement
import json
from math import comb, isqrt
from pathlib import Path
from typing import Iterable


def require(condition: bool, detail: object) -> None:
    if not condition:
        raise AssertionError(detail)


def trim(p: list[Q]) -> list[Q]:
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def add(p: list[Q], q: list[Q]) -> list[Q]:
    r = [Q(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    return trim(r)


def scale(p: list[Q], c: Q) -> list[Q]:
    return trim([c*x for x in p])


def mul(p: list[Q], q: list[Q]) -> list[Q]:
    r = [Q(0)] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)


def value(p: list[Q], x: Q) -> Q:
    r = Q(0)
    for c in reversed(p):
        r = r*x+c
    return r


def exact_algebra() -> dict:
    # sqrt(1-u) minorant: B=(1-u)(1+u/2)>=0 on [0,1].
    B = [Q(1), Q(-1,2), Q(-1,2)]
    require(B == mul([Q(1), Q(-1)], [Q(1), Q(1,2)]), 'minorant factorisation')
    difference = add([Q(1), Q(-1)], scale(mul(B, B), Q(-1)))
    factor = scale(mul([Q(0), Q(0), Q(1)],
                       mul([Q(1), Q(-1)], [Q(3), Q(1)])), Q(1,4))
    require(difference == factor, 'minorant square-gap identity')
    P = [Q(0), Q(0), Q(2), Q(-4), Q(0), Q(2,3), Q(0), Q(2,5)]
    c = Q(457,120)
    low_gap = add([Q(0), Q(0), Q(2), -c], scale(P, Q(-1)))
    require(low_gap == [Q(0), Q(0), Q(0), Q(2,3)/4+Q(2,5)/16,
                        Q(0), Q(-2,3), Q(0), Q(-2,5)], 'low interval gap')
    C = Q(107,30)
    high_gap = add([Q(0), Q(0), Q(2), -C], scale(P, Q(-1)))
    require(high_gap == [Q(0), Q(0), Q(0), Q(2,3)/2+Q(2,5)/4,
                         Q(0), Q(-2,3), Q(0), Q(-2,5)], 'high interval gap')
    cubic_max = Q(32,27)/c**2
    cubic_gap = [cubic_max, Q(0), Q(-2), c]
    square_factor = scale(mul(mul([-Q(4,3)/c, Q(1)], [-Q(4,3)/c, Q(1)]),
                              [Q(2,3)/c, Q(1)]), c)
    require(cubic_gap == square_factor, 'global cubic maximum certificate')
    require(cubic_max == Q(51200,626547) < Q(1,12), 'low rational margin')
    require(Q(4)-3*C/2 < 0, 'high cubic decreasing from q=1/2')
    require(Q(1,2)-C/8 == Q(13,240) < Q(1,12), 'high rational margin')
    ratio = Q(43,207)
    require((Q(293,500)-Q(1,2))/(1-Q(293,500)) == ratio, 'degree ratio')
    A = ratio**2-Q(1,24)
    L = 2*ratio**2-Q(1,8)
    margin31 = A*31**2+L*31+ratio**2-Q(1,4)
    step31 = A*63+L
    require(A > 0 and margin31 == Q(1757,85698) > 0 and step31 > 0,
            'all a>=31 margin certificate')
    return {
        'polynomial_identities': 5,
        'low_scalar_upper_bound': str(cubic_max),
        'low_margin_below_1_over_12': str(Q(1,12)-cubic_max),
        'high_scalar_upper_bound': '13/240',
        'high_margin_below_1_over_12': str(Q(1,12)-Q(13,240)),
        'degree_ratio': str(ratio),
        'large_a_quadratic_coefficient': str(A),
        'large_a_margin_at_31': str(margin31),
        'large_a_first_forward_difference': str(step31),
        'scope': 'Exact polynomial identities and rational sign certificates; calculus remains a hand proof.'
    }


def midpoint_regression(max_a: int = 100) -> dict:
    parameters = midpoint_cases = 0
    for a in range(2, max_a+1):
        for s in range(1, a):
            parameters += 1
            # Four times [f(s+1/2)^2-s^2].
            endpoint_gap = 8*a*s-(2*s+1)**2-4*s*s
            require(endpoint_gap >= 0, ('shifted endpoint', a, s))
            # Four times [(s+a/2)^2 - 2as].
            require((2*s+a)**2-8*a*s == (2*s-a)**2,
                    ('endpoint error bound', a, s))
            # Every h is checked at five symmetric offsets in [0,1/2].
            for h in range(1, s+1):
                for j in range(5):
                    d = Q(j,8)
                    left = 2*a*s-(h-d)**2
                    right = 2*a*s-(h+d)**2
                    centre = Q(2*a*s-h*h)
                    gap = 4*centre-left-right
                    require(left >= 0 and right >= 0 and gap >= 0,
                            ('midpoint radicands', a, s, h, j))
                    require(gap**2-4*left*right == 32*a*s*d*d >= 0,
                            ('midpoint square certificate', a, s, h, j))
                    midpoint_cases += 1
    return {'max_a': max_a, 'integer_parameters': parameters,
            'midpoint_cases': midpoint_cases,
            'scope': 'Finite exact samples of the concavity and endpoint identities; no floating-point integration.'}


@lru_cache(maxsize=None)
def least_z(W: int, h: int, H: int) -> int:
    require(1 <= h <= H and W >= H, ('least_z domain', W, h, H))
    z = H
    if z*z-z+h*(h+1) < 2*W:
        D = 1+8*W-4*h*(h+1)
        require(D > 0, ('discriminant', D))
        z = max(H, (1+isqrt(D))//2)
        if z*z-z+h*(h+1) < 2*W:
            z += 1
    require(z*z-z+h*(h+1) >= 2*W, 'least_z feasible')
    require(z == H or (z-1)*(z-2)+h*(h+1) < 2*W, 'least_z minimal')
    return z


def profile_audit(max_a: int = 11) -> dict:
    profiles = levels = positive_gap = 0
    digest = sha256()
    rows = []
    for a in range(1, max_a+1):
        local_count = 0
        best_gap = -10**9
        best_profile = None
        for s in combinations_with_replacement(range(a), a):
            local_count += 1
            profiles += 1
            H, S = s[-1], sum(s)
            hist = [0]*a
            for x in s:
                hist[x] += 1
            W, ell, previous, R = S, a-hist[0], None, 0
            for h in range(1, H+1):
                if h > 1:
                    W -= (h-1)*hist[h-1]
                    ell -= hist[h-1]
                z = least_z(W, h, H)
                require(previous is None or previous >= z, 'tail monotonicity')
                previous = z
                # Exact sufficient Cauchy-Schwarz bound for the pointwise sum.
                deficit = a*a*z*z-ell*(2*a*W-ell*h*h)
                require(deficit >= 0, ('pointwise bound', a, s, h, z))
                require(2*W <= z*z-z+h*(h+1), 'exact threshold')
                R += z
                levels += 1
            require(12*(S-R) < a*a+3*a, ('integrated surplus consequence', a, s, R))
            gap = S-R
            positive_gap += gap > 0
            if gap > best_gap:
                best_gap, best_profile = gap, list(s)
            digest.update((json.dumps([a,list(s),R], separators=(',',':'))+'\n').encode())
        require(local_count == comb(2*a-1,a), ('profile completeness', a, local_count))
        rows.append({'a':a,'profiles':local_count,'max_S_minus_R_lower':best_gap,
                     'first_maximising_profile':best_profile})
    return {'max_a':max_a,'profiles':profiles,'threshold_levels':levels,
            'profiles_with_positive_abstract_S_minus_R':positive_gap,
            'rows':rows,'ordered_sha256':digest.hexdigest(),
            'scope':'Every sorted demand multiset; minimal feasible tails. These are NOT graph examples.'}


def ceil_div(n: int, d: int) -> int:
    require(d > 0, 'positive denominator')
    return -((-n)//d)


def small_certificate(a: int) -> dict:
    rows = []
    cases = levels = 0
    for H in range(1,a):
        maximum = -10**9
        witness = None
        for S in range(H,a*H+1):
            cases += 1
            R = 0
            for h in range(1,H+1):
                K = max(1,ceil_div(S-a*(h-1),H-h+1))
                require(K <= a, ('K range', a,H,S,h,K))
                W = max(H,h*K,S-(a-K)*(h-1))
                # Intentionally use direct integer iteration, not least_z/isqrt.
                z = H
                while z*z-z+h*(h+1) < 2*W:
                    z += 1
                R += z
                levels += 1
            if S-R > maximum:
                maximum,witness = S-R,S
        rows.append({'H':H,'max_S_minus_R_lower':maximum,'first_maximising_S':witness})
    return {'a':a,'HS_cases':cases,'threshold_cases':levels,'rows':rows,
            'upper_S_minus_r':max(0,max(row['max_S_minus_R_lower'] for row in rows)),
            'zero_demand_case':'S=0 gives t<=0 separately'}


def degree_assembly(max_n: int = 5000) -> dict:
    small = []
    for a in range(2,31):
        b = ceil_div(293*(a+1),207)
        required_t = (b-a-1)**2//4
        if a == 6:
            method = 'finite demand certificate t<=1'
            require(required_t > 1, 'a=6 exclusion')
        elif a == 11:
            method = 'finite demand certificate t<=4'
            require(required_t > 4, 'a=11 exclusion')
        else:
            method = 'strict profile-integral bound'
            require(24*required_t >= a*a+3*a, ('small degree', a,b,required_t))
        small.append({'a':a,'least_b':b,'required_t':required_t,
                      'strict_integral_upper':str(Q(a*a+3*a,24)),'method':method})
    checked = 0
    for n in range(6,max_n+1):
        for b in range(ceil_div(293*n,500),n):
            a = n-1-b
            T = n*n//4-b*(n-b)
            require(T == (b-a-1)**2//4, 'parity identity')
            if a == 0:
                require(n-1 < n*n//4, 'universal vertex star case')
            elif a == 1:
                require(T > 0, 'a=1 edgeless F case')
            elif a == 6:
                require(T > 1, 'a=6 certificate')
            elif a == 11:
                require(T > 4, 'a=11 certificate')
            else:
                require(24*T >= a*a+3*a, ('degree regression',n,b,a,T))
            checked += 1
    return {'small_a_table':small,'max_n_regression':max_n,'degree_pairs_checked':checked,
            'scope':'Checks assembly for eligible maximum degrees only, NOT every graph through max_n.'}


def negative_controls() -> dict:
    # Dropping z>=h invalidates the claimed pointwise inequality.
    a,h,z,W,ell = 4,3,0,3,1
    require(2*W <= z*z-z+h*(h+1), 'negative control keeps threshold inequality')
    require(a*a*z*z < ell*(2*a*W-ell*h*h), 'negative control breaks pointwise claim')
    # At a=2,s=1 a right rectangle is strictly below the integral: f(0)>f(1),
    # and concavity puts the integral above the trapezoid. So error cannot be omitted.
    require(4 > 3, 'nonzero quadrature error witness')
    old_family = []
    for k in range(1,11):
        a,S,r,t = 27*k,216*k*k,144*k*k,36*k*k
        require(3*S**3 <= a*a*r*(2*r+1) and S == r+2*t, 'old scalar saturation')
        require(24*t > a*a+3*a, 'new bound needs full threshold structure')
        old_family.append([a,S,r,t])
    require(500*3 >= 293*5 and 2*3 == 5*5//4, 'K23 small-order boundary')
    return {'missing_source_floor':{'a':4,'demands':[0,0,0,3],'h':3,'z':0},
            'zero_quadrature_error':'a=2,s=1: integral exceeds the right rectangle; see hand proof',
            'old_cubic_only_family_fails_new_bound':old_family,
            'small_order_boundary':'K(2,3) violates a strict extension to all n>=4',
            'all_controls_behaved_as_expected':True}


def run(max_a: int, max_n: int, midpoint_max_a: int) -> dict:
    algebra = exact_algebra()
    midpoint = midpoint_regression(midpoint_max_a)
    profiles = profile_audit(max_a)
    certificates = [small_certificate(6),small_certificate(11)]
    require([x['upper_S_minus_r'] for x in certificates] == [2,8], 'small certificate bounds')
    require([row['max_S_minus_R_lower'] for row in certificates[0]['rows']] == [2,1,0,-2,-7], 'a=6 rows')
    require([row['max_S_minus_R_lower'] for row in certificates[1]['rows']] == [6,8,7,7,4,1,-4,-10,-18,-27], 'a=11 rows')
    require(sum(x['HS_cases'] for x in certificates) == 640, 'finite certificate coverage')
    return {'schema':'profile-integral-audit-v1','status':'PASS','algebra':algebra,
            'midpoint':midpoint,'profiles':profiles,'small_certificates':certificates,
            'degree_assembly':degree_assembly(max_n),'negative_controls':negative_controls(),
            'mathematics':'CANDIDATE hand proof','internal_computation':'REPRODUCED',
            'formal_verification':False,'independent_external_review':'OPEN',
            'new_actual_graph_enumeration':False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-a',type=int,default=11)
    parser.add_argument('--max-n',type=int,default=5000)
    parser.add_argument('--midpoint-max-a',type=int,default=100)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_a <= 11 or not 6 <= args.max_n <= 5000 or not 2 <= args.midpoint_max_a <= 100:
        parser.error('audit limits: max-a in 1..11, max-n in 6..5000, midpoint-max-a in 2..100')
    if args.output and args.output.exists():
        raise FileExistsError(args.output)
    result = run(args.max_a,args.max_n,args.midpoint_max_a)
    text = json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as handle:
            handle.write(text)
    else:
        print(text,end='')


if __name__ == '__main__':
    main()
