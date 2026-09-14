#!/usr/bin/env python3
"""Independent finite audit for SHARP_DOMINANCE_UPSET_HALL.md."""
from itertools import combinations_with_replacement
from pathlib import Path
import json
import random

SEED=7420914


def compatible(u,w):
    qu,cu,_=u; qw,cw,_=w
    return qu<=cw+1 and qw<=cu


def dominates(x,y):
    qx,cx,px=x; qy,cy,py=y
    return cx<=cy and (qx>qy or (qx==qy and px>=py))


def interval_compatible(u,w):
    qu,cu,_=u; qw,cw,_=w
    return max(qu,qw)<=min(cu,cw+1)


def build_D(p):
    n=len(p)
    return [[i!=j and compatible(p[i],p[j]) for j in range(n)] for i in range(n)]


def margin(p,D,m):
    n=len(p); total=0
    for w in range(n):
        inc=sum(1 for u in range(n) if (m>>u)&1 and D[u][w])
        total+=min(p[w][2],inc)
    total-=sum(p[u][0] for u in range(n) if (m>>u)&1)
    return total


def is_upset(p,m):
    n=len(p)
    for y in range(n):
        if not ((m>>y)&1): continue
        for x in range(n):
            if x!=y and dominates(p[x],p[y]) and not ((m>>x)&1):
                return False
    return True


def audit_profile(p,c):
    n=len(p); D=build_D(p)
    for u in range(n):
        for w in range(n):
            assert compatible(p[u],p[w])==interval_compatible(p[u],p[w])
            c['interval_checks']+=1
    vals=[margin(p,D,m) for m in range(1<<n)]
    c['margin_evaluations']+=1<<n
    for S in range(1<<n):
        miss=[x for x in range(n) if not ((S>>x)&1)]
        for ai in range(len(miss)):
            a=miss[ai]
            for bi in range(ai+1,len(miss)):
                b=miss[bi]
                assert vals[S|1<<a]+vals[S|1<<b]>=vals[S]+vals[S|1<<a|1<<b]
                c['submodularity_checks']+=1
    for x in range(n):
        for y in range(n):
            if x==y or not dominates(p[x],p[y]): continue
            bits=[z for z in range(n) if z not in (x,y)]
            for sm in range(1<<len(bits)):
                T=sum(1<<z for j,z in enumerate(bits) if (sm>>j)&1)
                dx=vals[T|1<<x]-vals[T]
                dy=vals[T|1<<y]-vals[T]
                assert dx<=dy
                c['exchange_checks']+=1
                if p[x][0]>=p[y][0]+2:
                    assert dx<=dy-1
                    c['strict_gap_checks']+=1
    mn=min(vals)
    mins=[m for m,v in enumerate(vals) if v==mn]
    max_card=max(m.bit_count() for m in mins)
    maxmins=[m for m in mins if m.bit_count()==max_card]
    assert all(is_upset(p,m) for m in maxmins)
    assert min(vals[m] for m in range(1<<n) if is_upset(p,m))==mn
    c['profiles']+=1
    c['profiles_with_negative_margin']+=int(mn<0)
    c['max_cardinality_minimizers']+=len(maxmins)
    c['upset_sets_checked']+=sum(is_upset(p,m) for m in range(1<<n))


def main():
    c={k:0 for k in [
        'profiles','profiles_with_negative_margin','interval_checks','margin_evaluations',
        'submodularity_checks','exchange_checks','strict_gap_checks',
        'max_cardinality_minimizers','upset_sets_checked']}
    universe=[
        (0,0,0),(0,1,1),(1,1,0),(1,2,1),
        (1,3,2),(2,2,1),(2,3,0),(2,4,2),
    ]
    exhaustive=0
    for n in range(1,6):
        for p in combinations_with_replacement(universe,n):
            audit_profile(p,c); exhaustive+=1
    rng=random.Random(SEED)
    random_profiles=3000
    for _ in range(random_profiles):
        n=rng.randint(1,8); p=[]
        for __ in range(n):
            q=rng.randint(0,6); rho=rng.randint(0,6); P=rng.randint(0,8)
            p.append((q,q+rho,P))
        audit_profile(tuple(p),c)
    report={
        'schema':'sharp-dominance-upset-hall-verification-v1',
        'result':'PASS',
        'seed':SEED,
        'exhaustive_profiles':exhaustive,
        'random_profiles':random_profiles,
        **c,
        'claims_checked':[
            'interval identity',
            'Hall-margin submodularity',
            'sharp exchange inequality',
            'strict demand-gap exchange',
            'maximum-cardinality minimizers are sharp hardness up-sets',
            'unrestricted minimum equals minimum over sharp hardness up-sets',
        ],
        'external_review':'OPEN',
        'note':'Independent finite arithmetic audit; not independent mathematical review of the Murty-Simon bridge.',
    }
    Path('SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
