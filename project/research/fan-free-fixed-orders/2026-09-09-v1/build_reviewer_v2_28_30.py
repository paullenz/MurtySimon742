#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, shutil, subprocess

ROOT=Path(__file__).resolve().parents[4]
FILTER=ROOT/'project/reviews/reviewer-paper-build/v1/fix_aligned_tags.lua'
DATE='9 September 2026'
FF=ROOT/'project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md'
AUD=ROOT/'project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def front(title,subtitle):
    return f'''---\ntitle: "{title}"\nsubtitle: "{subtitle}"\nauthor: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"\ndate: "{DATE}"\ndocumentclass: article\nfontsize: 11pt\ngeometry: [a4paper, margin=25mm]\ncolorlinks: true\nlinkcolor: "black"\nurlcolor: "blue"\n---\n\n'''

def render_md(md,pdf):
    subprocess.run([
      'pandoc',str(md),'--from=markdown+raw_tex+tex_math_single_backslash',
      f'--lua-filter={FILTER}','--pdf-engine=xelatex',
      '-V','geometry:a4paper','-V','geometry:margin=25mm','-V','fontsize=11pt',
      '-V','mainfont=FreeSerif','-V','sansfont=FreeSans','-V','monofont=FreeMono',
      '-V','colorlinks=true','-V','urlcolor=blue','-o',str(pdf)
    ],cwd=ROOT,check=True)

def render_tex(tex,pdf):
    # Compile twice for references. Keep all auxiliary files in the release dir.
    out=tex.parent
    for _ in range(2):
        subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',tex.name],cwd=out,check=True,
                       stdout=subprocess.DEVNULL)
    built=out/(tex.stem+'.pdf')
    if built != pdf:
        built.replace(pdf)
    for ext in ('.aux','.log','.out','.toc'):
        p=out/(tex.stem+ext)
        if p.exists(): p.unlink()

def companion(n,claim,history,extras,out):
    md=out/f'N{n}_Verification_Companion_v2.md'
    pdf=out/f'N{n}_Verification_Companion_v2.pdf'
    parts=[front(f'Murty-Simon at n={n} - verification companion','Fan-free reviewer edition 2; historical v1 preserved'),
      f'''\\begin{{abstract}}\nThis companion records the direct Fan-free upper-range replacement, the hostile assembly audit prompted by external critique, exact computational provenance, and preserved proof history. Fan's 1987 result remains cited as historical context but is not a logical dependency of the current project proof. Same-assistant checking is not external verification.\n\\end{{abstract}}\n\n**Claim under review.** `{claim}`.\n\n**Fan-free reduction.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`.\n\n**Hostile assembly audit.** `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md`.\n\n---\n''']
    for p in [history,FF,AUD,*extras]:
        if not p.exists(): raise FileNotFoundError(p)
        parts += [f'\n\n\\newpage\n\n# Included source: `{p.relative_to(ROOT)}`\n\n',p.read_text()]
    md.write_text(''.join(parts))
    render_md(md,pdf)
    return md,pdf

def build_n28():
    n=28; claim='e(G) <= 196, equality exactly K(14,14)'
    proof=ROOT/'project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex'
    history=ROOT/'project/reviews/n28/2026-09-09-fan-free-v2/HISTORY.md'
    out=ROOT/'releases/n28-reviewer-v2'; out.mkdir(parents=True,exist_ok=True)
    tex=out/'N28_Reviewer_Manuscript_v2.tex'; pdf=out/'N28_Reviewer_Manuscript_v2.pdf'
    shutil.copyfile(proof,tex); render_tex(tex,pdf)
    cmd,cpdf=companion(n,claim,history,[
      ROOT/'project/reviews/n28/2026-09-07-redteam-v1/REPORT.md',
      ROOT/'project/research/general_n/2026-09-07-direct-197-v8/README.md',
      ROOT/'project/research/general_n/2026-09-07-direct-197-v8/EXACT_CHECK_REPORT.json',
    ],out)
    finish(n,claim,'project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex','releases/n28-reviewer-v1/README.md',out,[tex,pdf,cmd,cpdf])

def build_md(n,claim,proof_rel,history_rel,old_rel,extras):
    proof=ROOT/proof_rel; history=ROOT/history_rel
    out=ROOT/f'releases/n{n}-reviewer-v2'; out.mkdir(parents=True,exist_ok=True)
    md=out/f'N{n}_Reviewer_Manuscript_v2.md'; pdf=out/f'N{n}_Reviewer_Manuscript_v2.pdf'
    md.write_text(front(f'Murty-Simon at n={n}: Fan-free candidate proof','Reviewer edition 2 - hostile-audited dependency replacement')+
      f'''\\begin{{abstract}}\nThis reviewer edition replaces the historical use of G. Fan's 1987 upper-density theorem by a direct order-specific exclusion of every larger edge count. Fan remains cited for attribution. The historical reviewer-v1 proof surface is preserved unchanged. The Fan-free assembly has passed an internal hostile coverage/integrity audit; independent mathematical and computational review remain open.\n\\end{{abstract}}\n\n**Canonical claim.** `{claim}`.\n\n**Logical source.** `{proof_rel}`.\n\n---\n\n'''+proof.read_text())
    render_md(md,pdf)
    cmd,cpdf=companion(n,claim,history,[ROOT/x for x in extras],out)
    finish(n,claim,proof_rel,old_rel,out,[md,pdf,cmd,cpdf])

