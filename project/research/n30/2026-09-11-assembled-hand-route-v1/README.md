# N30: complete supplementary proof with hand lemmas and integer tables

11 September 2026. Continuation from main `d680ddd208d338b019d00492f9498e6da2acfdbc` in `paullenz/MurtySimon742`.

**Complete supplementary candidate argument; internal exact arithmetic REPRODUCED. Independent specialist review OPEN. Frozen reviewer-v2 and the governed ledger are unchanged.**

The [assembled proof](ASSEMBLED_PROOF.md) now covers every degree and edge-count scope for the candidate statement `e(G)<=225`, with equality exactly `K(15,15)`.

The main new simplifications are:

- **Delta=17 is closed by hand.** The source-independent twelve-label bound gives Q<=18, while any positive surplus at Delta=17 requires Q>=19. In fact this branch has m<=221. The same padding argument closes every higher non-star degree.
- **Delta=15 equality is elementary.** In a 15-regular graph on thirty vertices, every nonadjacent pair has at least two common neighbors. Edge-criticality therefore forces every edge to be triangle-free, and then the graph is K(15,15). The published dominating-edge theorem is no longer needed by this route.
- **The Delta=16 assembly passes a fresh independent audit.** It reproduces all 272 m225 rows and nine m226 rows; the ledger excludes 61 and one respectively. A separately written evaluator verifies all 844 four-template gaps on the remaining 211 m225 rows, and all eight m226 source certificates.

The [twelve-label transfer](TWELVE_LABEL_TRANSFER.md) also gives the candidate corollary `e(G)<=Delta(n-Delta)` whenever `1<=n-1-Delta<=12` and `Delta>=17`. Its novelty is not assessed here.

## Proof and evidence

- [Complete supplementary proof](ASSEMBLED_PROOF.md).
- [Hash-pinned proof dependencies and removed historical dependencies](PROOF_DEPENDENCIES.json).
- [Source-independent twelve-label hand proof](TWELVE_LABEL_TRANSFER.md).
- [Graph bridge audit and historical text clarifications](BRIDGE_AUDIT.md).
- [Independent assembly audit](ASSEMBLY_AUDIT.json) and [standalone checker](audit_assembly.py).
- [All independently recomputed local minima and row gaps](INDEPENDENT_ENVELOPES.json).
- [Full arithmetic profile regression](PROFILE_REGRESSION.json) and [C++ source](profile_regression.cpp).
- [Provenance and next steps](HANDOVER.md).

The independent profile regression covers 5,200,300 thirteen-demand multisets and 1,352,078 twelve-demand multisets. It finds no clipping counterexamples. This exhaustive work is corroboration only: the written proofs use the clipping arguments and explicit bounded tables.

## Reproduce the audit

From the repository root:

```sh
g++ -O2 -std=c++17 project/research/n30/2026-09-11-assembled-hand-route-v1/profile_regression.cpp -o /tmp/n30-profile-regression
/tmp/n30-profile-regression /tmp/n30-profile-regression.json
python -I -B project/research/n30/2026-09-11-assembled-hand-route-v1/audit_assembly.py
```

The saved regression JSON is the checker's input. The first two commands reproduce it separately; comparison with the committed JSON is optional. The [CI workflow](../../../../.github/workflows/n30-assembled-hand-route.yml) regenerates it and then runs the audit. No older checker or discovery module, solver, or floating point is imported by the new Python evaluator.

## Remaining boundary

The logical route no longer needs large profile/residual searches, LP/Farkas systems, Fan's density theorem, the dominating-edge theorem, or any separate Delta=17 computational branch. It **does retain explicit proof-critical finite arithmetic** in the Delta=16 classification, tail reconstruction and endpoint tables. This distinction matters when describing it as a hand argument.

The next task is to consolidate this complete supplementary route into a coherent reviewer edition, with the table burden and universal-bridge review targets made clear. No new reviewer PDF is issued here, and internal checking is not external acceptance.
