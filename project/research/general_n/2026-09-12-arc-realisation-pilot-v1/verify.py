#!/usr/bin/env python3
"""Archive replay, exact model reproduction, witness/cut checks and accounting."""
from pathlib import Path
import json
from collections import Counter
from model import build
from storage import read_model,sha
from check_witness import extract
from check_flow import verify_certificate
from prepare_inputs import select
from run_flow_probes import run as probes
HERE=Path(__file__).resolve().parent

def main():
    inputs=json.loads((HERE/'pilot_inputs.json').read_text());assert inputs==select()
    results=json.loads((HERE/'runs/results.json').read_text());assert len(results)==12
    environment=json.loads((HERE/'runs/environment.json').read_text())
    assert environment['input_sha256']==sha((HERE/'pilot_inputs.json').read_bytes())
    for name,digest in environment['source_hashes'].items():assert sha((HERE/name).read_bytes())==digest,name
    catalogue=json.loads((HERE/'runs/EVIDENCE_STORAGE.json').read_text())['files'];assert len(catalogue)==12
    expected=[(rec,mode) for rec in inputs['sample'] for mode in inputs['modes']]
    counts=Counter();model_rows=0;model_columns=0;solver_seconds=0;wall_seconds=0
    for result,(rec,mode) in zip(results,expected):
        assert (result['layer'],result['state_id'],result['mode'])==(rec['layer'],rec['state_id'],mode)
        model=read_model(HERE/'runs'/result['model']['stored_file'],result['model'])
        assert model==build(rec,mode)
        stem=rec['layer']+'-'+str(rec['state_id'])+'-'+mode+'.model.json'
        assert catalogue[stem]==result['model']
        assert sha((HERE/'runs'/result['log']).read_bytes())==result['log_sha256']
        if result['solver_file']:
            raw=(HERE/'runs'/result['solver_file']).read_bytes();assert sha(raw)==result['solver_sha256']
            solved=json.loads(raw);assert solved['status']==result['solver_status']
            assert extract(model,solved['raw_x'])==result['witness']
            if result['witness'] is None:
                assert result['classification']==('UNCERTIFIED_INFEASIBILITY_REPORT' if solved['status']==2 else 'OPEN_NO_VERIFIED_INCUMBENT')
            solver_seconds+=solved['original_solver_seconds']
        model_rows+=len(model['rows']);model_columns+=len(model['variables']);wall_seconds+=result['original_wall_seconds'];counts[result['classification']]+=1
    flow=json.loads((HERE/'flow_probes.json').read_text());assert flow==json.loads(json.dumps(probes()))
    patterns=Counter();trivial=0;nonempty=0;minimum_endpoint=[]
    for row in flow['records']:
        rec=next(r for r in inputs['sample'] if (r['layer'],r['state_id'])==(row['layer'],row['state_id']))
        selected=set(map(tuple,row['selected']));residual=set(map(tuple,row['residual']));f=row['flow_result']
        assert not selected&residual and all(rec['s'][i]<=rec['rho'][u] for u,i in selected)
        assert [sum(u==v for u,i in residual) for v in range(rec['b'])]==rec['rho']
        assert all(sum(k==i for u,k in selected)>=rec['s'][i] for i in range(rec['a']))
        verify_certificate(rec['a'],rec['b'],selected,residual,row['capacities'],f)
        q=[sum(w==u for w,i in selected) for u in range(rec['b'])]
        degrees=[sum(j==i for w,j in selected|residual) for i in range(rec['a'])]
        failed=[[u,i,degrees[i],q[u]] for u,i in sorted(selected) if degrees[i]<q[u]]
        minimum_endpoint.append(dict(layer=row['layer'],state_id=row['state_id'],residual_method=row['residual_method'],
            violated_minimum_endpoint_loads=failed,
            scope='Checks R_i+x_i>=q_u only. Full load with p_u requires a routing.'))
        patterns[f['status']]+=1
        if f['required']-f['flow']==len(f['empty_eligibility_obligations']):trivial+=1
        nonempty+=f['required']-len(f['empty_eligibility_obligations'])
    model_checks=json.loads((HERE/'model_verification.json').read_text());flow_checks=json.loads((HERE/'flow_verification.json').read_text())
    assert model_checks['status']==flow_checks['status']=='PASS'
    report=dict(status='PASS',pilot_cases=6,pilot_attempts=12,classifications=dict(counts),
        exact_model_rows_rebuilt=model_rows,exact_model_variables_rebuilt=model_columns,
        original_solver_seconds=solver_seconds,original_total_wall_seconds=wall_seconds,
        flow_probe_patterns=len(flow['records']),flow_classifications=dict(patterns),
        fixed_pattern_failures_explained_entirely_by_empty_eligibility=trivial,
        obligations_with_nonempty_eligibility_across_probes=nonempty,
        constructed_pattern_minimum_endpoint_checks=minimum_endpoint,
        tiny_linear_vs_combinatorial_checks=model_checks['tiny_linear_vs_combinatorial_checks'],
        fixed_cross_patterns_exhaustively_checked=flow_checks['fixed_cross_patterns'],
        compatible_tiny_cross_patterns=flow_checks['compatible_cross_patterns'],
        new_whole_state_exclusions=0,combined_exclusions=994,combined_survivors=4584,
        external_mathematical_review='OPEN',unrestricted_theorem=False)
    (HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    (HERE/'new_exclusions.json').write_text('[]\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
