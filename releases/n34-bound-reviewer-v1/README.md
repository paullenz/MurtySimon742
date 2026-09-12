# N34 candidate upper bound: reviewer v1

> Historical bound-only checkpoint. The [current complete N34 reviewer-v2 package](../n34-reviewer-v2/README.md) establishes the candidate equality classification as well. The original hashes in this package's manifest describe [commit efcccf7](https://github.com/paullenz/MurtySimon742/commit/efcccf7f2a4b103f7b7ca3d5201dcb5485ce5fe0), before later navigation updates.

12 September 2026. **Candidate e(G)<=289 for 34-vertex diameter-two
edge-critical graphs. Equality classification and external review OPEN.**

Start with the [proof and exact ledger](../../project/research/n34/2026-09-12-m290-v1/README.md),
then the [universal bridge refinements](../../project/research/general_n/2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md)
and the [focused internal audit](../../project/research/n34/2026-09-12-m290-v1/AUDIT.md).

The previously open 290-edge branch has 1,614 conservative states. All are
excluded: 463 by exact degree mass, 199 by hand threshold contradictions,
and 952 by exact integer envelopes. The solver-free verifier checks 431,338
local inequalities and complete, disjoint coverage. Earlier N34 reductions
close all higher layers. K(17,17) attains the bound; whether it is the only
equality graph remains OPEN, with 13,546 states in the Delta=18 equality branch.

Replay from the repository root:

```sh
python project/research/n34/2026-09-12-m290-v1/verify.py
python project/research/n34/2026-09-12-frontier-v1/verify_upper_layers.py
python releases/n34-bound-reviewer-v1/check_manifest.py
```

These commands need only the Python standard library. The new
[verification report](../../project/research/n34/2026-09-12-m290-v1/verification.json)
and complete certificate coefficients are committed. SciPy is needed only
for optional proposal rediscovery. Failed earlier proposals and the complete
intermediate survivor lists remain preserved in the research package.

[MANIFEST.json](MANIFEST.json) pins this package's artifacts, the direct
replay dependencies and the unchanged dependency commit. The older
[joint-clipping release](../general-joint-clipping-reviewer-v1/README.md)
retains the general scalar bounds and historical N34 upper-layer checkpoint;
its original manifest is a snapshot of commit 21e78b7, not a promise that
subsequently updated navigation files retain their old hashes.

Paul Lenz directed the research; ChatGPT/Geeps developed and internally
checked the candidate mathematics and implementations. External specialist
review, novelty assessment and independent external reproduction remain OPEN.
