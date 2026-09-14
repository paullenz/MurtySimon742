#!/usr/bin/env python3
"""Independent NumPy replay of each exported C++ labelled profile.
Generation is shared with the frozen pilot; only arithmetic is independently
implemented. This audit makes no whole-state promotion or universal claim.
"""
import csv,collections,hashlib,json
from pathlib import Path
import numpy as np
from explore_thresholds import states
ROOT=Path(__file__).parent
counts=collections.Counter();first_hist=collections.Counter();best_threshold_hist=collections.Counter()
state_summary={}; examples=[];survivors=[];weighted_misses=[]

def batch(rows):
    q=np.array([[int(x) for x in r['q'].split(',')] for r in rows],dtype=np.int64)
    rho=np.array([[int(x) for x in r['rho'].split(',')] for r in rows],dtype=np.int64)
    P=np.array([[int(x) for x in r['P'].split(',')] for r in rows],dtype=np.int64)
    m,b=q.shape;c=q+rho
    a=np.array([states[int(r['state'])]['a'] for r in rows]);delta=b-a
    t=np.array([int(r['t']) for r in rows]);E=np.array([int(r['Esel']) for r in rows]);D0=np.array([int(r['D0']) for r in rows])
    assert all(min(states[int(r['state'])]['s'])>0 for r in rows), 'This frozen audit specializes the selected cap to z=0'
    ssum=np.array([sum(states[int(r['state'])]['s']) for r in rows])
    Q=q.sum(1);R=rho.sum(1);G=b*(delta-1)-(2*t+D0+E)
    assert np.all(Q==ssum+E) and np.all(D0==ssum-R-2*t)
    assert np.all(D0>=0) and np.all(E>=0) and np.all(t>0) and np.all(G>=0)
    assert np.all(c<=a[:,None]) and np.all(rho>=1)
    D=(q[:,:,None]<=c[:,None,:]+1)&(q[:,None,:]<=c[:,:,None])&(~np.eye(b,dtype=bool)[None,:,:])
    degree=(D|D.transpose(0,2,1)).sum(2)
    h=rho+delta[:,None]-1
    selected=rho-1+np.floor_divide(E[:,None],np.maximum(q,1));selected=np.where(q>0,selected,10**6)
    Pnew=np.minimum.reduce([h,b-1-q,degree-q,selected])
    assert np.array_equal(P,Pnew) and np.all(P>=0)
    L=(h-P).sum(1)
    lossformula=np.maximum.reduce([np.zeros_like(q),c+delta[:,None]-1-degree,np.where(q>0,delta[:,None]-np.floor_divide(E[:,None],np.maximum(q,1)),0)])
    assert np.array_equal(h-P,lossformula)
    Nhigher=(q[:,:,None]>=c[:,None,:]+2).sum(1)
    first=np.zeros(m,dtype=int)-1;firstI=first.copy();best=first.copy()*999;bestI=best.copy();besttau=first.copy();misses=np.zeros(m,dtype=int);uniform=np.zeros(m,dtype=int)
    for tau in range(1,int(q.max())+2):
        sel=q>=tau;N=sel.sum(1)
        y=(D&sel[:,:,None]).sum(1)
        J=np.maximum(0,N[:,None]-Nhigher)-sel
        assert np.all(J>=y)
        demand=np.where(sel,q,0).sum(1)
        H=np.minimum(P,y).sum(1);U=np.minimum(P,J).sum(1)
        exact=demand-H;lower=demand-U
        Omega=np.maximum(0,P-J).sum(1)
        Xi=np.maximum(0,J-y-np.maximum(0,J-P)).sum(1)
        low=Q-demand
        assert np.array_equal(lower,L+Omega-low-G)
        assert np.array_equal(exact,lower+Xi)
        first=np.where((first<0)&(exact>0),tau,first)
        firstI=np.where((firstI<0)&(lower>0),tau,firstI)
        besttau=np.where(exact>best,tau,besttau)
        best=np.maximum(best,exact);bestI=np.maximum(bestI,lower)
        misses+=H!=U;uniform+=exact
        for j in np.flatnonzero(Xi>0):
            if len(examples)<3:
                examples.append(dict(**rows[j],tau=tau,H=int(H[j]),U=int(U[j]),Xi=int(Xi[j]),
                                     exact_deficiency=int(exact[j]),interval_lower=int(lower[j])))
    for field,arr in [('first_exact',first),('first_interval',firstI),('best_exact',best),('best_interval',bestI),('threshold_mismatches',misses),('uniform',uniform)]:
        assert np.array_equal(arr,np.array([int(r[field]) for r in rows])),field
    counts['profiles_arithmetic_audited']+=m
    for j,r in enumerate(rows):
        fail=int(r['hall_failure'])
        counts['Hall_failures']+=fail;counts['Hall_passes']+=not fail
        if fail:
            counts['exact_tail_detected']+=best[j]>0;counts['interval_detected']+=bestI[j]>0
            counts['uniform_weight_detected']+=uniform[j]>0;counts['all_thresholds_exact']+=misses[j]==0
            counts['first_threshold_agrees']+=first[j]==firstI[j];counts['maximum_deficiency_agrees']+=best[j]==bestI[j]
            first_hist[int(firstI[j])]+=1;best_threshold_hist[int(besttau[j])]+=1
            if uniform[j]<=0 and len(weighted_misses)<3:weighted_misses.append(r)
        else:
            survivors.append(r)
            assert best[j]==bestI[j]==0
        key=(int(r['state']),int(r['Esel']))
        entry=state_summary.setdefault(key,dict(state=key[0],Esel=key[1],a=int(a[j]),b=b,t=int(t[j]),D0=int(D0[j]),r=int(R[j]),Q=int(Q[j]),G=int(G[j]),profiles=0,hall_failures=0,interval_detected=0,minimum_max_interval_deficiency=10**6,maximum_max_interval_deficiency=-10**6))
        entry['profiles']+=1;entry['hall_failures']+=fail;entry['interval_detected']+=fail and bestI[j]>0
        entry['minimum_max_interval_deficiency']=min(entry['minimum_max_interval_deficiency'],int(bestI[j]));entry['maximum_max_interval_deficiency']=max(entry['maximum_max_interval_deficiency'],int(bestI[j]))

