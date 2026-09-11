#!/usr/bin/env python3
"""Build the self-contained N30 reviewer-v3 manuscript and review bundle.

The frozen research inputs are never edited. Explicit transformations below
remove superseded status prose, qualify local references, and include every
proof-critical table. No generated theorem or arithmetic claim is inferred
from PDF rendering. Run from any directory; Python standard library only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = ROOT / 'releases/n30-reviewer-v3'
BASELINE = '81f37b80f643dd12f371680e673a95f6de793df2'
ASSEMBLY = 'project/research/n30/2026-09-11-assembled-hand-route-v1'
CLASS = 'project/research/n30/2026-09-11-m225-hand-classification-v1'
ENV = 'project/research/n30/2026-09-11-m225-resource-envelope-v1'
TAIL = 'project/research/n30/2026-09-11-threshold-tail-v1'
BRIDGE = 'project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md'
INPUTS: dict[str, str] = {}


def read(path):
    data = (ROOT / path).read_bytes()
    INPUTS[path] = hashlib.sha256(data).hexdigest()
    return data.decode()


def between(text, start, end=None):
    i = text.index(start)
    return text[i:text.index(end, i) if end else len(text)]


def required_replace(text, old, new):
    assert old in text, old
    return text.replace(old, new)


APPENDIX_LINKS = {
    'CANONICAL_BRIDGE.md': 'A',
    'TWELVE_LABEL_TRANSFER.md': 'B',
    'HAND_CLASSIFICATION.md': 'C',
    'PREIMAGE_ARITHMETIC.md': 'D',
    'N30_M225_THRESHOLD_SLACK_REDUCTION.md': 'E',
    'N30_M226_HAND_ENDPOINT_REDUCTION.md': 'F',
    'FOUR_ENVELOPE_REDUCTION.md': 'G',
    'EXACT_APPENDIX.md': 'H',
}


def links(text, origin):
    def replace(m):
        label, target = m.group(1), m.group(2)
        name = target.split('#')[0].split('/')[-1]
        if name in APPENDIX_LINKS:
            letter = APPENDIX_LINKS[name]
            return f'{label} (Appendix {letter})'
        if target.startswith(('https:', 'http:', '#')):
            return m.group(0)
        path = (ROOT / origin).parent / target.split('#')[0]
        path = path.resolve().relative_to(ROOT)
        assert (ROOT / path).exists(), path
        url = f'https://github.com/paullenz/MurtySimon742/blob/{BASELINE}/{path.as_posix()}'
        return f'[{label}]({url})'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace, text)


def clean(text):
    return text.replace('\u2014', '-').replace('\u2013', '-').replace('\u2011', '-').replace('\u2212', '-')


def qualify(text, letter):
    # Section numbers and displayed equation tags are local to each appendix.
    text = re.sub(r'^(#{2,3}) (\d+(?:\.\d+)?)\.? ', lambda m: f'{m[1]} {letter}.{m[2]}. ', text, flags=re.M)
    text = re.sub(r'\b(Section|Sections) (\d+)(?:[-–](\d+))?',
                  lambda m: f'{m[1]} {letter}.{m[2]}' + (f'-{letter}.{m[3]}' if m[3] else ''), text)
    text = re.sub(r'\\tag\{([^}]+)\}', lambda m: r'\tag{' + letter + '.' + m[1] + '}', text)
    return text


def appendix(letter, title, text, origin, landscape=False):
    body = clean(links(qualify(text, letter), origin))
    start = '\n\\clearpage\n\n' + ('```{=latex}\n' + r'\begin{landscape}' + '\n```\n\n' if landscape else '')
    end = '\n\n' + ('```{=latex}\n' + r'\end{landscape}' + '\n```\n' if landscape else '')
    return start + f'# Appendix {letter}. {title}\n\n' + body.strip() + end


def make_proof():
    path = ASSEMBLY + '/ASSEMBLED_PROOF.md'
    source = read(path)
    main = between(source, '## 1. Degree entry', '## 8. Complete assembly')
    main += between(source, '## 8. Complete assembly')
    main = main[:main.index('The universal graph bridge and all printed proof-critical arithmetic')]
    main = main.replace('Section 4 excluded all larger edge counts.', 'Section 4 excluded all larger edge counts.')
    main = main.replace('The [bridge audit](BRIDGE_AUDIT.md) checks', 'The internal bridge audit, reproduced in the verification companion, checks')
    main = main.replace('The corrected canonical bridge already avoids two wording/display errors in older copies.', 'Appendix A includes the corrected source-degree identity and the precise unique-exception argument.')
    main = main.replace('This completes the supplementary candidate statement.', 'This completes the candidate proof of Theorem 1.')
    main = links(main, path)
    front = r'''# The Murty-Simon bound at order thirty

**Reviewer edition 3 - complete candidate argument, 11 September 2026.**

Research direction: Paul Lenz. Mathematical development, internal auditing and drafting: ChatGPT/Geeps.

## Abstract

We present a candidate proof that every finite simple diameter-two edge-critical graph on thirty vertices has at most 225 edges, with equality exactly for the complete bipartite graph $K_{15,15}$. The proof uses a complement construction with selected and residual cross-edges, a threshold-capacity inequality, hand clipping lemmas, and explicit finite integer tables. A source-independent twelve-label bound closes every dense case of maximum degree at least seventeen. The degree-fifteen equality case has an elementary proof. At maximum degree sixteen, a hand classification of 100 demand profiles leaves eight source inequalities at 226 edges and 211 envelope evaluations at 225 edges. Every required mathematical argument and finite table is included in this manuscript. The verification companion records reproducibility, provenance and the boundary of internal checking.

**Status.** Complete candidate mathematics; exact internal arithmetic REPRODUCED; independent specialist mathematical review OPEN. Separately written checks by the same assistant are internal corroboration, not external validation. This edition does not change the governed theorem ledger, assert novelty, or claim the unrestricted conjecture.

**Theorem 1 (candidate).** Let $G$ be a finite simple graph on thirty vertices with diameter two such that deleting any edge increases its diameter. Then

$$e(G)\le225,\qquad e(G)=225\Longleftrightarrow G\cong K_{15,15}.$$

Distances between disconnected vertices are infinite. Write $m=e(G)$ and $\Delta=\Delta(G)$. A histogram such as $(1^7,2,3^8)$ means seven entries equal to one, one equal to two, and eight equal to three. Empty multiplicities are omitted. Indicator functions have values zero or one.

## How to read the proof

Sections 1-8 give the complete assembly. Appendices A-H supply its arguments and finite arithmetic without requiring another paper or a computational acceptance result. The appendix order follows the dependencies:

| Appendix | Material | Role in the proof |
|---|---|---|
| A | Selected/residual bridge | Universal graph-theoretic implications |
| B | Twelve-label bound | Hand closure of all dense degrees at least 17 |
| C | Thirteen-label classification | Hand reduction to exactly 100 profiles |
| D | All five- and six-lift intervals | Proof-critical finite classification arithmetic |
| E | Residual-tail reconstruction | Completeness of the endpoint row lists |
| F | Eight source inequalities | Proof-critical arithmetic at 226 edges |
| G | Four monotone envelopes | Formulas and local domains at 225 edges |
| H | All 211 positive-gap rows | Proof-critical endpoint arithmetic |

The larger profile sweeps and earlier LP/Farkas systems are not premises. **The printed finite tables are premises to be checked.** All such tables occur here, including rejected preimage intervals and every endpoint gap. A successful checker run cannot replace review of the universal bridge.

Notation is scoped locally. In the tail lemmas $p=N_1$ counts positive demands; in graph formulas $p_u$ is supplement indegree. Section 5 and Appendix E use $\lambda$ for ledger slack. Appendix G and its envelope evaluations use $\lambda$ for a certificate coefficient after ledger slack has been set to zero. Bridge equation numbers and section references are local to Appendix A; analogous conventions apply to the other appendices.

\clearpage

'''
    proof = front + clean(main)
    bridge = read(BRIDGE)
    bridge = between(bridge, '## 1. Setup', '## 10. Charging') + between(bridge, '## 11. Threshold-capacity', '## 12. Isolated-C')
    proof += appendix('A', 'Universal selected/residual bridge', bridge, BRIDGE)

    path = ASSEMBLY + '/TWELVE_LABEL_TRANSFER.md'
    tail12 = between(read(path), '## 1. Remove', '## 6. N30 consequences')
    tail12 = required_replace(tail12, 'This is the [earlier N29 hand argument](../../general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md) with the artificial source-count cutoff removed explicitly.', 'The source-count cutoff is absent from this definition.')
    proof += appendix('B', 'A source-independent twelve-label tail bound', tail12, path)

    path = CLASS + '/HAND_CLASSIFICATION.md'
    cls = between(read(path), '## 1. Statement', '## 7. How this changes')
    cls = required_replace(cls, 'The clipping arguments in the [earlier m226 profile proof](../2026-09-11-threshold-tail-v1/N30_M226_HAND_PROFILE_REDUCTION.md) do not require the lower bound `s_i>=2`. Here are the details needed to apply them to arbitrary demands.', 'The following clipping arguments apply to arbitrary demands, including zeros and ones.')
    proof += appendix('C', 'The complete thirteen-label classification', cls, path)

    path = CLASS + '/PREIMAGE_ARITHMETIC.md'
    pre = read(path).split('\n', 1)[1]
    proof += appendix('D', 'Complete preimage arithmetic', pre, path)

    path = TAIL + '/N30_M225_THRESHOLD_SLACK_REDUCTION.md'
    read(path)
    reconstruction = r'''For $(a,b)=(13,16)$ and $t=m-224>0$, put $g_{13}=0$ and use the thresholds $g_2,\ldots,g_{12}$ from Appendix C. Every actual residual degree is in $\{1,\ldots,13\}$. Let

$$z_h=\#\{u:\rho_u\ge h\},\qquad r=16+\sum_{h=2}^{13}z_h.$$

The thresholds and the demand ledger give $z_h\ge g_h$ and $\lambda=S-r-2t\ge0$. Substitution yields

$$Q-(16+2t)=\lambda+\sum_{h=2}^{13}(z_h-g_h).$$

Thus the residual rows are exactly those reconstructed by assigning this many nonnegative integer units to $\lambda,z_2-g_2,\ldots,z_{13}-g_{13}$, imposing $16\ge z_2\ge\cdots\ge z_{13}\ge0$. This means completeness of the integer relaxation; no sufficiency for an actual graph is asserted. A monotone tail determines a unique histogram, with multiplicities $16-z_2$ at one, $z_h-z_{h+1}$ at $h=2,\ldots,12$, and $z_{13}$ at thirteen. The thresholds $g_h$ need not themselves be monotone, so monotonicity must be imposed after the slack is assigned.

At $t=1$, at most three units are available. Applying this rule to the 100 profiles in Appendix C gives the following complete distribution.

| $Q$ | $\lambda$ | Rows |
|---:|---:|---:|
| 18 | 0 | 64 |
| 19 | 0 | 96 |
| 19 | 1 | 29 |
| 20 | 0 | 42 |
| 20 | 1 | 18 |
| 20 | 2 | 6 |
| 21 | 0 | 9 |
| 21 | 1 | 5 |
| 21 | 2 | 2 |
| 21 | 3 | 1 |

The total is 272. Appendix C shows that every high-score profile containing a zero has $p=12,x=12$ and $Q=18$. Such a profile has no available slack at $t=1$. Consequently every row with positive ledger slack has every demand positive. Its definition then gives $s_i=d_i-R_i$ at each label, so

$$S=\sum_i d_i-\sum_i R_i=2(r+t)-r=r+2t,$$

contradicting $\lambda>0$. This excludes exactly 61 rows. The remaining 211 rows are all printed in Appendix H. Checking that list against the reconstruction rule is a finite proof obligation; the count alone is not a completeness certificate.

At $t=2$, only the six $Q=20$ profiles and the unique $Q=21$ profile remain. The former have no available slack. For $s=(3^{13})$, $g_2=g_3=9$ and all higher thresholds vanish. Its one unit may be placed only in $\lambda$, in $z_2$, or in $z_4$; adding it at $z_3$ or any higher position violates monotonicity. This gives nine rows in total. The positive-ledger-slack row is $(s,\rho)=((3^{13}),(1^7,3^9))$ and is impossible by the same positive-demand argument. The other eight rows are all printed in Appendix F.

For the ledger-tight rows, equality in $\sum_i\max(0,d_i-R_i)\ge\sum_i(d_i-R_i)$ implies $d_i-R_i\ge0$ at every label. Hence $d_i=R_i+s_i$ also at zero-demand labels. This is the precise tightness fact used in the envelope argument.
'''
    proof += appendix('E', 'Complete residual-tail reconstruction', reconstruction, path)

    path = TAIL + '/N30_M226_HAND_ENDPOINT_REDUCTION.md'
    endpoint = between(read(path), '## 2. Tight demand', '## 6. Consequence')
    endpoint = endpoint.replace('The table records the exact minima `L_rho`; `verify_hand_endpoint_table.py` independently checks every allowed integer `(rho,q,p)` pair.', 'The table records the exact minima `L_rho`. Each is checked over the displayed finite integer source domain; the verification companion gives corroborating replay instructions.')
    proof += appendix('F', 'Eight explicit inequalities at 226 edges', 'The reconstruction in Appendix E leaves the following eight tight rows.\n\n' + endpoint, path)

    path = ENV + '/FOUR_ENVELOPE_REDUCTION.md'
    env = between(read(path), '## 1. Exact setup', '## 8. Resulting dependency')
    env = required_replace(env, 'This direct count is the [existing three-coordinate potential lemma](../../general_n/2026-09-09-rx-hall-v1/POTENTIAL_CERTIFICATE_LEMMA_3D.md), not an assumption about constructing a graph from a relaxation.', 'This is a direct count on the actual selected incidences; no converse construction from an integer relaxation is assumed.')
    env = env[:env.index('The [standalone checker]')]
    proof += appendix('G', 'Four exact monotone-envelope certificates', env, path)

    path = ENV + '/EXACT_APPENDIX.md'
    exact = read(path).split('\n', 1)[1]
    proof += appendix('H', 'All 211 tight endpoint rows', exact, path, landscape=True)
    proof += '\n\\clearpage\n\n# Review boundary\n\nThe candidate theorem follows from the implications and finite arithmetic printed above. The companion records where these texts originated, which historical dependencies were removed, and what the internal checks established. Independent specialist review of the bridge, both clipping arguments, completeness of the tables and every endpoint inequality remains OPEN.\n'
    return clean(proof)


def metadata(title, subtitle):
    return f'''---
title: "{title}"
subtitle: "{subtitle}"
author: "Paul Lenz research project - developed with ChatGPT/Geeps"
date: "11 September 2026"
documentclass: article
fontsize: 10pt
geometry: [a4paper, margin=23mm]
toc: true
toc-depth: 1
colorlinks: true
linkcolor: black
urlcolor: blue
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
header-includes:
  - \\usepackage{{amsmath,amssymb,mathtools,booktabs,microtype,pdflscape,etoolbox,fvextra}}
  - \\setlength{{\\emergencystretch}}{{3em}}
  - \\AtBeginEnvironment{{longtable}}{{\\fontsize{{8}}{{9.4}}\\selectfont}}
  - \\fvset{{fontsize=\\small,breaklines=true,breakanywhere=true}}
  - \\setcounter{{tocdepth}}{{1}}
---

'''


def make_companion():
    text = read(str(HERE.relative_to(ROOT)) + '/VERIFICATION_COMPANION.md')
    audit_path = ASSEMBLY + '/BRIDGE_AUDIT.md'
    audit = read(audit_path)
    text += '\n\\clearpage\n\n# Included internal bridge audit\n\n'
    text += 'The following audit is preserved from the pre-edition assembly. Its references to a supplementary route and frozen reviewer-v2 describe that earlier checkpoint; reviewer-v3 now packages that route. No new external review is implied.\n\n'
    text += clean(links(audit.split('\n', 1)[1], audit_path))
    text += '\n\\clearpage\n\n# Source and integrity inventory\n\n'
    text += 'The build records SHA-256 hashes for every input in SOURCE_MAP.json and packages the original input bytes. Sections were consolidated as described in EDITORIAL_REVIEW.md; historical sources remain unchanged.\n\n'
    for path, digest in sorted(INPUTS.items()):
        text += f'- `{path}`\n\n  SHA-256: `{digest}`\n\n'
    return text


def pdf(md, target):
    # Histogram carets in plain table cells are literal notation, not Markdown
    # paired superscript delimiters. TeX math still renders actual exponents.
    subprocess.run(['pandoc', str(md), '--from=markdown+raw_tex+tex_math_single_backslash-superscript',
        '--lua-filter=' + str(HERE / 'pdf_layout.lua'), '--pdf-engine=xelatex', '-o', str(target)], check=True, cwd=ROOT)


def inventory(paths):
    return [{'path':p.relative_to(ROOT).as_posix(), 'bytes':p.stat().st_size,
             'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(set(paths))]


def finalize():
    # A portable replay tree preserves path-sensitive audit code unchanged.
    extras = [ASSEMBLY+'/audit_assembly.py', ASSEMBLY+'/profile_regression.cpp',
              ASSEMBLY+'/PROFILE_REGRESSION.json', ASSEMBLY+'/ASSEMBLY_AUDIT.json',
              ASSEMBLY+'/INDEPENDENT_ENVELOPES.json', ASSEMBLY+'/check_publication.py',
              ASSEMBLY+'/ENVIRONMENT.json', ASSEMBLY+'/PROOF_DEPENDENCIES.json',
              ASSEMBLY+'/PUBLICATION_RECEIPT.json', CLASS+'/HAND_CLASSIFIED_PROFILES.txt',
              ENV+'/JOINT_CERTIFICATES.json', ENV+'/EXACT_AUDIT.json']
    source_map = json.loads((HERE/'SOURCE_MAP.json').read_text())
    paths = {ROOT/p for p in source_map['input_sha256']}
    paths.update(ROOT/p for p in extras)
    paths.add(ROOT/'.gitattributes')
    paths.update(p for p in HERE.iterdir() if p.is_file() and p.name not in {'PUBLICATION_RECEIPT.json'})
    paths.update(p for p in OUT.iterdir() if p.is_file() and p.name not in {'MANIFEST.json','BUNDLE_CONTENTS.json','N30_Reviewer_Package_v3.zip'})
    records = inventory(paths)
    bundle_data = {'schema':'n30-reviewer-v3-bundle-content-v1','files':records,
        'self_exclusions':['releases/n30-reviewer-v3/BUNDLE_CONTENTS.json','releases/n30-reviewer-v3/MANIFEST.json','releases/n30-reviewer-v3/N30_Reviewer_Package_v3.zip']}
    (OUT/'BUNDLE_CONTENTS.json').write_text(json.dumps(bundle_data,indent=2)+'\n')
    paths.add(OUT/'BUNDLE_CONTENTS.json')
    zpath=OUT/'N30_Reviewer_Package_v3.zip'
    with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(paths):
            zi=zipfile.ZipInfo('N30_Reviewer_Package_v3/'+p.relative_to(ROOT).as_posix(),(2026,9,11,0,0,0))
            zi.compress_type=zipfile.ZIP_DEFLATED
            zi.external_attr=0o100644<<16
            z.writestr(zi,p.read_bytes())
    manifest={'schema':'n30-reviewer-v3-manifest','date':'2026-09-11','baseline_commit':BASELINE,
        'claim':'e(G)<=225; equality exactly K(15,15)',
        'status':'Complete candidate; internal arithmetic REPRODUCED; independent specialist review OPEN',
        'proof_critical_finite_tables_retained':True,'governed_ledger_promotion':False,
        'external_review_complete':False,'old_reviewer_v2_preserved':True,
        'source_map':'project/reviews/n30/2026-09-11-reviewer-v3/SOURCE_MAP.json',
        'files':inventory(p for p in OUT.iterdir() if p.is_file() and p.name!='MANIFEST.json')}
    (OUT/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'package_files':len(paths),'zip_bytes':zpath.stat().st_size,'manifest':'PASS'}))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--sources-only',action='store_true')
    parser.add_argument('--finalize',action='store_true')
    args=parser.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    if args.finalize:
        finalize();return
    proof=make_proof()
    (HERE/'PROOF.md').write_text(proof)
    manuscript=OUT/'N30_Reviewer_Manuscript_v3.md'
    manuscript.write_text(metadata('The Murty-Simon bound at order thirty','Reviewer edition 3 - hand lemmas and explicit integer tables')+proof)
    companion=OUT/'N30_Verification_Companion_v3.md'
    companion.write_text(metadata('N30 verification companion','Reviewer edition 3 - dependencies, replay and review obligations')+make_companion())
    source_map={'schema':'n30-reviewer-v3-source-map','baseline_commit':BASELINE,'input_sha256':INPUTS,
        'appendices':APPENDIX_LINKS,'editorial_record':'EDITORIAL_REVIEW.md',
        'frozen_inputs_modified':False,'finite_tables_in_manuscript':True}
    (HERE/'SOURCE_MAP.json').write_text(json.dumps(source_map,indent=2)+'\n')
    if not args.sources_only:
        pdf(manuscript,manuscript.with_suffix('.pdf'))
        pdf(companion,companion.with_suffix('.pdf'))
    print(json.dumps({'manuscript_bytes':manuscript.stat().st_size,'companion_bytes':companion.stat().st_size,'inputs':len(INPUTS)}))


if __name__=='__main__':
    main()
