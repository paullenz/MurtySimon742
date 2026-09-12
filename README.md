# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 12 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication, green replay and same-assistant hostile audit are not external acceptance and do not prove the unrestricted conjecture.

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). The canonical theorem-level packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project actively welcomes hostile review, counterexamples, literature corrections and genuinely independent reproduction; GitHub Issues are the preferred place to report a suspected flaw.

## Current headline status

| Scope | Current project status |
|---|---|
| `n=25` | Complete candidate: `e(G) <= 156`, equality exactly `K(12,13)`; Fan-free reviewer-v2; complete partitioned replay and independent endpoint reconstruction green; external specialist review open |
| `n=27` | Complete candidate: `e(G) <= 182`, equality exactly `K(13,14)`; Fan-free reviewer-v2; hardened replay green; external review open |
| `n=28` | Complete candidate: `e(G) <= 196`, equality exactly `K(14,14)`; Fan-free reviewer-v2 plus 11 September analytic hardening; external review open |
| `n=29` | Complete candidate: `e(G) <= 210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch is hand-closed by threshold-tail compression; hostile internal audit found no blocking flaw; external review open |
| `n=30` | Complete candidate: `e(G) <= 225`, equality exactly `K(15,15)`; reviewer-v3; hand lemmas plus explicit proof-critical integer tables; internal arithmetic reproduced; external review open |
| `n=31` | Complete candidate: `e(G) <= 240`, equality exactly `K(15,16)`; source-first reviewer-v1; predominantly hand/structural; hostile internal audit found no blocking flaw; external review open |
| `n=32` | Complete candidate: `e(G) <= 256`, equality exactly `K(16,16)`; source-first reviewer-v1; 257-edge branch exact nine-rectangle closure, equality branch exact finite replay plus one hand tight-threshold contradiction; hostile internal audit found no blocking flaw; external review open |
| `n=33` | Complete candidate: `e(G) <= 272`, equality exactly `K(16,17)`; source-first reviewer-v1; `Delta=17` entirely hand-closed, sole new equality frontier has 21 demand profiles / 29 states, with 25 exact shifted-potential exclusions and 4 hand contradictions; hostile internal audit found no blocking flaw; external review open |
| `n=34` bound | Candidate conjectured bound `e(G)<=289`; bound reviewer-v1. All 1,614 states at 290 edges are excluded by 662 hand/accounting arguments and 952 integer certificates. Equality classification at 289 edges remains OPEN. |
| Balanced-degree / fixed-a structural results | Candidate all-order balanced-degree reduction; infinite `a=14` high-b family; tail bounds through `a=23`, including joint clipping and an adaptive six-level boundary; proof-critical finite arithmetic where stated; external review open |
| General maximum-degree result | Candidate theorem: `n >= 6` and `Delta(G) >= (7/12)n` imply `e(G) < floor(n^2/4)`; complete candidate hand argument with internal exact audits green; external review and novelty assessment open |
| RX-Hall / monotone-potential programme | Active finite-to-symbolic programme. It is **not** an unrestricted theorem. It supplies general structural experiments and proof-critical exact finite exclusions in N32, N33 and the partial N34 route. Floating infeasibility is not accepted as a proof event. |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## 12 September follow-through: general structure and n=34 bound

The [general step-back package](releases/general-stepback-v1/README.md) records
the candidate balanced-degree theorem for every `n>=7`, the infinite family
`n>=35, Delta=n-15 => e(G)<=15 Delta`, and the fifteen-/sixteen-label tail bounds.
The balanced-degree theorem and the 7/12 result together confine any prospective
counterexample with `n>=7` to `ceil(n/2)+1 <= Delta < 7n/12`, conditional on
the current candidate arguments.

The [joint-clipping reviewer package](releases/general-joint-clipping-reviewer-v1/README.md)
now extends the scalar tail bounds to `a=17,...,23`, where `a=n-1-Delta`
is the number of labels in the canonical bridge:

| a | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Maximum Q | 32 | 35 | 39 | 42 | 46 | 49 | 54 |

The new recurrence keeps lower tails compatible. Clipping to maximum demand
five works through a=22; at a=23, retaining six gives the last bound. All 46
rows requiring joint treatment and the terminal arithmetic were rechecked by
a separately structured exact verifier. This is finite proof-critical
arithmetic, not an unrestricted scalar theorem.

The earlier sixteen-label note overstated the a=17 obstruction: the independent
estimate was inconclusive, while actual compatible clipping has minimum gain
`+2`. The actual `6^23 -> 5^23` counterexample remains preserved. A second
clarification makes explicit that the potential lemma's exact-balance multiplier
may have either sign. The [focused foundations audit](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md)
records these corrections and the primary-source dependency check.

For [n=34](releases/n34-bound-reviewer-v1/README.md), the candidate bound now
reaches **289 edges**, the conjectured value. The previous reductions close
all higher layers; the new 290-edge package excludes all 1,614 conservative
states with 662 hand/accounting arguments and 952 exact integer certificates.
A separate solver-free verifier passed 431,338 local integer inequalities.
The [new bridge refinements](project/research/general_n/2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md)
extract the exact demand-deficit identity and a tight heavy-label subset lemma.

Equality classification at 289 edges remains OPEN: its Delta=18 branch has
13,546 conservative states. Complete candidate bound-and-equality packages
therefore still reach n=33; the candidate upper bound now reaches n=34.

## 12 September milestone: fixed-order frontier extended through n=33

The current fixed-order candidate frontier now reaches orders 31, 32 and 33.

### n=31

Candidate:

```text
e(G) <= 240 = floor(31^2/4),
with equality exactly K(15,16).
```

Start with [`releases/n31-reviewer-v1/README.md`](releases/n31-reviewer-v1/README.md). The route is predominantly hand/structural:

- `Delta>=18` closes through the source-independent twelve-label theorem;
- `Delta=17` closes through the thirteen-label theorem plus its equality analysis;
- `Delta=16` closes by witness-deficit counting, with equality forcing `K(15,16)`.

The [complete proof](project/research/n31/2026-09-11-hand-route-v1/PROOF.md), [hostile internal audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md), [arithmetic regression](project/research/n31/2026-09-11-hand-route-v1/check_n31_arithmetic.py), and [thirteen-label theorem](project/research/general_n/2026-09-11-thirteen-label-tail-v1/THIRTEEN_LABEL_TAIL.md) are preserved. The hostile audit found no blocking flaw; it remains same-assistant internal evidence, not external validation.

### n=32

Candidate:

```text
e(G) <= 256 = floor(32^2/4),
with equality exactly K(16,16).
```

Start with [`releases/n32-reviewer-v1/README.md`](releases/n32-reviewer-v1/README.md), then the [complete reviewer-v1 proof](project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md) and [hostile internal audit](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md).

For `Delta=17`, put `(a,b)=(14,17)` and `t=m-255`.

- `m>=259` is excluded by the fourteen-label score bound `Q<=23` against `Q>=17+2t`.
- `m=258` reduces to the three score-maximising demand profiles `3^14`, `3,4^13`, `4^14`, all excluded by hand.
- `m=257` has an exact 71-profile score frontier. The 70 positive-demand profiles expand to 154 residual-tail states and are all excluded by one fixed nine-term monotone rectangle potential with exact integer acceptance. The unique zero-demand profile `0,3^13` is killed by a hand threshold-equality/endpoint-load contradiction. See [`N32_T2_RECTANGLE_POTENTIAL.md`](project/research/n32/2026-09-12-t2-frontier-v1/N32_T2_RECTANGLE_POTENTIAL.md).
- `m=256` is the equality layer and is fully covered by the exact certification package under [`project/research/n32/2026-09-12-equality-v1/`](project/research/n32/2026-09-12-equality-v1/README.md).

The `t=1` score frontier contains exactly 381 demand profiles. Monotone residual-tail closure exposes one apparent profile, `3^11,5^3`, as impossible before modelling. The remaining conservative finite domain is 1,984 positive-demand states and 61 zero-demand states. The frozen equality ledger is:

```text
pre-model monotone-tail arithmetic impossibility               1 profile
lifted N30-potential exact rational exclusions              1,369 states
full RX/Hall exact integer Farkas exclusions                  614 states
hand tight-threshold contradiction                              1 state
strengthened zero-demand exact integer Farkas exclusions       61 states
```

The unique full-RX survivor is `s=1^2,2^12`, `rho=1^10,2^7`; threshold equality gives at least 18 selected exceptions back into seven high residual sources while endpoint load/source forcing permit at most seven. The complete [certification ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) records the exact accounting and trust boundary.

At `Delta=16`, handshaking gives `m<=256`. Equality makes the graph 16-regular. In the dense non-bipartite case the witness degree-sum bound gives at most 31, contradicting regular degree sum 32; hence equality is bipartite and therefore `K(16,16)`.

No floating-point infeasibility is a proof event in the N32 package.

### n=33

Candidate:

```text
e(G) <= 272 = floor(33^2/4),
with equality exactly K(16,17).
```

Start with [`releases/n33-reviewer-v1/README.md`](releases/n33-reviewer-v1/README.md), the [complete candidate proof](project/research/n33/2026-09-12-candidate-v1/PROOF.md), and the [hostile internal audit](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md).

At `m>=272`, average degree gives `Delta>=17`.

- **`Delta=17`: entirely hand.** With deficits `epsilon_x=17-d(x)` and `T=561-2m`, witness deficit gives `2h+o<=T` and
  ```text
  m <= C(h,2)+h(33-h)+o(o-1).
  ```
  At `m>=273`, the exact maxima for `h=0,...,7` are `210,188,173,165,164,170,183,203`, all below 273. At `m=272`, the maxima are `272,242,219,203,194,192,197,209,228`, so equality uniquely forces `h=0,o=17`; the witness count then makes those 17 vertices independent and degree 16, forcing `K(17,16)`.
- **`Delta=18`:** `(a,b)=(14,18)`, benchmark 270. For `m>=273`, `t>=3`, so `Q>=24>23`. Equality `m=272` has `t=2` and is the sole new finite frontier.
- **`Delta=19`:** the thirteen-label theorem gives `Q<=21`, while `m>=272` gives `Q>=31`.
- **`Delta>=20`:** the twelve-label source-independent theorem puts the graph below 272; `Delta=32` is the universal-vertex star case.

For the sole new equality branch `(a,b,t)=(14,18,2)`, the independent fourteen-label checker enumerates all 20,058,300 nondecreasing demand multisets and finds exactly

```text
Q=22 : 18 profiles
Q=23 :  3 profiles
------------------
total: 21 profiles
```

All are positive. Monotone residual-tail closure and every allowed slack increment produce exactly **29** `(s,rho)` states: 18 at `Q=22` and 11 at `Q=23`.

The natural `b=18` lift of the N32 nine-rectangle potential preserves the same graph-level `h=R+x` cutoffs:

```text
4 B(2,0)+2 B(2,7)+B(2,9)+B(2,11)+B(2,14)+B(2,15)
          +B(3,10)+B(3,12)+B(3,13).
