# Murty–Simon / Erdős Problem #742

Candidate proofs and reproducible research. **Updated 12 September 2026. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** Repository publication, green replay and same-assistant hostile audit are not external acceptance and do not prove the unrestricted conjecture.

**External reviewers:** start with [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md). The canonical theorem-level packages are indexed in [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md). The project actively welcomes hostile review, counterexamples, literature corrections and genuinely independent reproduction; GitHub Issues are the preferred place to report a suspected flaw.

## Current headline status

| Scope | Current project status |
|---|---|
| `n=25` | Complete candidate: `e(G) <= 156`, equality exactly `K(12,13)`; Fan-free reviewer-v2; complete partitioned replay and independent endpoint reconstruction green; external specialist review open |
| `n=27` | Complete candidate: `e(G) <= 182`, equality exactly `K(13,14)`; Fan-free reviewer-v2; hardened replay green; external review open |
| `n=28` | Complete candidate: `e(G) <= 196`, equality exactly `K(14,14)`; Fan-free reviewer-v2 plus 11 September analytic hardening; external review open |
| `n=29` | Complete candidate: `e(G) <= 210`, equality exactly `K(14,15)`; reviewer-v4; difficult `Delta=16` branch is now hand-closed by threshold-tail compression; hostile internal audit found no blocking flaw; external review open |
| `n=30` | Complete candidate: `e(G) <= 225`, equality exactly `K(15,15)`; reviewer-v3; hand lemmas plus explicit proof-critical integer tables; internal arithmetic reproduced; external review open |
| `n=31` | Complete candidate: `e(G) <= 240`, equality exactly `K(15,16)`; source-first reviewer-v1; predominantly hand/structural route using the thirteen-label theorem and witness-deficit equality; hostile internal audit found no blocking flaw; external review open |
| `n=32` | Complete candidate: `e(G) <= 256`, equality exactly `K(16,16)`; source-first reviewer-v1; `m>=258` hand-closed, 257-edge branch has exact nine-rectangle closure, and the 256-edge equality branch has a complete exact replay plus one hand tight-threshold contradiction; hostile internal audit found no blocking flaw; external review open |
| General maximum-degree result | Candidate theorem: `n >= 6` and `Delta(G) >= (7/12)n` imply `e(G) < floor(n^2/4)`; complete candidate hand argument with internal exact audits green; external review and novelty assessment open |
| RX-Hall / 3-D potential programme | Active finite-to-symbolic programme. It remains **not** an unrestricted theorem. It now has two roles: general structural experimentation, and proof-critical exact finite exclusion inside the N32 `Delta=17` package. All computational exclusions used there are exactified; floating infeasibility is not accepted as a proof event. |

The unrestricted Murty–Simon conjecture remains unsolved by this project.

## 12 September milestone: fixed-order frontier extended through n=32

The current fixed-order candidate frontier now reaches orders 31 and 32.

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

The [complete proof](project/research/n31/2026-09-11-hand-route-v1/PROOF.md), [hostile internal audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md), [arithmetic regression](project/research/n31/2026-09-11-hand-route-v1/check_n31_hand_route.py), and [thirteen-label theorem](project/research/general_n/2026-09-11-thirteen-label-tail-v1/THIRTEEN_LABEL_TAIL.md) are preserved. The hostile audit found no blocking flaw; it remains same-assistant internal evidence, not external validation.

### n=32

Candidate:

```text
e(G) <= 256 = floor(32^2/4),
with equality exactly K(16,16).
```

Start with [`releases/n32-reviewer-v1/README.md`](releases/n32-reviewer-v1/README.md), then the [complete reviewer-v1 proof](project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md) and [hostile internal audit](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md).

For `Delta=17`, put `(a,b)=(14,17)` and `t=m-255`.

- `m>=259` is excluded immediately by the fourteen-label score bound `Q<=23` against `Q>=17+2t`.
- `m=258` (`t=3`) reduces to the three score-maximising demand profiles `3^14`, `3,4^13`, `4^14`; all three are excluded by hand in [`project/research/n32/2026-09-11-hand-route-v1/`](project/research/n32/2026-09-11-hand-route-v1/).
- `m=257` (`t=2`) has an exact 71-profile score frontier. The 70 positive-demand profiles expand to 154 residual-tail states and are all excluded by one fixed nine-term monotone rectangle potential with exact integer acceptance. The unique zero-demand profile `0,3^13` is killed by a hand threshold-equality/endpoint-load contradiction. See [`N32_T2_RECTANGLE_POTENTIAL.md`](project/research/n32/2026-09-12-t2-frontier-v1/N32_T2_RECTANGLE_POTENTIAL.md).
- `m=256` (`t=1`) is the equality layer and is fully covered by the exact certification package under [`project/research/n32/2026-09-12-equality-v1/`](project/research/n32/2026-09-12-equality-v1/README.md).

