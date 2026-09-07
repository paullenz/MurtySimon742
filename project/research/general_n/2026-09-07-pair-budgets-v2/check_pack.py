#!/usr/bin/env python3
"""Standalone exact checker. Imports no search source and no third-party module.

Checks the fixed-profile evidence, not universal graph lemmas or order coverage.
"""
from pathlib import Path
import json,copy
from itertools import combinations


def derive(p):
    a,b,t=p['a'],p['b'],p['t'];d=p['d'];R=p['R'];rho=p['rho']
    assert len(d)==len(R)==a and len(rho)==b
    assert all(type(z) is int for z in [a,b,t]+d+R+rho)
    assert t>0 and all(0<=z<a for z in d) and all(0<=z<=b for z in R) and all(1<=z<=a for z in rho)
    r=sum(rho);assert sum(R)==r and sum(d)==2*(r+t)
    s=[max(0,x-y) for x,y in zip(d,R)];c=[]
    for u in range(b):
        suppliers=[rho[u]+rho[w] for w in range(b) if w!=u]
        feasible=[0]
        for q in range(1,min(a-rho[u],b-1)+1):
            labels=[d[i] for i in range(a) if d[i]<=rho[u]+q-1 and d[i]<=rho[u]+R[i]]
            upper=min([len(labels),len(suppliers)]+[
                sum(z<j for z in labels)+sum(z>=j for z in suppliers) for j in set(labels)])
            if upper>=q:feasible.append(q)
        c.append(max(feasible))
    while True:
        nxt=[max(q for q in range(c[u]+1) if sum(w!=u and rho[w]+c[w]>=q-1 for w in range(b))>=q) for u in range(b)]
        if nxt==c:break
        c=nxt
    elig=[{u for u in range(b) if d[i]<=rho[u]+c[u]-1 and d[i]<=rho[u]+R[i]} for i in range(a)]
    assert all(s[i]<=len(elig[i]) for i in range(a))
    f=[sum(s[i]>0 and s[i]==len(elig[i]) and u in elig[i] for i in range(a)) for u in range(b)]
    assert all(f[u]<=c[u] for u in range(b))
    pc=[min(b-1,rho[u]+b-a-1) for u in range(b)];assert min(pc)>=0
    triples=set()
    for i in range(a):
        for u in elig[i]:
            lo=max(1,f[u],d[i]-rho[u]+1)
            if lo>c[u]:continue
            for w in range(b):
                if u!=w and d[i]<=rho[u]+rho[w] and rho[w]+c[w]>=lo-1:
                    triples.add((i,u,w))
    pairs={tuple(sorted((u,w))) for i,u,w in triples}
    return a,b,d,R,rho,s,c,elig,pc,triples,pairs


def capacity(data,key):
    a,b,d,R,rho,s,c,elig,pc,triples,pairs=data
    kind=key[0]
    if kind=='source' and len(key)==2 and 0<=key[1]<b:return c[key[1]]
    if kind=='supplement' and len(key)==2 and 0<=key[1]<b:return pc[key[1]]
    if kind=='source_label' and len(key)==3 and 0<=key[1]<a and key[2] in elig[key[1]]:return 1
    if kind=='pair' and len(key)==3 and tuple(key[1:]) in pairs:return 1
    raise ValueError('unknown resource')


def verify_support(p,cert):
    a,b,d,R,rho,s,c,elig,pc,triples,pairs=derive(p)
    I=cert['labels'];assert len(I)==len(set(I)) and all(0<=i<a for i in I)
    W=sorted({w for i,u,w in triples if i in set(I)})
    assert cert['kind']=='supplement_support' and cert['W']==W
    assert cert['lhs']==sum(s[i] for i in I)>sum(pc[w] for w in W)==cert['rhs']


def verify_weighted(p,cert):
    data=derive(p);a,b,d,R,rho,s,c,elig,pc,triples,pairs=data
    y=cert['label_weights'];assert len(y)==a and all(type(z) is int and z>=0 for z in y)
    weights={}
    for rec in cert['resource_weights']:
        key=tuple(rec['resource']);w=rec['weight'];capacity(data,key)
        assert key not in weights and type(w) is int and w>=0
        weights[key]=w
    for i,u,w in triples:
        cover=weights.get(('source',u),0)+weights.get(('supplement',w),0)+weights.get(('source_label',i,u),0)+weights.get(('pair',min(u,w),max(u,w)),0)
        assert cover>=y[i]
    assert sum(y[i]*s[i] for i in range(a))>sum(capacity(data,k)*w for k,w in weights.items())


