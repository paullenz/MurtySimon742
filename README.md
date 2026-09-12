# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 12 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication, green replay and same-assistant hostile audit are not external acceptance and do not prove the unrestricted conjecture.

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). The canonical theorem-level packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project actively welcomes hostile review, counterexamples, literature corrections and genuinely independent reproduction; GitHub Issues are the preferred place to report a suspected flaw.

## How this research develops general theory

Our aim is to extract structural principles that explain why a diameter-two
edge-critical graph cannot be too dense. Specific graph orders provide
manageable cases in which to develop those principles, find weaknesses in
proposed arguments, and identify hypotheses that a more general theorem needs.
Progress at finitely many orders does not, by itself, establish a result for
all orders.

The [canonical bridge](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md)
translates graph structure into demands, residual budgets and selected
incidences. We organise these constraints by `a=n-1-Delta`, `b=Delta` and
the edge surplus `t=e(G)-b(a+1)`. This lets different orders share the same
structural framework. The graph-to-constraint implications are mathematical
claims that must be reviewed separately from the arithmetic checking them.

The working cycle is:

1. **Reduce the problem structurally.** Prove necessary inequalities and
   identify a complete domain of remaining cases, keeping the assumptions
   and dependencies explicit.
2. **Use computation to investigate the difficult cases.** Search for useful
   inequalities and propose certificates. Accept a computational exclusion
   only after exact verification and complete coverage checks; a floating-point
   solver report, timeout or unsuccessful search is not proof.
3. **Extract simpler explanations.** Examine which constraints make a
   certificate work, then seek a short hand argument that retains the decisive
   information. Some finite certificates remain proof-critical; each package
   states where they are still required.
4. **Generalise with explicit hypotheses.** Formulate a parameterized lemma,
   prove its graph-level implications, and test its reach against preserved
   difficult cases and failed attempts. Infinite-family conclusions require
   an argument covering the whole family.

N34 provides a concrete example. Its final 12,570-variable certificate was
replaced by a [four-step load potential and short hand proof](project/reviews/n34/2026-09-12-heavy-independent-v1/HAND_PROOF.md).
Tracking how many selected incidences go to heavy labels exposed a useful
restriction on where their supplements can lie. Combined with endpoint loads,
this gives the candidate bound `6k<=r+6z`: k counts labels with demand at least
two, z counts sources with residual degree at least two, and r is the total
residual budget. The hypothesis is that every source counted by z has
supplement indegree at most four. The final N34 state would require `78<=74`.
The lemma is independent of the order 34, but its hypothesis must be checked
anew: the corresponding generic N35 source bound permits indegree five.

That mechanism now yields a [general heavy-load and routing family](releases/general-heavy-load-reviewer-v1/README.md)
for every heavy threshold h, with an explicit cost for large supplement
indegrees. It strengthens the h=2 case to `8k<=r+8z` when p<=6 and gives
new demand-only inequalities. A [joint routing continuation](releases/general-joint-routing-reviewer-v1/README.md)
now conditions on the number of heavy senders and limits how many of their
arcs each destination can receive. It supplies 729 further exact exclusions
after all earlier hand rules. A [demand/tail projection and closed equality rule](releases/general-routing-tail-reviewer-v1/README.md)
simplify that mechanism into profile-level statements, with zero further
exclusions among its 5,578 state survivors. A [destination-compatibility pilot](releases/general-compatible-routing-reviewer-v1/README.md)
now excludes 19 of a preselected 29-state sample: two from extending the old
multiplier search, one further from retaining selected degrees, and sixteen
further from destination eligibility. One exclusion has a compact hand proof.
Mixed traffic cuts add no further whole-state exclusions in the sample.
A frozen-catalogue test on the full pool is the next gate; the pilot rate is
not an estimate of full-pool coverage.

## Failures, audit challenges and corrections are part of the record

**We record failed approaches, counterexamples to proposed lemmas, unsuccessful
or incomplete computations, audit challenges, discovered bugs, corrections
and unresolved proof obligations alongside successful results.** These records
help explain which ideas failed, which hypotheses matter, and why the current
argument differs from an earlier version.

Our [preservation standing orders](project/N25_PROJECT_STANDING_ORDERS.md) require
every material result and failure to be saved with enough provenance for
reconstruction and audit: code, parameters, inputs, outputs, certificates,
survivor lists and review findings as applicable. Original evidence and
superseded arguments are retained. Invalidated evidence is clearly labelled
and excluded from the active proof chain. Missing original evidence is recorded
as a recovery obligation; a later reconstruction is identified as such.

