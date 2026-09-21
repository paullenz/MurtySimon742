# Murty-Simon / Erdos Problem #742 - research archive and eventual D2C programme

<!-- Keep the live overview and status tables here. Put dated updates below them, never above them. -->
<!-- CURRENT-STATUS:START -->
## Current status

### Active mathematical target

The live problem is the **sufficiently-large / eventual second-extremal classification for diameter-2-critical graphs** around

`M(n)=floor((n-1)^2/4)+1`.

The stronger all-order 2019 Dailly-Foucaud-Hansberg conjecture is false: the published 2024 order-12 hostile control `X_3` has 32 edges while `M(12)=31`. It remains mandatory. Murty-Simon / Erdos #742 fixed-order material remains preserved, but first-proof priority there is not the active optimization target.

**Live handoff:** [`CURRENT_STATE.md`](CURRENT_STATE.md).

### 21 September 2026: sharp Q3 star-support theorem

The newest [review index](project/research/post_ms/2026-09-21-q3-star-support-v1/THEOREM_AND_REVIEW_INDEX.md) gives a scoped structural theorem: for a D2C graph with a Q3 root neighbourhood and antipodal-transversal outside codes, nonempty star support has at least four centres. Exactly four centres form an affine plane and require at least 19 vertices; an explicit 19-vertex, 66-edge graph attains the bound. Both nonparity plane orbits require at least 20 vertices. Five through eight centres and nontransversal codes remain open.

Two actual infinite families give positive linear gaps below M(n). The five-coordinate family improves the six-coordinate family only from n=26 onward (ties at 24,25). The latest [parity-factor reduction](project/research/post_ms/2026-09-21-q3-star-support-v1/OPPOSITE_EDGE_PARITY_FACTOR_REDUCTION.md) reduces the opposite-edge-plane existence problem to one copy of each parity code; fixed-core parity expansions are eventually below M(n), without a uniform threshold over cores.

The four-centre branch is now completely classified at the support level: only parity-plane support is realizable. Exact order results give a unique order-19 graph with 66 edges and a unique order-20 extremal structure with 73 edges. The parity-star interface is genuinely realizable (an n=26,m=104 graph is a positive control), and its remaining density loss has been reduced to a local matching-one lemma for missing parity-pair certificates. Finite SAT rejects the minimal matching-two core across star, coordinate and parity multiplicities through eight; this is evidence, not the missing general proof.

The raw certificate calculus passes 28,934 independent edge-deletion comparisons. The new graphs add no positive rigid-Hall fixture: all their checked maximum-degree roots have p=0, and this is proved for the balanced five-coordinate family. These are internal results awaiting external review, not a general eventual theorem. The current priority is raw realizability of the reduced nonparity-plane cores; the earlier conditional interface below remains preserved.

### 21 September 2026 post-audit forward correction

The midnight [daily red-team audit](project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md) elevated two immediate obligations: independently reconstruct the small half-ray equality faces and attack the zero-positive-fixture rigid-cut gap directly from raw criticality. Both were addressed in the next forward session.

**Equality-face gate:** a second independent replay of the repaired `N=0,1,2,3` cases passed at the stated conditional scope, so `Delta>=h+1` is no longer waiting on that audit gate. It is now strategically subordinate, however, because a stronger upstream boundary argument eliminates the entire diagnostic half-ray before H–U carrier optimization is needed.

**New raw realizability theorem:** for a rigid one-code outside block `Y=A_d` with multiplicity `y>=2` and at least two matched-selected heads `m>=2`, those heads force **full boundary exposure** `I(d,X)=[p]`. More importantly, the X-reverse orientation of a boundary edge is impossible: the matched source and any X-witness would share every vertex of the repeated same-code block, so their common-neighbour set cannot be a singleton. Thus every exposed coordinate must route through U-forward or matched-forward support.

A minimum outside source has `k` selected complementary U-witnesses in `U_bar d`, none of which can populate a one-match boundary class `U_{bar d xor e_i}`. Writing residual dimension `r=p-m`, the exact available boundary-forward population is

`e=u-k=c-r`.

If `C=C(d,X)` is the universal-coordinate set, the matched-forward leaf count satisfies

