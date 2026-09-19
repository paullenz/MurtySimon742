# Positive-buffer reverse collapse and head dichotomy

Date: 2026-09-19

Status: audit repair plus structural strengthening inside the rigid one-code `z=1` unloaded common-buffer branch. The result is conditional on the rigid complete-Hall hypotheses. It does **not** claim the eventual second-extremal theorem.

The active comparison is the first positive-buffer equality geometry

`r_b:=d_Y(b)=0`, `t:=p-g>=1`, `epsilon_b=t`,

so the unused common buffer is anticomplete to `Y` and attains the exact degree floor by being complete to `X` and `U_o`.

The published order-12, 32-edge graph `X_3` remains a mandatory negative control and is outside this branch (`u=0`).

---

## 1. Audit reconciliation and a necessary repair

Before doing forward mathematics this run reread:

- `CURRENT_STATE.md`;
- the root `README.md`;
- the current head and recent commits;
- `DAILY_RED_TEAM_AUDIT.md`;
- `SOURCE_PREMISE_REPAIR.md`;
- the independent actual-D2C graph regression through rooted slots, tight codes, Hall cuts and exact pair capacity;
- `COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md`;
- `COMMON_CORE_EXACT_SLACK_AND_REVERSE_DEFICIT.md`;
- the later zero-buffer reverse-collapse and final zero-buffer closure.

The audit boundary remains unchanged:

1. the two source-tuple premises are accepted only in their repaired raw/selected meanings;
2. the finite source-tuple theorem is not being used as unconditional graph-level closure here;
3. the actual-D2C regression has no recorded graph/formula mismatch and retains `X_3`;
4. no actual graph in the bounded corpus realizes the full rigid complete-Hall hypotheses, so the present deductions retain a conditional trust label;
5. exact local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain mandatory constraints;
6. the four-exception gate remains subordinate.

The reread exposed one historical error which must be superseded before using the positive-buffer handoff.

`COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md` allowed the following "reverse" Orientation B for a buffer edge `bx`:

`xz in E`, `bz notin E`, `N(b) cap N(z)={x}`,

and then classified `z` as a matched endpoint.

That matched classification is impossible for the simplest rooted reason: both `b` and every matched endpoint lie in `B=N(v)`, hence they share the root `v`. Therefore their common neighbourhood can never be the singleton `{x}` with `x in A`.

The later zero-buffer work reached the correct conclusion that the reverse channel is empty, by a stronger mate-degree argument. That later conclusion is sound. What is withdrawn here is the earlier **positive-buffer reverse matched channel** and every scalar `R_B,r_B,d` optimization that treated it as physically available.

The exact core-head facts and the identity

`E_core=k(p+k-1)+H_core`

from `COMMON_CORE_EXACT_SLACK_AND_REVERSE_DEFICIT.md` survive. Its reverse-deficit Sections 4 onward are superseded wherever they depend on a matched Orientation-B certificate.

The final zero-buffer closure is **not reopened**: after the later reverse collapse it uses the all-outside buffer certificates, raw `X--U_o` and `X--X` criticality, and exact degree bookkeeping. The current repair instead generalizes the correct no-reverse logic to `t=p-g>0`.

---

## 2. Setup: first positive-buffer equality geometry

Use the purified one-code notation.