The `t=1` score frontier contains exactly 381 demand profiles:

```text
Q=19 : 206
Q=20 : 104
Q=21 :  50
Q=22 :  18
Q=23 :   3
```

Monotone residual-tail closure exposes one apparent profile, `3^11,5^3`, as impossible before modelling. The remaining conservative finite domain is 1,984 positive-demand states and 61 zero-demand states. The frozen equality ledger is:

```text
pre-model monotone-tail arithmetic impossibility               1 profile
lifted N30-potential exact rational exclusions              1,369 states
full RX/Hall exact integer Farkas exclusions                  614 states
hand tight-threshold contradiction                              1 state
strengthened zero-demand exact integer Farkas exclusions       61 states
```

The unique full-RX survivor is

```text
s   = 1^2,2^12,
rho = 1^10,2^7.
```

At threshold `h=2`, `W_2=24=C_2(7)`, so equality holds throughout the threshold-capacity chain. That forces at least 18 selected exceptions back into the seven high residual sources, while endpoint load and source forcing give `p_u<=1` for each of them, hence at most seven. The contradiction is written out in [`HAND_EXCEPTION.md`](project/research/n32/2026-09-12-equality-v1/HAND_EXCEPTION.md).

For the zero-demand sector, the replay correctly retains `d_i` and `R_i` separately and restores the exact degree-mass identity; it does not use the positive-demand compression `d_i=R_i+s_i`. The isolated-`C` lemma supplies `d_i<=12`. All 61 states have exact integer Farkas exclusions.

The complete [certification ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) records the exact accounting and trust boundary. The replay entry point is:

```sh
bash project/research/n32/2026-09-12-equality-v1/run_replay.sh
```

No floating-point infeasibility is a proof event in the N32 equality package. Floating solvers propose coefficients; accepted exclusions are verified in exact rational or integer arithmetic.

At `Delta=16`, handshaking gives `m<=256`. Equality makes the graph 16-regular. In the non-bipartite dense case the no-dominating-edge witness inequality gives witness degree sum at most 31, contradicting regular degree sum 32. Hence equality is bipartite; diameter two forces complete bipartite, and 32 vertices/256 edges force `K(16,16)`.

The [N32 hostile internal audit](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md) found **no blocking flaw**. Its highest-value external review targets are the universal selected/residual bridge, threshold-capacity equality, endpoint load/source forcing, completeness of the residual-tail expansion, the zero-demand state model and an independent clean replay.

Both N31 and N32 remain **candidate mathematics** pending genuinely independent specialist review. No all-order conclusion is inferred from them.

## Public-review and integrity notes

The repository intentionally preserves failed approaches, bugs, superseded models and audit findings rather than silently rewriting them.

### Historical n=29 grouped-model normalization bug

During the restarted hostile audit of an additional n=29 `Delta=16` cumulative-threshold verifier, a **real normalization bug** was found in its first version: a label-group multiplicity was counted twice. The v1 cumulative-threshold certificates are therefore invalid as proof evidence and are retained only as audit history. A corrected v2 replay produced zero survivors. This bug does not affect the current reviewer-v4 hand proof.

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

The N31 and N32 candidate proofs were assembled without invoking Fan's density theorem in the first place. N32 does use the separate Dailly–Foucaud–Hansberg dominating-edge result to dispose of the relevant dense non-bipartite dominating-edge case; that is a different dependency and remains an external literature input to review.

Historical reviewer editions remain preserved unchanged.

## Fixed-order candidate results

### n=25

**Candidate:** `e(G) <= 156`, equality only `K(12,13)`.

[Fan-free reviewer-v2 package](releases/n25-reviewer-v2/README.md) · [current proof](project/reviews/n25/2026-09-09-fan-free-v2/PROOF.md) · [8 September re-audit](project/reviews/n25/2026-09-08-reaudit-v1/README.md).

The complete finite domain has been replayed in 16 disjoint clean-runner shards: 543,578 outer states, 3,442,212 labelled columns and 1,959 independently reconstructed final equality certificates. The terminal re-audit imports no frozen verifier and independently reconstructs the source-cap endpoint. Independent specialist review and novelty confirmation remain open.

### n=27

**Candidate:** `e(G) <= 182`, equality only `K(13,14)`.

[Fan-free reviewer-v2 package](releases/n27-reviewer-v2/README.md) · [current proof](project/reviews/n27/2026-09-09-fan-free-v2/PROOF.md) · [8 September red-team audit](project/reviews/n27/2026-09-08-redteam-v1/REPORT.md).

