#!/usr/bin/env python3
"""Recover both prior original streams and independently reconstruct the sample."""
from collections import defaultdict
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent

def recover(folder,name):
    meta=json.loads((folder/'EVIDENCE_STORAGE.json').read_text())['files'][name]
    stored=(folder/meta['stored_file']).read_bytes()
    assert len(stored)==meta['stored_bytes'] and hashlib.sha256(stored).hexdigest()==meta['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert len(raw)==meta['original_bytes'] and hashlib.sha256(raw).hexdigest()==meta['original_sha256']
    return raw

def main():
    heavy=HERE.parent/'2026-09-12-heavy-load-family-v1';joint=HERE.parent/'2026-09-12-joint-routing-pilot-v1'
    raw=recover(heavy,'remaining_states.json');old=json.loads(raw)
    routing=[json.loads(l) for l in recover(joint,'frontier_results.jsonl').splitlines()]
    ids={(r['layer'],r['state_id']) for r in routing if r['modes']['joint'] is None}
    summary_raw=(joint/'frontier_summary.json').read_bytes();summary=json.loads(summary_raw)
    assert len(ids)==5578 and ids==set(map(tuple,summary['survivor_ids']))
    pool=[r for r in old if (r['layer'],r['state_id']) in ids];assert len(pool)==5578
    strata=defaultdict(list)
    for r in pool:strata[r['layer'],r['original_method'],0 in r['s']].append(r)
    sample=[]
    for rows in strata.values():
        rows.sort(key=lambda r:r['state_id'])
        sample.extend(rows[i] for i in {0,len(rows)//2,len(rows)-1})
    sample.sort(key=lambda r:(r['layer'],r['state_id']))
    inputs=json.loads((HERE/'pilot_inputs.json').read_text())
    assert inputs['sample']==sample and len(sample)==29
    assert inputs['input_hashes']==dict(heavy_remaining_states=hashlib.sha256(raw).hexdigest(),joint_frontier_summary=hashlib.sha256(summary_raw).hexdigest())
    assert inputs['strata']=={str(k):len(v) for k,v in sorted(strata.items())}
    report=dict(status='PASS',prior_routing_states=len(routing),eligible_survivors=len(pool),sample=len(sample),strata=len(strata),
        recovered_prior_original_streams=2,selection_independent_of_solver_outcomes=True,external_review='OPEN')
    (HERE/'selection_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
