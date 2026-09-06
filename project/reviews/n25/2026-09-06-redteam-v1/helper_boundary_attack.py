#!/usr/bin/env python3
"""Document a source-cap helper defect outside the candidate's dimensions.
This test imports the two historical helpers only to expose their boundary
behaviour. The third arithmetic audit imports neither implementation.
"""
from pathlib import Path
import importlib.util
import json

ROOT=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent


def main():
    modules=[]
    for name in ('primary','independent'):
        path=ROOT/'N25_Full_Chain_Candidate_2026-09-06_v1'/('general_'+name+'.py')
        spec=importlib.util.spec_from_file_location('boundary_'+name,path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        module.A=15;module.B=9;modules.append(module)
    ds=(0,)*15;rs=(1,)*9
    first=modules[0].source_caps(ds,rs);second=modules[1].neighbours_bound(ds,rs,None)
    assert first==[14]*9 and second==[8]*9
    modules[0].matches=lambda labels,supplies: len(labels)<=len(supplies) and all(d<=c for d,c in zip(reversed(labels),supplies))
    assert modules[0].source_caps(ds,rs)==second
    result=dict(status='OUT_OF_SCOPE_HELPER_DEFECT_REPRODUCED',a=15,b=9,degrees=ds,residuals=rs,
                primary_caps=first,independent_caps=second,available_distinct_suppliers=8,
                reason='zip() in matches() silently truncates when there are too few suppliers',
                direction='Overestimates capacity; cannot by itself cause an unsound rejection',
                proposed_length_guard_tested=True,
                audited_candidate_a=[8,9,10],affects_audited_candidate=False,
                scope_explanation='In every audited scope, q<=a-1<=9 and b-1>=13, so supplier exhaustion cannot occur.')
    (OUT/'helper_boundary_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main()
