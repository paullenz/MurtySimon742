# Daily adversarial audit - independent Erdos #742 programme

**Audit date:** 22 September 2026  
**Audited interval:** 21 September 2026 00:00:38 BST to 22 September 2026 00:00:44 BST  
**Audited predecessor:** `0d11049574fce97f4630a4b71e8da78edbb7836c`  
**Mode:** adversarial audit, not forward theorem research

## Executive verdict

The 21 September pivot generated one focused independent-#742 session.  Its main
claim survives this audit at the repository's candidate/internal-review level:

\[
n\ge 6,\qquad \Delta(G)\ge {250n\over429}
\quad\Longrightarrow\quad
e(G)<\left\lfloor {n^2\over4}\right\rfloor .
\]

This is a strict improvement on the preserved candidate `7/12` threshold and
shrinks the live maximum-degree strip to

```text
n/2 < Delta(G) < 250n/429.
```

The audit independently replayed the rational scalar certificate, the convex
degree assembly, all eight exceptional `a` rows, the inherited `7/12` exact
checker and the threshold-capacity algebra.  All executed checks passed.  No
hidden use of the external `Erdos742/Erdos742` `e+disj+X` proof was found in the
new package or its inherited profile proof.  The route uses the project's
complement/quasi-edge, selected/residual, Hall and profile machinery.

This is not a proof of Erdos #742.  The remaining strip is nonempty, the shared
graph-to-profile spine remains internally rather than externally reviewed, and
the equality characterization is still open in the strip.  In particular,
balanced complete bipartite graphs on odd order have `Delta=(n+1)/2` and lie in
the remaining strip; any rigidity theorem must preserve rather than exclude
that geometry.

The audit found one real scope defect in
`POSITIVE_DENSITY_CODEGREE_CLUSTER.md`.  Its displayed hypotheses omitted the
lower-degree and selected-endpoint assumptions required by robust signature
stability and stated only `Q>=a^2/4`, although the upstream average bound uses
`Q<=a^2/4`.  The exact plateau conclusion is repairable because the intended
normalization has `Q=a^2/4`; the document and indexes have been narrowed to the
correct joint hypotheses.  The threshold theorem is unaffected.

## Focused-session gate

- Pivot commit: `5825c203da78ecaefaa63568f0883de25518df9f`.
- Completed focused independent-#742 sessions: **1**.
- The 24-session go/no-go gate is therefore **not yet due**.
- Session 1 already meets the gate's success criterion by producing a strict
  threshold improvement below `7/12` and a graph-realizability obstruction.
  This is evidence to continue through the gate, not permission to remove it.

## Material claims and audit disposition

| Claim | Evidence replayed | Disposition |
|---|---|---|
| `f(x)<121/1569` on `[0,1]` | exact rational root bracket and monomial upper bound in `check_39_67.py` | verified arithmetic |
| `t<121a^2/3138+a/8` | graph-to-profile replay plus scalar bound | candidate, conditional on shared graph bridge |
| all-order `250/429` threshold | convex assembly, `a>=65`, exact scan of `2<=a<=64`, eight inherited finite certificates | candidate theorem survives |
| `39/67` for `n>=4681` and threshold/order ladder | exact forward differences and exhaustive diagnostic through `n=10000` | candidate corollaries survive |
| uniform scalar plateau and ceiling `alpha_*=0.582065...` | calculus and numerical cross-check | valid obstruction to the decoupled scalar method |
| rational demand-`1/4`, `b/a=139/100` full-Hall plateau | rational margins and matrix-capacity replay | asymptotic relaxation only; not a graph |
| signature-union theorem `(SU1)-(SU5)` | direct set containment, support bound and triple double-count | candidate lemma survives inherited domination premise |
| robust signature stability `(RS)` | monotonicity, Cauchy and numerator/denominator bounds | candidate lemma survives at stated hypotheses |
| positive-density high-codegree corollary | arithmetic valid, theorem statement incomplete/inconsistent | **scope repaired; no longer cited as a broad band theorem** |
| balanced complete-bipartite equality | checked against degree regions | not excluded; equality classification remains open |

### Exact checker identifiers and results

The following all returned `PASS` during this audit:

- `check_39_67.py`;
- `check_full_hall_plateau.py`;
- `check_signature_union.py`;
- `check_robust_signature_stability.py`;
- `check_codegree_cluster.py` (arithmetic only; corrected hypotheses are in prose);
- `check_threshold_algebra.py` - 177,120 integer triples;
- `check_degree_regression.py` - 233,515 below-`7/12` degree pairs through `n=10000`;
- inherited `src/check_7_12.py` - 5,207,079 eligible degree pairs through `n=5000` plus all exact finite certificates.

Exact computation verifies the stated arithmetic and finite scans.  It does
not by itself verify the graph-to-profile construction or graph realizability.

## Load-bearing graph-to-profile review

