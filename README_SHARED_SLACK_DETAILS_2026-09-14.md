# Murty–Simon / Erdős Problem #742

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **Updated 14 September 2026 through the shared block-slack theorem and fresh-seed verification.** The new [proof package](project/research/general_n/2026-09-14-joint-blocks-v1/README.md) records the derivation, all hypothesis boundaries, complete integer certificates, a preserved counterexample and unsuccessful multiblock extensions.

The promoted finite frontier remains **1,971 exclusions / 3,607 survivors**, with **977 quantified whole-state closures**. The **2,655 recovered relational candidates remain unpromoted**. The unrestricted conjecture is **not claimed proved**. External mathematical review, novelty assessment and independent third-party reproduction remain OPEN.

## Fixed-order and general candidate status

| Scope | Preserved candidate result; external review open |
|---|---|
| n=25 | e(G)<=156, equality exactly K(12,13); reviewer-v2 |
| n=27 | e(G)<=182, equality exactly K(13,14); reviewer-v2 |
| n=28 | e(G)<=196, equality exactly K(14,14); reviewer-v2 plus analytic hardening |
| n=29 | e(G)<=210, equality exactly K(14,15); reviewer-v4; difficult Delta=16 branch hand-closed |
| n=30 | e(G)<=225, equality exactly K(15,15); reviewer-v3 |
| n=31 | e(G)<=240, equality exactly K(15,16); source-first reviewer-v1 |
| n=32 | e(G)<=256, equality exactly K(16,16); source-first reviewer-v1 |
| n=33 | e(G)<=272, equality exactly K(16,17); source-first reviewer-v1 |
| n=34 | e(G)<=289, equality exactly K(17,17); reviewer-v2; final heavy certificate hand-replaced |
| n=35 | e(G)<=306, equality exactly K(17,18); reviewer-v1 |
| General maximum-degree result | For n>=6, Delta(G)>=(7/12)n implies e(G)<floor(n^2/4); candidate theorem, external review and novelty assessment open |

**Canonical repository:** `paullenz/MurtySimon742`; see [CANONICAL_REPOSITORY.md](CANONICAL_REPOSITORY.md). **Restarts:** read [CURRENT_STATE.md](CURRENT_STATE.md), [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), and newer commits. The repository, not a chat transcript, is the durable source of truth.

**External reviewers:** begin with [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md) and [releases/REVIEW_READY_INDEX.md](releases/REVIEW_READY_INDEX.md). Hostile review, counterexamples, literature corrections and independent reproduction are welcome.

The previous root overview and handoff are preserved BYTE FOR BYTE in [README_PRE_SHARED_SLACK_2026-09-14.md](README_PRE_SHARED_SLACK_2026-09-14.md) and [CURRENT_STATE_PRE_SHARED_SLACK_2026-09-14.md](CURRENT_STATE_PRE_SHARED_SLACK_2026-09-14.md). Their older counts and queue observations are historical. Earlier archives, failed approaches and reviewer packages remain intact. The protected reviewer-navigation section below is retained unchanged.

## How this research develops general theory

Specific graph orders and explicitly defined relaxed profiles serve as laboratories for structural principles, not substitutes for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates a hypothetical graph into selected quasi-edge representatives, residual incidences, label demands, missing-pair loads and incoming capacities.

```text
a=n-1-Delta, b=Delta, t=e(G)-b(a+1),
Q=r+2t+D0+Esel,
D0=S-r-2t>=0, Esel=Q-S>=0.
```

Structural surplus is t, q-threshold tau, demand-block threshold eta. Zero-demand count z is never silently bounded by Esel. The cycle is exact constraints, finite tests, hand-proof extraction, hostile testing, separately structured verification, and return to the universal inequality. Surviving a relaxation never implies graph realizability.

## New result: spare selections are shared, not independently reusable

The [conditioned-excess argument](project/research/general_n/2026-09-14-conditioned-excess-v1/README.md) couples incoming caps and the charge envelope to the SAME excess in one demand block. It previously resolved row295's equality case: four sources would need total pressure10 but could carry at most8.

The new [shared-slack theorem](project/research/general_n/2026-09-14-joint-blocks-v1/README.md) quantifies the positive-slack case. Let L contain every zero-demand label. Define f_u as the number of source u's selections forced into L, M=sum f_u, and S_L=sum of its demands. Fix the actual low-block excess e_L and put

```text
H=Esel-e_L,
J=S_L+e_L-M.
```

J is the TOTAL number of low-block selected places beyond the forced selections. If pressure is d_u=(p_u-rho_u+1)_+, every selected positive label outside L needs at least d_u excess. Consequently, for d>=1,

```text
gamma_u(d;H)=(q_u-f_u-floor(H/d))_+,
gamma_u(0;H)=0,
sum_u gamma_u(d_u;H)<=J.
```

This is a shared budget: every source cannot spend the same J spare places separately. Its equivalent two-defect-coupled form is