```

Holding those nine integer weights fixed, the exact finite verifier excludes **25/29** states. Floating LP proposes scalar envelope coefficients only; after one-sided envelope repair, every accepted row is rechecked in integer arithmetic. All 25 exactify at denominator 10,000, with strict gap numerators from `-9990` to `-9937`.

The four uncovered profiles are all hand-impossible:

```text
A: s=(3,4,5^12), rho=(1^6,3,4,5^10)
B: s=(3,5^13),   rho=(1^6,3,5^11)
C: s=(4^2,5^12), rho=(1^6,4^2,5^10)
D: s=(4,5^13),   rho=(1^6,4,5^11)
```

Their decisive contradictions are:

```text
A: refined h=4 heavy-incidence capacity <=62, but W_4=64;
B: exact h=4 capacity gives sum_Z p>=45, endpoint forcing gives <=44;
C: tight h=5 plus h=4 gives sum_Z p>=64, source bounds give <=54;
D: exact h=2 capacity gives sum_Z p>=63, endpoint forcing gives <=47.
```

Thus no full RX/Hall Farkas stage is needed in the final N33 route. The replay entry point is

```sh
bash project/research/n33/2026-09-12-candidate-v1/run_replay.sh
```

and the [N33 hostile internal audit](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md) found **no blocking flaw**. External review remains essential, particularly for the shared bridge, threshold-capacity equality, endpoint load/source forcing, and independent reproduction of the 21-profile / 29-state frontier.

N31, N32 and N33 remain **candidate mathematics** pending genuinely independent specialist review. No all-order conclusion is inferred from them.

## Public-review and integrity notes

The repository intentionally preserves failed approaches, bugs, superseded models and audit findings rather than silently rewriting them.

### Historical n=29 grouped-model normalization bug

During a restarted hostile audit of an additional n=29 `Delta=16` cumulative-threshold verifier, a **real normalization bug** was found in its first version: a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are invalid as proof evidence and are retained only as audit history. A corrected v2 replay produced zero survivors. This bug does not affect the current reviewer-v4 hand proof.

See the [public-release audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md) and [minimal-kernel report](project/reviews/n29/2026-09-08-redteam-restart-v1/MINIMAL_KERNEL_REPORT.json).

### Threshold-capacity explanatory typo

A proof-text audit found a non-blocking sign/order typo in an earlier explanatory sentence in the threshold-capacity derivation. The corrected sign is exactly the direction needed for the final inequality already used, so no numerical result or candidate status changed. Current reviewer-facing proofs state the corrected argument.

### Source-degree display erratum

A later audit found another non-blocking display typo in the frozen N29 bridge: an intermediate source-degree identity omitted the selected cross-degree `q_u`. The correct identity is

```text
d_H(u)=(rho_u+q_u)+(b-1-q_u-p_u)=rho_u+b-1-p_u.
```

The resulting supplement bound was already the one used by the models. The frozen appendix is preserved with the visible [erratum](project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md).

### Internal audits are not external review

Several routes have been reimplemented or hostile-reviewed by separate assistant instances or separately structured programs. Those checks materially reduce implementation and transcription risk, but the repository does **not** call them independent mathematical review. Specialist scrutiny of the graph-theoretic bridge remains essential.

## Fan-free status of the fixed-order candidates

Fan's 1987 density theorem is historical attribution only, not a logical dependency of the current fixed-order candidates.

For `n=25,27,28,29,30`, direct order-specific upper-range replacements were constructed and audited in [`FAN_FREE_REDUCTION.md`](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md) and later simplified in [`POINTWISE_CAPS.md`](project/research/fan-free-fixed-orders/2026-09-11-pointwise-analytic-caps-v1/POINTWISE_CAPS.md). The associated [Fan-free audit](project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md) found no blocking coverage defect.

The N31, N32 and N33 candidate proofs were assembled without invoking Fan's density theorem in the first place. N32/N33 still use the separate Dailly–Foucaud–Hansberg dominating-edge result to dispose of the relevant dense non-bipartite dominating-edge case; that is a different external literature dependency and remains a review target.

Historical reviewer editions remain preserved unchanged.

## Fixed-order candidate results

### n=25

**Candidate:** `e(G) <= 156`, equality only `K(12,13)`.

[Fan-free reviewer-v2 package](releases/n25-reviewer-v2/README.md) · [current proof](project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md) · [8 September re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md).

The complete finite domain has been replayed in 16 disjoint clean-runner shards: 543,578 outer states, 3,442,212 labelled columns and 1,959 independently reconstructed final equality certificates. Independent specialist review and novelty confirmation remain open.

### n=27

**Candidate:** `e(G) <= 182`, equality only `K(13,14)`.

[Fan-free reviewer-v2 package](releases/n27-reviewer-v2/README.md) · [current proof](project/reviews/n27/2026-09-09-fan-free-v2/PROOF.md) · [8 September red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md).

The hardened replay checks 80,978,546 canonical columns and independently reconstructs all 35,435 terminal source-cap vectors. Independent review remains open.

### n=28

**Candidate:** `e(G) <= 196`, equality only `K(14,14)`.

[Fan-free reviewer-v2 package](releases/n28-reviewer-v2/README.md) · [current proof](project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex) · [11 September analytic hardening](project/reviews/n28/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md) · [red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md).

A later hand cap makes the historical zero-domain computation over the highest `Delta=15` edge range corroborative rather than proof-critical. Independent review remains open.

### n=29

**Candidate:** `e(G) <= 210`, equality exactly `K(14,15)`.

[Reviewer-v4 package](releases/n29-reviewer-v4/README.md) · [canonical proof](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md) · [hostile audit](project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md) · [threshold-tail hand proof](project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md).

The proof is now predominantly hand/structural. The difficult `Delta=16` branch is completely closed by `Q>=16+2t` against the hand theorem `Q<=18`. Historical LP/Farkas evidence is retained only as corroboration. Independent mathematical review remains open.

### n=30

**Candidate:** `e(G) <= 225`, equality exactly `K(15,15)`.

[Reviewer-v3 package](releases/n30-reviewer-v3/README.md) · [self-contained proof](project/reviews/n30/2026-09-11-reviewer-v3/PROOF.md) · [editorial/dependency review](project/reviews/n30/2026-09-11-reviewer-v3/EDITORIAL_REVIEW.md).

`Delta>=17` closes through the source-independent twelve-label theorem; `Delta=15` equality is direct; `Delta=16` is handled by hand classification plus explicit residual-tail and endpoint integer tables. Independent specialist review remains open.

### n=31

**Candidate:** `e(G) <= 240`, equality exactly `K(15,16)`.

[Reviewer-v1 source package](releases/n31-reviewer-v1/README.md) · [proof](project/research/n31/2026-09-11-hand-route-v1/PROOF.md) · [hostile audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md).

The proof is predominantly hand/structural. External specialist review remains open.

### n=32

**Candidate:** `e(G) <= 256`, equality exactly `K(16,16)`.

[Reviewer-v1 source package](releases/n32-reviewer-v1/README.md) · [proof](project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md) · [hostile audit](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md) · [equality certification ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md).

The high-degree range and 258-edge endpoint are hand-closed. The 257-edge level uses a compact exact nine-rectangle finite certificate plus one hand zero-demand contradiction. The 256-edge `Delta=17` equality layer uses the exact ledger above. Independent review remains open.

### n=33

**Candidate:** `e(G) <= 272`, equality exactly `K(16,17)`.

[Reviewer-v1 source package](releases/n33-reviewer-v1/README.md) · [proof](project/research/n33/2026-09-12-candidate-v1/PROOF.md) · [hostile audit](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md) · [replay index](project/research/n33/2026-09-12-candidate-v1/README.md).

The new proof surface is smaller than N32: the `Delta=17` equality branch is fully hand-rigid, and the sole new `(a,b,t)=(14,18,2)` frontier has only 29 residual states. Twenty-five are excluded by the shifted nine-rectangle potential with exact integer acceptance and four by explicit hand threshold arguments. No full RX/Hall Farkas stage is proof-critical. Independent review remains open.

### n=34: conjectured bound reached; equality open

**Candidate:** `e(G)<=289=floor(34^2/4)`.

[Bound reviewer-v1 package](releases/n34-bound-reviewer-v1/README.md)
· [proof and exact ledger](project/research/n34/2026-09-12-m290-v1/README.md)
· [solver-free verifier](project/research/n34/2026-09-12-m290-v1/verify.py)
· [internal audit](project/research/n34/2026-09-12-m290-v1/AUDIT.md).

The 290-edge branch is fully excluded: 463 states fail exact degree mass,
199 have hand threshold contradictions, and 952 have exact integer
certificates. All earlier higher-layer reductions remain in force.
K(17,17) attains 289 edges, but uniqueness is OPEN: the Delta=18 equality
branch retains 13,546 conservative states. Independent specialist review,
novelty assessment and external reproduction remain open.

## General structural programme

### Strongest current maximum-degree candidate: 7/12

The strongest reviewer-packaged general maximum-degree candidate is

```text
n >= 6 and Delta(G) >= (7/12)n
    ==> e(G) < floor(n^2/4).
