# Minimum-cut exactness of stratified rearrangements in two-sided nested Hall systems

**Status:** working paper. The central result is an internal candidate theorem; external mathematical review and dedicated novelty review remain open. The theorem is now stated independently of the Murty–Simon/D2C application.

## Abstract — provisional

We study a finite directed capacitated Hall system whose objects are simultaneously sources and receivers. Sources are partitioned into equal-demand layers and receivers have integer capacities. Within a layer we assume only a two-sided crossing-dominance property: whenever one receiver has strictly smaller capacity than another, the higher-capacity object dominates the lower one in both incoming and outgoing compatibility, apart from the deleted diagonal, and the two objects are mutually compatible.

For a source set `S`, let `H(S)` be its exact capped receiver capacity and `D(S)` its total demand. Layerwise rearrangement of the receiver capacities and multiplicities gives an upper bound `U(S)>=H(S)`, but this bound can be strict even at a minimum Hall witness. We prove that it is nevertheless exact after minimisation:

`min_S (H(S)-D(S)) = min_S (U(S)-D(S))`.

The proof combines submodularity of the Hall margin with a neutral-deletion operation. Every positive rearrangement crossing has a forced membership orientation; deleting its selected high-capacity endpoint preserves the minimum margin. Iterating produces a crossing-free minimum witness. The original q-stratified target-Hall theorem from the D2C programme becomes a corollary because its numerical compatibility relation implies the abstract two-sided dominance axioms.

## 1. Main phenomenon

The key distinction is:

- **pointwise rearrangement exactness:** `U(S)=H(S)` for every `S` — false;
- **minimum-margin exactness:** `min(U-D)=min(H-D)` — the candidate theorem proved here.

The final paper should include the smallest hostile example exhibiting pointwise failure.

## 2. Abstract model and theorem

Use the model and notation of [`ABSTRACT_CROSSING_DOMINANCE.md`](ABSTRACT_CROSSING_DOMINANCE.md): a finite set `V`, demand layers `L_i`, common integer demand `d_i` in each layer, receiver capacities `P_w`, and a loopless compatibility relation `R`.

The load-bearing hypothesis is **two-sided crossing dominance (TCD)**. For equal-layer `x,y` with `P_x<P_y`:

1. `x R y` and `y R x`;
2. for every third `z`, `z R x => z R y`;
3. for every third `z`, `x R z => y R z`.

Define exact capacity `H(S)`, demand `D(S)`, margin `F(S)=H(S)-D(S)`, and the layerwise rearranged upper bound `U(S)`.

> **Main theorem (internal candidate).** Every finite layered directed Hall system satisfying TCD obeys
>
> `min_S [U(S)-D(S)] = min_S [H(S)-D(S)]`.

Consequently exact Hall failure exists iff rearranged-layer Hall failure exists.

## 3. Crossing orientation

The layer-cake formula writes `H` as intersections of capacity-threshold and multiplicity-threshold sets. Strict rearrangement gap therefore supplies a same-layer pair with

`P_x<m<=P_y`, `y_x(S)>=m>y_y(S)`.

TCD incoming nesting and the missing diagonal imply that this inversion is only possible when

`x notin S`, `y in S`,

and then necessarily

`y_x(S)=y_y(S)+1`.

Thus the high-capacity selected endpoint `y` has receiver slack.

## 4. Submodularity and neutral deletion

`F` is submodular, so its minimisers form a lattice. Let `M+` be the unique maximal minimiser. If `x notin M+`, adding `x` to any minimum witness raises the integral margin by at least one.

For a crossing `(x,y)` with `x notin M+`, addition of `x` therefore opens at least `d+1` unsaturated receiver slots, where `d` is the common layer demand. Minimality of the witness says deletion of `y` can destroy at most `d` active receiver slots. TCD outgoing nesting maps all but the crossing target `y` from the first set into the second. The counts are forced equal and deletion of `y` is neutral.

## 5. Crossing-removal theorem

Start at `M+` and repeatedly delete the selected high endpoint of a crossing. A vertex deleted as a high endpoint has receiver multiplicity strictly below its capacity and multiplicities only decrease thereafter, so it can never later become a low-capacity/high-multiplicity endpoint. Hence every later low endpoint lies outside the original `M+`, allowing neutral deletion again.

The process terminates at a minimum witness `S*` with `U(S*)=H(S*)`. The main theorem follows immediately from the pointwise inequality `U>=H`.

## 6. Original q/c target-Hall system as a corollary

In the original application each copy has `q_w`, `c_w>=q_w`, capacity `P_w`, and

`u R w iff u!=w, q_u<=c_w+1, q_w<=c_u`.

Within a fixed q-layer, `c_x<=c_y => P_x<=P_y`. Hence `P_x<P_y` forces `c_x<c_y`. The compatibility inequalities then give mutual compatibility and both incoming and outgoing nesting away from the diagonal. Thus TCD holds.

This is a useful conceptual simplification: q/c arithmetic supplies the abstract dominance structure but is not itself needed by the minimum-cut proof.

## 7. Verification

[`verify_crossing_dominance.py`](verify_crossing_dominance.py) tests the abstract theorem directly. The frozen record [`CROSSING_DOMINANCE_VERIFICATION.json`](CROSSING_DOMINANCE_VERIFICATION.json) contains two exhaustive four-vertex regimes, including 211,716 demand instances in total and tens of thousands of instances/source sets where pointwise exactness fails. It records zero minimum-margin mismatches.

The finite verification is regression evidence, not proof.

## 8. Algorithmic and structural questions

Before submission, investigate without presupposing positive answers:

- whether TCD is best described as a known threshold/Ferrers subclass or a simple diagonal deletion/completion of one;
- whether the crossing-removal process yields a useful canonical minimum witness algorithm once a minimiser is known;
- whether TCD can be weakened to one-sided conditions plus an explicit crossing-orientation axiom;
- weighted/real-capacity variants;
- multiple or partially ordered stratification parameters.

## 9. Application back to D2C

Keep this section short. State which canonical bridge facts imply the q/c target-Hall model and therefore TCD. The application motivates the theorem but is not part of its proof.

## 10. Literature and novelty obligations

The closest structural literature currently appears to involve Ferrers/chain graphs, threshold digraphs, Hall deficiency, submodular minimiser lattices, and Monge/comonotone flow. In particular, Marmulla and Brandes (2026), *On Relations between Neighborhoods of Threshold and Ferrers Digraphs*, studies precisely how deleting loops from Ferrers digraphs alters literal neighbourhood nesting (DOI 10.7155/jgaa.v30i1.3099). That comparison should be made explicitly before choosing final terminology.

No search so far establishes novelty of the minimum-margin theorem. The final contribution statement must be narrowed if an equivalent result is found.

## 11. Trust boundary

The theorem has a hand proof and substantial standalone exhaustive regression, but it has not been independently proved or externally reviewed. Do not describe it as new, published, or accepted until the relevant checks are complete.
