#!/usr/bin/env python3
"""New caps on the OLD exported profile stream: no source-state regeneration."""
import csv,collections,json,hashlib
from pathlib import Path
import numpy as np
from explore_thresholds import states
ROOT=Path(__file__).parent
counts=collections.Counter();examples=[];firsts=collections.Counter();by_state={}

def batch(rows):
    q=np.array([[int(x) for x in r['q'].split(',')] for r in rows],dtype=np.int64)
    rho=np.array([[int(x) for x in r['rho'].split(',')] for r in rows],dtype=np.int64)
    oldP=np.array([[int(x) for x in r['P'].split(',')] for r in rows],dtype=np.int64)
    m,b=q.shape;c=q+rho;P=oldP.copy()
    s=np.array([states[int(r['state'])]['s'] for r in rows],dtype=np.int64)
    E=np.array([int(r['Esel']) for r in rows]);delta=b-s.shape[1]
    for eta in range(int(rho.max())+1):
        selected_low=q*(rho<=eta);demand_low=s*(s<=eta)
        C=E+demand_low.sum(1)-selected_low.sum(1)
        assert np.all(C>=0)
        number=(s<=eta).sum(1)
        k=np.minimum(np.minimum(number[:,None],q),C[:,None])
        cap=rho-1+(C[:,None]-k)//np.maximum(1,q-k)
        tested=np.ones(m,dtype=bool) if eta==0 else (rho==eta).any(1)
        P=np.where(tested[:,None]&(rho>eta)&(q>k),np.minimum(P,cap),P)
    assert np.all(P>=0) and np.all(P<=oldP)
    D=(q[:,:,None]<=c[:,None,:]+1)&(q[:,None,:]<=c[:,:,None])&(~np.eye(b,dtype=bool)[None,:,:])
    high=(q[:,:,None]>=c[:,None,:]+2).sum(1)
    first=np.full(m,-1,dtype=int);firstI=first.copy();best=np.zeros(m,dtype=int);bestI=best.copy();fixed=np.zeros(m,dtype=int);fixed3=fixed.copy();uniform=fixed.copy()
    for tau in range(1,int(q.max())+1):
        sel=q>=tau;demand=(q*sel).sum(1);y=(D&sel[:,:,None]).sum(1)
        J=np.maximum(0,sel.sum(1)[:,None]-high)-sel
        exact=demand-np.minimum(P,y).sum(1);lower=demand-np.minimum(P,J).sum(1)
        first=np.where((first<0)&(exact>0),tau,first);firstI=np.where((firstI<0)&(lower>0),tau,firstI)
        best=np.maximum(best,exact);bestI=np.maximum(bestI,lower);uniform+=exact
        if tau==delta:fixed=lower.copy()
        if tau==3:fixed3=lower.copy()
    for j,row in enumerate(rows):
        fail=int(row['hall_failure']);counts['old_exported_profiles']+=1
        counts['caps_changed']+=np.any(P[j]!=oldP[j]);counts['localized_tail_detected']+=best[j]>0
        counts['localized_interval_detected']+=bestI[j]>0
        counts['tau_delta_interval_detected']+=fixed[j]>0
        counts['tau_three_interval_detected']+=fixed3[j]>0
        counts['uniform_detected']+=uniform[j]>0
        counts['old_Hall_passes']+=not fail
        if not fail:counts['old_pass_now_interval_detected']+=bestI[j]>0;counts['old_pass_now_sumP_rejected']+=P[j].sum()<q[j].sum()
        firsts[int(firstI[j])]+=1
        state=by_state.setdefault(row['state'],dict(profiles=0,interval_detected=0,tau_delta_detected=0))
        state['profiles']+=1;state['interval_detected']+=int(bestI[j]>0);state['tau_delta_detected']+=int(fixed[j]>0)
        if fixed[j]<=0 and len(examples)<3:
            examples.append(dict(state=row['state'],q=q[j].tolist(),rho=rho[j].tolist(),P_local=P[j].tolist(),Esel=int(E[j]),s=s[j].tolist(),tau_delta=delta,fixed_deficiency_lower=int(fixed[j]),best_interval_deficiency=int(bestI[j]),first_interval_tau=int(firstI[j])))
rows=[]
with (ROOT/'INTERVAL_PROFILES.tsv').open() as f:
    for r in csv.DictReader(f,delimiter='\t'):
        if rows and (len(rows)>=4096 or r['q'].count(',')!=rows[0]['q'].count(',')):
            batch(rows);rows=[]
        rows.append(r)
if rows:batch(rows)
result=dict(status='PASS',scope='Localized caps reconstructed on OLD exported rows only; NOT a regenerated profile search or whole-state exclusion',counts={k:int(v) for k,v in counts.items()},first_interval_tau=dict(firsts),by_state=by_state,fixed_tau_delta_miss_examples=examples,source_profile_sha256=hashlib.sha256((ROOT/'INTERVAL_PROFILES.tsv').read_bytes()).hexdigest())
(ROOT/'LOCALIZED_EXPORTED_REPLAY.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('by_state','fixed_tau_delta_miss_examples')},indent=2,sort_keys=True))
