#!/usr/bin/env python3
"""Prepare an editorial reviewer edition from the frozen proof; no lemma changes.
Pandoc + XeLaTeX produce a standalone, editable TeX manuscript and PDF.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'N25_Full_Chain_Candidate_2026-09-06_v1/PROOF.md'
if not SOURCE.is_file():
    SOURCE=ROOT/'FROZEN_PROOF.md'
OUT=ROOT/('package' if (ROOT/'package').is_dir() else 'rebuilt_manuscript')
OUT.mkdir(exist_ok=True)
(ROOT/'build').mkdir(exist_ok=True)
NAME='N25_Reviewer_Manuscript_v1'

text=SOURCE.read_text()
text=text[text.index('## 1. Statement and scope'):]
text=text.replace('RESULTS.md','the accompanying RESULTS.md')
text=text.replace("the attachment's inactive-vertex lemma", "the frozen Delta=14 dossier's inactive-vertex lemma")
text=text.replace("the attachment's domain", "the frozen Delta=14 dossier's domain")
text=text.replace("the attachment's unchanged computations", "the frozen Delta=14 dossier's unchanged computations")
text=text.replace('printed in the attachment','printed in that dossier')
text=text.replace('equality exactly for the complete bipartite graph K_{12,13}',
                  'equality exactly for the complete bipartite graph K_{12,13}')
text=text.replace("Call an edge a direct witness if its endpoints have no common neighbour.",
                  "Call an edge a direct witness if its endpoints have no common neighbour; let D denote the set of such edges.")
text=text.replace("Call a nonedge a two-step witness if its endpoints have exactly one common neighbour.",
                  "Call a nonedge a two-step witness if its endpoints have exactly one common neighbour; let S denote the set of such nonedges. Notation introduced in this section is local to this section.")

greek={'Δ':r'\Delta','δ':r'\delta','ρ':r'\rho','ε':r'\varepsilon','ℓ':r'\ell',
       '≥':r'\ge','≤':r'\le','→':r'\to','∈':r'\in','∅':r'\varnothing','≠':r'\ne'}

def math_symbols(s):
    for a,b in greek.items():s=s.replace(a,b+' ')
    return s.replace('²','^2').replace('Q_min','Q_{min}')

def prose(s):
    # Preserve code spans and link destinations; only decorate mathematical tokens.
    chunks=re.split(r'(`[^`]+`|\]\(https?://[^)]+\)|\b[A-Za-z][A-Za-z_]*\.(?:py|md)\b)',s)
    for i,piece in enumerate(chunks):
        if piece.startswith('`') or piece.startswith(']('):continue
        if re.fullmatch(r'[A-Za-z][A-Za-z_]*\.(?:py|md)',piece):
            chunks[i]='`'+piece+'`'
            continue
        pattern=r'K_\{12,13\}|[A-Za-zερℓ]_\{[^}]+\}|[A-Za-zρℓε]_[A-Za-zρ]+(?:\([A-Za-z,]+\))?|[Δδ]\([A-Za-z]\)|Δ=[0-9,]+|[Δδρℓε≥≤→∈∅≠]|[a-zA-Z]\^?[²]|\bH5\b'
        piece=re.sub(pattern,lambda m:r'\ensuremath{'+('H_5' if m.group()=='H5' else math_symbols(m.group()).strip())+'}',piece)
        chunks[i]=piece
    return ''.join(chunks)

chunks=re.split(r'(\\\[.*?\\\])',text,flags=re.S)
parts=[]
for chunk in chunks:
    if chunk.startswith(r'\['):parts.append('$$'+math_symbols(chunk[2:-2])+'$$')
    else:parts.append(prose(chunk))
text=''.join(parts)
front='''---
title: "A candidate proof of the Murty–Simon conjecture at order 25"
subtitle: "Reviewer edition 1 — independent mathematical review pending"
author: "Prepared for Paul Lenz's N=25 research project"
date: "6 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
mainfont: "Latin Modern Roman"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
mathfont: "Latin Modern Math"
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
header-includes:
  - \\usepackage{fancyhdr}
  - \\pagestyle{fancy}
  - \\fancyhf{}
  - \\fancyhead[L]{\\small N=25 Murty--Simon candidate}
  - \\fancyhead[R]{\\small Reviewer edition 1}
  - \\fancyfoot[C]{\\thepage}
  - \\setlength{\\headheight}{14pt}
  - \\setlength{\\emergencystretch}{3em}
---

\\begin{abstract}
We present a candidate argument that every simple diameter-2 edge-critical graph on 25 vertices has at most 156 edges, with equality exactly for the complete bipartite graph $K_{12,13}$. Published reductions are combined with residual-edge injections and exhaustive integer necessary-condition checks. The computations have been reproduced using separately implemented programs, and explicit certificates exclude every final numerical equality case. Independent mathematical review remains pending. The argument and code were developed with substantial ChatGPT/Codex assistance; both arithmetic implementations were produced by the same assistant and are not checks by independent researchers.
\\end{abstract}

**Provenance.** This is an editorial rendering of the frozen candidate at [commit 20f059a](https://github.com/paullenz/MurtySimon25/commit/20f059a03b2f5e2b34b3e0fa5d2373ae65b14300). Equation and section numbers are retained. Typesetting and the explicit names of the Section 3 witness sets are editorial clarifications. The original proof, source, evidence and historical audits remain unchanged in the accompanying archive. No theorem-ledger promotion, external endorsement or novelty claim is made.

'''
appendix='''
\\newpage

## Appendix. Review and reproduction map

The accompanying reviewer package contains the unchanged original evidence ZIP, its SHA256, a top-level verification/replay wrapper, the literature and attribution check, and review forms. The original detailed band tables remain in RESULTS.md inside the evidence archive.

| Finite scope | Outer states | Labelled columns checked | Final subset certificates | Remaining |
|---|---:|---:|---:|---:|
| Delta 14, 157 edges | 59,264 | 1,480 | 0 | 0 |
| Delta 15, 157 edges | 108 | 0 | 0 | 0 |
| Delta 15, 156 edges | 211 | 0 | 0 | 0 |
| Delta 14, 156 edges, k=2–5 | 82,452 | 188,520 | 171 | 0 |
| Delta 14, 156 edges, k=1 | 401,543 | 3,252,212 | 1,788 | 0 |

The counts certify execution of the stated finite tests, conditional on their mathematical necessity. They do not establish the graph-theoretic lemmas by themselves.

The first mathematical review should focus on Sections 3, 5, 6, 7 and 9. The computational review should check exhaustive domain generation, both matching implementations, labelled-column enumeration and all subset-certificate coverage. Reports should identify precisely which statements were checked and record objections with a section or equation reference.

## References used in the argument

1. Genghua Fan, *On diameter 2-critical graphs*, Discrete Mathematics **67** (1987), 235–240. [DOI](https://doi.org/10.1016/0012-365X(87)90174-9). The exact bound used here is also stated on page 2 of reference 2. The publisher's full text was not available for this audit.
2. Tao Wang, *On Murty-Simon Conjecture*, arXiv:1205.4397v1 (20 May 2012). [Primary text](https://arxiv.org/pdf/1205.4397v1). Theorem 2.1 explicitly covers the odd-order complement-diameter-three case.
3. Teresa W. Haynes, Michael A. Henning, Lucas C. van der Merwe and Anders Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics **12** (2014), 1882–1889. [DOI](https://doi.org/10.2478/s11533-014-0449-3). [Primary text](https://d-nb.info/1372516379/34). Theorems 3.1, 3.2 and 3.6(a), with the odd-order point cross-checked against reference 2.
4. Antoine Dailly, Florent Foucaud and Adriana Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics **342** (2019), 3142–3159. [DOI](https://doi.org/10.1016/j.disc.2019.06.023). [Primary manuscript](https://arxiv.org/pdf/1812.08420). Theorem 4 is the dominating-edge input; its exceptional graph has six vertices.
'''
md=OUT/(NAME+'.md')
md.write_text(front+text+appendix)
subprocess.run(['pandoc',str(md),'-f','markdown+tex_math_single_backslash','-s','-t','latex','--pdf-engine=xelatex','-o',str(OUT/(NAME+'.tex'))],check=True)
for _ in range(2):
    subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(OUT),str(OUT/(NAME+'.tex'))],check=True,stdout=(ROOT/'build/latex_stdout.log').open('w'))
(OUT/'EDITORIAL_PROVENANCE.json').write_text(json.dumps(dict(
    source_commit='20f059a03b2f5e2b34b3e0fa5d2373ae65b14300',
    frozen_proof_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    editorial_changes=['PDF typography and inline mathematical notation','Explicit Section 3 witness-set names D and S','Reviewer abstract, provenance, references and result map'],
    new_mathematical_claims=False,external_mathematical_review=False),indent=2,sort_keys=True)+'\n')
print(OUT/(NAME+'.pdf'))
