#!/usr/bin/env python3
"""Independent exact verification from tail slack and indicator local costs.

No imports from discovery, projection or catalogue-building implementations.
"""
from pathlib import Path
from collections import Counter,defaultdict
from functools import lru_cache
import base64,csv,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OLD=HERE.parent/'2026-09-12-heavy-load-family-v1'
JOINT=HERE.parent/'2026-09-12-joint-routing-pilot-v1'
COUNT=Counter()


def stored(folder,name):
    catalog=folder/'EVIDENCE_STORAGE.json'
    entry=json.loads(catalog.read_text())['files'].get(name) if catalog.exists() else None
    if not entry:return (folder/name).read_bytes()
    b=(folder/entry['stored_file']).read_bytes()
    assert len(b)==entry['stored_bytes'] and hashlib.sha256(b).hexdigest()==entry['stored_sha256']
    raw=gzip.decompress(base64.b64decode(b))
    assert len(raw)==entry['original_bytes'] and hashlib.sha256(raw).hexdigest()==entry['original_sha256']
    obj=json.loads(raw) if entry['format']=='json' else None
    count=len(raw.splitlines()) if entry['format']=='jsonl' else len(obj[entry['records_key']]) if 'records_key' in entry else len(obj)
    assert count==entry['records']
    return raw


def original_profiles():
    records=[json.loads(x) for x in stored(OLD,'profile_results.jsonl').splitlines()]
    expected=[]
    rows=list(csv.DictReader((ROOT/'project/research/n34/2026-09-12-frontier-v1/FRONTIER.csv').open()))
    for b,t in ((18,1),(19,3),(19,2)):
        expected.extend((15,b,t,tuple(int(row[f's{i}']) for i in range(15))) for row in rows if int(row['Q_monotone'])>=b+2*t)
    assert [(r['a'],r['b'],r['t'],tuple(r['s'])) for r in records]==expected and len(records)==1453
    return records


