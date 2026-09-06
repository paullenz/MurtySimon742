# N=25 red-team audit, 6 September 2026

Read `N25_Red_Team_Report_2026-09-06.md` first. This is a further internal adversarial audit by the same assistant. It is not an external review or formal verification.

The audit found no blocking failure in the frozen candidate. It found a primary matching-helper defect outside every dimension used in the proof and reproduced counterexamples to several weakened versions of the lemmas. The candidate's actual hypotheses exclude those counterexamples.

## Reproduce

Use Python 3.10 or later and the standard library. Supply the unchanged reviewer ZIP previously delivered with edition 1:

```sh
python3 -I -B run_redteam.py --reviewer-zip /path/to/N25_Reviewer_Package_v1_2026-09-06.zip --output /path/to/new-redteam-run
```

The output directory must not already exist. The script checks the audit manifest, pins both nested archives by SHA256, checks every consumed proof-input hash, and runs the three audit scripts. Allow a few minutes and several hundred megabytes of memory; the largest stored ledgers are decompressed as streams. Timing depends on the machine.

`--prepare-only` checks and extracts the inputs without running the audit. That mode does not verify the mathematical or arithmetic claims.

## Contents and limits

- `structural_attack.py`: exhaustive labelled graph generation for orders 3–6, complete selected-edge choices on nonisomorphic small representatives, and seeded larger examples through order 25. No graph catalogue or proof-verifier imports.
- `arithmetic_attack.py`: a third check of every recorded outer state, labelled column and final certificate. Domain sizes use generating-function coefficients; source bounds use threshold cuts. No imports from either original scanner or certificate checker.
- `helper_boundary_attack.py`: imports the original helpers only to reproduce their out-of-scope supplier-count discrepancy.
- `*_results.json`, logs and `tested_graphs.json`: exact scope, counts and negative controls.
- `PROPOSED_CLARIFICATIONS.md`: explicit hypothesis statements, a direct alternative high-degree argument and the proposed helper guard. These have not been inserted into the frozen manuscript.
- `AUDIT_INPUTS.json`: exact hashes of the files consumed by the checks.
- `MANIFEST.json`: exact hashes of this audit's payloads.

The existing candidate PDF, proof, evidence archive and theorem ledger are unchanged. The external mathematical review and external computational review remain OPEN.
