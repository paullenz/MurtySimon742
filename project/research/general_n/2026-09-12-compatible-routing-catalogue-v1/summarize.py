#!/usr/bin/env python3
"""Coverage accounting, survivors and post-replay template compression."""
from collections import Counter
from pathlib import Path
import json
from evidence_io import records
HERE=Path(__file__).resolve().parent

def main():
    pool=records('pool_inputs.jsonl');results=records('frontier_results.jsonl')
    cat=json.loads((HERE/'catalogue.json').read_text());ids=cat['modes']['eligible']
    byrec={(r['layer'],r['state_id']):r for r in pool}
    sets={m:{(r['layer'],r['state_id']) for r in results if r['modes'][m]['witness_h']} for m in cat['modes']}
    pilot=HERE.parent/'2026-09-12-compatible-routing-pilot-v1'
    sample={(r['layer'],r['state_id']) for r in json.loads((pilot/'pilot_inputs.json').read_text())['sample']}
    pilotfail=set(map(tuple,json.loads((pilot/'verification.json').read_text())['survivors']))
    old=sample-pilotfail;inherited=old-sets['eligible'];combined=old|sets['eligible']
    modes={m:len(v) for m,v in sets.items()}
    layers={};strata={}
    for layer in sorted({r['layer'] for r in pool}):
        keys={k for k in byrec if k[0]==layer}
        layers[layer]=dict(pool=len(keys),catalogue_excluded=len(keys&sets['eligible']),pilot_only=len(keys&inherited),
                           combined_excluded=len(keys&combined),combined_survivors=len(keys-combined))
        for zero in (False,True):
            group={k for k in keys if (0 in byrec[k]['s'])==zero}
            strata[layer+('/zero-demand' if zero else '/positive-demand')]=dict(pool=len(group),catalogue_excluded=len(group&sets['eligible']),combined_survivors=len(group-combined))
    obligations={};single=Counter();common_counts=Counter();hcounts=Counter();ordinary_states=[];needs_forced=[]
    ordinary={t['id'] for t in cat['templates'] if not any(d[0]=='forced_transport' for kind,d,w in t['weights'])}
    assignments=[];single13=[]
    for row in results:
        mode=row['modes']['eligible'];h=mode['witness_h']
        if h is None:continue
        key=row['layer'],row['state_id'];hcounts[h]+=1;common=set(ids);allordinary=True
        for attempt in mode['thresholds'][-1]['attempts']:
            works={i for i,g in zip(ids,attempt['gaps']) if g>0};assert works
            obligations[key+(h,attempt['j'])]=works;common&=works;allordinary &= bool(works&ordinary)
        single.update(common);common_counts[len(common)]+=1
        (ordinary_states if allordinary else needs_forced).append(list(key))
        if 13 in common:single13.append(dict(layer=key[0],state_id=key[1],h=h))
        assignments.append(dict(layer=key[0],state_id=key[1],h=h,single_template_ids=sorted(common),ordinary_only_at_recorded_threshold=allordinary))
    uncovered=set(obligations);chosen=[]
    while uncovered:
        template=min(ids,key=lambda ti:(-sum(ti in obligations[key] for key in uncovered),ti))
        covered={key for key in uncovered if template in obligations[key]};assert covered
        chosen.append(dict(template_id=template,new_sender_count_obligations=len(covered)));uncovered-=covered
    assert len(sets['eligible'])==990 and len(combined)==994
    survivors=[dict(**rec,catalogue_survives=(rec['layer'],rec['state_id']) not in sets['eligible'],
                    inherited_pilot_exclusion=(rec['layer'],rec['state_id']) in inherited,
                    combined_survives=(rec['layer'],rec['state_id']) not in combined) for rec in pool if (rec['layer'],rec['state_id']) not in sets['eligible']]
    (HERE/'survivors.json').write_text(json.dumps(survivors,separators=(',',':'))+'\n')
    (HERE/'template_coverage.json').write_text(json.dumps(assignments,separators=(',',':'))+'\n')
    compression=dict(selection_timing='Post-replay analysis; not the frozen input catalogue',method='Greedy cover of recorded positive sender-count obligations, ties by template ID; no minimality claim',
        covered_whole_states=len(sets['eligible']),sender_count_obligations=len(obligations),selected=chosen,
        ordinary_only_whole_states_at_recorded_threshold=len(ordinary_states),recorded_witnesses_using_forced_tails=needs_forced,
        scope='No new weights or state exclusions. The subset covers the recorded winning thresholds, not all possible thresholds.')
    (HERE/'compression.json').write_text(json.dumps(compression,indent=2)+'\n')
    report=dict(schema='compatible-routing-full-pool-summary-v1',pool=5578,seeds=20,templates=len(cat['templates']),
        exclusions=modes,catalogue_survivors=5578-len(sets['eligible']),pilot_sample=29,pilot_exclusions=19,
        pilot_exclusions_retained=len(old&sets['eligible']),pilot_only_exclusions=sorted(map(list,inherited)),
        newly_excluded_beyond_pilot=len(sets['eligible']-old),combined_exclusions=len(combined),combined_survivors=5578-len(combined),
        layers=layers,strata=strata,winning_thresholds=dict(sorted(hcounts.items())),
        single_template_support={str(k):v for k,v in sorted(single.items())},
        states_needing_more_than_one_template_at_recorded_threshold=common_counts[0],
        compact_hand_template_id=13,compact_hand_template_whole_states=len(single13),
        compact_hand_template_by_layer_and_h={str(k):v for k,v in sorted(Counter((r['layer'],r['h']) for r in single13).items())},
        compressed_subset_templates=len(chosen),ordinary_only_at_recorded_threshold=len(ordinary_states),
        full_pool_replay=True,solver_used=False,changed_fixed_order_ledgers=False,improved_maximum_degree_threshold=False,
        unrestricted_theorem=False,external_review='OPEN')
    (HERE/'frontier_summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
