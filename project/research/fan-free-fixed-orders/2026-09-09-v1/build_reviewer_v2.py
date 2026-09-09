#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, subprocess

ROOT=Path(__file__).resolve().parents[4]
FILTER='project/reviews/reviewer-paper-build/v1/fix_aligned_tags.lua'
DATE='9 September 2026'

SPECS={
  25:{
    'claim':'e(G) <= 156, equality exactly K(12,13)',
    'proof':'project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md',
    'history':'project/reviews/n25/2026-09-09-fan-free-v2/HISTORY.md',
    'old':'releases/n25-reviewer-v1/README.md',
    'extra':['project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md','project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md','releases/n25-reviewer-v1/LITERATURE_AND_ATTRIBUTION.md'],
  },
  27:{
    'claim':'e(G) <= 182, equality exactly K(13,14)',
    'proof':'project/reviews/n27/2026-09-09-fan-free-v2/PROOF.md',
    'history':'project/reviews/n27/2026-09-09-fan-free-v2/HISTORY.md',
    'old':'releases/n27-reviewer-v1/README.md',
    'extra':['project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md','project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md','project/reviews/n27/2026-09-08-redteam-v1/REPORT.md'],
  }
}

def sha(p):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def front(title,subtitle):
    return f'''---\ntitle: "{title}"\nsubtitle: "{subtitle}"\nauthor: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"\ndate: "{DATE}"\ndocumentclass: article\nfontsize: 11pt\ngeometry: [a4paper, margin=25mm]\ncolorlinks: true\nlinkcolor: "black"\nurlcolor: "blue"\n---\n\n'''

def render(md,pdf):
    cmd=['pandoc',str(md),'--from=markdown+raw_tex+tex_math_single_backslash',f'--lua-filter={FILTER}','--pdf-engine=xelatex','-V','geometry:a4paper','-V','geometry:margin=25mm','-V','fontsize=11pt','-V','mainfont=FreeSerif','-V','sansfont=FreeSans','-V','monofont=FreeMono','-V','colorlinks=true','-V','urlcolor=blue','-o',str(pdf)]
    subprocess.run(cmd,cwd=ROOT,check=True)

def build(n,s):
    out=ROOT/f'releases/n{n}-reviewer-v2'; out.mkdir(parents=True,exist_ok=True)
    proof=ROOT/s['proof']; hist=ROOT/s['history']
    for p in [proof,hist,*[ROOT/x for x in s['extra']]]:
        if not p.exists(): raise FileNotFoundError(p)
    man=out/f'N{n}_Reviewer_Manuscript_v2.md'; mpdf=out/f'N{n}_Reviewer_Manuscript_v2.pdf'
    comp=out/f'N{n}_Verification_Companion_v2.md'; cpdf=out/f'N{n}_Verification_Companion_v2.pdf'
    man.write_text(front(f'Murty-Simon at n={n}: Fan-free candidate proof','Reviewer edition 2 - historical v1 preserved')+
        f'''\\begin{{abstract}}\nThis reviewer edition removes G. Fan's 1987 theorem as a logical dependency of the fixed-order candidate proof while retaining Fan's result as historical attribution. Every larger edge count formerly excluded only by Fan is now covered directly by the project's witness/residual necessary conditions and exact finite arithmetic. The historical reviewer-v1 package and frozen proof remain preserved. Independent mathematical and computational review remain open.\n\\end{{abstract}}\n\n**Canonical claim.** `{s['claim']}`.\n\n**Logical source.** `{s['proof']}`.\n\n**History rule.** Reviewer v1 is not overwritten; edition 2 is a new proof surface.\n\n---\n\n'''+proof.read_text())
    parts=[front(f'Murty-Simon at n={n} - verification companion','Reviewer edition 2 - Fan-free reduction, audit and history'),
      f'''\\begin{{abstract}}\nThis companion records the Fan-free upper-range replacement, exact computational provenance, semantic clarifications prompted by external-AI feedback, and the preserved proof history. It does not convert same-assistant checking into external review.\n\\end{{abstract}}\n\n**Claim under review.** `{s['claim']}`.\n\n**Historical reviewer-v1 package.** `{s['old']}` remains preserved.\n\n---\n''']
    for p in [hist,*[ROOT/x for x in s['extra']]]:
        parts += [f'\n\n\\newpage\n\n# Included source: `{p.relative_to(ROOT)}`\n\n',p.read_text()]
    comp.write_text(''.join(parts))
    render(man,mpdf); render(comp,cpdf)
    readme=out/'README.md'
    readme.write_text(f'''# n={n} Fan-free reviewer package v2\n\n**Current reviewer-facing edition - {DATE}.**\n\nClaim: `{s['claim']}`.\n\nStart with [N{n}_Reviewer_Manuscript_v2.pdf](N{n}_Reviewer_Manuscript_v2.pdf), then [N{n}_Verification_Companion_v2.pdf](N{n}_Verification_Companion_v2.pdf).\n\nFan's 1987 theorem is cited for historical attribution but is **not a logical dependency** of this edition. The replacement proof component is [`FAN_FREE_REDUCTION.md`](../../project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md).\n\nThe previous [`n{n}-reviewer-v1`](../n{n}-reviewer-v1/README.md) package remains preserved unchanged as historical provenance. No external acceptance or formal verification is claimed.\n''')
    files=[man,mpdf,comp,cpdf,readme]
    manifest={'schema':'murty-simon-fan-free-reviewer-v2','built':DATE,'n':n,'claim':s['claim'],'logical_proof':s['proof'],'historical_reviewer_v1':s['old'],'fan_logical_dependency':False,'external_review_complete':False,'files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]}
    (out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')

for n,s in SPECS.items(): build(n,s)

idx=ROOT/'releases/REVIEW_READY_INDEX.md'; t=idx.read_text()
old25='| n=25 | `e(G) <= 156`, equality `K(12,13)` | [PDF](n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) | package audit material in [n25 reviewer release](n25-reviewer-v1/README.md) | independent review open |'
new25='| n=25 | `e(G) <= 156`, equality `K(12,13)` | [PDF](n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) | [PDF](n25-reviewer-v2/N25_Verification_Companion_v2.pdf) | **Fan-free v2**; independent review open; [v1 history](n25-reviewer-v1/README.md) |'
old27='| n27 | `e(G) <= 182, with equality exactly K(13,14)` | [PDF](n27-reviewer-v1/N27_Reviewer_Manuscript_v1.pdf) | [PDF](n27-reviewer-v1/N27_Verification_Companion_v1.pdf) | complete candidate; independent mathematical and computational review OPEN |'
new27='| n27 | `e(G) <= 182, with equality exactly K(13,14)` | [PDF](n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) | [PDF](n27-reviewer-v2/N27_Verification_Companion_v2.pdf) | **Fan-free v2**; independent review OPEN; [v1 history](n27-reviewer-v1/README.md) |'
for old,new in [(old25,new25),(old27,new27)]:
    if t.count(old)!=1: raise SystemExit('review index anchor missing')
    t=t.replace(old,new,1)
if 'Fan-free reviewer-v2' not in t:
    t += '\n## Fixed-order history note\n\nThe current n=25 and n=27 reviewer surfaces are Fan-free reviewer-v2 editions. Their reviewer-v1 packages remain preserved as historical versions that used Fan\'s 1987 bound as a logical edge-count reduction. Fan remains cited in v2 for attribution, but the fixed-order proofs no longer depend on his theorem.\n'
idx.write_text(t)
print('FAN_FREE_REVIEWER_V2_BUILD_OK')
