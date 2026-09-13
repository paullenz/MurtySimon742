# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart point after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth. Read this file first, inspect later `main` commits, then follow the linked packages.

**Research state reconciled:** 13 September 2026 through the **N34 state-526 whole-state exclusion**, after the earlier state-227, state-279 and state-588 closures. External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

The temporary branches `threshold-family-scan` and `state279-proof` were reconciled into `main` by merge commit `566e064447a9cd54a8fa253c9049de0ffbc09efe`. Their histories remain preserved.

## Headline fixed-order candidate status

- `n=25`: complete candidate, `e(G)<=156`, equality exactly `K(12,13)`; reviewer-v2; external specialist review open.
- `n=27`: complete candidate, `e(G)<=182`, equality exactly `K(13,14)`; reviewer-v2; external review open.
- `n=28`: complete candidate, `e(G)<=196`, equality exactly `K(14,14)`; reviewer-v2 plus analytic hardening; external review open.
- `n=29`: complete candidate, `e(G)<=210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch hand-closed; external review open.
- `n=30`: complete candidate, `e(G)<=225`, equality exactly `K(15,15)`; reviewer-v3; external review open.
- `n=31`: complete candidate, `e(G)<=240`, equality exactly `K(15,16)`; source-first reviewer-v1; external review open.
- `n=32`: complete candidate, `e(G)<=256`, equality exactly `K(16,16)`; source-first reviewer-v1; external review open.
- `n=33`: complete candidate, `e(G)<=272`, equality exactly `K(16,17)`; source-first reviewer-v1; external review open.
- `n=34`: complete candidate, `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2; final heavy certificate replaced by a short hand argument; external review open.
- `n=35`: complete candidate, `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1; external review open.

These fixed-order candidate proofs are closed on their own preserved ledgers. General-theory survivor counts below are **not** unresolved N34/N35 cases.

## Canonical general theory

Canonical graph-to-constraint framework: [`CANONICAL_BRIDGE.md`](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).

Current candidate general results include:

- all-order balanced-degree reduction and fixed-`a`/tail families;
- maximum-degree theorem candidate: for `n>=6`, `Delta(G)>=(7/12)n` implies `e(G)<floor(n^2/4)`;
- all-threshold heavy-load/routing inequalities, incoming-degree penalties and low-demand consequences;
- joint heavy-routing, demand/tail projection and equality rigidity;
- compatible-destination routing, closed compatible potential and fixed-neighbourhood Hall/flow criterion;
- co-singleton trace hierarchy and receiver-containment spill inequality;
- pair-overlap/residual-cover inequalities;
- shared residual-budget endpoint/pair inequalities and the balance-or-concentration alternative;
- selection-free candidate-capacity bounds;
- selected-excess bound on every selected positive-demand incidence: `p_u-rho_u+1<=x_i-s_i`;
- exact-demand corollary: when `x=s`, every active source satisfies `p_u<=rho_u-1`;
- threshold excess-cap family: if `h_l=#{i:x_i-s_i>=l}`, then `q_u>h_l => p_u<=rho_u+l-2`.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Quantifier pivot and whole-state closures

Package: [`project/research/general_n/2026-09-13-alternative-attacks-v1/`](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md).

The central diagnosis is a **quantifier problem**. Fixed-pattern models become very strong once label identities and shared budgets are retained, but a whole-state theorem must control alternative selected geometries, q-vectors and excess profiles.

### State 227

[`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md) excludes N34 state 227. Exact enumeration handles `E=0,...,20`; a threshold-excess tail handles `E=21,...,34`; incoming capacity makes `E>=35` impossible. Frontier: `994/4,584 -> 995/4,583`.

### State 279

[`STATE_279_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md) excludes N34 state 279:

```text
a=15, b=18, t=1,
s=2^3,3^12,
rho=1^7,3^11,
r=40, S=42.
```

Exact low-excess replay covers `E=0,...,15`, with three hand-rigidity cases. The relaxed `h_2` threshold closes `E=16,...,34`; incoming capacity kills `E>=35`. Frontier: `995/4,583 -> 996/4,582`.

### State 588

[`STATE_588_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_WHOLE_STATE.md) excludes N34 state 588:

```text
a=15, b=18, t=1,
s=3^15,
rho=1^5,2,3^12,
r=43, S=45.
```

Exact low-excess replay covers `E=0,...,15`; its unique coarse equality is removed by an endpoint-rigidity contradiction `sum C_i>=106>97`. A cheap `h_2` tail screen is strict except at `E=16` and `E=24`; exact replay closes those two layers. Incoming capacity excludes `E>=35`. Frontier: `996/4,582 -> 997/4,581`.

### State 526

[`STATE_526_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_526_WHOLE_STATE.md) is the fourth whole-state exclusion:

```text
a=15, b=18, t=1,
s=2,3^14,
rho=1^5,2^2,3^11,
r=42, S=44.
```

Exact low-excess replay covers `E=0,...,16`. The unique coarse equality is

```text
E=7,
e_2=7,
e_3=0^14,
q_(rho=2)=1^2,
q_(rho=3)=1^2,5^7,6^2.
```

