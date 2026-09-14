# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart surface after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth.

## Canonical repository

- repository: `paullenz/MurtySimon742`
- GitHub repository ID: `1359206057`
- identity guard: [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md)
- legacy names such as `MurtySimon25` and historical `N25_*` filenames are not the current repository name.

**State synchronized:** 14 September 2026 through parent commit `3321d8ce18b77b78f421166ca55abc82f493b923` (`Freeze q-stratified crossing-gap audit`), including the frozen 812 q-stratified diagnosis, exact q-crossing identity, coupled residual-slack theory, positive-slack incidence pressure, and the audited exterior residual-upset reduction.

Previous versions remain preserved in Git history. This file must be updated whenever theorem status, frontier status, audit status or principal research priority changes.

---

## 1. Canonical promoted frontier — unchanged

```text
quantified whole-state closures: 977
canonical exclusions:           1,971
canonical survivors:            3,607
  N34-derived:                  3,529
  N35-derived:                     78
```

The closure ledger remains protected by `tools/check_n34_whole_state_ledger.py`. Of the 977 closures, 943 N34-derived states come from the cross-implemented potential-pair family; earlier closures remain separately preserved.

**Do not change the 3,607 headline from discovery/recovery output alone.** Promotion requires the dedicated cross-implementation audit and then a separate ledger-promotion step.

### Relational full-frontier audit status

The full layer/state-safe discovery scan of the 3,607 canonical survivors completed successfully:

```text
workflow run: 34820187136
status:       completed / success
```

Long-budget recovery also completed successfully:

```text
workflow run: 34844403328
status:       completed / success
```

The recovered aggregate contains **2,655 candidate relational exclusions**, hash-pinned at

```text
sha256:2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970
```

These are **not promoted**.

The first final-candidate cross-audit launch (`34849859218`) failed before mathematical auditing because a pretty-printed JSON object was accidentally appended to `$GITHUB_OUTPUT`. Source-completeness, source-hash, 2,655-candidate-count and candidate-input-coverage checks had already passed. This was a workflow-output bug, not mathematical disagreement.

The bug was repaired and the identical hash-pinned audit relaunched:

```text
workflow run: 34854911792
candidate set: 2,655
shards:        256
plan job:      success
shard status at this sync: queued / no promotion yet
```

Each shard runs two independently structured implementations, `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`. Promotion remains blocked unless all 2,655 states receive exact agreement with zero unresolved states.

Required chain:

```text
checkpointed discovery                COMPLETE
 -> layer-safe aggregate              COMPLETE
 -> long-budget recovery              COMPLETE
 -> final 2,655-state cross-audit     QUEUED/RUNNING; NOT YET PASS
 -> separate ledger promotion         OPEN
```

N34 and N35 provenance must remain separate throughout.

---

## 2. Fixed-order candidate results

Preserved candidate proofs remain:

- `n=25`: `e(G)<=156`, equality `K(12,13)`; external specialist review open.
- `n=27`: `e(G)<=182`, equality `K(13,14)`; external review open.
- `n=28`: `e(G)<=196`, equality `K(14,14)`; external review open.
- `n=29`: `e(G)<=210`, equality `K(14,15)`; difficult `Delta=16` branch hand-closed; external review open.
- `n=30`: `e(G)<=225`, equality `K(15,15)`; external review open.
- `n=31`: `e(G)<=240`, equality `K(15,16)`; external review open.
- `n=32`: `e(G)<=256`, equality `K(16,16)`; external review open.
- `n=33`: `e(G)<=272`, equality `K(16,17)`; external review open.
- `n=34`: `e(G)<=289`, equality `K(17,17)`; external review open.
- `n=35`: `e(G)<=306`, equality `K(17,18)`; external review open.

These fixed-order candidate proofs are separate from the 3,607-state general-theory frontier.

---

## 3. Canonical graph-to-constraint bridge

Canonical framework:

`project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`

Core notation:

```text
a = n-1-Delta,
b = Delta,
t = e(G)-b(a+1).
```

The bridge supplies the selected/residual ledger, demand inequalities, selected-edge forcing, endpoint load, residual activity for positive surplus, charging, threshold capacity, isolated-C exclusion and residual h-index consequences. Downstream Hall and finite arguments remain conditional on this bridge.

Highest-value external red-team targets remain the quasi-edge selection/injection and forcing portions, especially Sections 2–3, 6 and 8–12. External mathematical acceptance remains open.

---

## 4. Primary canonical Hall staircase — internally audited chain

Current package:

`project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`

Internally audited results include:

1. complete `(q,c,P)` type classes suffice for a minimum target-Hall cut;
2. labelled target flow is represented exactly by the quotient type network;
3. the Hall margin is submodular;
4. sharp-hardness dominance constrains minimum witnesses;
5. minimum-margin witnesses form a lattice;
6. their union `M+` is the unique maximal minimizer and a sharp-hardness up-set;
7. `M+` has a unique minimal-generator antichain;
8. its ordered generators form a moving staircase with strictly increasing `c`, weakly increasing `q`, and increasing `P` on equal-`q` plateaux;
9. the compatible-copy all-bands staircase cut reproduces the exact Hall margin of `M+`.

In the Murty source universe `c=q+rho<=a`, so there is at most one primary staircase generator breakpoint per integer cross-degree level and `h<=a+1`.

### Exact compatible-copy representation

Frozen 15-state pilot:

```text
profiles tested:          201,493,148
target-Hall failures:         205,919
compatible-copy detects:      205,919
compatible-copy misses:             0
```

Thus canonical target-Hall failure has an exact whole-staircase representation.

---

## 5. Exterior residual-slack system — second staircase

For primary canonical witness `M+`, let

```text
y_w = number of M+-sources directed-compatible with target w,
s_w = (P_w-y_w)_+.
```

Every nonempty exterior source set `T` must satisfy

```text
sum_w min(s_w,K_T(w)) >= D(T)+1.
```

Under the residual-cap sharp order

```text
x >=_s y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and s_x>=s_y)],
```

it suffices to test nonempty residual sharp up-sets. The independent finite audit is green:

```text
workflow run:                           34851263359
canonical profiles checked:                  2,314
profiles with nonempty exterior:             1,263
canonical exterior subsets checked:         32,245
minimum canonical exterior margin:               1
residual violation profiles checked:         1,787
random trials:                               1,600
result:                                    success
```

Current structural picture:

```text
primary P-staircase M+        deficient in a counterexample,
exterior residual-s staircase required to remain strictly expanding.
```

---

## 6. Receiver-layer correlation problem — q-stratification breakthrough

The global one-dimensional receiver-layer rearrangement detects

```text
205,107 / 205,919
```

exact target-Hall failures, leaving 812 false negatives.

### 6.1 Frozen 812 diagnosis

The complete 812-row diagnostic artifact is frozen and hash-pinned. Rearranging receiver layers **separately inside each q-stratum** eliminates the entire residue:

```text
812 global-layer false negatives examined
812 q-stratified detections
812 q-stratified upper bounds equal exact receiver capacity
0   positive q-stratified gaps
```

On these 812 canonical maximal witnesses:

```text
profiles with mixed selected/unselected status inside one q-level: 0
```

Selected q-levels form a threshold. First selected q:

```text
q*=3 : 349
q*=4 : 242
q*=5 : 173
q*=6 :  48
```

Gap from largest unselected q to smallest selected q:

```text
1 : 340
2 : 415
3 :  56
4 :   1
```

This is strong frozen-pilot evidence, **not a universal theorem**.

### 6.2 Exact q-crossing identity — internally audited

For arbitrary labelled Hall source set `S`, let `U_q(S)` be the q-only comonotone receiver-layer upper bound and `H(S)` the exact receiver capacity. The exact lost correlation is

```text
C_q(S)=sum_{q,m} min(H^S_{q,m},L^O_{q,m}),
```

where the terms count selected high-capacity and unselected low-capacity targets crossing inside equal-`(q,m)` preincoming blocks.

The audited identity is

```text
U_q(S)-H(S)=C_q(S).
```

Independent verifier:

```text
workflow run:                         34858775228
exhaustive cases:                       384,612
exhaustive positive-gap cases:           60,301
exhaustive maximum gap:                       2
nontrivial crossing blocks:             606,568
random trials:                            20,000
random positive-gap cases:                 4,142
random maximum gap:                            5
result:                                     PASS
```

The many positive-gap hostile examples are important: `C_q=0` is **not** an abstract Hall theorem. A concrete canonical Hall counterexample with `C_q=1` is preserved in `Q_STRATIFIED_EXACTNESS_COUNTEREXAMPLE.md`.

Therefore the Murty-specific target is now exact and narrow:

```text
control or exclude C_q>0
```

for canonical maximal witnesses arising from the Murty bridge.

### 6.3 Full frozen-pilot q-crossing replay

A fresh run over the same 201,493,148-profile frozen pilot has been launched to measure q-stratified reach and `C_q` across **all** 205,919 target-Hall failures:

```text
workflow run: 34859094097
status at this sync: queued
```

