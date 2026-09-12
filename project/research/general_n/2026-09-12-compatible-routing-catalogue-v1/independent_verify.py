#!/usr/bin/env python3
"""Separate Cartesian source domains, semantic costs, and exact-j dynamic programming."""
from collections import Counter
from functools import cache
from itertools import product
from pathlib import Path
import base64,gzip,hashlib,json
from evidence_io import records
HERE=Path(__file__).resolve().parent
COUNTS=Counter()

def decode(folder,name):
    meta=json.loads((folder/'EVIDENCE_STORAGE.json').read_text())['files'][name]
    data=(folder/meta['stored_file']).read_bytes()
    assert hashlib.sha256(data).hexdigest()==meta['stored_sha256'] and len(data)==meta['stored_bytes']
    raw=gzip.decompress(base64.b64decode(data))
    assert hashlib.sha256(raw).hexdigest()==meta['original_sha256'] and len(raw)==meta['original_bytes']
    return raw

def terms(raw):
    result=[]
    for kind,desc,w in raw:
        assert type(w) is int and (kind=='eq' and desc==['selected_balance'] or kind=='ub' and w>=0)
        assert desc[0] in ['heavy_mass','load','pair_capacity','heavy_receiving','selected_balance','all_transport','forced_transport']
        result.append((tuple(desc),w))
    return tuple(result)

@cache
def domain(a,b,h,j,rho,hi,lo,heavy_only):
    if heavy_only and rho<h:return ((0,0,0),)
    out=[]
    # Independent Cartesian filtering, not the replay engine's ragged loops.
    for q,p,H in product(range(a+1),range(b),range(a+1)):
        if q+rho>a or q+p>=b or p>rho+b-a-1:continue
        if H>q or H>hi or H>h and j==0:continue
        if heavy_only:
            if q!=H:continue
        elif q-H>lo:continue
        out.append((q,p,H))
    COUNTS['distinct_domain_options']+=len(out)
    return tuple(out)

@cache
def maxima(a,b,h,j,rho,hi,lo,heavy_only,weights):
    best=[None,None]
    for q,p,H in domain(a,b,h,j,rho,hi,lo,heavy_only):
        e=int(H>=h+1);F=H if e else 0
        receive=0 if rho<h else min(p,j-e)
        cost=0
        for desc,w in weights:
            kind=desc[0]
            if kind=='heavy_mass':co=-H
            elif kind=='load':co=-H*(h+sum(q+p<=k for k in range(h,4*h)))
            elif kind=='pair_capacity':co=F
            elif kind=='heavy_receiving':co=F-receive
            elif kind=='selected_balance':co=q-p
            elif kind=='all_transport':co=(q if q>=desc[1]+1 else 0)-(p if rho+q>=desc[1] else 0)
            elif kind=='forced_transport':co=(F if q>=desc[1]+1 else 0)-(receive if rho+q>=desc[1] else 0)
            else:raise AssertionError(desc)
            cost-=w*co
        COUNTS['source_potential_checks']+=1
        if best[e] is None or cost>best[e]:best[e]=cost
    assert best[0] is not None
    return tuple(best)

