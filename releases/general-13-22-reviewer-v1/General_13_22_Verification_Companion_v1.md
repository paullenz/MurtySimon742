---
title: "A layer-sum residual bound for diameter-2 edge-critical graphs - verification companion"
subtitle: "Reviewer edition 1 - replay, audit and provenance"
author: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"
date: "9 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
---

\begin{abstract}
This companion collects the principal replay instructions, audits, graph-to-model bridges and provenance documents supporting the reviewer manuscript. It is not a substitute for reading the mathematical proof. Exact arithmetic or certificate verification is identified as such in the underlying sources; same-assistant reconstructions are not represented as external independent review.
\end{abstract}

## Reviewer orientation

**Claim under review.** `n >= 6 and Delta(G) >= (13/22)n imply e(G) < floor(n^2/4)`.

**Status.** retained candidate hand proof; independent mathematical review OPEN.

**Sources assembled verbatim below:**

- `project/research/general_n/2026-09-08-layer-sum-v1/README.md`
- `project/research/general_n/2026-09-08-layer-sum-v1/CONSTRUCTION_AUDIT_2026-09-08.md`
- `project/research/general_n/2026-09-08-layer-sum-v1/LAYER_AGGREGATION_AUDIT_2026-09-08.md`
- `project/research/general_n/2026-09-08-layer-sum-v1/RED_TEAM_2026-09-08.md`
- `project/research/general_n/2026-09-08-layer-sum-v1/RECONCILIATION.md`

A failed or superseded route remains part of the repository history and is not silently promoted by inclusion in this companion. Reviewers should report suspected flaws through the repository's public review process.

---



\newpage

# Included source: `project/research/general_n/2026-09-08-layer-sum-v1/README.md`

# Layer-sum continuation — 8 September 2026

**Candidate hand proof; internal finite checks REPRODUCED; independent mathematical review OPEN.**

[Full mathematical derivation](PROOF.md). The current candidate implication is

    n>=6 and Delta(G)>=13n/22  ==>  e(G)<floor(n^2/4).

The coefficient 13/22 is 0.59090909..., compared with the previous continuation's 0.6129. This is a conditional all-order degree theorem, not a proof for every graph order without a degree restriction. K(2,3) prevents extending this strict statement to all n>=4.

The main inequalities, with a=n-1-Delta and t=m-Delta(n-Delta), are

    3 S^3 <= a^2 r(2r+1),
    t < 4a^2/81 + 1/8.

A strengthened intermediate form is now preferred. If H=max_i s_i and

    r_H=sum_{h=1}^H z_h=sum_u min(rho_u,H),

then

    3 S^3 <= a^2 r_H(2r_H+1),

and r_H<=r gives the displayed cubic bound. The proof has no large-a cutoff and does not depend on the old charging-deficit constants.

## Assurance status

The graph-to-quasi-edge bridge has a separate [construction audit](CONSTRUCTION_AUDIT_2026-09-08.md). A second implementation, independent of the layer-sum selected-system builder, exhaustively checked every labelled graph through six vertices, every minimum-degree root, every missing B-pair and every adjacent total-dominating pair created by insertion. Its clean GitHub run passed.

The local Lean slice in `../2026-09-07-stability-spare-sources-v9/formal/QuasiCore.lean` checks ten local lemmas in Lean 4.19.0, including four explicit edge-insertion-to-quasi-edge bridge lemmas. The first new Lean attempt exposed a proof-script equality-direction error; the corrected statement passed without changing the mathematical claim. This is deliberately preserved in the [assurance record](evidence/CONSTRUCTION_ASSURANCE_2026-09-08.json).

A further independent residual-injection checker is nonvacuous on larger deterministic critical-graph samples: 588 forced residual targets in 163 systems, while also exhaustively checking all selected systems through six vertices. The combined clean-runner workflow passed. This is internal assurance by the same assistant, not external reproduction or universal proof by enumeration.

