#!/usr/bin/env python3
"""Apply the hand family to complete preserved N34/N35 frontier domains."""
from collections import Counter
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import json
import sys
import time
from bounds import capped,uniform_cap,profile_gap

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'project/research/n34/2026-09-12-equality-v1'))
sys.path.insert(0,str(ROOT/'project/research/n34/2026-09-12-frontier-v1'))
from certificate_io import read_stage
from check_frontier import expand


def inputs():
    states,_=expand(1);old={}
    for stage in ('fixed','adaptive'):
        for rec in read_stage(stage):
            i=rec['state_id'];assert (tuple(rec['s']),tuple(rec['rho']))==states[i]
            if rec['method']!='unresolved':old[i]=rec['method']
    for i,(s,rho) in enumerate(states):
        if i not in old:
            assert s==(1,1)+(2,)*13 and rho==(1,)*10+(2,)*8
            old[i]='heavy_load_hand'
        yield dict(layer='n34-m289',state_id=i,a=15,b=18,t=1,s=s,rho=rho,original_method=old[i])
    for t in (3,2):
        for line in (ROOT/f'project/research/n35/2026-09-12-candidate-v1/t{t}.jsonl').read_text().splitlines():
            rec=json.loads(line)
            yield dict(layer=f'n35-m{304+t}',state_id=rec['state_id'],a=15,b=19,t=t,
                       s=tuple(rec['s']),rho=tuple(rec['rho']),original_method=rec['method'])


def search(rec):
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho'];r=sum(rho)
    contexts={}
    for h in range(1,max(s)+1):
        heavy=[v for v in s if v>=h]
        groups=Counter((rv+b-a-1,min(a-rv,sum(h<=v<=rv for v in s))) for rv in rho if rv>=h)
        contexts[h]=(heavy,groups)
    for stage in ('four_h','uniform','capped'):
        for h,(heavy,groups) in contexts.items():
            values=(4*h,) if stage=='four_h' else range(h,4*a+1)
            for T in values:
                lhs=h*sum(max(T,v) for v in heavy)
                rhs=h*r+sum(n*(capped(h,T,P,c) if stage=='capped' else uniform_cap(h,T,P)) for (P,c),n in groups.items())
                if lhs>rhs:
                    proof=profile_gap(a,b,s,rho,h,T,'capped' if stage=='capped' else 'uniform')
                    assert proof['lhs']==lhs and proof['rhs']==rhs
                    return dict(stage=stage,**proof)
    return None


def main():
    start=time.monotonic();counts={};matrix={};remaining=[];replaced=[]
    with (HERE/'frontier_results.jsonl').open('w') as out:
        for n,rec in enumerate(inputs(),1):
            layer=rec['layer'];counts.setdefault(layer,Counter());matrix.setdefault(layer,Counter())
            if min(rec['s'])>0 and sum(rec['s'])!=sum(rec['rho'])+2*rec['t']:
                rec['result']='existing_positive_degree_mass'
            else:
                witness=search(rec)
                rec['result']=witness['stage'] if witness else 'survives_searched_family'
                if witness:rec['witness']=witness
                else:remaining.append(rec)
            counts[layer][rec['result']]+=1
            matrix[layer][rec['original_method']+' -> '+rec['result']]+=1
            if 'witness' in rec and rec['original_method'] in ('fixed9','fixed13','adaptive'):
                replaced.append((layer,rec['state_id']))
            out.write(json.dumps(rec,separators=(',',':'))+'\n')
            if n%1000==0:print('PROGRESS',n,round(time.monotonic()-start,2),{k:dict(v) for k,v in counts.items()},flush=True)
    report=dict(status='COMPLETE_PARAMETER_SCAN',parameters='all h=1..max(s); T=4h, then integer T=h..4a',
        counts={k:dict(v) for k,v in counts.items()},original_method_transition={k:dict(v) for k,v in matrix.items()},
        previously_certified_states_now_excluded_by_family=len(replaced),replaced_certificate_states=replaced,
        remaining_states=len(remaining),scope='Survival is only within the stated parameter search; these are necessary-condition states, not graphs.',external_review='OPEN')
    (HERE/'frontier_summary.json').write_text(json.dumps(report,indent=2)+'\n')
    (HERE/'remaining_states.json').write_text(json.dumps(remaining,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('replaced_certificate_states','original_method_transition')},indent=2))


if __name__=='__main__':main()
