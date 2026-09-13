# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart point after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth. Read this file first, inspect later `main` commits, then follow the linked packages.

**Research state reconciled:** 13 September 2026 through the **N34 state-382 whole-state exclusion**, the fifth quantified whole-state closure after states 227, 279, 588 and 526. External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

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
- threshold excess-cap family: if `h_l=#{i:x_i-s_i>=l}`, then `q_u>h_l => p_u<=rho_u+l-2`;
- refined baseline-3/order-statistic candidate lemma for the `s_i in {2,3}` family, preserving the exact score `rho_u+q_u-1` and the negative zero-excess demand-two contribution.

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

Exact low-excess replay covers `E=0,...,16`. Its unique coarse equality is removed by a source-availability/endpoint-budget contradiction. The `h_2` tail is strict for every `E=17,...,34`; incoming capacity excludes `E>=35`. Frontier: `997/4,581 -> 998/4,580`.

### State 382

[`STATE_382_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_382_WHOLE_STATE.md) is the fifth whole-state exclusion:

```text
a=15, b=18, t=1,
s=2^2,3^13,
rho=1^6,2,3^11,
r=41, S=43.
```

Exact low-excess replay covers `E=0,...,17` and is strictly positive throughout: no equality case and no hand-rigidity exception are needed. The refined tail retains the universal negative contribution of zero-excess demand-two labels. Writing

```text
z_0=#{i:s_i=2,e_i=0},
```

the stronger necessary baseline inequality is

```text
T + 2 z_0 - P_+ <= 3(84+E).
```

This correction makes the tail strict for every `E=17,...,34`; the only non-strict layer of the refined relaxation is `E=16`, already strictly excluded by the exact replay. Incoming capacity excludes `E>=35`. Frontier: `998/4,580 -> 999/4,579`.

The follow-on note [`REFINED_BASELINE3_LEMMA.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/REFINED_BASELINE3_LEMMA.md) generalises the mechanism to every positive-demand scalar state with `s_i in {2,3}`. It uses the exact order statistic of the source score `rho_u+q_u-1`, so it is at least as strong as the deliberately relaxed state-382 tail envelope.

## Current whole-state generalisation record

The frozen frontier is now

```text
999 exclusions / 4,579 survivors.
```

Breakdown:

```text
4,501 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are survivors in a frozen generalisation experiment, **not surviving graphs** and not unresolved fixed-order N34/N35 cases.

The extraction utility [`extract_frozen_survivors.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/extract_frozen_survivors.py) is transport/replay infrastructure only; it does not apply a theorem.

## General-theory lesson from the five closures

The examples now support a reusable two-sided architecture:

1. **High-excess scarcity:** threshold counts `h_l` cap the incoming load of large-q sources.
2. **Zero/low-excess availability:** labels with small excess require sufficiently low-p sources; the incoming ledger may make those sources unavailable.
3. **Endpoint/order-statistic budget:** for a positive-demand label, `C_i=d_i+e_i`, while every selected source gives `d_i<=rho_u+q_u-1`; the `x_i`-th eligible source score therefore caps `C_i`.
4. **Negative baseline terms matter:** with baseline three, a demand-two label at zero excess contributes at most `-2`, not zero. State 382 is the first closure where preserving this term is decisive in several tail layers.
5. **Triage before exact enumeration:** use the cheap refined threshold relaxation to rank states by non-strict layers; exact profile enumeration should be reserved for those layers and the low-excess boundary.

State 588 shows the mechanism does not depend on demand-two correction terms. State 526 exposes source-availability rigidity. State 382 gives the cleanest fully strict low-excess replay and the first reusable negative-baseline correction.

## Adjacent-family scan now in progress/preserved

The files

- `prepare_refined_h2_family_scan.py`,
- `scan_refined_h2_family.cpp`,
- `.github/workflows/scan-refined-h2-adjacent-family.yml`

implement exact-integer triage for the structurally adjacent N34 family with demands only 2/3, at most four demand-two labels, residual degrees only 1/2/3, and at most three `rho=2` sources. The hash-verified input reconstruction contains nine records: the five closed regression states plus four active companion states. The first workflow attempt failed at C++ compilation because `std::tie` was applied to temporary `size()` values; that failure is preserved. The compile fix is committed, and the subsequent scan must be read from later commits/workflow evidence before making any new frontier claim.

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
2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selection-free candidate capacity, selected excess, the threshold family and the refined baseline-3/order-statistic lemma.
3. Independent reproduction of the state-227, state-279, state-588, state-526 and state-382 exact computations.
4. External checking of hand-rigidity/endpoint arguments in the closures that use them; state 382 itself requires no hand exception.
5. Continue preserving failures, invalidated shortcuts, solver timeouts and publication/tooling mistakes. Never treat numerical infeasibility or noncompletion as proof.

## Current research priorities

### P1. Complete refined threshold triage across the adjacent family, then widen it

Use the refined baseline-3/order-statistic relaxation first. Preserve full input, code, regression checks, outputs and ranking. Exact-enumerate only the non-strict excess layers of the best active companion state. After the adjacent family is understood, widen the same scanner across the remaining 4,579 frozen survivors where its hypotheses apply.

### P2. Seek a symbolic threshold/availability theorem

Extract a parameterized inequality in `(a,b,rho,s,E,h_l)` explaining all five closures and, if possible, their four adjacent companion states. The exact source-score order statistic in `REFINED_BASELINE3_LEMMA.md` is now the natural starting point.

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
2. inspect `main` commits newer than this reconciliation point;
3. read the alternative-attacks README and the five whole-state notes (227, 279, 588, 526, 382) plus verification summaries;
4. inspect `REFINED_BASELINE3_LEMMA.md` and the latest refined-family scan evidence;
5. continue from P1/P2 unless later preserved work changes priority;
6. preserve any material result or failure before relying on it downstream;
7. after a material change, update this handoff in the same repository-writing pass.

For the fuller reviewer-facing map use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).
