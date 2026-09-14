#!/usr/bin/env python3
"""Independent finite verifier for Q_STRATIFIED_CROSSING_GAP.md.

This verifier does not use the Hall-flow implementation. It works directly with
a single fixed-q stratum represented by two nondecreasing integer sequences:
P (target cap) and m (pre-diagonal incoming count), together with arbitrary
selected bits epsilon. It compares the direct receiver capacity, the q-only
comonotone rearrangement, and the claimed crossing statistic.
"""
from itertools import combinations_with_replacement, product
import json, random


def evaluate(P, m, eps):
    y = [mm-ee for mm,ee in zip(m,eps)]
    if min(y, default=0) < 0:
        return None
    exact = sum(min(p, yy) for p,yy in zip(P,y))
    ys = sorted(y)
    upper = sum(min(p, yy) for p,yy in zip(P,ys))

    crossing = 0
    blocks = 0
    for M in sorted(set(m)):
        HS = sum(1 for p,mm,e in zip(P,m,eps) if mm==M and e==1 and p>=M)
        LU = sum(1 for p,mm,e in zip(P,m,eps) if mm==M and e==0 and p<=M-1)
        if HS or LU:
            blocks += 1
        crossing += min(HS,LU)
    return exact, upper, crossing, blocks


def check(P,m,eps):
    out=evaluate(P,m,eps)
    if out is None:
        return None
    exact,upper,crossing,blocks=out
    if upper < exact:
        raise AssertionError(('upper below exact',P,m,eps,out))
    if upper-exact != crossing:
        raise AssertionError(('crossing identity failure',P,m,eps,out))
    return out


def main():
    exhaustive_cases=0
    positive_gap_cases=0
    max_gap=0
    crossing_blocks=0

    # Exhaust every nondecreasing P,m sequence through length 5 with values 0..4,
    # and every selected-bit pattern compatible with nonnegative actual incoming.
    vals=range(5)
    for n in range(0,6):
        Ps=list(combinations_with_replacement(vals,n))
        Ms=list(combinations_with_replacement(vals,n))
        for P in Ps:
            for m in Ms:
                for eps in product((0,1),repeat=n):
                    out=check(P,m,eps)
                    if out is None:
                        continue
                    exhaustive_cases += 1
                    exact,upper,crossing,blocks=out
                    positive_gap_cases += crossing>0
                    max_gap=max(max_gap,crossing)
                    crossing_blocks += blocks

    rng=random.Random(7420914)
    random_cases=20000
    random_positive=0
    random_max_gap=0
    for _ in range(random_cases):
        n=rng.randint(1,24)
        P=sorted(rng.randint(0,14) for _ in range(n))
        m=sorted(rng.randint(0,14) for _ in range(n))
        eps=[rng.randint(0,1) for _ in range(n)]
        # Make selected copies with m=0 unselected so y remains nonnegative.
        eps=[0 if mm==0 else e for mm,e in zip(m,eps)]
        exact,upper,crossing,blocks=check(P,m,eps)
        random_positive += crossing>0
        random_max_gap=max(random_max_gap,crossing)

    result={
        'schema':'q-stratified-crossing-gap-verification-v1',
        'exhaustive_max_length':5,
        'exhaustive_value_max':4,
        'exhaustive_cases':exhaustive_cases,
        'exhaustive_positive_gap_cases':positive_gap_cases,
        'exhaustive_max_gap':max_gap,
        'exhaustive_nontrivial_crossing_blocks':crossing_blocks,
        'random_seed':7420914,
        'random_cases':random_cases,
        'random_positive_gap_cases':random_positive,
        'random_max_gap':random_max_gap,
        'result':'PASS',
        'external_review':'OPEN'
    }
    print(json.dumps(result,indent=2,sort_keys=True))
    with open('Q_STRATIFIED_CROSSING_GAP_VERIFICATION.json','w') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')

if __name__=='__main__':
    main()
