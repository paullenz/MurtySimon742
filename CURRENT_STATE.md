# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** This is the short durable handoff for restarting research after a chat reset, context loss or client desynchronisation. The repository, not any chat transcript, is the source of truth. Read this file first, inspect commits newer than the research baseline below, then follow the linked canonical packages.

**Research state reconciled:** 13 September 2026 through commit `f32099397985fe104b5112434c458d8261e1d5bd`, including the exact full-domain receiver-containment spill application and audit. If `main` is newer, reconcile every later result, correction or failed experiment before continuing.

External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

## Headline theorem/proof status

- `n=25`: complete candidate, `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2; external specialist review open.
- `n=27`: complete candidate, `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2; external review open.
- `n=28`: complete candidate, `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening; external review open.
- `n=29`: complete candidate, `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed; external review open.
- `n=30`: complete candidate, `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3; hand lemmas plus proof-critical integer tables; external review open.
- `n=31`: complete candidate, `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1; external review open.
- `n=32`: complete candidate, `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1; external review open.
- `n=33`: complete candidate, `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1; external review open.
- `n=34`: complete candidate, `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final large heavy certificate replaced by a short hand argument; external review open.
- `n=35`: complete candidate, `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1; external review open.

These fixed-order candidate proofs are already closed on their own preserved ledgers. General-theory survivor counts below are **not** unresolved fixed-order cases.

## Current general theory

