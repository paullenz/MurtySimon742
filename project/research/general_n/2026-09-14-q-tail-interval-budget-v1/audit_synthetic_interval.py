#!/usr/bin/env python3
"""Independent BFS augmenting-path checks on synthetic bridge RELAXATIONS."""
import csv,json,collections
from pathlib import Path
from verify_interval_budget import check,directed,target_caps
ROOT=Path(__file__).parent

class Flow:
    def __init__(self,n):self.c=[{} for _ in range(n)];self.original={}
    def add(self,u,v,k):
        self.c[u][v]=self.c[u].get(v,0)+k;self.c[v].setdefault(u,0)
        self.original[(u,v)]=self.original.get((u,v),0)+k
    def solve(self,s,t):
        value=0
        while True:
            prev={s:None};queue=collections.deque([s])
            while queue and t not in prev:
                u=queue.popleft()
                for v,k in self.c[u].items():
                    if k>0 and v not in prev:prev[v]=u;queue.append(v)
            if t not in prev:return value
            v=t;amount=10**9
            while v!=s:amount=min(amount,self.c[prev[v]][v]);v=prev[v]
            v=t
            while v!=s:u=prev[v];self.c[u][v]-=amount;self.c[v][u]+=amount;v=u
            value+=amount

def incidence(q,rho,s):
    b=len(q);a=len(s);S=b+a;T=S+1;SS=T+1;TT=SS+1
    F=Flow(TT+1);balance=[0]*(TT+1)
    def edge(u,v,lo,hi):
        if hi<lo:raise ValueError('impossible lower bound')
        F.add(u,v,hi-lo);balance[u]-=lo;balance[v]+=lo
    for u in range(b):
        edge(S,u,q[u],q[u])
        for i in range(a):
            if s[i]<=rho[u]:edge(u,b+i,0,1)
    for i in range(a):edge(b+i,T,s[i],b)
    edge(T,S,0,sum(q));need=0
    for v in range(T+1):
        if balance[v]>0:F.add(SS,v,balance[v]);need+=balance[v]
        elif balance[v]<0:F.add(v,TT,-balance[v])
    if F.solve(SS,TT)!=need:return None
    labels=[[i for i in range(a) if (u,b+i) in F.original and F.original[(u,b+i)]-F.c[u][b+i]==1] for u in range(b)]
    assert all(len(labels[u])==q[u] for u in range(b))
    assert all(sum(i in row for row in labels)>=s[i] for i in range(a))
    return labels

def target(q,rho,P):
    b=len(q);S=2*b;T=S+1;F=Flow(T+1);D=directed(q,rho)
    for u in range(b):
        F.add(S,u,q[u]);F.add(b+u,T,P[u])
        for w in range(b):
            if D[u][w]:F.add(u,b+w,1)
    value=F.solve(S,T)
    arcs=[(u,w) for u in range(b) for w in range(b) if D[u][w] and F.c[u][b+w]==0]
    return value,arcs

def pair(q,rho):
    b=len(q);D=directed(q,rho);edges=[(u,w) for u in range(b) for w in range(u+1,b) if D[u][w] or D[w][u]]
    S=b+len(edges);T=S+1;F=Flow(T+1)
    for u in range(b):F.add(S,u,q[u])
    for k,(u,w) in enumerate(edges):
        p=b+k;F.add(p,T,1)
        if D[u][w]:F.add(u,p,1)
        if D[w][u]:F.add(w,p,1)
    return F.solve(S,T)

def main():
    counts=collections.Counter();positive_example=None;hallpass_example=None
    for raw in csv.DictReader((ROOT/'SYNTHETIC_INTERVAL_PROFILES.tsv').open(),delimiter='\t'):
        row={k:([int(x) for x in v.split(',')] if k in ('q','rho','s','P') else int(v)) for k,v in raw.items()}
        q,rho,s,P=[row[k] for k in ('q','rho','s','P')]
        assert row['z']==s.count(0) and len(s)==row['a'] and len(q)==row['b']
        assert target_caps(row['a'],q,rho,row['Esel'],row['z'])==P
        assert sum(q)==sum(s)+row['Esel']
        assert sum(s)==sum(rho)+2*row['t']+row['D0']
        assert all(q[u]+rho[u]<=row['a'] and rho[u]>=1 for u in range(len(q)))
        assert row['D0']>=0 and row['t']>0 and sum(rho)+row['t']<=row['a']*(row['a']-1)//2
        labels=incidence(q,rho,s);assert labels is not None
        assert pair(q,rho)==sum(q)
        flow,arcs=target(q,rho,P);assert (flow<sum(q))==bool(row['Hall_fail'])
        result=check(q,rho,P,row['a'],row['t'],row['D0'],row['Esel'])
        assert max(r['deficiency'] for r in result['rows'])==row['best_tail']
        assert max(r['interval_lower'] for r in result['rows'])==row['best_interval']
        counts['profiles']+=1;counts['D0_positive']+=row['D0']>0;counts['zero_demand_profiles']+=row['z']>0
        counts['Hall_failures']+=row['Hall_fail'];counts['interval_detections']+=row['best_interval']>0
        if row['D0']>0 and positive_example is None:positive_example=dict(profile=row,selected_labels=labels,result=result)
        if not row['Hall_fail'] and hallpass_example is None:
            hallpass_example=dict(profile=row,selected_labels=labels,target_arcs=arcs,result=result,
                                  warning='Separate selected-incidence and target-flow certificates; no joint graph realization is asserted.')
    result=dict(status='PASS',counts=dict(counts),first_positive_D0_example=positive_example,
                first_Hall_pass_example=hallpass_example,
                scope='Specified scalar/selected-incidence/pair-flow relaxation only; F-graph, residual columns and full quasi-edge forcing not imposed')
    (ROOT/'SYNTHETIC_INTERVAL_INDEPENDENT_AUDIT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if not k.endswith('example')},indent=2))
if __name__=='__main__':main()
