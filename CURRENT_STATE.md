# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** This is the durable restart surface for the project after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth.

## Canonical repository

- repository: `paullenz/MurtySimon742`
- GitHub repository ID: `1359206057`
- identity guard: [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md)
- legacy names such as `MurtySimon25` and historical `N25_*` filenames are **not** the current repository name.

**State synchronized:** 14 September 2026 through parent commit `eb10ae4b05c80ed6b3d919c3017a414e02344456` (`Freeze layered receiver reach pilot`), including the completed long-budget post-pair relational recovery, compatible-copy Hall exactness, canonical Hall marginal structure, layered receiver-capacity audit and the frozen layered receiver reach pilot.

The previous, more chronological versions of this file remain preserved in Git history. This file is intentionally kept tighter so a restart sees the actual live proof boundary first.

---

## 1. Canonical promoted frontier — unchanged pending audit

The canonical promoted whole-state position remains:

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
```

The 977 closure ledger remains protected by [`tools/check_n34_whole_state_ledger.py`](tools/check_n34_whole_state_ledger.py). Of those closures, 943 N34-derived states come from the independently cross-implemented potential-pair family; earlier closures remain separately preserved.

**Do not change the 3,607 headline merely because a discovery/recovery scan reports additional exclusions.** Promotion requires the dedicated audit gate described below.

### Full relational scan status

The layer/state-safe full scan of the 3,607 canonical survivors completed successfully:

```text
workflow run: 34820187136
head:         3255c0641b00ae97c426d1e089a6b6c92c8300fc
status:       completed / success
```

The long-budget retry/recovery of incomplete or unresolved discovery states also completed successfully:

```text
workflow run: 34844403328
status:       completed / success
```

This means the discovery and recovery stages have completed. **The resulting candidate exclusions are not yet canonical promotions.** The remaining gate is a fresh, separately implemented state-by-state audit of the recovered aggregate, followed by a distinct promotion step only if the implementations agree.

Required chain:

```text
checkpointed discovery                     COMPLETE
 -> layer-safe aggregate                   COMPLETE for discovery
 -> long-budget recovery                   COMPLETE
 -> fresh cross-implementation audit       OPEN
 -> separately gated ledger promotion      OPEN
```

N34 and N35 provenance must remain separate throughout.

---

## 2. Fixed-order candidate results

The preserved fixed-order candidate proofs remain:

- `n=25`: `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2; external specialist review open.
- `n=27`: `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2; external review open.
- `n=28`: `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening; external review open.
- `n=29`: `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed; external review open.
- `n=30`: `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3; external review open.
- `n=31`: `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1; external review open.
- `n=32`: `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1; external review open.
- `n=33`: `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1; external review open.
- `n=34`: `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final heavy certificate replaced by a short hand argument; external review open.
- `n=35`: `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1; external review open.

These are candidate proofs on their own preserved ledgers. The general-theory 3,607 frontier is a research frontier and is **not** a list of unresolved cases in the fixed-order N34/N35 proofs.

---

## 3. Canonical general bridge

The canonical graph-to-constraint framework is [`project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).

Core notation:

```text
a = n-1-Delta,
b = Delta,
t = e(G)-b(a+1).
```

The bridge supplies the exact selected/residual ledger, demand inequalities, selected-edge forcing, endpoint load, residual activity for positive surplus, charging, threshold capacity, isolated-C exclusion and residual h-index consequences. Downstream finite and Hall arguments remain conditional on this bridge. Highest-value external red-team targets remain the quasi-edge selection/injection and forcing portions of the bridge, especially Sections 2–3, 6 and 8–12.

External mathematical acceptance of the bridge remains OPEN.

---

## 4. Hall/orientation structural chain — current audited position

Current package:

[`project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md)

### 4.1 Exact type and cut structure

Internally audited results now include:

1. **Whole-type Hall theorem.** A minimum target-Hall cut may be chosen as a union of complete `(q,c,P)` type classes.
2. **Exact quotient max-flow and submodularity.** The labelled target-flow relaxation is exactly represented by the type-level quotient network.
3. **Sharp hardness order.** Minimum Hall witnesses admit the sharpened dominance structure

   ```text
   x >=_* y iff c_x<=c_y
                  and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
   ```

4. **Canonical maximal minimizer `M+`.** Minimum-margin type sets form a lattice. Their union is the unique inclusion-maximal/minimum-margin witness, is a sharp-hardness up-set and has a unique minimal-generator antichain.
5. **Moving staircase theorem.** Ordering its generators by cross degree gives

   ```text
   c_1 < ... < c_h,
   q_1 <= ... <= q_h,
   ```

   with `P` strictly increasing on equal-`q` plateaux. Membership in `M+` is a moving `(q,P)` threshold as `c` changes.

The Murty source universe has `c=q+rho<=a`, so there is at most one canonical generator breakpoint at each integer cross-degree level and `h<=a+1`.

### 4.2 Coarse staircase-band relaxation

[`STAIRCASE_BAND_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/STAIRCASE_BAND_HALL.md) groups selected source types by staircase generator. Generator-compatible target neighborhoods are contiguous intervals of band indices. This yields a smaller necessary band-flow relaxation.

