# Frozen checkpoint: n=29 reviewer-v4

Frozen 11 September 2026 after the reviewer-v4 hostile audit and hardening rebuild.

## Canonical frozen pointer

Use the immutable review snapshot branch:

```text
frozen/n29-reviewer-v4-2026-09-11
```

which points to commit

```text
3b85bef1860a78701b1ff610e163b21cc5598a0a
```

(commit message: `Publish N29 reviewer-v4 hand-proof package`).

This branch is to remain untouched unless an external reviewer identifies a substantive mathematical defect requiring a new edition. New research should proceed on `main` without rewriting this checkpoint.

## Frozen claim

```text
e(G) <= 210,
with equality exactly K(14,15).
```

Status remains **candidate mathematics** pending independent expert review.

## Frozen package hashes

From `releases/n29-reviewer-v4/MANIFEST.json` at the frozen commit:

```text
N29_Reviewer_Manuscript_v4.md
  sha256 13f5850aaeebaf9e040f25fbd3bbdaa8a4879424995d3ace0f4061b149670677
N29_Reviewer_Manuscript_v4.pdf
  sha256 09f2bb8a9689d503c419133f4eb29c3a84774a700a9f81b9a2624ac890505051
N29_Verification_Companion_v4.md
  sha256 981167e2e9c7a14dda97ae08a3ef4724e251df180b006e05f45aa60494f8c04e
N29_Verification_Companion_v4.pdf
  sha256 0efbce45dd69b4069868088134b7b0a4ccb0ab99e8946180474bcc6e2b01cbf6
README.md
  sha256 d19aca9a144b1164d252db34ba4da7c2acef51f595a0d2faeaea0723b469aff0
```

## Audit status at freeze

- reviewer-v4 package build/preflight: green;
- dedicated hostile-audit exact run `34621982241`: PASS;
- hostile audit verdict: no blocking flaw found;
- Delta=16 logical route: hand threshold-tail argument, no proof-critical finite computation;
- historical minimal-kernel/Farkas route retained only as corroboration;
- independent mathematical review and novelty assessment: OPEN.

## Preservation rule

Do not edit the frozen branch. If future work changes the n=29 proof materially, create a reviewer-v5 (or later) successor and preserve reviewer-v4 unchanged.