For examples, see the preserved [N29 normalization bug and audit](project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md),
the [corrections from the general-foundations review](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md),
and the [N34 failed relaxation, separate normalization audit and hand replacement](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md).
When a challenge reveals a flaw, the goal is to identify the first invalid
implication, state which downstream claims are affected, and preserve the
correction trail. An unresolved challenge remains visible as an open obligation.

Exact replay, internal audit, repository publication and external mathematical
acceptance are distinct statuses. Same-assistant reimplementations can reduce
implementation risk; external specialist review and novelty assessment remain
OPEN. The repository is intended to make both the arguments and their history
available for that scrutiny.

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
| `n=34` | Complete candidate: `e(G)<=289`, equality exactly `K(17,17)`; reviewer-v2. All 13,546 equality states close by 6,709 hand/accounting arguments and 6,837 integer envelopes. The final heavy Farkas certificate is replaced by a short hand proof. External review OPEN. |
| `n=35` | Complete candidate: `e(G)<=306`, equality exactly `K(17,18)`; reviewer-v1. All 485 new states close by 228 hand/accounting arguments and 257 integer envelopes. External review OPEN. |
| Balanced-degree / fixed-a structural results | Candidate all-order balanced-degree reduction; infinite `a=14` high-b family; tail bounds through `a=23`, including joint clipping and an adaptive six-level boundary; proof-critical finite arithmetic where stated; external review open |
| Heavy-load / routing family | Candidate all-threshold hand inequalities, explicit incoming-degree penalties, and new demand-only tail bounds. Low-demand consequence: `s_i<=2, t>0, b-a<=5 => 9t+4(b-a)<=a`. Reviewer-v1; external review OPEN. |
| Joint heavy routing | Candidate general lemma coupling heavy-sender count, destination indegrees and pair capacity. Reviewer-v1; 729 further exclusions from a corrected pool of 6,307; 5,578 survive the frozen catalogue. External review OPEN. |
| Demand/tail projection and equality rigidity | Candidate general hand lemmas; reviewer-v1. Adds 114 whole layer/profile exclusions before residual enumeration and a closed strictness criterion. Adds no exclusions among the 5,578 joint-routing survivors. External review OPEN. |
| Compatible destination routing | Candidate general eligibility and mixed-traffic inequalities; reviewer-v1. Frozen 29-state pilot: 19 exact exclusions, including 16 beyond selected-degree retention; 10 survivors. Mixed cuts add zero further states. Full-pool replay pending; external review OPEN. |
| General maximum-degree result | Candidate theorem: `n >= 6` and `Delta(G) >= (7/12)n` imply `e(G) < floor(n^2/4)`; complete candidate hand argument with internal exact audits green; external review and novelty assessment open |
| RX-Hall / monotone-potential programme | Active finite-to-symbolic programme. It is **not** an unrestricted theorem. It supplies general structural experiments and proof-critical exact finite exclusions in N32, N33, N34 and N35. Floating infeasibility is not accepted as a proof event. |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

For research planning, the [12 September outcome assessment](project/assessments/2026-09-12-outcome-forecast-v1/ASSESSMENT.md)
separates correctness, originality, validation of existing general candidates,
further general advances and a complete proof. Its forecasts are explicitly
subjective, with a stated horizon and sensitivity scenarios; they are not
mathematical evidence or external endorsement.

## Compatible destination routing

The [compatible-routing reviewer-v1 package](releases/general-compatible-routing-reviewer-v1/README.md)
retains total selected degree and the requirement that a source of selected
degree q can send only to destinations with residual-plus-selected degree
at least q-1. Separate traffic bounds and mixed cuts give a general potential
envelope, with an exact count of heavy senders.

The preselected 29-state pilot compares four nested models: 2 exclusions from
unrestricted multiplier search in the old bound, 3 after retaining selected
degrees, 19 after destination eligibility, and 19 after mixed cuts. All 321
integer certificates and 321 extracted envelopes pass exact checks implemented
separately from discovery. The [compact hand example](project/research/general_n/2026-09-12-compatible-routing-pilot-v1/COMPACT_EXAMPLE.md)
requires capacity at least 659, while its only possible sender counts permit
at most 636 or 628.

All ten sample survivors, unsuccessful searches, original solver proposals,
rounding repairs and audit challenges are preserved. The full pool of 5,578
previous general-routing survivors has not been replayed under the new rules.
The next step is a small frozen catalogue tested across that pool. The pilot
adds structural understanding and alternative certificates; the N34/N35
candidate ledgers and 7/12 candidate remain unchanged. External review is OPEN.

## Demand/tail projection and equality rigidity

