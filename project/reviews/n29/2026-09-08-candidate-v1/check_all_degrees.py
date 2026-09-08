#!/usr/bin/env python3
"""Exact arithmetic audit for the non-Delta16 pieces of the n=29 candidate.
Standard library only. It checks arithmetic consequences of written lemmas; it
is not a proof of the external Fan/Dailly theorems or the graph lemmas.
"""
from fractions import Fraction as Q
from math import comb
import json

n=29; target=n*n//4
assert target==210
# Fan bound as quoted by Wang: n^2/4 + (n^2-(81/5)n+56)/320.
fan=Q(n*n,4)+Q(n*n-Q(81,5)*n+56,320)
assert fan==Q(42317,200) and 211<fan<212

# Witness count at Delta=15. T=n Delta-2m and 2h+o<=T.
def witness_table(m):
    T=n*15-2*m
    rows=[]
    for h in range(T//2+1):
        o=T-2*h
        bound=comb(h,2)+h*(n-h)+2*comb(o,2)
        rows.append({'h':h,'o_max':o,'bound':bound})
    return T,rows
T211,w211=witness_table(211)
T210,w210=witness_table(210)
assert T211==13 and max(x['bound'] for x in w211)==156<211
assert T210==15 and max(x['bound'] for x in w210)==210
assert [x for x in w210 if x['bound']==210]==[{'h':0,'o_max':15,'bound':210}]
# Sharper equality count: 210 <= 210-e(O), hence e(O)=0.
assert 2*comb(15,2)==210

# Delta=17 pointwise charging score on a=11 labels.
score=[]
for s in range(11):
    v=Q(s*(12-2*s),11-s)
    assert v<=Q(16,7)
    # exact factorization of 16/7-v
    assert Q(16,7)-v == Q(2*(s-4)*(7*s-22),7*(11-s))
    score.append([s,str(v)])
assert 11*Q(16,7)==Q(176,7)
for m,t in [(210,6),(211,7)]:
    required=17+2*t
    assert required>Q(176,7)

# Delta >=18 h-index inequality b+2t <= floor((29-b)^2/4) is violated.
hindex=[]
for m in (210,211):
    for b in range(18,28):
        t=m-b*(n-b)
        lhs=b+2*t;rhs=(n-b)**2//4
        assert t>0 and lhs>rhs
        hindex.append({'m':m,'Delta':b,'t':t,'lhs':lhs,'rhs':rhs})

# Delta<=14 degree sum.
assert n*14//2==203<210

# Exact K(14,15) boundary graph check, including edge criticality.
A=range(14);B=range(14,29)
adj=[set() for _ in range(n)]
for u in A:
    for v in B:adj[u].add(v);adj[v].add(u)
def distance_le_two(graph,u,v):
    return u==v or v in graph[u] or bool(graph[u]&graph[v])
assert sum(len(x) for x in adj)//2==210
assert max(len(x) for x in adj)==15
assert all(distance_le_two(adj,u,v) for u in range(n) for v in range(n))
for u in A:
    for v in B:
        g=[set(x) for x in adj];g[u].remove(v);g[v].remove(u)
        assert not distance_le_two(g,u,v)

result={
 'status':'PASS','n':29,'target':210,'fan_strict_bound':str(fan),
 'delta15_m211':{'T':T211,'table':w211,'maximum_bound':156},
 'delta15_m210':{'T':T210,'table':w210,'unique_coarse_equality':{'h':0,'o':15},'sharper_eO_forced':0},
 'delta17_scores':score,'delta17_max_total':str(Q(176,7)),
 'hindex_cases':hindex,'delta_le_14_max':203,
 'K14_15_exact_graph_check':'PASS',
 'scope':'Arithmetic and explicit K(14,15) check only; Delta16 is separate finite replay; external and universal lemmas are hand/external inputs.'
}
print(json.dumps(result,indent=2))