Canonical graph-to-constraint framework: [`project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).

Current candidate general results include:

- all-order balanced-degree reduction and fixed-`a`/tail families in the step-back programme;
- candidate maximum-degree theorem: for `n>=6`, `Delta(G)>=(7/12)n` implies `e(G)<floor(n^2/4)`;
- general heavy-load/routing inequalities for every heavy threshold `h`, including incoming-degree penalties and the low-demand consequence `s_i<=2, t>0, b-a<=5 => 9t+4(b-a)<=a`;
- joint heavy-routing inequalities coupling sender counts, destination indegrees and pair capacity;
- demand/tail projection and equality-rigidity lemmas;
- destination-compatibility inequalities, the full compatible-routing catalogue and the closed compatible potential;
- fixed-neighbourhood B-side routing as an exact integer-flow/Hall criterion once selected/residual cross-neighbourhoods are fixed;
- **co-singleton trace hierarchy:** for every `T subset S_u`, `|T|=k>=1`, exact compatibility forces at least `q_u-k+1` B cross-neighbourhoods containing `T`, yielding higher-order moment inequalities;
- **receiver-containment spill inequality:** a candidate hand projection of the exact condition `S_v subset N_u` to the scalar profile `(a,b,s,rho,q)`.

The co-singleton pair moment is genuinely stronger than endpoint loads on abstract cross data: the preserved five-label/seven-source example satisfies every individual endpoint load but has pair moment `16<18`.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Active generalisation frontier

The joint-routing continuation left `5,578` states in the frozen generalisation pool. The compatible-routing catalogue plus four retained pilot-only witnesses exclude `994` of them, leaving **4,584** states:

- `4,506` N34 equality-derived states;
- `78` N35 `m=306`-derived states.

These are survivors of a proposed general simplification, not surviving graphs and not open N34/N35 proof obligations.

The closed compatible-potential continuation and the fixed-neighbourhood routing-flow pilot add zero whole-state exclusions beyond those 994.

### 13 September constraint-respecting continuation

Current package: [`project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md`](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md). Hand theory: [`CONTAINMENT_SPILL.md`](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/CONTAINMENT_SPILL.md). Audit: [`AUDIT.md`](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/AUDIT.md).

Key findings:

- broad fixed-selected-pattern residual/compatibility searches found no complete compatible cross pattern in the frozen six-state sample, but negative solver statuses are exploratory only and never proof;
- a directly checkable N34 state-60 partial pattern has exact demands/residual source degrees, no minimum endpoint-load violation, and **19 of 37** obligations with nonempty exact compatible-destination sets (20 eligible ordered pairs); 19 is not proved optimal;
- deterministic reconnaissance of the spill inequality cut 173/2,000 selected configurations in N34 state 13537, which motivated the scalar projection;
- the subsequent **complete positive-witness study supersedes any extrapolation from that sample**: [`FULL_DOMAIN_SPILL_EXACT.json`](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/FULL_DOMAIN_SPILL_EXACT.json) contains one directly checked witness for **every one of the 4,584 survivors**, with `x_i=s_i` exactly, satisfying source eligibility/capacity, selected/incoming balance, all preserved nested transport inequalities, scalar candidate-receiver counts and the spill inequality;
- complete result: `4,584` witnessed, `0` unresolved, **0 whole-state exclusions added**, minimum receiver margin `0`, minimum spill slack `0`.

This is an exact **limit result for the scalar spill projection**. It does not construct residual sets, actual compatible destinations, heavy-H data, Hall routings or graphs. The frontier therefore remains **994 exclusions / 4,584 survivors**.

## Most important unresolved correctness obligations

1. **External review of the shared foundations/canonical bridge.** Many later results share graph-to-model implications, so this is the main correlated correctness risk.
2. External review and novelty assessment of the candidate `7/12` theorem and the other general lemmas, including the co-singleton/containment-spill results.
3. Independent reproduction of proof-critical computations where a reviewer regards them as material.
4. Continue preserving failures, counterexamples to proposed lemmas, bugs, corrections and negative experiments. Never treat a timeout, solver noncompletion or raw infeasibility status as proof.

## Current research diagnosis

The scalar selected-degree projection has now reached a clear limit on the current frontier. Exact destination compatibility contains information that the scalar routing models discard:

```text
S_u \ N_(w_i)={i},
S_(w_i) subset N_u.
```

Across the `q_u` distinct exceptions of a single source, the first condition forces every co-singleton trace of `S_u`; equivalently, every selected `k`-subset must occur in at least `q_u-k+1` B cross-neighbourhoods. The second condition couples those exception rows back to `N_u`.

The spill inequality retains part of the second condition but loses the actual label overlaps. The complete 4,584-witness result shows that this loss is now decisive: further tuning of this scalar spill bound is low priority. The next progress must retain set-overlap information, beginning with pair (`k=2`) traces and residual-compatible realization.

## Next three research tasks — priority order

### P1. Pair-overlap / co-singleton projection

Develop the first genuinely set-sensitive consequence of the co-singleton trace lemma. Start with `k=2`.

For a source `u`, its `q_u` distinct exception rows must collectively contain each pair in `S_u` at least `q_u-1` times when the source row itself is included, and at least `q_u-2` times among the exception rows alone. Seek a global capacity bound using selected/residual pair incidences across B, distinguishing:

- selected-selected pair capacity;
- selected-residual mixed pair capacity;
- residual-residual pair capacity;
- the receiver-containment restriction `S_v subset N_u`.

The goal is a hand inequality retaining enough label-overlap information to be stronger than the exhausted scalar spill projection. Prove it before using finite data; then challenge it on abstract cross-data examples and the preserved frontier.

### P2. Exact residual-compatible construction on a frozen sample

Take the exact-demand spill-surviving selected patterns from a small frozen heterogeneous sample. Search residual placements satisfying endpoint loads and **exact** destination compatibility before final Hall routing. Preserve raw solver outcomes only as exploratory evidence.

For any failed pattern, extract a checkable combinatorial obstruction—preferably a pair/triple overlap deficit or a Hall-type cut on residual labels. For any successful pattern, apply the exact fixed-neighbourhood flow and inspect the next missing graph condition.

### P3. Complete-domain application of any new set-level cut

Only after P1/P2 identify a checkable set-level inequality, apply it to the complete preserved 4,584-state domain. Quantify local-configuration cuts and whole-state exclusions separately. Preserve zero-gain outcomes. Use N36 only as a structural laboratory, not as the primary objective.

## Research/preservation rules for every continuation

The standing orders in [`project/N25_PROJECT_STANDING_ORDERS.md`](project/N25_PROJECT_STANDING_ORDERS.md) remain binding. In particular:

- a chat transcript must never be the sole durable record of material work;
- preserve code, exact parameters, inputs, outputs, survivor lists, hashes, commands, certificates and environment information where applicable;
- record unsuccessful searches and invalidated arguments rather than deleting them;
- distinguish mathematical proof status, exact replay, internal audit, publication and external review;
- update `README.md` and reviewer entry points when a material frontier or theory change occurs;
- verify committed paths and reviewer/version consistency after publication;
- routine research commits to `paullenz/MurtySimon742` `main` are authorised without asking again; use non-forced updates.

## Restart protocol

On a fresh chat/session:

1. open this file;
2. inspect `main` commits newer than the research baseline recorded at the top;
3. reconcile any later result, correction or failed experiment into this handoff;
4. read the latest linked reviewer/research package relevant to the active task;
5. continue from the first unfinished priority above rather than reconstructing status from conversational memory;
6. after material progress, update this file in the same repository-writing pass.

For the fuller reviewer-facing map, use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).