```text
H+sum_u gamma_u(d_u;H)<=Q-r-2t-D0+S_L-M.
```

The full note retains the necessary eligibility ceilings, zero-demand treatment, monotonicity for tail pressure and a group-count corollary. An exact integer pressure DP gives a safe upper bound on tail incoming capacity. It is exact only for the stated pressure/slack projection, not for joint selected-incidence or graph realization.

### A hand-readable branch: 103 is less than 104

For one previously surviving row240 branch, H=4 and J=2. A tail needs104 incoming units; receivers provide28 free units plus74 pressure units without spending slack. With only two shared slack places, at most one further pressure unit is affordable. Therefore incoming capacity is at most28+74+1=103<104.

The complete profile exclusion covers all low-block excess totals, not only this illustrative branch: prior price certificates cover e_L39,40, and the new shared-slack bounds cover41 through45. Complete inherited/new coverage is also recorded for rows258 and342. The initial draft's overly broad marginal-cost wording and a conservative table entry were explicitly corrected; the theorem, verifier and frozen result were unchanged.

### Original sample and fresh-seed evidence

| Necessary screens on the SAME original 713 profiles | Rejected | Not rejected |
|---|---:|---:|
| Earlier localized/priced tests | 652 | 61 |
| Capped spill and integer envelope | 694 | 19 |
| Demand-block/source pressure | 701 | 12 |
| Conditioned excess | 704 | 9 |
| Shared block slack, retaining earlier screens | **707** | **6** |

The six original remaining rows are108,160,338,347,471,586. Their arrays remain in the committed original input. These are **not six remaining cases of the conjecture**, three new whole-state closures or a change to the canonical3,607-state frontier.

A fresh seed74220260919 of the SAME generator produced715 profiles passing the stated scalar-ledger, cap, selected-incidence and potential-pair-flow screens. Prior/new stages reject708 and retain seven. Shared slack adds three exclusions beyond the earlier screens in this fresh sample. All seven non-rejected arrays and all three complete new certificates are committed in [FRESH_RECHECK_FULL.json](project/research/general_n/2026-09-14-joint-blocks-v1/FRESH_RECHECK_FULL.json). Fresh row IDs are a distinct namespace. A new seed is not independently designed generation, graph realization or a universal theorem.

## Verification, negative results and reproducibility

The new local verifier completed9,293 exhaustive selected-incidence configurations,25,391 arbitrary low-block checks including12,305 positive-slack blocks,7,839 valid random-incidence systems from10,000 trials, and3,000 independent brute-force comparisons covering237,067 pressure vectors. All three standing hostile q-tail examples remain. These incidence and synthetic domains have separate stated assumptions.

The tempting stronger inequality summing high-label excess only once across all sources is false: two sources can share the same positive label. The explicit actual-incidence counterexample is preserved. The valid theorem instead counts low-block selected places in one matrix.

The simultaneous multiblock extension tested597 consistent block-total tuples on the six remaining profiles:25 failed total capacity,118 failed priced bounds and454 remain across all six. **It produced no additional full-profile exclusion.** The complete larger output is reconstructible from committed code/inputs and pinned by its full digest, and retained in the portable bundle and CI output. It is not falsely described as a raw JSON file committed in the package.

[One offline replay command](project/research/general_n/2026-09-14-joint-blocks-v1/REPRODUCE.md) checks exact source blobs, reruns the parent conditioned proof, verifies every new shared/fresh JSON value, regenerates the fresh corpus and reproduces the failed multiblock experiment. It needs Python standard library and g++17, not live artifact downloads or an optimizer. The unified whole-harness CI34898768799, queued at first inspection, subsequently completed SUCCESS on 14 September 2026; its downloaded parent/shared/fresh/multiblock outputs were compared locally with exact equality. See the dated [CI audit receipt](project/research/general_n/2026-09-14-joint-blocks-v1/CI_AUDIT.md). Earlier queued observations remain historical, not current status.

## Documentation and durable evidence

The [research evidence index](RESEARCH_EVIDENCE_INDEX.md) records the chain of assumptions and exact verification scopes. The [starting joint-block plan](project/research/general_n/2026-09-14-joint-blocks-v1/PLAN.md) was committed before new experiments.

All16 preceding raw/derived evidence files are now committed in the [durable directory](project/research/general_n/2026-09-14-evidence-preservation-v1/durable/) at `b6a15db114d7b4f3b71d73da816daec563f11824`. [PUBLICATION_AUDIT.md](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md) records that run34894544147 passed its mathematical/hash steps but failed Git rebase on an unclean checkout; publication-only repair34895776658 then succeeded using verified bytes. The old overall failed run is not relabeled green. The repair did not rerun or modify the256-shard audit.

Readable exploratory sources, unsuccessful numerical searches, all prior block-output objects, full original corpus/scanner and prior raw snapshots are preserved. Rejected encoded transfers remain documented in [TRANSFER_ERRATUM.md](project/research/general_n/2026-09-14-evidence-preservation-v1/TRANSFER_ERRATUM.md). Neither a successful file write nor a queued workflow is accepted as verification.

