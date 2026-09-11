#!/usr/bin/env python3
"""Check the written mathematical tables and the current publication surfaces."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import runpy
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
BASE='d063c25445671c2588f5a619ecbc468e9698806d'
PREFIX='project/research/n30/2026-09-11-m225-hand-classification-v1/'
SURFACES=['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md',
          'project/research/n30/2026-09-11-m225-resource-envelope-v1/README.md',
          'project/research/n30/2026-09-11-threshold-tail-v1/README.md',
          'project/research/n30/2026-09-11-m225-hall-continuation-v1/README.md']


def table_after(text,header):
    part=text.split(header+'\n',1)[1]
    rows=[]
    for line in part.splitlines():
        if not line.startswith('|'):
            break
        cells=[x.strip() for x in line.strip('|').split('|')]
        if all(re.fullmatch(r'[-:]+',x) for x in cells):
            continue
        rows.append(cells)
    return rows


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    ap.add_argument('--tables-only',action='store_true')
    args=ap.parse_args()
    math=runpy.run_path(str(HERE/'verify_hand_classification.py'),run_name='table_definitions')
    proof=(HERE/'HAND_CLASSIFICATION.md').read_text()
    rows=table_after(proof,'| z | p=12,x=12 | p=13,x=11 | p=13,x=12 | p=13,x=13 |')
    pairs=[(12,12),(13,11),(13,12),(13,13)]
    got={pair:{} for pair in pairs}
    for row in rows:
        if not row[0].isdigit():
            continue
        z=int(row[0])
        for pair,cell in zip(pairs,row[1:]):
            if cell!='—':
                got[pair][z]=[int(v) for v in cell.split(',')]
    assert got==math['CAP4']
    rows=table_after(proof,'| y | z | Permitted k | Number |')
    got={}
    for y,z,ks,count in rows:
        if not y.isdigit():
            continue
        vals=list(map(int,ks.split(',')))
        assert len(vals)==int(count)
        got[int(y),int(z)]=vals
    assert got==math['CAP5']
    rows=table_after(proof,'| y | z | k ranges from Table 2 | Maximum Q6 over all permitted k and 1<=j<=k |')
    got={}
    for y,z,ks,maximum in rows:
        pair=int(y),int(z)
        assert list(map(int,ks.split(',')))==math['CAP5'][pair]
        got[pair]=int(maximum)
    assert got==math['CAP6_MAX']
    rows=table_after(proof,'| z | C2(z) | C3(z) | C4(z) | C5(z) | C6(z) |')
    capacities=0
    for z,*vals in rows:
        for h,value in enumerate(vals,2):
            if h>int(z):
                assert value=='—'
            else:
                assert int(value)==math['capacity'](h,int(z))
                capacities+=1
    rows=table_after(proof,'| Q | Number of profiles |')
    assert {int(q):int(n) for q,n in rows}=={18:64,19:29,20:6,21:1}
    assert not any(line.endswith(chr(92)) and not line.endswith(chr(92)*2) for line in proof.splitlines())
    out={'status':'PASS','written_cap4_cap5_cap6_tables_match':True,
         'written_capacity_entries_checked':capacities,'written_score_distribution_match':True}
    if not args.tables_only:
        surfaces=[ROOT/p for p in SURFACES]+sorted(HERE.glob('*.md'))
        count=0;broken=[]
        for f in surfaces:
            for target in re.findall(r'\]\(([^\s)]+)\)',f.read_text()):
                if ':' in target or target.startswith('#'):
                    continue
                target=target.split('#')[0]
                if target:
                    count+=1
                    if not (f.parent/target).exists():
                        broken.append([str(f.relative_to(ROOT)),target])
        assert not broken,broken
        index=(ROOT/'README.md').read_text().split('## Review-paper index',1)[1].split('## Governance',1)[0]
        for n,v in [(25,2),(27,2),(28,2),(29,4),(30,2)]:
            for kind in ['Reviewer_Manuscript','Verification_Companion']:
                path=f'releases/n{n}-reviewer-v{v}/N{n}_{kind}_v{v}.pdf'
                assert path in index and (ROOT/path).is_file()
        for f in surfaces[:3]:
            content=f.read_text()
            assert 'reviewer-v4' in content and '2026-09-11-m225-hand-classification-v1' in content
        bridge=ROOT/'project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md'
        assert sha256(bridge.read_bytes()).hexdigest()=='4a2333802f011a51eca60041aeb412dc157bf8adf99807cb59581b4274152f42'
        tracked=subprocess.check_output(['git','diff','--name-only',BASE],cwd=ROOT,text=True).splitlines()
        untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
        allowed=set(SURFACES)|{'.github/workflows/n30-m225-hand-classification.yml'}
        assert all(p in allowed or p.startswith(PREFIX) for p in tracked+untracked)
        out.update({'baseline':BASE,'relative_links_checked':count,'broken_links':broken,
                    'current_versions':{'n25':2,'n27':2,'n28':2,'n29':4,'n30':2},
                    'frozen_bridge_unchanged':True,'tracked_and_untracked_changes_within_scope':True,
                    'scope':'Current entry pages, three predecessor READMEs and new checkpoint; not all historical links.'})
    if args.output:
        args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
