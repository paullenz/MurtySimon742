# Current short structural treatment — 17 September 2026

**Start with [Exact tight blocks: interface capacity and critical-edge rigidity](project/research/general_n/2026-09-17-structural-consolidation-v1/STRUCTURAL_TREATMENT.md).** This is the current compact entry point for the exact-block structural work, not a new claim about the unrestricted conjecture or a replacement for the fixed-order reviewer packages.

The approximately 2200-word treatment assembles the actual-graph representative bridge, exact interface accounting, universal-core inequality, zero-loss star forests and the new one-defect closure. Under the explicit whole-level hypothesis |T|=|H|=d>=5, its conclusion is

    D>=2floor(d/2)+2,
    W>=d+(d-1)m+2floor(d/2)+2.

At d=5: D>=6, W>=31, and W>=51 with extra high-source selections. The existence of an exact block is assumed. Novelty, sharpness and independent mathematical acceptance remain open. This is an internally checked candidate theorem, not a promotion.

## Reproduction

In `project/research/general_n/2026-09-17-structural-consolidation-v1/`, run

    python3 verify_published.py

The published Python and C++ sources regenerate both local-lemma test families and compare their counts and stream hashes with the pinned summaries. Python 3.10+ and a C++17 compiler are required; no network or third-party Python package is used.

The [star-forest summary](project/research/general_n/2026-09-17-structural-consolidation-v1/CHECK_SUMMARY.json) records 324554 matching decisions; the [bounded-hole summary](project/research/general_n/2026-09-17-structural-consolidation-v1/HOLE_CHECK_SUMMARY.json) records 407741. Each includes five effective premise-failure controls. [Fresh-directory regeneration](project/research/general_n/2026-09-17-structural-consolidation-v1/FRESH_REPLAY.json) reproduced both pinned decision streams. These are local short-path checks, not a census of canonical graph realizations. Both implementations are by the same assistant, not external independent reviewers.

The older universal-core 11357-record replay has not been rerun here. The current package is source-complete for its own new tests and does not need old recovery archives. Full generated streams are included in the separately delivered ZIP; their separate raw GitHub upload is not claimed.

## Review and next proof obligation

Review the representative existence argument and residual injections first, then full-pool coverage, the universal-core distinct-label count and the complete external-neighbour classification in the one-defect closure. The proof lists the immutable sources for each inherited result and preserves the pre-test derivations separately.

The next mathematical target is the actual-graph boundary d=5,D=6, with no assumption that L or beta vanishes. Exact-block coverage for arbitrary graphs is a separate open obligation. The canonical ledger remains 4626 exclusions / 952 survivors / 3632 whole-state closures. No old evidence, failed approach or review package is deleted.

For the operational handoff use [CURRENT_STATE.md](CURRENT_STATE.md). The older root README and reviewer index retain their historical snapshots; this entry and the live handoff identify the current structural theorem. The separate repair PR and historical archive work are not represented as completed by this package.