The threshold source-supplement capacity step has its own [adversarial audit](THRESHOLD_CAPACITY_AUDIT_2026-09-08.md). The earlier “maximise an integer quadratic” wording has been replaced by the exact gap identity

    (q-j)(q-j-1)/2 >= 0,

and a separate abstract orientation checker passed on a clean runner after 1,191,446 marked cases plus 5,302,626 exact arithmetic triples. Both essential premises are also negative-controlled: allowing opposite orientations of one unordered pair or letting a high source spend outside Z_h breaks the bound.

The layer aggregation has now received an independent [aggregation audit](LAYER_AGGREGATION_AUDIT_2026-09-08.md). It proves the stronger truncated-mass form above and exhaustively tests the componentwise-minimal admissible residual tail for every sorted demand profile through a=11: 478,192 profiles and 4,215,632 threshold levels. The clean GitHub runner passed. These are abstract consequences of the threshold family, not graph-realisability claims.

The downstream cubic-to-surplus optimisation and exact degree conversion have a separate [surplus and degree audit](SURPLUS_AND_DEGREE_AUDIT_2026-09-08.md). A clean runner checked 2,666,600 scalar `(a,S)` cases and 5,107,274 degree-assembly cases through n=5000. The audit also identifies an infinite scalar family with `t/a^2=4/81`, proving that **4/81 is sharp if one uses only the cubic inequality and `S>=r+2t`**. Any asymptotic improvement below 13/22 therefore has to exploit stronger upstream structure rather than better one-variable optimisation.

The full 13/22 result remains a candidate hand proof. The global finite-cardinality reduction, threshold counting and layer aggregation are not fully formalised in Lean, and there is still no independent researcher reproduction.

## Replay

The core arithmetic and selected-system programs use only the Python standard library:

```sh
python3 -I -B src/check_threshold_capacity.py
python3 -I -B src/check_layers.py --output /absolute/path/to/new-layer-report.json
python3 -I -B src/check_construction_independent.py
python3 -I -B src/check_residual_injection_independent.py
python3 -I -B src/check_threshold_adversarial.py
python3 -I -B src/check_layer_aggregation_adversarial.py
python3 -I -B src/check_surplus_degree_adversarial.py
```

The `check_layers.py` output path must not already exist. `EVIDENCE.json` contains the original layer-sum run records and graph inputs/results; [RESULTS.md](RESULTS.md) summarises them. The newer construction/injection run IDs, hashes, counts and formal scope are in [evidence/CONSTRUCTION_ASSURANCE_2026-09-08.json](evidence/CONSTRUCTION_ASSURANCE_2026-09-08.json). The GitHub workflow `.github/workflows/layer-sum-construction.yml` now runs the independent construction, residual-injection, threshold-capacity, aggregation, surplus and degree-assembly audits together.

The original layer-sum run checks 1,059 selected systems, including all choices at all maximum-degree roots in the 608 critical labelled graphs found through six vertices. Only 12 of those systems have nonzero demand, and none has positive surplus. Abstract arithmetic tests and oriented-graph tests are not actual critical-graph counterexample searches. The newer injection sample makes the residual forcing mechanism itself nonvacuous, but still does not produce a positive-surplus graph.

## Research direction

The assurance bottleneck has moved upstream. The final scalar optimisation cannot improve the asymptotic coefficient: 4/81 is sharp at that level. The most promising next attacks are therefore to retain information discarded when the full threshold family is collapsed into one cubic inequality: equality/near-equality rigidity, the full `(W_h,z_h)` profile, truncated residual mass `r_H`, and simultaneous cross-level restrictions coming from one selected graph.

The previous turn's unattached weighted-spare-source v10 uploads are not treated as a published or checked checkpoint. They are distinct from the concurrent demand-tail v10 and Jensen-tail v11 checkpoints, which are preserved; see [RECONCILIATION.md](RECONCILIATION.md). The prior threshold note, frozen papers, original evidence and theorem ledger remain unchanged.


