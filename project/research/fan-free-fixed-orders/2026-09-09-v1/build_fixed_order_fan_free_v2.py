#!/usr/bin/env python3
from pathlib import Path
import hashlib,re

ROOT=Path(__file__).resolve().parents[4]
FF='project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md'
DATE='9 September 2026'

def sha_text(s): return hashlib.sha256(s.encode()).hexdigest()
def once(text,old,new,label):
    c=text.count(old)
    if c!=1: raise SystemExit(f'{label}: expected one anchor, got {c}')
    return text.replace(old,new,1)

def build_n29():
    src=ROOT/'project/reviews/n29/2026-09-08-candidate-v1/PROOF.md'
    s=src.read_text(); h=sha_text(s)
    s=once(s,
      '# Murty–Simon at n=29: candidate proof with complete finite Delta=16 arithmetic',
      '# Murty–Simon at n=29: Fan-free candidate proof, edition 2','n29 title')
    s=once(s,
      '8 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal checking by ChatGPT/Geeps.',
      '9 September 2026. Fan-free edition 2, built from the frozen 8 September candidate proof. Research directed by Paul Lenz; mathematical development, implementation and internal checking by ChatGPT/Geeps.','n29 date')
    s=once(s,
      '**Status: candidate proof. The fixed-order arithmetic described below has been reproduced internally; independent mathematical review, external computational reproduction and novelty assessment remain OPEN. The graph-theoretic lemmas are not fully formalised.**',
      f'**Status: candidate proof. Independent mathematical review, external computational reproduction and novelty assessment remain OPEN. Fan\'s 1987 theorem is cited historically but is not a logical dependency of this edition. Frozen historical source SHA-256: `{h}`. Fan-free upper-range component: `{FF}`.**','n29 status')
    pat=r'## 2\. Published reductions and the two edge counts\n\n.*?\n\nA bipartite graph of diameter two is complete bipartite'
    new=f'''## 2. Fan-free upper reduction and the two edge counts

Historically, edition 1 used G. Fan's 1987 strict density estimate, as reported by Wang, to reduce the upper-bound problem to 211 edges. Fan remains cited for attribution, but **his theorem is not a logical dependency of edition 2**.

The direct replacement is `{FF}`. In summary, every edge count `m>=212` is excluded without Fan: degree sum handles `Delta<=14`; the witness-deficit inequality at `Delta=15` is monotone stronger above 211; fresh exact arithmetic closes `Delta=16` throughout `m=212..232`; the pointwise charging argument at `Delta=17` strengthens as `m` rises; the residual h-index argument likewise excludes `Delta=18..27`; and `Delta=28` is the universal-vertex/star case. Thus any upper-bound counterexample has exactly 211 edges. Equality at 210 is treated separately, exactly as in edition 1.

The complete historical Fan-based proof remains preserved at `{src.relative_to(ROOT)}`.

A bipartite graph of diameter two is complete bipartite'''
    s,n=re.subn(pat,new,s,flags=re.S)
    if n!=1: raise SystemExit(f'n29 Fan block replacements={n}')
    s=once(s,
      'Different missing pairs select different cross edges because the B-source and unique exception recover the pair. All other H[A,B] edges are residual.',
      'Selection is indexed by missing **unordered** B-pairs. For each such pair designate exactly one corresponding cross edge; opposite orientations of the same unordered pair cannot both be selected. Different selected edges therefore recover different unordered B-pairs from their B-source and unique exception. All other H[A,B] edges are residual.','n29 selection')
    s=once(s,
      "Fan's strict bound leaves only m<=211.",
      'The Fan-free upper-range reduction excludes every `m>=212`; it remains only to exclude `m=211` and analyse equality at `m=210`.','n29 assembly')
    s=s.replace("Fan's and Dailly–Foucaud–Hansberg's published theorems are external inputs and are not re-proved here.",
                "Dailly–Foucaud–Hansberg's published dominating-edge theorem remains an external input and is not re-proved here. Fan's theorem is retained only as historical attribution and is not used logically in edition 2.")
    out=ROOT/'project/reviews/n29/2026-09-09-fan-free-v2'; out.mkdir(parents=True,exist_ok=True)
    (out/'PROOF.md').write_text(s)
    (out/'HISTORY.md').write_text(f'''# n=29 proof history - Fan-free edition 2\n\nFrozen edition-1 source: `{src.relative_to(ROOT)}`\n\nSHA-256 at build time: `{h}`\n\nEdition 2 removes Fan's theorem as a logical upper-bound dependency, cites Fan historically, makes the unordered-pair selection convention explicit, and points the assembly to `{FF}`. The frozen edition-1 proof and all old evidence remain unchanged.\n''')

