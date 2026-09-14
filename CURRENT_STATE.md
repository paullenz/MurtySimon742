# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart surface after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth.

## Canonical repository

- repository: `paullenz/MurtySimon742`
- GitHub repository ID: `1359206057`
- identity guard: [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md)
- legacy names such as `MurtySimon25` and historical `N25_*` filenames are not the current repository name.

**State synchronized:** 14 September 2026 through parent commit `90417a9c1d8788689ff3a875e11f1e7938a66a79` (`Freeze canonical Hall slack-expansion CI audit`).

Previous longer versions remain preserved in Git history. This file is intentionally concise and should be updated whenever theorem status, frontier status, audit status or principal research priority changes.

---

## 1. Canonical promoted frontier — unchanged pending audit

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
```

The closure ledger remains protected by `tools/check_n34_whole_state_ledger.py`. Of the 977 closures, 943 N34-derived states come from the cross-implemented potential-pair family; earlier closures remain separately preserved.

**Do not change the 3,607 headline from discovery/recovery output alone.** Promotion requires the dedicated cross-implementation audit gate and then a separate ledger-promotion step.

### Relational full-frontier status

The layer/state-safe full scan of the 3,607 canonical survivors completed successfully:

```text
workflow run: 34820187136
head:         3255c0641b00ae97c426d1e089a6b6c92c8300fc
status:       completed / success
```

The long-budget retry/recovery of incomplete or unresolved states also completed successfully:

```text
workflow run: 34844403328
status:       completed / success
```

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

Preserved candidate proofs remain:

- `n=25`: `e(G)<=156`, equality `K(12,13)`; reviewer-v2; external specialist review open.
- `n=27`: `e(G)<=182`, equality `K(13,14)`; reviewer-v2; external review open.
- `n=28`: `e(G)<=196`, equality `K(14,14)`; reviewer-v2 plus analytic hardening; external review open.
- `n=29`: `e(G)<=210`, equality `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed; external review open.
- `n=30`: `e(G)<=225`, equality `K(15,15)`; reviewer-v3; external review open.
- `n=31`: `e(G)<=240`, equality `K(15,16)`; source-first reviewer-v1; external review open.
- `n=32`: `e(G)<=256`, equality `K(16,16)`; source-first reviewer-v1; external review open.
- `n=33`: `e(G)<=272`, equality `K(16,17)`; source-first reviewer-v1; external review open.
- `n=34`: `e(G)<=289`, equality `K(17,17)`; reviewer-v2; external review open.
- `n=35`: `e(G)<=306`, equality `K(17,18)`; reviewer-v1; external review open.

These fixed-order candidate proofs are separate from the 3,607-state general-theory frontier.

---

## 3. Canonical general bridge

Canonical graph-to-constraint framework:

`project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`

Core notation:

```text
a = n-1-Delta,
b = Delta,
t = e(G)-b(a+1).
```

The bridge supplies the selected/residual ledger, demand inequalities, forcing, endpoint load, residual activity for positive surplus, charging, threshold capacity, isolated-C exclusion and residual h-index consequences. Downstream Hall and finite arguments remain conditional on this bridge.

Highest-value external red-team targets remain the quasi-edge selection/injection and forcing portions, especially Sections 2–3, 6 and 8–12. External mathematical acceptance remains open.

---

## 4. Hall/orientation structural chain — internally audited position

Current package:

`project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`

### 4.1 Exact type/cut structure

Internally audited results include:

1. complete `(q,c,P)` type classes suffice for a minimum target-Hall cut;
2. the labelled target-flow relaxation is represented exactly by the quotient type network;
3. the Hall margin is submodular;
4. sharp-hardness dominance constrains minimum witnesses;
5. minimum-margin witnesses form a lattice;
6. their union `M+` is the unique maximal minimizer and is a sharp-hardness up-set;
7. `M+` has a unique minimal-generator antichain;
8. ordered by cross degree, those generators form a moving staircase with strictly increasing `c`, weakly increasing `q`, and increasing `P` on equal-`q` plateaux.

