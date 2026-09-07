# Label-tail v4: preserved original research checkpoint

7 September 2026. Additive publication of the original v4 package prepared in the generalised-attack chat.

**Candidate mathematics; internal arithmetic REPRODUCED; independent mathematical review OPEN.** No completed order 28 or 64, improved global coefficient, novelty determination, formal verification or theorem-ledger promotion is claimed.

## Recover the complete original checkpoint

The five `CAPSULE.part*.b64` files and `restore_checkpoint.py` preserve all 40 original payload files plus their manifest. Source code, proof, certificates, reports, exact survivor lists, actual-graph inputs and unfinished work are included. Four unchanged dependencies are taken from the already committed sibling `2026-09-07-demand-support-v3` package, with every dependency checked against its original hash.

From this directory in a complete repository checkout:

```sh
python3 -I -B restore_checkpoint.py --output /absolute/path/to/new-v4-copy --zip-output /absolute/path/to/MurtySimon_GeneralN_LabelTail_v4.zip
cd /absolute/path/to/new-v4-copy
python3 -I -B replay.py --verify-only
python3 -I -B replay.py --replay --output /absolute/path/to/new-v4-replay
```

Alternatively supply `--v3-directory /path/to/recovered-original-demand-support-v3` to the recovery command. Read `PROOF.md` and `REVIEW_AND_HANDOFF.md` in the recovered package. `replay.py` describes its compiler and optional discovery dependencies; recovery itself needs only Python's standard library, no network and no optimisation solver.

Recovery expands stored exact numerical rows and rejection codes, reuses the original stored rational dual weights, and repeats the original deterministic abstract-input recipe. It does not search for missing certificates. All historical output values and timing records are preserved, not replaced by new timings. Every original file hash and the complete original ZIP hash were reproduced in the publication environment (CPython 3.13.5). Different serialisation, PRNG or compression behaviour must fail the hashes rather than silently change evidence.

Original ZIP: **566,681 bytes**. SHA-256: `3944e786fb0ea5322ae3e18dd177ef8b01046d903076a4ca61caf89fdc5ae184`.

## Scope

The checkpoint derives the label-tail inequality, excludes the retained n=64/Delta33/m=1025 numerical profile by a hand argument, and generalises that argument to an infinite family of profiles. These are profile exclusions, not whole-order theorems. Its n=28/Delta15 work at m=196 checks 17,669,896 residual rows; 13,196 projected rows in 1,119 demand patterns remain for individual-column and adjacency analysis. Coverage of higher edge counts by the new tests is not assumed.

The original README and provenance are recovered unchanged. Their historical statement that v4 had not been committed is superseded by this publication. GitHub write actions were available and successfully used in this publication session. Earlier frozen proofs, other research directories and the governed theorem ledger are untouched. Preservation is not independent mathematical certification.
