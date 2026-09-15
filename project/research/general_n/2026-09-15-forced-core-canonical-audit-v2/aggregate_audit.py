#!/usr/bin/env python3
from __future__ import annotations
import csv, json, sys
from pathlib import Path

COMPARE=['layer','state_id','S','Emax','profiles_tested','paircap_fail','paircap_pass','incidence_fail','incidence_pass','pairhall_fail','pairhall_pass','targethall_fail','targethall_pass','cost_fail','cost_pass','core_fail','core_capacity_fail','core_high_fail','status']
EXPECTED_CANDIDATES=170
EXPECTED_SURVIVORS=136

def read_tsv(p):
    with Path(p).open(newline='') as f: return list(csv.DictReader(f,delimiter='\t'))

def main():
    if len(sys.argv)!=5: raise SystemExit('usage: aggregate_audit.py PLAN_DIR SHARDS_DIR REPLAY_TSV OUTDIR')
    plan=Path(sys.argv[1]); shards=Path(sys.argv[2]); replay=Path(sys.argv[3]); out=Path(sys.argv[4]); out.mkdir(parents=True,exist_ok=True)
    primary=read_tsv(plan/'PRIMARY_CANDIDATE_RESULTS.tsv')
    expected={(r['layer'],r['state_id']):r for r in primary}
    found=[]
    for p in sorted(shards.rglob('RESULT.tsv')): found.extend(read_tsv(p))
    got={(r['layer'],r['state_id']):r for r in found}
    if len(primary)!=EXPECTED_CANDIDATES or len(found)!=EXPECTED_CANDIDATES or set(got)!=set(expected):
        raise SystemExit(f'candidate key coverage mismatch primary={len(primary)} found={len(found)} unique={len(got)}')
    mism=[]
    for k in sorted(expected):
        a,b=expected[k],got[k]
        for col in COMPARE:
            if a[col]!=b[col]: mism.append({'layer':k[0],'state_id':k[1],'field':col,'primary':a[col],'independent':b[col]})
    if mism: raise SystemExit('independent exclusion mismatch: '+json.dumps(mism[:10]))
    rep=read_tsv(replay)
    if len(rep)!=EXPECTED_SURVIVORS or any(r['pass']!='1' or r['reason']!='PASS' for r in rep):
        bad=[r for r in rep if r['pass']!='1' or r['reason']!='PASS']
        raise SystemExit('survivor replay mismatch '+json.dumps(bad[:10]))
    ps=read_tsv(plan/'PRIMARY_SURVIVOR_RESULTS.tsv'); psm={r['state_id']:r for r in ps}; rm={r['state_id']:r for r in rep}
    if set(psm)!=set(rm): raise SystemExit('survivor key coverage mismatch')
    for sid,r in rm.items():
        p=psm[sid]
        for rc,pc in [('E','witness_E'),('cost','witness_cost'),('envelope','witness_envelope')]:
            if r[rc]!=p[pc]: raise SystemExit(f'survivor witness field mismatch {sid} {rc}: {r[rc]} != {p[pc]}')
    with (out/'INDEPENDENT_CANDIDATE_RESULTS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=found[0].keys(),delimiter='\t');w.writeheader();w.writerows(sorted(found,key=lambda r:(int(r['layer']),int(r['state_id']))))
    (out/'SURVIVOR_WITNESS_REPLAY.tsv').write_text(replay.read_text())
    summary={
      'schema':'canonical-forced-core-independent-audit-v2-final',
      'candidate_exclusions_compared':EXPECTED_CANDIDATES,'candidate_field_mismatches':0,
      'survivor_witnesses_replayed':EXPECTED_SURVIVORS,'survivor_witness_failures':0,
      'exact_candidate_compare_fields':COMPARE,
      'promotion_status':'AUDIT_COMPLETE_NOT_PROMOTED',
      'canonical_status_unchanged':{'exclusions':4626,'survivors':952,'whole_state_closures':3632},
      'provisional_if_separately_promoted':{'exclusions':4796,'survivors':782,'whole_state_closures':3802}
    }
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,sort_keys=True))
if __name__=='__main__': main()
