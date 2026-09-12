#!/usr/bin/env python3
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
LAYERS=['n34-m289','n35-m306','n35-m307']

def decode(folder,name):
    meta=json.loads((folder/'EVIDENCE_STORAGE.json').read_text())['files'][name]
    data=(folder/meta['stored_file']).read_bytes()
    assert len(data)==meta['stored_bytes'] and hashlib.sha256(data).hexdigest()==meta['stored_sha256']
    raw=gzip.decompress(base64.b64decode(data))
    assert len(raw)==meta['original_bytes'] and hashlib.sha256(raw).hexdigest()==meta['original_sha256']
    return raw

def main():
    old=HERE.parent/'2026-09-12-compatible-routing-catalogue-v1'
    raw=decode(old,'pool_inputs.jsonl');pool=[json.loads(line) for line in raw.splitlines()]
    results=[json.loads(line) for line in decode(old,'frontier_results.jsonl').splitlines()]
    survivors=json.loads(decode(old,'survivors.json'))
    ids={(r['layer'],r['state_id']) for r in pool};assert len(pool)==len(ids)==5578
    assert [(r['layer'],r['state_id']) for r in pool]==[(r['layer'],r['state_id']) for r in results]
    catalogue={(r['layer'],r['state_id']) for r in results if r['modes']['eligible']['witness_h']}
    pilot={(r['layer'],r['state_id']) for r in survivors if r['inherited_pilot_exclusion']}
    combined=catalogue|pilot
    assert len(catalogue)==990 and len(pilot)==4 and catalogue.isdisjoint(pilot)
    assert {(r['layer'],r['state_id']) for r in survivors if r['combined_survives']}==ids-combined
    (HERE/'pool_inputs.jsonl').write_bytes(raw)
    (HERE/'prior_exclusions.json').write_text(json.dumps(dict(catalogue=sorted(map(list,catalogue)),pilot_only=sorted(map(list,pilot)),combined=sorted(map(list,combined))),separators=(',',':'))+'\n')
    lines=[str(len(pool))]
    for r in pool:
        assert r['a']==15 and r['b'] in (18,19) and min(r['rho'])>=1
        values=[LAYERS.index(r['layer']),r['state_id'],r['a'],r['b'],r['t'],len(r['s']),*r['s'],len(r['rho']),*r['rho']]
        lines.append(' '.join(map(str,values)))
    (HERE/'engine_input.txt').write_text('\n'.join(lines)+'\n')
    report=dict(status='PASS',pool=5578,prior_catalogue=990,prior_pilot_only=4,prior_combined=994,
        pool_sha256=hashlib.sha256(raw).hexdigest(),experiment_sha256=hashlib.sha256((HERE/'EXPERIMENT.json').read_bytes()).hexdigest(),external_review='OPEN')
    (HERE/'input_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
