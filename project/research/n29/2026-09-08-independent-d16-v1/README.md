# n=29 Delta=16 — independent late-stage verifier v1

8 September 2026. Prepared during the restarted red-team audit requested by Paul Lenz.

**Status: PASS in the development run; clean-runner publication workflow supplied. Same-assistant independent implementation, not independent researcher reproduction, peer review, or formal verification. The n=29 theorem remains a CANDIDATE.**

## Purpose

The original n=29 Delta=16 exclusion reuses the hash-pinned n=28 direct197 implementation. Its production run is exact and internally checked, but common implementation ancestry is a material trust boundary.

This directory supplies a second implementation of the load-bearing **joint-state and strongest endpoint-certificate stages**. The new runtime source imports no module from the inherited Murty-Simon verifier/model. It was written directly from the graph-theoretic inequalities rederived in the restarted red team.

The aim is not to obtain a different numerical theorem. It is to ask whether the same n=29 Delta=16 contradiction survives a materially different implementation and whether every late-stage exclusion can be preserved as an exact proof object.

## Files

- `fresh_joint.py` — pure-Python independent joint-state engine. Standard library only.
- `fresh_endpoint.py` — independently coded strongest endpoint LP plus exact integer Farkas checker. SciPy is used only to propose a dual ray.
- `run_independent.py` — orchestration, independent boundary recounts, complete joint replay, exact certificate generation and evidence packaging.
- `N29_INDEPENDENT_D16_STATES.json.gz` — generated fresh joint survivors, after the clean workflow publishes evidence.
- `N29_INDEPENDENT_D16_CERTIFICATES.json.gz` — every exact fresh endpoint certificate, after publication.
- `MANIFEST.json` — source/evidence hashes and result summary, after publication.

The generated binary evidence is intentionally not hand-written into GitHub through the text connector. The workflow generates and commits it on the runner so connector payload limits cannot truncate it.

## Independence boundary

The fresh runtime verifier does **not** import or execute the inherited implementations of:

- joint propagation;
- independent joint checking;
- row-support C++;
- shared LP;
- source-degree-type LP;
- endpoint/total-degree LP;
- named Farkas-system reconstruction.

Instead it independently implements the corresponding combinatorics and endpoint relaxation.

There is still an explicit upstream dependency. The workflow uses the existing n=29 preparation route to obtain the retained demand intervals and the initial residual-row survivor file. That early preparation already has separate exact checking and two independent residual scanners in the candidate package, but this v1 does not claim to replace it.

Before trusting those prepared inputs, `run_independent.py` independently checks three large boundaries:

1. it regenerates the complete charging-domain counts using exact rational arithmetic;
2. it independently counts every raw sorted residual profile in the retained demand bands using an integer-partition dynamic program;
3. it independently recomputes the projected filter and requires the actual survivor rows to equal the saved projected set exactly.

Thus the fresh late-stage verifier is not fed a hand-picked list of final cases.

## Fresh joint-state engine

`fresh_joint.py` reimplements the finite propagation using different source code and only Python's standard library. Its ingredients include:

- exact column-total dynamic programming;
- source-to-supplement distinct matching;
- an independently implemented Dinic max-flow for source Hall;
- pair Hall over label subsets;
- a selected/residual/missing three-state row feasibility recurrence using exact bitset dynamic programming;
- iterative source-cap, forced-incidence and column-domain propagation.

The development run reproduced the production joint partition exactly.

At `m=211` (`t=3`), all 118 projected rows divide as:

| disposition | count |
|---|---:|
| survivor | 36 |
| source matching | 38 |
| source Hall | 2 |
| joint total source | 42 |

At `m=210` (`t=2`), all 1,225 projected rows divide as:

| disposition | count |
|---|---:|
| survivor | 593 |
| source matching | 311 |
| source Hall | 29 |
| label domain | 6 |
| total source | 58 |
| joint total source | 222 |
| pair Hall | 6 |

The agreement is row-by-row, not only an aggregate-count comparison.

## Fresh endpoint model