def degree_setup(p):
    data=derive(p);a,b,d,R,rho,s,c,elig,pc,triples,pairs=data
    W={w for i,u,w in triples};pc=[pc[u] if u in W else 0 for u in range(b)]
    deg=[sum(u in pair for pair in pairs) for u in range(b)]
    low=sum(s);high=min(sum(c),len(pairs),sum(pc),sum(min(b-R[i],len(elig[i])) for i in range(a)))
    return low,high,max(max(x,y) for x,y in zip(d,R)),c,pc,deg


def degree_caps(E,D0,c,pc,deg):
    out=[]
    for u in range(len(c)):
        possibilities=[]
        for sigma in range(deg[u]+1):
            if sigma>c[u]+pc[u]:continue
            required=max(0,sigma-pc[u])
            if sigma>D0 and required*(sigma-D0)>E:continue
            possibilities.append(sigma)
        out.append(max(possibilities))
    return out


def verify_closure(p,cert):
    low,high,D0,c,pc,deg=degree_setup(p)
    assert (cert['Qmin'],cert['Qupper_initial'],cert['D0'])==(low,high,D0)
    for row in cert['rounds']:
        assert high>=low and row['Qupper_before']==high and row['excess_upper']==high-low
        caps=degree_caps(high-low,D0,c,pc,deg)
        nxt=min(high,sum(caps)//2)
        assert row['degree_caps']==caps and row['Qupper_after']==nxt and nxt<high
        high=nxt
    assert cert['Qupper_final']==high<low


def verify_Q_rows(p,cert):
    low,high,D0,c,pc,deg=degree_setup(p)
    assert (cert['Qmin'],cert['Qmax'],cert['D0'])==(low,high,D0)
    assert [row['Q'] for row in cert['rows']]==list(range(low,high+1))
    for row in cert['rows']:
        Q=row['Q'];caps=degree_caps(Q-low,D0,c,pc,deg)
        assert row['excess']==Q-low and row['degree_caps']==caps
        assert row['lhs']==2*Q>sum(caps)==row['rhs']


def verify_witness(p,cert):
    data=derive(p);a,b,d,R,rho,s,c,elig,pc,triples,pairs=data
    selected=[tuple(z) for z in cert['selected']]
    assert len(selected)==len(set(selected)) and all(z in triples for z in selected)
    use={};need=[0]*a
    for i,u,w in selected:
        need[i]+=1
        for key in [('source',u),('supplement',w),('source_label',i,u),('pair',min(u,w),max(u,w))]:
            use[key]=use.get(key,0)+1
    assert need==s and all(cnt<=capacity(data,k) for k,cnt in use.items())


def main():
    root=Path(__file__).resolve().parent
    result=json.loads((root/'EXPERIMENTS.json').read_text());ncert=0
    for rec in result['results']:
        p=rec['profile']
        for field,check in [('support_certificate',verify_support),('weighted_certificate',verify_weighted),
                ('degree_closure_certificate',verify_closure),('degree_budget_certificate',verify_Q_rows)]:
            if rec.get(field):check(p,rec[field]);ncert+=1
        if rec.get('integer_witness',{}).get('status')=='RELAXATION_WITNESS':
            verify_witness(p,rec['integer_witness']);ncert+=1
    # Deliberately damaged outputs must fail the standalone checker.
    mutated=0
    rec=result['results'][0];bad=copy.deepcopy(rec['support_certificate']);bad['rhs']+=1
    try:verify_support(rec['profile'],bad)
    except AssertionError:mutated+=1
    else:raise AssertionError('damaged support certificate accepted')
    rec=result['results'][1];bad=copy.deepcopy(rec['degree_closure_certificate']);bad['Qupper_final']-=1
    try:verify_closure(rec['profile'],bad)
    except AssertionError:mutated+=1
    else:raise AssertionError('damaged closure certificate accepted')
    bad=copy.deepcopy(rec['integer_witness']);bad['selected'].append(bad['selected'][0])
    try:verify_witness(rec['profile'],bad)
    except AssertionError:mutated+=1
    else:raise AssertionError('duplicate selected pair accepted')
    out=dict(status='PASS',certificate_or_witness_checks=ncert,deliberate_mutations_rejected=mutated,
       imports_search_source=False,uses_third_party_modules=False,
       scope='Two explicit profiles, not a graph-order sweep. Same-assistant checker, not external review.')
    (root/'CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
