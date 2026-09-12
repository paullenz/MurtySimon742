#!/usr/bin/env python3
"""Independent integer replay: indicator potentials and cardinality dynamic programming.

Imports no discovery, envelope, catalog-builder or frontier-selection code.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'2026-09-12-heavy-load-family-v1'
COUNTS=Counter()


def stored(folder,name):
    catalog=folder/'EVIDENCE_STORAGE.json'
    entry=json.loads(catalog.read_text())['files'].get(name) if catalog.exists() else None
    if not entry:return (folder/name).read_bytes()
    data=(folder/entry['stored_file']).read_bytes()
    assert len(data)==entry['stored_bytes'] and hashlib.sha256(data).hexdigest()==entry['stored_sha256']
    raw=gzip.decompress(base64.b64decode(data))
    assert len(raw)==entry['original_bytes'] and hashlib.sha256(raw).hexdigest()==entry['original_sha256']
    assert (len(raw.splitlines()) if entry['format']=='jsonl' else len(json.loads(raw)))==entry['records']
    return raw


def dimensions(rec,h):
    s,rho,a=rec['s'],rec['rho'],rec['a']
    vertices=[(r,min(a-r,len([v for v in s if h<=v<=r]))) for r in rho if r>=h]
    W=sum(sv for sv in s if sv>=h);z=len(vertices)
    high=sorted([c for r,c in vertices if c>h],reverse=True)
    lows=sum(min(c,h) for r,c in vertices)
    bounds=[lows-j*h+min(sum(high[:j]),j*(z-j)+j*(j-1)//2) for j in range(len(high)+1)]
    return W,vertices,bounds


def hand(rec):
    s,rho=rec['s'],rec['rho']
    if min(s)>0 and sum(s)!=sum(rho)+2*rec['t']:return True
    for h in range(1,max(s)+1):
        W,vs,bs=dimensions(rec,h);z=len(vs)
        if h>=2 and z>=h and 2*W==z*(z-1)+h*(h+1) and W-h*(h+1)>sum(r-1 for r,c in vs):return True
        if W>max(bs):return True
    return False


@lru_cache(maxsize=None)
def local_scores(h,T,b,c,P,j,lam,mu,eta,den,mode):
    maxima=[None,None]
    for e in (0,1):
        if e>j:continue
        for H in range(c+1):
            if int(H>h)!=e:continue
            for p in range(P+1):
                if H+p>b-1:continue
                # Independently count the step indicators instead of using the ramp.
                steps=sum(H+p<=cutoff for cutoff in range(h,T))
                delivery=p if mode=='aggregate' else min(p,j-e)
                value=den*H*(h+steps)+eta*H-lam*(e*H-delivery)-mu*e*H
                COUNTS['local_options']+=1
                if maxima[e] is None or value>maxima[e]:maxima[e]=value
    return tuple(maxima)


def bound(rec,h,T,c):
    j,den,lam,mu,eta=[c[k] for k in ('j','denominator','lam','mu','eta')]
    assert all(type(v) is int and v>=0 for v in (j,lam,mu,eta)) and type(den) is int and den>0
    W,vs,bs=dimensions(rec,h);assert 0<=j<len(bs)
    dp=[0]+[None]*j
    for rv,cap in vs:
        lo,hi=local_scores(h,T,rec['b'],cap,rv+rec['b']-rec['a']-1,j,lam,mu,eta,den,c['mode'])
        nextdp=[None]*(j+1)
        for used,v in enumerate(dp):
            if v is None:continue
            nextdp[used]=v+lo if nextdp[used] is None else max(nextdp[used],v+lo)
            if used<j and hi is not None:
                nextdp[used+1]=v+hi if nextdp[used+1] is None else max(nextdp[used+1],v+hi)
        dp=nextdp
    assert dp[j] is not None
    pair=j*(len(vs)-j)+j*(j-1)//2
    upper=den*h*sum(rec['rho'])+dp[j]+mu*pair-eta*W
    lower=den*h*sum(max(T,v) for v in rec['s'] if v>=h)
    COUNTS['integer_envelopes']+=1
    return lower,upper


def certificate(rec,h,T,c,positive=True):
    lower,upper=bound(rec,h,T,c)
    assert (c['lhs'],c['rhs'],c['gap'])==(lower,upper,lower-upper)
    if positive:assert lower>upper


def witness(rec,w,mode):
    assert w['T']==4*w['h'] and 1<=w['h']<=max(rec['s'])
    W,vs,bs=dimensions(rec,w['h'])
    assert [c['j'] for c in w['cases']]==list(range(len(bs)))
    for c in w['cases']:
        if c.get('source_capacity_exclusion'):
            assert c['upper']==bs[c['j']] and W>c['upper'];COUNTS['specified_j_capacity_exclusions']+=1
        else:
            assert c['mode']==mode;certificate(rec,w['h'],w['T'],c)
    COUNTS['complete_state_witnesses']+=1


def main():
    prior=json.loads(stored(OLD,'remaining_states.json'))
    base=[r for r in prior if r['original_method'] in ('fixed9','fixed13','adaptive')]
    pool={(r['layer'],r['state_id']):r for r in base if not hand(r)}
    selection=json.loads((HERE/'pilot_inputs.json').read_text())
    assert len(base)==selection['historical_envelope_pool']==6499
    assert len(pool)==selection['eligible_pool']==6307
    removed={(r['layer'],r['state_id']) for r in selection['removed_by_reapplied_hand_rules']}
    assert removed=={(r['layer'],r['state_id']) for r in base}-pool.keys()
    groups=defaultdict(list)
    for r in pool.values():groups[r['layer'],r['original_method']].append(r)
    ids=set()
    for (layer,method),items in groups.items():
        chosen=range(len(items)) if layer=='n35-m307' else {0,len(items)//2,len(items)-1}
        ids.update((items[i]['layer'],items[i]['state_id']) for i in chosen)
    zeros=[r for r in pool.values() if min(r['s'])==0]
    ids.update((zeros[i]['layer'],zeros[i]['state_id']) for i in {0,len(zeros)//2,len(zeros)-1})
    assert selection['sample']==[pool[key] for key in sorted(ids)] and len(ids)==27
    pilot=[json.loads(line) for line in stored(HERE,'pilot_results.jsonl').splitlines()]
    assert [(r['layer'],r['state_id']) for r in pilot]==sorted(ids)
    pilot_counts=Counter();pilot_extra=[]
    for r in pilot:
        key=r['layer'],r['state_id'];rec=pool[key]
        for mode,w in r['modes'].items():
            if w:witness(rec,w,mode);pilot_counts[mode]+=1
        if r['modes']['joint'] and not r['modes']['aggregate']:pilot_extra.append(list(key))
        for log in r['attempts']:
            if 'exact' in log:certificate(rec,log['h'],log['T'],log['exact'],positive=False)
    templates=json.loads((HERE/'multiplier_catalog.json').read_text())['templates']
    records=[json.loads(line) for line in stored(HERE,'frontier_results.jsonl').splitlines()]
    assert [(r['layer'],r['state_id']) for r in records]==list(pool)
    counts=Counter();by_layer=defaultdict(Counter);excluded=[];survivors=[]
    for index,r in enumerate(records,1):
        key=r['layer'],r['state_id'];rec=pool[key]
        for mode,w in r['modes'].items():
            if w:witness(rec,w,mode)
            failed=r['failed_thresholds'][mode]
            assert [f['h'] for f in failed]==list(range(1,w['h'] if w else max(rec['s'])+1))
            for f in failed:
                h,j=f['h'],f['first_failed_j'];assert f['T']==4*h
                W,vs,bs=dimensions(rec,h);assert 0<=j<len(bs) and W<=bs[j]
                certificate(rec,h,4*h,f['best'],positive=False)
                best_gap,best_den=f['best']['gap'],f['best']['denominator'];assert best_gap<=0
                # Verify every frozen template fails at the recorded blocking j.
                for tid,tpl in enumerate(templates):
                    trial=dict(j=j,denominator=tpl['denominator'],mode=mode,
                               **{k:h*tpl[k] for k in ('lam','mu','eta')})
                    lhs,rhs=bound(rec,h,4*h,trial)
                    assert lhs<=rhs and (lhs-rhs)*best_den<=best_gap*tpl['denominator']
        outcome=('both' if r['modes']['aggregate'] and r['modes']['joint'] else
                 'joint_only' if r['modes']['joint'] else 'aggregate_only' if r['modes']['aggregate'] else 'survives_catalog')
        assert r['result']==outcome;counts[outcome]+=1;by_layer[r['layer']][outcome]+=1
        (excluded if r['modes']['joint'] else survivors).append(list(key))
        if index%1000==0:print('VERIFIED',index,flush=True)
    summary=json.loads((HERE/'frontier_summary.json').read_text())
    assert summary['counts']==dict(counts) and summary['by_layer']==dict(by_layer)
    assert summary['excluded_ids']==excluded and summary['survivor_ids']==survivors
    assert summary['new_joint_exclusions']==len(excluded) and summary['joint_survivors']==len(survivors)
    report=dict(status='PASS',pilot_states=27,pilot_exclusions=dict(pilot_counts),pilot_joint_beyond_aggregate=pilot_extra,
        full_pool=len(pool),full_joint_exclusions=len(excluded),full_joint_survivors=len(survivors),
        full_catalog_outcomes=dict(counts),reapplied_old_hand_removals=len(removed),checks=dict(COUNTS),
        implementation='Independent indicator-sum local scores and cardinality dynamic programming; no discovery imports.',external_review='OPEN')
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)

if __name__=='__main__':main()