The coarse relaxation is intentionally lossy. In the frozen deterministic 15-state pilot it detected:

```text
205,918 / 205,919 exact target-Hall failures
= 99.999514%
```

The unique false negative was N34 state `226`.

### 4.3 Compatible-copy band theorem — formal and audited

The state-226 diagnostic showed the coarse band model invented five source-target incidences by granting all members of a band the generator's compatibility. The correction is [`COMPATIBLE_COPY_BAND_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/COMPATIBLE_COPY_BAND_HALL.md): a band-to-target edge counts only source copies in that band which are individually compatible with that target.

The compatible-copy aggregation lemma passed a separately written dependency-free verifier:

```text
workflow run:                          34844598113
result:                                success
profiles checked:                      2,715
sharp up-sets checked:                43,988
labelled-pair capacity checks:       636,193
exact-to-refined flow-order checks:   43,988
state-226 fixture:                     PASS
state-226 refined flow / demand:       38 / 39
```

Frozen audit: [`COMPATIBLE_COPY_BAND_HALL_AUDIT.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/COMPATIBLE_COPY_BAND_HALL_AUDIT.md).

### 4.4 Canonical-witness exactness — major current theorem

A stronger consequence is internally audited in [`CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_WITNESS_COMPATIBLE_COPY_EXACTNESS.md).

For the canonical maximal Hall witness `M+`, take **all** of its staircase bands. For every target type, summing compatible-copy counts over those bands gives exactly the number of selected compatible source copies used in the original Hall cut, with the same diagonal deletion. Therefore the all-bands compatible-copy Hall margin is **exactly** `F(M+)`.

Consequences inside the target-flow relaxation:

- if target Hall fails, the compatible-copy network built from `M+` fails;
- the all-bands cut itself witnesses the same deficiency;
- the compatible-copy representation is not merely empirically near-exact on canonical failures: it captures the canonical Hall obstruction exactly.

Independent finite audit:

```text
workflow run:                   34847381427
result:                         success
profiles checked:               2,486
infeasible profiles:            1,518
whole-staircase identities:     2,486
feasibility-equivalence checks: 2,486
```

Artifact digest:

```text
sha256:f20e97ec0021e788e0903a36e8ae67235e747dc3c7581b693fd6af76de7504d3
```

### 4.5 Fresh end-to-end compatible-copy Murty pilot

The compatible-copy instrumentation was rerun from scratch on the frozen deterministic 15-state pilot:

```text
workflow run:       34846952940
result:             success
profiles tested:    201,493,148
target-Hall fails:      205,919
coarse band detects:    205,918
coarse band misses:           1
compatible-copy detects:205,919
compatible-copy misses:       0
```

Artifact digest:

```text
sha256:ad2b600051843e1f482b9a7a0f89fe2c64d2469911f5e18c2db6115c0c406b2d
```

This pilot is direct replay evidence for the 205,919/205,919 figure. The canonical-witness exactness theorem explains structurally why that result should occur for canonical target-Hall failures.

### 4.6 Canonical Hall marginal/boundary theorem

[`CANONICAL_HALL_MARGINALS.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_HALL_MARGINALS.md) records local optimality constraints at the canonical boundary.

For the unique maximal minimizer `M+`:

- every type outside `M+` has **strictly positive integer addition marginal**;
- equivalently, adding an outside type gains at least `n_tau q_tau + 1` units of target capacity;
- the gain has an explicit compatible unsaturated-slack formula;
- every exterior source copy has directed-compatible degree at least `q_tau+1`;
- removing a selected type from `M+` loses at most its demand;
- types belonging to the unique minimal minimizer `M-` satisfy the corresponding strict removal inequality.

Independent audit:

```text
workflow run:          34848012710
result:                success
profiles:              2,486
exterior types:        3,142
interior types:        5,585
M- types:              3,148
minimum exterior gap:  1
```

This is now a preferred route for constraining the staircase boundary itself.

### 4.7 Layered receiver-capacity projection — verified, strong but not exact

[`LAYERED_RECEIVER_CAPACITY.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/LAYERED_RECEIVER_CAPACITY.md) rewrites

```text
sum_w min(P_w,m_w)
```

as an exact overlap of receiver-capacity layers and compatible-source-count layers. Discarding only the target-by-target correlation gives a one-dimensional rearrangement upper bound. In the Murty setting the canonical residual/incoming budgets then bound high receiver-capacity layers.

Independent verification is green:

