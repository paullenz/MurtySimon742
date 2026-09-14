"""Dependency-free replay and hostile tests for source pricing.

This verifies only the explicitly stated necessary projection, not graphs.
Numerical discovery is neither imported nor trusted. Run with Python 3.10+.
"""
from __future__ import annotations
import hashlib
import itertools as it
import json
from pathlib import Path
import random
from source_price_core import envelope, receiver_lower

HERE = Path(__file__).resolve().parent


def brute_upper(p, alpha, price, xi):
    """Enumerate column subsets, independently of DP and top-score sorting."""
    s,q,rho,P = (p[k] for k in ('s','q','rho','P'))
    a,b = len(s),len(q)
    eligible = [[u for u in range(b) if q[u]>0 and rho[u]>=s[i]] for i in range(a)]
    choices = [[tuple(u for j,u in enumerate(us) if mask>>j&1)
                for mask in range(1<<len(us)) if mask.bit_count()>=s[i]]
               for i,us in enumerate(eligible)]
    answer = None
    order = sorted(range(a),key=lambda i:(s[i],i))
    for cols in it.product(*choices):
        es = [len(cols[i])-s[i] for i in range(a)]
        if sum(es)!=p['Esel']: continue
        if any(sum(len(cols[i]) for i in order[:k]) <
               sum(max(0,q[u]-sum(s[i]<=rho[u] for i in order[k:])) for u in range(b))
               for k in range(1,a+1)):
            continue
        score = sum(q[u]*price[u] for u in range(b))
        for i,col in enumerate(cols):
            for u in col:
                score += (alpha[u]*min(es[i],max(0,P[u]-rho[u]+1)) if s[i]>xi else 0)-price[u]
        if answer is None or score>answer: answer=score
    return answer


