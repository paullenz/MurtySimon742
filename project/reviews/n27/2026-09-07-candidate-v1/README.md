# N=27 candidate proof and complete evidence, edition 1

7 September 2026. Work developed with substantial ChatGPT/Codex assistance for Paul Lenz.

**Candidate status: the proposed upper bound and equality chain are complete, with internal arithmetic checks passed. Independent mathematical review and reproduction by another researcher remain OPEN.**

The proposed statement is that every simple diameter-two edge-critical graph on 27 vertices has at most 182 edges, with equality exactly for K13,14. Start with [PROOF.md](PROOF.md), then [RESULTS.json](RESULTS.json). This package extends the n=25 candidate method; it does not change or certify the frozen n=25 edition.

## Distribution

The downloadable evidence ZIP contains the complete directory described below. The GitHub source folder provides the manuscript, code and smaller records for browsing; obtain the large ledgers and column files from [the archive distribution](https://github.com/paullenz/MurtySimon25/tree/main/releases/n27-candidate-v1) before running verification.

## Verify or reproduce

From this extracted directory, verify the manifest, aggregate consistency and final certificates:

```sh
python3 -I -B replay.py --verify-only
```

To rebuild the programs and repeat the complete searches, checks and graph tests in a **new** directory:

```sh
python3 -I -B replay.py --replay --output /absolute/path/to/new-n27-replay
```

The second command requires Python 3.10 or later, a C++17 compiler available as `g++`, and development headers/libraries for zlib and OpenSSL libcrypto. The original environment is recorded in ENVIRONMENT.json. It writes substantial temporary evidence; allow several gigabytes of free disk space. No SAT solver, graph catalogue or floating-point optimisation is required. The C++ programs are built from source; executables are not distributed in the archive.

The full replay checks every outer state and every canonical residual column. The quick verification command does not rerun those searches. A successful computation remains conditional on the graph-theoretic lemmas in PROOF.md.

## Evidence map

- `general_primary.py`, `general_independent.py` and `d16_*`: separate Python implementations for Delta=16. Both dense edge counts fail the pair-threshold inequality.
- `survey.cpp`, `d15_*_ledger.jsonl.gz`, `d15_*_frontier.jsonl.gz`: the complete Delta=15 outer domains, pruning witnesses and retained states.
- `check_survey.cpp`, `d15_*_outer_check.json`: a separate outer checker using generating-function domain counts, strict ordered-key uniqueness and direct witness arithmetic.
- `columns.cpp`, `d15_*_columns.jsonl`, `d15_*_cuts.jsonl.gz`: canonical residual-column enumeration, source bounds and explicit subset cuts. The `check` mode rederives capacities by threshold matching and checks cuts directly without running max flow.
- `d15_*_check_columns.jsonl`: the full column replay. Every per-state digest agrees with the search. Search and replay share their C++ column generator; separate recurrence counts and labelled orbit weights check coverage.
- `pair_column.py`, `d15_*_pair_certificates.json.gz`: fixed-column pair-count inequalities eliminating the later survivors.
- `supplement_pair.py`, `d15_182_supplement_certificates.json`: the final four equality columns and their forced-source pair-budget contradictions.
- `check_final.py`, `FINAL_CHECK.json`: direct checking of all final strict inequalities and complete survivor coverage, importing no search program.
- `structural_validation.py`, `structural_results.json`, `tested_graphs.json`: actual-graph falsification tests through order 27, including the two new inequalities. These finite samples do not prove universal lemmas.
- `check_column_sample.py`, `COLUMN_SAMPLE_CHECK.json`, `validation_*`: a six-state cross-language check using fully labelled enumeration, augmenting-path matching and exhaustive subsets. Its mixed-edge-count fixture is explicitly a validation sample, not a production scope.
- `preflight.py`, `PREFLIGHT_CHECK.json`: exact Fan arithmetic, witness tables, degree bands and agreement between aggregate records.
- `ADAPTATION_PROVENANCE.json` and `.patch` files: origins and changes to the inherited n=25 Python code, including the supplier-length guard.
- `CLEAN_REPLAY_CHECK.json`, `clean_replay.log`, `clean_replay_logs/`: a full clean-directory rebuild and replay, with comparisons against all original generated data and source files.
- `MANIFEST.json`: byte counts and SHA-256 hashes of all distributed payloads; it does not hash itself.

The outer ledger's numeric dispositions are 0=pair threshold, 1=source total, 2=source threshold, 3=column lower bound, 4=retained for column analysis. Each row is `[k,r,d,rho,kind,witness]`; the frontier is `[k,r,d,rho,lower_columns]`.

The column cut file records `[frontier_index,R,caps,mask]` for each column reaching the subset stage. A positive mask is a strict rejection certificate. A zero mask retains the column and must be accounted for by the later pair/supplement stages. Numerical survivors at intermediate stages are preserved even though the final count is zero.

## Main changes beyond n=25

The residual surplus simplifies to `t = e(G) - Delta*(n-Delta)`. The attack preserves the general residual arguments, sorts residual columns only within equal-degree label blocks, iterates the supplement-cap bound to a fixed point, uses max flow to find subset cuts, then adds fixed-column pair demand and forced-source supplement restrictions. The final four equality columns require at least 37 or 39 selected pairs but permit only 21.

All mathematical development and internal checking here were produced by the same assistant. Neither multiple programs nor preserved checksums constitute external expert approval. No novelty or priority claim is made.
