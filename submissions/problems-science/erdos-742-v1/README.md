# Erdős Problem 742 — bounded submission packet v1

Prepared for the problems.science / Vela direct-submission workspace.

## Submission status

This packet presents **bounded candidate results** for the Murty–Simon conjecture / Erdős Problem 742. It does **not** claim a proof of the unrestricted all-order conjecture.

The underlying repository is AI-assisted research directed by Paul Lenz. The proofs, implementations and internal audits were produced in collaboration with ChatGPT/Geeps. Same-assistant reimplementations and green workflows are not external mathematical verification. Independent mathematical review, novelty assessment and independent computational reproduction remain open.

## Exact bounded claim submitted for review

Let `G` be a finite simple diameter-2-critical graph on `n` vertices. For each

```text
n in {25, 27, 28, 29, 30},
```

this project claims

```text
e(G) <= floor(n^2/4),
```

with equality if and only if

```text
G is K(floor(n/2), ceil(n/2)).
```

Equivalently, the five fixed-order claims are:

| n | claimed maximum | claimed equality graph |
|---:|---:|---|
| 25 | 156 | `K(12,13)` |
| 27 | 182 | `K(13,14)` |
| 28 | 196 | `K(14,14)` |
| 29 | 210 | `K(14,15)` |
| 30 | 225 | `K(15,15)` |

**No claim is made here for n=26 or for every n<=30.** The scope is exactly the five displayed orders.

## Frozen research base

The submission packet was branched from repository commit:

```text
6b160b8736bd308bc9373dcc0ae37029712d81de
```

Repository:

```text
https://github.com/paullenz/MurtySimon742
```

Submission branch:

```text
submission/problems-science-742-v1
```

The branch is intended as a stable external-review surface. Later exploratory work on the general-N RX-Hall programme is not part of the bounded claim unless explicitly incorporated in a later submission version.

## Reviewer entry points

Current Fan-free reviewer packages:

- n=25: `releases/n25-reviewer-v2/README.md`
- n=27: `releases/n27-reviewer-v2/README.md`
- n=28: `releases/n28-reviewer-v2/README.md`
- n=29: `releases/n29-reviewer-v2/README.md`
- n=30: `releases/n30-reviewer-v2/README.md`

General reviewer guide:

- `START_HERE_FOR_REVIEWERS.md`

The current fixed-order reviewer-v2 editions do **not** use G. Fan's 1987 upper-density theorem as a logical dependency. The replacement and its internal assembly audit are:

- `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md`
- `project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md`

## Important negative provenance

A genuine normalization bug was found during the hostile audit of an *additional* n=29 cumulative-threshold verifier. The historical v1 cumulative-threshold certificates are invalid as proof evidence and are retained only for audit history. The corrected v2 and the later minimal trusted kernel replay cleanly. Reviewers should not cite the flawed v1 verifier.

This failure history is intentionally included because the submission is intended to be falsifiable and auditable rather than polished by deletion.

## What is and is not evidence

The packet distinguishes:

1. hand mathematical reductions and graph-to-model lemmas;
2. finite necessary-condition systems;
3. exploratory floating-point solver output;
4. exact integer/rational certificates and exact replay;
5. same-assistant reimplementation;
6. genuinely independent external review.

The bounded claims rely on items 1–4. Item 5 is robustness evidence but not independence. Item 6 remains open.

## Recommended review order

For a first mathematical audit, start with n=29. It has the cleanest deliberately reduced graph-to-demand trusted kernel and exposes the main universal bridge explicitly. Once that bridge is accepted or corrected, the n=30 parameterised version and the other fixed-order packages become substantially easier to assess.

A reviewer looking for a fatal flaw should prioritize:

- complement/quasi-edge construction;
- injection and uniqueness of selected edges/supplements;
- residual activity;
- the demand implication;
- charging and threshold-capacity inequalities;
- the graph-to-model bridge;
- exact source-capacity/Hall relaxations;
- the residual-row scanner;
- grouped normalization in the corrected v2 model;
- exact Farkas sign/RHS verification.

## Secondary research, not part of this submitted claim

The repository also contains a candidate general maximum-degree implication

```text
n >= 6 and Delta(G) >= (7/12)n
    ==> e(G) < floor(n^2/4),
```

and an active RX-Hall / staircase programme. These are intentionally **not bundled into this v1 bounded submission**. They should be reviewed separately after the fixed-order bridge has received external scrutiny.

## Files in this packet

- `CLAIM.md` — formal human-readable statement and scope.
- `EVIDENCE_MAP.md` — proof/replay entry points and internal evidence summary.
- `REVIEW_CHECKLIST.md` — hostile-review and reproduction checklist.
- `PASTE_READY_SUBMISSION.md` — concise text for the problems.science workspace.
- `MANIFEST.json` — machine-readable scope/provenance metadata.
