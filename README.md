# Murty–Simon / Erdős Problem #742

**Reviewers — start here:** [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). GitHub Issues/comments are preferred for counterexamples, corrections and reproducibility reports.

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
| Source-price restoration | Original source-price replay **34905883642 SUCCESS**; earlier failed transfer run34904353492 remains recorded as failed |
| Conditioned source pricing | Exact branch scan over six original plus seven fresh profiles; run **34905354792 SUCCESS** for the frozen scan |
| Row471 rigidity | Conditioned branches `e_L=39,40` are exactly hand/verifier closed; run **34906169745 SUCCESS** including that rigidity check. Row471 remains open on `41,42,43,47` |
| Row108 source sharing | [`conditioned-source-sharing-v1`](project/research/general_n/2026-09-14-conditioned-source-sharing-v1/README.md) excludes **original synthetic row108** inside the stated selected-incidence relaxation: 40 exact block-total tuples -> 8 inherited multiblock rejections + 24 fixed-price closures + 8 exact common-pressure closures |
| Original synthetic sample | **708/713 rejected; five not rejected: 160,338,347,471,586.** Sample-level evidence only; no canonical whole-state promotion |
| Fresh-seed sample | **708/715 rejected; seven retained in a separate namespace.** Unchanged by the row108 result |
| Row108 verification | Local complete replay and remote workflow **34906766833 / job104185160249 SUCCESS**. The exact remote replay step completed successfully with the frozen 46,662 / 1,201 / 1,124 / 77 / 57,867 certificate counts |
| Documentation guards | Status-sync run34906766824 and reviewer-navigation run34906766838 both SUCCESS on the row108 commit. N30 package run34906766832 FAILED because the condensed root reviewer section omitted explicit frozen manuscript-PDF paths; this commit restores those links. No N30 proof/release bytes were changed |
| Active continuation | Attack row471 `e_L=41` first with selected-label/destination plus ONE common residual-neighbourhood constraint; in parallel carry exact common-pressure/source-incidence across the five remaining original profiles |

**Checkpoint — 14 September 2026, `row108-ci-receipt-v1`.** Inspected predecessor `010ea19981e67bab2395f6657a5416680cb2a3d1`. Row108's complete exact replay is now remotely green, while the unrelated N30 navigation regression from the predecessor is preserved explicitly and repaired by restoring the frozen PDF links. **Fixed-order, general7/12, canonical-frontier and sample mathematical status are unchanged from the predecessor.**

**Standing order:** every commit must update the current-status blocks in BOTH this README and [`CURRENT_STATE.md`](CURRENT_STATE.md), in the same atomic commit, including an explicit unchanged-mathematics statement when appropriate. Keep these fixed-order and general summaries near the top. See [`AGENTS.md`](AGENTS.md) and [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md).
<!-- CURRENT-STATUS:END -->