```

[Reviewer release](releases/general-7-12-reviewer-v1/README.md) · [standalone proof](project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md) · [hostile audit](project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md).

The scalar estimate gives

```text
t < 5a^2/128 + a/8.
```

Two separately structured exact checkers agree on the scalar arithmetic and finite assembly exceptions. Their large-`n` regressions are consistency checks, not proof by extrapolation. The main trust boundary is the shared graph-to-demand/profile-integral machinery. The associated ceiling analysis places the asymptotic limit of the current scalar-uniform architecture near `0.582066`, close to `7/12`; significant improvement is therefore expected to require more joint profile information.

Retained predecessors are the [293/500 release](releases/general-293-500-reviewer-v1/README.md) and [13/22 release](releases/general-13-22-reviewer-v1/README.md). None of these profile-integral theorems is needed by the current N29–N33 fixed-order proof routes.

### RX-Hall / monotone-potential programme

The active structural programme lives under [`project/research/general_n/2026-09-09-rx-hall-v1/`](project/research/general_n/2026-09-09-rx-hall-v1/README.md).

A selected incidence carries the coordinatewise compatibility

```text
(s,d,v) <= (rho,alpha,w),
```

so every coordinatewise nondecreasing potential yields a valid incidence-transport inequality. This provides a common language for BC rectangles, first-coordinate/SH thresholds, diagonal slack thresholds and analytic min-hinges.

Important exact finite milestones include:

- `n=29,t=3`: a nine-min-hinge exact analytic compression over all 94 hard profiles;
- `n=30,t=1`: a 13-generator 3-D potential with exactly two scalar templates for the seven preserved hard profiles;
- `n=29,t=2`: an 11-term 3-D potential with exactly three scalar templates over all 902 profiles;
- `n=29,t=3`: a simpler fixed potential requiring exactly four scalar templates;
- `n=32,t=2`: the proof-critical nine-rectangle common potential excluding all 154 positive-demand 257-edge states;
- `n=32,t=1`: the proof-critical two-stage exact finite equality replay;
- `n=33,t=2`: the shifted nine-rectangle potential excluding 25/29 equality states, with the four failures resolved by hand;
- `n=34,t=4`: two exact certificates exclude the 292-edge layer;
- `n=34,t=3`: 109 exact certificates and the tight-threshold hand lemma exclude all 110 states at 291 edges;
- `n=34,t=2`: exact degree mass, total/subset threshold hand lemmas and 952 integer envelopes exclude all 1,614 states at 290 edges.

The earlier `t+1` scalar-template pattern observed in the N29/N30 laboratories remains a **falsification target only**. N32/N33 should not be retrofitted into that pattern without a new parameterized theorem.

The RX-Hall programme therefore has both exploratory and fixed-order proof roles, but still does **not** constitute an unrestricted Murty–Simon theorem. Any general promotion depends first on independent review of the universal graph-to-incidence bridge and the monotone potential-certificate lemmas.

### Canonical bridge and threshold-tail family

The canonical selected/residual bridge is preserved at [`project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md). Its key consequences include the exact ledger, demand inequality, residual activity, selected-incidence forcing, endpoint load, source/supplement constraints and threshold capacity.