def build_n30():
    src=ROOT/'project/reviews/n30/2026-09-09-candidate-v1/PROOF.md'
    s=src.read_text(); h=sha_text(s)
    s=once(s,'# Murty–Simon at n=30: complete candidate proof','# Murty–Simon at n=30: Fan-free complete candidate proof, edition 2','n30 title')
    s=once(s,
      '9 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal audit by ChatGPT/Geeps.',
      '9 September 2026. Fan-free edition 2, built from the frozen candidate proof. Research directed by Paul Lenz; mathematical development, implementation and internal audit by ChatGPT/Geeps.','n30 date')
    s=once(s,
      '**Status: complete candidate proof. Independent expert mathematical review, external computational reproduction and novelty assessment remain OPEN.** This is not a proof of the unrestricted Murty–Simon conjecture.',
      f'**Status: complete candidate proof. Independent expert mathematical review, external computational reproduction and novelty assessment remain OPEN. Fan\'s 1987 theorem is cited historically but is not a logical dependency of this edition. Frozen source SHA-256: `{h}`. Fan-free upper-range component: `{FF}`.** This is not a proof of the unrestricted Murty–Simon conjecture.','n30 status')
    pat=r'## 2\. Published upper reduction\n\n.*?\n\nA bipartite diameter-two graph is complete bipartite'
    new=f'''## 2. Fan-free upper reduction

Historically, edition 1 used G. Fan's 1987 strict density estimate to reduce a possible counterexample to `m=226`. Fan remains cited for attribution, but **his theorem is not a logical dependency of edition 2**.

The replacement is `{FF}`. It directly excludes every `m>=227`: degree sum forces `Delta>=16`; exact trusted-kernel calculations cover `Delta=16` through its degree-sum ceiling `m=240`; a complete explicit early-kernel scan covers `Delta=17,m=227..255`; for `Delta=18..28` the charging domain was already empty at the lower dense scopes and only becomes harder as `t` increases; and `Delta=29` is the star case. Hence any upper-bound counterexample has exactly `m=226`, which is excluded below. Equality at `m=225` is treated separately.

The historical Fan-based proof remains preserved at `{src.relative_to(ROOT)}`.

A bipartite diameter-two graph is complete bipartite'''
    s,n=re.subn(pat,new,s,flags=re.S)
    if n!=1: raise SystemExit(f'n30 Fan block replacements={n}')
    s=once(s,
      'Write `ui -> w`, choose one such selected cross-edge for each missing B-pair, and call all other existing A-B edges residual. The source and unique exception recover the missing B-pair, so the selected assignment is injective.',
      'Write `ui -> w`. Selection is indexed by missing **unordered** B-pairs: designate exactly one such cross-edge for each unordered pair, never one per orientation, and call all other existing A-B edges residual. The source and unique exception recover the missing unordered B-pair, so the selected assignment is injective and opposite orientations cannot collide.','n30 selection')
    s=once(s,
      "Therefore no 226-edge counterexample exists, and Fan's strict bound gives\n\n```text\ne(G)<=225.\n```",
      'The Fan-free upper-range reduction already excludes every `m>=227`. Since the 226-edge scope has now also been excluded,\n\n```text\ne(G)<=225.\n```','n30 assembly')
    s=s.replace('9. the use and exact hypotheses of the cited published Fan and dominating-edge reductions.',
                '9. the use and exact hypotheses of the cited published dominating-edge reduction. Fan is historical attribution only in edition 2.')
    out=ROOT/'project/reviews/n30/2026-09-09-fan-free-v2'; out.mkdir(parents=True,exist_ok=True)
    (out/'PROOF.md').write_text(s)
    (out/'HISTORY.md').write_text(f'''# n=30 proof history - Fan-free edition 2\n\nFrozen edition-1 source: `{src.relative_to(ROOT)}`\n\nSHA-256 at build time: `{h}`\n\nEdition 2 removes Fan's theorem as a logical upper-bound dependency, cites Fan historically, makes the unordered-pair selection convention explicit, and incorporates the complete Fan-free upper-range evidence in `{FF}`. The frozen edition-1 proof and all old evidence remain unchanged.\n''')

