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
| Latest necessary bound | [Source-priced selected-incidence charge](project/research/general_n/2026-09-14-source-sharing-v1/README.md): signed source prices restore exact selected-incidence row budgets; external review open |
| Stronger search and boundary evidence | [Price/witness continuation](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md): 21/24 tested bounds improve and three exact joint-incidence/orientation witnesses show the stated uncoupled relaxation is feasible for original 160,338,347; no graph realization or profile exclusion |
| Conditioned/fresh continuation | [Conditioned source pricing](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md): exact row prices are coupled to the SAME block-excess branch and branch-specific caps; all six original and seven fresh boundary profiles remain non-rejected |
| Row-471 near miss | At `eta=2`: `e_L=39`, upper 232→225 vs lower 224 (gap -1); `e_L=40`, upper 230→225 vs lower 223 (gap -2). Best retained price puts 1 on sources 9 and 23 |
| Latest sample-excluding structural result | [Shared block-slack pressure](project/research/general_n/2026-09-14-joint-blocks-v1/README.md): sources must share one budget of spare selected places |
| Original synthetic sample | 707 of 713 rejected; six not rejected: 108,160,338,347,471,586 |
| Fresh-seed sample | 708 of 715 rejected; seven not rejected: 20,91,391,490,528,562,677 in a separate namespace |
| Preserved unsuccessful extensions | Simultaneous multiblock retained 454/597 tuples; coarse pricing, stronger bounded pricing, and conditioned pricing all add **zero full-profile closures**. These negative results remain explicit |
| Verification state | Shared-slack has a recorded remote pass. The original source-price workflow run 34904353492 failed **before mathematics** on a format-sensitive JSON byte-hash mismatch; this commit repairs the replay to canonical-JSON hashing while retaining full parsed equality. Conditioned-source-price remote replay is newly installed and not yet claimed passed |
| Active continuation | Focus on row-471 `eta=2`, `e_L=39,40`: impose one actual selected-incidence matrix together with destination-label and shared residual-neighbourhood constraints; seek a hand Hall/saturation obstruction rather than broadening blind price search |

**Checkpoint — 14 September 2026, `conditioned-source-pricing-v1`.** Inspected predecessor: `b2110c7e4c96483bc2aa9931777f9aac9956dcdd`. This commit preserves both earlier source-price packages and their complete negative/witness evidence, adds the planned same-block conditioned price scan, and tests the seven fresh profiles separately. Local deterministic checks cover 9,293 actual selected-incidence configurations and 24,063 priced inequalities, with 150 strict improvements over zero price; **no new profile closure** results. The strongest new information is the row-471 one- and two-unit near miss above. Complete local full-output SHA256 is `1aec5dc47102ec24f64cc9776c624b32d025112b06fb643f306a0768e091639a`. The failed original remote replay is preserved and its serialization-only hash bug is repaired without weakening parsed-result equality. Fixed-order, general 7/12 and canonical-frontier status are unchanged.

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

The [complete preceding overview](README_SHARED_SLACK_DETAILS_2026-09-14.md) is preserved **byte-for-byte** and contains the full shared-slack derivation, the hand-readable 103<104 branch, branch-coverage ranges, verification counts, fresh-seed results, negative experiments and publication history. Its status statements are historical observations as of that checkpoint; the opening summaries above and [live handoff](CURRENT_STATE.md) are current. Earlier archives remain intact. The protected reviewer-navigation section below is retained, with its N33 hostile-audit path corrected.

The [shared-slack proof package](project/research/general_n/2026-09-14-joint-blocks-v1/README.md), [offline replay guide](project/research/general_n/2026-09-14-joint-blocks-v1/REPRODUCE.md), [research evidence index](RESEARCH_EVIDENCE_INDEX.md), and [durable-evidence publication audit](project/research/general_n/2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md) retain exact inputs, proofs, failures, counterexamples and replay scopes. A successful file write or queued workflow is not verification. The [original source-price package](project/research/general_n/2026-09-14-source-sharing-v1/README.md), [stronger search/witness package](project/research/general_n/2026-09-14-source-pricing-witnesses-v1/README.md), and [conditioned source-price continuation](project/research/general_n/2026-09-14-conditioned-source-pricing-v1/README.md) retain distinct exact experiments and limitations.

## Failures, corrections and negative results are first-class evidence