The hardened replay checks 80,978,546 canonical columns and independently reconstructs all 35,435 terminal source-cap vectors. Independent review remains open.

### n=28

**Candidate:** `e(G) <= 196`, equality only `K(14,14)`.

[Fan-free reviewer-v2 package](releases/n28-reviewer-v2/README.md) · [current proof](project/reviews/n28/2026-09-09-fan-free-v2/PROOF.tex) · [11 September analytic hardening](project/reviews/n28/2026-09-09-fan-free-v2/ANALYTIC_HARDENING_2026-09-11.md) · [red-team report](project/reviews/n28/2026-09-07-redteam-v1/REPORT.md).

A later hand cap makes the historical zero-domain computation over the highest `Delta=15` edge range corroborative rather than proof-critical. Independent review remains open.

### n=29

**Candidate:**

```text
e(G) <= 210 = floor(29^2/4),
with equality exactly K(14,15).
```

[Reviewer-v4 package](releases/n29-reviewer-v4/README.md) · [canonical proof](project/reviews/n29/2026-09-11-reviewer-v4/PROOF.md) · [hostile audit](project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md) · [threshold-tail hand proof](project/research/general_n/2026-09-11-threshold-tail-collapse-v1/N29_DELTA16_THRESHOLD_TAIL_HAND_PROOF.md) · [frozen bridge](project/reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md).

The proof is now predominantly hand/structural. `Delta=15` is handled by witness-deficit counting and forces the equality graph. `Delta=16` is completely closed by a demand-only threshold-tail inequality: the bridge gives `Q>=16+2t`, while the hand clipping theorem gives `Q<=18`, so `t<=1`. `Delta=17` falls to a pointwise charging bound, higher degrees to the residual h-index machinery, and a universal vertex gives a star.

Historical LP/Farkas evidence is preserved as corroboration but is not proof-critical in reviewer-v4. A dedicated hostile internal audit found no blocking flaw. Independent mathematical review remains open.

### n=30

**Candidate:**

```text
e(G) <= 225 = floor(30^2/4),
with equality exactly K(15,15).
```

[Reviewer-v3 package](releases/n30-reviewer-v3/README.md) · [self-contained proof](project/reviews/n30/2026-09-11-reviewer-v3/PROOF.md) · [editorial/dependency review](project/reviews/n30/2026-09-11-reviewer-v3/EDITORIAL_REVIEW.md).

For `Delta>=17`, the source-independent twelve-label theorem closes the range and gives the stronger `m<=221` at `Delta=17`. `Delta=15` equality has a direct regularity/triangle-free proof. `Delta=16` is handled by a hand classification plus explicit residual-tail and endpoint integer tables; these finite tables remain proof-critical. A fresh implementation reproduces the displayed table arithmetic. Independent specialist review remains open.

### n=31

**Candidate:**

```text
e(G) <= 240 = floor(31^2/4),
with equality exactly K(15,16).
```

[Reviewer-v1 source package](releases/n31-reviewer-v1/README.md) · [proof](project/research/n31/2026-09-11-hand-route-v1/PROOF.md) · [hostile audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md).

The proof is predominantly hand/structural. `Delta>=18` closes through the twelve-label theorem, `Delta=17` through the thirteen-label theorem and its equality contradiction, and the balanced `Delta=16` branch through witness-deficit counting. The internal hostile audit found no blocking flaw; external specialist review remains open.

### n=32

**Candidate:**

```text
e(G) <= 256 = floor(32^2/4),
with equality exactly K(16,16).
```

[Reviewer-v1 source package](releases/n32-reviewer-v1/README.md) · [proof](project/reviews/n32/2026-09-12-reviewer-v1/PROOF.md) · [hostile audit](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md) · [equality certification ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) · [257-edge nine-rectangle closure](project/research/n32/2026-09-12-t2-frontier-v1/N32_T2_RECTANGLE_POTENTIAL.md).

The high-degree range and 258-edge endpoint are hand-closed. The 257-edge level uses a compact exact nine-rectangle finite certificate plus one hand zero-demand contradiction. The 256-edge `Delta=17` equality layer has the exact accounting displayed above: 1,369 lifted-potential certificates, 614 full-RX exact Farkas certificates, one hand survivor contradiction, 61 zero-demand exact Farkas certificates and one monotone-tail arithmetic impossibility. `Delta=16` equality is then forced to `K(16,16)` by regularity, the witness bound and bipartite diameter-two rigidity.

Same-assistant hostile audit found no blocking flaw. Independent mathematical review and independent computational reproduction remain open.

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

