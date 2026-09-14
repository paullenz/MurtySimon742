# Murty–Simon / Erdős #742 — current state handoff

**Purpose.** Durable restart point after chat reset, client desynchronisation or context loss. The repository, not any chat transcript, is the source of truth. Read this file first, inspect later `main` commits, then follow the linked packages.

**Research state reconciled:** 14 September 2026 through the audited post-pair relational recovery promotion and Hall-structure checkpoint: **977 quantified whole-state closures**, frontier **1,971/3,607** (`3,529` N34-derived survivors plus `78` N35-derived survivors). Eighteen closures predate the large family; **943 further N34-derived scalar states** are protected by the cross-implementation potential-pair audit. External mathematical review, novelty assessment and genuinely independent third-party computational reproduction remain OPEN unless a later preserved checkpoint explicitly changes that status. Internal replay, same-assistant audit and repository publication are not external acceptance.

**Durability guard:** [`tools/check_n34_whole_state_ledger.py`](tools/check_n34_whole_state_ledger.py) protects the 18 earlier closures plus the hash-pinned **943-state** [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv) family, checks ledger provenance, and currently verifies `977` ledger states. New closures may be added, but a later ledger/README rewrite must not silently remove any preserved closure.

The temporary branches `threshold-family-scan` and `state279-proof` were reconciled into `main` by merge commit `566e064447a9cd54a8fa253c9049de0ffbc09efe`. Their histories remain preserved.

<!-- HALL-STRUCTURE-2026-09-14:START -->
## 14 September Hall-structure checkpoint

**Status boundary.** The canonical promoted whole-state position remains **977 quantified closures, 1,971 exclusions / 3,607 survivors**. Nothing in this section changes that ledger count. The full post-pair relational scan is discovery/reconnaissance until its recovery pass and fresh cross-implementation audit complete; only a later separately gated promotion may change the headline frontier.

### Exact target-Hall compression

The current orientation/Hall package is [`project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md).

- **Whole-type Hall theorem.** For fixed `(q,c,P)` data, every labelled Hall cut is represented exactly by type counts, and coordinatewise discrete concavity implies a minimum Hall margin is attained by a union of complete `(q,c,P)` type classes. GitHub Actions run `34820069162` is green; its frozen audit checked `14,330` profiles, `593,984` labelled/compressed cut equalities and `391,896` coordinate-concavity lines with zero discrepancies.
- **Exact type-level max-flow theorem.** The full labelled target network is equivalent, by min-cut equality, to a quotient network on the distinct `(q,c,P)` types. The Hall-margin set function is submodular. GitHub Actions run `34821405958` is green. This gives exact small type-level certificates rather than labelled max-flow witnesses.
- **Interval form.** Numerical directed compatibility is exactly intersection of source interval `[q,c]` with target interval `[q,c+1]`, before deletion of the self-arc. This is the correct replacement for the disproved one-dimensional Ferrers-prefix simplification.

### Dominance and antichain structure

- [`DOMINANCE_UPSET_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/DOMINANCE_UPSET_HALL.md) proves an exchange/up-set theorem for the initial hardness order `q` up, `c` down, `P` up. Its independent CI replay, run `34827519117`, is green; the preserved artifact digest is `sha256:5e0977bedbd2615df54f4f31f95ec4847635355f10fad835257d92a65697bd21`.
- [`SHARP_DOMINANCE_UPSET_HALL.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SHARP_DOMINANCE_UPSET_HALL.md) strengthens the exchange order to

  ```text
  x >=_* y  iff  c_x<=c_y
                 and [q_x>q_y or (q_x=q_y and P_x>=P_y)].
  ```

  In particular, if `q_x>=q_y+2` and `c_x<=c_y`, **every** minimum Hall witness containing `y` also contains `x`, irrespective of `P`. Its dedicated CI replay, run `34830228571`, is green and frozen in [`SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/SHARP_DOMINANCE_UPSET_HALL_VERIFICATION.json): `4,286` profiles, `1,123,108` submodularity checks, `372,455` sharp exchange checks and `126,654` strict-gap checks, with zero discrepancies. Artifact digest: `sha256:b686e3f9663a082aa9b0ff9fa89d1c0a29904ca3622f205421a895e3babbf37c`.
