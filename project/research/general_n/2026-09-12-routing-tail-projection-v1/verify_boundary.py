#!/usr/bin/env python3
"""Independent scalar replay, enumerating possible high-sender counts."""
from pathlib import Path
from collections import Counter,defaultdict
import json
from verify import original_profiles,tails,dimensions,stored,OLD,JOINT
HERE=Path(__file__).resolve().parent


def main():
    originals=original_profiles();rows=[json.loads(l) for l in stored(HERE,'boundary_results.jsonl').splitlines()]
    assert len(rows)==len(originals)==1453
    counts=defaultdict(Counter);extra=[];raised=[];scalar_closed=set();checks=0
    for i,(row,rec) in enumerate(zip(rows,originals)):
        assert row['profile_id']==i;L=tails(rec);M=sum(rec['s'])-2*rec['t']
        for mode,proof in row['modes'].items():
            status=proof['result'];counts[mode][status]+=1
            if status=='prior_profile_exclusion':assert rec['new_minimum_residual']>M;continue
            assert rec['new_minimum_residual']<=M
            new=list(L);th=proof['thresholds'];assert [x['h'] for x in th]==list(range(1,len(th)+1))
            for threshold in th:
                h=threshold['h'];minimum=threshold['new_minimum'];start=rec['b'] if h==1 else L[h]
                end=minimum if minimum is not None else rec['b']
                assert [x['z'] for x in threshold['tests']]==list(range(start,end+1))
                for test in threshold['tests']:
                    z=test['z'];ctx=dimensions(rec,L,h,z)
                    if test['result']=='prior_tail_budget':assert ctx['beta']>ctx['D'];continue
                    assert ctx['beta']<=ctx['D']
                    P=ctx['Rmax']+rec['b']-rec['a']-1
                    feasible_j=[j for j in range(z+1) if j==0 or (z-j>=2*h and 2*h*j<=P*(z-j))]
                    largest=max(feasible_j);limit=h*(z+largest)
                    assert (test['P'],test['G'],test['load_upper'],test['W'],test['Jmax'],test['equality_W_upper'])==(P,ctx['G'],M+4*h*z,ctx['W'],largest,limit)
                    expected=('load_cap' if P<=3*h and ctx['G']>M+4*h*z else
                              'strict_boundary' if mode=='strict' and P<=3*h and ctx['G']==M+4*h*z and ctx['W']>limit else 'survives_scalar')
                    assert test['result']==expected;checks+=1
                    if expected in ('load_cap','strict_boundary'):counts[mode]['excluded_tail_values']+=1
                    else:assert z==minimum
                if minimum is None:assert status=='single_threshold_profile_exclusion' and h==len(th) and proof['h']==h
                else:new[h]=max(new[h],minimum)
            if status!='single_threshold_profile_exclusion':
                assert len(th)==max(rec['s'])
                for h in range(rec['a'],1,-1):new[h]=max(new[h],new[h+1])
                cost=rec['b']+sum(new[2:]);assert proof['minimum_residual']==cost
                assert proof['closed_tails']==new[1:rec['a']+1]
                assert status==('joint_tail_profile_exclusion' if cost>M else 'survives_scalar')
        ordinary,strict=row['modes']['load_cap'],row['modes']['strict']
        if strict['result'] in ('single_threshold_profile_exclusion','joint_tail_profile_exclusion'):
            scalar_closed.add(i)
            if ordinary['result']=='survives_scalar':extra.append(i)
        if strict.get('minimum_residual',0)>ordinary.get('minimum_residual',0):raised.append(i)
    summary=json.loads((HERE/'boundary_summary.json').read_text())
    assert summary['counts']==dict(counts) and summary['additional_whole_profiles_from_strictness']==extra and summary['raised_budget_vs_load_cap']==raised
    lookup={(f'n{r["a"]+r["b"]+1}-m{r["b"]*(r["a"]+1)+r["t"]}',tuple(r['s'])):i for i,r in enumerate(originals)}
    prior=set(map(tuple,json.loads((JOINT/'frontier_summary.json').read_text())['survivor_ids']))
    expected_states=[];state_counts=Counter()
    for rec in [json.loads(l) for l in stored(OLD,'frontier_results.jsonl').splitlines()]:
        key=rec['layer'],rec['state_id']
        if key not in prior:continue
        i=lookup[rec['layer'],tuple(rec['s'])];proof=rows[i]['modes']['strict'];reason=proof['result']
        if reason=='survives_scalar':
            if any(sum(rv>=h for rv in rec['rho'])<v for h,v in enumerate(proof['closed_tails'],1)):reason='new_tail_exclusion'
        expected_states.append(dict(layer=key[0],state_id=key[1],profile_id=i,reason=reason));state_counts[reason]+=1
    saved=json.loads(stored(HERE,'boundary_state_comparison.json'))
    assert saved==dict(counts=dict(state_counts),records=expected_states) and len(expected_states)==5578
    full=[json.loads(l) for l in stored(HERE,'profile_results.jsonl').splitlines()]
    closed={i for i,r in enumerate(full) if r['modes']['joint_budget']['result'] in ('single_threshold_profile_exclusion','joint_tail_profile_exclusion')}
    assert scalar_closed<=closed
    penalties=[i for i in closed if full[i]['modes']['no_penalty']['result']=='survives_projection']
    destinations=[i for i in closed if full[i]['modes']['aggregate']['result']=='survives_projection']
    slacks=Counter(sum(originals[i]['s'])-2*originals[i]['t']-originals[i]['new_minimum_residual'] for i in closed)
    report=dict(status='PASS',scalar_profiles=1453,scalar_tail_value_checks=checks,
                ordinary_cap_additional_profiles=31,strict_cap_additional_profiles=len(scalar_closed),
                strictness_extra_profile_ids=extra,strictness_raised_budget_ids=raised,
                full_projection_extra_due_to_budget_penalty=penalties,full_projection_extra_due_to_destination_term=destinations,
                full_projection_excluded_profile_slacks=dict(sorted(slacks.items())),
                scalar_closed_profiles_subset_of_projection=True,new_state_exclusions=5578-state_counts['survives_scalar'],
                implementation='Independent scalar replay enumerates admissible j instead of using the closed Jmax formula.',external_review='OPEN')
    (HERE/'boundary_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
