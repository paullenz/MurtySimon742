# Murty–Simon / Erdős Problem #742

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **Updated 14 September 2026 through conditioned spill slack and the row-295 equality obstruction: proof `ab132ffd4c82f50d4ffe2120e8167c861e7ba6a6`, executed verifier `0baedfab7df5870fdd8b475d7eed8163f075844f`, frozen result `73d06b1990b0995df7b78b2cf9226c730d6a9dcb`.**

The promoted finite frontier remains **1,971 exclusions / 3,607 survivors**, with **977 quantified whole-state closures**. The **2,655 recovered relational candidates remain unpromoted**. The unrestricted conjecture is **not claimed proved**. External mathematical review, novelty assessment and genuinely independent third-party reproduction remain OPEN.

**Canonical repository:** `paullenz/MurtySimon742`; see [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md). **Restarts:** read [`CURRENT_STATE.md`](CURRENT_STATE.md), the new [`RESEARCH_EVIDENCE_INDEX.md`](RESEARCH_EVIDENCE_INDEX.md), and commits newer than the synchronization point. The repository, not a chat transcript, is the durable source of truth.

**External reviewers:** begin with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). Hostile review, counterexamples, literature corrections and independent reproduction are welcome.

The entire preceding overview is preserved verbatim in [`README_PRE_CONDITIONED_2026-09-14.md`](README_PRE_CONDITIONED_2026-09-14.md), with its historical statistics and links. The full prior handoff is [`CURRENT_STATE_PRE_CONDITIONED_2026-09-14.md`](CURRENT_STATE_PRE_CONDITIONED_2026-09-14.md). Earlier histories, failed approaches and reviewer packages remain intact. The protected reviewer-navigation section below is retained.

## How this research develops general theory

Specific graph orders and explicitly defined relaxed profiles serve as laboratories for structural principles, not as substitutes for an all-order proof. The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates a hypothetical graph into selected quasi-edge representatives, residual incidences, label demands, missing-pair loads and incoming capacities.

```text
a=n-1-Delta, b=Delta, t=e(G)-b(a+1),
Q=r+2t+D0+Esel,
D0=S-r-2t>=0, Esel=Q-S>=0.
```

Structural surplus is t, q-threshold tau and demand-block threshold eta. Zero-demand count z is never silently restricted by z<=Esel. The working cycle is exact constraints, finite tests, hand-proof extraction, immediate hostile testing, separately structured verification and return to the universal inequality. Surviving a relaxation never implies graph realizability.

## New result: resolve a tight charge bound through forced incidences

The [conditioned-excess package](project/research/general_n/2026-09-14-conditioned-excess-v1/README.md) resolves the preceding row-295 equality case with a short hand contradiction.

Twelve sources must select both demand-one labels. The old pressure inequalities give lower and upper charge bounds both equal to126. Equality forces the low-label selected columns to be completely filled by those twelve sources, leaving only six excess units for all other labels. The four sources with q=3 would then need total pressure10, but each selects three distinct remaining labels and can have pressure at most2. Their total is at most8:

```text
feasibility would require 10 <= 8.
```

The proof identifies every equality condition; it does not infer impossibility merely because an upper bound is tight. The exact source-cap table and hand arithmetic are independently checked by the committed verifier. Its graph application inherits the canonical bridge's external-review status.

### General conditional spill-slack lemma

Let L contain all zero-demand labels, let A_u be the labels eligible at source u, and define

```text
S_L=sum_{i in L}s_i,
f_u=(q_u-|A_u outside L|)_+,
M=sum_u f_u,
m_u=|A_u intersect L|.
```

Fix the ACTUAL label excess e_L in L. Set J=S_L+e_L-M and E_H=Esel-e_L. Actual low-block selections satisfy sum k=M+J and k_u>=f_u, hence

```text
k_u<=kmax_u=min(q_u,m_u,f_u+J).
```

When q_u>kmax_u, distinct positive-demand labels outside L imply the stronger incoming cap

```text
p_u<=rho_u-1+floor(E_H/(q_u-kmax_u)).
```

The key improvement is to use the SAME e_L in this cap and the integer charge envelope. Exhaust all its possible integer values. A profile is excluded only after every branch is contradicted. This couples two earlier safe relaxations that could otherwise spend the shared excess differently. It requires no universal high-q-tail theorem or equality of a Hall minimum with a tail minimum.

### Completed finite reach: twelve remaining profiles become nine

The final verifier directly rechecks all twelve preceding sample non-rejections. Complete budget splits exclude rows295,365,570:

| Sample row | Conditioning threshold | All excess values covered |
|---|---:|---|
| 295 | eta=1 | e_L=22,...,28 |
| 365 | eta=1 | e_L=22,...,38 |
| 570 | eta=2 | e_L=43,...,49 |

Every branch is rejected by a strict integer price/capacity inequality or an empty necessary projection. Frozen certificates include129>126,206>205 and242>241. The [complete reproduction guide](project/research/general_n/2026-09-14-conditioned-excess-v1/REPRODUCE.md) binds the entire output, including failed attempts and non-rejected branches, to a canonical JSON SHA256.

Retaining the preceding certificates, the sampled corpus progresses as follows:

| Necessary screens on the same 713 sampled profiles | Rejected | Not rejected |
|---|---:|---:|
| Earlier localized/priced screen | 652 | 61 |
| Capped spill and integer envelope | 694 | 19 |
| Demand-block/source-cap pressure | 701 | 12 |
| Conditioned excess, retaining all prior screens | **704** | **9** |

