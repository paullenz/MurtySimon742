#!/usr/bin/env python3
"""Separate Cartesian domains and semantic row evaluation; no discovery imports."""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib,json
from evidence_io import read_records
HERE=Path(__file__).resolve().parent

def options(rec,h,j,mode):
    a,b=rec['a'],rec['b'];out=[]
    for rho in sorted(set(rec['rho'])):
        hi=sum(1 for s in rec['s'] if h<=s<=rho)
        lo=sum(1 for s in rec['s'] if s<h and s<=rho)
        if mode=='catalogue_free':
            if rho<h:continue
            for H,p in product(range(a+1),range(b)):
                if H>min(a-rho,hi) or H+p>b-1 or p>rho+b-a-1:continue
                if H>h and not j:continue
                out.append((rho,-1,p,H))
        else:
            for q,p,H in product(range(a+1),range(b),range(a+1)):
                if q+rho>a or q+p>b-1 or p>rho+b-a-1:continue
                if H>q or H>hi or q-H>lo:continue
                if H>h and not j:continue
                out.append((rho,q,p,H))
    return sorted(out,key=lambda t:(t[0],t[1],t[3],t[2]))

def descriptors(rec,h,mode,names):
    eq=[['source_count',rho] for rho in sorted(set(rec['rho'])) if mode!='catalogue_free' or rho>=h]
    eq.append(['high_sender_count'])
    if mode!='catalogue_free':eq.append(['selected_balance'])
    ub=[['heavy_mass'],['load'],['pair_capacity'],['heavy_receiving']]
    if mode in ('separate_transport','joint_transport'):
        for k in range(rec['a']+2):ub.extend([['all_transport',k],['forced_transport',k]])
    if mode=='joint_transport':
        ub.extend(['mixed_transport',k,l] for k in range(1,rec['a']+2) for l in range(k))
    bound_start=len(ub);ub.extend(['count_cap',i] for i in range(len(names)))
    return eq,ub,bound_start

def coefficient(desc,opt,h,j,mode,index):
    rho,q,p,H=opt;kind=desc[0];sender=int(H>=h+1);F=H if sender else 0
    receive=min(p,j-sender) if rho>=h else 0
    if kind=='source_count':return int(rho==desc[1])
    if kind=='high_sender_count':return sender
    if kind=='selected_balance':return q-p
    if kind=='heavy_mass':return -H
    if kind=='load':
        level=(H if mode=='catalogue_free' else q)+p
        ramp=sum(level<=cut for cut in range(h,4*h))
        return -H*(h+ramp)
    if kind=='pair_capacity':return F
    if kind=='heavy_receiving':return F-receive
    if kind=='count_cap':return int(index==desc[1])
    if kind=='all_transport':
        k=desc[1];return (q if q>=k+1 else 0)-(p if rho+q>=k else 0)
    if kind=='forced_transport':
        k=desc[1];return (F if q>=k+1 else 0)-(receive if rho+q>=k else 0)
    if kind=='mixed_transport':
        k,l=desc[1:];sent=(q-F if q>=k+1 else 0)+(F if q>=l+1 else 0)
        # Ordinary-reachable destinations use total capacity. Only the
        # remaining heavy-reachable destinations use forced-arc capacity.
        if rho+q>=k:sent-=p
        elif rho>=h and rho+q>=l:sent-=receive
        return sent
    raise ValueError(desc)

def rhs(desc,rec,h,j,names):
    kind=desc[0]
    if kind=='source_count':return rec['rho'].count(desc[1])
    if kind=='high_sender_count':return j
    if kind=='heavy_mass':return -sum(s for s in rec['s'] if s>=h)
    if kind=='load':return h*(sum(rec['rho'])-sum(max(4*h,s) for s in rec['s'] if s>=h))
    if kind=='pair_capacity':
        z=sum(rho>=h for rho in rec['rho']);return j*(z-j)+j*(j-1)//2
    if kind=='count_cap':return rec['rho'].count(names[desc[1]][0])
    return 0