This repository is intentionally **not** a success-only narrative. Failed lemmas, non-closing experiments, surviving relaxed profiles, hostile counterexamples, audit problems and wording corrections are part of the research record because they show exactly where an argument breaks, prevent the same mistake being rediscovered, and tell reviewers how much weight a surviving claim deserves. A later stronger result does not license us to rewrite the route as though the failed step never happened.

The standing rule is therefore: **do not quietly gloss over, delete, relabel or retrospectively “clean up” a failure.** Preserve the failed statement or experiment in its package or Git history; mark its status plainly; record the counterexample, limitation or audit event; and link the corrected or successor argument. Non-rejections remain visible rather than being presented as successes. A CI or publication failure stays a failure even if a later repair succeeds. Corrections should say whether they alter the theorem, the executable certificate, only the exposition, or the claimed verification scope.

Concrete examples already preserved in this repository include:

- **A tempting shared-slack shortcut was false.** The claim `sum_u (q_u-k_u)d_u <= E_high` fails because two sources can share the same positive label. The explicit two-source hostile fixture is retained in the shared-slack package. The valid theorem instead charges the single shared budget of low-block selected places; the counterexample is evidence for why that distinction is necessary.
- **The simultaneous multiblock extension did not close anything further.** It tested 597 consistent tuples across the six original boundary profiles and retained 454. That negative result is recorded explicitly rather than omitted because it produced no new profile exclusion; it narrowed the attack toward common selected-source usage.
- **Source pricing remains a non-closing strengthening.** The original coarse experiment, stronger bounded search, and now the conditioned/fresh scan all improve real upper bounds but close no boundary profile. The row-471 conditioned branches miss by only one and two units; that near miss is retained as guidance, not presented as success.
- **The original source-price remote replay failed before mathematics.** Run 34904353492 stopped at a raw JSON hash mismatch caused by serialization/formatting. The failure remains recorded. The repair canonicalizes JSON before hashing and still requires complete parsed-result equality; it does not relabel the failed run as green.
- **The row-240 prose needed correction.** An initial explanation said every further pressure unit cost two slack, which was too broad. The corrected argument restricts that statement to moves affordable under the branch budget `J=2`; the theorem, executable verifier and frozen exclusion were unchanged. The earlier wording remains recoverable in Git history.
- **Verification and publication failures are not repainted green.** Run 34894544147 passed its mathematical/hash steps but failed its Git rebase, so its overall failure remains recorded. The later publication-only repair run 34895776658 is separately identified as successful rather than being used to rewrite the earlier run's status.
- **Errata and hostile review are retained.** The [source-degree display erratum](project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md), the [alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md), and the q-stratified crossing-gap audit remain reviewer-visible even when later work supersedes or works around the issue they exposed.

This preservation policy applies equally to hand proofs, exploratory computation, exact verifiers, CI, audit challenges and reviewer editions. The point is not to accumulate dead ends indiscriminately; it is to keep every **material** failure or correction that changes what can safely be inferred, together with enough evidence to reproduce or understand it.

## Retained routes and audit gate

[Priced tails](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/PRICED_TAIL_BUDGET.md), [interval capacity](project/research/general_n/2026-09-14-q-tail-interval-budget-v1/README.md), [localized excess](project/research/general_n/2026-09-14-localized-excess-v1/README.md), [capped spill](project/research/general_n/2026-09-14-capped-spill-v1/README.md), [block pressure](project/research/general_n/2026-09-14-block-pressure-v1/README.md), and [conditioned excess](project/research/general_n/2026-09-14-conditioned-excess-v1/README.md) retain their own assumptions and evidence. The [exact q-stratified minimum](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_MINCUT_EXACTNESS.md), [type-complete witness corollary](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_TYPE_COMPLETE_WITNESS.md), and [q-layer threshold normal form](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_LAYER_THRESHOLD_NORMAL_FORM.md) remain fallbacks alongside crossing-wall/saturation and maximum-cut/stability. Equality of minima is not pointwise equality; check monotonicity before transferring witness theorems to new caps. The normal-form strategy paragraph now correctly requires some deficient subset for exclusion, rather than the all-subsets inequality that characterizes Hall feasibility.

Audit 34854911792 requires all 2,655 inputs, both implementations agreeing, zero unresolved cases, a successful aggregate and a separate reviewed ledger step before promotion. No new live shard count is asserted here. Fetch every job page or a complete diagnostic before reporting one. Preserve completed work; do not duplicate the audit, alter budgets/concurrency, or retry queued/successful jobs or computational timeouts. Sample exclusions do not change the canonical frontier.

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
