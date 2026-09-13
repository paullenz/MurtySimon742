# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** This is the short durable handoff for restarting research after a chat reset, context loss or client desynchronisation. The repository, not any chat transcript, is the source of truth. Read this file first, inspect commits newer than the research baseline below, then follow the linked canonical packages.

**Research state reconciled:** 13 September 2026 through commit `3bfce1b71f061e1709193cbd1b6c24bf5df0edf5` (13 September, 01:19 BST), including the complete scalar-spill limit result, the pair-overlap/residual-cover hand lemmas and their frozen exact replay. This handoff update reconciles existing evidence; it adds no new mathematical or computational result. If `main` is newer, reconcile every later result, correction or failed experiment before continuing.

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
- **receiver-containment spill inequality:** a candidate hand projection of the exact condition `S_v subset N_u` to the scalar profile `(a,b,s,rho,q)`;
- **pair-overlap / residual-cover inequalities:** for fixed selected sets, subtract selected-selected coverage from required pair traces and bound how many remaining pair deficits each source's residual labels can cover. The local maxima currently discard residual-label budgets shared across sources.

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

### Latest pair-overlap / residual-cover replay

[Hand lemmas](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/PAIR_OVERLAP.md);
[exact frozen output](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/PAIR_OVERLAP_CHECK.json);
[checker](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/check_pair_overlap.py).

| Quantity | Recorded result |
|---|---|
| Stored selected patterns checked | 4,584, one per combined survivor |
| Initial raw pair-moment failures | 23 |
| Degree-preserving pair repairs | All 23; at most three switches each |
| Local residual-cover failures on the resulting frozen patterns | 26; minimum slack -87 |
| Whole-state exclusions added | 0 |
| Combined frontier | 994 exclusions / 4,584 survivors |

The raw pair test has a passing selected-pattern witness for every state.
The stronger local residual-cover failures exclude only the 26 listed fixed
selected realizations. The replay does not quantify all admissible selected
sets or prove any state impossible. The hand note reports additional
search-assisted repairs of individual examples; those are separate from the
frozen replay and do not change its counts.

## Most important unresolved correctness obligations

1. **External review of the shared foundations/canonical bridge.** Many later results share graph-to-model implications, so this is the main correlated correctness risk.
2. External review and novelty assessment of the candidate `7/12` theorem and the other general lemmas, including the co-singleton, containment-spill and pair-overlap/residual-cover results.
3. Independent reproduction of proof-critical computations where a reviewer regards them as material.
4. Continue preserving failures, counterexamples to proposed lemmas, bugs, corrections and negative experiments. Never treat a timeout, solver noncompletion or raw infeasibility status as proof.

## Current research diagnosis

The scalar selected-degree projection has now reached a clear limit on the current frontier. Exact destination compatibility contains information that the scalar routing models discard:

```text
S_u \ N_(w_i)={i},
S_(w_i) subset N_u.
```

Across the `q_u` distinct exceptions of a single source, the first condition forces every co-singleton trace of `S_u`; equivalently, every selected `k`-subset must occur in at least `q_u-k+1` B cross-neighbourhoods. The second condition couples those exception rows back to `N_u`.

The complete spill study shows that this scalar projection cannot eliminate any current survivor. The pair continuation now retains actual label overlaps, but the raw pair test can also be satisfied in every state by rearranging selected labels without changing their degree data. The stronger local residual-cover bound rejects 26 fixed patterns; its reach over all admissible geometries is still unknown. It also maximizes each source independently, discarding residual-label budgets shared across rows. Those two losses of information define the next research target.

## Next three research tasks — priority order

### P1. Shared residual budgets and admissible selected geometries

Start from the already derived local residual-cover inequality in
[PAIR_OVERLAP.md](project/research/general_n/2026-09-13-constraint-respecting-cross-v1/PAIR_OVERLAP.md); do not restart its derivation
or the completed spill/pair replay. Retain residual-label budgets shared
across sources instead of maximizing every source independently. Seek a
checkable weighted cover or Hall obstruction, with explicit hypotheses.

Use the 26 fixed-pattern failures as diagnostic examples. Quantify the
obstruction over alternative admissible selected sets: a failure of one
stored pattern is not a whole-state exclusion. Preserve degree-preserving
repairs and counterexamples to proposed strengthenings.

### P2. Exact residual-compatible construction on a frozen sample

For patterns surviving the strengthened overlap checks, search residual
placements satisfying the shared budgets, endpoint loads and exact
destination compatibility. Then apply the fixed-neighbourhood integer-flow
criterion. Extract directly checkable obstructions from failed attempts;
solver infeasibility and timeouts alone remain exploratory.

If pair information still loses the decisive structure, test the analogous
triple-deficit construction, retaining the same complete-coverage standard.

### P3. Complete-domain application of any strengthened set-level cut

Apply a checked new inequality to the preserved 4,584-state domain only with
explicit coverage of every admissible branch needed for a whole-state claim.
Report fixed-pattern rejections and whole-state exclusions separately.
Preserve zero-gain outcomes. N36 remains a structural laboratory rather than
the primary objective.

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