\newpage

# Included source: `project/research/general_n/2026-09-08-layer-sum-v1/CONSTRUCTION_AUDIT_2026-09-08.md`

# Independent audit of the graph-to-quasi-edge construction

8 September 2026. Internal assurance work by ChatGPT/Geeps. **Candidate proof status remains unchanged; independent specialist review remains OPEN.**

## Result

No defect was found in the complement edge-insertion construction used by the layer-sum proof. The argument was reconstructed from first principles, compared with the standard quasi-edge observation in the total-domination literature, checked by a second exhaustive implementation on a clean GitHub runner, and its local edge-insertion bridge was checked in Lean 4.19.0.

## 1. First-principles reconstruction

Let G be diameter-two edge-critical and H its complement. An adjacent pair xy totally dominates H exactly when xy is a nonedge of G and x,y have no common G-neighbour; equivalently their G-distance is greater than two. Since diam(G)=2, H contains no adjacent total-dominating pair.

Take a missing edge uw of H, i.e. an edge of G. Criticality says G-uw has diameter greater than two, so H+uw contains an adjacent total-dominating pair xy. Since H had none, adding uw must be essential to this pair. Therefore either xy={u,w}, or xy uses exactly one endpoint of the new edge and its other edge was already present in H. A pair avoiding both u and w would have unchanged adjacency and unchanged open-neighbourhood union and so would already totally dominate H, impossible.

Now choose v of minimum H-degree and put A=N_H(v), B=V(H)\N_H[v]. For a missing pair uw inside B, both u and w miss v. Thus {u,w} cannot totally dominate H+uw. Hence every newly created adjacent total-dominating pair has the form ui (or wi), where i is an old H-neighbour of the source. It must dominate v, so i belongs to A.

Suppose the pair is ui in H+uw. The only neighbourhood incidence added to ui's open-neighbourhood union is u-w. Therefore before insertion

    N_H(u) union N_H(i) = V(H) \ {w}.

In particular ui is an existing cross-edge, u and i both miss w, and ui has exactly one common miss, namely the supplement w. This is precisely the quasi-edge object used by the layer-sum proof.

The same reasoning also proves uniqueness of the exception for a fixed selected edge. Therefore one selected cross-edge cannot represent two different missing B-pairs. Once one quasi-edge is selected for each missing B-pair, the global selection is injective. At a fixed source, its labels are distinct because the selected cross-edges are distinct, and its supplements are distinct because the underlying missing B-pairs are distinct.

This establishes the particular properties subsequently used in the edge ledger, residual injection and unordered-pair capacity. No assumption of unique quasi-edge *choice* is made: a missing B-pair may have several possible quasi-edges; the construction chooses one.

## 2. Literature cross-check

The standard total-domination formulation describes the same mechanism: adding a missing edge to the relevant complement creates an adjacent dominating pair called a quasi-edge; it uses an endpoint of the added edge, need not be unique, and has a unique undominated vertex before insertion. The usual observation says that for a missing edge uv either {u,v} dominates, or there is z with uz having unique exception v (or zv having unique exception u).

Our root v and B-pair setup explicitly rules out the first alternative because both B endpoints miss v. Thus the project's construction is a specialization of the standard quasi-edge observation. This comparison supports the logic but is not a substitute for checking the later new inequalities.

References consulted in this audit include the Haynes-Henning-van der Merwe-Yeo maximum-degree paper and the Murty-Simon total-domination papers indexed in the project literature notes. No claim of exhaustive literature priority follows.

## 3. Independent exhaustive implementation

`src/check_construction_independent.py` was written separately from `check_layers.py`. It does not import or call the selected-system constructor. It directly:

1. rebuilds all labelled simple graphs for 3<=n<=6;
2. tests diameter-two edge-criticality by deleting every edge;
3. constructs H and every minimum-degree root;
4. for every missing H[B] pair uw, constructs H+uw;
5. enumerates *every* adjacent total-dominating pair in H+uw;
6. verifies that {u,w} is excluded by the root, that every new pair is incident with exactly one of u,w, that the other endpoint lies in A, that the cross-edge existed before insertion, and that its old open-neighbourhood union is exactly V\{supplement}.

Recorded result:

    labelled simple graphs:              33,864
    diameter-two edge-critical graphs:      608
    minimum-degree roots:                    920
    missing B-pairs checked:                 720
    new adjacent total-dominating pairs:     720
    valid quasi-edge characterisations:      720
    ordered-case SHA-256:
      1f2b1bb5bd91d54937f166abd0c26badd8ddd105441cd37a6d0150c557d46c5e

All assertions passed locally and again in GitHub Actions run `34194951298` on Ubuntu 24.04, commit `604ce7b16d559d35386960b2d6d9d50be5aee319`. In this small exhaustive domain each insertion happened to have one adjacent total-dominating pair, but the proof and checker do not assume uniqueness generally.

This is a second implementation by the same assistant, not external reproduction and not a universal proof by enumeration.

## 4. Lean extension

The existing `formal/QuasiCore.lean` slice previously began *after* the quasi-edge premises. It now includes explicit local definitions of adding one edge and an adjacent total-dominating pair, plus four bridge lemmas formalising:

- an added edge cannot affect an ordered adjacency whose left endpoint avoids both inserted endpoints;
- a genuinely new adjacent total-dominating pair must be incident with the added edge;
- the newly added endpoint-pair cannot totally dominate when the two endpoints have a common missed vertex;
- an adjacent total-dominating pair `u,i` created by adding `u,w`, under the stated distinctness/missing-edge hypotheses and absence of an old pair, yields `Quasi adj u i w`.

The first GitHub Lean run, `34194781386` at commit `799410e5bebe290e73b72d306c260bd6812fe18b`, failed because the proof script for the common-miss endpoint lemma used the wrong equality component/direction in four cases. The other new bridge lemmas elaborated. The case handling was corrected without changing the mathematical statement.

The corrected source at commit `60f943d5aeed683cc520e043a1b6b26f581a750c` passed GitHub Actions run `34194930796` using Lean 4.19.0 on Ubuntu 24.04. The workflow explicitly rejects `sorryAx`, warnings and errors. The log reports no `sorryAx`; together with the six existing local lemmas, ten local quasi-edge/edge-insertion lemmas now check in this scoped file.

This does **not** formalise diameter-two edge-criticality, the finite selection/injection construction, the residual ledger, threshold pair counting, the layer-sum inequality, or the 13/22 consequence.

## 5. Remaining gap after this audit

The major unformalised pieces before the numerical layer theorem are primarily finite-cardinality selection/injection statements and the threshold/layer counting. The minimum-degree edge ledger is elementary and independently re-derived. The highest-value next formal target is the residual injection or an abstract finite version of the threshold pair-capacity lemma.

The absence of positive-surplus actual graph examples is not resolved by this audit. Any counterexample to the Murty-Simon density bound in the relevant maximum-degree range would necessarily have positive surplus, so existing actual-graph samples cannot exercise that hypothetical regime.

**Verdict:** the graph-to-selected-system bridge is materially better supported than at the start of this audit; no blocking logical defect has been found. The full 13/22 result remains a candidate until the remaining new counting argument receives independent mathematical review (and, ideally, broader formalisation).


\newpage

# Included source: `project/research/general_n/2026-09-08-layer-sum-v1/LAYER_AGGREGATION_AUDIT_2026-09-08.md`

# Adversarial audit of the layer aggregation

8 September 2026. Internal assurance by ChatGPT/Geeps. **The full 13/22 result remains CANDIDATE; independent mathematical review remains OPEN.**

## Verdict

