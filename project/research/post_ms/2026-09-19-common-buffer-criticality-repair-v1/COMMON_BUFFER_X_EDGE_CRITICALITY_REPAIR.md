# Repair of minimal common-buffer X-edge criticality

Date: 2026-09-19

Status: adversarial repair and replacement theorem inside the unloaded one-code `z=1` common-buffer branch. This note **invalidates Sections 4, 6 and 7 of `ANTICOMPLETE_BUFFER_X_EDGE_TRICHOTOMY.md` in their matched-only form**. The invalid text remains preserved in repository history and is not to be used downstream. No eventual second-extremal theorem is claimed.

## 1. Audit reconciliation and scope

Before forward work, `CURRENT_STATE.md`, `README.md`, the latest commits, the 19 September daily red-team audit/handoff, the source-premise repair, and the independent actual-D2C Hall/pair-capacity regression were reread. The source-tuple premises remain at their repaired raw/selected trust boundary, the actual-graph regression still reports no graph/formula mismatch and retains `X_3`, and the rigid complete Hall cut still has no positive actual-graph fixture. The present argument therefore remains a hand implication conditional on the rigid one-code hypotheses.

A hostile reread of the immediately preceding common-buffer note found a raw criticality orientation error. This is now the dominant local risk and is repaired before any further code-multiplicity argument.

The affected branch has:

- a complete rigid A-cut `X--Y`, with `x=|X|>=3`, `y=|Y|>0`;
- every source in `Y` of code `d`, with `A_{bar d}=emptyset`;
- `g=g_P`, `k=x-g>0`;
- `U_-=U_{bar d}=W_0 dotcup {b}`, with `|W_0|=k`;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- `r=d_Y(b)=0`;
- equality in the buffer-slack floor `epsilon_b=p-g`, so `b--X` and `b--U_o` are complete.

The safe predecessor facts from `UNLOADED_COMMON_BUFFER_SOURCE_EDGE_DICHOTOMY.md` are retained, including

`E_core>=k(p+k-2)`

and, for `r=0`,

`L_Y=y(p-g+1)+H_Y`,

where `H_Y` counts the `Y--U_o` nonedges.

## 2. Exact invalidation

For an edge `b x`, the invalid note called the following an orientation:

`x z in E`, `b z notin E`, `N(x) cap N(z)={b}`.

This is internally impossible: if `b z` is a nonedge, then `b` cannot belong to `N(z)`, so it cannot be the unique member of `N(x) cap N(z)`.

The correct two triangle-edge criticality orientations for the edge `b x` are:

**Orientation A (singleton head b):**

`b z in E`, `x z notin E`, `N(x) cap N(z)={b}`.          `(A)`

**Orientation B (singleton head x):**

`x z in E`, `b z notin E`, `N(b) cap N(z)={x}`.          `(B)`

The old Orientation-B analysis was already of form `(B)` and survives. The old Orientation-A localization does not survive because its adjacency to the buffer was reversed.

This invalidates the previous unconditional conclusion that every Orientation-A certificate must use a matched B-foot, and therefore invalidates the previous unconditional statement that at least `k=x-g` X-sources require gamma-aligned matched feet.

The arithmetic checker `check_z1_criticality_collapse.py` is **not** invalidated: it uses only the preceding common-buffer score theorem and not the faulty matched-only follow-on.

A hostile reread of `OMITTED_PAIR_NONEDGE_FORCING.md` found no analogous orientation inconsistency: its two omitted-edge orientations have the correct edge/nonedge relation to their singleton heads. The full-support `nu=y` theorem is therefore not rolled back by this repair.

## 3. Structural unit I: every minimal buffer--X edge still lies in a triangle

The old Lemma 3.1 survives. Since `c(b)=bar d` and every `x in X` has code neither `d` nor `bar d`, `c(x)` is neither equal nor complementary to `c(b)`. The two codes agree in at least one tight coordinate, hence `b` and `x` share a matched neighbour.

