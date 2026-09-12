#!/usr/bin/env python3
"""Freeze first/middle/last representatives before compatibility solver work."""
from collections import defaultdict
from pathlib import Path
import hashlib, importlib.util, json
HERE=Path(__file__).resolve().parent

def select():
    old=HERE.parent/'2026-09-12-heavy-load-family-v1'
    spec=importlib.util.spec_from_file_location('prior_heavy_evidence',old/'evidence_io.py')
    reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
    raw=reader.read_bytes('remaining_states.json')
    summary_path=HERE.parent/'2026-09-12-joint-routing-pilot-v1/frontier_summary.json'
    summary_raw=summary_path.read_bytes();summary=json.loads(summary_raw)
    ids=set(map(tuple,summary['survivor_ids']))
    records=[r for r in json.loads(raw) if (r['layer'],r['state_id']) in ids]
    assert len(records)==len(ids)==5578
    strata=defaultdict(list)
    for rec in records:strata[rec['layer'],rec['original_method'],min(rec['s'])==0].append(rec)
    chosen=[]
    for key,rows in sorted(strata.items()):
        rows.sort(key=lambda r:r['state_id'])
        chosen.extend(rows[i] for i in sorted({0,len(rows)//2,len(rows)-1}))
    chosen.sort(key=lambda r:(r['layer'],r['state_id']))
    assert len(chosen)==29
    return dict(schema='compatible-routing-pilot-selection-v1',baseline_commit='580c6692749d274725439ddb0bb4957e192792e7',
        pool=5578,selected=len(chosen),selection='First, middle and last state ID in each layer / original proof method / zero-demand-presence stratum; deduplicated indices.',
        input_hashes=dict(heavy_remaining_states=hashlib.sha256(raw).hexdigest(),joint_frontier_summary=hashlib.sha256(summary_raw).hexdigest()),
        strata={str(k):len(v) for k,v in sorted(strata.items())},sample=chosen)

if __name__=='__main__':
    report=select();(HERE/'pilot_inputs.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='sample'},indent=2))