The hostile replay in `GRAPH_TO_THRESHOLD_HOSTILE_REPLAY.md` was checked
against the canonical `7/12` proof.  The complement ledger, source-demand
injection, threshold sets and Cauchy projection have consistent quantifiers.
The supplement step correctly needs the residual-or-selected dichotomy; it
would be false if every supplement-label edge were simply called residual.

The most concentrated remaining trust risk is therefore the shared
graph-to-profile bridge as a whole, not the new rational optimization.  A
reviewer should reconstruct the selected quasi-edge choice, pair uniqueness,
the source-demand injection and threshold-capacity count directly from D2C
criticality before promoting `250/429` beyond candidate status.

## Independence review

Repository search found no invocation of the external universal `e+disj+X`
inequality in the independent strip package or the inherited `7/12` proof.
The common vocabulary is ordinary D2C complement/quasi-edge language.  On the
available evidence the route is structurally independent.  This is a source
dependency audit, not a theorem of intellectual independence; an external
reviewer should still compare proof cores before making a novelty claim.

## Equality geometry

The high-degree theorem is strict and therefore safely excludes equality only
for `Delta>=250n/429`.  The elementary degree-sum side deals with
`Delta<=n/2`.  The gap between them contains the expected equality examples:

- for even `n`, `K_{n/2,n/2}` has `Delta=n/2`;
- for odd `n`, `K_{(n-1)/2,(n+1)/2}` has `Delta=(n+1)/2>n/2`.

The plateau rigidity lemmas concern positive selected demand and explicitly do
not apply to the zero-demand complete-bipartite boundary.  Future strip
closure must therefore have a separate zero-demand/equality branch or a
stability theorem whose equality case is visibly complete bipartite.

## Earlier work in the audited day

Before the 19:23 BST pivot, the repository added a large eventual-D2C/Q3
package: equality-face repairs, raw one-code boundary routing, Q3 halfcube and
star-support classifications, actual D2C blow-up controls, an exactly-four-
centre closure and five-centre families.  These claims are not dependencies of
the new `250/429` theorem and remain preserved at their prior internal trust
levels.  This audit did not promote them.  Known same-day failures and repairs
remain visible, including the asymmetric rigid-cut scanner bug, the false
single-class obstruction, the invalid matching-one/cancellation guesses and
the corrected odd-`u` five-centre gap formula.

## Session-utilisation audit

Forward triggers were scheduled hourly at `HH:00:38` for `01<=HH<=23`.
Multiple records naming the same trigger are segments of one slot.  Missing or
`PENDING` boundaries are not reconstructed from commits or prose.

| Trigger BST | Earliest start | Evidenced forward stop | Preservation complete | Wall span | Forward span | Units | Classification / stop | >=50m |
|---|---|---|---|---:|---:|---:|---|---|
| 01:00:38 | 01:00:26 | initial PENDING; continuation 01:48:32 | initial PENDING; later 01:50:38, 01:59:20 | UNVERIFIED | >=20m59s | 27 | split/re-entered; final segment post-cutoff | UNVERIFIED |
| 02:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 03:00:38 | 03:00:51 | initial PENDING; late segment 03:59:26 | 04:00:45 for late segment | UNVERIFIED | UNVERIFIED | 3 | late delivery segment; initial close missing | UNVERIFIED |
| 04:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 05:00:38 | 05:00:47 | initial PENDING; late segment 05:59:12 | 06:00:01 for late segment | UNVERIFIED | UNVERIFIED | 4 | late preservation overlapped next trigger | UNVERIFIED |
| 06:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 07:00:38 | 07:02:17 | PENDING | PENDING | UNVERIFIED | UNVERIFIED | 0 | stale in-progress record | UNVERIFIED |
| 08:00:38 | 08:04:14 | initial PENDING; continuation 08:47:56 | 08:51:26 | UNVERIFIED | >=16m23s | 20 | split/re-entered; full union unknown | UNVERIFIED |
| 09:00:38 | 09:00:41 | initial PENDING; continuation 09:47:52 | 09:59:10 after zero-work late segment | UNVERIFIED | >=19m37s | 18 | premature-stop rule later superseded | UNVERIFIED/NONCOMPLIANT |
| 10:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 11:00:38 | 11:00:26 | initial PENDING; continuation 11:48:30 | latest segment 11:59:20 | UNVERIFIED | >=19m59s | 17 | split/re-entered; full union unknown | UNVERIFIED |
| 12:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 13:00:38 | 13:01:30 | initial PENDING; continuation 13:49:16 | 13:51:15 | UNVERIFIED | >=18m58s | 12 | split/re-entered; full union unknown | UNVERIFIED |
| 14:00:38 | 14:01:25 | 14:55:57 | 14:57:52 | 57m17s | >=22m10s; union UNVERIFIED | 15 | normal continuation; one segment lacks stop | UNVERIFIED |
| 15:00:38 | 15:02:03 | 15:55:44 | 15:59:30 | 57m27s | 52m58s | 26 | normal continuation; cutoff reached | MET |
| 16:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 17:00:38 | 17:03:31 | 17:52:05 | 17:53:22 | 49m51s | 48m00s | 10 | shortened window; stopped for preservation | NOT MET |
| 18:00:38 | 18:00:38 | 18:51:50 | 18:52:55 | 52m17s | 50m09s | 15 | natural checkpoint after target | MET |
| 19:00:38 | 19:01:53 | 19:53:30 | 19:54:27 | 52m34s | 50m51s | 16 | eventual-D2C work; pivot discovered before handoff | MET |
| 20:00:38 | 20:00:28 | 20:52:59 | 20:55:43 | 55m15s | 51m21s | 12 | independent-#742 focused session 1 | MET |
| 21:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 22:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |
| 23:00:38 | MISSING | MISSING | MISSING | UNVERIFIED | UNVERIFIED | - | missing telemetry; cause unknown | UNVERIFIED |

