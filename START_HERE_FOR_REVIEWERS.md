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
- `n=33`: `e(G) <= 272`, equality only `K(16,17)`;
- `n=34`: `e(G) <= 289`, equality only `K(17,17)`;
- `n=35`: `e(G) <= 306`, equality only `K(17,18)`.

The canonical reviewer packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The current fixed-order editions are Fan-free reviewer-v2 at `n=25,27,28`, reviewer-v4 at `n=29`, reviewer-v3 at `n=30`, source-first reviewer-v1 packages at `n=31,32,33,35`, and reviewer-v2 at `n=34`.

N29 has no proof-critical computation. N30 combines hand lemmas with explicit finite integer tables. N31 is predominantly hand/structural. N32 uses hand reductions plus exact finite replay in the difficult `Delta=17` branch. N33 is again compact: the sole new equality frontier has only 29 residual states, 25 exact shifted-potential exclusions and four hand contradictions.

The strongest current reviewer-packaged broad maximum-degree candidate is

```text
n >= 6 and Delta(G) >= (7/12)n  ==>  e(G) < floor(n^2/4).
```

Start with [`releases/general-7-12-reviewer-v1/README.md`](releases/general-7-12-reviewer-v1/README.md). This is a complete candidate hand argument with internal exact audits green; independent mathematical review, novelty assessment and external reproduction remain open.

The active RX-Hall / monotone-potential programme has exact finite compression results and is now proof-critical in parts of the N32/N33 fixed-order packages, but **no unrestricted theorem is claimed from that programme**.

No unrestricted all-order proof is claimed anywhere in the repository.

## New general structure and complete n=35 candidate

The [general step-back package](releases/general-stepback-v1/README.md) includes
the balanced-degree theorem for all n>=7 and the a=14 infinite family. The
[joint-clipping package](releases/general-joint-clipping-reviewer-v1/README.md)
adds sharp scalar tail bounds for a=17..23 and a general tight-threshold hand
obstruction. These results include proof-critical finite arithmetic where stated.

The [N34 reviewer-v2 package](releases/n34-reviewer-v2/README.md) retains the
complete candidate bound 289, equality K(17,17), and replaces its final large
certificate with a [short hand proof](project/reviews/n34/2026-09-12-heavy-independent-v1/HAND_PROOF.md). The equality
ledger is now 6,709 hand/accounting exclusions and 6,837 exact envelopes.
The [separate whole-count audit](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md) matches all original model
rows and independently checks a translated certificate as corroboration.

The [N35 reviewer-v1 package](releases/n35-reviewer-v1/README.md) gives the new
candidate bound 306, equality K(17,18). Its two new finite layers contain
485 states, all excluded by 228 hand/accounting arguments and 257 exact
envelopes. External mathematical review and reproduction remain OPEN.

The [general heavy-load/routing reviewer package](releases/general-heavy-load-reviewer-v1/README.md)
now extends the N34 hand mechanism to every heavy threshold, with explicit
incoming-degree penalties and demand-only tail bounds. Its low-demand
corollary is `s_i<=2, t>0, b-a<=5 => 9t+4(b-a)<=a`, with no residual-degree
cap. The study records 595 alternative hand exclusions for previously
certified states, 45 excluded layer/profile instances, and all survivors and
failed extensions. The existing fixed-order ledgers remain unchanged.

The [joint heavy-routing reviewer-v1 package](releases/general-joint-routing-reviewer-v1/README.md)
adds a candidate hand lemma coupling the number of heavy senders with each
destination's incoming capacity and the unordered-pair budget. A 27-case pilot
led to 729 further exact exclusions from the full corrected pool of 6,307;
563 depend on the sharper destination term within the same frozen catalogue.
All 5,578 survivors and the correction removing 192 old-rule exclusions are
preserved. The general maximum-degree result and fixed-order ledgers are
unchanged; external review remains OPEN.

