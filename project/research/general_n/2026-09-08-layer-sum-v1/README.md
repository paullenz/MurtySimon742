# Layer-sum continuation — 8 September 2026

**Candidate hand proof; internal finite checks REPRODUCED; independent mathematical review OPEN.**

[Full mathematical derivation](PROOF.md). The new candidate implication is

    n>=6 and Delta(G)>=13n/22  ==>  e(G)<floor(n^2/4).

The coefficient 13/22 is 0.59090909..., compared with the previous continuation's 0.6129. This is a conditional all-order degree theorem, not a proof for every graph order without a degree restriction. K(2,3) prevents extending this strict statement to all n>=4.

The main inequalities, with a=n-1-Delta and t=m-Delta(n-Delta), are

    3 S^3 <= a^2 r(2r+1),
    t < 4a^2/81 + 1/8.

Here r is residual cross-edge count and S the sum of minimum label demands. The proof sums exact capacity across all demand levels. It has no large-a cutoff and does not depend on the old charging-deficit constants.

## Replay

Both programs use only the Python standard library. Python 3.13.5 was used for the recorded runs; Python 3.10+ is required by the inherited program's integer bit counts.

```sh
python3 -I -B src/check_threshold_capacity.py
python3 -I -B src/check_layers.py --output /absolute/path/to/new-layer-report.json
```

The output path must not already exist. `EVIDENCE.json` contains the fresh run records and full graph inputs/results. Its `layers_report` member is the expected parsed output of the second command. `PROVENANCE.json` records the source checkpoint and preservation scope. File hashes are in [MANIFEST.json](MANIFEST.json); [RESULTS.md](RESULTS.md) summarises the checks. Publication receipt records branch read-back separately.

The run checks 1,059 selected systems, including all choices at all maximum-degree roots in the 608 critical labelled graphs found through six vertices. Only 12 systems have nonzero demand, and none has positive surplus. Abstract arithmetic tests and the inherited oriented-graph tests are not actual critical-graph counterexample searches. No Lean run or remote CI result is claimed.

The previous turn's unattached weighted-spare-source v10 uploads are not treated as a published or checked checkpoint. They are distinct from the concurrent demand-tail v10 and Jensen-tail v11 checkpoints, which are preserved; see [RECONCILIATION.md](RECONCILIATION.md). This directory has new derivation and execution provenance. The prior threshold note, frozen papers, original evidence and theorem ledger are unchanged. `HISTORY.json` and `history/initial-to-final.patch` preserve the weaker intermediate run and code changes without calling it an external audit.
