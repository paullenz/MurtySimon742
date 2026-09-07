# General structural programme — v9

7 September 2026. **Candidate theorems; independent review and novelty assessment OPEN.** Specialist outreach remains with Paul. No invitation was sent.

## Paper and main results

Read [the standalone paper (PDF)](General_Structural_Theorems_v9.pdf), [editable LaTeX](General_Structural_Theorems_v9.tex), or [the full readable proof](PROOF.md). This paper does not depend on the n25/n27/n28 finite computations.

For a=n-1-Delta and t=m-Delta(n-Delta), the new candidate bound at a>=25 is

```text
t < (3/2 - sqrt(2) - 1/5000) a^2.
```

Including 24 explicit small-a inequalities, the resulting all-order candidate implication is

```text
n >= 4 and Delta >= beta1*n  ==>  e(G) < floor(n^2/4),
c1 = 3/2 - sqrt(2) - 1/5000,
beta1 = (1/2 + sqrt(c1))/(1 + sqrt(c1)) = 0.6131682474535585...
```

The earlier project coefficient was 0.613270459830... . The numerical improvement is modest; the new mechanism is a fixed quadratic loss from shared pair capacity. This is demand-distribution stability, not an edit-distance theorem.

A separate source-class theorem gives `h*ell <= (2h-1)*z` when the maximum residual degree is h>=1 and exactly z sources have that degree, with h<=z<=h^2+h. In particular **h+2 sources support at most 2h+2 demand-h labels for h>=2**. No positive-surplus assumption is required. Reduced incidence sharpness is not actual-graph sharpness.

## Reproduce the supporting checks

From a fresh extracted package or checkout:

```sh
python3 -I -B replay.py --output /absolute/path/to/new-v9-check
```

This verifies the manifest, runs both exact-constants implementations, reconstructs every saved graph system, and repeats the seeded reduced-incidence and exhaustive oriented-graph checks. Only Python's standard library is needed. `--verify-only` reports integrity only; it is not arithmetic replay. The output directory must be new and outside the checkpoint.

Optional `src/graph_checks.py --generate --output NEW_REPORT` regenerates the additional sample and needs NetworkX 3.6.1; run that in a disposable copy because it writes the sample file. Optional exploratory optimisation needs SciPy and is not a proof dependency. No solver, old ZIP or network is required for the default replay.

For the formal slice, use official Lean 4.19.0 and run `lean formal/QuasiCore.lean`. The committed read-only workflow checked five local lemmas successfully. Its downloaded log, source and toolchain hashes are included. The default Python replay verifies those recorded files and their source match; it does not pretend to rerun Lean without a toolchain. Full graph-theoretic formalisation remains OPEN.

## Review and attribution

See [review and handoff](REVIEW_AND_HANDOFF.md), [literature comparison](literature/COMPARISON.md), and [provenance](PROVENANCE.json). The comparison now includes the omitted 2016 preprint; no best-known or priority claim is made. No blocking error was found in the rederived charging theorem, but this is internal scrutiny, not independent acceptance.

The actual-graph tests contain no positive-surplus graph and no nonempty spare class in the new theorem's range. Separate abstract tests exercise exceptional arcs nonvacuously but are not graph examples. Both implementations were developed by the same assistant. Finite tests support the written universal proof rather than proving it by extrapolation.

Frozen finite-order proofs, evidence archives and the governed theorem ledger are unchanged. No additional complete order is claimed. Publication is tracked separately in PUBLICATION_RECEIPT.json once the branch and all files have been verified.