The [routing-tail reviewer-v1 package](releases/general-routing-tail-reviewer-v1/README.md)
removes the unknown residual-degree tuple from a joint-routing inequality.
If D is the residual budget left after proved lower tails, and d is their
last positive level, every source has `rho<=d+D`. Raising a tail consumes
this budget and tightens the cap. Zero remaining budget forces every tail.

A second hand lemma describes equality in the load bound. When incoming
degree is at most 3h, equality forces each heavy source to send h or 2h
heavy arcs; a 2h-sender has incoming degree zero. Destination capacity then
gives an explicit criterion making the load inequality strict by one unit.

Across 1,453 layer/profile instances, the projection adds **114 whole-profile
exclusions** beyond the preceding 45, leaving 1,294 profile survivors.
The scalar equality rule adds nine profile exclusions over the ordinary
load-cap test; those are included in the 114. Exact replay and the
[counterexample/audit record](project/research/general_n/2026-09-12-routing-tail-projection-v1/AUDIT.md)
are preserved.

**All 5,578 states surviving the previous joint-routing catalogue still
survive these tests.** This is a simplification into demand-level theory,
not a reduction of the remaining frontier by this package. The compatible
routing pilot above tests stronger supplement eligibility; fuller label/supplement
compatibility remains open. No improvement to
the 7/12 result or unrestricted conjecture proof is claimed; external review
and novelty assessment remain OPEN.

## Joint heavy routing

The [joint-routing reviewer-v1 package](releases/general-joint-routing-reviewer-v1/README.md)
combines the load potential with destination capacity. With j heavy senders,
a destination can receive at most j of their arcs, or j-1 when it is itself
one of those senders. The candidate hand lemma combines this with incoming
degree and one orientation per unordered pair, for arbitrary graph parameters.

A 27-case pilot found twelve new exclusions, including four beyond its
aggregate-routing variant. Twenty multiplier ratios extracted from those
witnesses then excluded **729 further states** across the full comparison
pool. Using the same catalogue, 563 of those exclusions require the sharper
destination term. Independent integer replay passes; **5,578 states survive**
this catalogue. Their profiles, failed searches, witnesses and audit remain
available. Survival is not graph feasibility.

The comparison pool was corrected from 6,499 to 6,307: 192 historically
solver-certified cases already failed an earlier hand rule skipped by their
original run ordering. The [audit](project/research/general_n/2026-09-12-joint-routing-pilot-v1/AUDIT.md)
records every removal and explains why those cases are not new progress.
Canonical N34/N35 ledgers and the 7/12 maximum-degree result remain unchanged;
external mathematical review and novelty assessment are OPEN.

## General heavy-load and routing: the new structural result

The [reviewer-v1 family](releases/general-heavy-load-reviewer-v1/README.md)
extends the N34 hand argument to every heavy threshold h. For heavy label
count k_h, high-residual source count z_h and residual budget r, it gives
`4h k_h<=r+4h z_h` when incoming degree is at most 3h. The full version retains
weighted demands and an explicit penalty for degrees above 3h. Its hand
proof also gives exact source-capacity formulas and new tail bounds.

For positive surplus and `b-a<=2h+1`, the penalty can be eliminated from a
demand-only inequality. In particular, `s_i<=2` and `b-a<=5` force
`9t+4(b-a)<=a`, without any cap on residual degrees. This is a candidate
infinite-family restriction under stated profile hypotheses.

The complete study supplies alternative hand exclusions for 595 states that
previously required envelopes, and rejects 45 layer/profile instances before
residual enumeration. It also preserves a clear limit: 8,280 states survive
the searched family, and wider cutoffs and individual capacity refinements
add no exclusions on that domain. The [audit and full evidence](project/research/general_n/2026-09-12-heavy-load-family-v1/README.md)
include successful witnesses, all survivors, failed local extensions and exact
replay. Existing fixed-order theorem statements and reviewer ledgers remain
unchanged; external review and novelty assessment are OPEN.

## 12 September follow-through: N34 hand simplification and complete N35 candidate

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

For [n=34](releases/n34-reviewer-v2/README.md), the candidate result remains
**e(G)<=289, with equality exactly K(17,17)**. Reviewer-v2 replaces the last
large Farkas certificate with a [short hand theorem](project/reviews/n34/2026-09-12-heavy-independent-v1/HAND_PROOF.md): if
all sources with residual degree at least two have supplement indegree at
most four, then `6k<=r+6z`. The exceptional state would require `78<=74`.
Its 13,546-state equality ledger now has 6,709 hand/accounting exclusions and
6,837 exact envelopes. A separate whole-count reconstruction also matched
every original model row and verified the translated certificate.

