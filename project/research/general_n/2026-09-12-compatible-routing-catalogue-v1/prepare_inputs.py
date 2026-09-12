#!/usr/bin/env python3
"""Recover the complete old survivor pool and write deterministic engine input."""
from pathlib import Path
import base64,gzip,hashlib,json
HERE=Path(__file__).resolve().parent
LAYERS=['n34-m289','n35-m306','n35-m307']

def recover(folder,name):
    meta=json.loads((folder/'EVIDENCE_STORAGE.json').read_text())['files'][name]
    stored=(folder/meta['stored_file']).read_bytes()
    assert len(stored)==meta['stored_bytes'] and hashlib.sha256(stored).hexdigest()==meta['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert len(raw)==meta['original_bytes'] and hashlib.sha256(raw).hexdigest()==meta['original_sha256']
    return raw

def pool():
    heavy=HERE.parent/'2026-09-12-heavy-load-family-v1';joint=HERE.parent/'2026-09-12-joint-routing-pilot-v1'
    source=recover(heavy,'remaining_states.json');routing=recover(joint,'frontier_results.jsonl')
    previous=[json.loads(line) for line in routing.splitlines()]
    ids={(r['layer'],r['state_id']) for r in previous if r['modes']['joint'] is None}
    summary_raw=(joint/'frontier_summary.json').read_bytes();summary=json.loads(summary_raw)
    assert len(previous)==6307 and len(ids)==5578 and ids==set(map(tuple,summary['survivor_ids']))
    rows=sorted([r for r in json.loads(source) if (r['layer'],r['state_id']) in ids],key=lambda r:(r['layer'],r['state_id']))
    assert len(rows)==5578 and len({(r['layer'],r['state_id']) for r in rows})==5578
    return rows,dict(heavy_remaining_states=hashlib.sha256(source).hexdigest(),joint_frontier_results=hashlib.sha256(routing).hexdigest(),joint_frontier_summary=hashlib.sha256(summary_raw).hexdigest())

def main():
    rows,hashes=pool();cat=json.loads((HERE/'catalogue.json').read_text())
    (HERE/'pool_inputs.jsonl').write_text(''.join(json.dumps(r,separators=(',',':'))+'\n' for r in rows))
    lines=[str(len(cat['templates']))]
    for template in cat['templates']:
        weights={tuple(d):v for k,d,v in template['weights']}
        fields=[weights.get((k,),0) for k in ['heavy_mass','load','pair_capacity','heavy_receiving','selected_balance']]
        for kind in ['all_transport','forced_transport']:
            tails=sorted((d[1],v) for d,v in weights.items() if d[0]==kind);fields.append(len(tails))
            for k,v in tails:fields.extend([k,v])
        lines.append(' '.join(map(str,fields)))
    for mode in ['heavy_only','selected_degree','eligible']:
        ids=cat['modes'][mode];lines.append(' '.join(map(str,[len(ids),*ids])))
    lines.append(str(len(rows)))
    for r in rows:
        assert r['a']==15 and r['b'] in (18,19) and r['t']>0 and min(r['rho'])>=1
        values=[LAYERS.index(r['layer']),r['state_id'],r['a'],r['b'],r['t'],len(r['s']),*r['s'],len(r['rho']),*r['rho']]
        lines.append(' '.join(map(str,values)))
    (HERE/'engine_input.txt').write_text('\n'.join(lines)+'\n')
    report=dict(status='PASS',states=len(rows),layers={layer:sum(r['layer']==layer for r in rows) for layer in LAYERS},
        input_hashes=hashes,catalogue_sha256=hashlib.sha256((HERE/'catalogue.json').read_bytes()).hexdigest(),
        pool_sha256=hashlib.sha256((HERE/'pool_inputs.jsonl').read_bytes()).hexdigest(),external_review='OPEN')
    (HERE/'input_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
