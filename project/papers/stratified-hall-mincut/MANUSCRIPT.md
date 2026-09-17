# Minimum-cut exactness of stratified rearrangements in monotone directed Hall systems

**Status:** working paper skeleton. The central theorem is an internal candidate theorem already preserved in the research ledger; external mathematical review and a dedicated novelty search remain open. This manuscript deliberately abstracts away from Murty–Simon/D2C notation.

## Abstract — provisional

We consider a directed capacitated Hall system in which every labelled object is simultaneously a source and a potential receiver. Sources carry a nonnegative integer demand `q_u`; receivers carry a capacity `P_w`; and admissibility is controlled by a pair of monotone source/receiver parameters. For a source set `S`, let `H(S)` denote its exact capped receiver capacity and `D(S)` its total demand. Sorting receivers only by the demand layer `q` gives a comonotone rearrangement upper bound `U_q(S) >= H(S)`. This bound need not be exact for a fixed `S`, even when `S` is the maximal minimum Hall witness. We prove, under fixed-`q` capacity monotonicity, that the rearrangement is nevertheless exact after minimisation:

`min_S (H(S)-D(S)) = min_S (U_q(S)-D(S))`.

The proof uses submodularity of the Hall margin, the lattice of its minimisers, and a neutral-deletion operation that removes every positive within-layer crossing without changing the minimum margin. Consequently every instance has a crossing-free minimum witness, and q-stratification detects Hall failure exactly after minimisation. The result arose from a structured graph-extremal problem but is stated independently of that application.

## 1. Introduction

### 1.1 Problem

Hall-type feasibility problems often admit useful rearrangement bounds after vertices are stratified by one monotone parameter. A natural difficulty is that a rearranged or comonotone capacity can overestimate the capacity available to a particular source set. The question addressed here is whether such a relaxation may nevertheless be exact at the minimum cut.

### 1.2 Main phenomenon

There are two statements which must be kept distinct:

- **pointwise exactness:** `U_q(S)=H(S)` for every `S` — false;
- **minimum-cut exactness:** `min(U_q-D)=min(H-D)` — candidate theorem proved by the crossing-removal argument below.

The hostile five-copy example from the research ledger should appear early: it demonstrates that the stronger pointwise/maximal-witness statement is genuinely false and motivates the exact theorem.

### 1.3 Contributions

Provisional contributions, subject to novelty clearance:

1. an exact crossing-gap representation `U_q(S)-H(S)=C_q(S)`;
2. a neutral-deletion lemma for equal-`q` crossing pairs;
3. a terminating crossing-removal algorithm on the lattice of minimum Hall witnesses;
4. minimum-cut exactness of q-stratification;
5. a constructive certificate: if exact Hall fails, a crossing-free failing minimum witness exists.

## 2. Abstract model

For each labelled copy `w`, let

`q_w >= 0`, `c_w >= q_w`, and receiver capacity `P_w >= 0`.

Assume fixed-`q` capacity monotonicity:

`q_x=q_y` and `c_x<=c_y` imply `P_x<=P_y`.

Define directed compatibility by

`D(u,w)` iff `u!=w`, `q_u<=c_w+1`, and `q_w<=c_u`.

For a source set `S`, put

`y_w(S)=#{u in S : D(u,w)}`,

`H(S)=sum_w min(P_w,y_w(S))`,

`D(S)=sum_{u in S} q_u`,

`F(S)=H(S)-D(S)`.

The q-only comonotone receiver upper bound is denoted `U_q(S)`; its layer-cake definition should be given explicitly before the first theorem.

## 3. Crossing gap

Define the q-crossing statistic `C_q(S)` by the within-layer inversions between selected high-capacity receiver copies and unselected low-capacity copies at each multiplicity level. Establish the audited identity

`U_q(S)-H(S)=C_q(S) >= 0`.

This section should be written independently from the Murty notation and should include the smallest counterexample to pointwise exactness.

## 4. Submodularity and minimum-witness lattice

Prove that `F` is submodular. Therefore the family of minimisers is closed under union and intersection. Let

`delta=min_S F(S)`

and let `M+` be the unique maximal minimiser.

The only facts needed later are:

- every minimum witness lies inside `M+`;
- if `x notin M+`, then `x` lies in no minimum witness;
- integrality gives `F(S union {x}) >= delta+1` for a minimum witness `S` and `x notin M+`.

## 5. Neutral deletion lemma

Let `S` be a minimum witness contained in `M+`. Suppose distinct `x,y` satisfy

`x notin M+`, `y in S`, `q_x=q_y`, `c_x<c_y`,

and the selected target `y` has receiver slack `y_y(S)<P_y`.

Then

`F(S\{y})=F(S)=delta`.

Present the proof by comparing the marginal change caused by adding `x` and deleting `y`, using the source-neighbourhood containment forced by `c_x<c_y` within the same q-layer.

## 6. Crossing-removal theorem

Show that every positive crossing in a minimum witness supplies an endpoint satisfying the neutral-deletion lemma. Start from `M+` and repeatedly delete a selected high endpoint of a crossing.

The key invariant is that a previously deleted vertex cannot later become a low unselected crossing endpoint because receiver multiplicities only decrease. Hence every newly encountered low endpoint was outside the original `M+`.

The algorithm terminates at a minimum witness `S*` with

`C_q(S*)=0`.

## 7. Main theorem

> **Theorem (q-stratified minimum-cut exactness; internal candidate).** Under the hypotheses of Section 2,
>
> `min_S [U_q(S)-D(S)] = min_S [H(S)-D(S)]`.
>
> Consequently, exact Hall failure exists if and only if q-stratified Hall failure exists.

Proof: pointwise `U_q>=H` gives one inequality; Section 6 supplies a minimum exact-Hall witness on which equality holds.

## 8. Algorithmic and structural consequences

This section is intentionally open. Candidate directions to test before submission:

- whether the crossing-removal procedure yields a polynomial-time canonicalisation of minimum witnesses once an exact minimum witness is known;
- whether the model is naturally a Ferrers/Monge or polymatroidal flow special case;
- whether the theorem extends from the specific numerical compatibility relation to an axiomatic nested-neighbourhood condition;
- weighted/real-capacity variants;
- multiple stratification parameters.

No such extension should be claimed until proved.

## 9. Application back to the D2C/Murty bridge

Keep this short. Explain that the abstract system was extracted from the target-Hall relaxation used in the diameter-2-critical programme. State exactly which bridge hypotheses imply the abstract assumptions. Do not use the application to justify the abstract theorem.

## 10. Verification

Retain the independent exhaustive/random verifier as regression evidence, not proof. The current research record reports exhaustive testing of small labelled profiles, random larger profiles, and a hostile positive-crossing example. Before submission, regenerate the record from a frozen standalone script in this paper directory.

## 11. Literature and novelty obligations

Before any novelty claim:

1. search matching/Hall literature for minimum-deficiency sets and lattices of minimisers;
2. search Ferrers bipartite graphs and nested-neighbourhood systems;
3. search Monge/comonotone transportation and capacitated matching;
4. search submodular minimum-cut uncrossing/deletion theorems;
5. compare the theorem after stripping all current notation to its weakest axiomatic form.

The paper should explicitly cite prior results that subsume any component and narrow the claimed contribution accordingly.

## 12. Current trust boundary

The main theorem is presently an internally derived hand theorem with extensive finite regression, not an externally reviewed result. The manuscript must not describe it as new until the novelty search is completed, nor as established literature until independently checked.