- The exact quotient network can be augmented with capacity-`Q+1` dominance-closure arcs without changing its min-cut value; see [`DOMINANCE_CLOSED_MAXFLOW.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/DOMINANCE_CLOSED_MAXFLOW.md).
- [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_ANTICHAIN_CERTIFICATE.md) gives the next exact consequence: submodularity makes the minimum-margin cuts a lattice, so there is a unique maximal minimizer `M+`; it is a sharp-hardness up-set and is uniquely represented by its minimal antichain generators. A closure-augmented quotient max-flow recovers the same `M+` from one residual min-cut. Its dedicated CI replay, run `34830787798`, is green and frozen in [`CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_ANTICHAIN_CERTIFICATE_VERIFICATION.json): `4,286` profiles, `198,140` type-set margins, `28,460` minimizer-lattice pair checks, `4,286` closure-flow checks and `4,286` residual maximal-cut checks, with zero discrepancies. Artifact digest: `sha256:2ed919e019c7f65a21fbbe92d81e5db84db14e39889bd259d559e2feded08433`.

### Preserved failed simplifications

[`PRINCIPAL_UPSET_COUNTEREXAMPLE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/PRINCIPAL_UPSET_COUNTEREXAMPLE.md) prevents a false next step. A three-type `V` profile has every principal up-set nondeficient but a two-generator up-set of margin `-1`; a four-type example needs three incomparable generators. Therefore neither single-type cuts nor one principal up-set is exact in general.

The 15-state principal-upset reconnaissance pilot completed green as a computation but **is not a promotion certificate**: the full relational stack excluded `13/15` states, while principal up-sets completely explained only `2/13`. Principal up-sets killed `17,284` individual profiles versus `14,768` for single-type cuts, so they help pruning but do not capture the genuine multi-generator obstruction.

The canonical-antichain verification also found negative test profiles requiring up to six generators (`869, 1,303, 1,005, 324, 49, 6` profiles with respectively `1,...,6` generators). This is audit evidence, not an all-order bound; it reinforces that the right next object is the **structured staircase boundary**, not a guessed small generator count.

### Full frontier relational scan

The layer/state-safe full scan of the canonical `3,607` survivors is GitHub Actions run `34820187136`, head `3255c0641b00ae97c426d1e089a6b6c92c8300fc`. It uses per-state checkpointing and treats timeouts/errors as unresolved, never as exclusions. The downstream chain is:

```text
checkpointed discovery
 -> layer-safe aggregate
 -> long-budget recovery of every unresolved/unattempted state
 -> fresh two-implementation state-by-state audit
 -> separate gated promotion only after agreement.
```

A scan shard or preliminary relational exclusion is **not canonical evidence by itself**. N34 and N35 provenance are kept in separate ledgers to prevent layer-count drift. The correct structural priority while this scan proceeds is to analyse the verified sharp-dominance **antichain staircase** of deficient type-level min-cuts, not to force the already-refuted principal-upset shortcut.
<!-- HALL-STRUCTURE-2026-09-14:END -->

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
- refined baseline-3/order-statistic candidate lemma for the `s_i in {2,3}` family, preserving the exact score `rho_u+q_u-1` and negative zero-excess demand-two contribution;
- zero-excess endpoint-order candidate lemma: an exact-demand label of demand `d` requires at least `d` active sources with `rho_u>=d` and `p_u<=rho_u-1`, and its endpoint `C_i` is at least the `d`-th smallest eligible `q_u+p_u`;
- exact low-demand incidence-capacity scanner extending the audited adjacent-family verifier to a broader seven-state ring without rewriting its mathematical search logic;
- orientation target-capacity lemma for selected missing-B-edge orientations: if an edge is oriented `u->w`, then `q_u-1<=q_w+rho_w`; consequently, for every integer `k`, `sum_{w:q_w+rho_w<=k} p_w <= sum_{u:q_u<=k+1} q_u`. The exact E=0 replay closes states 77 and 60 with a minimum six-incidence deficit.
- exact directed compatibility and Hall-flow projection: an orientation `u->w` requires `q_u<=q_w+rho_w+1` and `q_w<=q_u+rho_u`; the resulting source-target relation is genuinely two-dimensional rather than Ferrers in general.
- whole-type orientation Hall theorem: for a fixed target-flow profile, group sources/targets by identical `(q,c,P)` type. The exact Hall margin is separately discretely concave in every type-count coordinate, so if any labelled Hall cut fails then a union of complete `(q,c,P)` type classes also fails with at least as large a deficiency. The target-flow test therefore reduces exactly to at most `2^k` complete-type cuts for `k` distinct types; [the theorem package](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/README.md) has a green exact finite audit but external mathematical review and novelty assessment remain open.
- total-excess source cap: in all-positive-demand branches, `p_u<=rho_u+floor(E/q_u)-1` for every active source, with an explicit zero-demand correction in the general statement.
- potential-pair capacity theorem: the actual missing graph `J` is a subgraph of a scalar potential graph `K_D`, giving `p_u+q_u<=d_KD(u)`; two structurally different full-frontier implementations use this to close 943 further N34-derived scalar states.
- low-`c`/high-`q` cross obstruction: for every integer `r`, with `ell_r=#{w:q_w+rho_w<=r}` and `u_r=#{u:q_u>=r+2}`, every legal branch satisfies `Q+ell_r*u_r<=binom(b,2)`.

The unrestricted Murty–Simon conjecture is **not** proved by this project.

## Quantifier pivot and whole-state closures

Package: [`project/research/general_n/2026-09-13-alternative-attacks-v1/`](project/research/general_n/2026-09-13-alternative-attacks-v1/README.md).

The central diagnosis is a **quantifier problem**. Fixed-pattern models become very strong once label identities and shared budgets are retained, but a whole-state theorem must control alternative selected geometries, q-vectors and excess profiles.

### State 227

[`STATE_227_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_227_WHOLE_STATE.md) excludes N34 state 227. Exact enumeration handles `E=0,...,20`; a threshold-excess tail handles `E=21,...,34`; incoming capacity makes `E>=35` impossible. Frontier: `994/4,584 -> 995/4,583`.

### State 279

[`STATE_279_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_279_WHOLE_STATE.md) excludes N34 state 279. Exact low-excess replay covers `E=0,...,15`, with three hand-rigidity cases; the relaxed `h_2` threshold closes `E=16,...,34`; incoming capacity kills `E>=35`. Frontier: `995/4,583 -> 996/4,582`.

### State 588

[`STATE_588_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_588_WHOLE_STATE.md) excludes N34 state 588. Its unique low-excess equality is removed by an endpoint-budget contradiction `sum C_i>=106>97`; the cheap `h_2` tail leaves only `E=16` and `E=24`, both closed by exact replay. Frontier: `996/4,582 -> 997/4,581`.

### State 526

[`STATE_526_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_526_WHOLE_STATE.md) excludes N34 state 526. Its unique coarse equality is removed by source-availability/endpoint-budget rigidity; the tail is strict for `E=17,...,34`. Frontier: `997/4,581 -> 998/4,580`.

### State 382

[`STATE_382_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_382_WHOLE_STATE.md) excludes N34 state 382. Exact low-excess replay through `E=17` is strict; retaining the negative zero-excess demand-two baseline term makes the tail strict through `E=34`. Frontier: `998/4,580 -> 999/4,579`.

### State 519

[`STATE_519_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_519_WHOLE_STATE.md) excludes N34 state 519. Exact profile replay leaves only `E=6,8,9`; a stronger source-availability replay retaining the endpoint loads of two required low-p sources raises their gaps to `2,4,2`. The refined tail is strict through `E=34`. GitHub Actions run `34773463128` completed green. Frontier: `999/4,579 -> 1,000/4,578`.

The mechanism is extracted in [`ZERO_EXCESS_ENDPOINT_ORDER.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ZERO_EXCESS_ENDPOINT_ORDER.md).

### State 153

[`STATE_153_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_153_WHOLE_STATE.md) is the seventh quantified closure:

```text
a=15, b=18, t=1,
s=2^5,3^10,
rho=1^7,2^2,3^9,
r=38, S=40.
```

The exact low-demand extension scanner is **strict on every excess layer `E=0,...,34`**, with global minimum gap `+1` and no nonpositive layers. The universal incoming cap gives

```text
sum p_u <= 7*3+2*4+9*5=74,
40+E=sum p_u<=74,
E<=34.
```

Thus the exact scan covers every possible excess value; no bespoke hand-rigidity exception is needed. GitHub Actions run `34780310971`, job `103786002313`, is green. Exact output is preserved in [`LOW_DEMAND_EXTENSION_153.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_DEMAND_EXTENSION_153.tsv) with machine provenance in [`STATE_153_WHOLE_STATE_VERIFICATION.json`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_153_WHOLE_STATE_VERIFICATION.json). Frontier: `1,000/4,578 -> 1,001/4,577`.

## Latest closures: states 77 and 60

The mixed demand-two/demand-three joint-Hall refinement made every previously weak positive-excess layer strict in states 77 and 60, leaving only `E=0` in each state. The remaining exact-demand layer is excluded by [`ORIENTATION_TARGET_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_TARGET_CAPACITY.md).

For a selected orientation of a missing `B`-edge `u->w`, every other selected label at `u` must also be cross-adjacent to `w`, giving

```text
q_u - 1 <= q_w + rho_w.
```

Hence every threshold `k` obeys the necessary target-capacity cut

```text
sum_{w:q_w+rho_w<=k} p_w <= sum_{u:q_u<=k+1} q_u.
```

The independent exact verifier [`verify_e0_orientation_capacity.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/verify_e0_orientation_capacity.py) enumerated all `201,670` `E=0` q-profiles for state 77 and all `253,001` for state 60. No profile passed; the closest profile in either state was still six incidences short. GitHub Actions run `34785891328` completed green and its replay output is preserved.

Whole-state records are [`STATE_77_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_77_WHOLE_STATE.md) and [`STATE_60_WHOLE_STATE.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/STATE_60_WHOLE_STATE.md). They are entries 15 and 16 of the canonical union; ordinal wording in older parallel notes is non-authoritative.

## Latest large frontier advance: potential-pair capacity

The orientation work sharpened from a one-sided target cut to the exact directed compatibility condition

```text
D(u,w) iff u!=w,
              q_u<=q_w+rho_w+1,
              q_w<=q_u+rho_u.
```

An unordered pair can be missing only if one of its two directions is compatible. This defines the potential-pair graph `K_D`; the actual missing graph satisfies

```text
J subseteq K_D,
q_u+p_u=d_J(u)<=d_KD(u).
```

The resulting pointwise cap, combined with canonical incoming/simple bounds and the total-excess source cap, was scanned over a deliberately **enlarged** q-universe: only `q_u<=min(a-rho_u,#{i:s_i<=rho_u})` and `sum q=S+E` were assumed, so no selected-incidence Hall feasibility was needed for the exclusions.

Two structurally different full-frontier implementations agree exactly on **943 further N34-derived whole-state exclusions**. The first constructs directed pairs from expanded source vectors; the second enumerates `(rho,q)` type multiplicities and computes `d_KD` from the closed-form counting theorem. On every excluded state they agree exactly on exhaustive profile count, pre-pair pass count and best final deficit. See [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md).

The promoted frozen frontier is

```text
1,971 exclusions / 3,607 survivors,
3,529 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

The theorem itself is separately replayed in [`verify_potential_pair_capacity.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/verify_potential_pair_capacity.py), which checked 122,608 small `(q,rho)` profiles, 2,259,488 ordered pairs and 588,416 degree identities. These are internal replay checks, not external acceptance.

A compact symbolic consequence is the threshold product obstruction

```text
Q + ell_r*u_r <= binom(b,2)
```

for every integer `r`, where `ell_r` counts low-`c` vertices and `u_r` counts high-`q` sources. This is now the highest-leverage all-order route.

## Current whole-state generalisation record

The frozen frontier is now

```text
1,971 exclusions / 3,607 survivors.
```

Breakdown:

```text
3,529 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

These are survivors in a frozen generalisation experiment, **not surviving graphs** and not unresolved fixed-order N34/N35 cases.

The extraction utility [`extract_frozen_survivors.py`](project/research/general_n/2026-09-13-alternative-attacks-v1/extract_frozen_survivors.py) is transport/replay infrastructure only; it does not apply a theorem.

## General-theory lesson from the quantified closures

The closures support a reusable two-sided architecture:

1. **High-excess scarcity:** threshold counts `h_l` cap the incoming load of large-q sources.
2. **Zero/low-excess availability:** exact-demand labels require enough sufficiently low-p selected sources.
3. **Endpoint upper order statistics:** every selected source gives `d_i<=rho_u+q_u-1`, so the selected-source score distribution caps `C_i` from above.
4. **Endpoint lower order statistics:** a zero-excess exact-demand label forces `C_i` at least the appropriate eligible-source order statistic of `q_u+p_u`.
5. **Negative baseline terms matter:** a demand-two label at zero excess contributes negatively in baseline three and should not be discarded.
6. **Triage before exact enumeration:** cheap refined relaxations should rank states and excess layers before profile enumeration.
7. **Some whole states now close without bespoke rigidity:** state 153 is strict on all admissible excess layers under the reusable exact incidence-capacity verifier, which is encouraging for scale.
8. **Missing-edge orientation is itself capacitated:** an oriented missing edge can only enter a target with enough cross-degree to support the source's other selected labels. This links the source-label Hall machinery back to the actual missing-edge orientation and suggests a stronger flow/Ferrers formulation.

State 588 shows the mechanism does not depend on demand-two terms. State 526 exposes source-availability rigidity. State 382 gives the clean universal negative-baseline correction. State 519 upgrades that correction to an endpoint-load order statistic. State 153 shows the strengthened machinery can sometimes supply a clean whole-state closure directly. States 77 and 60 show that the remaining obstruction can sometimes be eliminated by graph-level orientation capacity without fixing a selected geometry.

## Broader low-demand extension matrix

Commit `60f89cb49a493b6b65ccca93bcaa83291bef6f21` parallelized the exact extension scan across seven additional frozen N34 states. GitHub Actions run `34780310971` completed green in all seven jobs.

The current layer summary is:

| State | minimum gap | nonpositive excess layers |
|---:|---:|---|
| 153 | `+1` | none — **whole state closed** |
| 283 | `+1` | none — **whole state closed** |
| 122 | `+1` | none — **whole state closed** |
| 154 | `+1` | none — **whole state closed** |
| 231 | `+1` | none — **whole state closed** |
| 77 | `-7` in the original extension scan | historical weak layers `E=0,1,3,4,5,6,7`; **subsequently whole-state closed** |
| 60 | `-11` in the original extension scan | historical weak layers `E=0,...,7`; **subsequently whole-state closed** |

This table is now historical triage rather than the live frontier: **all seven states in this extension ring (153, 283, 231, 154, 122, 77 and 60) are whole-state closed** after the later endpoint-class, joint-Hall and orientation-capacity refinements. The original nonpositive layers remain recorded because failures and intermediate frontiers are part of the audit trail.

## Adjacent-family narrow scan

[`REFINED_H2_FAMILY_SCAN.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/REFINED_H2_FAMILY_SCAN.md) contains nine structurally adjacent N34 records. At scan time five were closed and four were active: states `230,282,385,519`. **All four are now closed**; the canonical ledger records their whole-state status.

The old refined-tail thresholds and intermediate gaps remain useful audit history, but neither this narrow family nor the seven-state extension ring contains a live target now. The old target ranking is superseded. The historical 3,623-state frontier has since fallen to the canonical **3,607-state** frontier after the audited 16-state relational recovery. Current work uses the checkpointed relational discovery/recovery/audit pipeline described below.

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
2. External review/novelty assessment of the candidate `7/12` theorem and later general lemmas, especially selected excess, total-excess source capacity, exact directed compatibility, potential-pair capacity, the low-c/high-q threshold product obstruction and the orientation Hall/flow projections.
3. Independent reproduction of the exact computations and hand steps linked from the canonical whole-state ledger.
4. External checking of hand-rigidity/endpoint arguments in the closures that use them.
5. Preserve the complete seven-state extension outputs, not only the successful state-153 layer table, before relying on them downstream.
6. Continue preserving failures, invalidated shortcuts, solver timeouts and publication/tooling mistakes. Never treat numerical infeasibility or noncompletion as proof.

<!-- CURRENT-PRIORITIES-2026-09-14:START -->
## Current research priorities

### P1. Exploit the verified canonical Hall antichain staircase

The sharp dominance theorem and [`CANONICAL_ANTICHAIN_CERTIFICATE.md`](project/research/general_n/2026-09-14-type-compressed-orientation-hall-v1/CANONICAL_ANTICHAIN_CERTIFICATE.md) are internally CI-green. The next all-order task is to turn the unique generator antichain into a sharper Murty-Simon-specific staircase description using `c=q+rho`, the canonical `q` caps, target-capacity formula `P`, demand forcing and excess constraints. Do **not** assume a universal one- or two-generator bound: preserved counterexamples and the finite audit rule that out as a safe general route.

### P2. Complete, recover and independently audit the 3,607-state relational scan

Run `34820187136` is the layer/state-safe checkpointed discovery pass over the canonical survivor frontier. Let every shard complete; record every timeout/error as unresolved; recover all unresolved/unattempted layer-states with the long-budget pass; then freshly replay every discovery exclusion through both the vector and independent type-count implementations. Only a later separately gated certificate promotion may change the canonical `1,971/3,607` headline.

### P3. Explain the N35-derived layer

Keep N34 and N35 closure ledgers separate. Compare the 78 N35-derived survivors against eliminated N34 profiles under the exact type-Hall, sharp-dominance and antichain descriptions. The goal is to identify a structural parameter that explains the layer difference, not merely to accumulate N35 exclusions.

### P4. Strengthen independent review and reproduction

Prioritise external checking of the canonical bridge, exact directed compatibility, whole-type Hall theorem, type-level max-flow equivalence, total-excess source cap, potential-pair theorem and the new dominance/antichain arguments. Repository CI and separately written same-assistant code are internal evidence, not third-party acceptance.

### P5. Preserve genuinely different routes

Continue maximum-cut/stability, selection-free and other independent approaches when they have leverage. Preserve negative results such as the coarse low-residual-reservoir scan and every counterexample to an over-strong simplification. Never infer proof from timeout, numerical infeasibility or a solver status alone.
<!-- CURRENT-PRIORITIES-2026-09-14:END -->

## Research/preservation rules

The standing orders in [`project/N25_PROJECT_STANDING_ORDERS.md`](project/N25_PROJECT_STANDING_ORDERS.md) remain binding. In particular:

- chat must never be the sole durable record of material work;
- preserve code, parameters, inputs, outputs, survivor lists, hashes, commands, certificates and environment information where applicable;
- preserve failed approaches, counterexamples and corrected interpretations rather than deleting them;
- distinguish mathematical proof status, exact replay, internal audit, publication and external review;
- the canonical whole-state ledger guard must retain every independently committed closure; it explicitly protects the 18 earlier closures and the hash-pinned 943-state potential-pair family with provenance checks;
- routine non-forced commits/pushes to canonical repository `paullenz/MurtySimon742` `main` are authorised without asking again;
- verify the branch head and key files after publication; do not use force-push or history rewriting.

## Restart protocol

On a fresh session:

1. open this file;
2. inspect `main` commits newer than this reconciliation point;
3. read the alternative-attacks README, [`WHOLE_STATE_LEDGER.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/WHOLE_STATE_LEDGER.tsv), and the closure records linked from that ledger;
4. inspect [`POTENTIAL_PAIR_CAPACITY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POTENTIAL_PAIR_CAPACITY.md), [`PAIR_CAPACITY_FRONTIER_AUDIT.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/PAIR_CAPACITY_FRONTIER_AUDIT.md), [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md), [`ORIENTATION_FLOW_HALL.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/ORIENTATION_FLOW_HALL.md), and the current residual result tables;
5. continue from P1/P2 unless later preserved work changes priority;
6. preserve any material result or failure before relying on it downstream;
7. after a material change, update this handoff in the same repository-writing pass.

For the fuller reviewer-facing map use [`README.md`](README.md) and [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md).

## 14 September 2026 — relational recovery promotion

The interrupted 1/32 relational pilot has now been recovered state-by-state. Sixteen N34-derived states passed fresh isolated replay in both the original vector-enumeration implementation and an independent type-count implementation; every proof-relevant stage count agreed exactly. The aggregate certificate is [`POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_RECOVERY_EXCLUDED.tsv), hash `c1ce4e645edf9dcc3e2f39ef42bd85030449b161549978877eb2e15ab2abe832`, with provenance in [`POST_PAIR_RELATIONAL_RECOVERY.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_RECOVERY.md).

Canonical generalisation frontier after promotion:

```text
1,971 exclusions / 3,607 survivors,
3,529 N34 equality-derived survivors,
78 N35 m=306-derived survivors.
```

The coarse low-residual-reservoir theorem was also scanned over the pre-promotion 3,623-state frontier: it applied to 3,421 states but closed none. That negative result is preserved in `LOW_RESIDUAL_RESERVOIR_RESULT.md` and is evidence that the exact two-dimensional relational structure carries information not captured by the coarse symbolic reservoir count.

**Next priority:** run the checkpointable relational machinery over the remaining ledger-current survivor frontier, preserving per-state artifacts and promoting only cross-checked closures; in parallel, extract symbolic two-dimensional Hall/dominance consequences that could replace finite scanning by a general theorem.

<!-- ACTIVE-RELATIONAL-2026-09-14:START -->
## 14 September 2026 — active post-pair relational programme

The **canonical promoted frontier remains `1,971 exclusions / 3,607 survivors`**. A stronger post-pair relational programme is running over those 3,607 ledger-current scalar survivors, but its discoveries are deliberately **not canonical closures** until they pass full coverage/recovery, fresh cross-implementation audit and a separately gated promotion.

The current layer/state-safe discovery run is GitHub Actions run `34820187136` at head `3255c0641b00ae97c426d1e089a6b6c92c8300fc`. It checkpointed every state separately and identifies every record by `(layer,state)`, so later timeout/cancellation cannot erase earlier completed evidence or conflate N34 and N35 IDs. The earlier run `34818390230` is preserved as historical reconnaissance but is not the authoritative full-frontier discovery pass.

The execution chain is documented in [`POST_PAIR_RELATIONAL_FULL_FRONTIER.md`](project/research/general_n/2026-09-13-alternative-attacks-v1/POST_PAIR_RELATIONAL_FULL_FRONTIER.md): checkpointed discovery, layer-safe aggregation, explicit unresolved accounting, long-budget recovery of every unresolved/unattempted layer-state, then fresh primary and independent type-count replay of every candidate exclusion. N34 and N35 promotions use separate ledgers.

In parallel, the target-Hall layer has been converted from an opaque labelled max-flow obstruction into exact type-level structure: complete types, quotient max-flow, submodular Hall margin, sharp hardness up-sets, dominance-closed min-cut, and a verified canonical antichain staircase. The preserved principal-upset counterexample shows that genuine multi-generator antichains are necessary. The next structural task is to exploit the Murty-Simon-specific relations to constrain that staircase while the finite scan completes.
<!-- ACTIVE-RELATIONAL-2026-09-14:END -->
