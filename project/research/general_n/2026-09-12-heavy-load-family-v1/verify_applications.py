#!/usr/bin/env python3
"""Independent exact witness and complete-domain checks; no bounds/discovery import."""
from collections import Counter
from pathlib import Path
import csv
import json
import sys
from evidence_io import read_records,read_bytes

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'project/research/n34/2026-09-12-frontier-v1'))
sys.path.insert(0,str(ROOT/'project/research/n34/2026-09-12-equality-v1'))
from check_frontier import expand
from certificate_io import read_stage


def main():
    expected={};states,_=expand(1);old={}
    for stage in ('fixed','adaptive'):
        for r in read_stage(stage):
            if r['method']!='unresolved':old[r['state_id']]=r['method']
    for i,(s,rho) in enumerate(states):
        if i not in old:
            assert s==(1,1)+(2,)*13 and rho==(1,)*10+(2,)*8
            old[i]='heavy_load_hand'
        expected['n34-m289',i]=(15,18,1,s,rho,old[i])
    for t in (2,3):
        file=ROOT/f'project/research/n35/2026-09-12-candidate-v1/t{t}.jsonl'
        for line in file.read_text().splitlines():
            r=json.loads(line)
            expected[f'n35-m{304+t}',r['state_id']]=(15,19,t,tuple(r['s']),tuple(r['rho']),r['method'])
    seen=set();counts={};replaced=0;checks=0;remaining=[];replacements=[]
    for rec in read_records('frontier_results.jsonl'):
        key=(rec['layer'],rec['state_id'])
        assert key in expected and key not in seen;seen.add(key)
        a,b,t,s,rho,old=expected[key]
        assert (a,b,t,list(s),list(rho),old)==tuple(rec[k] for k in ('a','b','t','s','rho','original_method'))
        result=rec['result'];counts.setdefault(key[0],Counter())[result]+=1
        if result=='existing_positive_degree_mass':
            assert min(s)>0 and sum(s)!=sum(rho)+2*t
        elif result=='survives_searched_family':
            assert 'witness' not in rec;remaining.append(rec)
        else:
            w=rec['witness'];h=w['h'];assert result==w['stage']=='four_h'
            assert w['mode']=='uniform' and w['T']==4*h and 1<=h<=max(s)
            lhs=h*sum(max(4*h,v) for v in s if v>=h);rhs=h*sum(rho)
            terms=[]
            for rv in rho:
                if rv<h:continue
                P=rv+b-a-1;c=min(a-rv,sum(h<=v<=rv for v in s))
                cap=4*h*h+h*max(0,P-3*h)
                # Independently check the local source inequality on every
                # relevant H,p; H>4h has zero ramp and cost h*p.
                for H in range(4*h+2):
                    for p in range(P+1):
                        f=sum(H+p<=j for j in range(h,4*h))
                        cost=h*(H+p)+H*f-h*H*(H>h)
                        assert cost<=cap;checks+=1
                assert h*P<=cap
                rhs+=cap;terms.append([rv,P,c,cap])
            assert (lhs,rhs,lhs-rhs,terms)==(w['lhs'],w['rhs'],w['gap'],w['source_terms'])
            assert lhs>rhs
            if old in ('fixed9','fixed13','adaptive'):
                replaced+=1;replacements.append(list(key))
    assert seen==set(expected) and len(seen)==14031
    summary=json.loads((HERE/'frontier_summary.json').read_text())
    assert {k:dict(v) for k,v in counts.items()}==summary['counts']
    assert replaced==summary['previously_certified_states_now_excluded_by_family']==595
    assert replacements==summary['replaced_certificate_states']
    assert remaining==json.loads(read_bytes('remaining_states.json'))
    assert len(remaining)==summary['remaining_states']==8280

    rows=list(csv.DictReader((ROOT/'project/research/n34/2026-09-12-frontier-v1/FRONTIER.csv').open()))
    profiles={}
    for b,t in ((18,1),(19,3),(19,2)):
        for row in rows:
            if int(row['Q_monotone'])>=b+2*t:
                s=tuple(int(row[f's{i}']) for i in range(15));profiles[b,t,s]=row
    seen=set();profile_counts={}
    for rec in read_records('profile_results.jsonl'):
        a,b,t=rec['a'],rec['b'],rec['t'];s=tuple(rec['s']);S=sum(s)
        key=(b,t,s);assert a==15 and key in profiles and key not in seen;seen.add(key)
        tails={};old={};single=[]
        for h in range(2,a):
            W=sum(v for v in s if v>=h)
            gamma=next(z for z in range(h,a+b+1) if z*(z-1)+h*(h+1)>=2*W) if W else 0
            G=sum(max(4*h,v) for v in s if v>=h);active=b-a<=2*h+1
            numerator=G-2*S+b+4*t;load=-((-numerator)//(3*h+1)) if active else 0
            tails[h]=max(gamma,load,0);old[h]=gamma
            gap=(h-1)*G+4*h*b-(5*h-1)*(S-2*t)
            if active and gap>0:single.append(dict(h=h,gap=gap))
            saved=next(v for v in rec['tails'] if v['h']==h)
            assert (saved['capacity_tail'],saved['load_tail'],saved['active'])==(gamma,load,active)
        closed={h:max(tails[j] for j in range(h,a)) for h in range(2,a)}
        before=b+sum(max(old[j] for j in range(h,a)) for h in range(2,a))
        after=b+sum(closed.values());budget=S-2*t
        assert (before,after,budget)==tuple(rec[k] for k in ('old_minimum_residual','new_minimum_residual','residual_budget'))
        assert list(reversed(single))==rec['single_threshold_witnesses']
        assert all(v['closed_tail']==closed[v['h']] for v in rec['tails'])
        result='single_threshold_exclusion' if single else 'joint_tail_exclusion' if after>budget else 'survives_joint_tail'
        assert result==rec['result']
        if single:assert after>budget
        layer=f'n{a+b+1}-m{b*(a+1)+t}';count=profile_counts.setdefault(layer,Counter())
        count[result]+=1;count['profiles']+=1
        if after>before:count['raised_minimum_residual_budget']+=1
    assert seen==set(profiles) and len(seen)==1453
    assert {k:dict(v) for k,v in profile_counts.items()}==json.loads((HERE/'profile_summary.json').read_text())['layers']
    report=dict(status='PASS',frontier_records=14031,exact_family_witnesses=871,previously_certified_replacements=replaced,
        source_witness_local_integer_checks=checks,profile_records=1453,
        profile_counts={k:dict(v) for k,v in profile_counts.items()},external_review='OPEN',
        limitation='Checks exclusions and complete recorded domains; surviving states make no graph feasibility claim.')
    (HERE/'application_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
