#!/usr/bin/env python3
"""Verify the q elimination and five-breakpoint formula against recorded gaps."""
from functools import cache
from pathlib import Path
from collections import Counter
import json
from evidence_io import records
HERE=Path(__file__).resolve().parent
COUNTS=Counter()

@cache
def local(a,b,h,j,rho,heavy,has_small):
    delta=b-a;assert a>=2 and b>=2 and delta>=0 and h>=2 and rho>=1
    if rho==1:return (4*min(delta,b-2) if has_small else 0,None)
    best=[None,None]
    for H in range(min(a-rho,heavy)+1):
        e=int(H>h)
        if e and j==0:continue
        P=min(rho+delta-1,b-1-H);assert P>=0
        points={0,P}|{p for p in [h-H,4*h-H,j-e] if 0<=p<=P}
        assert len(points)<=5
        for p in points:
            value=H*(h+max(0,4*h-max(h,H+p)))+H-2*e*H
            if rho>=h:value+=2*min(p,j-e)
            if H>2:value-=4*H
            value+=4*p;COUNTS['breakpoint_evaluations']+=1
            if best[e] is None or value>best[e]:best[e]=value
    return tuple(best)

def gap(rec,h,j):
    a,b,s,rho=rec['a'],rec['b'],rec['s'],rec['rho'];small=any(v<=1 for v in s)
    classes={rv:local(a,b,h,j,rv,sum(h<=v<=rv for v in s),small) for rv in set(rho)}
    low=sum(classes[rv][0] for rv in rho)
    differences=sorted([classes[rv][1]-classes[rv][0] for rv in rho if classes[rv][1] is not None],reverse=True)
    assert len(differences)>=j
    maximum=low+sum(differences[:j]);W=sum(v for v in s if v>=h);G=sum(max(4*h,v) for v in s if v>=h)
    return h*(G-sum(rho))+W-maximum

def main():
    cat=json.loads((HERE/'catalogue.json').read_text());expected=[['ub',['all_transport',2],4],['ub',['heavy_mass'],1],['ub',['heavy_receiving'],2],['ub',['load'],1]]
    assert cat['templates'][13]['weights']==expected
    position=cat['modes']['eligible'].index(13);pool=records('pool_inputs.jsonl');output=records('frontier_results.jsonl');checked=0;whole=0
    for rec,result in zip(pool,output):
        assert (rec['layer'],rec['state_id'])==(result['layer'],result['state_id'])
        mode=result['modes']['eligible'];winning=False
        for threshold in mode['thresholds']:
            allpositive=True;h=threshold['h']
            for attempt in threshold['attempts']:
                actual=gap(rec,h,attempt['j']);checked+=1
                assert actual==attempt['gaps'][position],(rec['layer'],rec['state_id'],h,attempt['j'])
                allpositive &= actual>0
            if h==mode['witness_h']:winning=allpositive
        whole+=winning
    assert whole==707
    report=dict(status='PASS',template_id=13,full_model_gaps_matched=checked,whole_states_at_recorded_winning_threshold=whole,
        source_contexts=local.cache_info().currsize,**COUNTS,
        exact_q_elimination=True,at_most_five_p_breakpoints_per_H=True,
        scope='Finite corroboration of the hand-proved parameterized reduction; no added exclusions',external_review='OPEN')
    (HERE/'fixed_potential_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