- `|C|=0` or `|C|>=3`: no matched-forward heads, so **`c>=p+r`**;
- `|C|=1`: at most one matched-forward head, so **`c>=p+r-1`**;
- `|C|=2`: at most two, so **`c>=p+r-2`**, with equality requiring the two universal coordinates to form an isolated matched-row `K_2`.

This is a literal graph-realizability condition inside the rigid one-code interface. It does not use the score ceiling, rooted-Q, pair-local Hall capacity, gamma collision or the audit-sensitive source-tuple capacity theorem.

Two important 20 September scalar escape families are therefore **not graph-realizable**: the corrected residual-one intermediate half-ray, and the large-gap family `p=3t,c=2t,m=2t,r=t,y=t`. Their survival of earlier scalar inequalities reflected a missing boundary-criticality condition, not a genuine candidate geometry. Reverse-gamma multiplicity remains relevant only for singleton outside-code classes `y_d=1`; same-session notes that allowed repeated-code reverse-only coordinates have been explicitly corrected or marked superseded.

There is still **no eventual theorem and no justified threshold `n_0`**. The bounded actual-D2C regression still contains **zero positive rigid complete Hall-cut fixtures with `x>=3`**. The new theorem is a stronger necessary condition inside that unexercised interface, not evidence that the interface is reachable or impossible in general.

### Preserved conditional interface and earlier direction

`rooted criticality -> selected/residual Hall ledger -> exact pair capacity -> rigid cut -> one-code purification -> raw B–A boundary trichotomy -> repeated-code reverse exclusion -> full boundary exposure (m>=2) -> complementary U-class exclusion -> exact forward reservoir e=c-r -> c>=p+r-|L(C)|`.

Within this conditional interface, the earlier proposed step was to intersect this near-maximal rooted-gap condition with the exact residual defect `delta=b(n-b)-m=r-e(F)`, rooted triangle count `Q=e(G[N(v)])`, and pair-local Hall/score identities. The qualitatively separate one-code regimes are `m<=1` and singleton outside block `y=1`.

Key current packages:

- [21 September daily red-team audit](project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md)
- [Raw boundary-code-edge trichotomy, corrected](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/RIGID_CUT_BOUNDARY_CODE_EDGE_TRICHOTOMY.md)
- [Global matched-leaf collapse](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/GLOBAL_MATCHED_LEAF_COLLAPSE_AND_PARTIAL_U_BILL.md)
- [Full boundary exposure / forward-only theorem](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/ONE_CODE_FULL_BOUNDARY_EXPOSURE_THEOREM.md)
- [Corrected residual-one consequence](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/RESIDUAL_ONE_BOUNDARY_POPULATION_OBSTRUCTION.md)
- [Half-ray raw population closure](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/HALF_RAY_BOUNDARY_CERTIFICATE_SCORE_CLOSURE.md)
- [Second equality-face hostile replay](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/HALF_RAY_EQUALITY_FACE_SECOND_HOSTILE_REPLAY.md)
- [Dependency correction map](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/REPEATED_CODE_REVERSE_EXCLUSION_DEPENDENCY_CORRECTION.md)
- [19 September source-premise repair](project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md)
- [Actual-graph rigid/Hall regression](project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md)

### Trust boundary

The newest packages are **internal candidate mathematics**. Hand derivation, checker replay, actual-graph regression, same-project CI, independent proof review, external specialist review and publication acceptance are distinct gates. Finite abstract parameter scans are not graph counts. The zero-positive-fixture rigid-cut gap remains explicit and is not evidence either for realizability or impossibility.

Invalidated/superseded material remains preserved. In particular, the old `HU-PRIVATE/HU-QI/HU-IHOLE` chain is not admissible; the first uncorrected superconstant formulas from commit `945dc220...` remain superseded; and the same-session residual-one reverse-capacity wedge is marked superseded after the repeated-code reverse exclusion.

### Canonical preserved finite ledger

**4,626 exclusions / 952 survivors / 3,632 whole-state closures.** Fixed-order candidate proofs, audits, exact-block work, h-index/receiver theory, selected-incidence Hall machinery and the mixed `{4,5}` all-excess closure remain preserved with their original trust boundaries. Earlier external #742 work changes priority/novelty, not the internal logical status of those artifacts.