def reconstruct(rec,h,j,mode):
    names=options(rec,h,j,mode);eq,ub,start=descriptors(rec,h,mode,len(names) and names or [])
    rows={}
    for kind,items in [('eq',eq),('ub',ub)]:
        rows[kind]=[]
        for desc in items:
            co={}
            for col,opt in enumerate(names):
                value=coefficient(desc,opt,h,j,mode,col)
                if value:co[col]=value
            rows[kind].append(dict(name=desc,coefficients=co,rhs=rhs(desc,rec,h,j,names)))
    return dict(names=names,bounds=[rec['rho'].count(x[0]) for x in names],eq=rows['eq'],ub=rows['ub'],bound_start=start,h=h,j=j,mode=mode,
                target=-rhs(['load'],rec,h,j,names))

def capacity(rec,h):
    caps=sorted([min(rec['a']-rho,sum(h<=s<=rho for s in rec['s'])) for rho in rec['rho'] if rho>=h],reverse=True)
    z=len(caps);large=sum(c>h for c in caps);answers=[]
    for j in range(large+1):
        small=sum(min(h,c) for c in caps)-j*h
        pair=j*(z-j)+j*(j-1)//2
        answers.append(small+min(sum(caps[:j]),pair))
    return answers

def check_certificate(model,certificate):
    weights={};total_rhs=0
    for kind in ('eq','ub'):
        seen=set()
        for row,w in certificate[kind]:
            assert type(row) is int and row not in seen and 0<=row<len(model[kind])
            assert type(w) is int and (kind=='eq' or w>=0)
            seen.add(row);weights[kind,row]=w;total_rhs+=w*model[kind][row]['rhs']
    for col in range(len(model['names'])):
        total=sum(w*model[kind][row]['coefficients'].get(col,0) for (kind,row),w in weights.items())
        assert total>=0,(col,total)
    assert total_rhs==certificate['rhs'] and total_rhs<0

def main():
    records=json.loads((HERE/'pilot_inputs.json').read_text())['sample']
    byid={(r['layer'],r['state_id']):r for r in records}
    results=read_records('pilot_results.jsonl')
    assert len(results)==len(records)==29 and len({(r['layer'],r['state_id']) for r in results})==29
    counts=Counter();checks=0;certs=0;models=0;capacity_cases=0;status=Counter()
    for result in results:
        rec=byid[result['layer'],result['state_id']]
        for attempt in result['attempts']:
            model=reconstruct(rec,attempt['h'],attempt['j'],attempt['mode']);models+=1
            digest=hashlib.sha256(json.dumps(model,sort_keys=True,separators=(',',':')).encode()).hexdigest()
            assert digest==attempt['model_sha256'],(result['state_id'],attempt['mode'],attempt['h'],attempt['j'])
            status[attempt['status']]+=1
            if attempt['certificate']:
                check_certificate(model,attempt['certificate']);certs+=1;checks+=len(model['names'])
        for mode,witness in result['modes'].items():
            if witness is None:continue
            counts[mode]+=1;h=witness['h'];caps=capacity(rec,h)
            assert [case['j'] for case in witness['cases']]==list(range(len(caps)))
            for case in witness['cases']:
                j=case['j']
                if 'source_capacity' in case:
                    assert caps[j]==case['source_capacity']<sum(s for s in rec['s'] if s>=h);capacity_cases+=1
                else:
                    a=result['attempts'][case['attempt_index']]
                    assert (a['mode'],a['h'],a['j'])==(mode,h,j) and a['certificate']
    ordered=['catalogue_free','selected_balance','separate_transport','joint_transport']
    sets={m:{(r['layer'],r['state_id']) for r in results if r['modes'][m]} for m in ordered}
    for left,right in zip(ordered,ordered[1:]):assert sets[left]<=sets[right]
    summary=json.loads((HERE/'summary.json').read_text());assert dict(counts)==summary['exclusions'] and models==summary['attempts']
    report=dict(status='PASS',independent_model_hashes=models,integer_certificates=certs,integer_column_checks=checks,capacity_cases=capacity_cases,
        solver_status_counts=dict(status),exclusions=dict(counts),additional_selected_degree=len(sets[ordered[1]]-sets[ordered[0]]),
        additional_destination_eligibility=len(sets[ordered[2]]-sets[ordered[1]]),additional_mixed_cuts=len(sets[ordered[3]]-sets[ordered[2]]),
        survivors=[list((r['layer'],r['state_id'])) for r in results if not r['modes']['joint_transport']],external_review='OPEN')
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
