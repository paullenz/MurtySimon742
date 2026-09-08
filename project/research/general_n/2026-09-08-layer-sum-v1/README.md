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
