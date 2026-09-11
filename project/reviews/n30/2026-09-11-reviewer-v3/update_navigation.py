#!/usr/bin/env python3
"""One-time, idempotent reviewer-v3 navigation update; frozen proofs untouched."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[4]
NEW='project/reviews/n30/2026-09-11-reviewer-v3'
REL='releases/n30-reviewer-v3'


def section(text,start,end,replacement):
    a=text.index(start);b=text.index(end,a)
    return text[:a]+replacement.rstrip()+'\n\n'+text[b:]


def main():
    p=ROOT/'README.md';s=p.read_text()
    s=re.sub(r'^\| `n=30` \|.*$', '| `n=30` | Complete candidate: `e(G) <= 225`, equality exactly `K(15,15)`; **reviewer-v3 package** with self-contained hand lemmas and every proof-critical integer table; Delta>=17 closed by a hand bound, Delta=15 equality proved directly; internal arithmetic REPRODUCED; independent specialist review OPEN |',s,flags=re.M)
    s=s.replace('The current reviewer-facing PDF packages are Fan-free v2 at `n=25,27,28,30` and reviewer-v4 at `n=29`.','The current reviewer-facing PDF packages are Fan-free v2 at `n=25,27,28`, reviewer-v4 at `n=29`, and reviewer-v3 at `n=30`.')
    old=s[s.index('### n=30 — complete candidate'):s.index('## General structural programme')]
    a=old.index('[**Fan-free reviewer v2**]') if '[**Fan-free reviewer v2**]' in old else old.index('[**Current reviewer-v3 package**]')
    b=old.index('\n\n',a)
    link=f'[**Current reviewer-v3 package**]({REL}/README.md) · [manuscript PDF]({REL}/N30_Reviewer_Manuscript_v3.pdf) · [verification companion PDF]({REL}/N30_Verification_Companion_v3.pdf) · [complete ZIP]({REL}/N30_Reviewer_Package_v3.zip) · [self-contained proof source]({NEW}/PROOF.md) · [editorial/dependency review]({NEW}/EDITORIAL_REVIEW.md) · [historical reviewer-v2 package](releases/n30-reviewer-v2/README.md).'
    old=old[:a]+link+old[b:]
    old=old.replace('The [complete supplementary assembly](project/research/n30/2026-09-11-assembled-hand-route-v1/ASSEMBLED_PROOF.md) now covers every degree and edge-count scope with hand lemmas and explicit integer tables.','Reviewer-v3 consolidates the [complete supplementary assembly](project/research/n30/2026-09-11-assembled-hand-route-v1/ASSEMBLED_PROOF.md) into a standalone manuscript containing the universal bridge, every hand lemma, every preimage interval and all endpoint tables.')
    old=old.replace('The next task is a coherent new reviewer edition; no new PDF or external acceptance is claimed by this checkpoint.','Reviewer-v3 now packages the complete route with a verification companion and portable replay ZIP. The next task is independent specialist review of this coherent edition; no external acceptance is claimed.')
    s=section(s,'### n=30 — complete candidate','## General structural programme',old)
    s=s.replace('`n=29` is reviewer-v4; the other fixed orders remain Fan-free reviewer-v2, with 11 September analytic hardening annotations at `n=28` and `n=30`.','`n=29` is reviewer-v4 and `n=30` is reviewer-v3; `n=25,27,28` remain Fan-free reviewer-v2, with 11 September analytic hardening at `n=28`.')
    s=re.sub(r'^\| n=30 \|.*$',f'| n=30 | [Reviewer manuscript v3]({REL}/N30_Reviewer_Manuscript_v3.pdf); [complete ZIP]({REL}/N30_Reviewer_Package_v3.zip) | [Verification companion v3]({REL}/N30_Verification_Companion_v3.pdf) |',s,flags=re.M)
    p.write_text(s)

    p=ROOT/'START_HERE_FOR_REVIEWERS.md';s=p.read_text()
    s=s.replace('The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28,30` and **reviewer-v4 at `n=29`**, with the entire dense `Delta=16` branch now excluded by a hand threshold-tail argument.','The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, and **reviewer-v3 at `n=30`**. N29 has no proof-critical computation; N30 combines hand lemmas with explicit finite integer tables.')
    s=s.replace('- `n=30, Delta=17`: every `m>=228` is now a hand exclusion;','- `n=30, Delta=17`: reviewer-v3 proves the stronger `m<=221` by a source-independent hand tail bound;')
    s=s.replace('- `n=30, Delta=16`: the later [threshold-tail hand reduction](project/research/n30/2026-09-11-threshold-tail-v1/README.md) now excludes every `m>=226` in this degree branch; the earlier pointwise `m>=234` cap remains corroboration.','- `n=30, Delta=16`: reviewer-v3 excludes every `m>=225` using the hand classification and explicit endpoint integer tables; the earlier pointwise caps remain corroboration.')
    n30=f'''## n=30 complete candidate

**Current reviewer-v3 package:**

- [Self-contained manuscript PDF]({REL}/N30_Reviewer_Manuscript_v3.pdf)
- [Verification companion PDF]({REL}/N30_Verification_Companion_v3.pdf)
- [Complete portable review ZIP]({REL}/N30_Reviewer_Package_v3.zip)
- [Canonical proof source]({NEW}/PROOF.md), [editorial/dependency review]({NEW}/EDITORIAL_REVIEW.md), and [review report template]({NEW}/REVIEW_REPORT_TEMPLATE.md)

The candidate statement is `e(G)<=225`, with equality exactly `K(15,15)`. The manuscript includes every needed graph lemma and every proof-critical table; there is no need to assemble the proof by following research links.

Delta>=17 is closed by a source-independent twelve-label hand bound, with the stronger `m<=221` at Delta=17. Delta=15 equality has an elementary regularity/triangle-free proof. At Delta=16, a hand classification derives exactly 100 profiles and Q<=21; finite residual-tail reconstruction and eight source inequalities settle m226, while four explicit envelopes cover all 211 tight m225 rows after 61 ledger exclusions.

The historical large scans, grouped LPs, Farkas rays, higher-degree charging computations, isolated-C strengthening, Fan theorem and dominating-edge theorem are no longer premises. **The printed Delta=16 classification, residual-tail and endpoint tables remain proof-critical finite arithmetic.**

The preceding [assembly audit](project/research/n30/2026-09-11-assembled-hand-route-v1/ASSEMBLY_AUDIT.json) reproduced all 844 per-template m225 gaps and all eight m226 contradictions, and its [bridge audit](project/research/n30/2026-09-11-assembled-hand-route-v1/BRIDGE_AUDIT.md) found no blocking flaw. This is same-assistant internal evidence. The ZIP supports a one-command replay from its extracted root.

The [historical reviewer-v2 package](releases/n30-reviewer-v2/README.md) and all original proof/certificate bytes remain preserved. Reviewer-v3 updates the reading surface; the governed theorem ledger is unchanged. Independent specialist review is OPEN.
'''
    s=section(s,'## n=30 complete candidate','## General 7/12 candidate',n30)
    p.write_text(s)

    p=ROOT/'releases/REVIEW_READY_INDEX.md';s=p.read_text()
    s=re.sub(r'^The current fixed-order PDF packages.*$', 'The current fixed-order PDF packages are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, and **reviewer-v3 at `n=30`**. N28 retains its 11 September analytic-hardening annotation. N30 reviewer-v3 contains the complete hand-lemma and finite-table proof, companion and portable ZIP.',s,flags=re.M)
    s=re.sub(r'^\*\*Current supplements:\*\*.*$', '**Current review notes:** reviewers of the frozen N29 bridge appendix should apply the [source-degree display erratum](../project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md). N30 reviewer-v3 incorporates the corrected canonical bridge and the [assembled route](../project/research/n30/2026-09-11-assembled-hand-route-v1/ASSEMBLED_PROOF.md), with every mathematical dependency and finite table included in its manuscript. Internal arithmetic is REPRODUCED; independent specialist review remains OPEN.',s,flags=re.M)
    s=re.sub(r'^\| n30 \|.*$', '| n30 | `e(G) <= 225, with equality exactly K(15,15)` | [PDF v3](n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) | [PDF v3](n30-reviewer-v3/N30_Verification_Companion_v3.pdf) | **Reviewer-v3 hand lemmas + explicit integer tables**; [package](n30-reviewer-v3/README.md), [ZIP](n30-reviewer-v3/N30_Reviewer_Package_v3.zip), [proof](../project/reviews/n30/2026-09-11-reviewer-v3/PROOF.md); internal arithmetic REPRODUCED; independent review OPEN; [v2 history](n30-reviewer-v2/README.md) |',s,flags=re.M)
    s=s.replace('The current PDF packages are reviewer-v2 at n=25,27,28,30 and reviewer-v4 at n=29. The n=28/n=30 upper ranges have additional hand caps that replace several historical zero-domain computations as logical dependencies.','The current PDF packages are reviewer-v2 at n=25,27,28, reviewer-v4 at n=29 and reviewer-v3 at n=30. N28 has additional hand caps; N30 reviewer-v3 includes its complete hand-lemma and explicit-integer-table route.')
    p.write_text(s)

    p=ROOT/'project/research/n30/2026-09-11-assembled-hand-route-v1/README.md'
    s=p.read_text();note='**Later reviewer edition:** this checkpoint is now consolidated in [N30 reviewer-v3](../../../../releases/n30-reviewer-v3/README.md), with a self-contained manuscript, verification companion and portable replay ZIP. The text below records the preceding assembly checkpoint.\n\n'
    if note not in s:
        a=s.index('\n')+1;s=s[:a]+'\n'+note+s[a:].lstrip('\n')
    p.write_text(s)


if __name__=='__main__':
    main()