- `X--Y` is complete, `x=|X|>=3`, `y=|Y|>0`.
- Every source in `Y` has code `d`; `X` contains neither `d` nor `bar d`.
- `g=g_P`, `k=x-g>0`.
- `U_-=U_{bar d}=W_0 dotcup {b}`, with `|W_0|=k`.
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`.
- `U_o=U\U_-`, `u_o=u-k-1`.
- `r=d_Y(b)=0`.
- Put

> `t:=p-g>=1`.                                             `(2.1)`

The buffer degree floor is `epsilon_b>=p-g=t`. We study the first equality layer

> `epsilon_b=t`.                                           `(2.2)`

Exactly as in the preserved source-edge note, equality in the buffer degree count forces

> `b--X` complete and `b--U_o` complete.                  `(2.3)`

The common core has a graph-fixed injective head map

`h:W_0 -> X`

with image `H_0`, `|H_0|=k`, and every core witness has exactly one X-neighbour and no Y-neighbour.

The `g` matched gamma-`d` crossing feet likewise have graph-fixed singleton X-heads. Let their head set be `H_M`.

For a fixed source `s in Y`, the selected crossing system has exactly `g+k=x` distinct witnesses and certifies the `x` distinct crossing edges. Hence

> `X=H_M dotcup H_0`,                                     `(2.4)`
>
> `|H_M|=g`, `|H_0|=k`.                                  `(2.5)`

No cross-source witness injectivity is being assumed.

---

## 3. Unit I — reverse Orientation B is completely impossible

Fix an edge `bx`, `x in X`. It lies in many triangles, so D2C criticality gives one of the two singleton orientations.

Orientation B would require a vertex `z` with

> `xz in E`, `bz notin E`, `N(b) cap N(z)={x}`.           `(B)`

Under `(2.3)` no location for `z` survives.

- `z=v` is impossible because `bv` is an edge.
- `z in X` is impossible because `b--X` is complete.
- `z in U_o` is impossible because `b--U_o` is complete.
- `z in Y`: both `b` and `z` are adjacent to every vertex of `X`, so their common neighbourhood contains all `x>=3` vertices of `X`.
- `z in U_-\{b}`: `b` and `z` have the same tight code `bar d`, hence share all `p` selected matched neighbours.
- `z` matched: both `b` and `z` lie in `B=N(v)`, so the root `v` is an additional common neighbour.

Therefore

> **NO-REVERSE THEOREM.** Orientation B does not occur for any buffer--X edge in the `r=0`, `epsilon_b=t` equality geometry. `(NR)`

This is a raw graph statement. It does not depend on the finite source-tuple theorem or on any witness-incidence uniqueness convention.

---

## 4. Unit II — Orientation A has only matched or outside-U locations

Every buffer edge must therefore use Orientation A:

> `bz in E`, `xz notin E`, `N(x) cap N(z)={b}`.           `(A)`

The standard location check leaves only:

1. a matched endpoint `z`, in which case the generalized matched-foot localization gives
   `gamma(z)=c(x)`; or
2. an unmatched vertex `z in U_o`, in which case
   `c(z)=bar c(x)` and `z` is anticomplete to `Y`.

Indeed:

- the root has all matched neighbours of `x` as additional common neighbours;
- `Y` and `U_-` are nonadjacent to `b`;
- an `X` witness would share all of nonempty `Y` with `x`;
- the remaining unmatched location is `U_o`.

The new work is to show that even the apparently available matched Orientation-A channel is actually empty once the two graph-fixed head systems in `(2.4)` are used.

---

## 5. Unit III — matched-crossing heads have singleton A-code classes

Fix a matched gamma-`d` crossing foot `q`. Since every `s in Y` is adjacent to all of `X` and the selected certificate has

`N(s) cap N(q)={h_M(q)}`,

the X-neighbourhood of `q` itself is the singleton

> `N_X(q)={h_M(q)}`.                                      `(5.1)`

Now suppose another `x' in X` had the same tight Boolean code as `h_M(q)`. Tight code determines adjacency to every matched endpoint, so `x'` would also be adjacent to `q`. Since `s` is adjacent to every vertex of X, both `h_M(q)` and `x'` would lie in `N(s) cap N(q)`, contradicting singletonness.

Hence:

> every head in `H_M` has a code which occurs exactly once in `X`; `(5.2)`
>
> the `g` codes represented by `H_M` are pairwise distinct. `(5.3)`

Because `Y` has only code `d` and `X` contains neither `d` nor `bar d`, these are in fact singleton A-code classes in the whole A-layer.

This is stronger than the aligned-code size cap: it is an exact graph-fixed singleton statement for the matched-crossing heads.

---

## 6. Unit IV — no core head can use a matched buffer certificate

Let `x=h(w_0) in H_0`, where `w_0 in W_0`.

Suppose Orientation A for `bx` used a matched witness `z`. Then `b~z`.

But `b,w_0 in U_{bar d}` have the same tight code, so they have exactly the same selected matched neighbour in every tight fibre. Therefore

`b~z  =>  w_0~z`.

Since also `w_0~x`, the vertex `w_0` is a second common neighbour of `x` and `z`, contradicting

`N(x) cap N(z)={b}`.

Thus:

> every core head in `H_0` is outside-U certified.        `(6.1)`

For its chosen outside witness `z_x in U_o`, the same singleton condition forces

> `w_0 z_x notin E`.                                      `(6.2)`