The [routing-tail reviewer-v1 package](releases/general-routing-tail-reviewer-v1/README.md)
projects joint routing onto demands and proved lower tails, and extracts a
closed equality-rigidity criterion. It adds 114 whole layer/profile exclusions
beyond the earlier 45 demand-level exclusions. The scalar strictness rule adds
nine over the ordinary load-cap test, all included in those 114. All 5,578
previous joint-routing survivors remain. The package preserves that negative
frontier result, full evidence and invalid extensions; external review is OPEN.

The [compatible-routing reviewer-v1 package](releases/general-compatible-routing-reviewer-v1/README.md)
adds selected-degree destination eligibility and mixed traffic inequalities.
A preselected 29-state pilot excludes 19 cases: two by extending the preceding
multiplier search, one further by retaining selected degrees, and sixteen
further by destination eligibility. Mixed cuts add no further whole-state
exclusions. It includes a compact hand example, 321 exact certificates and
321 independently checked potential envelopes, all failed searches and ten
sample survivors. That pilot tested only its sample; the full-pool continuation
below now measures catalogue coverage. Generalization and fixed-order status
remain candidate; external review is OPEN.

The [compatible-catalogue reviewer-v1 package](releases/general-compatible-catalogue-reviewer-v1/README.md)
freezes 20 simple pilot vectors, then replays all 5,578 prior survivors. It
excludes 990, retaining 15 pilot successes; four pilot-only witnesses are
preserved separately. The combined record has 994 exclusions and 4,584 survivors.
One fixed potential handles 707 cases and has a new general hand reduction:
no q enumeration and at most five p candidates per H. Exact code checks all
1,564,007 catalogue gaps and the inherited pilot cases. Original outputs,
failures, a post-replay 11-template compression and full survivor accounting
are preserved. No new density threshold or fixed-order theorem is claimed;
external review remains OPEN.

For the preceding general-foundations review pass, see the
[focused foundations checklist](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md).
It checks the primary dominating-edge theorem's exception, the witness-capacity
injection, the entire canonical bridge and the new exact certificates. It also
records corrections to the a=17 obstruction wording and the free balance
multiplier in the potential lemma. Same-assistant checks remain internal evidence.

## Current fixed-order extensions: n=31, n=32, n=33, n=34, n=35

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

### n=34

Candidate `e(G)<=289`, equality exactly `K(17,17)`.

- [Reviewer-v2 package](releases/n34-reviewer-v2/README.md)
- [Complete proof](project/research/n34/2026-09-12-equality-v1/README.md)
- [Exact v2 equality replay](project/reviews/n34/2026-09-12-heavy-independent-v1/verify_v2.py)
- [Hand replacement and normalization audit](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md)

All 13,546 equality states are excluded. This extends the prior upper bound
of 289 to the complete candidate equality classification. External review is OPEN.

### n=35

Candidate `e(G)<=306`, equality exactly `K(17,18)`.

- [Reviewer-v1 package](releases/n35-reviewer-v1/README.md)
- [Complete proof and ledger](project/research/n35/2026-09-12-candidate-v1/PROOF.md)
- [Exact replay](project/research/n35/2026-09-12-candidate-v1/verify.py)
- [Focused internal audit](project/research/n35/2026-09-12-candidate-v1/AUDIT.md)

The sole new Delta=19 branch has 19 states at 307 edges and 466 at 306 edges.
All are covered, including three zero-demand states. The proof uses 257
exact envelopes with 92,701 local integer checks and 228 hand/accounting
exclusions. Review the bridge, complete frontier and degree dependencies
alongside the certificates. External review remains OPEN.

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

The current fixed-order candidates do not rely logically on Fan's 1987 density theorem. Direct Fan-free replacements were constructed for `n=25..30`; N31/N32/N33/N34/N35 were assembled without invoking Fan's theorem in the first place.

Same-assistant hostile audits and reimplementations are useful internal evidence but are explicitly **not** external independent review.

## Governance and limits

No complete fixed-order candidate above `n=35`, proof through `n=1,000`, unrestricted all-order solution, novelty determination, full formal verification or external endorsement is claimed.

Finite arithmetic states are necessary-condition systems, not graphs. Exact rejection is useful only if the graph-to-model implications are correct. Reviewers should therefore prioritize the universal graph bridge over merely rerunning solvers.

For the canonical package list and current status wording, use [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md).
