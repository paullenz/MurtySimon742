# Murty–Simon / Erdős Problem #742

Open, reproducible research on the Murty–Simon conjecture / Erdős Problem #742. **Updated 14 September 2026 through the audited q-stratified crossing-gap development.** The canonical promoted finite frontier remains **1,971 exclusions / 3,607 survivors**, with **977 quantified whole-state closures**. A recovered set of **2,655 additional relational candidate exclusions is not yet promoted** and remains behind a fresh cross-implementation audit gate.

The unrestricted Murty–Simon conjecture is **not claimed proved** by this repository. Independent mathematical review, novelty assessment and genuinely independent third-party computational reproduction remain OPEN. Green CI, exact replay, same-assistant audit and repository publication are not external acceptance.

**Canonical repository:** `paullenz/MurtySimon742`. See [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md).

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). Canonical theorem-level packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project welcomes hostile review, counterexamples, literature corrections and genuinely independent reproduction; GitHub Issues are the preferred place to report a suspected flaw.

**Research restarts:** read [`CURRENT_STATE.md`](CURRENT_STATE.md), then inspect commits newer than its synchronization point. The repository, not any chat transcript, is the durable source of truth.

## Current headline status

| Scope | Current project status |
|---|---|
| `n=25` | Complete candidate: `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2; external specialist review open |
| `n=27` | Complete candidate: `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2; external review open |
| `n=28` | Complete candidate: `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening; external review open |
| `n=29` | Complete candidate: `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed; external review open |
| `n=30` | Complete candidate: `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3; external review open |
| `n=31` | Complete candidate: `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1; external review open |
| `n=32` | Complete candidate: `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1; external review open |
| `n=33` | Complete candidate: `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1; external review open |
| `n=34` | Complete candidate: `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final heavy certificate replaced by a short hand proof; external review open |
| `n=35` | Complete candidate: `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1; external review open |
| General maximum-degree result | Candidate theorem: for `n>=6`, `Delta(G)>=(7/12)n` implies `e(G)<floor(n^2/4)`; internal exact audits green; external review and novelty assessment open |
| Canonical Hall route | Exact type-compressed target Hall, canonical maximal witness `M+`, moving staircase, compatible-copy exactness, strict exterior residual expansion and residual sharp-upset reduction are internally audited |
| Receiver correlation route | Global receiver layers detect `205,107/205,919` frozen-pilot Hall failures; the 812-case residue is `q`-stratified exact; exact crossing identity `U_q-H=C_q` is independently internally audited |
| Generalisation frontier | **1,971 exclusions / 3,607 survivors** from canonical quantified whole-state ledgers; `3,529` are N34 equality-derived and `78` are N35 `m=306`-derived; these are scalar states, not surviving graphs |
| Recovered relational candidates | **2,655** further candidate exclusions from the completed full-frontier recovery; **not promoted** pending fresh two-implementation audit and separate ledger promotion |

## How this research develops general theory

The aim is to extract structural principles explaining why a diameter-two edge-critical graph cannot be too dense. Specific graph orders are used as laboratories in which to develop those principles, expose false shortcuts and identify hypotheses needed by broader theorems. Progress at finitely many orders does not by itself establish an all-order result.

The [canonical graph-to-constraint bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md) translates graph structure into demands, residual budgets, selected quasi-edge representatives and source/destination loads. We organise the constraints by

```text
a=n-1-Delta,
b=Delta,
t=e(G)-b(a+1).
```

The working cycle is:

```text
graph structure
 -> exact constraint bridge
 -> strong finite experiments
 -> extract structural theorem
 -> hostile counterexample search
 -> independent finite verifier
 -> return to the all-order inequality.
```

Failed approaches, rejected lemmas, bugs, counterexamples and audit challenges are preserved rather than silently discarded.

## Current all-order structural route

The main general-theory programme has moved beyond arbitrary Hall-cut search. The present structure is a pair of coupled canonical staircases.

### 1. Primary canonical Hall staircase

The current package is [`project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md).

Internally audited results include:

- complete `(q,c,P)` type classes suffice for a minimum target-Hall cut;
- the labelled target-flow relaxation is represented exactly by a quotient type network;
- the Hall margin is submodular;
- sharp-hardness dominance constrains minimum witnesses;
- minimum-margin witnesses form a lattice;
- their union `M+` is the unique maximal minimizer and a sharp-hardness up-set;
- `M+` has a unique minimal-generator antichain;
- ordered by cross degree, those generators form a moving staircase with strictly increasing `c`, weakly increasing `q`, and increasing `P` on equal-`q` plateaux;
- the compatible-copy whole-staircase representation reproduces the exact Hall margin of `M+`.

See [`CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md).

