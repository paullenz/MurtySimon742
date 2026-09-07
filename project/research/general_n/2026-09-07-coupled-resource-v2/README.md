# General-order coupled attack — research version 2

7 September 2026. Paul Lenz / ChatGPT-Geeps. **Candidate mathematical work; independent review OPEN.** No complete order above 27 is claimed, and no frozen n=25/n=27 file or governed theorem-ledger status is changed.

## Main progress

The new residual charging argument gives a candidate all-order degree threshold

`Delta >= ((10-sqrt(2))/14)n = 0.6132704598... n`

for a strict edge bound below `floor(n^2/4)`, at n>=4. Unlike version 1's 0.630601937... argument, this coefficient proof does not require the residual-activity lemma.

With residual activity, an exact rational inequality is made strict by a uniform source–supplement pair-shortage proof. At n=31, Delta=18, equality would require 48 selected edges but supply only 15 distinct pairs. The first-stage screen now leaves only Delta=16 at n=29 and only Delta=17 at n=31. These remaining cases are NOT resolved here.

A generic coupled resource separator and two exact checkers are implemented. Source, source–label, unordered-pair and supplement budgets are coupled. On one stored hard n=27 profile, a demand-four label has no permissible supplement, yielding the checked contradiction 4>0. This is a regression on an already-rejected profile, not a completed new order.

## Start here

Read `PROOF.md` for the full charging proof, all-order coefficient, strict equality obstruction, supplement degree identity and weighted certificate theorem. Read `REPORT.json` for exact scope, test counts, hashes and limitations. `EVIDENCE.json.gz.b64` preserves the actual output JSON files and logs, including every seeded graph adjacency list and all scalar exclusion records; it is not only a hash reference.

The source files are `coupled.py`, `verify_certificate.py`, `test_coupled.py` and `replay.py`. The two checkers use different matching algorithms but were both developed by the same assistant. This is not independent authorship or independent expert review.

## Replay

From this folder, with Python 3.10 or later:

```
python3 -B replay.py
python3 -B replay.py --full
```

The default replay checks the compressed evidence, exact scalar results and both certificate checkers. The full replay additionally repeats all graph, abstract-incidence and domain-comparison tests in a temporary directory and compares the resulting test evidence byte-for-byte. Do not use `-O` or `PYTHONOPTIMIZE`: the test harness deliberately relies on assertions and rejects optimized execution.

Neither replay needs SciPy. Optional coefficient discovery uses SciPy:

```
python3 coupled.py --discover --output new_results.json
```

The recorded discovery used CPython 3.13.5 and SciPy 1.17.0. Discovery coefficients from another solver version may differ; only exact certificate verification determines acceptance. Solver timeouts and numerical infeasibility messages are never proof certificates.

## Scope and next target

The engine is a fractional-relaxation separator, not a complete integer-branching solver or exhaustive degree-profile enumerator. No positive-surplus actual graph occurred in testing. Finite tests do not prove universal graph lemmas.

The remaining attack is the near-half-degree region. The new strictness theorem suggests a quantitative stability target: extend the shortage beyond exact maximizing profiles. Complete profile coverage, justified branching, shared-adjacency constraints and external mathematical review remain separate open obligations.

Version 1 is preserved at `project/research/general_n/2026-09-07-residual-hindex-v1/`, commit `4bd48b12c6f5953af92adcb614f509b2aa06391a`. The preliminary scalar exploration is retained as `explore_scalar.py` and is not a proof verifier. No novelty or priority claim is made.