### Utilisation totals

- Scheduled forward slots: **23**.
- Slots with any telemetry: **14**; slots with no telemetry: **9**.
- Fully verified whole-slot records: **5** (`15,17,18,19,20`).
- Of those five, four met the target and one recorded 48 minutes.
- Closed, non-overlapping forward intervals evidenced across all logs total at
  least **371m25s**.  This is a lower bound, not a day-utilisation estimate.
- Distinct substantive units recorded: **195**.
- Whole-day utilisation remains **UNVERIFIED** because nine slots are missing
  and several split slots have `PENDING` boundaries.

## Repository hygiene findings

At audited head `0d110495...`, `scripts/check_status_sync.py --head HEAD`
failed because the final telemetry-only commit did not change the protected
`CURRENT_STATE.md` status block.  The README also contained two stale public
statements: its title and later "Current research chain" still described the
eventual-D2C programme as active, and the operational section said that
programme continued as the live target.  This audit repairs those
contradictions and records the failure rather than rewriting history.

## Prioritized next-hours programme

1. **Independent bridge reconstruction.**  Re-prove the complete selected
   quasi-edge/profile lemma from raw D2C criticality in a standalone note,
   including selection existence, pair uniqueness, source-demand injection,
   supplement dichotomy and every quantifier in threshold capacity.  Stop and
   freeze `250/429` if any reuse or choice-dependence gap appears.
2. **Actual-graph regression of the bridge.**  Build a graph-level checker that
   constructs the exact `A,B,F,S_u,R_u,s_i,z_h` objects for actual D2C graphs
   and verifies every displayed inequality under multiple legal selections.
   Include balanced complete bipartite graphs of both parities and `X_3`.
3. **High-codegree cluster attack, corrected scope.**  Only after steps 1-2,
   seek a raw-criticality upper bound/classification for pairs with a common
   selected source and `F`-codegree at least `a/5`.  Do not use the repaired
   corollary outside its full plateau hypotheses.
4. **Equality branch.**  Isolate zero-demand and near-zero-demand geometry and
   prove a stability statement that visibly retains exactly the balanced
   complete-bipartite equality cases.
5. **Gate discipline.**  Count each completed independent-#742 hour once.
   Continue through session 24 because session 1 produced qualifying progress;
   at the first audit after session 24, recommend continue/pivot on the actual
   closure evidence then available.

### Stop/pivot criteria

- Any graph-to-profile flaw blocks every threshold claim depending on it.
- A high-codegree argument that uses only scalar/Hall marginals has returned to
  the certified plateau barrier and must be stopped.
- Bounded failure to find a graph is not nonrealizability.
- Any proposed strip closure that excludes odd balanced complete bipartite
  graphs has mishandled equality and must be rejected.

## Files and commits

- Pivot: `5825c203da78ecaefaa63568f0883de25518df9f`.
- Independent strip package: commit
  `a69487d826eb0a687f7a0f3889a077a35a8284f8`.
- Completed focused session checkpoint:
  `fd9f816c84e66254c13b78848eef0a94dd4f62cc`.
- Audited head: `0d11049574fce97f4630a4b71e8da78edbb7836c`.
- Main theorem: `FIRST_OBSTRUCTION_AND_39_67.md`.
- Bridge replay: `GRAPH_TO_THRESHOLD_HOSTILE_REPLAY.md`.
- Plateau obstruction: `FULL_HALL_PLATEAU_OBSTRUCTION.md`.
- Signature rigidity: `SIGNATURE_UNION_RIGIDITY.md` and
  `ROBUST_SIGNATURE_STABILITY.md`.
- Corrected corollary: `POSITIVE_DENSITY_CODEGREE_CLUSTER.md`.

All mathematical results remain internal candidate work until independent
specialist review.  The polished PDF is preserved at
`output/pdf/Erdos742_Daily_Red_Team_Audit_2026-09-22.pdf`.
