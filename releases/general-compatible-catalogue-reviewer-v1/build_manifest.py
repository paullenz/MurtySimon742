#!/usr/bin/env python3
"""Pin full-catalogue evidence, general reduction, direct inputs and navigation."""
from pathlib import Path
import hashlib,json,platform
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-compatible-routing-catalogue-v1'
RAW={'pool_inputs.jsonl','engine_input.txt','frontier_results.jsonl','survivors.json','template_coverage.json'}

def main():
    paths={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'}
    for folder in [ROOT/RESEARCH,HERE]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                     and p.name not in RAW|{'MANIFEST.json','PUBLICATION_RECEIPT.json','reproduction_environment.json'})
    for package in ['general-compatible-routing-reviewer-v1','general-routing-tail-reviewer-v1',
                    'general-joint-routing-reviewer-v1','general-heavy-load-reviewer-v1','n34-reviewer-v2','n35-reviewer-v1']:
        paths.add('releases/'+package+'/MANIFEST.json')
    paths.add('project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md')
    for name in ['HEAVY_LOAD_FAMILY.md','EVIDENCE_STORAGE.json','remaining_states.json.gz.b64']:
        paths.add('project/research/general_n/2026-09-12-heavy-load-family-v1/'+name)
    for name in ['JOINT_ROUTING_LEMMA.md','frontier_summary.json','EVIDENCE_STORAGE.json','frontier_results.jsonl.gz.b64']:
        paths.add('project/research/general_n/2026-09-12-joint-routing-pilot-v1/'+name)
    for name in ['COMPATIBLE_ROUTING.md','COMPACT_EXAMPLE.md','pilot_inputs.json','envelopes.json','verification.json',
                 'EVIDENCE_STORAGE.json','pilot_results.jsonl.gz.b64']:
        paths.add('project/research/general_n/2026-09-12-compatible-routing-pilot-v1/'+name)
    artifacts={}
    for name in sorted(paths):
        data=(ROOT/name).read_bytes();artifacts[name]=dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    report=dict(schema='general-compatible-catalogue-reviewer-v1',date='2026-09-12',repository='paullenz/MurtySimon742',
        unchanged_dependency_baseline='be45e9c540ece11290e6f07e3a31bd8dcc3da2d0',python=platform.python_version(),
        scope=dict(candidate_general_analytic_reduction=True,exact_q_elimination=True,at_most_five_p_candidates_per_H=True,
                   pool=5578,frozen_seed_vectors=20,templates_with_control_projections=31,
                   exclusions=dict(heavy_only=0,selected_degree=0,eligible=990),pilot_only_exclusions=4,
                   newly_excluded_beyond_pilot=975,combined_exclusions=994,combined_survivors=4584,
                   fixed_potential_whole_states=707,full_model_reduction_checks=28591,
                   exact_catalogue_gaps=1564007,post_replay_compressed_templates=11,
                   full_pool_replay=True,solver_used=False,changed_fixed_order_ledgers=False,
                   improved_maximum_degree_threshold=False,unrestricted_theorem=False,external_review='OPEN'),
        artifacts=artifacts,notes=[
            'The general analytic reduction has a hand proof; finite applications require exact maxima and complete sender-count coverage.',
            'Twenty seed vectors were ranked and frozen before full-pool replay; the eleven-template compression is explicitly post-replay.',
            'Four original pilot-only witnesses are retained separately, not lost or double counted.',
            'Five original streams are losslessly preserved with all gaps, failures, survivor flags and original hashes.',
            'Initial input preparation failure, source formatting warnings and original runtime are preserved.',
            'Preceding current manifests and the complete baseline pin unchanged transitive evidence.',
            'This manifest excludes itself, the publication receipt and fresh timing files to avoid circular or historical-timing claims.'])
    (HERE/'MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n');print('PINNED',len(artifacts),'artifacts')

if __name__=='__main__':main()
