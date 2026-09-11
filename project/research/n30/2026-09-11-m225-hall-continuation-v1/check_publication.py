#!/usr/bin/env python3
"""Scoped publication checks required by the project's preservation orders."""
from pathlib import Path
from hashlib import sha256
import argparse,json,re,subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    surfaces=[ROOT/'README.md',ROOT/'START_HERE_FOR_REVIEWERS.md',ROOT/'releases/REVIEW_READY_INDEX.md',
              HERE.parent/'2026-09-11-threshold-tail-v1/README.md']
    surfaces+=list(HERE.glob('*.md'))
    surfaces+=[ROOT/'project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md']
    broken=[];count=0
    for path in surfaces:
        for target in re.findall(r'\]\(([^\s)]+)\)',path.read_text()):
            if ':' in target or target.startswith('#'):continue
            target=target.split('#')[0]
            if not target:continue
            count+=1
            if not (path.parent/target).exists():broken.append([str(path.relative_to(ROOT)),target])
    assert not broken,broken
    readme=(ROOT/'README.md').read_text()
    index=readme.split('## Review-paper index',1)[1].split('## Governance',1)[0]
    for n,v in [(25,2),(27,2),(28,2),(29,4),(30,2)]:
        for kind in ['Reviewer_Manuscript','Verification_Companion']:
            target=f'releases/n{n}-reviewer-v{v}/N{n}_{kind}_v{v}.pdf'
            assert target in index and (ROOT/target).is_file(),target
    for p in surfaces[:3]:assert 'reviewer-v4' in p.read_text()
    bridge=ROOT/'project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md'
    assert sha256(bridge.read_bytes()).hexdigest()=='4a2333802f011a51eca60041aeb412dc157bf8adf99807cb59581b4274152f42'
    changes=subprocess.check_output(['git','diff','--name-only','b104846d222f09cb0d8bbf25ff9f51f6d1165bdf'],cwd=ROOT,text=True).splitlines()
    allowed={'README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md',
             'project/research/n30/2026-09-11-threshold-tail-v1/README.md'}
    for p in changes:
        assert p in allowed or p.startswith('project/research/n30/2026-09-11-m225-hall-continuation-v1/') or p.startswith('project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/') or p=='.github/workflows/n30-m225-scalar-excess.yml',p
    out={'status':'PASS','relative_links_checked':count,'broken_links':broken,
         'current_fixed_order_versions':{'25':2,'27':2,'28':2,'29':4,'30':2},
         'frozen_bridge_sha256_unchanged':True,'tracked_change_allowlist_passed':True,
         'scope':'Current entry pages and this checkpoint; no full historic-link audit claimed.'}
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
