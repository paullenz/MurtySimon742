#!/usr/bin/env python3
"""Exact tight-block equality/rigidity certificates; independent of q."""
import base64, gzip, json
from pathlib import Path

def read_inputs(base):
    lines=(base/'INDEPENDENT_INPUT.txt').read_text().splitlines()
    ps=[]
    for line in lines[1:]:
        t=line.split();layer=t.pop(0);x=list(map(int,t));sid,a,b,n=x[:4];s=x[4:4+n]
        nr=x[4+n];rho=x[5+n:];assert len(rho)==nr==b and len(s)==a
        ps.append(dict(layer=layer,state_id=sid,a=a,b=b,s=s,rho=rho))
    assert len(ps)==int(lines[0])==4588
    old=json.loads(gzip.decompress(base64.b64decode((base/'RESULTS.json.gz.b64').read_bytes())))
    active={(p['layer'],p['state_id']) for p in old['rows'] if p['active']}
    assert len(active)==952
    return ps,active

def inspect(p):
    rows=[]
    for d in sorted(set(p['s'])):
        if d<1 or p['s'].count(d)!=d:continue
        H=[u for u,r in enumerate(p['rho']) if r>=d]
        M=[u for u,r in enumerate(p['rho']) if r==d-1]
        if len(H)!=d or len(M)!=d:continue
        L=[u for u,r in enumerate(p['rho']) if r<d-1]
        K=[i for i,s in enumerate(p['s']) if s!=d and s>sum(p['rho'][u]>=s for u in L)]
        capacity=min(p['rho'][u] for u in H)
        excess_lower=sum(max(0,len(K)-p['rho'][u]) for u in H)
        pair_upper=d*(d-1)//2
        rows.append(dict(d=d,H=H,M=M,L=L,K=K,required_union=len(K),residual_union_capacity=capacity,
            rejected=len(K)>capacity,preliminary_pair_lower=excess_lower,
            preliminary_pair_upper=pair_upper,preliminary_pair_rejected=excess_lower>pair_upper))
    return rows

def run(base):
    ps,active=read_inputs(base);rows=[]
    for p in ps:
        checks=inspect(p)
        if checks:rows.append(dict(layer=p['layer'],state_id=p['state_id'],active=(p['layer'],p['state_id']) in active,
            rejected=any(c['rejected'] for c in checks),checks=checks))
    return dict(status='INTERNAL_WHOLE_STATE_CERTIFICATES_NOT_PROMOTED',input_count=len(ps),active_count=len(active),
        applicable_states=len(rows),rejected_states=sum(r['rejected'] for r in rows),
        active_rejected=[{'layer':r['layer'],'state_id':r['state_id']} for r in rows if r['active'] and r['rejected']],rows=rows)

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('base',type=Path);ap.add_argument('output',type=Path);a=ap.parse_args()
    r=run(a.base);a.output.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2))
