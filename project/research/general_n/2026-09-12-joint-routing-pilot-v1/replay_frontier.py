#!/usr/bin/env python3
"""Apply only the frozen rational templates to the complete eligible pool."""
from functools import lru_cache
from pathlib import Path
from collections import Counter
import json,sys,time
from joint_bound import context
from select_pilot import old_hand,read_bytes
HERE=Path(__file__).resolve().parent

@lru_cache(maxsize=None)
def maxima(h,T,b,c,P,j,lam,mu,eta,den,mode):
    v=[None,None]
    for H in range(c+1):
        e=int(H>h)
        if e and j==0:continue
        for p in range(min(P,b-1-H)+1):
            incoming=p if mode=='aggregate' else min(p,j-e)
            x=den*(h*H+H*max(0,T-max(h,H+p)))+eta*H-(lam+mu)*H*e+lam*incoming
            if v[e] is None or x>v[e]:v[e]=x
    return v


def check(ctx,b,j,tpl,mode):
    h=ctx['h'];den=tpl['denominator'];lam,mu,eta=[h*tpl[k] for k in ('lam','mu','eta')]
    lows=0;differences=[]
    for g in ctx['groups']:
        lo,hi=maxima(h,ctx['T'],b,g['c'],g['P'],j,lam,mu,eta,den,mode)
        lows+=g['n']*lo
        if hi is not None:differences.extend([hi-lo]*g['n'])
    upper=den*h*ctx['r']+lows+sum(sorted(differences,reverse=True)[:j])+mu*(j*ctx['z']-j*(j+1)//2)-eta*ctx['W']
    lower=den*h*ctx['G']
    return dict(j=j,denominator=den,lam=lam,mu=mu,eta=eta,lhs=lower,rhs=upper,gap=lower-upper,mode=mode)


def search(rec,templates,mode):
    failures=[]
    for h in range(1,max(rec['s'])+1):
        ctx=context(rec,h,4*h);cases=[]
        for j,bound in enumerate(ctx['jbounds']):
            if ctx['W']>bound:
                cases.append(dict(j=j,source_capacity_exclusion=True,upper=bound));continue
            best=None
            for tid,tpl in enumerate(templates):
                c=check(ctx,rec['b'],j,tpl,mode);c['template_id']=tid
                if best is None or c['gap']*best['denominator']>best['gap']*c['denominator']:best=c
                if c['gap']>0:break
            if best['gap']<=0:
                failures.append(dict(h=h,T=4*h,first_failed_j=j,best=best));break
            cases.append(best)
        else:return dict(h=h,T=4*h,cases=cases),failures
    return None,failures


def main():
    start=time.monotonic()
    templates=json.loads((HERE/'multiplier_catalog.json').read_text())['templates']
    pool=[r for r in json.loads(read_bytes('remaining_states.json'))
          if r['original_method'] in ('fixed9','fixed13','adaptive') and not old_hand(r)]
    counts=Counter();layer_counts={};replaced=[];survivors=[]
    with (HERE/'frontier_results.jsonl').open('w') as out:
        for i,rec in enumerate(pool,1):
            record=dict(layer=rec['layer'],state_id=rec['state_id'],modes={},failed_thresholds={})
            for mode in ('aggregate','joint'):
                w,failed=search(rec,templates,mode)
                record['modes'][mode]=w;record['failed_thresholds'][mode]=failed
            outcome=('both' if record['modes']['aggregate'] and record['modes']['joint'] else
                     'joint_only' if record['modes']['joint'] else
                     'aggregate_only' if record['modes']['aggregate'] else 'survives_catalog')
            record['result']=outcome;counts[outcome]+=1
            layer_counts.setdefault(rec['layer'],Counter())[outcome]+=1
            (replaced if record['modes']['joint'] else survivors).append([rec['layer'],rec['state_id']])
            out.write(json.dumps(record,separators=(',',':'))+'\n')
            if i%500==0 or i==len(pool):print('PROGRESS',i,dict(counts),round(time.monotonic()-start,2),flush=True)
    report=dict(status='COMPLETE_FROZEN_CATALOG_REPLAY',eligible_states=len(pool),templates=len(templates),
        parameter_scope='Every h=1..max(s), T=4h; all feasible j; frozen 20 scale-invariant rational templates.',
        counts=dict(counts),by_layer={k:dict(v) for k,v in layer_counts.items()},
        new_joint_exclusions=len(replaced),joint_survivors=len(survivors),excluded_ids=replaced,survivor_ids=survivors,
        external_review='OPEN',scope='Necessary-condition states; survival is failure of this finite catalog, not graph feasibility. Canonical fixed-order ledgers unchanged.')
    (HERE/'frontier_summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if not k.endswith('_ids')},indent=2),flush=True)

if __name__=='__main__':main()
