# Murty–Simon / Erdős Problem #742

**Reviewers — start here:** [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). **GitHub Issues and comments are the preferred medium for feedback**: they keep counterexamples, corrections and discussion durable and attached to the relevant evidence. A short counterexample or a precise identification of the first invalid implication is especially valuable.

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **The unrestricted conjecture is not claimed proved.** External mathematical review, novelty assessment and independent third-party reproduction remain OPEN.

<!-- CURRENT-STATUS:START -->
## Current status: fixed-order candidates

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

## Current status: general research

| Workstream | Latest established or recorded position |
|---|---|
| General maximum-degree candidate | For n>=6, Delta(G)>=(7/12)n implies e(G)<floor(n^2/4); external review and novelty assessment open |
| Canonical finite frontier | **1,971 exclusions / 3,607 survivors; 977 quantified whole-state closures** — unchanged |
| Relational candidates | **2,655 recovered candidates remain UNPROMOTED** pending the full audit and separate reviewed ledger step |
| Original source-price bound | [Exact selected-incidence charge](project/research/general_n/2026-09-14-source-sharing-v1/README.md): signed source prices restore one exact row budget. Its 576 price evaluations give four weighted improvements and no profile closure |
| Stronger search and boundary evidence | [Price/witness continuation](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md): 21/24 tested bounds improve; three integer-checked joint-incidence/orientation witnesses show feasibility of the explicitly listed uncoupled relaxation for original160,338,347, NOT graph realizability |
| Conditioned source pricing | [Conditioned package](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md): same block-excess branches and legitimate caps; 9,293 incidence configurations, 24,063 priced inequalities, 150 strict improvements. Remote replay **34905354792 passed** the exact frozen full-output check |
| New row471 rigidity | [Hand branch closure](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/ROW471_RIGIDITY.md): at eta=2, e_L=39 forces at least 12 high excess with only 8 available; e_L=40 forces at least 10 with only 7. Exact integer verifier added. Row471 is **not** fully excluded |
| Row471 remaining conditioned branches | After the new hand step: **e_L=41,42,43,47**. The preceding conditioned scan had also retained 39,40; those two are now separately closed |
| Latest sample-excluding result | [Shared block-slack pressure](project/research/general_n/2026-09-14-joint-blocks-v1/README.md): sources share one budget of spare selected places |
| Original synthetic sample | Still **707/713 rejected**; six profiles not fully rejected: 108,160,338,347,471,586. Closing two internal branches of row471 does not change this count |
| Fresh-seed sample | Still **708/715 rejected**; seven retained in a separate namespace. Same generator, not independent generation |
| Retained negative experiment | Simultaneous multiblock test left 454/597 tuples across all six originals; no extra profile closure |
| Verification scopes | Original source-price restored replay 34905883642 passed after preserving the earlier failed transfer run; conditioned replay 34905354792 passed; stronger/witness package retains its separately stated local scope. External mathematical review remains open |
| Active continuation | Attack row471 **e_L=41 first**, then 42,43,47, with one actual selected-incidence matrix plus selected-label/destination and common residual-neighbourhood constraints; seek a reusable Hall/saturation lemma rather than broadening blind price search |

**Research checkpoint — 14 September 2026, `row471-rigidity-v1`.** Inspected predecessor: `aa6c41fcede3bf2e7e935a00840030ef0b9ee1df`. The conditioned source-price near misses at row471 `e_L=39,40` have been converted into exact hand contradictions. For `e_L=39`, the receiver/source-price squeeze forces `d_9>=4,d_23>=4,d_13>=2`; only one low-block selection is available among all demand-three-eligible sources, so even maximally overlapping high selections need at least 12 high excess while only 8 exists. For `e_L=40`, the analogous forced pressures are `4,3,2`, two low selections are available, and at least 10 high excess is required while only 7 exists. **These close two branches, not the row471 profile.** Original sample count stays707/713; fixed-order, general7/12 and canonical-frontier status are unchanged. The preceding conditioned replay run34905354792 is now recorded SUCCESS; the new branch verifier is added to that workflow and requires a fresh remote run before its own remote status is claimed.

