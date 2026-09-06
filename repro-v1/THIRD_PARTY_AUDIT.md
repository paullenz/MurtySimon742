# Third-party audit protocol

This release is designed so a referee/auditor can distinguish verified mathematics from computational evidence without trusting chat history.

## 1. Fast audit

Run:

```bash
bash scripts/reproduce_all.sh --fast
python3 tests/test_ledger_negative.py
```

This checks bundled hashes and ZIP integrity, rejects uncertified theorem imports, and reruns deterministic arithmetic/coverage checks from the preserved capsules.

## 2. Full checkpoint audit

Obtain the separately preserved archive `delta14_full_checkpoint_2026-09-06.zip` and place it in `external/`. Its expected SHA-256 is recorded in the release ledger. Then run `bash scripts/reproduce_all.sh --full`.

The release intentionally does not silently treat screening-stage UNSAT exits as certified proof leaves.

## 3. Trust boundary

Only branches with `theorem_dependency_allowed: true` in `ledger/theorem_ledger.json` may be cited as proved in the paper. `REPRODUCED` means a complete fresh no-survivor computation exists but proof-producing or independence requirements remain.

## 4. Independent reproduction requested

A serious external audit should independently rebuild catalogues, regenerate encodings, generate LRAT for every terminal finite UNSAT leaf, replay it with an independent checker, run bad-proof regression tests, and compare the resulting leaf manifest with the theorem and proof-obligation ledgers.