```text
workflow run:       34848254327
result:             success
arbitrary trials:   5,000
Murty-like trials: 10,000
strict losses seen: 4,675
```

The dedicated frozen reach pilot is [`LAYERED_RECEIVER_REACH_PILOT.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/LAYERED_RECEIVER_REACH_PILOT.md):

```text
workflow run:                       34848635869
result:                             success
profiles tested:                    201,493,148
target-Hall failures:                   205,919
layered receiver detected:              205,107
layered receiver false negatives:           812
detection fraction:                  99.605670%
maximum observed passing layer excess:       5
```

Artifact digest:

```text
sha256:6221ecb4a20685a1f3c02e3a3bd8ce8d18c729572a504d8a981a2c9ffcd179c0
```

This is an important narrowing result. The one-dimensional receiver-layer distributions retain almost all exact Hall obstruction, but the lost correlation between capacity level and compatible-source-count level matters for 812 pilot profiles. The next attack should target that specific correlation loss rather than revert to arbitrary Hall subsets.

---

## 5. Preserved negative results / routes not to repeat

The following shortcuts are false and must remain visible:

- no universal one-dimensional Ferrers ordering of individual sources;
- one principal sharp up-set is not sufficient in general;
- no universal two-generator bound: Murty pilot failures reach eight canonical generators, with four modal;
- interval-neighborhood bands do **not** imply it suffices to test contiguous sets of bands; a preserved three-band counterexample has a failing disconnected cut `{1,3}` while every contiguous interval passes;
- the receiver-layer rearrangement is not exact: the frozen pilot has 812 false negatives;
- a scan survival means only survival of the tested relaxation, never graph realizability.

Failures, bugs, rejected lemmas, audit challenges and counterexamples are research assets and must continue to be preserved rather than overwritten.

---

## 6. Current mathematical priority

The canonical Hall obstruction is now represented exactly by a **canonical moving staircase**, and its compatible-copy all-bands cut reproduces the exact canonical Hall deficiency. The principal goal is therefore to derive a Murty-specific **parametric inequality** that forces the canonical whole-staircase Hall margin to be nonnegative under the bridge constraints.

The layered receiver experiment narrows the missing ingredient further: pure one-dimensional capacity/count layers explain 205,107 of 205,919 pilot Hall failures, leaving **812 correlation-sensitive failures**.

The preferred next route is:

1. stratify those 812 false negatives by rearrangement slack, canonical generator count, receiver-capacity levels, compatible-count levels, `q/c/rho`, total excess `E` and state;
2. identify the smallest target-correlation statistic that distinguishes the 812 from true Hall-feasible profiles;
3. prove a Murty-specific bound on that statistic using residual budgets, source cap `q+rho<=a`, incoming caps, total-excess bounds and canonical boundary marginals;
4. fold that bound into the whole-staircase Hall inequality.

The aim is a symbolic all-order inequality, not another fixed-order-only screen.

---

## 7. Immediate operational priorities

1. **Finish the fresh cross-implementation audit of the recovered 3,607-state relational scan.** Only after exact agreement may candidate exclusions be promoted to the canonical ledger.
2. **Diagnose the 812 layered-receiver false negatives.** Preserve the full classification and any failed proposed correlation summaries.
3. **Develop the all-order whole-staircase inequality** from the canonical boundary and receiver-correlation structure.
4. **Red-team each new universal lemma independently.** Finite green CI supports arithmetic and implementation consistency but is not external mathematical acceptance.
5. **Keep reviewer navigation and this handoff synchronized** whenever theorem-level status changes.

---

## 8. Standing current-state synchronization order

`CURRENT_STATE.md` is the mandatory restart surface.

It must be synchronized whenever any of the following occurs:

- a canonical frontier/ledger count changes;
- a discovery or recovery stage completes;
- a theorem or corollary is promoted into the internally audited chain;
- a proposed theorem is falsified or materially weakened;
- an audit gate completes or fails;
- a material pilot changes the principal research direction;
- a new principal attack becomes the research priority;
- work pauses after a material research block.

Every sync must state the **trust boundary**: discovery, internal finite verification, same-assistant audit, independent implementation, external mathematical review and external reproduction are distinct statuses.

Before any project restart, first confirm [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md), then read this file, then inspect commits newer than the synchronization point.

---

## 9. External-status boundary

Nothing above constitutes external acceptance of the unrestricted Murty–Simon conjecture.

At present:

- fixed-order results are candidate proofs with external review open;
- Hall/bridge structural results have increasingly strong internal proofs and independent finite replays, but external mathematical review and novelty assessment remain open;
- the 3,607-state relational discovery/recovery output is not a canonical frontier reduction until the fresh cross-implementation audit and separate promotion gate pass;
- genuinely independent third-party computational reproduction remains open.

Internal success should continue to be recorded precisely, but never described as external verification.