# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** This is the short durable handoff for restarting research after a chat reset, context loss or client desynchronisation. The repository, not any chat transcript, is the source of truth. Read this file first, inspect commits newer than the research baseline below, then follow the linked canonical packages.

**Research state reconciled:** 13 September 2026 through commit `882a43fa222e890537d34c044ee5f0877b61210a`, including the constraint-respecting cross-neighbourhood continuation and its co-singleton/containment-spill theory. If `main` is newer, reconcile every later result, correction or failed experiment before continuing.

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
- **receiver-containment spill inequality:** a candidate hand projection of the exact condition `S_v subset N_u` to the scalar profile `(a,b,s,rho,q)`. For source `u`, actual selected mass outside `N_u` is bounded below from demand/eligibility totals and above by the maximum outside mass that can be placed while retaining `q_u` contained candidate receivers.

The co-singleton pair moment is genuinely stronger than endpoint loads on abstract cross data: the preserved five-label/seven-source example satisfies every individual endpoint load but has pair moment `16<18`.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Active generalisation frontier

The joint-routing continuation left `5,578` states in the frozen generalisation pool. The compatible-routing catalogue plus four retained pilot-only witnesses exclude `994` of them, leaving **4,584** states:

- `4,506` N34 equality-derived states;
- `78` N35 `m=306`-derived states.

These are survivors of a proposed general simplification, not surviving graphs and not open N34/N35 proof obligations.

The closed compatible-potential continuation adds zero new exclusions beyond those 994. The fixed-neighbourhood routing-flow pilot also adds zero whole-state exclusions.

The 13 September constraint-respecting continuation likewise adds **zero whole-state exclusions so far**. Its key bounded findings are:

- broad fixed-selected-pattern residual/compatibility searches found no complete compatible cross pattern in the frozen sample, but negative solver statuses are preserved only as exploratory evidence, never proof;
- a directly checkable N34 state-60 partial pattern has exact demands/residual source degrees, no minimum endpoint-load violation, and **19 of 37** obligations with nonempty exact compatible-destination sets (20 eligible ordered pairs); 19 is not proved optimal;
- deterministic reconnaissance of the new spill inequality on 2,000 exact-demand selected patterns per frozen state cuts **173/2,000** patterns (183 source-level violations) in N34 state 13537 and zero in the other five sampled states. This is not exhaustive state coverage.

Current continuation: [`project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md`](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/README.md). Hand theory: [`CONTAINMENT_SPILL.md`](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/CONTAINMENT_SPILL.md).

## Most important unresolved correctness obligations

1. **External review of the shared foundations/canonical bridge.** Many later results share graph-to-model implications, so this is the main correlated correctness risk.
2. External review and novelty assessment of the candidate `7/12` theorem and the other general lemmas, including the new trace/spill projection.
3. Independent reproduction of proof-critical computations where a reviewer regards them as material.
4. Continue preserving failures, counterexamples to proposed lemmas, bugs, corrections and negative experiments. Never treat a timeout, solver noncompletion or raw infeasibility status as proof.

## Current research diagnosis

The main obstacle is structural rather than raw finite arithmetic. Exact destination compatibility contains information that the earlier scalar routing models discard: an actual exception `w_i` must satisfy both

```text
S_u \ N_(w_i)={i},
S_(w_i) subset N_u.
```

The first condition creates all co-singleton traces of `S_u`; the second creates receiver-containment pressure. The new spill inequality is the first hand projection found in this continuation that retains part of that second condition while eliminating the actual label sets.

This is the best immediate avenue because it can be tested against the complete preserved `q`/source-option domain without constructing full cross-neighbourhoods.

## Next three research tasks — priority order

### P1. Exact full-domain spill integration

Add the receiver-containment spill inequality to the **complete preserved selected-degree/source-option domain** underlying the 4,584 compatible-routing survivors. Use exact integer arithmetic and complete coverage, not randomized sampling.

Determine separately:

- how many local `q` configurations the new cut removes;
- whether any whole states lose every admissible `q` configuration;
- whether the cut strengthens the recurring/closed compatible potential even where it does not exclude a whole state.

Preserve the full before/after domain, exact witnesses and all zero-gain results. Do not count a state exclusion unless every admissible branch is covered.

### P2. Extract a simpler demand/tail consequence

If P1 produces exact exclusions, inspect the first and most common spill witnesses for a projection eliminating `q` as well. Seek a hand inequality in `s,rho,a,b,t` or residual tails analogous to earlier successful certificate-to-theory reductions.

Also test the higher-order trace moments (`k=2` first) on the complete domain. Their usefulness should be judged by exact coverage, not sample frequency.

### P3. Return to constructive cross-neighbourhood/Hall search with the new cuts

After applying the new profile cuts, resume complete-compatible-cross construction on a small frozen heterogeneous sample. Require endpoint loads and at least one exact compatible destination before routing; then apply the exact Hall flow. A successful cross pattern or a genuinely collective Hall deficit is valuable. Use N36 only as a structural laboratory, not as the primary target.

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
