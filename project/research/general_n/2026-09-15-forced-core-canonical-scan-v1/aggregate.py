#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys,hashlib
from pathlib import Path

def main():
    if len(sys.argv)!=4:raise SystemExit('usage: aggregate.py PLAN_DIR SHARDS_DIR OUTDIR')
    plan=Path(sys.argv[1]);root=Path(sys.argv[2]);out=Path(sys.argv[3]);out.mkdir(parents=True,exist_ok=True)
    P=json.loads((plan/'PLAN.json').read_text()); expected={tuple(x) for x in P['target_keys']}
    rows=[]
    for p in sorted(root.rglob('RESULT.tsv')):
        with p.open(newline='') as f: rows.extend(csv.DictReader(f,delimiter='\t'))
    keys={(int(r['layer']),int(r['state_id'])) for r in rows}
    if len(rows)!=len(keys):raise SystemExit('duplicate scan rows')
    if keys!=expected:raise SystemExit(f'scan coverage mismatch missing={sorted(expected-keys)[:10]} extra={sorted(keys-expected)[:10]} rows={len(rows)}')
    excluded=[r for r in rows if r['status']=='FORCED_CORE_EXCLUDED']
    rescanned_surv=[r for r in rows if r['status']=='SURVIVES_FORCED_CORE']
    other=[r for r in rows if r['status'] not in {'FORCED_CORE_EXCLUDED','SURVIVES_FORCED_CORE'}]
    if other:raise SystemExit('unexpected status')
    with (plan/'PRESERVED_WITNESS_SURVIVORS.tsv').open(newline='') as f:retained=list(csv.DictReader(f,delimiter='\t'))
    final_surv=len(retained)+len(rescanned_surv)
    exkeys=sorted((int(r['layer']),int(r['state_id'])) for r in excluded)
    summary={'schema':'canonical-forced-core-scan-result-v1','source_results_sha256':P['source_results_sha256'],'input_survivors':P['canonical_survivors'],'stored_witness_retained':len(retained),'rescanned_targets':len(rows),'new_candidate_whole_state_exclusions':len(excluded),'rescanned_survivors':len(rescanned_surv),'remaining_survivors_if_candidates_valid':final_surv,'candidate_exclusions_n34':sum(a==0 for a,b in exkeys),'candidate_exclusions_n35':sum(a==1 for a,b in exkeys),'candidate_keys':[list(x) for x in exkeys],'promotion_status':'DISCOVERY_ONLY_NOT_PROMOTED','external_review':'OPEN'}
    with (out/'RESULTS.tsv').open('w',newline='') as f:
        if rows:
            w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t');w.writeheader();w.writerows(sorted(rows,key=lambda r:(int(r['layer']),int(r['state_id']))))
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    (out/'CANDIDATE_KEYS.tsv').write_text('layer\tstate_id\n'+''.join(f'{a}\t{b}\n' for a,b in exkeys))
    for name in ['RESULTS.tsv','SUMMARY.json','CANDIDATE_KEYS.tsv']:
        p=out/name;print(name,hashlib.sha256(p.read_bytes()).hexdigest())
    print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
