#!/usr/bin/env python3
"""Scalar demand-tail scan: preceding load cap versus its strict boundary."""
from pathlib import Path
from collections import Counter,defaultdict
import json,sys
from projection import baseline,context
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'2026-09-12-heavy-load-family-v1'))
from evidence_io import read_records


def solve(rec,strict):
    L=baseline(rec);new=dict(L);M=sum(rec['s'])-2*rec['t'];thresholds=[]
    if rec['new_minimum_residual']>M:return dict(result='prior_profile_exclusion')
    for h in range(1,max(rec['s'])+1):
        tests=[];minimum=None
        for z in ([rec['b']] if h==1 else range(L[h],rec['b']+1)):
            ctx=context(rec,L,h,z)
            if not ctx['options'][0]:tests.append(dict(z=z,result='prior_tail_budget'));continue
            P=ctx['Rmax']+rec['b']-rec['a']-1
            bound=M+4*h*z
            Jmax=max(0,min(z-2*h,P*z//(P+2*h)))
            outcome=('load_cap' if P<=3*h and ctx['G']>bound else
                     'strict_boundary' if strict and P<=3*h and ctx['G']==bound and ctx['W']>h*(z+Jmax) else 'survives_scalar')
            tests.append(dict(z=z,P=P,G=ctx['G'],load_upper=bound,W=ctx['W'],Jmax=Jmax,equality_W_upper=h*(z+Jmax),result=outcome))
            if outcome=='survives_scalar':minimum=z;break
        thresholds.append(dict(h=h,new_minimum=minimum,tests=tests))
        if minimum is None:return dict(result='single_threshold_profile_exclusion',h=h,thresholds=thresholds)
        new[h]=max(new[h],minimum)
    for h in range(rec['a'],1,-1):new[h]=max(new[h],new[h+1])
    budget=rec['b']+sum(new[h] for h in range(2,rec['a']+1))
    return dict(result='joint_tail_profile_exclusion' if budget>M else 'survives_scalar',minimum_residual=budget,
                closed_tails=[new[h] for h in range(1,rec['a']+1)],thresholds=thresholds)


def main():
    records=read_records('profile_results.jsonl');counts=defaultdict(Counter);extra=[];raised=[]
    with (HERE/'boundary_results.jsonl').open('w') as out:
        for i,rec in enumerate(records):
            row=dict(profile_id=i,modes={})
            for strict in (False,True):
                mode='strict' if strict else 'load_cap';r=solve(rec,strict);row['modes'][mode]=r;counts[mode][r['result']]+=1
                counts[mode]['excluded_tail_values']+=sum(t['result'] in ('strict_boundary','load_cap') for th in r.get('thresholds',[]) for t in th['tests'])
            a,b=row['modes']['load_cap'],row['modes']['strict']
            if b['result'] in ('single_threshold_profile_exclusion','joint_tail_profile_exclusion') and a['result']=='survives_scalar':extra.append(i)
            if b.get('minimum_residual',0)>a.get('minimum_residual',0):raised.append(i)
            out.write(json.dumps(row,separators=(',',':'))+'\n')
    report=dict(status='COMPLETE_SCALAR_SCAN',profiles=len(records),counts={k:dict(v) for k,v in counts.items()},
                additional_whole_profiles_from_strictness=extra,raised_budget_vs_load_cap=raised,external_review='OPEN',
                scope='Closed equality-rigidity inequality and tail slack; no optimization solver.')
    (HERE/'boundary_summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

    scalar=[json.loads(l) for l in (HERE/'boundary_results.jsonl').read_text().splitlines()]
    lookup={(f'n{r["a"]+r["b"]+1}-m{r["b"]*(r["a"]+1)+r["t"]}',tuple(r['s'])):i for i,r in enumerate(records)}
    prior=set(map(tuple,json.loads((HERE.parent/'2026-09-12-joint-routing-pilot-v1/frontier_summary.json').read_text())['survivor_ids']))
    states=[];state_counts=Counter()
    for r in read_records('frontier_results.jsonl'):
        key=r['layer'],r['state_id']
        if key not in prior:continue
        i=lookup[r['layer'],tuple(r['s'])];cert=scalar[i]['modes']['strict']
        reason=cert['result'] if cert['result']!='survives_scalar' else ('new_tail_exclusion' if any(sum(rv>=h for rv in r['rho'])<L for h,L in enumerate(cert['closed_tails'],1)) else 'survives_scalar')
        states.append(dict(layer=key[0],state_id=key[1],profile_id=i,reason=reason));state_counts[reason]+=1
    (HERE/'boundary_state_comparison.json').write_text(json.dumps(dict(counts=dict(state_counts),records=states),separators=(',',':'))+'\n')


if __name__=='__main__':main()