Equality in the incoming ledger forces all q=1 sources to high p, so they can select only the unique high-excess label. Every zero-excess demand-three label is therefore selected only at q=5/6, p=2 sources and has `C_i>=7`. Those fourteen labels alone force `sum C_i>=98`, contradicting the exact total `sum C_i=93`.

The relaxed `h_2` tail has gap zero only at `E=16`, already strictly excluded by the exact scan with gap 23; every `E=17,...,34` has positive gap. Total incoming capacity `sum p<=78` excludes `E>=35`.

Replay: [`STATE_526_REPLAY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_526_REPLAY.md). Machine summary: [`STATE_526_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_526_WHOLE_STATE_VERIFICATION.json).

## Current whole-state generalisation record

The frozen frontier is now

```text
998 exclusions / 4,580 survivors.
```

Breakdown:

```text
4,502 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are survivors in a frozen generalisation experiment, **not surviving graphs** and not unresolved fixed-order N34/N35 cases.

The extraction utility [`extract_frozen_survivors.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/extract_frozen_survivors.py) is transport/replay infrastructure only; it does not apply a theorem.

## General-theory lesson from the four closures

The examples support a reusable two-sided architecture:

1. **High-excess scarcity:** threshold counts `h_l` cap the incoming load of large-q sources.
2. **Zero/low-excess availability:** labels with small excess require sufficiently low-p sources; the incoming ledger may make those sources unavailable.
3. **Endpoint budget:** once source availability is forced, `C_i>=q_u+p_u` can make the total label budget impossible.
4. **Triage before exact enumeration:** use the cheap `h_2` relaxation to rank states by non-strict layers; exact profile enumeration should be reserved for those layers and the low-excess boundary.

State 588 shows the mechanism does not depend on demand-two correction terms. State 526 gives the cleanest source-availability contradiction so far: the zero-excess labels alone exceed the entire `C` ledger.

## Independent maximum-cut route

For any cut `X|Y`, let `I` be its internal edges and `M` its missing cross-pairs. Exactly

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would imply Murty–Simon. A direct matching from every maximum-cut internal edge to a uniquely witnessed cross nonedge is **false**; any viable proof must use aggregate charging, alternating exchanges or stability.

## Corrected interpretation of switching

Degree-preserving `2x2` repairs live in the **relaxed selected-incidence matrix**. They are not automatically legal switches of actual graph quasi-edge representatives. No active theorem assumes unrestricted graph-level switching.

## Most important correctness obligations

1. **External review of the canonical bridge**, especially the graph-to-quasi-edge implications; this remains the main correlated correctness risk.
2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selection-free candidate capacity, selected excess and the threshold family.
3. Independent reproduction of the state-227, state-279, state-588 and state-526 exact computations.
4. External checking of the hand-rigidity arguments in all four whole-state closures.
5. Continue preserving failures, invalidated shortcuts, solver timeouts and publication/tooling mistakes. Never treat numerical infeasibility or noncompletion as proof.

## Current research priorities

### P1. Run threshold triage across the remaining 4,580 survivors

Use the cheap `h_2` relaxation first, rank states by the number and severity of non-strict excess layers, then exact-enumerate only exceptional layers. Preserve scan inputs, code, outputs and ranking.

### P2. Seek a symbolic threshold/availability theorem

Extract a parameterized inequality in `(a,b,rho,s,E,h_l)` that explains the common state-227/state-279/state-588/state-526 closures. Include the low-excess source-availability rigidity exposed most cleanly by state 526.

### P3. Continue the selection-free raw candidate-capacity projection

Seek useful degree/tail projections of the candidate sets `K_u` that do not require the entire raw graph.

### P4. Maintain the maximum-cut route in parallel

Do not retry the falsified direct matching. Test aggregate Hall/charging or stability statements around a maximum cut.

### P5. Return to shared residual/pair geometry after quantified pruning

Bring the stronger shared-budget and exact-destination machinery back after the threshold programme has reduced the alternative-margin/profile space.

## Research/preservation rules

The standing orders in [`project/N25_PROJECT_STANDING_ORDERS.md`](project/N25_PROJECT_STANDING_ORDERS.md) remain binding. In particular:

- chat must never be the sole durable record of material work;
- preserve code, parameters, inputs, outputs, survivor lists, hashes, commands, certificates and environment information where applicable;
- preserve failed approaches, counterexamples and corrected interpretations rather than deleting them;
- distinguish mathematical proof status, exact replay, internal audit, publication and external review;
- routine non-forced commits/pushes to canonical repository `paullenz/MurtySimon742` `main` are authorised without asking again;
- verify the branch head and key files after publication; do not use force-push or history rewriting.

## Restart protocol

On a fresh session:

1. open this file;
2. inspect `main` commits newer than the reconciliation point;
3. read the alternative-attacks README and the state 227, 279, 588 and 526 whole-state notes plus verification summaries;
4. continue from P1/P2 unless later preserved work changes priority;
5. preserve any material result or failure before relying on it downstream;
6. after a material change, update this handoff in the same repository-writing pass.

For the fuller reviewer-facing map use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).
