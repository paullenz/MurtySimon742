#!/usr/bin/env python3
"""Pin the general-family release, current navigation and direct replay inputs."""
from pathlib import Path
import hashlib
import json
import platform

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-heavy-load-family-v1'


def main():
    paths={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'}
    for folder in [ROOT/RESEARCH,HERE]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and p.name not in ('MANIFEST.json','PUBLICATION_RECEIPT.json')
            and p.name not in ('frontier_results.jsonl','profile_results.jsonl','remaining_states.json'))
    dependencies=[
        'project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md',
        'project/research/general_n/2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md',
        'project/research/general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md',
        'project/reviews/n34/2026-09-12-heavy-independent-v1/HAND_PROOF.md',
        'project/reviews/n34/2026-09-12-heavy-independent-v1/README.md']
    for name in ['check_frontier.py','FRONTIER.csv','enumerate_frontier.cpp','enumeration.log']:
        dependencies.append('project/research/n34/2026-09-12-frontier-v1/'+name)
    for name in ['certificate_io.py','CERTIFICATE_STORAGE.json','fixed.jsonl.gz.b64','adaptive.jsonl.gz.b64']:
        dependencies.append('project/research/n34/2026-09-12-equality-v1/'+name)
    for name in ['t2.jsonl','t3.jsonl','verification.json','PROOF.md']:
        dependencies.append('project/research/n35/2026-09-12-candidate-v1/'+name)
    paths.update(dependencies);artifacts={}
    for name in sorted(paths):
        data=(ROOT/name).read_bytes();artifacts[name]=dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    report=dict(schema='general-heavy-load-reviewer-v1',date='2026-09-12',repository='paullenz/MurtySimon742',
        unchanged_dependency_baseline='398b8d949c244f7229a8ba723fb11b5fbdb7c536',python=platform.python_version(),
        scope=dict(candidate_all_threshold_family=True,explicit_incoming_penalty=True,demand_only_corollaries=True,
                   state_records=14031,family_exclusions=871,alternative_envelope_exclusions=595,
                   remaining_after_mass_and_family=8280,profile_records=1453,excluded_layer_profile_instances=45,
                   changed_fixed_order_ledgers=False,external_review='OPEN',unrestricted_theorem=False),
        artifacts=artifacts,notes=[
            'The hand proof establishes the parameter family; finite tests corroborate it and measure its reach.',
            'Unchanged transitive dependencies remain at the pinned complete repository baseline.',
            'The manifest excludes itself and the publication receipt to avoid circular hashes.',
            'Complete study streams and survivors are stored losslessly, with original and encoded hashes.',
            'Historical fixed-order ledgers and prior publication receipts are preserved.'])
    (HERE/'MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PINNED',len(artifacts),'artifacts')


if __name__=='__main__':main()
