#!/usr/bin/env python3
"""Configuration LP discovery and exact local-maxima certificate checking.

Tests all 135 frozen selected patterns surviving the endpoint-only control.
Modes distinguish residual-placement control from genuine pair constraints.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
from endpoint_control import frozen_patterns,budgets,residual_price_max,prior

HERE=Path(__file__).resolve().parent

def options(rec,S):
    D=prior.deficit_graph(rec,S);edges=sorted(D);opts=[]
    for u,Su in enumerate(S):
        for R in combinations([i for i in range(rec['a']) if i not in Su],rec['rho'][u]):
            N=Su|set(R);cover=[k for k,(i,j) in enumerate(edges) if i in N and j in N and not(i in Su and j in Su)]
            opts.append((u,R,cover))
    return D,edges,opts

def exact_check(rec,S,D,edges,opts,w,alpha,nu,mu):
    r,q,x,L,U,h=budgets(rec,S);a,b=rec['a'],rec['b']
    w=list(map(F,w));alpha={tuple(k):F(v) for k,v in alpha.items()};nu=list(map(F,nu));mu=F(mu)
    assert len(w)==len(edges) and all(v>=0 for v in w)
    assert all(u in range(b) and i in S[u] and v>=0 for (u,i),v in alpha.items())
    lam=[sum((alpha.get((u,i),F(0)) for u in range(b)),F(0)) for i in range(a)]
    row=[sum((alpha.get((u,i),F(0)) for i in S[u]),F(0)) for u in range(b)]
    local=[None]*b
    for u,R,cover in opts:
        value=sum((w[k] for k in cover),F(0))+sum((lam[i]-nu[i] for i in R),F(0))
        local[u]=value if local[u] is None else max(local[u],value)
    budget,_=residual_price_max(nu,L,U,r)
    const=sum((v*(x[i]-q[u]) for (u,i),v in alpha.items()),F(0))+sum((h[u]*max(F(0),mu-row[u]) for u in range(b)),F(0))
    lhs=sum((w[k]*D[e] for k,e in enumerate(edges)),F(0))+mu*sum(q)
    rhs=sum(local,F(0))+budget+const
    return lhs-rhs,lhs,rhs,local

def solve(rec,S,with_pairs,D,edges,opts):
    r,q,x,L,U,h=budgets(rec,S);a,b=rec['a'],rec['b'];Q=sum(q);n=len(opts)
    inc=[(u,i) for u in range(b) for i in sorted(S[u])]
    # Always feasible discovery relaxation: a common nonnegative slack relaxes
    # every endpoint, label bound and (when enabled) pair requirement.
    nr=len(inc)+2*a+(len(edges) if with_pairs else 0)
    rows=[];cols=[];data=[];rhs=[x[i]-q[u] for u,i in inc]+U+[-v for v in L]+([-D[e] for e in edges] if with_pairs else [])
    label_rows=[[k for k,(u,j) in enumerate(inc) if j==i] for i in range(a)]
    for z,(u,R,cover) in enumerate(opts):
        for i in R:
            for k in label_rows[i]:rows.append(k);cols.append(z);data.append(-1)
            rows.extend([len(inc)+i,len(inc)+a+i]);cols.extend([z,z]);data.extend([1,-1])
        if with_pairs:
            for k in cover:rows.append(len(inc)+2*a+k);cols.append(z);data.append(-1)
    for k,(u,i) in enumerate(inc):rows.append(k);cols.append(n+u);data.append(1)
    for k in range(nr):rows.append(k);cols.append(n+b);data.append(-1)
    Aub=coo_matrix((data,(rows,cols)),shape=(nr,n+b+1)).tocsr()
    er=[u for u,R,cov in opts]+[b]*b;ec=list(range(n))+list(range(n,n+b));ev=[1]*len(er)
    Aeq=coo_matrix((ev,(er,ec)),shape=(b+1,n+b+1)).tocsr()
    objective=np.zeros(n+b+1);objective[-1]=1
    start=time.monotonic()
    res=linprog(objective,A_ub=Aub,b_ub=rhs,A_eq=Aeq,b_eq=[1]*b+[Q],bounds=[(0,None)]*n+[(0,k) for k in h]+[(0,None)],method='highs',options={'time_limit':20})
    out={'mode':'shared_pair' if with_pairs else 'placement_control','solver_status':int(res.status),'message':res.message,'elapsed_seconds':time.monotonic()-start,'configurations':n}
    if res.success:
        out['minimum_relaxation']=float(res.fun)
        if res.fun>1e-7:
            neg=[max(F(0),F(float(-v)).limit_denominator(100000)) for v in res.ineqlin.marginals]
            alpha={e:neg[k] for k,e in enumerate(inc)}
            nu=[neg[len(inc)+i]-neg[len(inc)+a+i] for i in range(a)]
            w=neg[len(inc)+2*a:] if with_pairs else [F(0)]*len(edges)
            mu=F(float(res.eqlin.marginals[-1])).limit_denominator(100000)
            gap,lhs,rhs,local=exact_check(rec,S,D,edges,opts,w,alpha,nu,mu)
            out.update(exact_gap=str(gap),exact_lhs=str(lhs),exact_rhs=str(rhs))
            if gap>0:
                out['exact_pattern_exclusion']=True
                out['certificate']={'pair_weights':[[*e,str(w[k])] for k,e in enumerate(edges) if w[k]],'endpoint_weights':[[u,i,str(v)] for (u,i),v in alpha.items() if v],'residual_prices':list(map(str,nu)),'incoming_multiplier':str(mu),'local_maxima':list(map(str,local))}
    return out

def main():
    previous=json.loads((HERE/'ENDPOINT_CONTROL.json').read_text())
    survivors={(w['layer'],w['state_id']) for w in previous['records'] if not w.get('exact_pattern_exclusion')}
    records=[]
    for rec,S,_ in frozen_patterns():
        if (rec['layer'],rec['state_id']) not in survivors:continue
        D,edges,opts=options(rec,S)
        entry={'layer':rec['layer'],'state_id':rec['state_id'],'placement_control':solve(rec,S,False,D,edges,opts)}
        if not entry['placement_control'].get('exact_pattern_exclusion'):
            entry['shared_pair']=solve(rec,S,True,D,edges,opts)
        records.append(entry)
        if len(records)%10==0:print('shared pair',len(records),flush=True)
        (HERE/'SHARED_PAIR.json').write_text(json.dumps({'scope':'partial until summary is added','records':records},separators=(',',':'))+'\n')
    summary={'input_patterns':len(survivors),'tested':len(records),'placement_control_exclusions':sum(x['placement_control'].get('exact_pattern_exclusion',False) for x in records),'additional_pair_exclusions':sum(x.get('shared_pair',{}).get('exact_pattern_exclusion',False) for x in records),'solver_nonoptimal':sum(v.get('solver_status',0)!=0 for x in records for k,v in x.items() if k in ('placement_control','shared_pair')),'whole_state_exclusions':0}
    (HERE/'SHARED_PAIR.json').write_text(json.dumps({'schema':'shared-pair-budget-v1','date':'2026-09-13','scope':'Fixed selected-pattern exclusions only. Passing a fractional relaxation is not an integer residual realization, exact routing or graph.','summary':summary,'records':records},separators=(',',':'))+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