On the frozen 15-state pilot:

```text
profiles tested:          201,493,148
target-Hall failures:         205,919
compatible-copy detects:      205,919
compatible-copy misses:             0
```

The older coarse-band relaxation missed exactly one profile; that failure was preserved and led directly to the compatible-copy correction.

### 2. Exterior residual-slack staircase

For the primary canonical witness `M+`, write

```text
y_w = number of M+-sources directed-compatible with target w,
s_w = (P_w-y_w)_+.
```

The [strict exterior slack-expansion theorem](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_HALL_SLACK_EXPANSION.md) says every nonempty exterior source set `T` must satisfy

```text
sum_w min(s_w,K_T(w)) >= D(T)+1.
```

The [residual sharp-upset reduction](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/EXTERIOR_SLACK_UPSET_REDUCTION_AUDIT.md) removes arbitrary exterior-subset search: if residual strict expansion fails, a residual sharp up-set witnesses the failure.

This yields the present structural picture:

```text
primary P-staircase M+           must be deficient,
exterior residual-s staircase    must remain strictly expanding.
```

The two systems compete for the same target resources. The [coupled residual-slack budget](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/COUPLED_RESIDUAL_SLACK_BUDGET.md) and [positive-slack incidence pressure](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/POSITIVE_SLACK_INCIDENCE_PRESSURE.md) make that competition explicit.

### 3. The 812 receiver-layer exceptions and the `q` pivot

A one-dimensional receiver-layer rearrangement detects

```text
205,107 / 205,919
```

exact target-Hall failures in the frozen pilot, leaving 812 correlation-sensitive failures.

The full 812-case diagnostic is preserved in [`Q_STRATIFIED_812_DIAGNOSTIC.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_812_DIAGNOSTIC.md). Its key result is:

```text
812 global-layer false negatives examined
812 q-stratified detections
812 q-stratified upper bounds equal exact receiver capacity
0   positive q-stratified gaps
```

Thus the entire difficult residue is explained by allowing receiver capacity to be rearranged across different `q` levels. The newer scalar residual-slack inequalities remain valid but do not themselves eliminate any of these 812 profiles; the decisive missing information is `q`-level correlation.

### 4. Exact crossing statistic `C_q`

The [q-stratified crossing-gap identity](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/Q_STRATIFIED_CROSSING_GAP_AUDIT.md) identifies exactly what can still be lost after retaining `q`:

```text
U_q(S)-H(S)=C_q(S),
```

where

```text
C_q(S)=sum_{q,m} min(H^S_{q,m},L^O_{q,m}).
```

The identity has passed a separately written verifier with 384,612 exhaustive cases and 20,000 random trials, including many deliberately hostile positive-crossing examples. A preserved counterexample shows that `C_q=0` is **not** an abstract Hall theorem.

Therefore the current Murty-specific analytic target has become very sharp:

```text
control or exclude C_q>0
```

for the canonical maximal witness, using the bridge, selected-excess budget, residual/source caps and canonical maximality.

[`CANONICAL_EQUAL_Q_SWAP_RIGIDITY.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_EQUAL_Q_SWAP_RIGIDITY.md) gives the first structural consequence: every positive equal-`q` crossing forces a rigid swap/saturation wall. This is now the main hand-proof target.

## Finite frontier and audit gates