In the Murty source universe `c=q+rho<=a`, so there is at most one generator breakpoint per integer cross-degree level and `h<=a+1`.

### 4.2 Compatible-copy staircase representation

The coarse staircase-band relaxation detected `205,918/205,919` exact target-Hall failures in the frozen 15-state pilot. Its unique false negative was state 226.

The corrected compatible-copy band theorem counts only source copies actually compatible with each target. Its independent verifier is green:

```text
workflow run:                        34844598113
profiles checked:                    2,715
sharp up-sets checked:              43,988
labelled-pair capacity checks:     636,193
state-226 refined flow / demand:     38 / 39
```

### 4.3 Canonical-witness exactness

For the canonical maximal Hall witness `M+`, take **all** staircase bands. Summing compatible-copy counts across all bands gives exactly the original selected compatible-source multiplicity at every target, including diagonal deletion. Hence the all-bands compatible-copy Hall margin is exactly `F(M+)`.

Independent audit:

```text
workflow run:                   34847381427
result:                         success
profiles checked:               2,486
infeasible profiles:            1,518
whole-staircase identities:     2,486
feasibility-equivalence checks: 2,486
```

Fresh Murty pilot replay:

```text
workflow run:        34846952940
profiles tested:     201,493,148
target-Hall fails:       205,919
compatible-copy detects: 205,919
compatible-copy misses:        0
```

Thus canonical target-Hall failure is now represented exactly by a canonical moving staircase and its whole-staircase compatible-copy cut.

### 4.4 Canonical boundary marginals

For `M+`:

- every exterior type has strictly positive integer addition marginal;
- adding exterior type `tau` gains at least `n_tau q_tau+1` target-capacity units;
- every exterior source copy has directed-compatible degree at least `q_tau+1`;
- removing a selected type loses at most its removed demand;
- types in the unique minimal minimizer `M-` obey the corresponding strict removal inequality.

Audit:

```text
workflow run:          34848012710
profiles:              2,486
exterior types:        3,142
interior types:        5,585
minimum exterior gap:      1
result:                success
```

### 4.5 Strict exterior slack expansion — latest audited theorem

`CANONICAL_HALL_SLACK_EXPANSION.md` strengthens the one-type marginal theorem to **every nonempty set of exterior complete types**.

For the residual receiver slack left by `M+`,

```text
s_sigma = (P_sigma-y_sigma(M+))_+,
```

and any nonempty exterior type set `T`,

```text
sum_sigma n_sigma min(s_sigma,K_T(sigma)) >= D(T)+1.
```

Equivalently, the entire exterior of a deficient canonical staircase must itself form a strictly expanding residual Hall system in the unused receiver slots left by `M+`.

Whole-exterior consequence:

```text
sum_sigma n_sigma s_sigma >= D(O)+1
```

whenever the exterior `O` is nonempty.

Independent audit:

```text
workflow run:          34849028879
result:                success
profiles checked:      2,086
infeasible profiles:   1,193
exterior subsets:     11,828
interior subsets:     16,121
M- subsets:            6,125
minimum exterior gap:      1
```

The `+1` is sharp on the audit suite.

### 4.6 Layered receiver-capacity projection

The exact receiver term

```text
sum_w min(P_w,m_w)
```

can be written as overlap of receiver-capacity layers and compatible-source-count layers. Forgetting only the target-by-target correlation gives a one-dimensional rearrangement upper bound.

The theorem verifier is green:

```text
workflow run:       34848254327
arbitrary trials:   5,000
Murty-like trials: 10,000
strict losses:      4,675
result:             success
```

Frozen Murty pilot:

```text
workflow run:                        34848635869
profiles tested:                     201,493,148
target-Hall failures:                    205,919
layered receiver detected:               205,107
layered receiver false negatives:            812
detection fraction:                   99.605670%
maximum passing layer excess:                 5
```

