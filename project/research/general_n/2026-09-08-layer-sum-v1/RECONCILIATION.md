# Concurrent-checkpoint reconciliation — 8 September 2026

The layer-sum derivation and fresh runs started from `f332e47ae4c32dd28ff0c7765130fff2770b20e0`. Before creating its publication commit, the branch was read again and had advanced by 16 commits to `ac90a88de6e0548a3c52976095e3cbbf8641606f` (tree `9d56440a10b7610713a89f9b61a864e520f67ecb`). The comparison and current README were inspected. Publication is rebuilt on that newer parent rather than overwriting it.

The concurrent work adds the demand-tail-stability-v10 and Jensen-tail-v11 directories, their workflows, exact-check records, a sixth local Lean lemma, and README history. All those existing files are retained unchanged by this layer-sum publication. The root README is merged additively, with the immediately preceding version preserved as `project/reviews/history/README_before_layer_sum_2026-09-08.md` (original blob `f595ff34f685d7910a7ea03c72366f56454e2237`).

The current concurrent README reports a v11 candidate threshold of 0.6116 for n>=4, supported by a clean-runner exact Sturm check. This continuation neither reruns that check nor audits the full v11 proof; it preserves its scope and evidence rather than claiming them as new work here. The new 13/22 layer-sum candidate applies for n>=6, uses the shared threshold mechanism rederived in its own proof, and needs none of the new v10/v11 numerical constants. It improves the stated degree coefficient for n>=6, not the n>=4 strict domain. K(2,3) is retained as the explicit boundary exception.

The earlier unreferenced blobs called weighted-spare-source v10 in the previous chat turn are not the newly committed demand-tail-stability-v10 directory. They remain an unresolved historical preservation obligation and are not adopted as checked evidence.

The mathematical proof, both checking programs, their outputs and the intermediate arithmetic history were not altered by this publication rebase. Only navigation, provenance and this reconciliation were added or updated. No frozen finite-order proof, original archive, theorem-ledger entry, existing concurrent source or external-review status is changed by this publication.