## Retained exact routes and audit gate

[Priced tails](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md), [interval capacity](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md), [localized excess](project/research/general_n/2026-09-14-localized-excess-v1/README.md), [capped spill](project/research/general_n/2026-09-14-capped-spill-v1/README.md) and [block pressure](project/research/general_n/2026-09-14-block-pressure-v1/README.md) retain their own evidence and counterexamples. The earlier205,931-export explanation retains its original shared-generation/early-stopping scope, not a new whole-state scan.

The [exact q-stratified minimum](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md), [type-complete witness corollary](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md), and [q-layer threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) remain fallbacks. Equality of minima is not pointwise equality; check monotonicity before transferring witness theorems to new caps. Crossing-wall/saturation and maximum-cut/stability routes remain retained.

Audit34854911792 has a strict promotion gate: all2,655 inputs, both implementations agreeing, zero unresolved, successful aggregate and a separate reviewed ledger step. No new live shard count is asserted here. Fetch every job page or a complete diagnostic before reporting current status. Preserve completed work; do not duplicate the audit, alter budgets/concurrency or retry queued/successful jobs or computational timeouts. Capped-spill34885163695 and combined capped/block34887492789 passed their scopes; this does not complete the relational audit.

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

This reviewer-facing index is intentionally duplicated here as a protected navigation surface. The detailed canonical status remains [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md), and new editions must update both surfaces rather than deleting this section.

### Fixed-order papers and packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) — [manuscript PDF](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf).
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) — [manuscript PDF](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf).
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) — [manuscript PDF](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf).
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) — [manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) and [verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf).
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) — [manuscript PDF](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) and [verification companion PDF](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf).
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md).
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md) — source-first proof/review package; [exact equality ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md).
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n33/2026-09-12-candidate-v1/AUDIT.md).
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md) — complete candidate package; [normalization audit and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md).
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md) — complete candidate package; [internal audit](project/research/n35/2026-09-12-candidate-v1/AUDIT.md).

### General-theory papers and reviewer packages

- [`7/12` maximum-degree reviewer-v1](releases/general-7-12-reviewer-v1/README.md) — [manuscript PDF](releases/general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf).
- [`13/22` retained maximum-degree reviewer-v1](releases/general-13-22-reviewer-v1/README.md) — [manuscript PDF](releases/general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf).
- [`293/500` retained maximum-degree reviewer-v1](releases/general-293-500-reviewer-v1/README.md) — [manuscript PDF](releases/general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) and [verification companion PDF](releases/general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf).
- [General step-back structural package](releases/general-stepback-v1/README.md) — balanced-degree theorem candidate, `a=14`, fifteen-label and sixteen-label results.
- [Joint-clipping reviewer-v1](releases/general-joint-clipping-reviewer-v1/README.md) — sharp scalar tail bounds and tight-threshold obstruction.
- [Heavy-load / routing reviewer-v1](releases/general-heavy-load-reviewer-v1/README.md).
- [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md).
- [Demand/tail projection reviewer-v1](releases/general-routing-tail-reviewer-v1/README.md).
- [Compatible-destination routing reviewer-v1](releases/general-compatible-routing-reviewer-v1/README.md).
- [Compatible-routing full-catalogue reviewer-v1](releases/general-compatible-catalogue-reviewer-v1/README.md).
- [Closed-compatible-potential reviewer-v1](releases/general-closed-compatible-reviewer-v1/README.md).
- [Fixed-neighbourhood / arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md).
- [Whole-type orientation Hall research package](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md) — exact type/cut structure, canonical moving staircase, compatible-copy exactness, exterior residual expansion and q-stratified correlation programme; internal audits green where explicitly marked, external review/novelty open.

### Reviewer entry points, audits and corrections

- [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) — reviewer orientation and high-value review targets.
- [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md) — canonical theorem-level manuscript/package index.
- [Canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
- [General-foundations audit](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md).
- [N29 public-release / normalization audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md).
- [Source-degree display erratum](project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md).
- [Alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md).
- [q-stratified crossing-gap audit](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_CROSSING_GAP_AUDIT.md).

Superseded reviewer editions and failed/corrected research remain preserved in Git history and the linked package histories; they are not silently deleted.
<!-- REVIEW-MATERIALS:END -->

## Next research target and trust boundary

Attack common selected-source usage across several blocks or the full multiresource shared-slack constraint. Six original and seven fresh non-rejected profiles are explicit boundary evidence, not graph constructions. The universal goal remains a contradiction forced by full canonical structure rather than extrapolation from either sample.

Hand derivation, separately structured same-assistant verification, remote CI, preservation and external acceptance are distinct. No timeout, missing output, unsuccessful search or floating infeasibility is proof. The canonical selected/residual bridge remains the principal correlated external-review dependency. Preserve reviewer navigation, failed approaches and every audit gate.