<!-- SOURCE-PRICE-PUBLICATION:START -->
**Publication verification — 2026-09-14 22:48:27 UTC; run 34905883642.** The original source-price result file is restored to its pre-existing SHA256 `1953c61d26c68dc2bcbb9aeddbe0d18336e05b118541f4d9ca3f9528c808caae`. The UNCHANGED offline harness passed all source/input hashes, the canonical twelve-row input, the six-row transcription, 9,043 incidence/demand checks, 371 brute-force comparisons, three hostile/boundary fixtures and complete output equality for all 576 price evaluations. The failed run 34904353492 remains recorded. **Mathematical status unchanged: zero new profile exclusions.** This receipt covers the original source-sharing package, NOT the separate stronger price/witness package. Validated checkout: `e6c9915826173b7b4ab8f76dc9b944b710128b0b`; this atomic commit publishes the repaired data and paired status receipt. See [repair audit](project/research/general_n/2026-09-14-source-sharing-v1/CI_AUDIT.md).
<!-- SOURCE-PRICE-PUBLICATION:END -->

**Standing order:** every commit must update the current-status blocks in BOTH this README and [CURRENT_STATE.md](CURRENT_STATE.md), in the same atomic commit. Record the actual change even when mathematical status is unchanged. Keep these summaries near the top. See [CANONICAL_REPOSITORY.md](CANONICAL_REPOSITORY.md) and [AGENTS.md](AGENTS.md).
<!-- CURRENT-STATUS:END -->

**Canonical repository:** `paullenz/MurtySimon742`. **Restarts:** read [CURRENT_STATE.md](CURRENT_STATE.md), [RESEARCH_EVIDENCE_INDEX.md](RESEARCH_EVIDENCE_INDEX.md), and newer commits. The repository, not a chat transcript, is the durable source of truth.

## Research approach and detailed evidence

Specific graph orders and explicitly defined relaxed profiles are laboratories for structural principles, not substitutes for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates a hypothetical graph into selected quasi-edge representatives, residual incidences, label demands, missing-pair loads and incoming capacities. Keep structural surplus t, q-threshold tau and block threshold eta distinct:

```text
a=n-1-Delta, b=Delta, t=e(G)-b(a+1),
Q=r+2t+D0+Esel,
D0=S-r-2t>=0, Esel=Q-S>=0.
```

The cycle is exact constraints, finite tests, hand-proof extraction, hostile testing, separately structured verification, and return to the universal inequality. Zero-demand labels stay explicit; never silently assume their count is bounded by Esel. Surviving a relaxation does not imply graph realizability.

The [complete shared-slack overview](README_SHARED_SLACK_DETAILS_2026-09-14.md) is preserved **byte-for-byte**, including the hand-readable103<104 branch, full branch coverage, verification counts, fresh-seed results, failures and publication history. The [preceding handoff](CURRENT_STATE_PRE_COMMIT_STATUS_2026-09-14.md), all later research checkpoints in Git history, and the protected reviewer-navigation section remain retained. Historical observations are not live status.

The [shared-slack proof](project/research/general_n/2026-09-14-joint-blocks-v1/README.md), [offline replay guide](project/research/general_n/2026-09-14-joint-blocks-v1/REPRODUCE.md), [evidence index](RESEARCH_EVIDENCE_INDEX.md), and [durable publication audit](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md) retain exact inputs, proofs, counterexamples and scope. The original source-price, stronger search/witness and conditioned-price packages linked above remain distinct experiments. A file write or queued workflow is not verification.

## Failures, corrections and negative results are first-class evidence

This repository is intentionally **not** a success-only narrative. Failed lemmas, non-closing experiments, surviving relaxed profiles, hostile counterexamples, audit problems and wording corrections are part of the research record because they show exactly where an argument breaks, prevent the same mistake being rediscovered, and tell reviewers how much weight a surviving claim deserves. A later stronger result does not license us to rewrite the route as though the failed step never happened.

