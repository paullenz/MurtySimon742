# Hall/min-cut continuation checkpoint — 27 September 2026

## What was achieved

`CANONICAL_CLOSURE.md` reconstructs the original stratified minimum-margin theorem and supplies three internally derived extensions: a unique greatest rearrangement-tight minimum witness (independent of deletion order); weaker pair compatibility; and real receiver capacities with the sharp uniform demand restriction `d_y <= floor(d_x)` across strictly increasing receiver capacities. A counterexample family handles every violating demand pair. The result is a standalone Hall-system statement, NOT a proof that every Murty–Simon model has nonnegative Hall margin.

The original verifier was reproduced byte-for-byte and found to exhaust one-shot demand iterators. Its actual demand counts were 3 and 9. Materialising the iterators and adding a coverage invariant repairs the problem. The repaired program and a separately written checker both reproduce the 39,636 and 172,080 historical counts with no minimum mismatch. This establishes fresh evidence, not the provenance of the historical frozen JSON.

The evidence contains 2,306,226 exhaustive instance checks across seven OVERLAPPING regimes, plus 1,500 structured directed examples with 5–9 vertices, all 64 states/192 crossing choices of a six-deletion example, exact boundary cases and 24 instances of the general sharpness family. All arithmetic is integral or exact rational. The general theorems rest on their written proofs, not these finite totals.

## Files and replay

Read `CANONICAL_CLOSURE.md` and `VERIFICATION.json` first. The three new checkers, the original defective checker and the repaired checker are preserved here. `EXECUTION_RECORDS.json.gz` is a lossless consolidation of all eleven detailed JSON execution records: decompress it to obtain a JSON object whose `records` member maps original filenames to their complete values. The coordinating-chat ZIP additionally preserves each original output file separately, with its original formatting. `SOURCE_HASHES.json` binds the published core bytes; the ZIP has a fuller evidence manifest. Python's standard library is sufficient; no network, service, API or dependency installation is needed.

To read the consolidated evidence without modifying it:

```sh
python -c "import gzip,json; print(json.dumps(json.load(gzip.open('EXECUTION_RECORDS.json.gz','rt')),indent=2))"
```

```sh
python verify_crossing_dominance.original.py
python verify_crossing_dominance.py
python verify_closure.py --regime all --output CLOSURE_VERIFICATION.json
python verify_real_capacities.py --regime unit --output REAL_UNIT.json
python verify_real_capacities.py --regime one --output REAL_ONE.json
python verify_real_capacities.py --regime two --output REAL_TWO.json
python verify_rounded_demands.py
```

The published integer checker outputs were obtained by separately executing `one`, `two`, `weak`, `adversarial` and `random` with the SAME final source; `all` is their combined entry point. Do not run with Python assertion removal (`-O`). The raw records include deterministic case-stream hashes; the manifest binds the actual tested source bytes. The larger random regime is a structured block-threshold family, not a uniform sample of all WCD systems.

## Trust boundary and next action

This was an additional audit and derivation within the same research programme. It was not a blinded independent derivation, external expert review, formal proof-assistant verification, or a completed novelty search. All inherited finite-order/D2C certification boundaries remain unchanged.

Next: compare the greatest-tight-minimizer/rounded-demand theorem with the FULL Marmulla–Brandes threshold/Ferrers paper, DOI 10.7155/jgaa.v30i1.3099, and the original minimum-cut-lattice literature it or follow-up references identify. The required outcome is a precise implication proof or separation example. Reading an abstract or finding similar terminology is not enough. Do not claim novelty or a new Murty–Simon consequence before that check.

No research cadence, local worker, deployed service or paid execution lane was enabled by this checkpoint. Financial and health alerts were not touched.
