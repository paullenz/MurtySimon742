#!/usr/bin/env python3
"""Pin the closed formula, full replay, review evidence and current navigation."""
from pathlib import Path
import hashlib,json,platform
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
RESEARCH='project/research/general_n/2026-09-12-closed-compatible-potential-v1'
RAW={'pool_inputs.jsonl','engine_input.txt','frontier_results.jsonl','reference_results.jsonl','survivors.json'}

def main():
    paths={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md'}
    for folder in [ROOT/RESEARCH,HERE]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                     and p.name not in RAW|{'MANIFEST.json','PUBLICATION_RECEIPT.json'})
    for package in ['general-compatible-catalogue-reviewer-v1','general-compatible-routing-reviewer-v1',
                    'general-routing-tail-reviewer-v1','general-joint-routing-reviewer-v1',
                    'general-heavy-load-reviewer-v1','n34-reviewer-v2','n35-reviewer-v1']:
        paths.add('releases/'+package+'/MANIFEST.json')
    paths.add('project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md')
    paths.add('project/research/general_n/2026-09-12-compatible-routing-pilot-v1/COMPATIBLE_ROUTING.md')
    for name in ['FIXED_POTENTIAL.md','AUDIT.md','catalogue.json','EVIDENCE_STORAGE.json','pool_inputs.jsonl.gz.b64',
                 'frontier_results.jsonl.gz.b64','survivors.json.gz.b64','template_coverage.json.gz.b64','verification.json']:
        paths.add('project/research/general_n/2026-09-12-compatible-routing-catalogue-v1/'+name)
    artifacts={}
    for name in sorted(paths):
        raw=(ROOT/name).read_bytes();artifacts[name]=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    report=dict(schema='general-closed-compatible-reviewer-v1',date='2026-09-12',repository='paullenz/MurtySimon742',
        unchanged_dependency_baseline='dfcfbc26da5c32b76b83c19de47e08cdc3ea4815',python=platform.python_version(),
        scope=dict(candidate_general_closed_local_maxima=True,local_candidate_bound_per_sender_class=59,
                   variable_ordinary_eligibility_cutoff=True,local_parameter_challenges=39902,pool=5578,
                   fixed_k2_exclusions=708,all_k_exclusions=832,new_exclusions_over_prior_combined=0,
                   combined_exclusions=994,combined_survivors=4584,integer_gaps=476427,
                   prior_template13_gaps_rechecked=28591,invalid_shortcut_examples=2,
                   full_pool_replay=True,solver_used=False,changed_fixed_order_ledgers=False,
                   improved_maximum_degree_threshold=False,unrestricted_theorem=False,external_review='OPEN'),
        artifacts=artifacts,notes=[
            'The general closed formula has a hand proof with explicit source-domain and integer-boundary conditions.',
            'Two independent full replay implementations produce byte-identical evidence; the finite checks do not prove the general bridge.',
            'The fixed-weight variable-cutoff family adds zero combined frontier exclusions; all earlier successes and remaining cases are retained.',
            'Five logical streams share four unique stored streams because the independent outputs are byte-identical; separate original logs and timings remain preserved.',
            'The prior 707 count was restricted to recorded winning thresholds; the full cutoff-2 search finds an already excluded case at a later threshold.',
            'Preceding current manifests and the complete baseline pin unchanged transitive evidence.',
            'This manifest excludes itself and the publication receipt to avoid circular hashes.'])
    (HERE/'MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n');print('PINNED',len(artifacts),'artifacts')

if __name__=='__main__':main()
