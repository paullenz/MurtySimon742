# Historical exploration preceding the canonical conditioned verifier

These two source files match the executed local prototypes byte for byte. They retain their original local paths and are not the canonical portable entry point.

`explore_equality.py` reconstructs an optimizing excess vector for row 295 and tries additional singleton selected-column lower bounds. Those bounds alone do NOT lower the old maximum below 126. The useful result was the equality structure, not a newly strict scalar optimum.

`conditional_trial.py` is the first case-split experiment. It established candidate exclusions of rows 295, 365 and 570. Its broad-domain boundary handling is intentionally not used as the final verifier: in particular, the final independently expressed implementation explicitly rejects impossible nonzero excess in an empty conditioning block and wrong total excess in the whole-label block. Those boundaries are included in the small tests. The prototype was run only on the stated nonempty proper demand prefixes.

The canonical replay is `../verify_conditioned_excess.py`, not either historical prototype. Its full hash-bound output retains all successful and unsuccessful branches of the declared twelve-profile search. `../FROZEN_RESULT.json` gives every branch needed for the three exclusions and the non-excluded ranges for the other nine. The portable bundle additionally retains the original prototype output. No prototype solver status or missing output is promoted to a certificate.

This records why strengthening singleton bounds did not finish the argument and why the SAME exact block-excess total must be used in both the receiver caps and the charge envelope. Earlier block-weight and numerical multiplier failures are separately preserved in `../../2026-09-14-evidence-preservation-v1/`.