def soundness_tests():
    count=0
    for b in range(1,4):
      for a in range(1,4):
        for bits in range(1<<(a*b)):
          X=[[bits>>(u*a+i)&1 for i in range(a)] for u in range(b)]
          q=[sum(row) for row in X]
          x=[sum(X[u][i] for u in range(b)) for i in range(a)]
          for st in it.product(*(range(v+1) for v in x)):
            s=list(st); es=[x[i]-s[i] for i in range(a)]
            rho=[max([1]+[s[i] for i in range(a) if X[u][i]]) for u in range(b)]
            D=[(count+u)%(b+1) for u in range(b)]
            P=[rho[u]-1+D[u] for u in range(b)]
            d=[min([D[u]]+[es[i] for i in range(a) if X[u][i] and s[i]>0]) for u in range(b)]
            alpha=[(count+2*u)%4 for u in range(b)]
            price=[(count+3*u)%7-3 for u in range(b)]
            xi=count%(max(s,default=0)+1)
            p={'s':s,'q':q,'rho':rho,'P':P,'Esel':sum(es)}
            actual=sum(alpha[u]*d[u] for u in range(b) for i in range(a) if X[u][i] and s[i]>xi)
            got=envelope(p,alpha,price,xi)
            assert got is not None and actual<=got['upper'], (p,actual,got)
            shifted=envelope(p,alpha,[v+5 for v in price],xi)
            assert shifted['upper']==got['upper']
            count+=1
    rng=random.Random(74220260920)
    comparisons=0
    for _ in range(1000):
        a,b=rng.randint(1,3),rng.randint(1,3)
        s=[rng.randrange(b+1) for _ in range(a)]
        q=[rng.randrange(a+1) for _ in range(b)]
        E=sum(q)-sum(s)
        if E<0: continue
        rho=[rng.randint(1,b+1) for _ in range(b)]
        P=[rho[u]-1+rng.randrange(b+1) for u in range(b)]
        alpha=[rng.randrange(4) for _ in range(b)]
        price=[rng.randint(-4,4) for _ in range(b)]
        xi=rng.randrange(b+1)
        p={'s':s,'q':q,'rho':rho,'P':P,'Esel':E}
        got=envelope(p,alpha,price,xi)
        actual=brute_upper(p,alpha,price,xi)
        assert (None if got is None else got['upper'])==actual
        comparisons+=1
    valid=0
    for attempt in range(10000):
        a,b=rng.randint(2,5),rng.randint(2,5)
        Y=[[0]*b for _ in range(b)]
        for u in range(b):
            for v in range(u+1,b):
                z=rng.randrange(3)
                if z==1: Y[u][v]=1
                if z==2: Y[v][u]=1
        q=[sum(y) for y in Y]
        incoming=[sum(Y[u][v] for u in range(b)) for v in range(b)]
        rho=[rng.randint(1,4) for _ in range(b)]
        if max(q)>a or any(Y[u][v] and not(q[u]<=q[v]+rho[v]+1 and q[v]<=q[u]+rho[u])
                          for u in range(b) for v in range(b)): continue
        X=[[int(i in chosen) for i in range(a)] for chosen in [set(rng.sample(range(a),v)) for v in q]]
        d=[max(0,incoming[u]-rho[u]+1) for u in range(b)]
        s=[]
        for i in range(a):
            users=[u for u in range(b) if X[u][i]]
            ceiling=min([len(users)-max([0]+[d[u] for u in users])]+[rho[u] for u in users])
            s.append(rng.randrange(max(0,ceiling)+1))
        es=[sum(X[u][i] for u in range(b))-s[i] for i in range(a)]
        assert all(not X[u][i] or s[i]==0 or d[u]<=es[i] for u in range(b) for i in range(a))
        P=[incoming[u]+rng.randrange(3) for u in range(b)]
        p={'s':s,'q':q,'rho':rho,'P':P,'Esel':sum(es)}
        alpha=[rng.randrange(4) for _ in range(b)]; xi=rng.randrange(max(s)+1)
        actual=sum(alpha[u]*d[u] for u in range(b) for i in range(a) if X[u][i] and s[i]>xi)
        low=receiver_lower(p,alpha,xi)
        assert not low.get('capacity_impossible') and low['lower']<=actual
        valid+=1
        if valid==1000: break
    assert valid==1000
    toy={'s':[1,1],'q':[1,1,2],'rho':[1,1,1],'P':[1,0,0],'Esel':2}
    zero=envelope(toy,[1,1,1],[0,0,0])['upper']
    priced=envelope(toy,[1,1,1],[1,0,0])['upper']
    assert (zero,priced)==(2,1)
    # Omitting the uncharged column's price would falsely produce -1 here.
    hostile={'s':[0],'q':[1],'rho':[1],'P':[1],'Esel':1}
    assert envelope(hostile,[1],[-1])['upper']==0
    return {'exhaustive_incidence_configs':count,'gauge_checks':count,
            'independent_column_enumerations':comparisons,
            'valid_oriented_incidence_lower_checks':valid,
            'oriented_trials':attempt+1,'toy_zero_upper':zero,'toy_priced_upper':priced,
            'uncharged_negative_price_fixture':'PASS'}


def replay():
    inp=json.loads((HERE/'inputs.json').read_text())
    rows={p['row']:p for p in inp['rows']}
    records=json.loads((HERE/'BEST_PRICES.json').read_text())['records']
    checked=[]
    for rec in records:
        p=rows[rec['row']]
        assert len(p['s'])==p['a'] and len(p['q'])==len(p['rho'])==len(p['P'])==p['b']
        assert sum(p['s'])==sum(p['rho'])+2*p['t']+p['D0']
        scale=rec['scale']; mode=rec['mode']; xi=rec['xi']
        alpha=[scale*(1 if mode==0 or v<=2 else 3) for v in p['q']]
        zero=envelope(p,alpha,[0]*p['b'],xi)
        got=envelope(p,alpha,rec['price'],xi)
        low=receiver_lower(p,alpha,xi)
        assert zero['upper']==rec['zero_upper'] and got['upper']==rec['upper']
        assert low['lower']==rec['lower']
        checked.append({'row':p['row'],'mode':mode,'xi':xi,'scale':scale,
                        'zero_upper':zero['upper'],'upper':got['upper'],'lower':low['lower'],
                        'strict_contradiction':low['lower']>got['upper']})
    return checked


if __name__=='__main__':
    out={'schema':'source-pricing-verified-v1','tests':soundness_tests(),'replay':replay()}
    out['profile_exclusions']=sorted({r['row'] for r in out['replay'] if r['strict_contradiction']})
    out['scope']='Necessary selected-incidence/receiver projection only; external review OPEN; canonical frontier unchanged.'
    print(json.dumps(out,sort_keys=True,indent=2))
