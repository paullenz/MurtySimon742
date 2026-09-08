#!/usr/bin/env python3
"""N25 terminal-certificate audit, independent of all frozen checking source.
Exact subset-state matching rederives caps; one simultaneous refinement only.
This verifies terminal rows, NOT the omitted outer/column generation stages.
"""
import argparse, gzip, hashlib, json
from collections import Counter
from functools import lru_cache
from pathlib import Path


def need(ok, message):
    if not ok:
        raise ValueError(message)


def integer(x, lo, hi, name):
    need(type(x) is int and lo <= x <= hi, 'invalid integer: '+name)


def vector(v, length, lo, hi, name):
    need(type(v) is list and len(v)==length, 'invalid vector: '+name)
    for x in v:
        integer(x,lo,hi,name)


def loads(s):
    def invalid(x):
        raise ValueError('nonfinite JSON constant: '+x)
    def unique(pairs):
        d={}
        for k,v in pairs:
            need(k not in d,'duplicate JSON key: '+k)
            d[k]=v
        return d
    return json.loads(s,parse_constant=invalid,object_pairs_hook=unique)


@lru_cache(maxsize=200000)
def assignment_possible(labels, supplies, wanted):
    """Enumerate reachable subsets of distinct labels, one supplier at a time."""
    if wanted==0:
        return True
    if wanted>min(len(labels),len(supplies)):
        return False
    reachable={0}
    for supply in supplies:
        eligible=sum(1<<i for i,d in enumerate(labels) if d<=supply)
        following=set(reachable)
        for used in reachable:
            free=eligible & ~used
            while free:
                bit=free & -free
                free-=bit
                target=used|bit
                if target.bit_count()>=wanted:
                    return True
                following.add(target)
        reachable=following
    return False


def caps(d,rho,R):
    first=[]
    for b,rb in enumerate(rho):
        supplies=tuple(sorted(rb+rw for w,rw in enumerate(rho) if w!=b))
        feasible=[0]
        for q in range(1,min(len(d)-rb,len(rho)-1)+1):
            labels=tuple(d[i] for i in range(len(d)) if d[i]<rb+q and d[i]<=rb+R[i])
            if assignment_possible(labels,supplies,q):
                feasible.append(q)
        first.append(max(feasible))
    Q=sum(max(0,x-y) for x,y in zip(d,R))
    if sum(first)<Q:
        return first,first.copy()
    refined=[max(q for q in range(c+1) if sum(w!=b and rho[w]+first[w]>=q-1 for w in range(len(rho)))>=q) for b,c in enumerate(first)]
    return first,refined


def parse_state(key, R):
    need(type(key) is str,'state key must be string')
    raw=loads(key);need(type(raw) is list and len(raw)==4,'state shape')
    k,r,d,rho=raw
    integer(k,1,5,'k');integer(r,14,43-5*k,'r')
    vector(d,10,0,9-k,'d');need(d==sorted(d) and max(d)==9-k,'exact degree maximum')
    vector(rho,14,1,10,'rho');need(rho==sorted(rho) and sum(rho)==r,'residual sum/order')
    need(sum(d)==2*(r+2),'degree sum')
    vector(R,10,0,14,'R');need(sum(R)==r,'column sum')
    h=max(j for j in range(11) if sum(v>=j for v in rho)>=j)
    need(all(y>=max(0,x-h) for x,y in zip(d,R)),'column lower bound')
    return d,rho


def verify(ledger, certificate):
    cert=loads(certificate.read_text())
    need(cert['input_sha256']==hashlib.sha256(ledger.read_bytes()).hexdigest(),'input identity')
    expected={};source_rows=0
    with gzip.open(ledger,'rt',encoding='ascii') as f:
        for line in f:
            row=loads(line);source_rows+=1
            need(row['kind'] in {'pair_threshold','source_total','source_threshold','column_lower_bound','all_columns','survives'},'unknown disposition')
            if row['kind']!='survives':
                continue
            for col in row['witness']['survivors']:
                d,rho=parse_state(row['key'],col['columns'])
                key=(row['key'],tuple(col['columns']))
                need(key not in expected,'duplicate terminal input')
                vector(col['caps'],14,0,10,'caps');vector(col['refined_caps'],14,0,10,'refined caps')
                derived,refined=caps(d,rho,col['columns'])
                need(derived==col['caps'] and refined==col['refined_caps'],'source caps not independently justified')
                need(sum(refined)>=sum(max(0,x-y) for x,y in zip(d,col['columns'])),'not a terminal survivor')
                expected[key]=(d,rho,refined)
    observed=set();digest=hashlib.sha256();hist=Counter();minimum=None
    for row in cert['certificates']:
        d,rho=parse_state(row['key'],row['columns'])
        key=(row['key'],tuple(row['columns']))
        need(key in expected and key not in observed,'unexpected/duplicate certificate');observed.add(key)
        vector(row['caps'],14,0,10,'certificate caps')
        need(row['caps']==expected[key][2],'certificate source caps')
        w=row['witness'];S=w['subset']
        need(type(S) is list and S,'empty subset')
        for i in S:integer(i,0,9,'subset index')
        need(len(S)==len(set(S)),'repeated subset index')
        demand=sum(max(0,d[i]-row['columns'][i]) for i in S)
        upper=[min(c,sum(d[i]<rb+c and d[i]<=rb+row['columns'][i] for i in S)) for rb,c in zip(rho,row['caps'])]
        integer(w['required'],0,100,'required');integer(w['available'],0,140,'available')
        vector(w['by_source'],14,0,10,'source bounds')
        need(w['required']==demand and w['by_source']==upper and w['available']==sum(upper),'witness arithmetic')
        need(demand>sum(upper),'non-strict witness')
        slack=demand-sum(upper);minimum=slack if minimum is None else min(minimum,slack)
        hist[len(S)]+=1
        digest.update((json.dumps([key,row['caps'],S,demand,upper],separators=(',',':'))+'\n').encode())
    need(cert['survivors']==[],'unresolved terminal survivors')
    for k in ['checked','eliminated','surviving_columns','surviving_outer_states']:
        integer(cert[k],0,10000000,k)
    need(cert['checked']==cert['eliminated']==len(expected)==len(observed),'incomplete coverage/count')
    need(cert['surviving_columns']==cert['surviving_outer_states']==0,'nonzero survivor metadata')
    return {'status':'PASS','source_rows_read':source_rows,'terminal_columns':len(expected),'subset_size_histogram':dict(sorted(hist.items())),'minimum_strict_slack':minimum,'ordered_sha256':digest.hexdigest(),'matching':'reachable labelled-subset dynamic program','refinement_passes':1,'imports_frozen_verifiers':False,'whole_outer_domain_validated_by_this_program':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('candidate',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    need(not a.output.exists(),'output exists')
    results={name:verify(a.candidate/name/'primary_ledger.jsonl.gz',a.candidate/name/'hall_certificates.json') for name in ['d14_156','d14_156_k1']}
    need([r['terminal_columns'] for r in results.values()]==[171,1788],'production terminal counts')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps({'status':'PASS','scopes':results,'external_review':False},indent=2)+'\n')
    print(json.dumps(results,indent=2))
if __name__=='__main__':main()