For [n=35](releases/n35-reviewer-v1/README.md), the new complete candidate is
**e(G)<=306, with equality exactly K(17,18)**. Only Delta=19 needs new finite
work: 19 states at 307 edges and 466 at 306 edges. All are excluded by 228
hand/accounting arguments and 257 exact envelopes, with 92,701 local integer
checks and no unresolved state. All three zero-demand states are covered.
The [proof](project/research/n35/2026-09-12-candidate-v1/PROOF.md) states the degree reduction, complete frontier,
exact certificate argument and external review boundary.

The fixed-order candidate frontier now reaches n=35. Independent specialist
review, novelty assessment and external reproduction remain OPEN.

## 12 September milestone: fixed-order frontier extended through n=35

The current fixed-order candidate frontier now reaches orders 31, 32, 33, 34 and 35.

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

### n=34 and n=35

The [N34 reviewer-v2 package](releases/n34-reviewer-v2/README.md) combines the
previous upper-bound argument with the complete equality replay and new hand
replacement. The [N35 reviewer-v1 package](releases/n35-reviewer-v1/README.md)
extends the candidate frontier to 306 edges, equality exactly K(17,18).
Their exact ledgers and proof dependencies are detailed below.

These remain **candidate mathematics** pending independent specialist review.
No unrestricted all-order conclusion is inferred from them.

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

The N31, N32, N33, N34 and N35 candidate proofs were assembled without invoking Fan's density theorem in the first place. N32/N33/N34/N35 still use the separate Dailly–Foucaud–Hansberg dominating-edge result to dispose of the relevant dense non-bipartite dominating-edge case; that is a different external literature dependency and remains a review target.

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

### n=34

**Candidate:** `e(G)<=289`, equality exactly `K(17,17)`.

[Reviewer-v2 package](releases/n34-reviewer-v2/README.md)
· [hand replacement and normalization audit](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md)
· [complete v2 equality replay](project/reviews/n34/2026-09-12-heavy-independent-v1/verify_v2.py).

All 13,546 Delta=18 equality states close by 6,709 hand/accounting arguments
and 6,837 integer envelopes. The remaining Delta=17 case forces K(17,17)
by the balanced-degree theorem. All 620 zero-demand states are covered.
The historical large certificate remains corroborating evidence.

### n=35

**Candidate:** `e(G)<=306`, equality exactly `K(17,18)`.

[Reviewer-v1 package](releases/n35-reviewer-v1/README.md)
· [complete proof](project/research/n35/2026-09-12-candidate-v1/PROOF.md)
· [exact replay](project/research/n35/2026-09-12-candidate-v1/verify.py)
· [focused internal audit](project/research/n35/2026-09-12-candidate-v1/AUDIT.md).

Delta=18 follows from the balanced-degree theorem; Delta=20 from the a=14
high-b theorem; Delta>=21 from the 7/12 theorem. At Delta=19, the fifteen-label
bound leaves only 307 and 306 edges. Their 19 and 466 states are all excluded
by 228 hand/accounting arguments and 257 exact envelopes. External specialist
review, novelty assessment and independent reproduction remain OPEN.

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
- `n=34,t=2`: exact degree mass, total/subset threshold hand lemmas and 952 integer envelopes exclude all 1,614 states at 290 edges;
- `n=34,t=1`: all 13,546 equality states close by 6,709 hand/accounting exclusions and 6,837 exact envelopes; the final Farkas exclusion is replaced by hand.
- `n=35,t=3,2`: all 485 states close by 228 hand/accounting exclusions and 257 exact envelopes.

The earlier `t+1` scalar-template pattern observed in the N29/N30 laboratories remains a **falsification target only**. N32/N33 should not be retrofitted into that pattern without a new parameterized theorem.

The RX-Hall programme therefore has both exploratory and fixed-order proof roles, but still does **not** constitute an unrestricted Murty–Simon theorem. Any general promotion depends first on independent review of the universal graph-to-incidence bridge and the monotone potential-certificate lemmas.

### General heavy-load and routing inequalities

The [new candidate family](releases/general-heavy-load-reviewer-v1/README.md)
combines endpoint loads, actual heavy selected degree and supplement routing.
It supplies all-threshold inequalities with explicit incoming-degree penalties,
exact elementary source maxima, and demand-only tail refinements. Its measured
reach and failed extensions are recorded in the structural-result section above.

The 595 alternative envelope exclusions do not silently change the canonical
N34/N35 ledgers. The subsequent joint-routing and compatible-routing packages
above test destination constraints against preserved survivors.

