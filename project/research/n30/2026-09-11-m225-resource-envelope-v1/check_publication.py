#!/usr/bin/env python3
"""Check this checkpoint's current entry links and permitted changes."""
from pathlib import Path
from hashlib import sha256
import argparse,json,re,subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
BASE='34763cb17ce554a27e57643cfb8e74882e66fc86'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args()
    rels=['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md',
          'project/research/n30/2026-09-11-threshold-tail-v1/README.md',
          'project/research/n30/2026-09-11-m225-hall-continuation-v1/README.md']
    surfaces=[ROOT/p for p in rels]+sorted(HERE.glob('*.md'))
    count=0;broken=[]
    for f in surfaces:
        for target in re.findall(r'\]\(([^\s)]+)\)',f.read_text()):
            if ':' in target or target.startswith('#'):continue
            target=target.split('#')[0]
            if not target:continue
            count+=1
            if not (f.parent/target).exists():broken.append([str(f.relative_to(ROOT)),target])
    assert not broken,broken
    readme=(ROOT/'README.md').read_text();index=readme.split('## Review-paper index',1)[1].split('## Governance',1)[0]
    for n,v in [(25,2),(27,2),(28,2),(29,4),(30,2)]:
        for kind in ['Reviewer_Manuscript','Verification_Companion']:
            path=f'releases/n{n}-reviewer-v{v}/N{n}_{kind}_v{v}.pdf'
            assert path in index and (ROOT/path).is_file()
    for f in surfaces[:3]:
        text=f.read_text();assert 'reviewer-v4' in text and '2026-09-11-m225-resource-envelope-v1' in text
    bridge=ROOT/'project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md'
    assert sha256(bridge.read_bytes()).hexdigest()=='4a2333802f011a51eca60041aeb412dc157bf8adf99807cb59581b4274152f42'
    tracked=subprocess.check_output(['git','diff','--name-only',BASE],cwd=ROOT,text=True).splitlines()
    permitted=set(rels)|{'.github/workflows/n30-m225-four-envelopes.yml'}
    for p in tracked:
        assert p in permitted or p.startswith('project/research/n30/2026-09-11-m225-resource-envelope-v1/'),p
    out={'status':'PASS','baseline':BASE,'relative_links_checked':count,'broken_links':broken,
         'current_versions':{'n25':2,'n27':2,'n28':2,'n29':4,'n30':2},
         'frozen_bridge_unchanged':True,'tracked_changes_within_scope':True,
         'scope':'Current reviewer entry pages, predecessor README notices and the new checkpoint; not a full historic-link audit.'}
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