No blocking defect has been found in the passage from the threshold family

    2 W_h <= z_h^2-z_h+h(h+1)

to the cubic residual inequality. The audit instead exposes a slightly stronger intermediate statement. If

    H=max_i s_i,
    r_H=sum_{h=1}^H z_h=sum_u min(rho_u,H),

then for S>0

    3 S^3 <= a^2 r_H(2r_H+1).                       (A)

Since r_H<=r, this immediately implies the published candidate inequality

    3 S^3 <= a^2 r(2r+1).

The stronger form isolates the only final relaxation: replacing the residual mass visible below the maximum demand by the full residual mass.

## 1. Maximum-demand confinement is stronger than previously stated

Choose a label i with s_i=H. Since x_i>=s_i, that label occurs on at least H distinct selected cross-edges. They have distinct sources because a simple cross-edge (u,i) can be selected at most once. Source demand gives rho_u>=H at each of those sources.

Consequently every one of the first H residual tail counts contains those H sources:

    z_h>=H  for 1<=h<=H.

Summing gives the stronger observation

    r_H=sum_{h=1}^H z_h >= H^2.                     (B)

The earlier proof only recorded H^2<=r. Statement (B) is what the aggregation actually supplies before the final relaxation r_H<=r.

## 2. First Cauchy-Schwarz step

Let

    W_h=sum_{i:s_i>=h} s_i,
    L=sum_{h=1}^H sqrt(W_h).

The layer-cake identity is exact:

    sum_h W_h=sum_i s_i^2.

Cauchy-Schwarz on the a demands gives

    S^2 <= a sum_i s_i^2 = a sum_h W_h.

Also W_h<=S, so W_h<=sqrt(S)sqrt(W_h). Hence

    sum_h W_h <= sqrt(S)L.

For S>0,

    S^3 <= a^2 L^2.                                 (C)

There is no reversal or strictness issue here. The only use of W_h<=S is termwise and all quantities are nonnegative.

## 3. Weighted Cauchy-Schwarz step

Because z_h>=H>=1, every denominator is positive. Write

    sqrt(W_h)=sqrt(z_h)*sqrt(W_h/z_h).

Cauchy-Schwarz gives

    L^2 <= (sum_h z_h)(sum_h W_h/z_h)
         = r_H sum_h W_h/z_h.                       (D)

Divide the threshold inequality by z_h and sum:

    2 sum_h W_h/z_h
      <= sum_h z_h - H + sum_h h(h+1)/z_h
      = r_H-H + sum_h h(h+1)/z_h.

Using z_h>=H,

    sum_h h(h+1)/z_h
      <= (1/H) sum_{h=1}^H h(h+1)
      = (H+1)(H+2)/3.

Therefore

    2 sum_h W_h/z_h
      <= r_H + (H^2+2)/3
      <= r_H + (r_H+2)/3
      = (4r_H+2)/3,                                 (E)

where the second inequality is exactly (B).

Combining (D) and (E) gives

    3 L^2 <= r_H(2r_H+1).                           (F)

Equations (C) and (F) prove (A). Since x -> x(2x+1) is increasing for x>=0 and r_H<=r, the original cubic bound follows.

This version is cleaner than the earlier presentation because no mixed replacement of r_H and H^2 by r is needed inside one product.

## 4. Independent abstract counterexample search

A new checker, `src/check_layer_aggregation_adversarial.py`, does not enumerate graphs. It enumerates every nondecreasing demand multiset of length a with entries in {0,...,a-1} for every 1<=a<=11. For each profile it constructs the componentwise-minimal nonincreasing integer tail z_h satisfying exactly the two structural consequences used here:

1. z_h>=H for 1<=h<=H;
2. 2W_h<=z_h^2-z_h+h(h+1).

The monotone closure is necessary because z_h is a degree-tail count. This is adversarial: any other feasible tail has at least as much truncated mass r_H, and the right side of (A) is increasing in r_H. Thus the minimal tail is the hardest abstract case for the cubic inequality for that demand profile.

