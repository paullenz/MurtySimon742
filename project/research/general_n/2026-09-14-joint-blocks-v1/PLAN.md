# Joint-block continuation: documented starting point

14 September 2026. This file records the programme BEFORE new research experiments. Proposed statements below are not results. Canonical repository: `paullenz/MurtySimon742`.

## Verified starting point

The conditioned-excess proof, executed verifier and frozen full-output hash are preserved in [the conditioned package](../2026-09-14-conditioned-excess-v1/README.md). It rejects sampled rows 295, 365 and 570, retaining nine rows 108,160,240,258,338,342,347,471,586. The cumulative original 713-profile sample therefore has 704 rejections, not 704 new whole-state exclusions. Row 295 has both the hand equality contradiction 10>8 and a conditional price certificate.

The [publication audit](../2026-09-14-evidence-preservation-v1/PUBLICATION_AUDIT.md) now confirms durable data in commit `b6a15db114d7b4f3b71d73da816daec563f11824`. Publication-only run 34895776658, job104149243135, was directly checked and completed SUCCESS. It reused verified artifacts; it did not rerun the 256-shard audit. The earlier run34894544147 passed its exact mathematical/hash checks but failed its Git rebase because the checkout was unclean. Keep that old run classified as failed publication, not failed mathematics, and do not relabel its whole run green. The repair and failure are both preserved.

All recent original inputs, full conditioned output including unsuccessful branches, nine remaining arrays, prior complete capped/block outputs, historical capped-spill outputs and provenance manifest are now in [durable/](../2026-09-14-evidence-preservation-v1/durable/). The existing root [evidence index](../../../../RESEARCH_EVIDENCE_INDEX.md) and [handoff](../../../../CURRENT_STATE.md) remain the restart navigation. This is preservation of the recent research scope, not external review of every historical manuscript.

## Ordered research obligations

1. Generalize the row-295 tight-block argument quantitatively: bound the total pressure of a source group when only J additional selections can enter a low-demand block. Derive every inequality directly from a single actual incidence matrix and one shared excess vector. A group charge must not spend the same label excess once per source without accounting for multiplicity.
2. Condition on several nested demand-block excess totals simultaneously. Bounds for different blocks must use the same vector. Enumerate all allowed block totals or provide an exact coverage argument; never choose only a favourable split. Preserve any negative result of this stronger projection.
3. Where useful, impose common source usage across label upper bounds. Independent top-source choices remain only an upper relaxation. Distinguish finding an incidence matrix from realizing the canonical residual matrix/F-graph/quasi-edge system.
4. Immediately test candidate inequalities on actual small selected-incidence systems (including zero demands, empty/full blocks and positive slack), then the nine retained synthetic rows and fresh synthetic inputs. Use independent integer/brute-force comparisons and retain all counterexamples. A sample count is reconnaissance, not an all-order theorem.

## Invariants and audit boundary

Keep Q=r+2t+D0+Esel, with structural t, q-threshold tau and label-block threshold eta. All zero-demand labels belong to any block whose complement uses positive-label endpoint forcing. Do not assume z<=Esel. Retain every legitimate cap, especially potential-pair degrees; negative caps reject branches rather than being clipped.

Canonical promoted frontier remains 1971 exclusions / 3607 survivors / 977 whole-state closures. Do not promote the2655 relational candidates: exact coverage, both implementations agreeing, zero unresolved, a successful aggregate and a separate reviewed ledger step are required. Their live monitoring remains separate from this hand argument. No audit restarts, timeout-budget changes, concurrency changes or weakened hashes are authorized by this plan.

Internal derivation, separately structured finite arithmetic, successful CI/publication and external mathematical acceptance are different evidence classes. The selected/residual graph bridge remains the principal correlated external-review dependency.
