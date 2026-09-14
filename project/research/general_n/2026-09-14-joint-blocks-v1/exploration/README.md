# Historical slack and rational-price exploration

These are the ORIGINAL prototype source bytes retained from the local session, not the canonical proof entry points. The canonical independently audited implementation is `../verify_shared_slack.py`, with full inherited branch coverage and explicit empty-projection handling. Prototype sentinel values or missing boundary guards are not additional proof claims.

To reconstruct the old local layout in a separate scratch directory, put both scripts together, copy the committed capped verifier to `lib/prior.py`, block verifier to `lib/block.py`, the original committed twelve-profile input to `remainder12.json`, and the durable complete conditioned output to `conditioned_full.json`. Do not change the source inputs to improve a result. `python3 dual_trial.py` uses exact `fractions.Fraction`, no optimizer or floating solver.

The complete original stdout is preserved in the portable bundle. It is deterministically reproduced by these sources and committed input files. Its raw SHA256 is recorded in EXPERIMENT_RECORD.json. The comparison found that scalar rational pricing covers rows258 and342 but leaves row240's eta2 branches e_L41 and45 unrejected; the integer DP covers them. This is a negative boundary for this relaxation, not proof that all possible price/cut formulations fail. At e_L44 the rational upper bound was103, whereas the integer maximum is102; this distinction caused the corrected draft table entry.

A full simultaneous-block attempt is separately preserved in `../explore_multiblock.py` and its exact-output hash. It leaves454 of597 tuples across all six profiles. Neither a non-rejection nor a best tested multiplier constructs an actual graph.