`fresh_endpoint.py` independently encodes the strongest continuous endpoint relaxation directly from the audited graph constraints. Among its variables and constraints are:

- selected/residual/missing source-label incidences;
- residual column totals and F-edge incidences;
- selected source-to-supplement arcs and pair injection;
- supplement forcing;
- exact source selected-degree types;
- source/supplement pair-degree flow;
- source-conditioned residual and F-degree ledgers;
- the source-local criticality bound;
- actual column selected degrees `x_i`;
- source supplement indegrees `p_u`;
- selected-incidence coupling requiring `R_i+x_i >= q_u+p_u`.

The code does not call the production builders or their checkers. It also avoids repeated duplicate `x<=1` rows that arise from the layered construction of the older builder; this changes redundant inequality counts, not the mathematical relaxation.

During development, the two deepest `m=210` rows reproduced the same variable and equality dimensions as the production endpoint model and independently gave exact contradictions with right-hand sides `-830` and `-355`.

## Exact certificate rule

SciPy/HiGHS is allowed to propose a dual ray. A row is not excluded by numerical solver status.

For every alleged contradiction, the fresh checker constructs integer multipliers and verifies exactly that:

- inequality multipliers are nonnegative integers;
- equality multipliers are signed integers;
- the combined coefficient of every nonnegative primal variable is nonnegative;
- the combined right-hand side is strictly negative.

Only then is the row counted as rejected.

The development run generated exact certificates for **all 629 fresh joint survivors**:

- 36/36 at `m=211`;
- 593/593 at `m=210`;
- unresolved rows: **0**.

The least-negative exact right-hand side encountered in the development run was `-10`, so even the tightest accepted contradiction remained an exact strict inequality.

## Independent boundary counts

The orchestration requires the following exact counts before running the fresh joint engine:

| scope | charging tuples | raw residual profiles | projected rows |
|---|---:|---:|---:|
| `m=211`, `t=3` | 4,867 | 1,848,957 | 118 |
| `m=210`, `t=2` | 9,251 | 5,765,218 | 1,225 |

The charging counts are recomputed from

`sum s_i(13-2s_i)/(12-s_i) >= 16+2t`

with exact `Fraction` arithmetic. The residual-profile counts are independently reconstructed by integer partition DP over sorted 16-tuples in `1,...,12`. The projected rows are reconstructed and compared as complete ordered lists.

## Replay

The clean workflow is `.github/workflows/n29-independent-d16.yml`.

It:

1. checks out the repository on Ubuntu 24.04;
2. pins SciPy 1.17.0 and the compiler/checker dependencies used only for preparing the upstream input;
3. verifies the SHA-256 of the inherited direct197 archive before using it for preparation;
4. rebuilds the n=29 prepared `t=3` and `t=2` inputs using the existing preparation/scanner route;
5. invokes only this directory's fresh source for the independent late-stage run;
6. requires every expected joint count and every exact endpoint certificate;
7. writes gzip evidence and a hash manifest;
8. uploads the evidence as a workflow artifact and commits the generated evidence files back to this directory.

The evidence commit is additive. It does not alter the original n=29 candidate proof or governed theorem ledger.

## What this materially improves

This v1 substantially reduces the risk that the n=29 Delta=16 result is an artefact of one inherited joint/LP implementation. It independently reconstructs the joint partition and then proves every one of the 629 late-stage rows infeasible with separately generated exact proof objects.

It also mitigates red-team finding `RT-N29-002`: unlike the original production shard reports, this run preserves every accepted late-stage Farkas certificate in a complete bundle. The historical preservation limitation of the original production artifacts remains accurately recorded; it is not retroactively rewritten.

## What remains open

This is still the same assistant's mathematical and software work. It is therefore **not independent researcher reproduction**.

The principal remaining assurance steps are:

- a separate researcher or independently authored program reproducing the result;
- specialist review of the graph-to-model necessity arguments;
- if desired, a further independent replacement of the *early* demand-support/residual-row preparation so that no inherited prepared input is used at all;
- formal verification of the structural lemmas and/or exact finite certificates.

No theorem-ledger promotion is justified merely by this same-assistant independent implementation.