def finish(n,claim,proof_rel,old_rel,out,files):
    readme=out/'README.md'
    readme.write_text(f'''# n={n} Fan-free reviewer package v2\n\n**Current reviewer-facing edition — {DATE}.**\n\nClaim: `{claim}`.\n\nStart with [N{n}_Reviewer_Manuscript_v2.pdf](N{n}_Reviewer_Manuscript_v2.pdf), then [N{n}_Verification_Companion_v2.pdf](N{n}_Verification_Companion_v2.pdf).\n\nFan's 1987 theorem is retained for historical attribution but is **not a logical dependency** of this edition. The replacement is [`FAN_FREE_REDUCTION.md`](../../project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md), and the assembled replacement has passed the internal [`FAN_FREE_AUDIT.md`](../../project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md).\n\nThe previous [`n{n}-reviewer-v1`](../n{n}-reviewer-v1/README.md) package remains preserved unchanged as historical provenance. No external acceptance or formal verification is claimed.\n''')
    files=files+[readme]
    manifest={'schema':'murty-simon-fan-free-reviewer-v2','built':DATE,'n':n,'claim':claim,
      'logical_proof':proof_rel,'historical_reviewer_v1':old_rel,'fan_logical_dependency':False,
      'fan_free_hostile_audit_status':'PASS (internal)','external_review_complete':False,
      'files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]}
    (out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')

build_n28()
build_md(29,'e(G) <= 210, equality exactly K(14,15)',
         'project/reviews/n29/2026-09-09-fan-free-v2/PROOF.md',
         'project/reviews/n29/2026-09-09-fan-free-v2/HISTORY.md',
         'releases/n29-reviewer-v1/README.md',[
           'project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md',
           'project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md'])
build_md(30,'e(G) <= 225, equality exactly K(15,15)',
         'project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md',
         'project/reviews/n30/2026-09-09-fan-free-v2/HISTORY.md',
         'releases/n30-reviewer-v1/README.md',[
           'project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md'])

# Update only the three rows this builder owns; n25/n27 v2 are already current.
idx=ROOT/'releases/REVIEW_READY_INDEX.md'; t=idx.read_text()
rows={
  '| n=28 | `e(G) <= 196`, equality `K(14,14)` | [PDF](n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) | [PDF](n28-reviewer-v1/N28_Verification_Companion_v1.pdf) | independent review open |':
  '| n=28 | `e(G) <= 196`, equality `K(14,14)` | [PDF](n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) | [PDF](n28-reviewer-v2/N28_Verification_Companion_v2.pdf) | **Fan-free v2**; internal hostile audit PASS; independent review open; [v1 history](n28-reviewer-v1/README.md) |',
  '| n29 | `e(G) <= 210, with equality exactly K(14,15)` | [PDF](n29-reviewer-v1/N29_Reviewer_Manuscript_v1.pdf) | [PDF](n29-reviewer-v1/N29_Verification_Companion_v1.pdf) | complete candidate; independent mathematical review OPEN |':
  '| n29 | `e(G) <= 210, with equality exactly K(14,15)` | [PDF](n29-reviewer-v2/N29_Reviewer_Manuscript_v2.pdf) | [PDF](n29-reviewer-v2/N29_Verification_Companion_v2.pdf) | **Fan-free v2**; internal hostile audit PASS; independent review OPEN; [v1 history](n29-reviewer-v1/README.md) |',
  '| n30 | `e(G) <= 225, with equality exactly K(15,15)` | [PDF](n30-reviewer-v1/N30_Reviewer_Manuscript_v1.pdf) | [PDF](n30-reviewer-v1/N30_Verification_Companion_v1.pdf) | complete candidate; independent mathematical review OPEN |':
  '| n30 | `e(G) <= 225, with equality exactly K(15,15)` | [PDF](n30-reviewer-v2/N30_Reviewer_Manuscript_v2.pdf) | [PDF](n30-reviewer-v2/N30_Verification_Companion_v2.pdf) | **Fan-free v2**; internal hostile audit PASS; independent review OPEN; [v1 history](n30-reviewer-v1/README.md) |'
}
for old,new in rows.items():
    if t.count(old)!=1: raise SystemExit('review index row anchor missing: '+old[:35])
    t=t.replace(old,new,1)
old='The current n=25 and n=27 reviewer surfaces are Fan-free reviewer-v2 editions. Their reviewer-v1 packages remain preserved as historical versions that used Fan\'s 1987 bound as a logical edge-count reduction. Fan remains cited in v2 for attribution, but the fixed-order proofs no longer depend on his theorem.'
new='The current project reviewer surfaces at n=25,27,28,29,30 are Fan-free reviewer-v2 editions. Their reviewer-v1 packages remain preserved as historical versions that used Fan\'s 1987 bound as a logical edge-count reduction. Fan remains cited in v2 for attribution, but none of those five current project fixed-order proofs depends on his theorem. The assembled replacement has passed the internal hostile coverage/integrity audit; independent review remains open.'
if old not in t: raise SystemExit('history-note anchor missing')
t=t.replace(old,new,1); idx.write_text(t)
print('FAN_FREE_REVIEWER_V2_28_30_BUILD_OK')
