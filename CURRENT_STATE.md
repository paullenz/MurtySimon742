# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart point after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth. Read this file first, inspect later `main` commits, then follow the linked packages.

**Research state reconciled:** 13 September 2026 through the **N34 state-279 whole-state exclusion** in [`project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md), after the earlier state-227 closure. External mathematical review, novelty assessment and independent computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

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
- selected-excess bound on every selected positive-demand incidence:
  `p_u-rho_u+1<=x_i-s_i`;
- exact-demand corollary: when `x=s`, every active source satisfies `p_u<=rho_u-1`;
- **threshold excess-cap family:** if `h_l=#{i:x_i-s_i>=l}`, then
  `q_u>h_l => p_u<=rho_u+l-2`.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Quantifier pivot and whole-state closures

Package: [`project/research/general_n/2026-09-13-alternative-attacks-v1/`](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md).

The central diagnosis is a **quantifier problem**, not merely a shortage of scalar inequalities. Fixed-pattern models become very strong once label identities and shared budgets are retained, but a whole-state theorem must control alternative selected geometries, `q`-vectors and excess profiles.

### State 227

[`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md) excludes N34 state 227 as a whole scalar state. Exact enumeration handles `E=0,...,20`; a threshold-excess tail argument handles `E=21,...,34`; incoming capacity makes `E>=35` impossible. Machine summary: [`STATE_227_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE_VERIFICATION.json).

This moved the frozen frontier from `994 exclusions / 4,584 survivors` to `995 / 4,583`.

### State 279

[`STATE_279_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md) is the second whole-state exclusion produced by the programme. State data are

```text
a=15, b=18, t=1,
s   = 2^3,3^12,
rho = 1^7,3^11,
r=40,
S=42.
```

The preserved proof combines a hand reduction with exact integer enumeration. The low-excess verifier covers `E=0,...,15`, with three explicitly recorded hand-rigidity cases; the threshold tail closes `E=16,...,34`, with minimum reported gap 2; total incoming capacity makes `E>=35` impossible. Machine summary: [`STATE_279_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE_VERIFICATION.json). External review of the bridge and hand-rigidity arguments and independent computational reproduction remain open.

## Current whole-state generalisation record

The frontier is now

```text
996 exclusions / 4,582 survivors.
```

Breakdown:

```text
4,504 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are survivors in a frozen generalisation experiment, **not surviving graphs** and not unresolved fixed-order N34/N35 cases.

The temporary extraction utility [`extract_frozen_survivors.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/extract_frozen_survivors.py) is transport/replay infrastructure only; it does not apply a new theorem. The associated workflow is [`.github/workflows/threshold-survivor-extract.yml`](.github/workflows/threshold-survivor-extract.yml).

## Independent maximum-cut route

For any cut `X|Y`, let `I` be its internal edges and `M` its missing cross-pairs. Exactly

```text
e(G)=|X||Y|+I-M.
```

Thus `I<=M` for some cut would imply Murty–Simon. Deterministic reconnaissance found zero maximum-cut violations among the recorded small D2C instances and sampled positive `C5` blow-ups; a short hand argument proves the desired cut inequality for every positive independent-set blow-up of `C5`.

A direct matching from every maximum-cut internal edge to a uniquely witnessed cross nonedge is **false**. Any viable proof must use aggregate charging, alternating exchanges or stability rather than one-edge/one-nonedge matching.

## Corrected interpretation of switching

Degree-preserving `2x2` repairs live in the **relaxed selected-incidence matrix**. They are not automatically legal switches of actual graph quasi-edge representatives, because the switched cross-edge may not have the required exact total-domination exception.

Use either explicit all-geometry models where the matrix relaxation is stated as such, or selection-free raw candidate data / genuinely legal representative availability at graph level. No active theorem assumes unrestricted graph-level switching.

## Most important correctness obligations

1. **External review of the canonical bridge**, especially the graph-to-quasi-edge implications; this remains the main correlated correctness risk.
2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selection-free candidate capacity, selected excess and the threshold family.
3. Independent reproduction of the state-227 and state-279 exact-profile and tail computations.
4. External checking of the state-279 hand-rigidity cases.
5. Continue preserving failures, invalidated shortcuts, solver timeouts and publication/tooling mistakes. Never treat numerical infeasibility or noncompletion as proof.

## Current research priorities

### P1. Apply the threshold excess-cap family across the remaining 4,582 survivors

Start with `l=1,2,3`, couple it to the existing top-k endpoint envelope, and quantify `q`/excess profiles before returning to selected-set geometry. State 227 and state 279 now show that the mechanism is not isolated to one state.

### P2. Seek a symbolic threshold theorem

Extract a parameterized inequality in `(a,b,rho,s,E,h_l)` that replaces per-state enumeration for broad classes. Compare the common structure of the state-227 and state-279 closures.

### P3. Use the frozen-survivor extraction workflow to run systematic family scans

The extraction utility now provides a durable way to recover the frozen survivor pool for broad threshold-family experiments. Preserve any new exclusion counts, parameters, scripts and replay outputs before using them downstream.

### P4. Project raw candidate-capacity subsets

Seek useful selection-free projections in terms of degree/tail data that do not require the entire raw graph.

### P5. Maintain the maximum-cut route in parallel

Do not retry the falsified direct matching. Test aggregate Hall/charging or stability statements around a maximum cut.

### P6. Return to shared residual/pair geometry after quantified pruning

The shared-budget and exact-destination machinery remains powerful. Bring it back after the threshold programme has reduced the alternative-margin/profile space; do not default to another single stored selected pattern.

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
3. read the alternative-attacks v1 README, `STATE_227_WHOLE_STATE.md`, `STATE_279_WHOLE_STATE.md` and the verification JSON files;
4. continue from P1/P2 unless later preserved work changes priority;
5. preserve any material result or failure before relying on it downstream;
6. after a material change, update this handoff in the same repository-writing pass.

For the fuller reviewer-facing map use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).
