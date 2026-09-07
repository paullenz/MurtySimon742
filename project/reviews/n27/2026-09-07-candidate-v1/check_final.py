#!/usr/bin/env python3
"""Independent direct replay of final pair and supplement-budget certificates.
No imports from any search program. Checks complete coverage and stored input hashes.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import gzip,hashlib,json
ROOT=Path(__file__).resolve().parent

def key(row):return json.dumps(row,separators=(',',':'))

def run(e):
    prefix=ROOT/f'd15_{e}'
    source=Path(str(prefix)+'_survivors.jsonl.gz')
    originals=[json.loads(s) for s in gzip.open(source,'rt')]
    expected={key(row) for row in originals};assert len(expected)==len(originals)
    summary=json.loads(Path(str(prefix)+'_pair_summary.json').read_text())
    assert summary['input_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
    certs=json.load(gzip.open(str(prefix)+'_pair_certificates.json.gz','rt'))
    covered=set();thresholds=Counter()
    for item in certs:
        row=item['row'];w=item['witness'];state,k,r,d,rho,R,c=row
        kr=key(row);assert kr in expected and kr not in covered;covered.add(kr)
        j=w['threshold'];assert 1<=j<=max(d)
        S=[i for i,x in enumerate(d) if x>=j]
        demand=sum(max(0,d[i]-R[i]) for i in S)
        pairs=[(u,v) for u,v in combinations(range(len(rho)),2) if rho[u]+rho[v]>=j]
        assert S==w['subset'] and demand==w['required'] and len(pairs)==w['available_pairs'] and demand>len(pairs)
        thresholds[str(j)]+=1
    leftovers=[json.loads(s) for s in gzip.open(str(prefix)+'_pair_survivors.jsonl.gz','rt')]
    remaining={key(row) for row in leftovers};assert len(remaining)==len(leftovers)
    assert not remaining&covered and expected==remaining|covered
    assert summary['checked']==len(expected) and summary['eliminated']==len(covered) and summary['surviving_columns']==len(remaining)
    assert dict(thresholds)==summary['threshold_counts']
    if remaining:
        spath=Path(str(prefix)+'_pair_survivors.jsonl.gz')
        data=json.loads(Path(str(prefix)+'_supplement_certificates.json').read_text())
        assert data['input_sha256']==hashlib.sha256(spath.read_bytes()).hexdigest()
        supplied=set()
        for item in data['certificates']:
            row=item['row'];w=item['witness'];state,k,r,d,rho,R,c=row;a=len(d);b=len(rho)
            kr=key(row);assert kr in remaining and kr not in supplied;supplied.add(kr)
            demand=[max(0,di-ri) for di,ri in zip(d,R)]
            allowed=[{v for v in range(b) if d[i]-rho[v]<c[v] and d[i]-rho[v]<=R[i]} for i in range(a)]
            assert all(demand[i]<=len(allowed[i]) for i in range(a))
            forced=[sum(v in allowed[i] and demand[i]==len(allowed[i]) and demand[i]>0 for i in range(a)) for v in range(b)]
            possible=set()
            for i in range(a):
                for v in allowed[i]:
                    for u in range(b):
                        if u==v or rho[v]+rho[u]<d[i]:continue
                        lower=max(forced[v],1,d[i]-rho[v]+1)
                        if lower<=c[v] and lower<=rho[u]+c[u]+1:possible.add(tuple(sorted((u,v))))
            assert w['kind']=='supplement_pair_budget'
            assert w['demand_by_label']==demand and w['eligible_sources']==[sorted(s) for s in allowed]
            assert w['forced_by_source']==forced and {tuple(p) for p in w['allowed_pairs']}==possible
            assert len(w['allowed_pairs'])==len(possible) and sum(demand)==w['required'] and len(possible)==w['available']
            assert sum(demand)>len(possible)
        assert supplied==remaining and data['checked']==data['eliminated']==len(remaining)
        assert data['surviving_columns']==0 and not data['survivors']
    return {'edges':e,'pair_certificates':len(certs),'supplement_certificates':len(remaining),'unresolved':0}

if __name__=='__main__':
    result={'status':'PASS','scopes':[run(e) for e in (183,182)],'external_review':False}
    (ROOT/'FINAL_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
