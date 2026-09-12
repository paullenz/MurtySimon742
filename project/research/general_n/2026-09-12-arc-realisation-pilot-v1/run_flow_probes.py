#!/usr/bin/env python3
from pathlib import Path
import json
from flow import selected_pattern,solve
from check_flow import verify_certificate
from storage import sha
HERE=Path(__file__).resolve().parent

def run():
    raw=(HERE/'pilot_inputs.json').read_bytes();inputs=json.loads(raw);records=[]
    for rec in inputs['sample']:
        a,b=rec['a'],rec['b'];selected=selected_pattern(rec)
        for method in ['first','last']:
            residual=set()
            for u,rho in enumerate(rec['rho']):
                available=[i for i in range(a) if (u,i) not in selected]
                chosen=available[:rho] if method=='first' else (available[-rho:] if rho else [])
                residual.update((u,i) for i in chosen)
            capacities=[rv+b-a-1 for rv in rec['rho']]
            result=solve(a,b,selected,residual,capacities);verify_certificate(a,b,selected,residual,capacities,result)
            records.append(dict(layer=rec['layer'],state_id=rec['state_id'],residual_method=method,
                selected=sorted(selected),residual=sorted(residual),capacities=capacities,flow_result=result,
                scope='One constructed cross pattern; no whole-state exclusion.'))
    # Any original pilot witness is analysed without changing or replacing its cross sets.
    originals=HERE/'runs/results.json'
    if originals.exists():
        for result in json.loads(originals.read_text()):
            if result['classification']!='VERIFIED_RELAXATION_WITNESS':continue
            from storage import read_model
            model=read_model(HERE/'runs'/result['model']['stored_file'],result['model']);vector=result['witness']['integer_vector']
            selected={tuple(n[1:]) for n,x in zip(model['variables'],vector) if n[0]=='x' and x}
            residual={tuple(n[1:]) for n,x in zip(model['variables'],vector) if n[0]=='r' and x}
            rec=model['record'];caps=[r+rec['b']-rec['a']-1 for r in rec['rho']]
            flow=solve(rec['a'],rec['b'],selected,residual,caps);verify_certificate(rec['a'],rec['b'],selected,residual,caps,flow)
            records.append(dict(layer=rec['layer'],state_id=rec['state_id'],residual_method='original_'+result['mode'],
                selected=sorted(selected),residual=sorted(residual),capacities=caps,flow_result=flow,scope='Original solver witness cross pattern only.'))
    return dict(schema='fixed-cross-flow-probes-v1',input_sha256=sha(raw),flow_plan_sha256=sha((HERE/'FLOW_PLAN.md').read_bytes()),records=records)

if __name__=='__main__':
    report=run();(HERE/'flow_probes.json').write_text(json.dumps(report,indent=2)+'\n')
    for r in report['records']:
        f=r['flow_result'];print(r['layer'],r['state_id'],r['residual_method'],f['status'],f['flow'],'/',f['required'],'empty',len(f['empty_eligibility_obligations']))
