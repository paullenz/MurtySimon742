#!/usr/bin/env python3
"""Discover and exactly check shared-label endpoint budget certificates.

The LP is discovery only. Each accepted exclusion is checked with rational
arithmetic using the elementary weighted endpoint inequality.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import sys
import time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

HERE = Path(__file__).resolve().parent
PREV = HERE.parent / '2026-09-13-constraint-respecting-cross-v1'
sys.path.insert(0, str(PREV))
import check_pair_overlap as prior

def frozen_patterns():
    pool = prior.pool()
    full = json.loads((PREV/'FULL_DOMAIN_SPILL_EXACT.json').read_text())
    out = json.loads((PREV/'PAIR_OVERLAP_CHECK.json').read_text())
    repairs = {(w['layer'],w['state_id']):w['switches'] for w in out['pair_repairs']}
    failures = {(w['layer'],w['state_id']) for w in out['local_residual_cover_failures']}
    for w in full['witnesses']:
        key=w['layer'],w['state_id']; rec=pool[key]; S=[set(row) for row in w['selected']]
        for u,v,i,j in repairs.get(key,[]):
            assert i in S[u]-S[v] and j in S[v]-S[u]
            S[u].remove(i);S[u].add(j);S[v].remove(j);S[v].add(i)
        assert prior.selected_degrees(S,rec['a'])==rec['s']
        assert all(rec['rho'][u]>=rec['s'][i] for u in range(rec['b']) for i in S[u])
        yield rec,S,key in failures

def budgets(rec,S):
    a,b=rec['a'],rec['b'];r=sum(rec['rho']);q=list(map(len,S));x=prior.selected_degrees(S,a)
    # C has no isolated vertex on this domain by the canonical bridge.
    assert rec['t']>0 and b>a-1-rec['t']
    excess=sum(rec['s'])-r-2*rec['t']; assert excess>=0
    L=[max([0]+[q[u]-x[i] for u in range(b) if i in S[u]]) for i in range(a)]
    U=[min(b-x[i],a-2-rec['s'][i]+(excess if rec['s'][i]==0 else 0)) for i in range(a)]
    h=[min(rec['rho'][u]+b-a-1,b-1-q[u]) for u in range(b)]
    return r,q,x,L,U,h

def residual_price_max(prices,L,U,r):
    """Exact support function of integer box bounds and a fixed total mass."""
    assert all(0<=l<=u for l,u in zip(L,U)) and sum(L)<=r<=sum(U)
    amounts=list(L);left=r-sum(L)
    for i in sorted(range(len(L)),key=lambda i:(-prices[i],i)):
        take=min(left,U[i]-L[i]);amounts[i]+=take;left-=take
    assert left==0
    return sum((prices[i]*amounts[i] for i in range(len(L))),F(0)),amounts

def endpoint_certificate(rec,S,alphas,betas):
    r,q,x,L,U,h=budgets(rec,S);a,b=rec['a'],rec['b']
    alphas={tuple(k):F(v) for k,v in alphas.items()};betas=list(map(F,betas))
    assert all(u in range(b) and i in S[u] and v>=0 for (u,i),v in alphas.items())
    assert len(betas)==b and all(v>=0 for v in betas)
    assert all(betas[u]+sum((alphas.get((u,i),F(0)) for i in S[u]),F(0))>=1 for u in range(b))
    prices=[sum((alphas.get((u,i),F(0)) for u in range(b)),F(0)) for i in range(a)]
    cap,allocation=residual_price_max(prices,L,U,r)
    bound=cap+sum((betas[u]*h[u] for u in range(b)),F(0))+sum((v*(x[i]-q[u]) for (u,i),v in alphas.items()),F(0))
    return F(sum(q))-bound,bound,allocation

def solve_control(rec,S):
    r,q,x,L,U,h=budgets(rec,S);a,b=rec['a'],rec['b']; edges=[(u,i) for u in range(b) for i in sorted(S[u])]
    assert sum(L)<=r<=sum(U) and all(l<=u for l,u in zip(L,U))
    rows=[];cols=[];vals=[];rhs=[]
    for k,(u,i) in enumerate(edges):
        rows.extend([k,k]);cols.extend([a+u,i]);vals.extend([1,-1]);rhs.append(x[i]-q[u])
    for u in range(b):
        rows.append(len(rhs));cols.append(a+u);vals.append(1);rhs.append(h[u])
    mat=coo_matrix((vals,(rows,cols)),shape=(len(rhs),a+b)).tocsr()
    res=linprog([0]*a+[-1]*b,A_ub=mat,b_ub=rhs,A_eq=[[1]*a+[0]*b],b_eq=[r],bounds=list(zip(L,U))+[(0,None)]*b,method='highs')
    out={'layer':rec['layer'],'state_id':rec['state_id'],'solver_status':int(res.status),'solver_message':res.message,'selected_total':sum(q),'residual_total':r}
    if res.success:
        out['relaxed_maximum_incoming']=-float(res.fun)
        out['reported_gap']=sum(q)+float(res.fun)
        if out['reported_gap']>1e-7:
            aa={e:max(F(0),F(float(-res.ineqlin.marginals[k])).limit_denominator(10000)) for k,e in enumerate(edges)}
            bb=[max(F(0),F(float(-res.ineqlin.marginals[len(edges)+u])).limit_denominator(10000)) for u in range(b)]
            for u in range(b):bb[u]+=max(F(0),1-bb[u]-sum((aa.get((u,i),F(0)) for i in S[u]),F(0)))
            gap,bound,allocation=endpoint_certificate(rec,S,aa,bb)
            out['exact_gap']=str(gap);out['exact_upper_bound']=str(bound)
            if gap>0:
                out['certificate']={'alpha':[[u,i,str(v)] for (u,i),v in aa.items() if v],'beta':list(map(str,bb)),'maximizing_residual_allocation':allocation}
                out['exact_pattern_exclusion']=True
    return out

def main():
    start=time.monotonic();records=[]
    for rec,S,old_failure in frozen_patterns():
        out=solve_control(rec,S);out['prior_local_cover_failure']=old_failure;records.append(out)
        if len(records)%500==0:print('endpoint control',len(records),flush=True)
    payload={'schema':'shared-residual-endpoint-control-v1','date':'2026-09-13','scope':'Frozen selected-pattern control; p is variable. Numerical feasibility does not construct an integer residual realization or a graph. Exact certificates exclude only their fixed selected pattern.','summary':{'patterns':len(records),'exact_pattern_exclusions':sum(x.get('exact_pattern_exclusion',False) for x in records),'new_beyond_old_fixed_pattern_failures':sum(x.get('exact_pattern_exclusion',False) and not x['prior_local_cover_failure'] for x in records),'solver_nonoptimal':sum(x['solver_status']!=0 for x in records),'whole_state_exclusions':0},'elapsed_seconds':time.monotonic()-start,'records':records}
    (HERE/'ENDPOINT_CONTROL.json').write_text(json.dumps(payload,separators=(',',':'))+'\n');print(json.dumps(payload['summary'],indent=2))

if __name__=='__main__':main()
