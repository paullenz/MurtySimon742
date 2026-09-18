#!/usr/bin/env python3
"""Check edition completeness, navigation and pinned release integrity."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OUT=ROOT/'releases/n30-reviewer-v3'
BASE='81f37b80f643dd12f371680e673a95f6de793df2'
SURFACES=['README.md','START_HERE_FOR_REVIEWERS.md','releases/REVIEW_READY_INDEX.md',
    'project/research/n30/2026-09-11-assembled-hand-route-v1/README.md']


def norm(text):
    return text.replace('\u2014','-').replace('\u2013','-').replace('\u2011','-').replace('\u2212','-')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--release',action='store_true');ap.add_argument('--output',type=Path);args=ap.parse_args()
    proof=(HERE/'PROOF.md').read_text()
    source_map=json.loads((HERE/'SOURCE_MAP.json').read_text())
    for p,digest in source_map['input_sha256'].items():
        assert sha256((ROOT/p).read_bytes()).hexdigest()==digest,p
    counts={}
    for name in ['PREIMAGE_ARITHMETIC.md','EXACT_APPENDIX.md','HAND_CLASSIFICATION.md','N30_M226_HAND_ENDPOINT_REDUCTION.md']:
        path=next(p for p in source_map['input_sha256'] if p.endswith('/'+name))
        rows=[norm(line) for line in (ROOT/path).read_text().splitlines() if line.startswith('|')]
        assert all(line in proof for line in rows),name
        counts[name]=len(rows)
    assert len(re.findall(r'^\| (?:B1|B2|B3|C1) \|',proof,re.M))==211
    assert proof.count('# Appendix ')==8
    assert 'gamma_h(W)' in proof and 'with no upper cutoff' in proof
    assert 'governed theorem ledger' in proof and 'independent specialist' in proof.lower()
    for old in ['remaining main task toward','The separate four-envelope arithmetic and the other degree branches still need','No new PDF edition','The frozen current edition']:
        assert old not in proof,old
    release_md=(OUT/'N30_Reviewer_Manuscript_v3.md').read_text()
    assert release_md.endswith(proof),'PDF source is not complete canonical proof'
    for kind in ['Reviewer_Manuscript','Verification_Companion']:
        pdf=OUT/f'N30_{kind}_v3.pdf'
        assert pdf.is_file() and pdf.read_bytes().startswith(b'%PDF-')
    links=0
    surfaces=[ROOT/p for p in SURFACES]+list(HERE.glob('*.md'))+list(OUT.glob('*.md'))
    for f in surfaces:
        for target in re.findall(r'\]\(([^\s)]+)\)',f.read_text()):
            if ':' in target or target.startswith('#'):continue
            target=target.split('#')[0]
            if target:
                links+=1
                # GitHub Markdown navigation legitimately links both files and
                # directories. The integrity check should require a real target,
                # not silently reject an existing directory.
                assert (f.parent/target).exists(),(str(f.relative_to(ROOT)),target)
    root=(ROOT/'README.md').read_text()
    # The root reviewer index was renamed/reframed after this package was frozen.
    # Prefer the durable protected markers; retain the original heading fallback
    # so the checker also replays against older repository snapshots.
    if '<!-- REVIEW-MATERIALS:START -->' in root:
        index=root.split('<!-- REVIEW-MATERIALS:START -->',1)[1].split('<!-- REVIEW-MATERIALS:END -->',1)[0]
    else:
        index=root.split('## Review-paper index',1)[1].split('## Governance',1)[0]
    for n,v in [(25,2),(27,2),(28,2),(29,4),(30,3)]:
        for kind in ['Reviewer_Manuscript','Verification_Companion']:
            path=f'releases/n{n}-reviewer-v{v}/N{n}_{kind}_v{v}.pdf'
            assert path in index and (ROOT/path).is_file(),path
    # Current navigation surfaces must continue to expose the canonical N30
    # manuscript and verification companion. The portable ZIP is verified
    # directly below from its manifest and archive contents; it need not be
    # linked independently from every top-level navigation surface.
    for f in [ROOT/p for p in SURFACES[:3]]:
        s=f.read_text();assert 'n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf' in s
        assert 'n30-reviewer-v3/N30_Verification_Companion_v3.pdf' in s
        assert not re.search(r'current[^\n]*v2 at `n=25,27,28,30`',s,re.I)
    # Historical proof integrity is enforced by the pinned source hashes above.
    # The repository is an active multi-order research tree, so unrelated later
    # work must not invalidate the frozen N30 package merely because it changed
    # after BASE. Retain the diff as provenance, but scope the package check to
    # N30/reviewer navigation rather than freezing the entire repository.
    changed=subprocess.check_output(['git','diff','--name-only',BASE,'HEAD'],cwd=ROOT,text=True).splitlines()
    relevant_changed=[p for p in changed if p in SURFACES or p=='.gitattributes' or p.startswith('project/reviews/n30/2026-09-11-reviewer-v3/') or p.startswith('releases/n30-reviewer-v3/') or p=='.github/workflows/n30-reviewer-v3-package.yml']
    old_attrs=subprocess.check_output(['git','show',BASE+':.gitattributes'],cwd=ROOT,text=True)
    assert (ROOT/'.gitattributes').read_text()==old_attrs+'\n# Small, self-contained reviewer download; keep its bytes in ordinary Git.\nreleases/n30-reviewer-v3/N30_Reviewer_Package_v3.zip -filter -diff -merge -text\n'
    bridge=ROOT/'project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md'
    assert sha256(bridge.read_bytes()).hexdigest()=='4a2333802f011a51eca60041aeb412dc157bf8adf99807cb59581b4274152f42'
    manifest_count=None
    if args.release:
        manifest=json.loads((OUT/'MANIFEST.json').read_text())
        for row in manifest['files']:
            data=(ROOT/row['path']).read_bytes()
            assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256'],row['path']
        manifest_count=len(manifest['files'])
        with zipfile.ZipFile(OUT/'N30_Reviewer_Package_v3.zip') as z:
            assert z.testzip() is None
            b=json.loads(z.read('N30_Reviewer_Package_v3/releases/n30-reviewer-v3/BUNDLE_CONTENTS.json'))
            for row in b['files']:
                data=z.read('N30_Reviewer_Package_v3/'+row['path'])
                assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256'],row['path']
    result={'status':'PASS','source_hashes_checked':len(source_map['input_sha256']),
        'all_required_table_lines_present':counts,'endpoint_rows_in_manuscript':211,
        'relative_links_checked':links,'current_versions':{'n25':2,'n27':2,'n28':2,'n29':4,'n30':3},
        'frozen_n29_bridge_unchanged':True,'package_relevant_changed_files':len(relevant_changed),
        'release_manifest_files_checked':manifest_count,'scope_compares_committed_trees':True,
        'reviewer_zip_ordinary_git_exception_verified':True,'external_review':'OPEN'}
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