The `k` core vertices `w_0` are distinct, so these are `k` distinct physical missing pairs even if several core heads share one outside witness. Hence

> `H_core=e_bar(W_0,U_o)>=k`.                             `(6.3)`

Using the exact core identity,

> `E_core>=k(p+k)`.                                       `(6.4)`

This is a physical-hole theorem, not certificate multiplicity bookkeeping.

---

## 7. Unit V — no matched-crossing head can use a matched buffer certificate either

Now let `x in H_M`, and let `q` be its matched gamma-`d` crossing foot. Thus

> `gamma(q)=d`, `q~x`.                                    `(7.1)`

Suppose the buffer edge `bx` used a matched Orientation-A witness `z`.

Since `b~z` and `b` has code `bar d`, `z` is precisely the endpoint selected by `bar d` in its tight fibre.

If `z` lies in the same fibre as `q`, then the only endpoint of that fibre adjacent to `b` is `q` itself; but `q~x`, while Orientation A requires `z not~x`. So the fibres are distinct.

For distinct fibres, `gamma(q)=d` says that in the fibre containing `z`, the matched neighbour of `q` is the endpoint opposite `d`, namely the endpoint selected by `bar d`. That endpoint is exactly `z`. Therefore

> `q~z`.                                                   `(7.2)`

But `q~x` as well. Thus `q` is a common neighbour of `x` and `z` distinct from `b`, again contradicting

`N(x) cap N(z)={b}`.

Therefore:

> **MATCHED-CHANNEL COLLAPSE.** No buffer--X edge in the equality geometry can use a matched Orientation-A witness. `(MC0)`

Combining `(NR)` and `(MC0)`:

> every one of the `x` buffer--X edges is certified by a witness in `U_o`. `(7.3)`

This is the main structural advance of the run.

---

## 8. Unit VI — distinct outside reservoir and the population obstruction

For every `x in X`, choose one outside witness `z_x in U_o`. Then

`c(z_x)=bar c(x)` and `z_x` is anticomplete to `Y`.

The `g` heads in `H_M` have pairwise distinct singleton A-code classes by Unit III. Therefore their selected outside witnesses:

1. are pairwise distinct, because one U-vertex has only one code; and
2. cannot be reused by any core head, because that would require the core head to have the same code as the corresponding singleton `H_M` head.

Since `k>0`, the core heads need at least one further outside witness.

Thus, if `m` is the number of distinct physical outside witnesses,

> `m>=g+1`.                                                `(8.1)`

All these witnesses lie in `U_o`, whose size is `u-k-1`. Hence

> `u-k-1>=g+1`,                                           `(8.2)`
>
> **`u>=x+2`.**                                            `(POP)`

This is a new pure population obstruction. It is independent of the scorecard and pair-capacity inequalities.

Because

`a=2p+u-lambda-1`, `y=a-x`,

`(POP)` also gives

> `y>=2p-lambda+1`.                                       `(8.3)`

The matched-crossing singleton codes have therefore converted the first positive-buffer equality geometry into a genuinely unmatched-heavy branch.

---

## 9. Unit VII — exact source-slack amplification

Every outside witness is anticomplete to `Y`. Since the `m>=g+1` witnesses are physical and distinct,

> `H_Y>=y(g+1)`.                                          `(9.1)`

The exact `r=0` source-slack identity is

`L_Y=y(p-g+1)+H_Y`.

Using `t=p-g` and `(9.1)`,

> `L_Y>=y(t+1+g+1)`                                     
> `     =y(p+2)`.                                         `(LY+)`

The cancellation `t+g=p` is important: **the Y-side payment no longer becomes cheap when the buffer slack `t` is small.**

In particular, the first positive layer `t=1` already has

> `L_Y>=y(p+2)`,                                          `(9.2)`

not merely the predecessor `2y`.

---

## 10. Unit VIII — outside-witness slack

Let an outside witness `z in U_o` serve `tau_z` buffer heads. The preserved U-degree calculation gives

> `epsilon_z >= [p-x+tau_z]_+`
> `             =[t-k+tau_z]_+`.                          `(10.1)`

The `g` outside witnesses attached to `H_M` each serve exactly one buffer head: their source code class is a singleton. They are disjoint from the witnesses used by the core heads.

The core block has total selected load `k`. Therefore a safe parameter-only lower bound is:

- if `k<=t`, the core witnesses contribute at least `t`, and each of the `g` singleton-head witnesses contributes at least `t-k+1`;
- if `k>t`, zero is the sharp unconditional floor without further control on core-witness splitting.