The complete domain through a=11 contains:

    sorted demand profiles:       478,192
    nonzero profiles:             478,181
    threshold levels checked:   4,215,632

The checker also verifies the layer-cake identity, S^2<=a sum s_i^2, r_H>=H^2, the exact rational summed-threshold estimate, and (A) using integer arithmetic except for exact `Fraction` divisions.

The smallest observed integer slack in (A) is positive. The smallest observed ratio RHS/LHS is

    13301/11000 = 1.2091818...

at a=11 with all eleven demands equal to 10 and r_H=141. This numerical margin is not asserted to persist asymptotically and is not used in the proof.

## 5. Scope and remaining risk

This audit is deliberately abstract. It does not claim that every tested demand/tail profile is graph-realisable, nor does it use absence of a finite counterexample as the universal proof. The universal argument is the short chain (B)-(F), using standard Cauchy-Schwarz plus the already-audited threshold inequality.

The main remaining mathematical risks now lie upstream and downstream rather than inside the aggregation algebra:

* upstream: the graph-to-threshold structural premises, especially source demand and high-source supplement confinement;
* downstream: solving the cubic residual inequality into the surplus bound `t<4a^2/81+1/8` and assembling the exact 13/22 degree consequence.

The upstream pieces now have separate construction, residual-injection and threshold-capacity audits, plus a scoped local Lean slice for quasi-edge logic. The full finite-cardinality reduction and the layer aggregation are not formally verified in Lean.

**Research decision:** treat the layer aggregation as internally strengthened, with (A) as the preferred intermediate statement. Before trying to improve 13/22, attack the downstream cubic-to-surplus optimisation and small-order assembly independently.


\newpage

# Included source: `project/research/general_n/2026-09-08-layer-sum-v1/RED_TEAM_2026-09-08.md`

# Adversarial audit of the layer-sum candidate

8 September 2026. Internal red-team by ChatGPT/Geeps. **Independent mathematical review remains OPEN.** This audit does not promote the candidate theorem to externally verified status.

## Verdict

No blocking defect was found in the three load-bearing steps audited here: (i) the residual injection/source-demand lemma, (ii) heavy-supplement confinement and unordered-pair capacity, and (iii) the layer summation through the common residual budget. The surplus optimisation and small-order boundary were also re-derived independently. The candidate implication remains

    n>=6 and Delta(G)>=13n/22  ==>  e(G)<floor(n^2/4).

The principal unresolved risk is still the hand proof of the universal graph-to-selected-system construction and its local injections; finite tests contain no positive-surplus graph.

## 1. Residual injection

Fix a selected edge `ui->w` with label `i in A`, source `u in B`, supplement `w in B`. Let `j` be an F-neighbour of `i`, so `ij` is absent in H. Since `ui` has unique exception `w`, it dominates `j`; therefore `uj` is an H-edge.

Partition these `d_i` vertices `j` according to whether `uj` is residual or selected. At most `rho_u` are residual. If `uj` is selected, let its supplement be `w_j`. Distinct selected cross-edges at source u correspond to distinct missing B-pairs, so their supplements are distinct; moreover `w_j != w`. Since `ui` has only exception w, it dominates `w_j`; `u w_j` is absent (it is the missing B-pair underlying `uj->w_j`), hence `i w_j` is present in H.

The edge `i w_j` cannot itself be selected. The selected edge `u j->w_j` has exception `w_j`, hence `j w_j` is absent in H. Also `ij` is absent by the choice of j. Thus the adjacent pair `i,w_j` fails to dominate the A-vertex j, whereas every selected cross-edge in this construction has its unique exception in B. Consequently `i w_j` is residual. Distinct `w_j` give distinct residual edges at i. Therefore

    d_i <= rho_u + R_i,
    s_i=max(0,d_i-R_i) <= rho_u.