Do not promote the 812 observation to full-pilot exactness until this run completes successfully.

---

## 7. Murty-specific residual/slack inequalities — useful but not decisive on the 812

### Coupled primary-incoming / residual-slack budget

For

```text
S_j={w:s_w>=j},
sigma_j=|S_j|,
Y_j=sum_{w in S_j} y_w,
```

positive-surplus residual activity gives

```text
sum_{w in S_j} max(0,y_w+a-b+j) <= r-b.
```

When `a-b+j>=0`:

```text
Y_j+(a-b+j)sigma_j <= r-b.
```

### Positive-slack incidence pressure

With `Z={w:s_w>=1}` and `O=B\M+`:

```text
D(O)+|O|+Y_1 <= sum_{w in Z} d_D^-(w).
```

The incoming term is an exact two-dimensional `(q,c)` rectangle count.

### Exact evaluation on all 812

These newer scalar consequences have now been tested against the entire frozen 812 residue:

```text
coupled residual-slack budget: minimum remaining slack 17
positive-slack incidence pressure: minimum slack 1
whole-exterior residual expansion: minimum slack 2
profiles excluded by these scalar tests alone: 0
```

So the 812 are **not** hiding a violation of the current scalar slack budgets. The decisive missing information is q-level correlation.

---

## 8. Preserved negative results / routes not to repeat

- no universal one-dimensional Ferrers ordering of individual sources;
- one principal sharp up-set is not sufficient in general;
- no universal two-generator bound: primary failures reach eight generators in the broader pilot;
- interval-neighborhood bands do not make contiguous band cuts sufficient;
- global receiver-layer rearrangement is not exact: 812 frozen-pilot false negatives exist;
- q-only exactness is not an abstract Hall theorem: positive `C_q` examples are preserved;
- the whole-exterior scalar slack total alone is too coarse;
- the current coupled slack and incidence-pressure inequalities do not by themselves eliminate the 812;
- survival of a relaxation never implies graph realizability.

Failures, rejected lemmas, bugs, counterexamples and audit challenges must remain preserved.

---

## 9. Current mathematical priority

The target-correlation problem has narrowed from arbitrary target matching to one explicit crossing statistic.

Current route:

```text
hypothetical counterexample
 -> deficient canonical primary P-staircase M+
 -> exact whole-staircase Hall deficit
 -> q-stratified receiver layers
 -> exact error term C_q
 -> show Murty-specific canonical structure forces C_q=0
    or bounds C_q below the available Hall deficit
 -> contradiction.
```

In parallel:

```text
primary staircase M+
 -> residual slack s_w
 -> strictly expanding exterior residual-s staircase
 -> coupled residual/source-cap budgets.
```

The first structural consequence of a positive q-crossing is the equal-q swap saturation wall recorded in `CANONICAL_EQUAL_Q_SWAP_RIGIDITY.md`: a crossing forces the selected higher-`c` endpoint to be under-saturated while every receiver gained by that higher-`c` source over the lower-`c` unselected endpoint is strictly over-saturated.

Immediate analytic priorities:

1. complete the frozen full-pilot q-crossing replay and record whether any of the 205,919 failures have `C_q>0`;
2. attack `C_q>0` symbolically via equal-q swap rigidity, residual/excess budget, source-cap and canonical maximality;
3. derive a Murty-specific upper bound on total crossing mass `C_q` in terms of `a,b,r,t`;
4. combine that bound with the exact q-stratified layer inequality and primary Hall deficit;
5. independently red-team every universal implication before promotion;
6. in parallel, complete the 2,655-state independent relational audit before changing the 3,607 frontier.

The desired endpoint remains an all-order hand/structural contradiction, but the remaining target-level correlation is now an explicit low-dimensional quantity rather than a general max-flow problem.

---

## 10. Standing synchronization / trust boundary

`CURRENT_STATE.md` is the mandatory restart surface. Synchronize it whenever a frontier count changes, an audit completes/fails, a theorem enters/leaves the audited chain, a material pilot changes direction, or work pauses after a material block.

Every sync must distinguish:

- discovery/reconnaissance;
- internal proof derivation;
- finite verification;
- independently structured implementation audit;
- external mathematical review;
- genuinely independent third-party computational reproduction.

Nothing above is external acceptance of the unrestricted Murty–Simon conjecture. Fixed-order proofs remain candidate proofs with external review open; the bridge and Hall/staircase/q-crossing theory have strong internal derivations and finite audits but external mathematical review and novelty assessment remain open; the 2,655 relational candidates remain unpromoted until the final cross-audit and separate promotion gate pass.