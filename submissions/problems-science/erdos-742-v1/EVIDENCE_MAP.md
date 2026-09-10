# Evidence map — bounded Erdős 742 submission v1

This file maps the five submitted fixed-order claims to their current reviewer-facing proof and replay surfaces.

## Canonical reviewer index

Start with:

```text
releases/REVIEW_READY_INDEX.md
START_HERE_FOR_REVIEWERS.md
```

All five submitted fixed-order claims use the current **Fan-free reviewer-v2** editions. Historical reviewer-v1 editions are preserved for provenance but are not the preferred proof surface.

---

## n=25

Claim:

```text
e(G) <= 156; equality exactly K(12,13).
```

Reviewer package:

```text
releases/n25-reviewer-v2/README.md
releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf
releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf
```

Current proof surface:

```text
project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md
```

Internal replay summary recorded by the root project status:

```text
16 disjoint clean-runner shards
543,578 outer states
3,442,212 labelled columns
1,959 independently reconstructed final equality certificates
```

Status: candidate theorem; independent specialist review open.

---

## n=27

Claim:

```text
e(G) <= 182; equality exactly K(13,14).
```

Reviewer package:

```text
releases/n27-reviewer-v2/README.md
releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf
releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf
```

Current proof surface:

```text
project/reviews/n27/2026-09-09-fan-free-v2/PROOF.md
```

Internal hardened replay summary:

```text
80,978,546 canonical columns checked
35,435 terminal source-cap vectors independently reconstructed
```

Status: candidate theorem; independent review open.

---

## n=28

Claim:

```text
e(G) <= 196; equality exactly K(14,14).
```

Reviewer package:

```text
releases/n28-reviewer-v2/README.md
releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf
releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf
```

Current proof surface:

```text
project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex
```

Important direct lower-band component:

```text
project/research/general_n/2026-09-07-direct-197-v8/README.md
```

The direct `(n,Delta,m)=(28,15,197)` calculation records:

```text
787 shared certificates
790 source-degree-type certificates
7 endpoint-type certificates
0 survivors
```

The historical direct-v8 note still describes Fan's bound in its original proof context. For the submitted theorem, use the reviewer-v2 Fan-free edition and the common Fan-free replacement below.

Status: candidate theorem; internal hostile audit passed; independent review open.

---

## n=29

Claim:

```text
e(G) <= 210; equality exactly K(14,15).
```

Reviewer package:

```text
releases/n29-reviewer-v2/README.md
releases/n29-reviewer-v2/N29_Reviewer_Manuscript_v2.pdf
releases/n29-reviewer-v2/N29_Verification_Companion_v2.pdf
```

Current proof:

```text
project/reviews/n29/2026-09-09-fan-free-v2/PROOF.md
```

Preferred graph-to-model review surface:

```text
project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md
project/reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md
project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md
```

Preferred minimal trusted kernel:

```text
project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json
project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_prepare.py
project/reviews/n29/2026-09-08-redteam-restart-v1/minimal_rows.cpp
project/reviews/n29/2026-09-08-redteam-restart-v1/independent_threshold_model_v2.py
project/reviews/n29/2026-09-08-redteam-restart-v1/run_minimal_kernel.py
.github/workflows/n29-minimal-kernel.yml
```

Minimal-kernel summary:

| edge count | t | retained demand profiles | residual rows | exact late rejections | survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

Every late exclusion is checked with exact integer Farkas arithmetic. Floating-point LP output is proposal machinery, not the proof event.

### Known invalid historical route

The first additional cumulative-threshold verifier `independent_threshold_model.py` contained a grouped normalization error and its v1 certificates are **invalid as proof evidence**. Use `independent_threshold_model_v2.py` and/or the minimal trusted kernel. The flawed v1 remains preserved only for audit history.

Status: complete fixed-order candidate; independent mathematical review open.

---

## n=30

Claim:

```text
e(G) <= 225; equality exactly K(15,15).
```

Reviewer package:

```text
releases/n30-reviewer-v2/README.md
releases/n30-reviewer-v2/N30_Reviewer_Manuscript_v2.pdf
releases/n30-reviewer-v2/N30_Verification_Companion_v2.pdf
```

Current proof:

```text
project/reviews/n30/2026-09-09-fan-free-v2/PROOF.md
```

Candidate package / assembly audit:

```text
project/reviews/n30/2026-09-09-candidate-v1/README.md
project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md
```

Key exact replay summary:

```text
Delta=17, 226 edges:
  250 / 250 charging-feasible profiles threshold-rejected.

Delta=17, 225 edges:
  1,137 profiles rejected by threshold/source-count cuts;
  remaining 18 rejected by exact Hall duals.
  clean replay: 34292054922.

Delta=16:
  parameterised stripped kernel at (a,b)=(13,16);
  clean runs: 34286806474, 34287440190, 34287739057;
  9 final rows at 226 edges and 272 at 225 edges;
  all final rows rejected by exact integer Farkas certificates.

Final assembly replay:
  34292557008 — green.
```

Status: complete fixed-order candidate; independent review open.

---

## Common Fan-free upper-range replacement

The current five submitted proofs do not logically depend on Fan's 1987 density theorem.

Use:

```text
project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md
project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md
project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT_REPORT.json
```

The internal hostile assembly audit checks complete upper edge-range coverage, zero survivors at required exact checkpoints, exact-certificate flags, absence of residual logical Fan invocation from v2 proof surfaces, and integrity of historical source hashes. It reports an internal PASS. This is not external validation.

---

## Evidence excluded from the bounded submission

The following may be scientifically relevant but are **not dependencies of the five-order claim**:

```text
general 7/12 maximum-degree candidate
RX-Hall / pairwise staircase research programme
n=29 t=2 five-template potential compression
other exploratory floating-point scans
```

They remain in the repository for future work and separate review.
