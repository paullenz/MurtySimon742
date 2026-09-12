# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** This is the short durable handoff for restarting research after a chat reset, context loss or client desynchronisation. The repository, not any chat transcript, is the source of truth. Read this file first, then inspect commits newer than the baseline below, then follow the linked canonical reviewer/research packages.

**State reconstructed:** 13 September 2026 from public `main` through commit `a4e025e88432953d3a51b7cb5c1f30aa990ee5ff` (`Record verified publication of the fixed-neighbourhood routing flow criterion`). If `main` is newer, reconcile this file against all later commits before continuing.

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
- destination-compatibility inequalities and the full compatible-routing catalogue;
- closed compatible potentials with an exact local-maxima reduction;
- fixed-neighbourhood B-side routing as an exact integer-flow/Hall criterion once selected/residual cross-neighbourhoods are fixed.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Active generalisation frontier

The joint-routing continuation left `5,578` states in the frozen generalisation pool. The compatible-routing catalogue plus four retained pilot-only witnesses exclude `994` of them, leaving **4,584** states:

- `4,506` N34 equality-derived states;
- `78` N35 `m=306`-derived states.

These are survivors of a proposed general simplification, not surviving graphs and not open N34/N35 proof obligations.

The closed compatible-potential continuation adds **zero** new exclusions beyond those 994. Its value is the exact general formula and analytic reduction.

The fixed-neighbourhood routing-flow pilot also adds **zero** whole-state exclusions. All 12 solver attempts on six frozen survivors timed out without an incumbent. Twelve deterministic fixed-cross probes have exact Hall obstructions, but every one already violates minimum endpoint-load constraints; they therefore demonstrate no new strength over the previous frontier bounds.

Canonical latest package: [`releases/general-arc-realisation-reviewer-v1/README.md`](releases/general-arc-realisation-reviewer-v1/README.md).

## Most important unresolved correctness obligations

1. **External review of the shared foundations/canonical bridge.** Many later results share graph-to-model implications, so this is the main correlated correctness risk.
2. External review and novelty assessment of the candidate `7/12` theorem and the other general lemmas.
3. Independent reproduction of proof-critical computations where a reviewer regards them as material.
4. Continue preserving failures, counterexamples to proposed lemmas, bugs, corrections and negative experiments. Never treat a timeout, solver noncompletion or floating infeasibility report as proof.

## Current research diagnosis

The main obstacle is now structural rather than raw finite arithmetic. Fixed-order proving through N35 is strong enough that the highest-value work is to explain why the finite machinery succeeds and project those explanations to parameter-uniform statements.

The latest routing theorem separates two questions:

1. choose selected/residual cross-neighbourhoods satisfying the earlier graph-derived constraints;
2. for those fixed sets, route all selected incidences via the exact compatibility/flow criterion.

The first bounded pilot failed because its deterministic cross-pattern construction did **not** enforce minimum endpoint loads or nonempty compatible destinations before testing routing. The next experiment must correct that design rather than merely spend more solver time on the old formulation.

## Next three research tasks — priority order

### P1. Constraint-respecting cross-neighbourhood construction

Freeze a small heterogeneous sample from the 4,584 survivor pool, including N34 and N35 states and materially different demand/residual profiles. Construct cross-neighbourhoods while enforcing, before any routing test:

- exact selected/residual source degrees;
- the preserved source/demand restrictions;
- all minimum endpoint-load inequalities;
- at least one genuinely compatible destination/exception for every selected incidence;
- the fixed-neighbourhood pair-compatibility conditions;
- any already-proved heavy-source/destination restrictions that are logically prior to routing.

Then apply the exact fixed-neighbourhood integer-flow/Hall test. Preserve the frozen sample, constructor, every outcome and every failed attempt. A fixed-pattern obstruction is not a whole-state exclusion unless the search quantifies over the full admissible pattern domain.

### P2. Extract a profile-level Hall inequality

For any nontrivial failed routing instance, study the deficient Hall set as a mathematical object. Seek a bound on the union of compatible destination sets using only profile data such as `s`, `rho`, `a`, `b`, `t`, heavy-sender counts and existing tail variables. The target is a parameter-uniform hand lemma eliminating cross-neighbourhood variables, not merely another finite certificate.

A successful routing instance is also useful: inspect which structural feature permits routing and identify the next missing graph constraint.

### P3. Use later orders only as structural laboratories

Do not make N36 the primary target merely to extend the finite sequence. Attack N36 (or later orders) when it provides a clean testbed for a new general mechanism, a boundary case for a proposed lemma, or a way to falsify an over-generalisation.

## Research/preservation rules for every continuation

The standing orders in [`project/N25_PROJECT_STANDING_ORDERS.md`](project/N25_PROJECT_STANDING_ORDERS.md) remain binding. In particular:

- a chat transcript must never be the sole durable record of material work;
- preserve code, exact parameters, inputs, outputs, survivor lists, hashes, commands, certificates and environment information where applicable;
- record unsuccessful searches and invalidated arguments rather than deleting them;
- distinguish mathematical proof status, exact replay, internal audit, publication and external review;
- update `README.md` and reviewer entry points when a material frontier change occurs;
- verify committed paths and reviewer/version consistency after publication;
- routine research commits to `paullenz/MurtySimon742` `main` are authorised without asking again; use non-forced updates.

## Restart protocol

On a fresh chat/session:

1. open this file;
2. inspect `main` commits newer than the baseline recorded at the top;
3. reconcile any later result, correction or failed experiment into this handoff;
4. read the latest linked reviewer/research package relevant to the active task;
5. continue from the first unfinished priority above rather than reconstructing status from conversational memory;
6. after material progress, update this file in the same repository-writing pass.

For the fuller reviewer-facing map, use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).