Define

> `E_out^0 = t+g(t-k+1)` if `k<=t`, and `0` if `k>t`.      `(10.2)`

Then

> `E_{U_o}>=E_out^0`.                                     `(10.3)`

No assertion is made that the core witnesses themselves are distinct.

---

## 11. Unit IX — sharpened score obstruction

Let

> `phi(g)=g(g-1)` for `g>=3`, and `0` for `g<=2`.

The gamma-collision theorem gives `L_A>=phi(g)`, while Unit VII gives `L_A>=L_Y`.

Units VI--VIII and the exact core identity therefore give

> **`S=E_U+L_A`**
>
> `>= k(p+k)+t+E_out^0`
> `   +max{phi(g), y(p+2)}.`                              `(S+)`

This is a structural floor for the first positive-buffer equality geometry.

The predecessor equality floor was only

`k(p+k-1)+t+max{phi(g),y(t+1)}`.

The gain is not merely a better scalar coefficient: it comes from three physical statements which survive independently:

1. every core head forces a literal `W_0--U_o` hole;
2. every matched-crossing head also needs an outside witness;
3. those `g` matched-head witnesses are physically distinct and separated from the core witness pool.

---

## 12. Unit X — rooted residual and triangle-count feedback

Let

`Z=au-e(A,U)`

be the physical A--U nonedge count.

The new geometry supplies four disjoint families of holes:

1. each core witness has only one X-neighbour: `k(x-1)`;
2. every Y-source misses the `k` core vertices and the buffer: `y(k+1)`;
3. the `g+1` distinct outside witnesses are anticomplete to Y: `y(g+1)`;
4. every buffer head is nonadjacent to its selected outside witness: `x`.

Therefore

> `Z>=k(x-1)+y(k+1)+y(g+1)+x`
>
> `  =ka+y(g+2)+g`.                                      `(Z+)`

Use the exact rooted identity

> `Z=u(p-lambda)+2q+E_U`.                                `(RID)`

Put

> `D_+=ka+y(g+2)+g-u(p-lambda)`,                         `(12.1)`
>
> `E_0=k(p+k)+t+E_out^0`.                                `(12.2)`

Then exact integer minimization gives

> `q+E_U >= E_0+ceil([D_+-E_0]_+/2)`.                   `(12.3)`

For an above-`M(n)` candidate `E_U<=C0`, so separately

> `q>=ceil([D_+-C0]_+/2)`.                               `(12.4)`

Consequently the rooted triangle count

> `Q=p(p+u-1)+q`                                          `(12.5)`

is forced upward whenever `D_+>C0`.

Finally the preserved residual identity

`f=(p-lambda)(p+u)+q+E_U-delta`

gives the explicit A-edge lower bound

> `f >= (p-lambda)(p+u)`
> `     +E_0+ceil([D_+-E_0]_+/2)-delta`.                 `(12.6)`

Thus the new physical reservoir feeds directly into the requested residual-defect / rooted-triangle programme; it is not merely a scorecard side calculation.

---

## 13. Unit XI — exact local pair constraints retained, and what the diagnostic says

The audit-mandated one-code pair remains `P={d,bar d}`. Pair purity still gives

> `Ccap_P=R_code(S_P)[g+2S_P/(lambda+1)]`,               `(13.1)`

with no `2h_P` term.

All `xy` crossing edges still require

> `2xy<=Ccap_P`,                                          `(13.2)`

and the purified one-code bill remains

> `Ccap_P+L_Y>=y(p+x+k)`.                                `(ONE-P)`

The aligned crowding bill `(CROWD)` also remains active.

The new outside witnesses have codes complementary to X-codes, hence never lie in pair `P`; therefore their slack is outside `S_P`. In an above-threshold candidate,

> `S_P<=C0-E_out^0`.                                      `(13.3)`

The pair-local baseline inside `P` already contains

> `k(p+k)+t+L_Y`.                                         `(13.4)`

The companion checker intersects `(13.1)--(13.4)`, `(ONE-P)` and `(CROWD)` with the new structural floor on the same coarse diagnostic box used in the preceding common-buffer scans.

Result: after the new physical population and score obstructions are imposed, the relaxed exact pair inequalities reject **no additional abstract parameter states** on that box.

