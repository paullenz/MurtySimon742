#!/usr/bin/env python3
"""Check current reviewer links, written transfer table, and publication scope."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
BASE='d680ddd208d338b019d00492f9498e6da2acfdbc'
PREFIX='project/research/n30/2026-09-11-assembled-hand-route-v1/'
SURFACES=['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md']+[
    f'project/research/n30/{folder}/README.md' for folder in [
    '2026-09-11-m225-hand-classification-v1','2026-09-11-m225-resource-envelope-v1',
    '2026-09-11-threshold-tail-v1','2026-09-11-m225-hall-continuation-v1','2026-09-09-delta17-v1']]


def threshold(h,w):
    if not w:return 0
    z=h
    while z*(z-1)+h*(h+1)<2*w:z+=1
    return z


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);ap.add_argument('--tables-only',action='store_true');args=ap.parse_args()
    text=(HERE/'TWELVE_LABEL_TRANSFER.md').read_text()
    table=text.split('| k,l | W5 before | W5 after | gamma5 drop |\n',1)[1].split('\n\n',1)[0]
    rows=[]
    for line in table.splitlines():
        fields=[v.strip() for v in line.strip('|').split('|')]
        if ',' not in fields[0]:continue
        k,l=map(int,fields[0].split(','));before,after,drop=map(int,fields[1:])
        assert before==6*k+5*l and after==5*(k+l)
        assert threshold(5,before)-threshold(5,after)==drop
        rows.append((k,l))
    assert rows==[(11,0),(11,1),(12,0)]
    for k,l in [(10,0),(10,1),(10,2),(11,0),(11,1)]:
        assert threshold(4,5*k+4*l)-threshold(4,4*(k+l))==1
    assert [threshold(3,4*9+3*l)-threshold(3,3*(9+l)) for l in range(4)]==[2,1,1,1]
    assert [threshold(3,4*10+3*l)-threshold(3,3*(10+l)) for l in range(3)]==[1,2,1]
    for f in HERE.glob('*.md'):
        assert not any(line.endswith(chr(92)) and not line.endswith(chr(92)*2) for line in f.read_text().splitlines())
    out={'status':'PASS','written_transfer_payment_tables_match':True}
    if not args.tables_only:
        surfaces=[ROOT/p for p in SURFACES]+sorted(HERE.glob('*.md'))
        count=0;broken=[]
        for f in surfaces:
            for target in re.findall(r'\]\(([^\s)]+)\)',f.read_text()):
                if ':' in target or target.startswith('#'):continue
                target=target.split('#')[0]
                if target:
                    count+=1
                    if not (f.parent/target).exists():broken.append([str(f.relative_to(ROOT)),target])
        assert not broken,broken
        index=(ROOT/'README.md').read_text().split('## Review-paper index',1)[1].split('## Governance',1)[0]
        for n,v in [(25,2),(27,2),(28,2),(29,4),(30,2)]:
            for kind in ['Reviewer_Manuscript','Verification_Companion']:
                path=f'releases/n{n}-reviewer-v{v}/N{n}_{kind}_v{v}.pdf'
                assert path in index and (ROOT/path).is_file()
        for f in surfaces[:3]:
            content=f.read_text()
            assert 'reviewer-v4' in content and '2026-09-11-assembled-hand-route-v1' in content
        bridge=ROOT/'project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md'
        assert sha256(bridge.read_bytes()).hexdigest()=='4a2333802f011a51eca60041aeb412dc157bf8adf99807cb59581b4274152f42'
        changed=subprocess.check_output(['git','diff','--name-only',BASE],cwd=ROOT,text=True).splitlines()
        new=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
        allowed=set(SURFACES)|{'.github/workflows/n30-assembled-hand-route.yml'}
        assert all(p in allowed or p.startswith(PREFIX) for p in changed+new)
        out.update({'baseline':BASE,'relative_links_checked':count,'broken_links':broken,
                    'current_versions':{'n25':2,'n27':2,'n28':2,'n29':4,'n30':2},
                    'frozen_bridge_unchanged':True,'all_local_changes_within_scope':True,
                    'scope':'Three current entry points, five predecessor READMEs, and every new Markdown file; not all historical links.'})
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':main()