### Canonical bridge and threshold-tail family

The canonical selected/residual bridge is preserved at [`project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md). Its key consequences include the exact ledger, demand inequality, residual activity, selected-incidence forcing, endpoint load, source/supplement constraints and threshold capacity.

The source-independent twelve-label theorem, thirteen-label theorem and fourteen-label theorem form the hand core of the fixed-order tail sequence. The fifteen-/sixteen-label results add explicit finite terminal tables; the joint-clipping package extends scalar bounds through twenty-three labels with proof-critical exact arithmetic.

These structures now give the complete candidate bound and equality classification at n=35. **No unrestricted all-order result is claimed.**

## Review-paper / package index

Historical packages remain preserved. N31, N32, N33, N34 and N35 are currently source-first Markdown/replay packages rather than PDF releases.

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
| n=34 | [Reviewer-v2 source package](releases/n34-reviewer-v2/README.md) | [Normalization audit and hand proof](project/reviews/n34/2026-09-12-heavy-independent-v1/README.md); [complete equality replay](project/reviews/n34/2026-09-12-heavy-independent-v1/v2_verification.json) |
| n=35 | [Reviewer-v1 source package](releases/n35-reviewer-v1/README.md) | [Internal audit](project/research/n35/2026-09-12-candidate-v1/AUDIT.md); [complete exact replay](project/research/n35/2026-09-12-candidate-v1/verification.json) |
| **General 7/12** | [Reviewer manuscript](releases/general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf) |
| Heavy-load / routing family | [Reviewer-v1 source package](releases/general-heavy-load-reviewer-v1/README.md) | [Hand proof](project/research/general_n/2026-09-12-heavy-load-family-v1/HEAVY_LOAD_FAMILY.md); [internal audit and exact applications](project/research/general_n/2026-09-12-heavy-load-family-v1/README.md) |
| Joint heavy routing | [Reviewer-v1 source package](releases/general-joint-routing-reviewer-v1/README.md) | [Hand lemma and exact applications](project/research/general_n/2026-09-12-joint-routing-pilot-v1/README.md) |
| Demand/tail projection | [Reviewer-v1 source package](releases/general-routing-tail-reviewer-v1/README.md) | [General lemmas and negative frontier result](project/research/general_n/2026-09-12-routing-tail-projection-v1/README.md) |
| Compatible destination routing | [Reviewer-v1 source package](releases/general-compatible-routing-reviewer-v1/README.md) | [Compact hand proof](project/research/general_n/2026-09-12-compatible-routing-pilot-v1/COMPACT_EXAMPLE.md); [audit and bounded pilot](project/research/general_n/2026-09-12-compatible-routing-pilot-v1/AUDIT.md) |
| General step-back | [Balanced-degree / fixed-a source package](releases/general-stepback-v1/README.md) | [Internal audit](project/reviews/general-theory/2026-09-12-stepback-v1/HOSTILE_AUDIT.md) |
| Joint clipping / historical N34 upper layers | [Reviewer-v1 source package](releases/general-joint-clipping-reviewer-v1/README.md) | [Focused foundations audit](project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md); [N34 exact verification](project/research/n34/2026-09-12-frontier-v1/upper_layer_verification.json) |
| General 293/500 | [Reviewer manuscript](releases/general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf) |
| General 13/22 | [Reviewer manuscript](releases/general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf) |

For the canonical package list and status wording, use [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md).

## Governance and limits

**No complete fixed-order candidate above n=35, no proof through n=1,000, no unrestricted all-order solution, no novelty determination, no full formal verification and no external endorsement are claimed.**

Finite arithmetic states are necessary-condition systems, not graphs. Exact rejection of those states is mathematically useful only if the graph-to-model implications are correct. Saved actual-graph regressions contain no positive-surplus graph; they are regression tests, not a substitute for universal proof.

Paul Lenz directed the project. ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Same-assistant independent implementations and hostile audits are explicitly not described as external independent review.

Frozen fixed-order proofs, original archives, failed approaches, correction notes and the governed theorem ledger remain preserved. The README immediately preceding the n=29 publication remains at `project/reviews/history/README_before_n29_candidate_2026-09-08.md`. See also [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [repository sync policy](project/REPO_SYNC_POLICY.md), and the [theorem ledger](repro-v1/ledger/theorem_ledger.json).

## Review and corrections

Please use [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and open a GitHub Issue for suspected errors. Corrections should preserve the original failure evidence, identify the first invalid implication as precisely as possible, and state clearly which downstream claims are affected.

## Licence

MIT — see [`LICENSE`](LICENSE).
