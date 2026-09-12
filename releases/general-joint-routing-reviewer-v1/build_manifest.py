#!/usr/bin/env python3
"""Pin current navigation, this release, and every direct mathematical/replay input."""
from pathlib import Path
import hashlib,json,platform
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-joint-routing-pilot-v1'


def main():
    paths={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'}
    for folder in [ROOT/RESEARCH,HERE]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                     and p.name not in ('MANIFEST.json','PUBLICATION_RECEIPT.json','pilot_results.jsonl','frontier_results.jsonl'))
    dependencies=[
        'project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md',
        'project/research/general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md',
        'project/research/general_n/2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md',
        'releases/general-heavy-load-reviewer-v1/MANIFEST.json',
        'releases/n34-reviewer-v2/MANIFEST.json','releases/n35-reviewer-v1/MANIFEST.json']
    for name in ['HEAVY_LOAD_FAMILY.md','README.md','AUDIT.md','evidence_io.py','EVIDENCE_STORAGE.json','remaining_states.json.gz.b64','application_verification.json','frontier_summary.json']:
        dependencies.append('project/research/general_n/2026-09-12-heavy-load-family-v1/'+name)
    paths.update(dependencies);artifacts={}
    for name in sorted(paths):
        data=(ROOT/name).read_bytes();artifacts[name]=dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    report=dict(schema='general-joint-routing-reviewer-v1',date='2026-09-12',repository='paullenz/MurtySimon742',
        unchanged_dependency_baseline='e64091d771888fa68d60f0c8292fce9accf82d1a',python=platform.python_version(),
        scope=dict(candidate_general_lemma=True,pilot_states=27,pilot_joint_exclusions=12,
                   corrected_full_pool=6307,old_hand_removals=192,frozen_templates=20,new_joint_exclusions=729,
                   additional_over_aggregate_catalog=563,catalog_survivors=5578,changed_fixed_order_ledgers=False,
                   improved_maximum_degree_bound=False,unrestricted_theorem=False,external_review='OPEN'),
        artifacts=artifacts,notes=[
            'The all-parameter lemma has a hand proof; finite exclusions require the recorded exact arithmetic.',
            'The preceding family manifest and complete baseline pin unchanged transitive dependencies.',
            'The manifest excludes itself and the publication receipt to avoid circular hashes.',
            'Original search streams are losslessly encoded with both stored and original hashes.',
            'Historical fixed-order proofs, evidence, ledgers and receipts are preserved.'])
    (HERE/'MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n');print('PINNED',len(artifacts),'artifacts')

if __name__=='__main__':main()
