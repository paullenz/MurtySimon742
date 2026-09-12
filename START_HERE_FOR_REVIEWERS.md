# Start here for reviewers

**Updated 12 September 2026.**

## What this repository is

This repository contains **AI-assisted candidate mathematics** concerning the Murty–Simon conjecture / Erdős Problem #742, together with code, exact certificates, replay workflows, hostile audits and failed intermediate approaches.

Nothing here should be treated as externally accepted mathematics merely because a workflow is green. The fixed-order and general structural results are explicitly labelled **candidate** until they receive genuinely independent mathematical review. Same-assistant reimplementations reduce implementation risk but are not external independence.

Paul Lenz directed the project and chose the research priorities. ChatGPT/Geeps supplied the mathematical development, implementations, manuscripts and internal audits.

If you find an error, please open a GitHub Issue. A short counterexample or a precise identification of the first invalid implication is more valuable than a general assessment.

## Headline candidate results

The repository currently contains complete candidate fixed-order Murty–Simon results for:

- `n=25`: `e(G) <= 156`, equality only `K(12,13)`;
- `n=27`: `e(G) <= 182`, equality only `K(13,14)`;
- `n=28`: `e(G) <= 196`, equality only `K(14,14)`;
- `n=29`: `e(G) <= 210`, equality only `K(14,15)`;
- `n=30`: `e(G) <= 225`, equality only `K(15,15)`;
- `n=31`: `e(G) <= 240`, equality only `K(15,16)`;
- `n=32`: `e(G) <= 256`, equality only `K(16,16)`;
- `n=33`: `e(G) <= 272`, equality only `K(16,17)`.