### Standalone-paper programme

Two internal candidate paper packages remain under development:

1. [Stratified Hall / minimum-cut exactness](project/papers/stratified-hall-mincut/MANUSCRIPT.md) - abstract two-sided crossing-dominance / Hall-margin exactness.
2. [Boolean-flow / D2C stability](project/papers/boolean-flow-d2c/MANUSCRIPT.md) - zero-residual Boolean-coordinate structure, the `n<=294` boundary cutoff, and root-edge stability.

See the [standalone paper index](project/papers/README.md) and claim ledgers before citing any result as established or new.

### Current fixed-order candidate packages

| Scope | Preserved candidate result; external review open |
|---|---|
| n=25 | `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2 |
| n=27 | `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2 |
| n=28 | `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening |
| n=29 | `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed |
| n=30 | `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3 |
| n=31 | `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1 |
| n=32 | `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1 |
| n=33 | `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1 |
| n=34 | `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final heavy certificate hand-replaced |
| n=35 | `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1 |

### Operational programme

The eventual-D2C programme continues through 27 September 2026 with a dedicated daily adversarial checkpoint. Each daily audit is reserved for attempted falsification, independent replay, session-utilisation audit, repo/README/CURRENT_STATE reconciliation and a dated 24-hour report rather than forward research. Autonomous forward work must inherit the latest audit gate, retain `X_3`, and not revive superseded evidence.