Retained predecessors are the [293/500 release](releases/general-293-500-reviewer-v1/README.md) and [13/22 release](releases/general-13-22-reviewer-v1/README.md). The 7/12 result supersedes them in threshold strength. None of these profile-integral theorems is needed by the current N29–N32 fixed-order proof routes.

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
- `n=32,t=1`: the proof-critical two-stage exact finite equality replay described above.

The earlier `t+1` scalar-template pattern observed in the N29/N30 laboratories remains a **falsification target only**. N32 should not be retrofitted into that pattern without a new parameterized theorem: its equality proof uses a different two-stage exact architecture plus a hand equality case.

The RX-Hall programme therefore has both exploratory and fixed-order proof roles, but it still does **not** constitute an unrestricted Murty–Simon theorem. Any general promotion depends first on independent review of the universal graph-to-incidence bridge and the monotone potential-certificate lemmas.

### Canonical bridge and threshold-tail family

The canonical selected/residual bridge is preserved at [`project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`](project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md). Its key consequences include the exact ledger, demand inequality, residual activity, selected-incidence forcing, endpoint load, source/supplement constraints and threshold capacity.

The source-independent twelve-label theorem, thirteen-label theorem and fourteen-label theorem form the current fixed-order tail sequence. They are especially valuable because they convert much of the difficult high-degree arithmetic into short hand inequalities and equality classifications.

These structures are promising for orders beyond 32, but **no candidate result for n=33 or any higher complete order is claimed here**.

## Review-paper / package index

Historical packages remain preserved. N31 and N32 are currently source-first Markdown/replay packages rather than PDF releases.

| Scope | Proof / paper | Evidence / review |
|---|---|---|
| n=25 | [Reviewer manuscript v2](releases/n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n25-reviewer-v2/N25_Verification_Companion_v2.pdf) |
| n=27 | [Reviewer manuscript v2](releases/n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n27-reviewer-v2/N27_Verification_Companion_v2.pdf) |
| n=28 | [Reviewer manuscript v2](releases/n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) | [Verification companion v2](releases/n28-reviewer-v2/N28_Verification_Companion_v2.pdf) |
| n=29 | [Reviewer manuscript v4](releases/n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) | [Verification companion v4](releases/n29-reviewer-v4/N29_Verification_Companion_v4.pdf); [hostile audit](project/reviews/n29/2026-09-11-reviewer-v4-redteam-v1/REPORT.md) |
| n=30 | [Reviewer manuscript v3](releases/n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf); [portable ZIP](releases/n30-reviewer-v3/N30_Reviewer_Package_v3.zip) | [Verification companion v3](releases/n30-reviewer-v3/N30_Verification_Companion_v3.pdf) |
| n=31 | [Reviewer-v1 source package](releases/n31-reviewer-v1/README.md) | [Hostile internal audit](project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md) |
| n=32 | [Reviewer-v1 source package](releases/n32-reviewer-v1/README.md) | [Hostile internal audit](project/reviews/n32/2026-09-12-reviewer-v1/HOSTILE_AUDIT.md); [exact equality ledger](project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) |
| **General 7/12** | [Reviewer manuscript](releases/general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf) |
| General 293/500 | [Reviewer manuscript](releases/general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf) |
| General 13/22 | [Reviewer manuscript](releases/general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) | [Verification companion](releases/general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf) |

For the canonical package list and status wording, use [`releases/REVIEW_READY_INDEX.md`](releases/REVIEW_READY_INDEX.md).

## Governance and limits

**No complete fixed-order candidate above n=32, no proof through n=1,000, no unrestricted all-order solution, no novelty determination, no full formal verification and no external endorsement are claimed.**

Finite arithmetic states are necessary-condition systems, not graphs. Exact rejection of those states is mathematically useful only if the graph-to-model implications are correct. Saved actual-graph regressions contain no positive-surplus graph; they are regression tests, not a substitute for universal proof.

Paul Lenz directed the project. ChatGPT/Geeps supplied mathematical development, software, manuscripts and internal checks. Same-assistant independent implementations and hostile audits are explicitly not described as external independent review.

Frozen fixed-order proofs, original archives, failed approaches, correction notes and the governed theorem ledger remain preserved. The README immediately preceding the n=29 publication remains at `project/reviews/history/README_before_n29_candidate_2026-09-08.md`. See also [standing orders](project/N25_PROJECT_STANDING_ORDERS.md), [repository sync policy](project/REPO_SYNC_POLICY.md), and the [theorem ledger](repro-v1/ledger/theorem_ledger.json).

## Review and corrections

Please use [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) and open a GitHub Issue for suspected errors. Corrections should preserve the original failure evidence, identify the first invalid implication as precisely as possible, and state clearly which downstream claims are affected.

## Licence

MIT — see [`LICENSE`](LICENSE).
