#!/usr/bin/env python3
"""Scalar tight-label block necessary conditions; no q enumeration."""
import argparse, base64, csv, gzip, hashlib, json
from collections import Counter
from pathlib import Path

CATALOGUE_SHA256 = '2c6bb11ec3c6dfb45a07b511c1e85c8c44898201c0f045630e0f622ee93647eb'

def inspect(p):
    out=[]
    for d,k in sorted(Counter(p['s']).items()):
        if d<1 or sum(r>=d for r in p['rho'])!=d: continue
        labels=[i for i,x in enumerate(p['s']) if x==d]
        sources=[v for v,r in enumerate(p['rho']) if r>=d]
        receivers=[v for v,r in enumerate(p['rho']) if k-1<=r<d]
        capacities=[min(d,max(0,p['rho'][v]+p['b']-p['a']-1)) for v in receivers]
        out.append(dict(d=d,k=k,labels=labels,sources=sources,receivers=receivers,
            capacities=capacities,count_fail=len(receivers)<k,
            capacity_fail=sum(capacities)<d*k,required=d*k,available=sum(capacities)))
    return out

def run(catalogue,ledger34,ledger35):
    raw=gzip.decompress(base64.b64decode(catalogue.read_bytes()))
    assert hashlib.sha256(raw).hexdigest()==CATALOGUE_SHA256
    ps=json.loads(raw)
    ledgers={l:{int(x['state']) for x in csv.DictReader(p.open(),delimiter='\t')}
             for l,p in [('n34-m289',ledger34),('n35-m306',ledger35)]}
    rows=[]
    for p in ps:
        active=p['combined_survives'] and p['state_id'] not in ledgers[p['layer']]
        checks=inspect(p)
        rows.append(dict(layer=p['layer'],state_id=p['state_id'],active=active,
            rejected=any(c['count_fail'] or c['capacity_fail'] for c in checks),checks=checks))
    active=[r for r in rows if r['active']]
    assert len(active)==952
    return dict(status='INTERNAL_WHOLE_STATE_CERTIFICATES_NOT_PROMOTED',catalogue_sha256=CATALOGUE_SHA256,
        catalogue_count=len(rows),combined_count=sum(p['combined_survives'] for p in ps),
        active_count=len(active),all_rejected=sum(r['rejected'] for r in rows),
        active_rejected=[{'layer':r['layer'],'state_id':r['state_id']} for r in active if r['rejected']],rows=rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('repository',type=Path);ap.add_argument('output',type=Path)
    args=ap.parse_args(); base=args.repository/'project/research/general_n'
    result=run(base/'2026-09-12-compatible-routing-catalogue-v1/survivors.json.gz.b64',
        base/'2026-09-13-alternative-attacks-v1/WHOLE_STATE_LEDGER.tsv',
        base/'2026-09-13-alternative-attacks-v1/WHOLE_STATE_LEDGER_N35.tsv')
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))

if __name__=='__main__':main()