The nine remaining row IDs are108,160,240,258,338,342,347,471,586. The original twelve complete input arrays remain committed in [`REMAINDER_12.json`](project/research/general_n/2026-09-14-block-pressure-v1/REMAINDER_12.json). **This is not a three-state reduction of the canonical3607-state frontier, an independently regenerated exhaustive graph search or an all-order proof.**

The new local checks passed9293 actual selected-incidence configurations,42649 conditioned inequalities,2000 independent brute-force envelope comparisons and all three standing hostile q-tail examples. Empty/full conditioning blocks are explicitly checked. The new verifier is standard-library code; it reuses prior cap/receiver routines but independently expresses the new conditional cap and DP. Same-assistant independent implementation is not external acceptance.

## Retained foundations, failures and exact routes

The [demand-block/source-pressure package](project/research/general_n/2026-09-14-block-pressure-v1/README.md) retains the209>190 certificate and complete prior sample verification. [Capped positive excess and all-source spill](project/research/general_n/2026-09-14-capped-spill-v1/README.md) retains57>48, its400758 checks,3000 independent DP comparisons and812-profile replay. [Priced tails](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md), [interval capacity](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md) and [localized excess](project/research/general_n/2026-09-14-localized-excess-v1/README.md) remain separate links in the chain. The earlier205931-export explanation and80>77 fixture retain their original shared-generation/early-stopping scope, not a new whole-state scan here.

The [exact q-stratified minimum](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md), [type-complete witness corollary](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md) and [q-layer threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) remain fallbacks under their stated hypotheses. Equality of minima is not pointwise equality. Check monotonicity before transferring witness theorems to new caps.

The [hostile q-tail examples](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/MURTY_Q_TAIL_HALL_CONJECTURE.md), old-cap fixed-weight obstruction, frozen interval gaps and incomplete wider scans remain preserved. The row-295 singleton-bound attempt failed to lower126; the new proof instead uses equality rigidity. Source-weight, multiblock and numerical multiplier explorations and their non-exclusions are now preserved as readable historical code and JSON objects in the [evidence-preservation package](project/research/general_n/2026-09-14-evidence-preservation-v1/README.md). Numerical solver status is not proof.

Crossing-wall/saturation and independent maximum-cut/stability routes remain retained. The latter uses e(G)=|X||Y|+I-M; I<=M for some cut would suffice, but the naive edge-to-missing-pair matching shortcut is false.

## Documentation and reproducibility

The new [research evidence index](RESEARCH_EVIDENCE_INDEX.md) separates proof dependencies, internal checks, raw input provenance, exact replay, archival status and external review. Eleven original exploratory source files have been recovered byte-for-byte, with a prior-module convenience copy and all five block-experiment output objects. Original source Git blobs were checked before publication. Two large historical capped output files were regenerated locally with exact original raw-byte hashes.

The new conditioned checkpoint can be replayed from committed source and its twelve committed inputs alone, with no live artifact download. Full canonical output hash:

```text
7a29e4b93739f676fe2f11701235d0982d621b85b1086de7ece057723221455e
```

A new hash-strict [materialization helper](project/research/general_n/2026-09-14-evidence-preservation-v1/materialize_evidence.py) and CI run34894544147 verify and publish the older raw corpus, scanner, pilot/812 inputs, complete combined-CI snapshots, historical outputs and the full conditioned replay into the repository. It passed locally; remote publication was still queued at inspection. Do not equate a queued workflow with a committed durable archive: check its successful materialization record and commit. Rejected encoded-transfer attempts are documented in [TRANSFER_ERRATUM.md](project/research/general_n/2026-09-14-evidence-preservation-v1/TRANSFER_ERRATUM.md), and were not accepted as evidence.

## Finite frontier and GitHub audit gates

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
recovered relational candidates: 2,655 — UNPROMOTED
```

**Capped-spill34885163695 and combined capped/block-pressure34887492789 have passed.** Complete actual/expected outputs from the latter were downloaded and compared locally. Its full257-job snapshot at14September2026 19:43:10UTC records the successful plan,128 successful audit shards and128 queued shards. This is a timestamped snapshot, not a current aggregate-completion claim. New conditioned/evidence-sealing run34894544147 remained queued at direct recheck.

Audit34854911792 still has a strict promotion gate: all2655 inputs covered, both implementations agreeing, zero unresolved states, successful aggregate, then a separate reviewed ledger step. No successful or queued job was restarted, the256-shard audit was not duplicated, and its budgets/concurrency were not changed. The hourly monitor retains its conservative retry rules. Green internal CI, repository publication and external mathematical acceptance are different statuses.

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

Use common excess totals across several blocks, or enforce the joint selected-incidence requirements lost by independent top-source optimization. Row295 is now excluded through equality rigidity; the nine explicitly retained sample profiles are the next boundary tests. The universal goal remains a contradiction forced by full canonical structure, not by fitting the sample.

Hand derivation, finite verification, separately structured internal arithmetic, remote CI, data preservation and external mathematical acceptance are distinct. No timeout, missing output, failed search or floating infeasibility is proof. The canonical selected/residual bridge remains the principal correlated external-review dependency. Preserve reviewer navigation, failed approaches and every audit gate.