Thus every edge `b x` lies in a triangle and must have a certificate of type `(A)` or `(B)` above.

## 4. Structural unit II: corrected Orientation A is matched-or-outside

Fix `x in X` and a certificate `(A)`.

The witness z cannot be:

- the root: `N(x) cap N(v)` contains the p matched neighbours of x and also b under buffer equality;
- in `Y`: b is anticomplete to Y;
- in `U_-`: `G[U_-]` is edgeless;
- in `X`: every vertex of Y is adjacent to both x and z, so the common neighbourhood is not `{b}`.

Two locations remain.

### A1. Matched B-foot

If z is matched, the singleton head b is nonmatched. Generalized gamma localization gives

`gamma(z)=c(x)`.                                           `(A-M)`

### A2. Outside unmatched witness

If `z in U_o`, buffer equality supplies `b z in E`, as required. Since the singleton common neighbour b is unmatched, x and z have no common matched neighbour. Tight-code complementarity therefore gives

`c(z)=bar c(x)`.                                          `(A-U1)`

Moreover every source `s in Y` is adjacent to x because `X--Y` is complete. If `s z` were also an edge, s would be a second common neighbour of x and z. Hence

`z` is anticomplete to Y.                                 `(A-U2)`

So the corrected Orientation-A classification is exact:

> a buffer--X edge using Orientation A is certified either by a matched foot with `gamma(z)=c(x)`, or by an outside unmatched witness `z in U_o` of complementary code which is anticomplete to Y.

The outside-U channel is real and must not be deleted.

## 5. Structural unit III: reverse Orientation B capacity survives

The old reverse-orientation proof remains valid.

Under `(B)`, z cannot be the root, X or `U_o`, since all are adjacent to b; it cannot lie in Y because the whole X-set would be common neighbours; and it cannot lie in `U_-`, because b and z have the same code `bar d` and therefore share their matched neighbours.

Thus z is matched. Gamma localization with source b gives

`gamma(z)=bar d`.                                         `(B-M)`

There are exactly g such matched endpoints. For a fixed matched endpoint z, the graph set `N(b) cap N(z)` is fixed, so if it is a singleton it determines at most one X-head. Therefore:

> at most g of the x buffer--X edges can use Orientation B. `(REV)`

Consequently at least

> `k=x-g`                                                   `(FORCE-A)`

buffer--X edges must use corrected Orientation A.

This is the safe replacement for the invalid matched-only theorem.

## 6. Structural unit IV: matched-or-outside demand

Choose any k of the buffer--X edges which are forced into Orientation A, and choose one valid Orientation-A certificate for each. Partition their X-sources into

- `X_M`: those assigned a matched foot;
- `X_U`: those assigned an outside unmatched witness.

Put

`q_M=|X_M|`, `ell=|X_U|`.

Then

> `q_M+ell=k`.                                             `(MO1)`

For `x in X_M`, `c(x)` occurs in matched gamma support by `(A-M)`.
For `x in X_U`, there is a witness `z in U_o` with `c(z)=bar c(x)` and `z` anticomplete to Y.

No injectivity of matched feet or outside witnesses is assumed.

There are exactly `p-g` tight fibres whose gamma pair is not `{d,bar d}`. Since every X-code is different from d and `bar d`, all matched feet serving `X_M` lie in those `p-g` fibres. Hence the codes represented in `X_M` lie in a set of at most

> `2(p-g)` gamma codes.                                    `(MO2)`

This gives the corrected concentration/dispersion interface.

## 7. Structural unit V: aligned-code capacity forces an outside load

Assume the above-`M(n)` scorecard bound `S<=C0` and `lambda>=0`, the regime in which the existing exact pair capacity is used. Let

`D0=5p+5u-3lambda-2`,

`R_code(C0)=floor((D0+sqrt(D0^2+12C0))/3)`,

and put