The canonical promoted finite position is

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
```

The 943-state N34 potential-pair family and earlier whole-state closures are protected by the canonical ledger and durability checks in the [alternative-attacks package](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md).

A subsequent layer/state-safe full relational scan and long-budget recovery completed on all 3,607 canonical survivors. The recovered aggregate contains **2,655 candidate relational exclusions**. These remain deliberately unpromoted.

At this README update:

```text
recovered candidate exclusions: 2,655
final cross-implementation audit run: 34854911792
status: queued / not yet PASS
promotion: blocked
canonical frontier: unchanged at 3,607 survivors
```

The audit uses two independently structured implementations and requires exact state-by-state agreement with zero unresolved states before any promotion.

Separately, the full frozen-pilot `q`-crossing replay is run `34859094097`; at this update it is also queued. The 812-case result and the independently verified crossing identity are already frozen, but full-pilot `C_q=0` is **not** being claimed before that replay completes.

## Fixed-order frontier through n=35

The fixed-order candidates have their own complete ledgers and reviewer packages. The 3,607-state generalisation frontier is **not** a list of unresolved obligations in those fixed-order proofs.

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

## Failures, audit challenges and corrections are part of the result

The project deliberately preserves negative results because they constrain the general theory. Important examples now include:

- the N29 normalization bug and its [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md);
- the [general-foundations corrections](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md);
- the [N34 failed relaxation and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md);
- the [alternative-attacks audit](project/research/general_n/2026-09-13-alternative-attacks-v1/AUDIT.md);
- no universal one-dimensional Ferrers ordering of individual sources;
- one principal sharp up-set is not sufficient in general;
- no universal two-generator bound: canonical failures in the broader pilot reach eight generators;
- interval-neighborhood bands do not make contiguous band cuts sufficient;
- the coarse staircase-band relaxation is not exact (state 226 is the preserved counterexample);
- global receiver-layer rearrangement is not exact (812 frozen-pilot false negatives);
- `q`-stratified exactness is not a theorem of arbitrary Hall systems: a preserved positive-`C_q` counterexample exists;
- survival of any relaxation never implies graph realizability.

Exact replay, internal audit, repository publication and external mathematical acceptance are distinct statuses.

## How the earlier generalisation machinery reached this point

The current Hall/correlation programme grew out of several earlier routes rather than replacing their record.

| Programme | Main recorded result | Role now |
|---|---|---|
| [General heavy load](releases/general-heavy-load-reviewer-v1/README.md) | all-threshold load/routing family; hundreds of finite exclusions | aggregate structural foundation |
| [Joint heavy routing](releases/general-joint-routing-reviewer-v1/README.md) | exact catalogue exclusions | preserved finite route |
| [Compatible routing catalogue](releases/general-compatible-catalogue-reviewer-v1/README.md) | strong routing/Hall finite screens | precursor to the quantified frontier |
| [Containment spill / pair overlap](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md) | scalar spill witnesses and fixed-pattern failures | exposed the quantifier gap |
| [Shared residual budgets](project/research/general_n/2026-09-13-shared-residual-budget-v1/README.md) | very strong fixed-geometry rejection | showed why selection quantification was essential |
| [Alternative attacks](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md) | selection-free/excess/Hall/orientation/potential-pair machinery and 977 quantified closures | canonical finite-frontier foundation |
| [Type-compressed orientation Hall](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md) | exact canonical Hall staircase, residual staircase and q-correlation structure | current main general-theory route |

The detailed state-by-state chronology remains preserved in these packages and in Git history; the top-level README is intentionally focused on the current theorem structure and audit boundary.

## Current research priorities

1. **Control the crossing statistic `C_q`.** Use canonical equal-`q` swap rigidity, selected-excess accounting, residual/source caps and the bridge to prove `C_q=0` for genuine canonical witnesses, or at least bound it below what is needed to repair a Hall deficit.
2. **Complete the full frozen-pilot q-crossing replay.** The 812 difficult profiles already have `C_q=0`; run `34859094097` tests the exact statistic across all 205,919 target-Hall failures without changing any theorem status prematurely.
3. **Complete the 2,655-state final relational cross-audit.** Run `34854911792` must obtain exact agreement between the two implementations with zero unresolved states before any new whole-state exclusion is promoted.
4. **Derive the all-order two-staircase contradiction.** The desired endpoint is a symbolic theorem showing that a deficient primary `P`-staircase and a strictly expanding residual `s`-staircase cannot coexist under Murty bridge constraints.
5. **Strengthen independent review and reproduction.** Highest-value external targets remain the graph-to-constraint bridge, selected/quasi-edge injection and forcing steps, directed compatibility, total-excess/source caps, potential-pair theorem, and the new Hall/staircase chain.
6. **Continue genuinely independent routes.** Maximum-cut/stability and other structurally different attacks remain useful both as possible proofs and as red-team checks against overfitting the Hall programme.

## Independent maximum-cut route

For any cut `X|Y`, if `I` is the number of internal edges and `M` the number of missing cross-pairs,

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would prove Murty–Simon. A direct one-internal-edge/one-cross-nonedge matching proof is false and is preserved as a failed route, but the cut/stability direction remains a useful independent programme.

## Trust boundary

The largest correlated mathematical risk is still the canonical bridge: its graph-to-quasi-edge implications, selected/residual ledger, forcing lemmas and endpoint consequences require independent specialist review. The Hall/staircase theory has increasingly strong internal proofs and separately written finite audits, but those do not substitute for external mathematical checking.

No solver timeout, floating infeasibility status, unsuccessful search, missing output or unreviewed discovery file is used as proof. Candidate finite exclusions are promoted only through their stated replay/audit gates.

For restart-level detail and the exact live CI state, read [`CURRENT_STATE.md`](CURRENT_STATE.md).