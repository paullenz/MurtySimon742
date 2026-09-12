#!/usr/bin/env python3
"""Full demand-profile application using only the frozen integer catalogue."""
from collections import Counter,defaultdict
from functools import lru_cache
from pathlib import Path
import json,sys,time
from projection import baseline,context
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'2026-09-12-heavy-load-family-v1'))
from evidence_io import read_records


@lru_cache(maxsize=None)
def source_maxima(h,b,c,P,j,lam,mu,eta,den,aggregate):
    A=[None,None]
    for H in range(c+1):
        e=int(H>h)
        if e and j==0:continue
        for p in range(min(P,b-1-H)+1):
            B=h*H+H*max(0,4*h-max(h,H+p))
            incoming=p if aggregate else min(p,j-e)
            val=den*B+eta*H-(lam+mu)*e*H+lam*incoming
            if A[e] is None or val>A[e]:A[e]=val
    return tuple(A)


def evaluate(ctx,j,tpl,mode):
    h,z=ctx['h'],ctx['z'];den=tpl['denominator'];lam,mu,eta,kappa=[h*tpl[k] for k in ('lam','mu','eta','kappa')]
    A=[None,None]
    for rv,c,P in ctx['types']:
        vals=source_maxima(h,ctx['b'],c,P,j,lam,mu,eta,den,mode=='aggregate')
        for e,v in enumerate(vals):
            if v is not None:
                val=v-kappa*(rv-h)
                if A[e] is None or val>A[e]:A[e]=val
    lhs=den*h*ctx['G']
    rhs=den*h*ctx['M']+kappa*ctx['E']+(z-j)*A[0]+(j*A[1] if j else 0)+mu*(j*(z-j)+j*(j-1)//2)-eta*ctx['W']
    return dict(j=j,denominator=den,lam=lam,mu=mu,eta=eta,kappa=kappa,lhs=lhs,rhs=rhs,gap=lhs-rhs,local_maxima=A)


def search(rec,catalog,mode):
    L=baseline(rec);M=sum(rec['s'])-2*rec['t'];new=dict(L);thresholds=[]
    if rec['new_minimum_residual']>M:return dict(result='prior_profile_exclusion')
    for h in range(1,max(rec['s'])+1):
        tests=[];minimum=None
        for z in ([rec['b']] if h==1 else range(L[h],rec['b']+1)):
            ctx=context(rec,L,h,z)
            if not ctx['options'][0]:
                tests.append(dict(z=z,existing_tail_budget_exclusion=True,E=ctx['E'],Rmax=ctx['Rmax']));continue
            cases=[]
            for j,upper in enumerate(ctx['jbounds']):
                if ctx['W']>upper:cases.append(dict(j=j,capacity_exclusion=True,upper=upper));continue
                best=None
                for tid,tpl in enumerate(catalog):
                    if mode=='no_penalty' and tpl['kappa']:continue
                    c=evaluate(ctx,j,tpl,mode);c['template_id']=tid
                    if best is None or c['gap']*best['denominator']>best['gap']*c['denominator']:best=c
                    if c['gap']>0:break
                if best['gap']<=0:
                    minimum=z;tests.append(dict(z=z,first_failed_j=j,best=best));break
                cases.append(best)
            else:
                tests.append(dict(z=z,cases=cases));continue
            break
        thresholds.append(dict(h=h,baseline=L[h],new_minimum=minimum,tests=tests))
        if minimum is None:return dict(result='single_threshold_profile_exclusion',h=h,thresholds=thresholds)
        new[h]=max(new[h],minimum)
    for h in range(rec['a'],1,-1):new[h]=max(new[h],new[h+1])
    cost=rec['b']+sum(new[h] for h in range(2,rec['a']+1))
    return dict(result='joint_tail_profile_exclusion' if cost>M else 'survives_projection',minimum_residual=cost,
                closed_tails=[new[h] for h in range(1,rec['a']+1)],thresholds=thresholds)


def main():
    start=time.monotonic();catalog=json.loads((HERE/'multiplier_catalog.json').read_text())['templates']
    records=read_records('profile_results.jsonl');counts=defaultdict(Counter);layers=defaultdict(lambda:defaultdict(Counter));profile_map={};extra=[]
    with (HERE/'profile_results.jsonl').open('w') as out:
        for i,rec in enumerate(records):
            row=dict(profile_id=i,a=rec['a'],b=rec['b'],t=rec['t'],s=rec['s'],modes={})
            layer=f'n{rec["a"]+rec["b"]+1}-m{rec["b"]*(rec["a"]+1)+rec["t"]}'
            for mode in ('no_penalty','aggregate','joint_budget'):
                result=search(rec,catalog,mode);row['modes'][mode]=result
                counts[mode][result['result']]+=1;layers[layer][mode][result['result']]+=1
                if result.get('minimum_residual',0)>rec['new_minimum_residual']:
                    counts[mode]['raised_budget_in_surviving_or_joint_profile']+=1
            profile_map[layer,tuple(rec['s'])]=row
            out.write(json.dumps(row,separators=(',',':'))+'\n')
            if i%200==0:print('PROFILES',i,{k:dict(v) for k,v in counts.items()},round(time.monotonic()-start,2),flush=True)
    prior_joint=json.loads((HERE.parent/'2026-09-12-joint-routing-pilot-v1/frontier_summary.json').read_text())
    survivors=set(map(tuple,prior_joint['survivor_ids']));state_counts=defaultdict(Counter);state_records=[]
    for rec in read_records('frontier_results.jsonl'):
        key=rec['layer'],rec['state_id']
        if key not in survivors:continue
        row=profile_map[rec['layer'],tuple(rec['s'])];result=dict(layer=key[0],state_id=key[1],profile_id=row['profile_id'],modes={})
        for mode,proof in row['modes'].items():
            status=proof['result']
            if status in ('single_threshold_profile_exclusion','joint_tail_profile_exclusion','prior_profile_exclusion'):
                why=dict(reason=status)
            else:
                bad=[h for h,L in enumerate(proof['closed_tails'],1) if sum(v>=h for v in rec['rho'])<L]
                why=dict(reason='new_tail_exclusion',h=bad[0]) if bad else dict(reason='survives_projection')
            result['modes'][mode]=why;state_counts[mode][why['reason']]+=1
        state_records.append(result)
    assert len(state_records)==5578
    (HERE/'state_comparison.json').write_text(json.dumps(state_records,separators=(',',':'))+'\n')
    summary=dict(status='COMPLETE_FROZEN_CATALOG_REPLAY',profiles=len(records),templates=len(catalog),
                 counts={k:dict(v) for k,v in counts.items()},layers={k:{m:dict(c) for m,c in v.items()} for k,v in layers.items()},
                 prior_joint_survivors=5578,state_comparison={k:dict(v) for k,v in state_counts.items()},
                 scope='One pass from the preceding heavy-load closed tails. Survivors are necessary-condition records, not graphs.',external_review='OPEN')
    (HERE/'profile_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':main()
