#!/usr/bin/env python3
"""Pin compatible-routing evidence, direct inputs and current navigation."""
from pathlib import Path
import hashlib,json,platform
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-compatible-routing-pilot-v1'

def main():
    paths={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'}
    for folder in [ROOT/RESEARCH,HERE]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                     and p.name not in {'pilot_results.jsonl','MANIFEST.json','PUBLICATION_RECEIPT.json'})
    for package in ['general-routing-tail-reviewer-v1','general-joint-routing-reviewer-v1',
                    'general-heavy-load-reviewer-v1','n34-reviewer-v2','n35-reviewer-v1']:
        paths.add('releases/'+package+'/MANIFEST.json')
    paths.add('project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md')
    for name in ['HEAVY_LOAD_FAMILY.md','evidence_io.py','EVIDENCE_STORAGE.json','remaining_states.json.gz.b64']:
        paths.add('project/research/general_n/2026-09-12-heavy-load-family-v1/'+name)
    for name in ['JOINT_ROUTING_LEMMA.md','frontier_summary.json','EVIDENCE_STORAGE.json','frontier_results.jsonl.gz.b64']:
        paths.add('project/research/general_n/2026-09-12-joint-routing-pilot-v1/'+name)
    artifacts={}
    for name in sorted(paths):
        data=(ROOT/name).read_bytes();artifacts[name]=dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    report=dict(schema='general-compatible-routing-reviewer-v1',date='2026-09-12',repository='paullenz/MurtySimon742',
        unchanged_dependency_baseline='580c6692749d274725439ddb0bb4957e192792e7',python=platform.python_version(),
        scope=dict(candidate_compatible_routing_inequalities=True,candidate_general_potential_envelope=True,
                   compact_hand_example=True,prior_pool=5578,sample=29,
                   exclusions=dict(catalogue_free=2,selected_balance=3,separate_transport=19,joint_transport=19),
                   additional_from_eligibility=16,additional_whole_states_from_mixed_cuts=0,survivors=10,
                   full_pool_replay=False,integer_certificates=321,extracted_envelopes=321,
                   changed_fixed_order_ledgers=False,improved_maximum_degree_threshold=False,
                   unrestricted_theorem=False,external_review='OPEN'),artifacts=artifacts,notes=[
            'General implications and the compact example have hand proofs; finite applications require exact replay.',
            'The original solver stream is losslessly preserved, including all failures, proposals, repairs and timings.',
            'Clean rediscovery matches all result fields except measured elapsed times; original times remain preserved.',
            'Preceding current manifests and the complete baseline pin unchanged transitive evidence.',
            'This manifest excludes itself and the publication receipt to avoid circular hashes.',
            'The sample was selected before discovery and is not a random estimate of full-pool coverage.'])
    (HERE/'MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n');print('PINNED',len(artifacts),'artifacts')

if __name__=='__main__':main()