Potential failure modes checked: reusing a supplement, accidentally allowing `w_j=w`, treating an H-edge as selected despite an A-exception, and confusing F-adjacency with H-adjacency. None survives the definitions.

## 2. Heavy supplements and pair capacity

For threshold h let `I_h={i:s_i>=h}` and `Z_h={u:rho_u>=h}`. The source-demand lemma puts every selected incidence of a heavy label in `Z_h`.

If a source u has `ell_u>h` selected heavy labels and `ui->w` is one of them, supplement forcing makes w adjacent in H to every other selected heavy label at u. If `w notin Z_h`, then w cannot select a heavy label (source demand would require `rho_w>=h`). Hence all of those at least h heavy-label neighbours at w are residual, contradicting `rho_w<h`. Therefore every heavy arc from a source with load >h has its supplement in `Z_h`.

Each such selected arc uses the unordered B-pair `{u,w}` that generated it. No unordered missing B-pair has two selected orientations. If j sources in `Z_h` have load >h, the heavy arcs from them therefore occupy distinct unordered pairs of `Z_h` incident with the j-source set. Their number is at most

    j(z_h-j)+binom(j,2)=j z_h-j(j+1)/2.

The other `z_h-j` sources have at most h heavy incidences each. Since actual selected degree at every heavy label is at least its demand,

    W_h <= X_h <= (z_h-j)h+j z_h-j(j+1)/2.

Maximising over integer j gives

    W_h <= h z_h+binom(z_h-h,2),
    2W_h <= z_h^2-z_h+h(h+1).

The audit specifically checked the possible double-counting of an unordered pair when both endpoints are high-load. It is counted once by `binom(j,2)`, not twice. This is essential.

## 3. Layer summation

Let `H0=max_i s_i>0`. A label with demand H0 has at least H0 distinct selected cross-edges and hence H0 distinct sources. Source demand puts every one at residual degree at least H0. Thus `z_h>=H0` for every `1<=h<=H0`, and the residual layer cake gives `H0^2<=r`.

Set

    r0=sum_{h=1}^{H0} z_h <= r,
    L=sum_{h=1}^{H0} sqrt(W_h).

The demand layer cake is exact:

    sum_h W_h=sum_i s_i^2.

Also `W_h<=S` because it is a sub-sum of the nonnegative demands. Therefore

    S^2 <= a sum_i s_i^2
        = a sum_h W_h
        <= a sqrt(S) L,

so `S^3<=a^2 L^2`.

Weighted Cauchy-Schwarz gives

    L^2 <= r0 sum_h W_h/z_h.

Dividing the exact threshold bound by z_h and summing gives

    2 sum_h W_h/z_h
      <= r0-H0 + sum_h h(h+1)/z_h
      <= r0-H0 + (H0+1)(H0+2)/3
       = r0+(H0^2+2)/3.

The second inequality uses `z_h>=H0`; no monotonicity beyond the residual layer cake is silently assumed. Since `r0<=r` and `H0^2<=r`, both nonnegative factors can be enlarged to obtain

    2L^2 <= r[r+(r+2)/3],
    3L^2 <= r(2r+1).

Combining proves `3S^3<=a^2 r(2r+1)`.

Potential failure modes checked: confusing maximum demand with maximum residual degree; summing W_h beyond H0; using a reversed Cauchy-Schwarz inequality; replacing z_h by H0 in the wrong direction; and enlarging one factor while another could be negative. All relevant quantities are nonnegative and the displayed directions are correct.

## 4. Surplus optimisation and boundary

From `3S^3<=a^2r(2r+1)`, completing the square gives

    (r+1/4)^2 >= (3/2)S^3/a^2+1/16,
    r > sqrt(3/2) S^(3/2)/a - 1/4

when S>0. Together with `2t<=S-r`, put `u=sqrt(3/2)*sqrt(S)/a`. Then

    2t < (2/3)a^2 u^2(1-u)+1/4.

