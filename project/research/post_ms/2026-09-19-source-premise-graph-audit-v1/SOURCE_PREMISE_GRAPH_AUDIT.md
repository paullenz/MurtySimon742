# Source-premise graph audit — corrected checkpoint

> **SUPERSEDING CORRECTION — 19 September 2026.** The checker version discussed in the historical material below mislabeled the alpha/matched-source orientation as beta. Its statements about beta P1/P2 are therefore not current evidence. The corrected orientation, direct P1 proof, selected-P2 proof, B_beta counting audit, executable X_3 fixture and graph-derived selected/Hall ledger are preserved in [SOURCE_PREMISE_REPAIR.md](SOURCE_PREMISE_REPAIR.md). Historical discussion below is retained as an audit trail; any statement there that P1 remains unresolved is superseded by the repair note.

## Status

**The provisional raw-P2 counterexample written in the immediately preceding checkpoint was invalid and is withdrawn.**  Replaying it through the preserved checker exposed that the displayed order-9 graph is not D2C and, more basically, its alleged tight pair `(6,8)` at root `4` cannot be a root-neighbour pair because `8` is not adjacent to `4`.  This correction is preserved explicitly rather than silently hiding the failed diagnostic.

This failure strengthens, rather than relaxes, the 2026-09-19 daily red-team requirement: the graph-to-constraint interface must be independently executable and must reject malformed fixtures before any premise is promoted.

## Audit obligations retained

The source-tuple theorem remains conditional on two upstream premises:

1. **P1 (distinct physical sources):** for a fixed A-witness `x`, selected beta obligations on different target coordinates use distinct physical sources in `U`.
2. **P2 (selected source-coordinate uniqueness):** a selected physical `(source y, target coordinate i)` is used once in the selected system.

The historical theorem note in commit `cee68f4684f5e2ed348804fc931043a0f44f0d5d` explicitly says that the selected beta witness for `(y,i)` is a chosen representative of a single physical `P--U` obligation.  Thus selected P2 is documented as a **selection/deduplication convention**, not as a theorem saying all raw A-witness realizations are unique.  This distinction must be kept explicit.

However, this only makes downstream use safe if every lower bound called `B_beta` is genuinely a lower bound on the number of distinct selected physical `(y,i)` obligations.  A lower bound on pre-deduplication witness incidences would not automatically transfer.

## Independently replayed graph-level facts

A clean NetworkX implementation reconstructing tight antipode pairs directly from the definitions in `ANTIPODE_TIGHT_MATCHING_STABILITY.md` was replayed on the full graph atlas through order seven.

- exactly **21** unlabeled D2C graph-atlas classes occur through order seven;
- all roots of all 21 classes were checked;
- the reconstructed tight antipodes formed matchings as required;
- the current raw beta-certificate implementation produced one certificate in total across that small atlas sample;
- no P1 collision and no raw P2 collision occurred in this independently rechecked sample.

These are regression facts only.  They do **not** prove P1 or graph-level raw uniqueness.

The previously reported larger randomized counts and seven alleged raw-P2 collisions are **not retained as verified evidence**, because the first preserved explicit fixture failed independent replay.  They must be regenerated from the corrected checker before use.

## What is actually established at this checkpoint

1. The red-team audit correctly identified the source-premise interface as load-bearing.
2. Selected P2 has a documented definitional basis: one chosen representative per physical `(y,i)` obligation.
3. The attempted raw-P2 refutation failed independent validation and is withdrawn.
4. P1 remains unresolved.
5. The transfer from graph-level beta lower bounds to selected `B_beta` remains unresolved until the counting semantics of those lower bounds is checked theorem by theorem.
6. Therefore the finite source-tuple/FDPr/layer-cake capacity theorem remains **conditional**, exactly as the daily red-team audit required.

## Immediate next work

1. Locate and inspect the root-imbalance and switching lower bounds for `B_beta`; determine whether they count distinct physical source-coordinate obligations after selection or raw witness incidences before deduplication.
2. Regenerate the graph-level regression only from fixtures that pass exact D2C validation and rooted-object consistency checks.
3. Add the published `X_3` adjacency itself as a mandatory negative-control fixture and verify `n=12`, `m=32`, `M(12)=31`, D2C, rooted partition, and the expected `u=0` canonical branch.
4. Continue targeted P1 search/proof only after the checker has those self-tests.
5. Do not resume the one-code downstream branch until these upstream interface points are reconciled.