**Canonical repository:** `paullenz/MurtySimon742`. For a restart read [`CURRENT_STATE.md`](CURRENT_STATE.md), [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and newer commits. The complete pre-row108 root overview is preserved byte-for-byte in [`README_PRE_ROW108_2026-09-14.md`](README_PRE_ROW108_2026-09-14.md).

## Current research chain

Specific graph orders and explicitly defined relaxed profiles are laboratories for structural principles, not substitutes for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates a hypothetical graph into selected quasi-edge representatives, residual incidences, label demands, missing-pair loads and incoming capacities.

- [Shared block slack](project/research/general_n/2026-09-14-joint-blocks-v1/README.md): one shared low-block slack budget; original707/713 and fresh708/715 at that checkpoint.
- [Source-priced selected incidence](project/research/general_n/2026-09-14-source-sharing-v1/README.md): exact source-row dualization; restored replay34905883642 passed while the earlier failure remains preserved.
- [Stronger source-price search / witnesses](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md): 21/24 tested bounds improve; uncoupled witnesses for original160,338,347 show why stronger destination/residual correlation is needed.
- [Conditioned source pricing](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md): exact branch totals and legitimate caps. Its row471 rigidity successor closes `e_L=39,40`; run34906169745 passed the exact scan and rigidity verifier, leaving41,42,43,47.
- [Conditioned source sharing / row108](project/research/general_n/2026-09-14-conditioned-source-sharing-v1/README.md): exact row/type incidence plus one common source pressure excludes row108 in the stated relaxation; remote replay34906766833 succeeded.

For row108, one fixed signed price vector closes24 of the32 block-total tuples surviving the older multiblock screen. The remaining eight require unit charge at least211. Exact row/type flow reduces46,662 excess histograms to1,201 feasible histograms;1,124 already have exact incidence-charge upper below211, and exact common-pressure branch-and-bound eliminates the remaining77. Complete verifier output canonical parsed-JSON SHA256: `5ea860b79516d9a34e73a67fafdb7875cd3c9c99b01594b4bf3aab2c3e8a7629`.

## Failures and audit gates remain first-class evidence

Do not quietly delete, relabel or retrospectively clean up a failed lemma, non-closing experiment, counterexample or CI event. The454/597 simultaneous-multiblock non-rejection remains a negative predecessor result. Source-price run34904353492 remains failed even though the exact restoration replay later succeeded. N30 run34906766832 remains failed because the predecessor README omitted explicit frozen PDF navigation; this repair does not repaint that run green. Sample exclusions never change the canonical frontier without the separate promotion gate.

The2,655 recovered relational candidates require complete coverage, two implementations agreeing, zero unresolved cases, successful aggregate and a separate reviewed ledger step before promotion. No fresh live shard count is asserted here.

<!-- REVIEW-MATERIALS:START -->
## Papers and review materials

This reviewer-facing navigation surface is protected. Detailed canonical status remains [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md); new editions must update both surfaces rather than deleting this section.

### Fixed-order papers and packages

- [`n=25 reviewer-v2`](releases/n25-reviewer-v2/README.md) — [manuscript PDF](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf).
- [`n=27 reviewer-v2`](releases/n27-reviewer-v2/README.md) — [manuscript PDF](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf).
- [`n=28 reviewer-v2`](releases/n28-reviewer-v2/README.md) — [manuscript PDF](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) and [verification companion PDF](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf).
- [`n=29 reviewer-v4`](releases/n29-reviewer-v4/README.md) — [manuscript PDF](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) and [verification companion PDF](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf).
- [`n=30 reviewer-v3`](releases/n30-reviewer-v3/README.md) — [manuscript PDF](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) and [verification companion PDF](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf).
- [`n=31 reviewer-v1`](releases/n31-reviewer-v1/README.md).
- [`n=32 reviewer-v1`](releases/n32-reviewer-v1/README.md).
- [`n=33 reviewer-v1`](releases/n33-reviewer-v1/README.md).
- [`n=34 reviewer-v2`](releases/n34-reviewer-v2/README.md).
- [`n=35 reviewer-v1`](releases/n35-reviewer-v1/README.md).

### General-theory papers and reviewer packages

- [`7/12` maximum-degree reviewer-v1](releases/general-7-12-reviewer-v1/README.md).
- [`13/22` retained maximum-degree reviewer-v1](releases/general-13-22-reviewer-v1/README.md).
- [`293/500` retained maximum-degree reviewer-v1](releases/general-293-500-reviewer-v1/README.md).
- [General step-back structural package](releases/general-stepback-v1/README.md).
- [Joint-clipping reviewer-v1](releases/general-joint-clipping-reviewer-v1/README.md).
- [Heavy-load / routing reviewer-v1](releases/general-heavy-load-reviewer-v1/README.md).
- [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md).
- [Demand/tail projection reviewer-v1](releases/general-routing-tail-reviewer-v1/README.md).
- [Compatible-destination routing reviewer-v1](releases/general-compatible-routing-reviewer-v1/README.md).
- [Compatible-routing full-catalogue reviewer-v1](releases/general-compatible-catalogue-reviewer-v1/README.md).
- [Closed-compatible-potential reviewer-v1](releases/general-closed-compatible-reviewer-v1/README.md).
- [Fixed-neighbourhood / arc-realisation reviewer-v1](releases/general-arc-realisation-reviewer-v1/README.md).
<!-- REVIEW-MATERIALS:END -->

## Trust boundary

Hand derivation, same-assistant verification, remote CI, durable preservation and external acceptance are distinct. No timeout, missing output, unsuccessful search or floating infeasibility is proof. The canonical selected/residual bridge remains the principal correlated external-review dependency.