The identity

    4/27-u^2(1-u)=(u-2/3)^2(u+1/3)

is nonnegative for u>=0, giving `t<4a^2/81+1/8`.

For `Delta>=13n/22`, `Delta-n/2 >= 2(n-Delta)/9 = 2(a+1)/9`. The parity-safe density lower bound is

    t >= 4(a+1)^2/81-1/4.

This contradicts the upper bound for a>=4. The a=1,2,3 cases are handled separately in the proof. `K(2,3)` is a genuine n=5 equality example satisfying the ratio premise, so the n>=6 scope must not be weakened to n>=4 without an explicit exception.

## 5. Additional finite adversarial check

An independent arithmetic search was started over demand vectors and nested threshold-source counts, using only the threshold-capacity constraints rather than graph samples. It found no counterexample through the fully completed domains a<=5. The a=6 brute-force attempt was deliberately stopped when its naive enumeration became inefficient; no result for a=6 is claimed from that attempt. This is supplementary evidence only and is not used in the proof.

## 6. Remaining review obligations

1. Specialist review of the quasi-edge existence/selection argument in the complement formulation.
2. Independent review of the residual-injection statement, especially the assertion that `i w_j` cannot be selected because it has an A-vertex exception.
3. Independent review of the unordered-pair orientation injection.
4. Formalisation of the graph-to-selected-system and layer-sum lemmas if practical.
5. Search for or construct positive-surplus actual graph examples; current finite graph samples do not exercise the dense contradiction nonvacuously.
6. Only after those checks, optimise the layer inequality further or use it against the middle-degree region.

**Research decision:** do not lower the coefficient further yet. The current highest-value action is proof assurance, not numerical optimisation. This follows the project's standing instruction to avoid sunk-cost continuation and to prioritise the most consequential unresolved obligation.


\newpage

# Included source: `project/research/general_n/2026-09-08-layer-sum-v1/RECONCILIATION.md`

# Concurrent-checkpoint reconciliation — 8 September 2026

The layer-sum derivation and fresh runs started from `f332e47ae4c32dd28ff0c7765130fff2770b20e0`. Before creating its publication commit, the branch was read again and had advanced by 16 commits to `ac90a88de6e0548a3c52976095e3cbbf8641606f` (tree `9d56440a10b7610713a89f9b61a864e520f67ecb`). The comparison and current README were inspected. Publication is rebuilt on that newer parent rather than overwriting it.

The concurrent work adds the demand-tail-stability-v10 and Jensen-tail-v11 directories, their workflows, exact-check records, a sixth local Lean lemma, and README history. All those existing files are retained unchanged by this layer-sum publication. The root README is merged additively, with the immediately preceding version preserved as `project/reviews/history/README_before_layer_sum_2026-09-08.md` (original blob `f595ff34f685d7910a7ea03c72366f56454e2237`).

The current concurrent README reports a v11 candidate threshold of 0.6116 for n>=4, supported by a clean-runner exact Sturm check. This continuation neither reruns that check nor audits the full v11 proof; it preserves its scope and evidence rather than claiming them as new work here. The new 13/22 layer-sum candidate applies for n>=6, uses the shared threshold mechanism rederived in its own proof, and needs none of the new v10/v11 numerical constants. It improves the stated degree coefficient for n>=6, not the n>=4 strict domain. K(2,3) is retained as the explicit boundary exception.

The earlier unreferenced blobs called weighted-spare-source v10 in the previous chat turn are not the newly committed demand-tail-stability-v10 directory. They remain an unresolved historical preservation obligation and are not adopted as checked evidence.

The mathematical proof, both checking programs, their outputs and the intermediate arithmetic history were not altered by this publication rebase. Only navigation, provenance and this reconciliation were added or updated. No frozen finite-order proof, original archive, theorem-ledger entry, existing concurrent source or external-review status is changed by this publication.