This is a useful negative result, not a reason to discard the pair machinery. It means the next gain should come from **more physical geometry** (or a sharper localization of pair slack), not from replacing `S_P` by another coarse scalar upper bound.

---

## 14. Diagnostic impact

The companion checker scans

- `3<=p<=18`,
- `1<=u<=18`,
- all admissible `lambda>=0`,
- all `3<=x<a`,
- all positive buffer slacks `t=p-g>=1`,

and compares only the `r=0`, `epsilon_b=t` equality comparator.

Among abstract states which passed the predecessor equality floor:

> `320,525`

were possible before this repair.

The new pure population obstruction

> `u>=x+2`

rejects

> `146,603`.

Among the remainder, the repaired score floor `(S+)` rejects another

> `40,087`.

Thus the new structural package leaves

> `133,835`

abstract equality states in that coarse box, excluding

> `186,690`

of the predecessor states.

For the first positive layer `t=1`:

- predecessor states: `20,178`;
- rejected by population alone: `12,307`;
- rejected next by the repaired score floor: `2,056`;
- remaining abstract states: `5,815`.

Among the `133,835` remaining states, the rooted residual bound `(12.4)` forces `q>0` in

> `7,274`

states; the largest forced value in this bounded diagnostic is `48`.

The relaxed local `Ccap_P/(ONE-P)/(CROWD)` intersection adds zero further exclusions after the new structural floor.

These are **parameter-state diagnostics, not graph counts and not realizability evidence**.

---

## 15. Trust boundary and dependency audit

Promoted hand statements:

- `(NR)` is raw D2C criticality plus the rooted fact that two B-vertices share `v`.
- `(5.2)--(5.3)` use only the graph-fixed matched crossing singleton and tight-code determination of matched adjacency.
- `(6.1)--(6.4)` count literal physical incidences/nonedges.
- `(MC0)` uses only `gamma(q)=d`, `c(b)=bar d`, tight-fibre adjacency, and singleton criticality.
- `(POP)` counts distinct physical U_o vertices, not witness incidences.
- `(LY+)`, `(S+)`, `(Z+)` and the residual bounds are bookkeeping consequences of those physical facts.
- No finite source-tuple capacity theorem is needed in the proof.
- The checker is audit support only.

Superseded historical material:

1. the matched reverse Orientation-B channel in `COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md`;
2. reverse-head capacity statements derived from that channel;
3. the reverse-deficit optimization in `COMMON_CORE_EXACT_SLACK_AND_REVERSE_DEFICIT.md` Sections 4 onward.

Retained historical material:

1. the unloaded common-buffer source-edge theorem;
2. the exact core head map and core slack identity;
3. the later zero-buffer reverse collapse and all-outside conclusion;
4. the final zero-buffer branch closure, which is not reopened;
5. exact one-code pair capacity, `(ONE-P)`, `(CROWD)`, and rooted residual identities.

`X_3` remains untouched because it has `u=0` and cannot enter a branch now requiring the much stronger `u>=x+2`.

---

## 16. Next move

Do **not** move to `z=2`.

The first positive-buffer equality geometry has now collapsed much further than the previous handoff suggested: every buffer edge uses `U_o`, the matched-crossing heads force `g` distinct outside witnesses, and an additional core witness is unavoidable.

The highest-value next attack is the surviving outside-U geometry itself.

1. Classify equality/near-equality in the reservoir bound `m>=g+1`. If `m=g+1`, all k core heads reuse a single additional witness; determine the exact common-code and adjacency consequences and attack that common-core outside witness by raw D2C criticality.
2. In parallel, inspect the rooted B-edge slots generated by any would-be matched buffer foot only as a **hostile sanity check**; the present theorem says none exist.
3. Push `(Z+)` through the unused rooted-slot identity `delta=r-f` and the Hamming-energy package before global scalarization.
4. Retain exact local `Ccap_P`, `(ONE-P)` and `(CROWD)` throughout, but do not expect the coarse upper-envelope relaxation to close the branch by itself.
5. If the `m=g+1` equality layer fails, quantify the surcharge for each additional core-witness code class; this should amplify both `L_Y` and the unmatched-population requirement.
6. Only after the `r=0`, `epsilon_b=t` layer is exhausted should the loaded (`r>0`) or extra-buffer-slack (`epsilon_b>t`) positive-buffer cases become primary.

The four-exception gate remains subordinate unless one of these physical classifications makes it load-bearing.