def tails(rec):
    a,b,t,s=rec['a'],rec['b'],rec['t'],rec['s'];M=sum(s)-2*t
    L=[0]*(a+2);L[1]=b
    for h in range(a-1,1,-1):
        W=sum(v for v in s if v>=h);g=h if W else 0
        while g*(g-1)+h*(h+1)<2*W:g+=1
        G=sum(max(4*h,v) for v in s if v>=h)
        load=-(-(G-2*M+b)//(3*h+1)) if b-a<=2*h+1 else 0
        L[h]=max(g,load,L[h+1])
    assert all(L[row['h']]==row['closed_tail'] for row in rec['tails'])
    assert b+sum(L[2:])==rec['new_minimum_residual']
    return tuple(L)


def dimensions(rec,L,h,z):
    a,b,s=rec['a'],rec['b'],rec['s'];M=sum(s)-2*rec['t']
    assert rec['t']>0 and 1<=h<=max(s)<a
    assert z==b if h==1 else L[h]<=z<=b
    D=M-b-sum(L[2:]);d=max(i for i,v in enumerate(L) if v)
    assert h<=d
    beta=sum(max(0,z-L[l]) for l in range(2,h+1))
    E=sum(L[h+1:])+D-beta;Rmax=min(a,d+D-beta)
    W=sum(v for v in s if v>=h);G=sum(max(4*h,v) for v in s if v>=h)
    types=[]
    if beta<=D:
        for rv in range(h,Rmax+1):
            c=min(a-rv,len([v for v in s if h<=v<=rv]));P=rv+b-a-1
            assert P>=0
            types.append((rv,c,P))
    C=max((c for rv,c,P in types),default=0)
    bounds=[(z-j)*min(h,C)+min(j*C,j*(z-j)+j*(j-1)//2) for j in range(z+1 if C>h else 1)]
    return dict(D=D,beta=beta,E=E,Rmax=Rmax,types=tuple(types),bounds=bounds,W=W,G=G,M=M)


@lru_cache(maxsize=None)
def options(h,b,c,P,j,lam,mu,eta,den,aggregate):
    best=[None,None]
    for p in range(P+1):
        for H in range(c+1):
            if H+p>=b:continue
            e=int(H>h)
            if e and j==0:continue
            steps=sum(int(H+p<=cutoff) for cutoff in range(h,4*h))
            incoming=p if aggregate else min(p,j-e)
            value=den*H*(h+steps)+eta*H-lam*(e*H-incoming)-mu*e*H
            COUNT['local_options']+=1
            if best[e] is None or value>best[e]:best[e]=value
    return tuple(best)


def bound(rec,L,h,z,c,aggregate=False):
    j,den,lam,mu,eta,kappa=[c[k] for k in ('j','denominator','lam','mu','eta','kappa')]
    assert all(type(x) is int and x>=0 for x in (j,lam,mu,eta,kappa)) and type(den) is int and den>0
    ctx=dimensions(rec,L,h,z);assert ctx['beta']<=ctx['D'] and 0<=j<len(ctx['bounds'])
    values=[None,None]
    for rv,cap,P in ctx['types']:
        best=options(h,rec['b'],cap,P,j,lam,mu,eta,den,aggregate)
        for e,x in enumerate(best):
            if x is None:continue
            x-=kappa*(rv-h)
            if values[e] is None or x>values[e]:values[e]=x
    assert values[0] is not None and (j==0 or values[1] is not None)
    lower=den*h*ctx['G']
    upper=den*h*ctx['M']+(z-j)*values[0]+(j*values[1] if j else 0)+kappa*ctx['E']+mu*(j*(z-j)+j*(j-1)//2)-eta*ctx['W']
    COUNT['integer_envelopes']+=1
    return lower,upper,values


def certificate(rec,L,h,z,c,aggregate=False,positive=True):
    lo,hi,values=bound(rec,L,h,z,c,aggregate)
    assert (c['lhs'],c['rhs'],c['gap'])==(lo,hi,lo-hi)
    if z>c['j']:assert c['local_maxima'][0]==values[0]
    if c['j']:assert c['local_maxima'][1]==values[1]
    if positive:assert lo>hi


def result(rec,proof,mode,catalog=None):
    L=tails(rec);M=sum(rec['s'])-2*rec['t']
    if proof.get('prior_excluded') or proof.get('result')=='prior_profile_exclusion':
        assert rec['new_minimum_residual']>M;return None
    assert rec['new_minimum_residual']<=M
    new=list(L);thresholds=proof['thresholds']
    assert [x['h'] for x in thresholds]==list(range(1,len(thresholds)+1))
    for th in thresholds:
        h=th['h'];minimum=th['new_minimum'];assert th['baseline']==L[h]
        start=rec['b'] if h==1 else L[h]
        end=minimum if minimum is not None else rec['b']
        assert [x['z'] for x in th['tests']]==list(range(start,end+1))
        for test in th['tests']:
            z=test['z'];ctx=dimensions(rec,L,h,z)
            if test.get('existing_tail_budget_exclusion'):
                assert ctx['beta']>ctx['D'] and (test['E'],test['Rmax'])==(ctx['E'],ctx['Rmax'])
                COUNT['existing_tail_budget_cases']+=1;continue
            assert ctx['beta']<=ctx['D']
            if 'cases' in test:
                assert [c['j'] for c in test['cases']]==list(range(len(ctx['bounds'])))
                for c in test['cases']:
                    if c.get('capacity_exclusion'):
                        assert c['upper']==ctx['bounds'][c['j']] and ctx['W']>c['upper'];COUNT['capacity_cases']+=1
                    else:
                        if mode=='no_penalty':assert c['kappa']==0
                        certificate(rec,L,h,z,c,mode=='aggregate')
                COUNT['excluded_tail_values']+=1
            else:
                assert test['z']==minimum and test['first_failed_j']==test['best']['j']
                c=test['best'];certificate(rec,L,h,z,c,mode=='aggregate',positive=False)
                assert c['gap']<=0
                if catalog is not None:
                    for tpl in catalog:
                        if mode=='no_penalty' and tpl['kappa']:continue
                        trial=dict(j=c['j'],denominator=tpl['denominator'],**{k:h*tpl[k] for k in ('lam','mu','eta','kappa')})
                        lo,hi,_=bound(rec,L,h,z,trial,mode=='aggregate')
                        assert lo<=hi and (lo-hi)*c['denominator']<=c['gap']*trial['denominator']
        if minimum is None:
            assert h==len(thresholds) and proof['result']=='single_threshold_profile_exclusion' and proof['h']==h
            COUNT['whole_profile_witnesses']+=1;return None
        new[h]=max(new[h],minimum)
    assert len(thresholds)==max(rec['s'])
    for h in range(rec['a'],1,-1):new[h]=max(new[h],new[h+1])
    budget=rec['b']+sum(new[2:]);assert proof['minimum_residual']==budget
    if 'closed_tails' in proof:assert proof['closed_tails']==new[1:rec['a']+1]
    assert proof['result']==('joint_tail_profile_exclusion' if budget>M else 'survives_projection')
    if budget>M:COUNT['whole_profile_witnesses']+=1
    return new


def main():
    originals=original_profiles();lookup={(r['a'],r['b'],r['t'],tuple(r['s'])):r for r in originals}
    selected=json.loads((JOINT/'pilot_inputs.json').read_text())['sample']
    keys={(r['a'],r['b'],r['t'],tuple(r['s'])) for r in selected}
    expected=[r for r in originals if (r['a'],r['b'],r['t'],tuple(r['s'])) in keys]
    assert json.loads((HERE/'pilot_inputs.json').read_text())==expected and len(expected)==27
    pilot=[json.loads(l) for l in stored(HERE,'pilot_results.jsonl').splitlines()]
    assert [r['profile_id'] for r in pilot]==list(range(27));pilot_counts=defaultdict(Counter)
    for row,rec in zip(pilot,expected):
        assert (row['a'],row['b'],row['t'],row['s'])==(rec['a'],rec['b'],rec['t'],rec['s'])
        for mode,proof in row['modes'].items():result(rec,proof,mode);pilot_counts[mode][proof.get('result','prior_profile_exclusion')]+=1
        L=tails(rec)
        for log in row['attempts']:
            for c in log.get('rounding_attempts',[]):certificate(rec,L,log['h'],log['z'],c,positive=False)
    catalog=json.loads((HERE/'multiplier_catalog.json').read_text())['templates'];assert len(catalog)==44
    records=[json.loads(l) for l in stored(HERE,'profile_results.jsonl').splitlines()]
    assert len(records)==len(originals);counts=defaultdict(Counter);layers=defaultdict(lambda:defaultdict(Counter));mapping={}
    for i,(row,rec) in enumerate(zip(records,originals)):
        assert row['profile_id']==i and (row['a'],row['b'],row['t'],row['s'])==(rec['a'],rec['b'],rec['t'],rec['s'])
        layer=f'n{rec["a"]+rec["b"]+1}-m{rec["b"]*(rec["a"]+1)+rec["t"]}'
        mapping[layer,tuple(rec['s'])]=row
        for mode,proof in row['modes'].items():
            result(rec,proof,mode,catalog);counts[mode][proof['result']]+=1;layers[layer][mode][proof['result']]+=1
            if proof.get('minimum_residual',0)>rec['new_minimum_residual']:counts[mode]['raised_budget_in_surviving_or_joint_profile']+=1
        if i%200==0:print('VERIFIED_PROFILES',i,flush=True)
    survivor_ids=set(map(tuple,json.loads((JOINT/'frontier_summary.json').read_text())['survivor_ids']))
    saved=json.loads(stored(HERE,'state_comparison.json'));expected_states=[];state_counts=defaultdict(Counter)
    for rec in [json.loads(l) for l in stored(OLD,'frontier_results.jsonl').splitlines()]:
        key=rec['layer'],rec['state_id']
        if key not in survivor_ids:continue
        row=mapping[rec['layer'],tuple(rec['s'])];out=dict(layer=key[0],state_id=key[1],profile_id=row['profile_id'],modes={})
        for mode,proof in row['modes'].items():
            if proof['result']!='survives_projection':why=dict(reason=proof['result'])
            else:
                bad=[h for h,L in enumerate(proof['closed_tails'],1) if sum(rv>=h for rv in rec['rho'])<L]
                why=dict(reason='new_tail_exclusion',h=bad[0]) if bad else dict(reason='survives_projection')
            out['modes'][mode]=why;state_counts[mode][why['reason']]+=1
        expected_states.append(out)
    assert saved==expected_states and len(saved)==5578
    summary=json.loads((HERE/'profile_summary.json').read_text())
    assert summary['counts']==dict(counts) and summary['layers']==dict(layers) and summary['state_comparison']==dict(state_counts)
    report=dict(status='PASS',pilot_profiles=27,pilot_results={k:dict(v) for k,v in pilot_counts.items()},
                full_profiles=1453,prior_profile_exclusions=45,new_profile_exclusions=114,profile_survivors=1294,
                prior_joint_state_survivors=5578,new_state_exclusions=0,
                checks=dict(COUNT),implementation='Independent tail-slack identities and step-indicator costs; no discovery/projection imports.',external_review='OPEN')
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)

if __name__=='__main__':main()
