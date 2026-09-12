#!/usr/bin/env python3
"""Full stream agreement, complete case coverage, prior-model comparison and accounting."""
from collections import Counter
from pathlib import Path
import base64,gzip,hashlib,json
from evidence_io import read_bytes,records
from replay import gaps
HERE=Path(__file__).resolve().parent

def recover(folder,name):
    m=json.loads((folder/'EVIDENCE_STORAGE.json').read_text())['files'][name]
    stored=(folder/m['stored_file']).read_bytes()
    assert len(stored)==m['stored_bytes'] and hashlib.sha256(stored).hexdigest()==m['stored_sha256']
    raw=gzip.decompress(base64.b64decode(stored))
    assert len(raw)==m['original_bytes'] and hashlib.sha256(raw).hexdigest()==m['original_sha256']
    return raw

def capacities(rec,h):
    caps=sorted([min(rec['a']-rho,sum(h<=s<=rho for s in rec['s'])) for rho in rec['rho'] if rho>=h],reverse=True)
    return [sum(min(c,h) for c in caps)-j*h+min(sum(caps[:j]),j*(len(caps)-j)+j*(j-1)//2) for j in range(sum(c>h for c in caps)+1)]

def main():
    raw=read_bytes('frontier_results.jsonl');reference=read_bytes('reference_results.jsonl');assert raw==reference
    experiment_raw=(HERE/'EXPERIMENT.json').read_bytes();experiment=json.loads(experiment_raw)
    input_meta=json.loads((HERE/'input_verification.json').read_text())
    assert hashlib.sha256(experiment_raw).hexdigest()==input_meta['experiment_sha256']
    assert hashlib.sha256((HERE/'PLAN.md').read_bytes()).hexdigest()==experiment['plan_sha256']
    assert experiment['weights']==dict(load=1,heavy_mass=1,heavy_receiving=2,ordinary_transport=4)
    assert experiment['modes']==dict(fixed_k2=[2],all_k='0..a+1') and experiment['LP_used'] is False
    pool=records('pool_inputs.jsonl');result=records('frontier_results.jsonl');assert len(pool)==len(result)==5578
    old=HERE.parent/'2026-09-12-compatible-routing-catalogue-v1';assert read_bytes('pool_inputs.jsonl')==recover(old,'pool_inputs.jsonl')
    oldresult=[json.loads(line) for line in recover(old,'frontier_results.jsonl').splitlines()]
    oldcat=json.loads((old/'catalogue.json').read_text());position=oldcat['modes']['eligible'].index(13)
    keys={(r['layer'],r['state_id']) for r in pool};byrec={(r['layer'],r['state_id']):r for r in pool};assert len(keys)==5578
    sets={m:set() for m in ['fixed_k2','all_k']};counts=Counter();positive=[]
    for rec,row in zip(pool,result):
        key=rec['layer'],rec['state_id'];assert (row['layer'],row['state_id'])==key and set(row['modes'])==set(sets)
        for mode,data in row['modes'].items():
            witness=None
            for h,threshold in enumerate(data['thresholds'],2):
                assert threshold['h']==h and h<=max(rec['s']);counts['thresholds']+=1
                caps=capacities(rec,h);assert caps==threshold['capacities'];W=sum(s for s in rec['s'] if s>=h);ai=0;blocked=False
                for j,cap in enumerate(caps):
                    if cap<W:counts['capacity_bypasses']+=1;continue
                    attempt=threshold['attempts'][ai];ai+=1;counts['sender_count_attempts']+=1
                    assert attempt['j']==j and len(attempt['gaps'])==(1 if mode=='fixed_k2' else rec['a']+2)
                    assert all(type(v) is int for v in attempt['gaps']);counts['integer_gaps']+=len(attempt['gaps'])
                    value=max(attempt['gaps'])
                    if value<=0:blocked=True;break
                    positive.append(value)
                assert ai==len(threshold['attempts'])
                if not blocked:
                    assert h==data['thresholds'][-1]['h'];witness=h;break
            if witness is None:assert len(data['thresholds'])==max(rec['s'])-1
            assert witness==data['witness_h']
            if witness:sets[mode].add(key)
    assert sets['fixed_k2']<=sets['all_k']
    # Review the entire preceding recorded domain for template 13, including
    # gaps skipped by the new experiment's different stopping points.
    old_checks=0
    for row in oldresult:
        rec=byrec[row['layer'],row['state_id']]
        for threshold in row['modes']['eligible']['thresholds']:
            for attempt in threshold['attempts']:
                assert gaps(rec,threshold['h'],attempt['j'],[2])[0]==attempt['gaps'][position]
                old_checks+=1
    assert old_checks==28591
    old_catalogue={(r['layer'],r['state_id']) for r in oldresult if r['modes']['eligible']['witness_h']}
    oldsurvivors=json.loads(recover(old,'survivors.json'));old_pilot={(r['layer'],r['state_id']) for r in oldsurvivors if r['inherited_pilot_exclusion']}
    old_combined=old_catalogue|old_pilot
    prior=json.loads((HERE/'prior_exclusions.json').read_text())
    assert old_catalogue==set(map(tuple,prior['catalogue'])) and old_pilot==set(map(tuple,prior['pilot_only'])) and old_combined==set(map(tuple,prior['combined']))
    assert len(old_combined)==994
    coverage=json.loads(recover(old,'template_coverage.json'));old13={(r['layer'],r['state_id']) for r in coverage if 13 in r['single_template_ids']}
    newly=sets['all_k']-old_combined;combined=old_combined|sets['all_k']
    survivors=[r for r in pool if (r['layer'],r['state_id']) not in combined]
    (HERE/'survivors.json').write_text(json.dumps(survivors,separators=(',',':'))+'\n')
    (HERE/'new_exclusions.json').write_text(json.dumps(sorted(map(list,newly)),indent=2)+'\n')
    report=dict(status='PASS',pool=5578,closed_and_full_enumeration_byte_identical=True,
        original_result_bytes=len(raw),original_result_sha256=hashlib.sha256(raw).hexdigest(),**counts,
        minimum_best_positive_gap=min(positive),prior_template13_gaps_rechecked=old_checks,
        exclusions={m:len(v) for m,v in sets.items()},added_by_cutoff_variation=len(sets['all_k']-sets['fixed_k2']),
        prior_template13_recorded_winning_thresholds=len(old13),fixed_k2_additional_later_threshold_cases=sorted(map(list,sets['fixed_k2']-old13)),
        all_k_prior_pilot_only_overlap=sorted(map(list,sets['all_k']&old_pilot)),new_exclusions_over_prior_combined=len(newly),
        combined_exclusions=len(combined),combined_survivors=len(survivors),
        layers={layer:dict(pool=sum(r['layer']==layer for r in pool),fixed_k2=sum(k[0]==layer for k in sets['fixed_k2']),
                          all_k=sum(k[0]==layer for k in sets['all_k']),combined_survivors=sum(r['layer']==layer for r in survivors)) for layer in sorted({r['layer'] for r in pool})},
        external_review='OPEN')
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
