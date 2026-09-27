# Hall/min-cut reduction checkpoint — 27 September 2026

Start with [REPORT.md](REPORT.md): hand proofs, primary-source access status, exact test scopes and the next mathematical obligation. [THEOREM_A.md](THEOREM_A.md) is the byte-preserved preceding closure proof; its old relative test references belong to the earlier bundle, and its old next-step paragraph is superseded by the report.

The new results are a capacity-permutation saddle formulation, a feasibility-to-deficit dummy reduction, an explicit prescribed-zero exact-margin matrix reduction, and a seven-vertex counterexample to unrestricted minimax (with a direct-sum unbounded-gap extension). These are internal results, not a novelty claim or a promotion of any Murty-Simon theorem/equality status.

## Reproduce

Use Python 3.10 or later, standard library only, from this directory:

```sh
python3 check_reductions.py --output replay --part core
python3 check_reductions.py --output replay --part padding
python3 verify_certificate.py replay/PROPER_CUT_CERTIFICATE.json
```

The first two commands must not use -O. The small independent verifier uses explicit validation and works with or without -O. No command makes a network request, schedules work or uses a paid service.

RESULTS.json and PADDING_RESULTS.json identify the tested source hashes and domains. FANO_COMPACT.json losslessly stores the complete FANO_COUNTEREXAMPLE.json bytes (all 21-by-128 margins, flows and relaxed margins) as zlib-compressed base64, with the decoded length and SHA-256. Join its payload_base64_lines, decode with Python base64.b64decode then zlib.decompress; the result must exactly match the checker-generated FANO_COUNTEREXAMPLE.json bytes. Both representations are included in the downloadable bundle. CERTIFICATE.json is a selected exhaustive-test witness; PROPER_CUT_CERTIFICATE.json supplies the nontrivial singleton-cut example.

SHA256SUMS covers the checkpoint files other than itself and this README. It records the compact remote table. The coordinating-chat bundle also preserves the prior full closure ZIP and patch; those earlier expanded replay sources were not all republished in this folder. No claims are made that historical missing artifacts have been recovered.

Next: check the specialised Anstee/William Y. C. Chen structural condition against the report's exact U-feasibility implication. Feasibility-versus-deficit strength is no longer a valid standalone separation argument. External specialist review remains open.
