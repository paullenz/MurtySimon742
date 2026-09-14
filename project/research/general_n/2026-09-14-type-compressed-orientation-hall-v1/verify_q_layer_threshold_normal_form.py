#!/usr/bin/env python3
"""Independent finite verification of Q_LAYER_THRESHOLD_NORMAL_FORM.md.

The verifier compares the direct q-stratified layer definition with the
order-statistic / c-tail formula.  It does not import scanner code.
"""
from __future__ import annotations

import itertools
import json
import math
import random
from pathlib import Path

HERE=Path(__file__).resolve().parent
OUT=HERE/'Q_LAYER_THRESHOLD_NORMAL_FORM_VERIFICATION.json'


def incoming(S, types, w):
    qw,cw,_=types[w]
    return sum(
        1 for u in S
        if u!=w and types[u][0]<=cw+1 and qw<=types[u][1]
    )


def direct_terms(S, types):
    S=set(S)
    ans={}
    for q in sorted({x[0] for x in types}):
        W=[w for w,x in enumerate(types) if x[0]==q]
        ymax=max([incoming(S,types,w) for w in W]+[0])
        pmax=max([types[w][2] for w in W]+[0])
        for k in range(1,max(ymax,pmax)+1):
            alpha=sum(types[w][2]>=k for w in W)
            beta=sum(incoming(S,types,w)>=k for w in W)
            ans[(q,k)]=(alpha,beta,min(alpha,beta))
    return ans


def threshold_terms(S, types):
    S=set(S)
    ans={}
    for q in sorted({x[0] for x in types}):
        W=[w for w,x in enumerate(types) if x[0]==q]
        active=sorted(types[u][0] for u in S if types[u][1]>=q)
        ymax=max([incoming(S,types,w) for w in W]+[0])
        pmax=max([types[w][2] for w in W]+[0])
        for k in range(1,max(ymax,pmax)+1):
            # cap side: fixed-q monotonicity makes P>=k a c-suffix
            eligible=[types[w][1] for w in W if types[w][2]>=k]
            if eligible:
                theta=min(eligible)
                alpha=sum(types[w][1]>=theta for w in W)
            else:
                alpha=0

            rk=active[k-1] if len(active)>=k else math.inf
            rk1=active[k] if len(active)>=k+1 else math.inf
            beta=(
                sum(w not in S and types[w][1]>=rk-1 for w in W)
                +sum(w in S and types[w][1]>=rk1-1 for w in W)
            )
            ans[(q,k)]=(alpha,beta,min(alpha,beta))
    return ans


def fixed_q_monotone(types):
    for i,x in enumerate(types):
        for j,y in enumerate(types):
            if x[0]==y[0] and x[1]<=y[1] and x[2]>y[2]:
                return False
    return True


def check_profile(types):
    n=len(types)
    for mask in range(1<<n):
        S={i for i in range(n) if (mask>>i)&1}
        a=direct_terms(S,types)
        b=threshold_terms(S,types)
        if a!=b:
            raise AssertionError({
                'types':types,
                'source_set':sorted(S),
                'direct':a,
                'threshold':b,
            })
    return 1<<n


def cap_functions():
    # q=0 at c=0,1,2; q=1 at c=1,2; P in 0,1,2.
    s0=[x for x in itertools.product(range(3),repeat=3)
        if x[0]<=x[1]<=x[2]]
    s1=[x for x in itertools.product(range(3),repeat=2)
        if x[0]<=x[1]]
    out=[]
    for a in s0:
        for b in s1:
            out.append({
                (0,0):a[0],(0,1):a[1],(0,2):a[2],
                (1,1):b[0],(1,2):b[1],
            })
    return out


def exhaustive():
    alphabet=[(0,0),(0,1),(0,2),(1,1),(1,2)]
    funcs=cap_functions()
    profiles=source_sets=0
    for n in range(1,5):
        for qc in itertools.product(alphabet,repeat=n):
            for f in funcs:
                types=[(q,c,f[(q,c)]) for q,c in qc]
                if not fixed_q_monotone(types):
                    raise AssertionError('generated non-monotone profile')
                profiles+=1
                source_sets+=check_profile(types)
    return profiles,source_sets


def random_phase():
    rng=random.Random(74220260914)
    trials=30000
    max_n=10
    for _ in range(trials):
        n=rng.randint(1,max_n)
        funcs={}
        for q in range(5):
            cur=0; d={}
            for c in range(q,7):
                cur=rng.randint(cur,6)
                d[c]=cur
            funcs[q]=d
        types=[]
        for _ in range(n):
            q=rng.randint(0,4)
            c=rng.randint(q,6)
            types.append((q,c,funcs[q][c]))
        if not fixed_q_monotone(types):
            raise AssertionError('random monotonicity failure')
        mask=rng.randrange(1<<n)
        S={i for i in range(n) if (mask>>i)&1}
        if direct_terms(S,types)!=threshold_terms(S,types):
            raise AssertionError({'types':types,'source_set':sorted(S)})
    return trials,max_n


def main():
    profiles,source_sets=exhaustive()
    trials,max_n=random_phase()
    result={
        'schema':'q-layer-threshold-normal-form-verification-v1',
        'exhaustive_labelled_profiles':profiles,
        'exhaustive_source_sets':source_sets,
        'exhaustive_q_values':[0,1],
        'exhaustive_c_rule':'q..2',
        'exhaustive_P_values':[0,1,2],
        'fixed_q_cap_monotonicity':True,
        'random_trials':trials,
        'random_maximum_n':max_n,
        'random_seed':74220260914,
        'result':'PASS',
        'promotion_status':'INTERNAL_ARITHMETIC_SUPPORT_ONLY',
        'external_review':'OPEN',
    }
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
