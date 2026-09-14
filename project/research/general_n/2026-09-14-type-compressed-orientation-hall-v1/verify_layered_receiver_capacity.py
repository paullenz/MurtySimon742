#!/usr/bin/env python3
from pathlib import Path
import json, random

SEED=742091403
OUT=Path(__file__).resolve().parent/'LAYERED_RECEIVER_CAPACITY_VERIFICATION.json'

def check_layers(P,Y):
    m=max(P+Y+[0])
    exact=sum(min(p,y) for p,y in zip(P,Y))
    layer=sum(sum(1 for p,y in zip(P,Y) if p>=k and y>=k) for k in range(1,m+1))
    upper=sum(min(sum(p>=k for p in P),sum(y>=k for y in Y)) for k in range(1,m+1))
    sorted_upper=sum(min(p,y) for p,y in zip(sorted(P,reverse=True),sorted(Y,reverse=True)))
    assert exact==layer<=upper==sorted_upper
    return exact,upper

def main():
    rng=random.Random(SEED)
    stats={'arbitrary_trials':0,'murty_like_trials':0,'strict_comonotone_loss':0}
    for _ in range(5000):
        b=rng.randint(1,12)
        P=[rng.randint(0,10) for _ in range(b)]
        Y=[rng.randint(0,10) for _ in range(b)]
        check_layers(P,Y); stats['arbitrary_trials']+=1
    for _ in range(10000):
        b=rng.randint(3,9); a=rng.randint(2,8)
        rho=[rng.randint(1,a) for _ in range(b)]
        q=[rng.randint(0,a-rho[i]) for i in range(b)]
        c=[q[i]+rho[i] for i in range(b)]
        P=[]
        for i in range(b):
            cap=max(0,min(b-1-q[i],rho[i]+b-a-1))
            P.append(rng.randint(0,cap))
        sel=[bool(rng.getrandbits(1)) for _ in range(b)]
        Y=[]
        for w in range(b):
            Y.append(sum(1 for u in range(b) if sel[u] and u!=w and q[u]<=c[w]+1 and q[w]<=c[u]))
        exact,upper=check_layers(P,Y)
        stats['strict_comonotone_loss']+=int(exact<upper)
        r=sum(rho); totalY=sum(Y); scalar=0
        for k in range(1,b):
            alpha=sum(p>=k for p in P)
            L=sum(x<=b-1-k for x in q)
            if a-b+k<=0: R=b
            else: R=min(b,(r-b)//(a-b+k))
            assert alpha<=min(L,R)
            scalar+=min(L,R,min(b,totalY//k))
        assert exact<=scalar
        stats['murty_like_trials']+=1
    report={'schema':'layered-receiver-capacity-verification-v1','result':'PASS','seed':SEED,**stats,'external_review':'OPEN'}
    OUT.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__': main()
