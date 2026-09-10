# Paste-ready problems.science submission text

## Suggested title

Bounded Murty-Simon verification at orders 25, 27, 28, 29 and 30

## Claim / contribution summary

I am submitting a bounded candidate result for Erdős Problem 742 (the Murty-Simon conjecture), not a claim to have proved the unrestricted conjecture.

For every finite simple diameter-2-critical graph `G` on

```text
n in {25,27,28,29,30},
```

the submitted proof packages claim

```text
e(G) <= floor(n^2/4),
```

with equality if and only if

```text
G ≅ K(floor(n/2),ceil(n/2)).
```

Explicitly, the claimed maxima/equality cases are:

```text
n=25: 156, equality K(12,13)
n=27: 182, equality K(13,14)
n=28: 196, equality K(14,14)
n=29: 210, equality K(14,15)
n=30: 225, equality K(15,15)
```

This submission does **not** claim the result for every `n<=30` and makes no new claim for `n=26`.

## Evidence

The public research repository is:

```text
https://github.com/paullenz/MurtySimon742
```

The frozen submission branch is:

```text
submission/problems-science-742-v1
```

It was branched from research commit:

```text
6b160b8736bd308bc9373dcc0ae37029712d81de
```

Please begin with:

```text
START_HERE_FOR_REVIEWERS.md
releases/REVIEW_READY_INDEX.md
submissions/problems-science/erdos-742-v1/README.md
submissions/problems-science/erdos-742-v1/EVIDENCE_MAP.md
submissions/problems-science/erdos-742-v1/REVIEW_CHECKLIST.md
```

Each submitted order has a current reviewer-v2 manuscript and verification companion under `releases/`. The current fixed-order editions are Fan-free: G. Fan's 1987 upper-density theorem is retained as historical attribution but is not a logical dependency of these five proofs. The replacement upper-range argument and internal hostile assembly audit are in:

```text
project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md
project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md
```

The finite computational exclusions use exact integer/rational certificate checks. Floating-point solver status is used, where applicable, only to propose certificate data and is not itself treated as a proof event.

## Review boundary / known failure history

This is AI-assisted candidate mathematics. Paul Lenz directed the project and research priorities; ChatGPT/Geeps supplied much of the mathematical development, code, manuscripts and internal audits. Same-assistant reimplementations are useful robustness evidence but are not independent external verification.

A genuine normalization bug was found during hostile auditing of an additional n=29 cumulative-threshold verifier. Its historical v1 certificates are explicitly invalid as proof evidence and remain in the repository only for audit provenance. The corrected v2 model and a smaller minimal trusted kernel replay cleanly. The current reviewer surfaces identify the valid route and the known-bad historical route unambiguously.

The highest-value external review target is the universal graph-to-residual / graph-to-demand bridge. Exact machine replay verifies the finite arithmetic conditional on that bridge; it does not replace an independent mathematical audit of it.

## Requested disposition

Please assess this as a **bounded contribution** for the five stated orders only. I would particularly welcome:

- a counterexample to any universal bridge lemma;
- an independent implementation/replay of the exact certificate logic;
- correction of any literature or novelty claim;
- formal verification of any part of the bridge or fixed-order arguments.

No unrestricted resolution of Erdős Problem 742 is asserted by this submission.
