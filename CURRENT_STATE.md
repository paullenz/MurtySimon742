# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart surface after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth.

## Canonical repository

- repository: `paullenz/MurtySimon742`
- GitHub repository ID: `1359206057`
- identity guard: [`CANONICAL_REPOSITORY.md`](CANONICAL_REPOSITORY.md)
- legacy names such as `MurtySimon25` and historical `N25_*` filenames are not the current repository name.

**State synchronized:** 14 September 2026 through commit `c0bacae1252f6a80821e9c3aab4ab1a0a4526630` (`Relaunch final relational candidate audit after output fix`), including the completed 812 receiver-layer diagnostic, coupled residual-slack theory, positive-slack incidence pressure, and the internally audited exterior residual-upset reduction.

Previous versions remain preserved in Git history. This file is intentionally concise and must be updated whenever theorem status, frontier status, audit status or principal research priority changes.

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

The long-budget recovery of unresolved/unattempted discovery states also completed successfully:

```text
workflow run: 34844403328
status:       completed / success
```

The recovered aggregate contains **2,655 candidate relational exclusions**. These are **not promoted**. The recovered results are hash-pinned at

```text
sha256:2c892301854660c8c1f73a13c4949ce2fb7e1e5706f9ecffbbe79f9483e71970
```

The first final-candidate cross-audit launch (`34849859218`) failed before mathematical auditing because a pretty-printed JSON object was accidentally appended to `$GITHUB_OUTPUT`; GitHub Actions rejected the `{` as an invalid output line. Before that formatting failure the workflow had successfully downloaded the recovered aggregate and passed the source-completeness, source-hash, 2,655-candidate-count and candidate-input-coverage checks. This failure is plumbing, not evidence of mathematical disagreement.

The output-channel bug was repaired and the hash-pinned audit has now been explicitly relaunched:

```text
commit:       c0bacae1252f6a80821e9c3aab4ab1a0a4526630
workflow run: 34854911792
status at sync: queued
candidate set: 2,655
shards:        256
```

Each shard compiles and runs two independently structured implementations, `scan_post_pair_relational.cpp` and `scan_post_pair_relational_types.cpp`, and promotion is blocked unless all 2,655 states receive exact cross-implementation agreement with zero unresolved states.

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
8. ordered by cross degree, those generators form a moving staircase with strictly increasing `c`, weakly increasing `q`, and increasing `P` on equal-`q` plateaux;
9. the compatible-copy all-bands staircase cut reproduces the exact Hall margin of `M+`.

In the Murty source universe `c=q+rho<=a`, so there is at most one primary staircase generator breakpoint per integer cross-degree level and `h<=a+1`.

### Exact compatible-copy representation

The coarse band relaxation detected `205,918/205,919` target-Hall failures in the frozen 15-state pilot. The unique miss, state 226, exposed the compatible-copy correction. The compatible-copy theorem passed independent finite verification, and the canonical all-bands exactness theorem then showed that for `M+` this representation is exact, not merely near-exact.

Fresh pilot replay:

```text
profiles tested:          201,493,148
target-Hall failures:         205,919
compatible-copy detects:      205,919
compatible-copy misses:             0
```

---

## 5. Exterior residual-slack system — second staircase

For primary canonical witness `M+`, let

```text
y_w = number of M+-sources directed-compatible with target w,
s_w = (P_w-y_w)_+.
```

The strict exterior slack-expansion theorem says that every nonempty exterior source set `T` must satisfy

```text
sum_w min(s_w,K_T(w)) >= D(T)+1.
```

Thus a hypothetical deficient primary staircase is accompanied by a **strictly expanding residual receiver system** outside it.

### Exterior sharp-upset reduction — internally audited

The residual system no longer requires arbitrary exterior-subset search. Under the residual-cap sharp order

```text
x >=_s y
iff c_x<=c_y
    and [q_x>q_y or (q_x=q_y and s_x>=s_y)],
```

if any nonempty exterior set has residual margin `<=0`, then some nonempty residual sharp up-set does. The finite audit is green:

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

This gives the current structural picture:

```text
primary P-staircase M+        must be deficient in a counterexample,
exterior residual-s staircase must remain strictly expanding.
```

The general-theory target is to prove these two staircase requirements cannot coexist under Murty residual/source-cap budgets.

---

## 6. 812 receiver-layer exceptions — completed diagnostic

The one-dimensional receiver-layer rearrangement detects `205,107/205,919` exact target-Hall failures, leaving 812 correlation-sensitive failures. The detailed diagnostic has now completed successfully on the same deterministic 15-state sample.

### Concentration

All **812** exceptions occur in only **8** sample states:

```text
state 1626:  61
state 2439:  90
state 2984:   5
state 5519: 249
state 6085:  14
state 7610: 262
state 8179: 116
state  429:  15
```

### Canonical generator count

```text
2 generators: 140
3 generators: 499
4 generators:  98
5 generators:  75
1 or >=6:       0
```

So the correlation-sensitive cases are not high-complexity antichains; 3 generators dominate and the maximum is 5.

### Exact Hall deficiency

```text
deficit 1: 687
deficit 2: 116
deficit 3:   9
deficit >=4: 0
```

The maximum exact deficiency is only 3.

### Rearrangement excess

```text
excess 0: 537
excess 1: 133
excess 2:  94
excess 3:  40
excess 4:   5
excess 5:   3
```

The lost target-correlation gap is at most 7. There are only **169 distinct q-profiles** among the 812 exceptions.

This is a strong narrowing result: the missing correlation is bounded and low-dimensional rather than an arbitrary Hall phenomenon.

---

## 7. New Murty-specific correlation inequalities

The 812 diagnostic has already produced useful symbolic structure.

### Coupled primary-incoming / residual-slack budget

For slack layer

```text
S_j={w:s_w>=j},
sigma_j=|S_j|,
Y_j=sum_{w in S_j} y_w,
```

positive-surplus residual activity and the Murty target cap imply

```text
sum_{w in S_j} max(0,y_w+a-b+j) <= r-b.      (7.1)
```

When `a-b+j>=0`, this becomes

```text
Y_j+(a-b+j)sigma_j <= r-b.                   (7.2)
```

Near balance this is especially sharp:

```text
b=a+1:  Y_1 <= r-b,
         Y_j+(j-1)sigma_j <= r-b  for j>=2;

b=a:    Y_j+j sigma_j <= r-b.
```

Interpretation: a target cannot both receive many primary staircase incidences and retain much residual slack without consuming residual degree budget.

### Positive-slack incidence pressure

Let `Z={w:s_w>=1}` and `O=B\M+`. Labelled singleton exterior expansion gives

```text
D(O)+|O| <= e_D(O,Z),
```

and hence

```text
D(O)+|O|+Y_1 <= sum_{w in Z} d_D^-(w).        (7.3)
```

Using the exact directed compatibility rectangle

```text
q_u<=c_w+1,
c_u>=q_w,
```

the incoming term has an exact two-dimensional count. Therefore the same positive-slack targets must simultaneously supply exterior incidence capacity, absorb primary incoming multiplicity, and fit inside the residual-excess budget (7.1).

This is currently the cheapest promising route to a symbolic contradiction.

---

## 8. Preserved negative results / routes not to repeat

- no universal one-dimensional Ferrers ordering of individual sources;
- one principal sharp up-set is not sufficient in general;
- no universal two-generator bound: primary failures reach eight generators in the broader pilot;
- interval-neighborhood bands do not make contiguous band cuts sufficient;
- receiver-layer rearrangement is not exact: 812 frozen-pilot false negatives remain;
- the whole-exterior scalar slack total alone is too coarse/redundant; the useful information is layered and correlation-sensitive;
- survival of a relaxation never implies graph realizability.

Failures, rejected lemmas, bugs, counterexamples and audit challenges must remain preserved.

---

## 9. Current mathematical priority

The research priority has shifted from searching arbitrary Hall cuts to proving a **two-staircase incompatibility theorem**.

Current route:

```text
hypothetical counterexample
 -> deficient canonical primary P-staircase M+
 -> exact compatible-copy whole-staircase deficit
 -> residual slack s_w left by that primary staircase
 -> strictly expanding exterior residual-s staircase
 -> coupled residual budget + incidence-pressure inequalities
 -> contradiction sought from Murty bridge constraints.
```

Immediate analytic tasks:

1. apply (7.1)–(7.3) explicitly to the 812 diagnostic profiles and measure how many are already impossible;
2. stratify any residue by the exact two-dimensional compatibility rectangle, not by arbitrary Hall subsets;
3. derive the smallest additional inequality required for the residual-s staircase;
4. generalize that inequality in `a,b,r,t` rather than fitting fixed N;
5. independently red-team every universal implication before promoting it into the audited chain.

The desired endpoint is an all-order hand/structural inequality showing that the deficient primary staircase and required exterior residual staircase cannot coexist.

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

Nothing above is external acceptance of the unrestricted Murty–Simon conjecture. Fixed-order proofs remain candidate proofs with external review open; the bridge and new Hall/staircase theory have increasingly strong internal derivations and finite audits but external mathematical review and novelty assessment remain open; the 2,655 relational candidates remain unpromoted until the final cross-audit and separate promotion gate pass.
