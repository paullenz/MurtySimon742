#!/usr/bin/env python3
"""Bounded input/coverage diagnostic, not a full catalogue or graph replay.

Run beside SAMPLE_PROFILES.json and verify_screen.cpp. Optional --repo-root
compares each normalized sample against the pinned-schema repository file.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

SOURCE_PATH = ('project/research/general_n/'
               '2026-09-15-saturated-receiver-barrier-v1/RESCUE_PROFILES.json')
FIELDS = {'layer','state_id','a','b','t','s','rho','q'}


def tight_level_certificate(s: list[int], rho: list[int], d: int) -> dict:
    if d < 2:
        raise ValueError('The endpoint-cap diagnostic requires d >= 2')
    tight = [i for i, x in enumerate(s) if x == d]
    high = [u for u, r in enumerate(rho) if r >= d]
    low = [i for i, x in enumerate(s) if x <= d - 2]
    applicable = len(tight) == len(high) == d
    reject = applicable and len(low) < d
    return dict(d=d, tight_labels=tight, high_sources=high,
                permitted_K_labels=low, exact_block=applicable,
                excluded_by_this_screen=reject,
                tight_degree_required=2*d-1 if applicable else None,
                tight_degree_available=d-1+len(low) if applicable else None)


def diagnostics(row: dict) -> dict:
    if set(row) != FIELDS:
        raise ValueError(f"Unexpected field set for {row.get('state_id')}")
    a,b,s,rho,q = (row[x] for x in ('a','b','s','rho','q'))
    if len(s)!=a or len(rho)!=b or len(q)!=b:
        raise ValueError('Array lengths do not agree with a,b')
    if not all(isinstance(x,int) and x>=0 for x in s+rho+q):
        raise ValueError('Nonnegative integer arrays required')
    eligibility=[sum(x<=r for x in s) for r in rho]
    if any(qq>cap or qq+r>a for qq,r,cap in zip(q,rho,eligibility)):
        raise ValueError('Saved q violates elementary source bounds')
    forced={str(u):[i for i,x in enumerate(s) if x<=r]
            for u,(r,qq,cap) in enumerate(zip(rho,q,eligibility))
            if qq==cap}
    n=a+b+1
    e=b*(a+1)+row['t']
    levels=[tight_level_certificate(s,rho,d) for d in sorted(set(s)) if d>=2]
    return dict(layer=row['layer'],state_id=row['state_id'],schema_fields=sorted(row),
                n=n,edge_count_from_record=e,conjectured_upper=n*n//4,
                comparison='EQUALITY' if e==n*n//4 else ('ABOVE' if e>n*n//4 else 'BELOW'),
                pivot_surplus=row['t'],true_counterexample_minimum_surplus=1+(b-a-1)**2//4,
                residual_total=sum(rho),demand_total=sum(s),selected_total=sum(q),
                demand_histogram={str(k):v for k,v in sorted(Counter(s).items())},
                residual_histogram={str(k):v for k,v in sorted(Counter(rho).items())},
                saturated_source_selected_sets=forced,
                fully_identified_nonempty_selected_sets=len(forced),
                exact_F_adjacency_supplied=False,full_selected_sets_supplied=False,
                residual_label_sets_supplied=False,full_destination_assignment_supplied=False,
                psi_input_ready=False,incoming_ceilings=[r+b-a-1 for r in rho],
                levels=levels,whole_record_screen_reject=any(t['excluded_by_this_screen'] for t in levels))


def controls() -> list[dict]:
    results=[]
    for name,s,rho,d,match,reject in [
        ('one_fewer_low_label',[3,3,3,1,1],[3,3,3],3,True,True),
        ('boundary_is_not_excluded',[3,3,3,1,1,1],[3,3,3],3,True,False),
        ('high_count_must_match',[3,3,3,1,1],[3,3],3,False,False),
        ('exact_demand_level_must_match',[3,3,3,3,1,1],[3,3,3],3,False,False),
        ('d_minus_one_is_not_allowed',[4]*4+[3]*4,[4]*4,4,True,True),
    ]:
        r=tight_level_certificate(s,rho,d)
        assert r['exact_block']==match and r['excluded_by_this_screen']==reject
        results.append(dict(name=name,expected_match=match,expected_reject=reject,
                            scope='Scalar control only, not a canonical graph'))
    return results


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo-root',type=Path)
    args=ap.parse_args()
    root=Path(__file__).resolve().parent
    raw=(root/'SAMPLE_PROFILES.json').read_bytes()
    rows=json.loads(raw)
    if [r['state_id'] for r in rows]!=[232,978,979]:
        raise ValueError('This checkpoint is limited to the named three-row sample')
    source_compare='NOT_RUN_NO_COMPLETE_REPO_MOUNT'
    if args.repo_root is not None:
        allrows=json.loads((args.repo_root/SOURCE_PATH).read_text())
        lookup={(r['layer'],r['state_id']):r for r in allrows}
        for r in rows:
            assert lookup[(r['layer'],r['state_id'])]==r
        source_compare='PASS_ALL_THREE_NORMALIZED_RECORDS'
    results=[diagnostics(r) for r in rows]
    lines=[str(len(rows))]
    for r in rows:
        lines.append(' '.join(map(str,[r['state_id'],r['a'],r['b']]+r['s']+r['rho'])))
    cpp_input='\n'.join(lines)+'\n'
    with tempfile.TemporaryDirectory(prefix='coverage-diagnostic-') as tmp:
        exe=Path(tmp)/'verify'
        subprocess.run(['g++','-std=c++17','-O2','-Wall','-Wextra',str(root/'verify_screen.cpp'),'-o',str(exe)],check=True,timeout=20)
        cp=subprocess.run([str(exe)],input=cpp_input,text=True,stdout=subprocess.PIPE,check=True,timeout=20)
    observed=[list(map(int,line.split())) for line in cp.stdout.splitlines()]
    expected=[]
    for rr in results:
        for c in rr['levels']:
            expected.append([rr['state_id'],c['d'],len(c['tight_labels']),len(c['high_sources']),len(c['permitted_K_labels']),int(c['exact_block']),int(c['excluded_by_this_screen'])])
    assert observed==expected,(observed,expected)
    neg=controls()
    # q is absent from the certificate's arguments: both actual sampled q
    # vectors and any alternative q give the same statement on fixed s,rho.
    assert [r['state_id'] for r in results if r['whole_record_screen_reject']]==[978,979]
    assert all(r['comparison']=='EQUALITY' for r in results)
    assert all(not r['psi_input_ready'] for r in results)
    report=dict(status='PASS_BOUNDED_SCHEMA_AND_SCALAR_CERTIFICATE_DIAGNOSTIC',
                predecessor='a5cf0b19359e357010f0c0167321a6854e964fa2',
                source_path=SOURCE_PATH,source_blob='3d683af1884e9b9e6974b69553a5d1246f25f259',
                sample_sha256=hashlib.sha256(raw).hexdigest(),sample_extraction='Normalized manual extraction of the first three records from connector lines 1-193; not an entire-file byte comparison',
                source_comparison=source_compare,records_checked=len(rows),
                python_cpp_level_rows=len(expected),python_cpp_full_level_agreement=True,
                scalar_obstruction_ids=[978,979],non_rejected_sample_ids=[232],
                missing_Psi_inputs=['F-neighbour identities or certified common lower sets','monitored selected incidence identities beyond forced subsets','residual label sets or a proved core-defect bound','destination-superset proof when using a restricted destination set'],
                results=results,controls=neg,
                old_acceptance_pipeline_replay='NOT_RUN',full_catalogue_coverage_census='NOT_RUN',
                original_graph_enumeration='NOT_RUN',prior_exclusion_overlap='NOT_CHECKED',
                canonical_promotion='NOT_PERFORMED',independent_expert_review='OPEN')
    (root/'CHECK_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','records_checked','python_cpp_level_rows','scalar_obstruction_ids','non_rejected_sample_ids','sample_sha256')},indent=2))

if __name__=='__main__':
    main()
