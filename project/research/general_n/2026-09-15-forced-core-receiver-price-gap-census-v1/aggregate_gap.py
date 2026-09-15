#!/usr/bin/env python3
from __future__ import annotations
import csv, json, sys
from pathlib import Path

EXPECTED=170

def read_rows(path: Path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def i(r,k): return int(r[k])

def main():
    if len(sys.argv)!=4:
        raise SystemExit('usage: aggregate_gap.py AUDIT_PLAN SHARDS OUTDIR')
    plan=Path(sys.argv[1]); shards=Path(sys.argv[2]); out=Path(sys.argv[3]); out.mkdir(parents=True,exist_ok=True)
    primary=read_rows(plan/'PRIMARY_CANDIDATE_RESULTS.tsv')
    if len(primary)!=EXPECTED: raise SystemExit(f'expected {EXPECTED} primary candidates, got {len(primary)}')
    pby={(i(r,'layer'),i(r,'state_id')):r for r in primary}
    if len(pby)!=EXPECTED: raise SystemExit('duplicate primary candidate key')

    rows=[]
    for p in sorted(shards.rglob('RESULT.tsv')):
        rr=read_rows(p)
        if len(rr)!=1: raise SystemExit(f'{p}: expected one result row, got {len(rr)}')
        rows.extend(rr)
    if len(rows)!=EXPECTED: raise SystemExit(f'expected {EXPECTED} shard rows, got {len(rows)}')
    rby={(i(r,'layer'),i(r,'state_id')):r for r in rows}
    if len(rby)!=EXPECTED: raise SystemExit('duplicate census key')
    if set(rby)!=set(pby):
        raise SystemExit(f'key mismatch missing={sorted(set(pby)-set(rby))} extra={sorted(set(rby)-set(pby))}')

    enriched=[]; mismatches=[]; gaps=[]
    for key in sorted(pby):
        p=pby[key]; r=rby[key]
        checks={
            'S': i(r,'S')==i(p,'S'),
            'Emax': i(r,'Emax')==i(p,'Emax'),
            'profiles_tested': i(r,'profiles_tested')==i(p,'profiles_tested'),
            'predicted_core_fail': i(r,'predicted_core_fail')==i(p,'core_fail'),
            'internal_profile_partition': i(r,'agg_fail')+i(r,'partition_gap_fail')+i(r,'exact_core_pass')==i(r,'profiles_tested'),
            'internal_core_partition': i(r,'agg_fail')+i(r,'partition_gap_fail')==i(r,'predicted_core_fail'),
        }
        if not all(checks.values()): mismatches.append({'key':key,'checks':checks,'primary_core_fail':i(p,'core_fail'),'row':r})
        e=dict(r)
        e['primary_core_fail']=p['core_fail']
        e['primary_core_capacity_fail']=p['core_capacity_fail']
        e['primary_core_high_fail']=p['core_high_fail']
        e['primary_last_core_h']=p['last_core_h']
        e['primary_last_core_r']=p['last_core_r']
        enriched.append(e)
        if i(r,'partition_gap_fail'):
            gaps.append(e)
    if mismatches:
        (out/'MISMATCHES.json').write_text(json.dumps(mismatches,indent=2,sort_keys=True)+'\n')
        raise SystemExit(f'{len(mismatches)} state-level census mismatches')

    fields=list(enriched[0].keys())
    with (out/'RESULTS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(enriched)
    with (out/'GAP_WITNESSES.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(gaps)

    totals={k:sum(i(r,k) for r in rows) for k in [
        'profiles_tested','agg_capacity_fail','agg_high_fail','agg_fail',
        'partition_only_fail','partition_high_only_fail','partition_gap_fail',
        'exact_core_pass','predicted_core_fail']}
    primary_core=sum(i(p,'core_fail') for p in primary)
    hard=[key for key,p in pby.items() if i(p,'last_core_h') in (4,5)]
    hard_gap=sum(i(rby[k],'partition_gap_fail') for k in hard)
    hard_core=sum(i(pby[k],'core_fail') for k in hard)
    status='ZERO_GAP_ON_COMPLETE_170_CANDIDATE_UNIVERSES' if totals['partition_gap_fail']==0 else 'PARTITION_ONLY_GAPS_FOUND'
    summary={
        'schema':'forced-core-receiver-price-gap-census-v1',
        'candidate_state_count':EXPECTED,
        'coverage':'complete type-profile enumeration for all 170 forced-core discovery candidates',
        'status':status,
        'totals':totals,
        'authoritative_primary_core_fail':primary_core,
        'core_fail_count_exactly_reconciled':totals['predicted_core_fail']==primary_core,
        'partition_gap_state_count':len(gaps),
        'partition_gap_profile_count':totals['partition_gap_fail'],
        'primary_last_core_h_4_or_5_state_count':len(hard),
        'primary_last_core_h_4_or_5_core_fail_profiles':hard_core,
        'primary_last_core_h_4_or_5_partition_gap_profiles':hard_gap,
        'interpretation':(
            'Finite empirical exactness on these 170 complete candidate universes only; not a proof of general equivalence.'
            if not gaps else
            'At least one exact partition rejection is not captured by the scalar/fractional aggregate conditions; see GAP_WITNESSES.tsv.'
        ),
        'promotion_status':'ANALYTIC_CENSUS_ONLY_NOT_PROMOTED'
    }
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__': main()
