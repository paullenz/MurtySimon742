#!/usr/bin/env python3
"""Combinatorial verifier. No model-builder, NumPy or solver imports."""
from collections import Counter

def verify_objects(rec,mode,selected,residual,arcs):
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho']
    assert len(selected)==len(set(selected)) and len(residual)==len(set(residual)) and len(arcs)==len(set(arcs))
    selected=set(selected);residual=set(residual);arcs=set(arcs)
    assert all(0<=u<b and 0<=i<a for u,i in selected|residual)
    assert not selected&residual
    assert all(0<=u<b and 0<=v<b and u!=v and 0<=i<a for u,i,v in arcs)
    assert {(u,i) for u,i,v in arcs}==selected and len(arcs)==len(selected)
    assert len({tuple(sorted((u,v))) for u,i,v in arcs})==len(arcs)
    S=[{i for w,i in selected if w==u} for u in range(b)]
    N=[{i for w,i in selected|residual if w==u} for u in range(b)]
    q=[len(v) for v in S];p=[sum(w==v for u,i,w in arcs) for v in range(b)]
    assert [sum(w==u for w,i in residual) for u in range(b)]==rho
    assert all(s[i]<=rho[u] for u,i in selected)
    x=[sum(i in labels for labels in S) for i in range(a)]
    degree=[sum(i in labels for labels in N) for i in range(a)]
    assert all(x[i]>=s[i] for i in range(a))
    assert all(q[u]+rho[u]<=a and p[u]<=rho[u]+b-a-1 and q[u]+p[u]<=b-1 for u in range(b))
    assert all(degree[i]>=q[u]+p[u] for u,i in selected)
    assert all(rho[v]+q[v]>=q[u]-1 for u,i,v in arcs)
    for h in range(1,max(s,default=0)+1):
        heavy=[sum(s[i]>=h for i in labels) for labels in S]
        assert all(rho[v]>=h for u,i,v in arcs if s[i]>=h and heavy[u]>h)
    if mode=='label_compatible':
        for u,i,v in arcs:
            assert i not in N[v]
            missing={w for t,k,w in arcs if t==u}|{t for t,k,w in arcs if w==u}
            assert all(i in N[w] for w in missing-{v})
        # The receiver conflict lemma, checked independently of the row encoding.
        for v in range(b):
            incoming={i for u,i,w in arcs if w==v}
            assert not incoming&N[v]
            assert len(incoming)<=a-rho[v]-q[v]
            for u,i,w in arcs:
                if w==v:assert S[u]&incoming=={i}
    return dict(selected_arcs=len(arcs),residual_incidences=len(residual),q=q,p=p,
                label_selected_degrees=x,label_cross_degrees=degree,
                incoming_distinct_labels=[len({i for u,i,w in arcs if w==v}) for v in range(b)])

def verify_vector(model,vector):
    assert len(vector)==len(model['variables']) and all(type(v) is int for v in vector)
    assert all(lo<=v<=hi for v,lo,hi in zip(vector,model['lower_bounds'],model['upper_bounds']))
    for row in model['rows']:
        value=sum(c*vector[j] for j,c in row['terms'])
        assert row['lower'] is None or value>=row['lower'],row['name']
        assert row['upper'] is None or value<=row['upper'],row['name']
    selected=[];residual=[];arcs=[]
    for name,value in zip(model['variables'],vector):
        if name[0] in ('x','r','z'):
            assert value in (0,1)
            if value:{'x':selected,'r':residual,'z':arcs}[name[0]].append(tuple(name[1:]))
    result=verify_objects(model['record'],model['mode'],selected,residual,arcs)
    return dict(status='PASS',linear_rows_checked=len(model['rows']),**result)

def extract(model,raw):
    if raw is None:return None
    vector=[round(v) for v in raw]
    if any(abs(v-w)>1e-5 for v,w in zip(raw,vector)):return dict(status='REJECTED_NONINTEGER')
    try:check=verify_vector(model,vector)
    except AssertionError as exc:return dict(status='REJECTED_EXACT_CHECK',error=str(exc))
    return dict(status='VERIFIED_RELAXATION_WITNESS',integer_vector=vector,check=check)