**Reviewers:** [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) · [`REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md) · [papers and review materials](#papers-and-review-materials).
<!-- CURRENT-STATUS:END -->

## Dated research updates - current and preserved history

**21 September 2026 - post-audit boundary-realizability correction.** Raw boundary criticality now shows that a repeated outside code class cannot use the X-reverse boundary orientation. In the one-code branch with at least two matched-selected heads this combines with full boundary exposure and the exact escape reservoir `e=c-r` to force `c>=p+r` generically, with only the precisely described one-/two-universal-coordinate relaxations. The corrected intermediate half-ray and the preserved large-gap scalar escape family are therefore not literal graph candidates. A dependency-correction note preserves the same-session reverse-capacity route that this stronger observation superseded. See [`CURRENT_STATE.md`](CURRENT_STATE.md) and [the forward-only theorem](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/ONE_CODE_FULL_BOUNDARY_EXPOSURE_THEOREM.md).

**21 September 2026 - daily adversarial audit, superconstant frontier and telemetry repair.** The audit retained the corrected local superconstant-deficit result only at conditional/provisional status, kept the zero-positive-fixture rigid-cut gap as the dominant graph-level risk, and found that day-wide session utilisation could not be verified because most hourly telemetry was missing. A durable session-log schema was added and the live status handoff was reconciled after a Status synchronization failure. See the [full audit](project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md), [`CURRENT_STATE.md`](CURRENT_STATE.md), and [telemetry schema](project/research/session_logs/SESSION_LOG_SCHEMA.md).

**20 September 2026 - daily adversarial audit and all-R frontier reconciliation.** The audit found no fatal contradiction in the repaired live chain, but kept its conditional scope. It independently replayed the source-premise and arithmetic checks, retained the zero-positive-fixture rigid-cut gap as the dominant interface risk, identified a dead `t` diagnostic output in the latest checker, and found that the audited head had outrun both `CURRENT_STATE.md` and the README. See the [full audit](project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md).

**19 September 2026 - first daily adversarial audit and repair day.** The [daily red-team audit](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md) independently re-derived the finite source-tuple capacity theorem conditional on its named premises and confirmed `X_3`. Subsequent work repaired the alpha/beta orientation error, rebuilt actual-graph Hall/pair-capacity regression, repaired a common-buffer criticality orientation, restored the missing physical outside-reservoir condition, and compressed the live branch to the all-R equality pinch.

**17 September 2026 - programme reset.** External work in `Erdos742/Erdos742` changed the priority interpretation of the Murty-Simon project, while the 2024 order-12 counterexample falsified the contemplated all-order second-extremal strengthening. The active programme therefore became the sufficiently-large/eventual D2C problem. See [literature correction](project/research/post_ms/2026-09-17-stronger-pivot-v1/LITERATURE_CORRECTION_2024_EXCEPTION.md) and [dependency audit](project/research/post_ms/2026-09-17-stronger-pivot-v1/DEPENDENCY_AUDIT_2019_FALSE_CONJECTURE.md).

### Preserved status snapshots

The pre-20-September and pre-19-September root README snapshots remain preserved under [`archive/status-snapshots/`](archive/status-snapshots/). No historical snapshot or invalidated proof artifact was deleted by this audit.

<!-- REDTEAM-HISTORY:START -->
## Hostile / red-team audit history and resulting proof hardening

**21 September 2026 - daily eventual-D2C audit.** The audit found no fatal contradiction in the corrected local H–U/superconstant chain but retained it as a conditional branch theorem. It elevated the unexercised rigid-cut realizability interface and small equality-face reconstruction as the next mathematical audit gates, and separately found severe telemetry incompleteness plus a Status synchronization failure. The exact report is [DAILY_RED_TEAM_AUDIT.md](project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md).

**20 September 2026 - daily eventual-D2C audit.** The audit found no fatal contradiction in the final repaired all-R local package, but retained the conditional rigid-cut trust boundary and the zero-positive-fixture gap. It independently replayed the current arithmetic, confirmed that several older counts and orientation claims remain superseded, and made the same-code criticality / ordered witness-injection theorem the next mandatory raw-criticality audit. The exact report is [DAILY_RED_TEAM_AUDIT.md](project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md).

**19 September 2026 - daily eventual-D2C audit.** The [full report](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md) found no fatal contradiction in the then-current rooted-witness/Hall/rigid-U-witness spine, but tightened the evidence labels. The source-tuple capacity theorem was independently re-derived conditional on its graph-to-selected-system premises; subsequent same-day repair then proved those two premises at the exact selected-system semantics used downstream.

**n=29 - real normalization bug found and corrected.** Hostile review established that a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore **invalid as proof evidence**. A corrected v2 replay, smaller exact kernel and later hand clipping argument removed the defect and much of the computational dependency. See [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md), [minimal kernel](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json), and [reviewer-v4](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md).

**Blind external red-team follow-up.** The [blind external red-team follow-up](project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md) preserved a non-blocking sign/order typo while distinguishing it from the corrected normalization defect; even non-fatal criticism remains visible rather than being erased by a later clean proof.

**Fan dependency removed from the fixed-order logical spine.** The direct reduction in [FAN_FREE_REDUCTION.md](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md) and companion [FAN_FREE_AUDIT.md](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md) replaced the historical Fan-density dependency for the preserved fixed-order packages. The external-feedback audit that prompted the hardening remains at [REPORT.md](project/reviews/cross-cutting/2026-09-09-external-ai-feedback-audit-v1/REPORT.md).

**Hostile coverage/integrity audit surfaces remain first-class evidence.** Preserved packages include the [n=25 re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md), [n=27 red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md), [n=28 red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md), [n=30 assembly audit](project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md), and [general 7/12 hostile audit](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md).

**Preservation rule:** a hostile audit may strengthen, weaken, invalidate or redirect a claim. All four outcomes are evidence. Invalidated and superseded computations remain visible; failed audits, counterexamples and reviewer-triggered proof changes are not to be removed because a later route is cleaner.
<!-- REDTEAM-HISTORY:END -->

## Current research chain

The active chain is the **eventual dense D2C programme**:

- [Literature correction / 12-vertex exception](project/research/post_ms/2026-09-17-stronger-pivot-v1/LITERATURE_CORRECTION_2024_EXCEPTION.md)
- [Published-figure hostile-control certification](project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md)
- [False-2019-conjecture dependency audit](project/research/post_ms/2026-09-17-stronger-pivot-v1/DEPENDENCY_AUDIT_2019_FALSE_CONJECTURE.md)
- [Rooted witness-slot saturation](project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/)
- [Hall density / cut stability](project/research/post_ms/2026-09-18-hall-density-cut-stability-v1/)
- [Same-code complementary-pair localization](project/research/post_ms/2026-09-18-large-code-pair-v1/)
- [Rigid Hall witness deficit and one-code trap](project/research/post_ms/2026-09-18-rigid-hall-witness-deficit-v1/)
- [19 September daily adversarial audit](project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md)
- [Source-premise repair](project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md)
- [Actual-graph rigid/Hall regression](project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md)
- [20 September same-code raw-criticality audit](project/research/post_ms/2026-09-20-same-code-raw-criticality-audit-v1/SAME_CODE_RAW_CRITICALITY_AUDIT.md)
- [Corrected H–U capacity chain](project/research/post_ms/2026-09-20-rigid-interface-direct-audit-v1/)
- [21 September daily adversarial audit](project/research/post_ms/2026-09-21-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md)
- [21 September rigid-boundary realizability package](project/research/post_ms/2026-09-21-rigid-realizability-audit-v1/)

## Failures and audit gates remain first-class evidence

Do not quietly delete, relabel or retrospectively clean up a failed lemma, non-closing experiment, counterexample or CI event. Historical deterministic process failures remain evidence, including `35402717100` / `105785888407`, `35405621026` / `105794668021`, `35405621004` / `105794668117`, `35406193034` / `105796333427`, and `35406504877` / `105797249965`. The 20 September stale-handoff failure `35473850313` / `105979551184` remains preserved. The 21 September audit additionally records Status synchronization failure `35543011012` / `106163951722` at pre-audit head `4a7cf5ab4b94451a9e502cd901c906ab9890b048`.

Finite discovery, audit, ledger promotion and external mathematical acceptance remain separate gates. Synthetic or abstract-system rejections do not alter the canonical graph frontier by themselves.

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

**Reviewer entry:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md), then [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md).

### Active standalone paper candidates

- [Stratified Hall / minimum-cut manuscript](project/papers/stratified-hall-mincut/MANUSCRIPT.md) · [claim ledger](project/papers/stratified-hall-mincut/CLAIM_LEDGER.md) · [abstract theorem](project/papers/stratified-hall-mincut/ABSTRACT_CROSSING_DOMINANCE.md)
- [Boolean-flow D2C manuscript](project/papers/boolean-flow-d2c/MANUSCRIPT.md) · [claim ledger](project/papers/boolean-flow-d2c/CLAIM_LEDGER.md) · [all-private stability theorem](project/research/post_ms/2026-09-17-stronger-pivot-v1/ALL_PRIVATE_STABILITY.md)

### Fixed-order reviewer packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) · [manuscript](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) · [verification companion](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf)
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) · [manuscript](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) · [verification companion](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf)
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) · [manuscript](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) · [verification companion](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf)
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) · [manuscript](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) · [verification companion](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf)
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) · [manuscript](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) · [verification companion](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf)
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md)
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md)
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md)
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md)
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md)

### General-theory reviewer packages

- [`7/12` maximum-degree reviewer-v1](releases/general-7-12-reviewer-v1/README.md)
- [`13/22` retained maximum-degree reviewer-v1](releases/general-13-22-reviewer-v1/README.md)
- [`293/500` retained maximum-degree reviewer-v1](releases/general-293-500-reviewer-v1/README.md)
- [General step-back structural package](releases/general-stepback-v1/README.md)
- [Joint-clipping reviewer-v1](releases/general-joint-clipping-reviewer-v1/README.md)
- [Heavy-load / routing reviewer-v1](releases/general-heavy-load-reviewer-v1/README.md)
- [Joint-routing reviewer-v1](releases/general-joint-routing-reviewer-v1/README.md)
- [Routing-tail reviewer-v1](releases/general-routing-tail-reviewer-v1/README.md)
- [Compatible-routing reviewer-v1](releases/general-compatible-routing-reviewer-v1/README.md)
- [Compatible-routing full-catalogue reviewer-v1](releases/general-compatible-catalogue-reviewer-v1/README.md)
- [Closed-compatible reviewer-v1](releases/general-closed-compatible-reviewer-v1/README.md)
- [Arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md)
<!-- REVIEW-MATERIALS:END -->