def build_n28():
    src=ROOT/'releases/n28-reviewer-v1/N28_Reviewer_Manuscript_v1.tex'
    s=src.read_text(); h=sha_text(s)
    s=s.replace('Reviewer edition 1','Reviewer edition 2')
    s=s.replace(r'7 September 2026\\\small Reviewer edition 2; independent mathematical review open',
                r'9 September 2026\\\small Fan-free reviewer edition 2; independent mathematical review open')
    s=once(s,
      "Fan's published strict estimate reduces the upper-bound problem to 197 edges.",
      "Fan's published strict estimate is retained for historical attribution, but edition 2 replaces it logically by a direct Fan-free exclusion of every edge count above 197.",'n28 abstract')
    pat=r"The external density input is Fan's strict estimate, as reported by Wang \\cite\[p\.~2\]\{wang\}:.*?needs examination does\."
    new=(r"Historically, reviewer edition 1 used Fan's strict estimate, as reported by Wang \cite[p.~2]{wang}, to deduce $m\le197$. "
         r"Fan remains cited for attribution, but his theorem is \emph{not} a logical dependency of edition 2. "
         "The replacement is the project note \\texttt{"+FF.replace('_','\\_')+r"}: the existing 197-edge calculation remains unchanged, while every $m\ge198$ is excluded directly. "
         r"Degree sum handles $\Delta\le14$; fresh exact arithmetic closes $\Delta=15$ for $m=198,\ldots,210$; the pointwise charging bound at $\Delta=16$ and residual h-index bounds at $\Delta=17,\ldots,26$ only strengthen as $m$ increases; and $\Delta=27$ is the star case. "
         r"The historical Fan-based reviewer-v1 manuscript remains preserved unchanged.")
    s,n=re.subn(pat,lambda _m:new,s,flags=re.S)
    if n!=1: raise SystemExit(f'n28 Fan block replacements={n}')
    s=s.replace(r'Fan supplies the global reduction to $m\le197$.',
                r'The Fan-free upper-range reduction supplies the global reduction to $m\le197$; Fan is cited historically only.')
    s=s.replace("Fan's theorem", "Fan's historical theorem")
    out=ROOT/'project/reviews/n28/2026-09-09-fan-free-v2'; out.mkdir(parents=True,exist_ok=True)
    (out/'PROOF.tex').write_text(s)
    (out/'HISTORY.md').write_text(f'''# n=28 proof history - Fan-free edition 2\n\nFrozen reviewer-v1 source: `{src.relative_to(ROOT)}`\n\nSHA-256 at build time: `{h}`\n\nEdition 2 retains the direct 197-edge/equality mathematics, removes Fan's bound as the logical global cap, cites Fan historically, and points to `{FF}` for the direct exclusion of all larger edge counts. Reviewer v1 and all original archives remain unchanged.\n''')

if __name__=='__main__':
    build_n28(); build_n29(); build_n30()
    print('FIXED_ORDER_FAN_FREE_V2_BUILD_OK')