#!/usr/bin/env python3
"""Independent finite verifier for EXTERIOR_SLACK_UPSET_REDUCTION.md.

Checks two logically separate claims:

1. For a canonical labelled Hall profile, the union M+ of all minimum cuts is
   complete-type/sharp-upward closed and every nonempty labelled exterior set
   has strict residual-slack margin at least one.
2. For an arbitrary residual-capacity Hall profile, existence of any nonempty
   set with margin <= 0 is equivalent to existence of a nonempty sharp up-set
   with margin <= 0.  This explicitly includes the delicate zero-margin case
   where the empty set is also a global minimizer.
"""
from itertools import combinations_with_replacement
import json, random


def compat(a,b):
    q,c,_=a; q2,c2,_=b
    return q <= c2+1 and q2 <= c


def margin(profile, mask, caps=None):
    n=len(profile)
    if caps is None: caps=[x[2] for x in profile]
    total=0
    for w in range(n):
        incoming=sum(1 for u in range(n) if (mask>>u)&1 and u!=w and compat(profile[u],profile[w]))
        total += min(caps[w],incoming)
    total -= sum(profile[u][0] for u in range(n) if (mask>>u)&1)
    return total


def sharp_dom(profile,caps,x,y):
    qx,cx,_=profile[x]; qy,cy,_=profile[y]
    return cx<=cy and (qx>qy or (qx==qy and caps[x]>=caps[y]))


def is_upset(profile,caps,mask,allowed=None):
    n=len(profile)
    if allowed is None: allowed=(1<<n)-1
    for y in range(n):
        if not ((allowed>>y)&1 and (mask>>y)&1): continue
        for x in range(n):
            if x==y or not ((allowed>>x)&1): continue
            if sharp_dom(profile,caps,x,y) and not ((mask>>x)&1):
                return False
    return True


def canonical_check(profile,stats):
    n=len(profile); full=(1<<n)-1
    vals=[margin(profile,m) for m in range(1<<n)]
    m=min(vals)
    mins=[x for x,v in enumerate(vals) if v==m]
    M=0
    for x in mins: M |= x
    if margin(profile,M)!=m:
        raise AssertionError('union of minimizers not minimum')
    caps=[x[2] for x in profile]
    if not is_upset(profile,caps,M):
        raise AssertionError('canonical M+ not sharp up-set')

    # identical labelled vertices must be selected together in M+.
    for i in range(n):
        for j in range(i+1,n):
            if profile[i]==profile[j] and (((M>>i)&1) != ((M>>j)&1)):
                raise AssertionError('M+ splits identical type')

    outside=full^M
    dM=[]
    for w in range(n):
        dM.append(sum(1 for u in range(n) if (M>>u)&1 and u!=w and compat(profile[u],profile[w])))
    slack=[max(0,caps[w]-dM[w]) for w in range(n)]

    ext_subsets=0
    min_ext=None
    sub=outside
    while sub:
        diff=margin(profile,M|sub)-m
        fs=margin(profile,sub,slack)
        if diff!=fs:
            raise AssertionError(('residual identity mismatch',profile,M,sub,diff,fs,slack))
        if fs<1:
            raise AssertionError(('strict labelled exterior expansion failed',profile,M,sub,fs))
        min_ext=fs if min_ext is None else min(min_ext,fs)
        ext_subsets+=1
        sub=(sub-1)&outside
    stats['canonical_profiles']+=1
    stats['canonical_exterior_subsets']+=ext_subsets
    if outside:
        stats['canonical_nonempty_exterior']+=1
        stats['minimum_canonical_exterior_margin']=min(stats['minimum_canonical_exterior_margin'],min_ext)


def residual_equivalence_check(profile,stats):
    n=len(profile); full=(1<<n)-1
    caps=[x[2] for x in profile]
    vals={m:margin(profile,m,caps) for m in range(1,1<<n)}
    min_non=min(vals.values())
    up=[v for m,v in vals.items() if is_upset(profile,caps,m,full)]
    if not up:
        raise AssertionError('no nonempty up-set')
    min_up=min(up)
    if (min_non<=0)!=(min_up<=0):
        raise AssertionError(('violation/upset equivalence failed',profile,min_non,min_up))

    # Directly verify the proof mechanism in the <=0 cases.
    if min_non<=0:
        allvals=[margin(profile,m,caps) for m in range(1<<n)]
        gm=min(allvals)
        minimizers=[m for m,v in enumerate(allvals) if v==gm]
        maxcard=max(bin(m).count('1') for m in minimizers)
        witnesses=[m for m in minimizers if bin(m).count('1')==maxcard]
        if not any(m and is_upset(profile,caps,m,full) for m in witnesses):
            raise AssertionError(('no nonempty maximum-cardinality upset minimizer',profile,gm,witnesses))
        stats['residual_violation_profiles']+=1
        if gm==0:
            stats['residual_zero_margin_cases']+=1
        else:
            stats['residual_negative_cases']+=1
    stats['residual_profiles']+=1


def main():
    stats={
        'schema':'exterior-slack-upset-reduction-verification-v1',
        'result':'PASS',
        'canonical_profiles':0,
        'canonical_nonempty_exterior':0,
        'canonical_exterior_subsets':0,
        'minimum_canonical_exterior_margin':10**9,
        'residual_profiles':0,
        'residual_violation_profiles':0,
        'residual_zero_margin_cases':0,
        'residual_negative_cases':0,
        'random_trials':0,
        'external_review':'OPEN'
    }

    # q<=c in the finite universe; target caps are deliberately varied.
    universe=[
        (0,0,0),(0,1,1),(0,2,2),
        (1,1,0),(1,2,1),(1,3,2),
        (2,2,1),(2,3,2),(2,4,3),
    ]

    # Exhaustive multiset profiles through four labelled vertices.
    for n in range(1,5):
        for prof in combinations_with_replacement(universe,n):
            canonical_check(list(prof),stats)
            residual_equivalence_check(list(prof),stats)

    # Broad deterministic random challenge, including more vertices/caps.
    rng=random.Random(742091404)
    for _ in range(1600):
        n=rng.randint(1,7)
        prof=[]
        for _ in range(n):
            q=rng.randint(0,3)
            c=rng.randint(q,min(6,q+3))
            P=rng.randint(0,min(5,n))
            prof.append((q,c,P))
        canonical_check(prof,stats)
        residual_equivalence_check(prof,stats)
        stats['random_trials']+=1

    if stats['minimum_canonical_exterior_margin']==10**9:
        stats['minimum_canonical_exterior_margin']=None
    stats['claims_checked']=[
        'union of labelled Hall minimizers is the unique maximal minimizer',
        'canonical labelled M+ is a sharp up-set and does not split identical types',
        'every nonempty labelled exterior set has residual-slack margin at least one',
        'residual-slack margin equals the canonical addition marginal exactly',
        'any nonempty residual margin <=0 exists iff a nonempty residual sharp up-set has margin <=0',
        'zero-margin violations still yield a nonempty maximum-cardinality sharp-upset minimizer'
    ]
    open('EXTERIOR_SLACK_UPSET_REDUCTION_VERIFICATION.json','w').write(json.dumps(stats,indent=2,sort_keys=True)+'\n')
    print(json.dumps(stats,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