The canonical reviewer packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28`, reviewer-v4 at `n=29`, reviewer-v3 at `n=30`, source-first reviewer-v1 packages at `n=31,32,33`, and bound reviewer-v1 at `n=34` (equality OPEN).

N29 has no proof-critical computation. N30 combines hand lemmas with explicit finite integer tables. N31 is predominantly hand/structural. N32 uses hand reductions plus exact finite replay in the difficult `Delta=17` branch. N33 is again compact: the sole new equality frontier has only 29 residual states, 25 exact shifted-potential exclusions and four hand contradictions.

The strongest current reviewer-packaged broad maximum-degree candidate is

```text
n >= 6 and Delta(G) >= (7/12)n  ==>  e(G) < floor(n^2/4).
```

Start with [`releases/general-7-12-reviewer-v1/README.md`](releases/general-7-12-reviewer-v1/README.md). This is a complete candidate hand argument with internal exact audits green; independent mathematical review, novelty assessment and external reproduction remain open.

The active RX-Hall / monotone-potential programme has exact finite compression results and is now proof-critical in parts of the N32/N33 fixed-order packages, but **no unrestricted theorem is claimed from that programme**.

No unrestricted all-order proof is claimed anywhere in the repository.

## New general structure and n=34 upper bound

The [general step-back package](releases/general-stepback-v1/README.md) includes
the balanced-degree theorem for all n>=7 and the a=14 infinite family. The
[joint-clipping package](releases/general-joint-clipping-reviewer-v1/README.md)
adds sharp scalar tail bounds for a=17..23 and a general tight-threshold hand
obstruction. These results include proof-critical finite arithmetic where stated.

The [N34 bound reviewer-v1 package](releases/n34-bound-reviewer-v1/README.md)
now establishes the **candidate conjectured bound e(G)<=289**. All 1,614
290-edge states have exact exclusions: 662 hand/accounting and 952 integer
certificates. The [new internal audit](project/research/n34/2026-09-12-m290-v1/AUDIT.md)
checks the exact residual budget, zero-demand handling and heavy-label subset lemma.
Equality classification remains OPEN, with 13,546 conservative Delta=18
states at 289 edges. Complete bound-and-equality packages still reach n=33.

For the preceding general-foundations review pass, see the
[focused foundations checklist](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md).
It checks the primary dominating-edge theorem's exception, the witness-capacity
injection, the entire canonical bridge and the new exact certificates. It also
records corrections to the a=17 obstruction wording and the free balance
multiplier in the potential lemma. Same-assistant checks remain internal evidence.

## Current fixed-order extensions: n=31, n=32, n=33

### n=31

Candidate `e(G)<=240`, equality exactly `K(15,16)`.

- [`releases/n31-reviewer-v1/README.md`](releases/n31-reviewer-v1/README.md)
- [`project/research/n31/2026-09-11-hand-route-v1/PROOF.md`](project/research/n31/2026-09-11-hand-route-v1/PROOF.md)
- [`project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md`](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md)

The route is predominantly hand/structural: high degrees close through the twelve-label theorem, `Delta=17` through the thirteen-label theorem and equality analysis, and `Delta=16` through witness-deficit counting.

### n=32

Candidate `e(G)<=256`, equality exactly `K(16,16)`.

- [`releases/n32-reviewer-v1/README.md`](releases/n32-reviewer-v1/README.md)
- [`project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md`](project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md)
- [`project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md`](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md)
- [`project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md`](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md)

For N32 the highest-value external targets are the shared selected/residual bridge, threshold-capacity equality, endpoint load, the t=1 residual-tail expansion and the strengthened zero-demand model. Exact replay is important implementation evidence but is not a substitute for reviewing those implications.

### n=33

Candidate `e(G)<=272`, equality exactly `K(16,17)`.

- [`releases/n33-reviewer-v1/README.md`](releases/n33-reviewer-v1/README.md)
- [`project/research/n33/2026-09-12-candidate-v1/PROOF.md`](project/research/n33/2026-09-12-candidate-v1/PROOF.md)
- [`project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md`](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md)
- [`project/research/n33/2026-09-12-candidate-v1/README.md`](project/research/n33/2026-09-12-candidate-v1/README.md)

N33 has an especially small new proof surface. `Delta=17` is fully hand-closed and equality forces `K(17,16)`. The only new finite branch is `(a,b,t)=(14,18,2)` at `Delta=18,m=272`: 21 demand profiles expand to 29 residual-tail states; a shifted nine-rectangle potential excludes 25 with exact integer acceptance and four are excluded by hand. No full RX/Hall Farkas stage is needed.

Highest-value N33 review targets are the same shared bridge, threshold-capacity/equality and endpoint-load lemmas, plus independent reproduction of the 21-profile / 29-state frontier and the four displayed hand contradictions.

## Recommended bridge audit: n=29

The n=29 reviewer-v4 candidate remains an especially clean place to audit the universal graph-to-demand machinery because no finite computation is logically required.

Current package:

- [`releases/n29-reviewer-v4/README.md`](releases/n29-reviewer-v4/README.md)
- [`project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md`](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md)
- [`project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md`](project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md)
- [`project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md`](project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md)
- [`project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md`](project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md)

For `Delta=16`, reviewer-v4 uses only the exact ledger/demand inequality, residual activity, selected-incidence forcing, selected-source capacity and threshold capacity. These give `Q(s)>=16+2t`; the hand tail-deficit theorem gives `Q(s)<=18`, hence `t<=1` and excludes every `m>=210` in this degree branch.

The highest-value external review remains the **universal bridge + threshold-capacity lemma + hand clipping argument**, followed by the short `Delta=15`, `Delta=17` and higher-degree branches.

## n=30 package

The current reviewer-v3 package contains the complete hand-lemma and explicit-integer-table proof:

- [Self-contained manuscript PDF](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf)
- [Verification companion PDF](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf)
- [Complete portable review ZIP](releases/n30-reviewer-v3/N30_Reviewer_Package_v3.zip)
- [Canonical proof source](project/reviews/n30/2026-09-11-reviewer-v3/PROOF.md)

`Delta>=17` is closed by the source-independent twelve-label theorem, `Delta=15` equality is direct, and `Delta=16` uses a hand classification plus explicit residual-tail and endpoint tables. Independent specialist review remains open.

## General 7/12 candidate

Reviewer material:

- [`releases/general-7-12-reviewer-v1/README.md`](releases/general-7-12-reviewer-v1/README.md)
- [`project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md`](project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md)
- [`project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md`](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md)

The scalar estimate gives `t < 5a^2/128 + a/8`. Large-n regressions are consistency checks, not proof by extrapolation. The main mathematical trust boundary is the shared graph-to-demand/profile-integral bridge.

## Robustness and correction policy

The repository preserves failed approaches and discovered bugs rather than rewriting history.

Important correction notes include:

- the historical n=29 grouped-model normalization bug, whose v1 certificates are quarantined and not used by the current reviewer-v4 proof;
- the non-blocking threshold-capacity explanatory sign/order typo, corrected in current proof text;
- the frozen N29 bridge source-degree display erratum, which omitted `q_u` in one displayed intermediate identity while using the correct resulting supplement bound.

The current fixed-order candidates do not rely logically on Fan's 1987 density theorem. Direct Fan-free replacements were constructed for `n=25..30`; N31/N32/N33 were assembled without invoking Fan's theorem in the first place.

Same-assistant hostile audits and reimplementations are useful internal evidence but are explicitly **not** external independent review.

## Governance and limits

No complete fixed-order candidate above `n=33`, proof through `n=1,000`, unrestricted all-order solution, novelty determination, full formal verification or external endorsement is claimed.

Finite arithmetic states are necessary-condition systems, not graphs. Exact rejection is useful only if the graph-to-model implications are correct. Reviewers should therefore prioritize the universal graph bridge over merely rerunning solvers.

For the canonical package list and current status wording, use [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md).