@cache
def envelope(a,b,s,rho,h,j,heavy_only,weights):
    best={}
    for rv in set(rho):
        hi=sum(h<=v<=rv for v in s);lo=sum(v<h and v<=rv for v in s)
        best[rv]=maxima(a,b,h,j,rv,hi,lo,heavy_only,weights)
    dp={0:0}
    for rv in rho:
        nxt={}
        for used,amount in dp.items():
            for e,value in enumerate(best[rv]):
                if value is None or used+e>j:continue
                nxt[used+e]=max(nxt.get(used+e,amount+value),amount+value)
        dp=nxt
    assert j in dp
    constant=0
    for desc,w in weights:
        if desc[0]=='heavy_mass':constant-=w*sum(v for v in s if v>=h)
        if desc[0]=='load':constant+=w*h*(sum(rho)-sum(max(4*h,v) for v in s if v>=h))
        if desc[0]=='pair_capacity':constant+=w*(j*sum(v>=h for v in rho)-j*(j+1)//2)
    return -constant-dp[j]

def gap(rec,h,j,heavy_only,weights):
    return envelope(rec['a'],rec['b'],tuple(rec['s']),tuple(rec['rho']),h,j,heavy_only,weights)

def capacity(rec,h):
    limits=[]
    for rho in rec['rho']:
        if rho>=h:limits.append(min(rec['a']-rho,sum(h<=s<=rho for s in rec['s'])))
    limits.sort(reverse=True);z=len(limits);out=[]
    for j in range(sum(v>h for v in limits)+1):
        ordinary=sum(min(h,c) for c in limits)-j*h
        out.append(ordinary+min(sum(limits[:j]),j*(z-j)+j*(j-1)//2))
    return out

def main():
    pool=records('pool_inputs.jsonl');results=records('frontier_results.jsonl')
    oldheavy=decode(HERE.parent/'2026-09-12-heavy-load-family-v1','remaining_states.json')
    oldjoint=decode(HERE.parent/'2026-09-12-joint-routing-pilot-v1','frontier_results.jsonl')
    prior=[json.loads(line) for line in oldjoint.splitlines()]
    ids={(r['layer'],r['state_id']) for r in prior if r['modes']['joint'] is None}
    assert len(prior)==6307 and len(ids)==5578
    expected=sorted([r for r in json.loads(oldheavy) if (r['layer'],r['state_id']) in ids],key=lambda r:(r['layer'],r['state_id']))
    assert pool==expected and len(results)==5578
    assert [(r['layer'],r['state_id']) for r in results]==[(r['layer'],r['state_id']) for r in pool]
    cat=json.loads((HERE/'catalogue.json').read_text());templates=[terms(x['weights']) for x in cat['templates']]
    sets={m:set() for m in cat['modes']};positive=[];thresholds=attempts=values_checked=bypasses=0
    for index,(rec,result) in enumerate(zip(pool,results)):
        assert set(result['modes'])==set(cat['modes'])
        for mode,entries in result['modes'].items():
            assert mode in sets;witness=None
            for h,entry in enumerate(entries['thresholds'],2):
                assert entry['h']==h and h<=max(rec['s']);thresholds+=1
                caps=capacity(rec,h);assert caps==entry['capacities']
                W=sum(v for v in rec['s'] if v>=h);ai=0;blocked=False
                for j,c in enumerate(caps):
                    if c<W:bypasses+=1;continue
                    attempt=entry['attempts'][ai];ai+=1;attempts+=1;assert attempt['j']==j
                    exact=[gap(rec,h,j,mode=='heavy_only',templates[ti]) for ti in cat['modes'][mode]]
                    assert exact==attempt['gaps'],(rec['layer'],rec['state_id'],mode,h,j)
                    values_checked+=len(exact)
                    if max(exact)<=0:blocked=True;break
                    positive.append(max(exact))
                assert ai==len(entry['attempts'])
                if not blocked:
                    assert h==entries['thresholds'][-1]['h'];witness=h;break
            if witness is None:assert len(entries['thresholds'])==max(rec['s'])-1
            assert entries['witness_h']==witness
            if witness:sets[mode].add((rec['layer'],rec['state_id']))
        if (index+1)%1000==0:print('VERIFIED',index+1,'states',flush=True)
    assert sets['heavy_only']<=sets['selected_degree']<=sets['eligible']
    # Carry forward original pilot-only whole-state witnesses rather than
    # losing them when restricting the reusable catalogue.
    pilot=HERE.parent/'2026-09-12-compatible-routing-pilot-v1'
    oldresults=[json.loads(line) for line in decode(pilot,'pilot_results.jsonl').splitlines()]
    oldenv=json.loads((pilot/'envelopes.json').read_text())
    byenv={(e['layer'],e['state_id'],e['attempt_index']):e for e in oldenv}
    byrec={(r['layer'],r['state_id']):r for r in pool}
    oldset={(r['layer'],r['state_id']) for r in oldresults if r['modes']['separate_transport']}
    inherited=oldset-sets['eligible'];inherited_cases=0
    for result in oldresults:
        key=result['layer'],result['state_id']
        if key not in inherited:continue
        rec=byrec[key];witness=result['modes']['separate_transport'];h=witness['h'];caps=capacity(rec,h)
        assert [c['j'] for c in witness['cases']]==list(range(len(caps)))
        for case in witness['cases']:
            j=case['j'];inherited_cases+=1
            if 'source_capacity' in case:assert case['source_capacity']==caps[j]<sum(v for v in rec['s'] if v>=h)
            else:
                env=byenv[key+(case['attempt_index'],)];assert (env['mode'],env['h'],env['j'])==('separate_transport',h,j)
                assert gap(rec,h,j,False,terms(env['weights']))==env['gap']>0
    report=dict(status='PASS',states=5578,thresholds=thresholds,attempted_sender_counts=attempts,
        exact_catalogue_gaps_checked=values_checked,capacity_bypasses=bypasses,
        domain_cache_entries=domain.cache_info().currsize,potential_cache_entries=maxima.cache_info().currsize,
        **COUNTS,minimum_best_positive_integer_gap=min(positive),
        exclusions={m:len(s) for m,s in sets.items()},catalogue_survivors=5578-len(sets['eligible']),
        pilot_exclusions=len(oldset),pilot_retained=len(oldset&sets['eligible']),inherited_pilot_only=sorted(map(list,inherited)),
        inherited_sender_count_cases=inherited_cases,combined_exclusions=len(oldset|sets['eligible']),combined_survivors=5578-len(oldset|sets['eligible']),
        integer_arithmetic='Python unbounded integers; separate Cartesian source domains and per-source cardinality dynamic programming',external_review='OPEN')
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
