#!/usr/bin/env python3
"""Deterministic six-state selection, independent of new solver outcomes."""
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent

def sha(raw):return hashlib.sha256(raw).hexdigest()

def select():
    prior=HERE.parent/'2026-09-12-closed-compatible-potential-v1'
    catalogue=(prior/'EVIDENCE_STORAGE.json').read_bytes()
    meta=json.loads(catalogue)['files']['survivors.json']
    stored=(prior/meta['stored_file']).read_bytes()
    assert len(stored)==meta['stored_bytes'] and sha(stored)==meta['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert len(raw)==meta['original_bytes'] and sha(raw)==meta['original_sha256']
    pool=json.loads(raw);assert len(pool)==4584
    sample=[];strata={}
    for layer in sorted({r['layer'] for r in pool}):
        rows=sorted((r for r in pool if r['layer']==layer),key=lambda r:r['state_id'])
        strata[layer]=len(rows)
        sample.extend(rows[i] for i in sorted({0,len(rows)//2,len(rows)-1}))
    assert len(sample)==6
    return dict(schema='arc-realisation-pilot-input-v1',baseline='31b5e78d9f80bc9328973db03ab6f497025e5ddc',
        plan_sha256=sha((HERE/'PLAN.md').read_bytes()),prior_catalogue_sha256=sha(catalogue),
        prior_survivors_sha256=sha(raw),pool=4584,strata=strata,selected=6,sample=sample,
        modes=['degree_routing','label_compatible'],solver_options=dict(time_limit=20.0,node_limit=100000,presolve=True),
        wall_guard_seconds=45,objective='zero; feasibility only')

if __name__=='__main__':
    result=select();(HERE/'pilot_inputs.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='sample'},indent=2))
