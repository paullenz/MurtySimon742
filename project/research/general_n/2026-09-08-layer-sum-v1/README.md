# Layer-sum continuation — 8 September 2026

**Candidate hand proof; internal finite checks REPRODUCED; independent mathematical review OPEN.**

[Full mathematical derivation](PROOF.md). The current candidate implication is

    n>=6 and Delta(G)>=13n/22  ==>  e(G)<floor(n^2/4).

The coefficient 13/22 is 0.59090909..., compared with the previous continuation's 0.6129. This is a conditional all-order degree theorem, not a proof for every graph order without a degree restriction. K(2,3) prevents extending this strict statement to all n>=4.

The main inequalities, with a=n-1-Delta and t=m-Delta(n-Delta), are

    3 S^3 <= a^2 r(2r+1),
    t < 4a^2/81 + 1/8.

Here r is residual cross-edge count and S the sum of minimum label demands. The proof sums exact capacity across all demand levels. It has no large-a cutoff and does not depend on the old charging-deficit constants.

## Assurance status

The graph-to-quasi-edge bridge has now received a separate [construction audit](CONSTRUCTION_AUDIT_2026-09-08.md). A second implementation, independent of the layer-sum selected-system builder, exhaustively checked every labelled graph through six vertices, every minimum-degree root, every missing B-pair and every adjacent total-dominating pair created by insertion. Its clean GitHub run passed.

The local Lean slice in `../2026-09-07-stability-spare-sources-v9/formal/QuasiCore.lean` now checks ten local lemmas in Lean 4.19.0, including four explicit edge-insertion-to-quasi-edge bridge lemmas. The first new Lean attempt exposed a proof-script equality-direction error; the corrected statement passed without changing the mathematical claim. This is deliberately preserved in the [assurance record](evidence/CONSTRUCTION_ASSURANCE_2026-09-08.json).

A further independent residual-injection checker is nonvacuous on larger deterministic critical-graph samples: 588 forced residual targets in 163 systems, while also exhaustively checking all selected systems through six vertices. The combined clean-runner workflow passed. This is internal assurance by the same assistant, not external reproduction or universal proof by enumeration.

The remaining new mathematical risk is concentrated further downstream: finite-cardinality selection/injection formalisation, threshold source-supplement pair capacity, and the layer-sum counting/optimisation. The full 13/22 result is not formally verified.

## Replay

The core arithmetic and selected-system programs use only the Python standard library:

```sh
python3 -I -B src/check_threshold_capacity.py
python3 -I -B src/check_layers.py --output /absolute/path/to/new-layer-report.json
python3 -I -B src/check_construction_independent.py
python3 -I -B src/check_residual_injection_independent.py
```

The `check_layers.py` output path must not already exist. `EVIDENCE.json` contains the original layer-sum run records and graph inputs/results; [RESULTS.md](RESULTS.md) summarises them. The newer construction/injection run IDs, hashes, counts and formal scope are in [evidence/CONSTRUCTION_ASSURANCE_2026-09-08.json](evidence/CONSTRUCTION_ASSURANCE_2026-09-08.json).

The original layer-sum run checks 1,059 selected systems, including all choices at all maximum-degree roots in the 608 critical labelled graphs found through six vertices. Only 12 of those systems have nonzero demand, and none has positive surplus. Abstract arithmetic tests and oriented-graph tests are not actual critical-graph counterexample searches. The newer injection sample makes the residual forcing mechanism itself nonvacuous, but still does not produce a positive-surplus graph.

The previous turn's unattached weighted-spare-source v10 uploads are not treated as a published or checked checkpoint. They are distinct from the concurrent demand-tail v10 and Jensen-tail v11 checkpoints, which are preserved; see [RECONCILIATION.md](RECONCILIATION.md). The prior threshold note, frozen papers, original evidence and theorem ledger remain unchanged.