The standing rule is therefore: **do not quietly gloss over, delete, relabel or retrospectively “clean up” a failure.** Preserve the failed statement or experiment in its package or Git history; mark its status plainly; record the counterexample, limitation or audit event; and link the corrected or successor argument. Non-rejections remain visible rather than being presented as successes. A CI or publication failure stays a failure even if a later repair succeeds. Corrections should say whether they alter the theorem, the executable certificate, only the exposition, or the claimed verification scope.

Concrete examples already preserved in this repository include:

- **A tempting shared-slack shortcut was false.** The claim `sum_u (q_u-k_u)d_u <= E_high` fails because two sources can share the same positive label. The explicit two-source hostile fixture is retained in the shared-slack package. The valid theorem instead charges the single shared budget of low-block selected places; the counterexample is evidence for why that distinction is necessary.
- **The simultaneous multiblock extension did not close anything further.** It tested 597 consistent tuples across the six original boundary profiles and retained 454. That negative result is recorded explicitly rather than omitted because it produced no new profile exclusion; it narrows the next attack toward common selected-source usage.
- **The row-240 prose needed correction.** An initial explanation said every further pressure unit cost two slack, which was too broad. The corrected argument restricts that statement to moves affordable under the branch budget `J=2`; the theorem, executable verifier and frozen exclusion were unchanged. The earlier wording remains recoverable in Git history.
- **Verification and publication failures are not repainted green.** Run 34894544147 passed its mathematical/hash steps but failed its Git rebase, so its overall failure remains recorded. The later publication-only repair run 34895776658 is separately identified as successful rather than being used to rewrite the earlier run's status. The original source-price run34904353492 likewise remains a recorded failure even though the exact transferred-data error was later restored and replayed successfully in34905883642.
- **Errata and hostile review are retained.** The [source-degree display erratum](project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md), the [alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md), and the q-stratified crossing-gap audit remain reviewer-visible even when later work supersedes or works around the issue they exposed.

This preservation policy applies equally to hand proofs, exploratory computation, exact verifiers, CI, audit challenges and reviewer editions. The point is not to accumulate dead ends indiscriminately; it is to keep every **material** failure or correction that changes what can safely be inferred, together with enough evidence to reproduce or understand it.

## Retained routes and audit gate

[Priced tails](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md), [interval capacity](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md), [localized excess](project/research/general_n/2026-09-14-localized-excess-v1/README.md), [capped spill](project/research/general_n/2026-09-14-capped-spill-v1/README.md), [block pressure](project/research/general_n/2026-09-14-block-pressure-v1/README.md), and [conditioned excess](project/research/general_n/2026-09-14-conditioned-excess-v1/README.md) retain their own assumptions and evidence. The [exact q-stratified minimum](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md), [type-complete witness corollary](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md), and [q-layer threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) remain fallbacks alongside crossing-wall/saturation and maximum-cut/stability. Equality of minima is not pointwise equality; check monotonicity before transferring witness theorems to new caps. The normal-form strategy paragraph correctly requires a deficient subset for exclusion, rather than the all-subsets inequality characterizing Hall feasibility.

Audit34854911792 requires all2,655 inputs, both implementations agreeing, zero unresolved cases, a successful aggregate and a separate reviewed ledger step before promotion. No new live shard count is asserted. Fetch every job page or a complete diagnostic before reporting one. Preserve completed work; do not duplicate the audit, alter budgets/concurrency, or retry queued/successful jobs or computational timeouts. Sample exclusions do not change the canonical frontier.

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
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md) — source-first proof/review package; [hostile audit](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md).
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

## Trust boundary

Hand derivation, separately structured same-assistant verification, remote CI, preservation and external acceptance are distinct. No timeout, missing output, unsuccessful search or floating infeasibility is proof. The canonical selected/residual bridge remains the principal correlated external-review dependency. Preserve reviewer navigation, failed approaches and every audit gate.
