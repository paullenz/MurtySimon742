#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,platform
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-arc-realisation-pilot-v1'
PRIOR=['n34-reviewer-v2','n35-reviewer-v1','general-heavy-load-reviewer-v1','general-joint-routing-reviewer-v1',
       'general-routing-tail-reviewer-v1','general-compatible-routing-reviewer-v1',
       'general-compatible-catalogue-reviewer-v1','general-closed-compatible-reviewer-v1']

def main():
    paths={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'}
    for folder in [ROOT/RESEARCH,HERE]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                     and p.name not in {'MANIFEST.json','PUBLICATION_RECEIPT.json'})
    paths.update('releases/'+p+'/MANIFEST.json' for p in PRIOR)
    paths.add('project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md')
    for name in ['README.md','EVIDENCE_STORAGE.json','survivors.json.gz.b64','verification.json']:
        paths.add('project/research/general_n/2026-09-12-closed-compatible-potential-v1/'+name)
    artifacts={}
    for path in sorted(paths):
        raw=(ROOT/path).read_bytes();artifacts[path]=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    result=dict(schema='general-arc-realisation-reviewer-v1',date='2026-09-12',repository='paullenz/MurtySimon742',
        unchanged_dependency_baseline='31b5e78d9f80bc9328973db03ab6f497025e5ddc',python=platform.python_version(),
        scope=dict(candidate_general_fixed_neighbourhood_flow_criterion=True,B_side_only=True,
                   pilot_cases=6,pilot_attempts=12,verified_pilot_incumbents=0,uncertified_infeasibility_reports=0,
                   open_time_limited_attempts=12,constructed_flow_probes=12,fixed_pattern_obstructions=12,
                   all_constructed_probes_already_fail_minimum_endpoint_load=True,
                   new_whole_state_exclusions=0,combined_exclusions=994,combined_survivors=4584,
                   tiny_fixed_patterns=729,tiny_model_checks=8192,original_models_rebuilt=12,
                   changed_fixed_order_ledgers=False,improved_maximum_degree_threshold=False,
                   unrestricted_theorem=False,external_review='OPEN'),artifacts=artifacts,notes=[
            'Conditional B-side sufficiency does not construct H[A] or establish graph edge-criticality.',
            'The fixed-pattern flow certificates do not exclude the corresponding demand/residual states.',
            'Every original pilot call ended without an incumbent. No solver status counts as proof.',
            'Clean validation reproduces deterministic evidence and original model bytes, not time-limited solver outcomes.',
            'This manifest excludes itself and the publication receipt to avoid circular hashes.'])
    (HERE/'MANIFEST.json').write_text(json.dumps(result,indent=2)+'\n');print('PINNED',len(artifacts),'artifacts')

if __name__=='__main__':main()