> `R_A=floor(R_code(C0)/2)`.                               `(RC)`

The preserved aligned-code self-pricing theorem gives `w_c=2n_c+t_c<=R_code(C0)`, hence every A-code class has

> `n_c<=R_A`.                                              `(RC-A)`

Combining `(MO2)` and `(RC-A)`, the matched Orientation-A channel can contain at most

> `2(p-g) R_A` X-sources.                                  `(MATCH-CAP)`

Therefore every above-threshold survivor in this equality geometry must have

> `ell >= ell_0 := [k-2(p-g)R_A]_+`.                      `(OUT-FORCE)`

This theorem uses no matched-foot injectivity. It prices concentration through the already-proved aligned-code cap, exactly the repair path demanded by the previous handoff.

A particularly clean specialization is immediate:

### Zero-buffer-slack corollary

If `epsilon_b=0`, then the buffer floor forces `g=p`. Hence there are **no** non-P gamma fibres and `(MATCH-CAP)` is zero. Therefore

> `ell=k=x-p`.                                             `(ZERO-OUT)`

So the old claim that zero buffer slack forces at least `x-p` gamma-aligned matched feet is reversed: it forces at least `x-p` **outside unmatched** certificates.

## 8. Structural unit VI: outside-witness reuse creates holes and slack

Let W be the set of distinct outside witnesses chosen for the `ell` sources in `X_U`, and put `m=|W|`. For `z in W`, let `t_z` be the number of chosen X-sources using z. Then

`sum_{z in W} t_z=ell`, `t_z>=1`.

Because a fixed z has one code and `(A-U1)` forces every source it serves to have the complementary code, all sources served by z lie in one A-code class. Thus `(RC-A)` gives

> `t_z<=R_A`.                                              `(REUSE1)`

Consequently, when `ell>0`,

> `m>=ceil(ell/R_A)`.                                     `(REUSE2)`

(with the evident interpretation that `R_A=0` makes the branch impossible).

Every z is anticomplete to Y by `(A-U2)`, so the physical Y--`U_o` hole count satisfies

> `H_Y>=y m`.                                              `(HOLE-Y)`

Each z is also nonadjacent to the `t_z` X-sources it serves. For a U-vertex,

`d_{A union U}(z)=p+u-1-epsilon_z`.

Since z has no Y-neighbours, misses those `t_z` X-vertices, and has at most all other U-vertices as neighbours,

> `epsilon_z >= [p-x+t_z]_+`.                             `(WU1)`

Summing and using convex truncation gives

> `E_W:=sum_{z in W}epsilon_z`
> ` >= [ell-(x-p)m]_+`.                                   `(WU2)`

These are physical graph incidences, not selected-witness multiplicities.

## 9. Structural unit VII: repaired score and pair-local floors

For `r=0`, the source slack identity is exact:

> `L_Y=y(p-g+1)+H_Y`.                                     `(LY0)`

Thus any corrected equality geometry with `ell,m` as above satisfies

> `L_Y>=y(p-g+1+m)`.                                      `(LYM)`

The core W0 and the buffer are disjoint U-vertices, so their U-slack contribution is at least

`E_core+(p-g)`, with `E_core=k(p+k-2)`.

The outside witness slack `E_W` is disjoint again. Therefore

> `S >= E_core+(p-g)+E_W`
> `     +max{phi(g), y(p-g+1+m)}`,                        `(S-REPAIR)`

where `phi(g)=g(g-1)` for `g>=3` and zero for `g<=2`.

This is a strict structural refinement whenever the corrected outside channel is actually used. The one-code pair itself also has the local floor

> `S_P>=E_core+(p-g)+y(p-g+1+m)`.                         `(SP-LOCAL)`

Hence the audit-required local tools remain active on the **same** pair P:

- exact crossing traffic: `2xy<=Ccap_P` in this unloaded model;
- exact `Ccap_P=R_code(S_P)[g+2S_P/(lambda+1)]`;
- `(ONE-P)`;
- `(CROWD)`: `S_P>=y(3y-D0)` whenever positive.

The next calculation should retain `S_P` and `(SP-LOCAL)` rather than replace them by total C0 prematurely.

## 10. Structural unit VIII: rooted residual feedback

The corrected outside witnesses also strengthen the physical A--U nonedge count.

The k common core witnesses have one X-neighbour each, so they force `k(x-1)` X--U nonedges. Every source misses all k core witnesses and the buffer, giving `y(k+1)` Y--U nonedges. The m outside witnesses add at least `ym` further Y--U holes and the ell chosen source-witness pairs add ell X--U holes. Therefore

> `Z >= k(a-1)+y+ym+ell`.                                 `(Z-REPAIR)`

Using the exact rooted identity

`Z=u(p-lambda)+2q+E_U`,

put

> `D_CB=k(a-1)+y+ym+ell-u(p-lambda)`.                     `(D-CB)`

Also

> `E_U>=E0:=E_core+(p-g)+E_W`.                            `(EU0)`

The exact integer minimization then gives

> `q+E_U >= E0+ceil([D_CB-E0]_+/2)`.                     `(QE-CB)`

Substituting in

`f=(p-lambda)(p+u)+q+E_U-delta`

gives the corresponding rooted residual/A-edge floor. This is the repaired feedback from common-buffer criticality into the defect ledger.

For zero buffer slack (`g=p`, `ell=k`) this simplifies to

> `Z>=k a+y(1+m)`,                                        `(Z-ZERO)`

with `m>=ceil(k/R_A)` in an above-threshold survivor.

## 11. Diagnostic replay

A companion checker audits `(WU2)`, the aligned-code capacity arithmetic, and the same coarse parameter box as the preceding z=1 checker. It does not enumerate D2C graphs.

On `3<=p<=18`, `1<=u<=18`, `lambda>=0`:

- 345,219 abstract `(p,u,lambda,x,g)` r=0 equality branches pass the predecessor scalar floor;
- 17,174 of those have positive forced outside load under `(OUT-FORCE)`;
- in this box every such positive-load case is the zero-buffer specialization `g=p`;
- 113 of those zero-buffer abstract branches are rejected by the repaired Y-hole score floor alone;
- 17,061 zero-buffer abstract branches remain after that diagnostic gate.

These are parameter-branch counts, **not graph counts**. Their value is diagnostic: the main theorem gain is the corrected structure and the forced outside channel at zero buffer slack, not the small finite rejection count.

## 12. Trust boundary and next move

Survives from the predecessor:

- the unloaded common-buffer score theorem;
- triangle-freeness of source--buffer edges in the `r>0` branch;
- the rectangular `H_Y>=r d_o` payment;
- the reverse Orientation-B matched capacity `<=g`;
- the arithmetic z=1 score regression.

Withdrawn/superseded:

- the old Orientation-A adjacency statement;
- matched-only Orientation-A localization;
- the unconditional claim that at least k X-sources have gamma-aligned matched feet;
- the old code-only next action built on that claim.

Repaired frontier:

1. keep the common-buffer `r=0` equality branch, but use the matched-or-outside theorem `(MO1)`;
2. in the zero-buffer subbranch `g=p`, use `(ZERO-OUT)`, `(SP-LOCAL)` and `(QE-CB)` first: the entire forced Orientation-A load is outside-U;
3. intersect the resulting local `S_P` floor with exact `Ccap_P`, `(ONE-P)` and `(CROWD)` before any global scalar collapse;
4. when `p-g>0`, combine `(MATCH-CAP)` with the outside-hole surcharge rather than assuming matched-foot injectivity;
5. only then return to the `r>0` common-buffer branch; do not move to `z=2` yet.

`X_3` remains untouched because its canonical root has `u=0`; all common-buffer mechanisms here require `k+1<=u`.