The source-independent twelve-label theorem, thirteen-label theorem and fourteen-label theorem form the hand core of the fixed-order tail sequence. The fifteen-/sixteen-label results add explicit finite terminal tables; the joint-clipping package extends scalar bounds through twenty-three labels with proof-critical exact arithmetic.

These structures now give the candidate conjectured bound at n=34. **Its equality classification remains OPEN, and no unrestricted all-order result is claimed.**

## Review-paper / package index

Historical packages remain preserved. N31, N32 and N33 are currently source-first Markdown/replay packages rather than PDF releases.

| Scope | Proof / paper | Evidence / review |
|---|---|---|
| n=25 | [Reviewer manuscript v2](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf) |
| n=27 | [Reviewer manuscript v2](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf) |
| n=28 | [Reviewer manuscript v2](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf) |
| n=29 | [Reviewer manuscript v4](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) | [Verification companion v4](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf); [hostile audit](project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md) |
| n=30 | [Reviewer manuscript v3](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf); [portable ZIP](releases/n30-reviewer-v3/N30_Reviewer_Package_v3.zip) | [Verification companion v3](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf) |
| n=31 | [Reviewer-v1 source package](releases/n31-reviewer-v1/README.md) | [Hostile internal audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md) |
| n=32 | [Reviewer-v1 source package](releases/n32-reviewer-v1/README.md) | [Hostile internal audit](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md); [exact equality ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) |
| n=33 | [Reviewer-v1 source package](releases/n33-reviewer-v1/README.md) | [Hostile internal audit](project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md); [exact replay](project/research/n33/2026-09-12-candidate-v1/README.md) |
| n=34 bound | [Bound reviewer-v1 source package](releases/n34-bound-reviewer-v1/README.md) | [Internal audit](project/research/n34/2026-09-12-m290-v1/AUDIT.md); [complete 290-edge verification](project/research/n34/2026-09-12-m290-v1/verification.json); equality classification OPEN |
| **General 7/12** | [Reviewer manuscript](releases/general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf) |
| General step-back | [Balanced-degree / fixed-a source package](releases/general-stepback-v1/README.md) | [Internal audit](project/reviews/general-theory/2026-09-12-stepback-v1/HOSTILE_AUDIT.md) |
| Joint clipping / historical N34 upper layers | [Reviewer-v1 source package](releases/general-joint-clipping-reviewer-v1/README.md) | [Focused foundations audit](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md); [N34 exact verification](project/research/n34/2026-09-12-frontier-v1/upper_layer_verification.json) |
| General 293/500 | [Reviewer manuscript](releases/general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf) |
| General 13/22 | [Reviewer manuscript](releases/general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf) |

For the canonical package list and status wording, use [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md).

## Governance and limits

**No complete fixed-order candidate above n=33, no proof through n=1,000, no unrestricted all-order solution, no novelty determination, no full formal verification and no external endorsement are claimed.**

Finite arithmetic states are necessary-condition systems, not graphs. Exact rejection of those states is mathematically useful only if the graph-to-model implications are correct. Saved actual-graph regressions contain no positive-surplus graph; they are regression tests, not a substitute for universal proof.

Paul Lenz directed the project. ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Same-assistant independent implementations and hostile audits are explicitly not described as external independent review.

Frozen fixed-order proofs, original archives, failed approaches, correction notes and the governed theorem ledger remain preserved. The README immediately preceding the n=29 publication remains at `project/reviews/history/README_before_n29_candidate_2026-09-08.md`. See also [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [repository sync policy](project/REPO_SYNC_POLICY.md), and the [theorem ledger](repro-v1/ledger/theorem_ledger.json).

## Review and corrections

Please use [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and open a GitHub Issue for suspected errors. Corrections should preserve the original failure evidence, identify the first invalid implication as precisely as possible, and state clearly which downstream claims are affected.

## Licence

MIT — see [`LICENSE`](LICENSE).
