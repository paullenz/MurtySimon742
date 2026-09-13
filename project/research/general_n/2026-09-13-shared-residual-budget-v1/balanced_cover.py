#!/usr/bin/env python3
"""Exact balanced selected-label cover, or a checkable concentration witness."""
from collections import deque
from pathlib import Path
import json
from endpoint_control import frozen_patterns,budgets

HERE=Path(__file__).resolve().parent

def balanced_cover(rec,S):
    r,q,x,L,U,h=budgets(rec,S); active=[u for u in range(rec['b']) if q[u]];labels=[i for i in range(rec['a']) if x[i]]
    m=len(active);c=len(labels);assert m and c
    # Integer scaling of one unit per active source and m/c per used label.
    n=2+m+c;source=n-2;sink=n-1;adj=[[] for _ in range(n)];res={};original={}
    def edge(u,v,k):
        adj[u].append(v);adj[v].append(u);res[u,v]=k;res[v,u]=0;original[u,v]=k
    for z,u in enumerate(active):
        edge(source,z,c)
        for j,i in enumerate(labels):
            if i in S[u]:edge(z,m+j,c*m+1)
    for j in range(c):edge(m+j,sink,m)
    flow=0
    while True:
        parent={source:None};todo=deque([source])
        while todo and sink not in parent:
            u=todo.popleft()
            for v in adj[u]:
                if v not in parent and res[u,v]>0:parent[v]=u;todo.append(v)
        if sink not in parent:break
        amount=c*m;v=sink
        while v!=source:amount=min(amount,res[parent[v],v]);v=parent[v]
        v=sink
        while v!=source:u=parent[v];res[u,v]-=amount;res[v,u]+=amount;v=u
        flow+=amount
    H0=sum(h[u] for u in range(rec['b']) if not q[u]);Q=sum(q)
    gap=(2*c-m)*Q-c*H0-m*r
    out={'layer':rec['layer'],'state_id':rec['state_id'],'active_sources':m,'used_labels':c,'selected_total':Q,'residual_total':r,'empty_source_incoming_capacity':H0,'integer_bound_gap':gap}
    if flow==c*m:
        cert=[[u,i,original[z,m+j]-res[z,m+j]] for z,u in enumerate(active) for j,i in enumerate(labels) if (z,m+j) in original and original[z,m+j]-res[z,m+j]]
        assert all(sum(v for u0,i,v in cert if u0==u)==c for u in active)
        assert all(sum(v for u,i0,v in cert if i0==i)==m for i in labels)
        out.update(balanced=True,integer_cover=cert,exact_pattern_exclusion=gap>0)
    else:
        rows=[active[z] for z in range(m) if z in parent];I=sorted(set().union(*(S[u] for u in rows)))
        assert c*len(rows)>m*len(I)
        out.update(balanced=False,concentrated_sources=rows,concentrated_labels=I,exact_pattern_exclusion=False)
    return out

def main():
    results=[balanced_cover(rec,S) for rec,S,_ in frozen_patterns()]
    out={'schema':'balanced-selected-cover-v1','scope':'Exact fixed-pattern balance-or-concentration witnesses; no whole-state exclusion.','summary':{'patterns':len(results),'balanced':sum(x['balanced'] for x in results),'concentrated':sum(not x['balanced'] for x in results),'exact_pattern_exclusions':sum(x['exact_pattern_exclusion'] for x in results),'whole_state_exclusions':0},'records':results}
    (HERE/'BALANCED_COVER.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(out['summary'],indent=2))
if __name__=='__main__':main()
