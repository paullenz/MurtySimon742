#!/usr/bin/env python3
"""Pin current navigation, this package, and all direct replay/proof inputs."""
from pathlib import Path
import hashlib,json,platform
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-routing-tail-projection-v1'
RAW={'pilot_results.jsonl','profile_results.jsonl','state_comparison.json','boundary_results.jsonl','boundary_state_comparison.json'}


def main():
    paths={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'}
    for folder in [ROOT/RESEARCH,HERE]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                     and p.name not in RAW|{'MANIFEST.json','PUBLICATION_RECEIPT.json'})
    for package in ['general-joint-routing-reviewer-v1','general-heavy-load-reviewer-v1','n34-reviewer-v2','n35-reviewer-v1']:
        paths.add('releases/'+package+'/MANIFEST.json')
    paths.update('project/research/general_n/'+p for p in [
        '2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md',
        '2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md',
        '2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md'])
    for name in ['HEAVY_LOAD_FAMILY.md','evidence_io.py','EVIDENCE_STORAGE.json','profile_results.jsonl.gz.b64','frontier_results.jsonl.gz.b64','profile_summary.json','frontier_summary.json','application_verification.json']:
        paths.add('project/research/general_n/2026-09-12-heavy-load-family-v1/'+name)
    for name in ['JOINT_ROUTING_LEMMA.md','pilot_inputs.json','multiplier_catalog.json','frontier_summary.json']:
        paths.add('project/research/general_n/2026-09-12-joint-routing-pilot-v1/'+name)
    for name in ['FRONTIER.csv','check_frontier.py','enumerate_frontier.cpp','enumeration.log']:
        paths.add('project/research/n34/2026-09-12-frontier-v1/'+name)
    artifacts={}
    for name in sorted(paths):
        b=(ROOT/name).read_bytes();artifacts[name]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
    report=dict(schema='general-routing-tail-reviewer-v1',date='2026-09-12',repository='paullenz/MurtySimon742',
        unchanged_dependency_baseline='fcdacbf32e79930977f7da77697f4b6f90b18ca0',python=platform.python_version(),
        scope=dict(candidate_general_tail_projection=True,candidate_closed_equality_rigidity=True,pilot_profiles=27,
                   pilot_exclusions=9,full_layer_profile_instances=1453,prior_profile_exclusions=45,new_profile_exclusions=114,
                   remaining_profiles=1294,templates=44,scalar_additional_over_ordinary_cap=9,prior_joint_state_survivors=5578,
                   new_state_exclusions=0,changed_fixed_order_ledgers=False,improved_maximum_degree_threshold=False,
                   unrestricted_theorem=False,external_review='OPEN'),artifacts=artifacts,notes=[
            'General parameter claims have hand proofs; finite coverage claims require exact replay.',
            'Five original streams are stored losslessly with original and encoded hashes.',
            'Preceding current manifests and the complete baseline pin unchanged transitive evidence.',
            'This manifest excludes itself and the publication receipt to avoid circular hashes.',
            'The zero additional-state result is part of the scope; profile simplification is not a new fixed-order closure.'])
    (HERE/'MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n');print('PINNED',len(artifacts),'artifacts')

if __name__=='__main__':main()
