#!/usr/bin/env python3
"""Exact residual-resource cuts; optional LP-assisted certificate discovery.

All mathematical claims remain candidate derivations pending external review.
The LP solver proposes coefficients only. check_certificate uses exact integers.
No full order sweep, integer-branching solver or formal proof assistant is used.
Run: python3 coupled.py --output RESULTS.json
     python3 coupled.py --discover --output RESULTS_WITH_DISCOVERY.json
"""
from __future__ import annotations
import sys
if sys.flags.optimize:
    raise RuntimeError('Regression checks require Python without -O or PYTHONOPTIMIZE.')

import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import json
import platform


@lru_cache(None)
def scalar_max(a: int) -> tuple[F, tuple[int, ...]]:
    if a < 1:
        raise ValueError('a must be positive')
    values = [F(s*(a+1-2*s), a-s) for s in range(a)]
    best = max(values)
    return a*best, tuple(s for s,x in enumerate(values) if x == best)


def scalar_excludes(a: int, b: int, t: int) -> bool:
    """For t>0 and the candidate residual construction. Strict for a>=5."""
    best, _ = scalar_max(a)
    return b+2*t >= best if a >= 5 else b+2*t > best


def profile_data(profile: dict) -> dict:
    d, rho, R = (list(profile[k]) for k in ('d','rho','R'))
    a, b = len(d), len(rho)
    if not a or not b or len(R) != a:
        raise ValueError('bad dimensions')
    if any(type(x) is not int for xs in (d,rho,R) for x in xs):
        raise ValueError('integer entries required')
    if any(not 0 <= x < a for x in d) or any(not 0 <= x <= a for x in rho) or any(not 0 <= x <= b for x in R):
        raise ValueError('entry out of range')
    if sum(rho) != sum(R) or sum(d) % 2:
        raise ValueError('inconsistent ledger')
    s = [max(0,di-ri) for di,ri in zip(d,R)]
    caps = [min(a-x,b-1) for x in rho]
    # A real source of degree q has q distinct labels and supplements.
    # Each supplement has at least q-1 cross-neighbours.
    rounds = 0
    while True:
        new = []
        for u, ru in enumerate(rho):
            best = 0
            for q in range(1,caps[u]+1):
                labels = sorted(di for di,ri in zip(d,R)
                                if di <= ru+ri and di <= ru+q-1)
                suppliers = sorted(rho[w] for w in range(b) if w != u
                                   and rho[w]+caps[w] >= q-1)
                j = 0
                for rw in suppliers:
                    if j < len(labels) and labels[j] <= ru+rw:
                        j += 1
                if j >= q:
                    best = q
            new.append(best)
        rounds += 1
        if new == caps:
            break
        caps = new
    eligible = [[u for u in range(b) if caps[u] > 0
                 and d[i] <= rho[u]+R[i] and d[i] <= rho[u]+caps[u]-1]
                for i in range(a)]
    forced = [set(us) if s[i] > 0 and s[i] == len(us) else set()
              for i,us in enumerate(eligible)]
    f = [sum(u in fs for fs in forced) for u in range(b)]
    triples = []
    for i in range(a):
        for u in eligible[i]:
            lam = max(1,f[u],d[i]-rho[u]+1)
            if lam > caps[u]:
                continue
            for w in range(b):
                if w != u and w not in forced[i] and d[i] <= rho[u]+rho[w] and rho[w]+caps[w] >= lam-1:
                    triples.append((u,i,w))
    sink = [max(0,min(b-1,rho[w]+b-a-1)) for w in range(b)]
    return {'a':a,'b':b,'s':s,'c':caps,'p':sink,'triples':triples,
            'rounds':rounds,'r':sum(rho),'t':sum(d)//2-sum(rho)}


def resource_keys(a: int, b: int) -> list[tuple]:
    return ([('source',u) for u in range(b)]
            +[('incidence',u,i) for u in range(b) for i in range(a)]
            +[('pair',u,w) for u,w in combinations(range(b),2)]
            +[('supplement',w) for w in range(b)])


def triple_resources(u: int, i: int, w: int) -> tuple[tuple,...]:
    return (('source',u),('incidence',u,i),('pair',min(u,w),max(u,w)),('supplement',w))


def resource_capacity(key: tuple, data: dict) -> int:
    if key[0] == 'source':
        return data['c'][key[1]]
    if key[0] == 'supplement':
        return data['p'][key[1]]
    return 1


def check_certificate(profile: dict, certificate: dict) -> dict:
    """Reject malformed certificates; recompute domains, caps and all costs."""
    data = profile_data(profile)
    a,b = data['a'],data['b']
    y = certificate['label_weights']
    if len(y) != a or any(type(v) is not int or v < 0 for v in y):
        raise ValueError('bad label weights')
    allowed_keys = set(resource_keys(a,b))
    z = {}
    for row in certificate['resource_weights']:
        key, val = tuple(row[:-1]),row[-1]
        if key not in allowed_keys or key in z or type(val) is not int or val < 0:
            raise ValueError('bad resource weight')
        z[key] = val
    for u,i,w in data['triples']:
        if y[i] > sum(z.get(k,0) for k in triple_resources(u,i,w)):
            raise ValueError('an allowed triple is not covered')
    lhs = sum(x*v for x,v in zip(y,data['s']))
    rhs = sum(v*resource_capacity(k,data) for k,v in z.items())
    if lhs <= rhs:
        raise ValueError('no strict contradiction')
    return {'status':'EXACT_CERTIFICATE_PASS','weighted_demand':lhs,
            'weighted_capacity':rhs,'margin':lhs-rhs,
            'allowed_triples_checked':len(data['triples']),
            'source_caps':data['c'],'supplement_caps':data['p']}


def discover_certificate(profile: dict) -> dict:
    """Optional numerical discovery; returned exclusions require exact checking."""
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import lil_matrix
    data = profile_data(profile)
    a,b = data['a'],data['b']
    keys = resource_keys(a,b)
    ids = {k:a+j for j,k in enumerate(keys)}
    nvar = a+len(keys)
    cost = np.array([-v for v in data['s']]+[resource_capacity(k,data) for k in keys],dtype=float)
    A = lil_matrix((len(data['triples']),nvar))
    for j,(u,i,w) in enumerate(data['triples']):
        A[j,i] = 1
        for key in triple_resources(u,i,w):
            A[j,ids[key]] = -1
    eq = lil_matrix((1,nvar)); eq[0,:a] = 1
    res = linprog(cost,A_ub=A.tocsr(),b_ub=np.zeros(len(data['triples'])),
                  A_eq=eq.tocsr(),b_eq=[1],bounds=(0,None),method='highs',
                  options={'time_limit':20.0})
    if not res.success or res.x is None:
        return {'status':'NO_CERTIFICATE','solver_status':int(res.status)}
    vec = [max(F(0),F(float(x)).limit_denominator(1000000)) for x in res.x]
    # Repair any rationalization deficit upward using source resources.
    for u,i,w in data['triples']:
        gap = vec[i]-sum(vec[ids[k]] for k in triple_resources(u,i,w))
        if gap > 0:
            vec[ids[('source',u)]] += gap
    denominator = lcm(*(x.denominator for x in vec))
    ints = [int(x*denominator) for x in vec]
    common = gcd(*ints) or 1
    ints = [x//common for x in ints]
    cert = {'label_weights':ints[:a],
            'resource_weights':[list(k)+[ints[a+j]] for j,k in enumerate(keys) if ints[a+j]]}
    try:
        checked = check_certificate(profile,cert)
    except ValueError:
        return {'status':'NO_EXACT_CERTIFICATE','solver_objective':float(res.fun)}
    return {'status':'EXACT_CERTIFICATE','certificate':cert,'check':checked}


def n27_fixture() -> dict:
    # Transcribed from first row, blob 39d9425b8209ecd1c447905279a56b4d64214dc5.
    return {'d':[5,6,6,6,6,6,7,7,8,8,9],
            'rho':[1]*8+[3,3,3,4,4,5,5],
            'R':[1,2,2,3,3,3,4,4,4,4,5]}


def scalar_rows() -> list[dict]:
    result = []
    for n in [27,28,29,30,31,32,33,34,35,40,50,100]:
        remaining,certs = [],[]
        for b in range((n+1)//2+1,n-1):
            a=n-1-b; t=n*n//4-b*(n-b)
            best,ks=scalar_max(a)
            if scalar_excludes(a,b,t):
                certs.append({'b':b,'a':a,'t':t,'lhs':b+2*t,
                              'bound':str(best),'maximizers':list(ks),
                              'strict_equality_obstruction_used':b+2*t==best})
            else:
                remaining.append(b)
        result.append({'n':n,'target':n*n//4,'remaining_degrees':remaining,'exclusions':certs})
    return result


def arithmetic_tests() -> dict:
    pointwise=0; maxima=0; cutoff=0
    for a in range(1,501):
        best,ks=scalar_max(a)
        for s in range(a):
            # f0(s)<=a(3-2sqrt(2)), by exact squared comparison.
            f0=F(s*(a-2*s),a-s)
            z=3*a-f0
            assert z >= 0 and z*z >= 8*a*a
            pointwise+=1
        if a>=5:
            assert best>a and all(2<=s and 2*s<a for s in ks)
            for s in ks:
                z=F(a*s,a-s)
                assert z < a < 2*(a-s)
            maxima+=1
    for n in range(4,1001):
        for b in range((n+1)//2+1,n-1):
            z=10*n-14*b
            if z<=0 or z*z<=2*n*n:
                a=n-1-b; t=n*n//4-b*(n-b)
                x=3*a*a-2*t
                assert t>0 and (x<0 or x*x<8*a**4)
                cutoff+=1
    return {'pointwise_irrational_bound_checks':pointwise,
            'strict_equality_maximizer_checks':maxima,
            'high_degree_checks_through_n1000':cutoff,'status':'PASS'}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('RESULTS.json'))
    p.add_argument('--discover',action='store_true')
    args=p.parse_args()
    result={'status':'CANDIDATE mathematics; exact arithmetic reproduced; external review OPEN',
            'environment':{'python':platform.python_version()},'arithmetic_tests':arithmetic_tests(),
            'scalar_rows':scalar_rows(),'n27_profile':n27_fixture(),
            'n27_derived_caps':profile_data(n27_fixture())['c'],
            'limitations':['No order above 27 proved complete.','No complete degree-profile enumeration performed.',
                           'Certificate engine is a relaxation separator, not a full graph or integer-branching solver.']}
    if args.discover:
        import scipy
        result['environment']['scipy']=scipy.__version__
        result['n27_discovery']=discover_certificate(n27_fixture())
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('scalar_rows',)},indent=2))
    for row in result['scalar_rows']:
        print(row['n'],row['remaining_degrees'])

if __name__=='__main__':
    main()