pending=[]
with (ROOT/'INTERVAL_PROFILES.tsv').open() as f:
    for r in csv.DictReader(f,delimiter='\t'):
        if pending and (r['q'].count(',')!=pending[0]['q'].count(',') or len(pending)>=4096):
            batch(pending);pending=[]
        pending.append(r)
if pending:batch(pending)
# The scanner's original output must exactly match all frozen logical values.
old=list(csv.DictReader((ROOT/'Q_STRATIFIED_RECEIVER_REACH_PILOT.tsv').open(),delimiter='\t'))
new=list(csv.DictReader((ROOT/'INTERVAL_REPLAY.tsv').open(),delimiter='\t'))
assert len(old)==len(new)==15
for x,y in zip(old,new):
    assert {k:v for k,v in x.items() if k!='seconds'}=={k:v for k,v in y.items() if k!='seconds'}
result=dict(status='PASS',counts={k:int(v) for k,v in counts.items()},first_interval_threshold_histogram=dict(first_hist),best_exact_threshold_histogram=dict(best_threshold_hist),
            prior_scanner_logical_columns_identical=True,profiles_generated=int(sum(int(r['profiles_tested']) for r in new)),
            reverse_gap_examples=examples,uniform_weight_miss_examples=weighted_misses,
            source_profile_sha256=hashlib.sha256((ROOT/'INTERVAL_PROFILES.tsv').read_bytes()).hexdigest(),
            scope='Independent arithmetic audit on shared frozen generation; reconnaissance, no frontier promotion')
(ROOT/'INTERVAL_FULL_PILOT_AUDIT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
(ROOT/'INTERVAL_HALL_PASS_PROFILES.json').write_text(json.dumps(survivors,indent=2,sort_keys=True)+'\n')
with (ROOT/'INTERVAL_BUDGET_CORRELATIONS.csv').open('w') as f:
    wr=csv.DictWriter(f,fieldnames=list(next(iter(state_summary.values()))));wr.writeheader();wr.writerows(state_summary.values())
print(json.dumps({k:v for k,v in result.items() if not k.endswith('examples')},indent=2,sort_keys=True))
