#!/usr/bin/env python3
"""Check the frozen selection protocol, final accounting and compressed coverage."""
from pathlib import Path
from math import gcd
from functools import reduce
import hashlib,json
from evidence_io import records,read_bytes
HERE=Path(__file__).resolve().parent

def primitive(raw):
    d=reduce(gcd,[abs(w) for k,desc,w in raw if w],0) or 1
    return tuple(sorted((k,tuple(desc),w//d) for k,desc,w in raw if w))

def main():
    cat=json.loads((HERE/'catalogue.json').read_text());pilot=HERE.parent/'2026-09-12-compatible-routing-pilot-v1'
    original=(pilot/'envelopes.json').read_bytes();assert hashlib.sha256(original).hexdigest()==cat['pilot_envelopes_sha256']
    possible={primitive(e['weights']) for e in json.loads(original) if e['mode']!='joint_transport'}
    ranked=sorted(possible,key=lambda v:(sum(abs(w) for k,d,w in v),len(v),v));assert len(ranked)==155
    assert [primitive(s['weights']) for s in cat['seeds']]==ranked[:20]
    templates=[primitive(t['weights']) for t in cat['templates']]
    assert len(templates)==len(set(templates))==31 and [t['id'] for t in cat['templates']]==list(range(31))
    seeds=set(ranked[:20]);heavy={primitive([t for t in s if t[1][0] not in ('all_transport','forced_transport','selected_balance')]) for s in seeds}
    selected=heavy|{primitive([t for t in s if t[1][0] not in ('all_transport','forced_transport')]) for s in seeds}
    eligible=selected|seeds
    for mode,wanted in [('heavy_only',heavy),('selected_degree',selected),('eligible',eligible)]:
        assert {templates[i] for i in cat['modes'][mode]}==wanted
    input_meta=json.loads((HERE/'input_verification.json').read_text())
    assert hashlib.sha256((HERE/'catalogue.json').read_bytes()).hexdigest()==input_meta['catalogue_sha256']
    assert hashlib.sha256(read_bytes('pool_inputs.jsonl')).hexdigest()==input_meta['pool_sha256']
    output=records('frontier_results.jsonl');pool=records('pool_inputs.jsonl');keys={(r['layer'],r['state_id']) for r in pool}
    sets={m:{(r['layer'],r['state_id']) for r in output if r['modes'][m]['witness_h']} for m in cat['modes']}
    assert sets['heavy_only']<=sets['selected_degree']<=sets['eligible']
    summary=json.loads((HERE/'frontier_summary.json').read_text());verify=json.loads((HERE/'verification.json').read_text())
    assert summary['exclusions']=={m:len(s) for m,s in sets.items()}==verify['exclusions']
    inherited=set(map(tuple,verify['inherited_pilot_only']));combined=sets['eligible']|inherited
    assert inherited.isdisjoint(sets['eligible']) and inherited<=keys
    assert summary['combined_exclusions']==len(combined)==994 and summary['combined_survivors']==len(keys-combined)==4584
    survivors=json.loads(read_bytes('survivors.json'))
    assert {(r['layer'],r['state_id']) for r in survivors}==keys-sets['eligible']
    for r in survivors:
        key=r['layer'],r['state_id'];assert r['catalogue_survives'] and r['inherited_pilot_exclusion']==(key in inherited) and r['combined_survives']==(key not in combined)
    compression=json.loads((HERE/'compression.json').read_text());ids=cat['modes']['eligible'];chosen={r['template_id'] for r in compression['selected']}
    assert len(chosen)==11 and chosen<=set(ids)
    cases=0;single13=0;ordinary=0
    ordinaryids={t['id'] for t in cat['templates'] if all(d[0]!='forced_transport' for k,d,w in t['weights'])}
    coverage=json.loads(read_bytes('template_coverage.json'));cover={(r['layer'],r['state_id']):r for r in coverage}
    assert set(cover)==sets['eligible']
    for r in output:
        mode=r['modes']['eligible']
        if not mode['witness_h']:continue
        common=set(ids);allordinary=True
        for attempt in mode['thresholds'][-1]['attempts']:
            winners={ti for ti,g in zip(ids,attempt['gaps']) if g>0}
            assert winners&chosen;cases+=1;common&=winners;allordinary &= bool(winners&ordinaryids)
        c=cover[r['layer'],r['state_id']]
        assert c['single_template_ids']==sorted(common) and c['ordinary_only_at_recorded_threshold']==allordinary
        single13+=13 in common;ordinary+=allordinary
    assert cases==compression['sender_count_obligations']==6314
    assert single13==summary['compact_hand_template_whole_states']==707
    assert ordinary==summary['ordinary_only_at_recorded_threshold']==989
    report=dict(status='PASS',ranked_pilot_vectors=155,frozen_seeds=20,templates=31,mode_sizes={m:len(v) for m,v in cat['modes'].items()},
        complete_survivor_accounting=True,compressed_templates=11,compressed_sender_count_obligations=cases,
        single_hand_template_whole_states=single13,ordinary_only_at_recorded_threshold=ordinary,
        combined_survivors=4584,external_review='OPEN')
    (HERE/'catalogue_and_summary_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