So pure one-dimensional receiver-layer distributions explain almost all canonical Hall failures, but 812 pilot profiles genuinely require some target-level correlation information.

---

## 5. Preserved negative results / routes not to repeat

- no universal one-dimensional Ferrers ordering of individual sources;
- one principal sharp up-set is not sufficient in general;
- no universal two-generator bound: Murty pilot failures reach eight canonical generators, with four modal;
- interval-neighborhood bands do not make contiguous band cuts sufficient;
- receiver-layer rearrangement is not exact: 812 frozen-pilot false negatives remain;
- survival of a relaxation never implies graph realizability.

Failures, rejected lemmas, bugs, counterexamples and audit challenges must remain preserved.

---

## 6. Current mathematical priority

The main target is now a **Murty-specific all-order inequality ruling out a deficient canonical staircase**.

The structural picture is:

```text
hypothetical counterexample
 -> canonical deficient Hall staircase M+
 -> exact whole-staircase compatible-copy deficit
 -> strict residual Hall expansion on every exterior set
 -> Murty residual/incoming/source-cap budgets
```

The strongest immediate opportunity is to force a contradiction between the **deficient interior staircase** and the **strictly expanding exterior residual-slot system**.

In parallel, the 812 layered-receiver false negatives identify exactly where one-dimensional rearrangement loses too much correlation.

Preferred mathematical attack:

1. classify the 812 false negatives by state, deficit, rearrangement slack, generator count, receiver-capacity layers, compatible-count layers, `q,c,rho`, total excess `E` and exterior demand/slack;
2. test whether strict exterior slack expansion eliminates or sharply stratifies those 812 when expressed only in layer statistics;
3. identify the smallest correlation statistic still needed after exterior expansion;
4. prove a Murty-specific bound on that statistic from `q+rho<=a`, residual budgets, incoming caps, total-excess caps and the bridge;
5. substitute that bound into the exact whole-staircase Hall inequality.

The aim is a symbolic all-order contradiction, not another fixed-order-only screen.

---

## 7. Immediate operational priorities

1. **Build and run the fresh cross-implementation audit of the recovered 3,607-state relational scan.** This is the only route to safely reducing the promoted frontier from 3,607.
2. **Classify the 812 layered-receiver false negatives**, preserving the complete diagnostic table and all failed proposed summaries.
3. **Exploit strict exterior slack expansion** against the Murty receiver/residual budgets; start with the whole-exterior inequality, then sharpen to selected exterior subsets if needed.
4. **Develop the all-order whole-staircase inequality** by restoring only the minimal target-correlation statistic needed beyond the layered receiver bound.
5. **Red-team each universal lemma independently** and keep external-review status separate from internal finite verification.

Operationally, priorities 1 and 2 can run independently; priority 3 is the main hand-proof/general-theory line.

---

## 8. Standing synchronization order

`CURRENT_STATE.md` is the mandatory restart surface.

Synchronize it whenever:

- a canonical frontier/ledger count changes;
- discovery or recovery completes;
- a theorem/corollary enters or leaves the internally audited chain;
- an audit gate completes or fails;
- a material pilot changes research direction;
- the principal attack changes;
- work pauses after a material research block.

Every sync must distinguish discovery, internal finite verification, same-assistant audit, independent implementation, external mathematical review and external reproduction.

Before restart: confirm `CANONICAL_REPOSITORY.md`, read this file, inspect commits newer than the synchronization point, reconcile material changes, then continue.

---

## 9. External-status boundary

Nothing above is external acceptance of the unrestricted Murty–Simon conjecture.

- fixed-order results remain candidate proofs with external review open;
- bridge/Hall structural results have strong internal proofs and finite audits, but external mathematical review and novelty assessment remain open;
- the recovered 3,607-state relational scan is not a canonical frontier reduction until the fresh cross-implementation audit and separate promotion gate pass;
- genuinely independent third-party computational reproduction remains open.
