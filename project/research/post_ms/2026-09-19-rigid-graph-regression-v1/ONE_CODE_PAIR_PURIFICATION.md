# One-code rigid pair purification and the gamma/U tradeoff

Date: 2026-09-19

Status: internal structural theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

The published order-12, size-32 graph `X_3` remains a mandatory hostile control. Nothing below asserts an all-order second-extremal bound.

## 1. Audit reconciliation

The 19 September daily red-team audit required the graph-to-source/Hall interface to be checked before pushing the rigid one-code branch. The source-tuple premises have now been repaired at the exact raw/selected level used by the finite source-tuple theorem, and the companion graph-level regression in this package independently reconstructs the rooted partition, tight codes, rooted witness slots, A-edge criticality channels, complementary-pair data, exact Hall-cut decomposition and pair-local capacity ingredients on actual D2C graphs.

This note therefore resumes the audit-authorized one-code line. It does **not** return to the closed mixed `{4,5}` selected-excess ladder, and the bounded four-exception gate remains subordinate.

The main point is that the generic one-code statement in `RIGID_HALL_WITNESS_DEFICIT_AND_ONE_CODE_TRAP.md` still carries two pieces of slack which disappear once the complementary-pair geometry is used exactly:

1. the matched singleton count `mu_X` can be replaced by the **pair-local gamma-fibre count** `g_P`; and
2. the two-sided matched-foot term `h_P` in `Ccap_P` is exactly zero.

This produces a compact gamma-versus-U-witness tradeoff and a new scorecard floor.

---

## 2. Setup

Use the rigid Hall notation. Let `X` be a nonempty proper family of complementary tight-code pairs, with

`x=|A_X|>=3`,

`Y=A\A_X`, `y=|Y|`,

and assume the rigid conclusion

`M_X=E_X=0`.

Thus the A-cut `A_X -- Y` is complete and every crossing A-edge chooses its criticality source in `Y`.

Assume the **one-code outside branch**:

> every vertex of `Y` has the same tight Boolean code `d`.

Let

`P={d,bar d}`

be its unordered complementary pair. Recall

`T0=a-p`, `L=lambda+1`,

`g0=x-T0=p-y`,

and let `g_P` be the number of tight fibres whose two matched-foot gamma codes form `P`.

For the pair-local non-direct traffic write

`t_P=P_P+C_P`,

where `P_P` is matched-B traffic and `C_P` is A/U unique-common-neighbour traffic. The exact preserved capacity is

> `2t_P <= Ccap_P`,
>
> `Ccap_P=R_code(S_P)[g_P+2S_P/L]+2h_P`.                 `(2.1)`

---

## 3. Pair purity

### Lemma 3.1 — the outside complementary pair contains no opposite A-code

In the one-code branch,

> `A_P=Y=A_d`,
>
> `A_bar d=emptyset`.                                     `(3.1)`

### Proof

`X` is a union of whole unordered complementary code pairs. Since `d` occurs outside `X`, the pair `P={d,bar d}` itself lies outside `X`; hence every A-vertex whose code is `d` or `bar d` lies in `Y`. But `Y` contains only the code `d`. Therefore `A_bar d` is empty and `A_P=Y`. `square`

This elementary observation is load-bearing below.

---

## 4. Matched witnesses are pair-local

For a matched endpoint `w`, let `gamma(w)` be its row-complement source code from `MATCHED_FOOT_COLLISION_CAPACITY.md`. If a matched endpoint certifies a non-direct A-edge with source `z`, then

> `c(z)=gamma(w)`.                                        `(4.1)`

For every fibre counted by `g_P`, exactly one endpoint has gamma code `d` and the other has gamma code `bar d`.

### Lemma 4.1 — at most `g_P` matched crossing witnesses per outside source

Fix `z in Y`. The `x` crossing edges from `z` into `A_X` use pairwise distinct criticality witnesses. Among those witnesses, at most `g_P` can be matched B-endpoints. Consequently, with

> `k_P:=(x-g_P)_+`,                                       `(4.2)`

at least `k_P` of the crossing witnesses of every `z in Y` lie in

> `U_bar d`.                                              `(4.3)`

### Proof

Any matched witness used by the source `z` must satisfy `gamma(w)=c(z)=d`. There are exactly `g_P` matched endpoints with gamma code `d`, one in each fibre whose gamma pair is `P`. The singleton-head property makes the witnesses for the `x` crossing heads pairwise distinct. The remaining witnesses cannot lie in `A`: the cut is complete, so an A-witness on the opposite side would have more than one neighbour in `A_X`, contradicting the singleton-head condition. Hence at least `(x-g_P)_+` witnesses lie in `U`, and A/U localization gives code `bar d`. `square`

This strictly sharpens the generic `k=(x-mu_X)_+` whenever singleton matched endpoints from irrelevant gamma classes inflate `mu_X`.

### Corollary 4.2 — pair-local U population

> `|U_bar d| >= k_P`.                                     `(4.4)`

---

## 5. The two-sided matched-foot term vanishes

### Lemma 5.1 — `h_P=0`

In the one-code branch,

> `h_P=0`.                                                `(5.1)`

Hence the exact pair capacity simplifies to

> `Ccap_P=R_code(S_P)[g_P+2S_P/L]`.                       `(5.2)`

### Proof

Every non-direct certificate sourced in pair `P` has its A-source in `A_P=Y=A_d`. A matched foot used by such a source must therefore have gamma code `d`. The endpoint in the same tight fibre whose gamma code is `bar d` has zero traffic, because `A_bar d` is empty. Thus for every fibre in `I_P`, one of `t_i^0,t_i^1` is zero, so

`min(t_i^0,t_i^1)=0`.

Summing over the fibres gives `h_P=0`. `square`

A companion actual-graph regression checks the more general statement that every one-sided occupied complementary A-pair has zero two-sided matched-foot load under each tested certificate policy.

---

## 6. Sharpened rigid witness deficit

The proof of the preserved rigid deficit theorem can now be repeated with `k_P` in place of `k` because Lemma 4.1 supplies `k_P` distinct U-witnesses for every outside source.

Let

`Z_X` and `Z_Y`

be the A--U nonedge deficits on `A_X` and `Y`, respectively. Since there is only one outside code, the U-witness union lies entirely in `U_bar d`.

### Theorem 6.1 — pair-local one-code deficit

> `Z_X >= k_P(x-1)`,                                      `(6.1)`
>
> `Z_Y >= y k_P`,                                         `(6.2)`
>
> `Z >= k_P(a-1)`.                                        `(6.3)`

### Proof

A used U-witness has exactly one neighbour in `A_X`, so each distinct witness contributes at least `x-1` nonedges to `Z_X`; one outside source already requires `k_P` distinct such witnesses. Every outside source has `k_P` distinct U-witness incidences, each a distinct Y--U nonedge, giving `Z_Y>=yk_P`. Add the two bounds and use `x+y=a`. `square`

### Theorem 6.2 — pair-local U-slack floor

Put `E_bar d=sum_{w in U_bar d} epsilon_w`. If `g0=x-T0=p-y>=1`, then

> `E_bar d >= k_P(p-1)`.                                  `(6.4)`

If `g0<=1`, writing `u_bar=|U_bar d|`, then

> `E_bar d >= [y k_P-(1-g0)u_bar]_+`.                     `(6.5)`

In particular the same inequalities hold with `E_U` in place of `E_bar d` and with `u` in place of `u_bar` in the second bound.

### Proof

For a U-witness `w` used by `t_w` outside sources, the preserved singleton-head slack inequality gives

`epsilon_w >= [g0+t_w-1]_+`.

There are at least `k_P` distinct witnesses and at least `yk_P` source-witness incidences, all inside `U_bar d`. If `g0>=1`, summing gives

`E_bar d >= yk_P+k_P(g0-1)=k_P(y+g0-1)=k_P(p-1)`.

If `g0<=1`, convex truncation over at most `u_bar` vertices gives `(6.5)`. `square`

---

## 7. Gamma/U scorecard tradeoff

The gamma-collision theorem says that a common gamma class on `g_P>=3` tight fibres is a switchable zero-signed subcore and therefore forces

> `L_A >= g_P(g_P-1)`.                                    `(7.1)`

For `g_P<=2` retain the safe zero floor. Define

> `phi(g)=g(g-1)` for `g>=3`, and `phi(g)=0` for `g<=2`.   `(7.2)`

Because `L_A` and `E_U` are disjoint parts of the scorecard `S=L_A+E_U`, Theorem 6.2 gives the central tradeoff.

### Theorem 7.1 — one-code gamma/U scorecard floor

If `g0>=1`, then

> `S >= phi(g_P)+(x-g_P)_+(p-1)`.                         `(7.3)`

Eliminating the unknown `g_P`, define

> `Psi_p(x)=min_{0<=g<=p} {phi(g)+(x-g)_+(p-1)}`.          `(7.4)`

Then every rigid one-code cut with `g0>=1` satisfies

> `S >= Psi_p(x)`.                                        `(7.5)`

This is a finite, pair-local obstruction depending only on the rigid-family size and the number of tight fibres.

### Exact evaluation

For `x>=3`, values `g>x` never improve on `g=x` when `x<=p`. The exceptional cheap cases `g=0,1,2` are minimized at `g=2`, contributing `(x-2)(p-1)`. For `g>=3` and `g<=min(p,x)`,

`phi(g)+(x-g)(p-1)=g^2-pg+x(p-1)`,                       `(7.6)`

so the remaining minimum is attained at the integer(s) nearest `p/2`, clamped to `[3,min(p,x)]`.

Thus `Psi_p(x)` is an explicit two-candidate calculation, not a new optimization problem.

A useful continuous corollary is

> `Psi_p(x)`
> ` >= max(0, min(x(x-1), x(p-1)-p^2/4)-2)`.             `(7.7)`

The exact discrete `Psi_p(x)` should be used in finite work.

### Above-threshold consequence

For an above-`M(n)` candidate the preserved scorecard gives `S<=C0`. Therefore a rigid one-code cut in the `g0>=1` regime must satisfy

> `Psi_p(x)<=C0`.                                         `(7.8)`

This is substantially more informative than the old population condition `x<=p+u`: making `g_P` large avoids U-witness load but quadratically prices the gamma collision class; making `g_P` small avoids that collision cost but forces `k_P` unmatched witnesses and their slack.

---

## 8. Purified exact pair bill

The original one-code traffic lower bound remains

> `t_P>=xy+e(Y)`.                                         `(8.1)`

The exact degree identity on `Y` is

> `2e(Y)=y(y-T0)-L_Y+Z_Y`.                                `(8.2)`

Using `Z_Y>=yk_P`,

> `2t_P+L_Y >= y(p+x+k_P)`.                              `(8.3)`

Combining `(8.3)` with `(5.2)` gives the audit-requested exact `Ccap_P+(ONE)` synthesis.

### Theorem 8.1 — purified `(ONE)`

> `R_code(S_P)[g_P+2S_P/L]+L_Y`
> ` >= y(p+x+k_P)`.                                       `(ONE-P)`

When `g_P<=x`, this is

> `R_code(S_P)[g_P+2S_P/L]+L_Y`
> ` >= y(p+2x-g_P)`.                                      `(8.4)`

The aligned crowding inequality remains

> `S_P>=y(3y-D0)` whenever `3y>=D0`.                      `(CROWD)`

The important correction is that no `2h_P` term is available to pay `(ONE-P)`.

---

## 9. Separating the matched and A/U channels

The exact pair bill can still be generous because `R_code(S_P)g_P` treats the matched channel through a code-radius envelope. Pair purity gives an exact smaller matched-source count.

### Lemma 9.1 — one-sided matched traffic

> `P_P<=g_P y`.                                           `(9.1)`

### Proof

There are `g_P` matched endpoints with gamma code `d`. A fixed such foot can certify at most one head for each A-source, and there are exactly `y` A-sources of code `d`. Endpoints with gamma code `bar d` have zero load. `square`

Hence, if `g_P<=x`,

> `C_P>=y(x-g_P)+e(Y)`.                                   `(9.2)`

Combining with `(8.2)` and `Z_Y>=y(x-g_P)` gives

### Theorem 9.2 — channel-separated one-code demand

For `g_P<=x`,

> `2C_P+L_Y >= y(p+2x-3g_P)`.                            `(9.3)`

The exact weighted A/U capacity localizes even further. Put

`u_bar=|U_bar d|`,

`E_bar=sum_{w in U_bar d} epsilon_w`.

Because `A_bar d` is empty, the preserved directed A/U capacity becomes

> `L C_P <= u_bar L_Y+yE_bar`.                            `(9.4)`

Therefore every one-code rigid survivor with `g_P<=x` satisfies

> `L_Y + 2(u_bar L_Y+yE_bar)/L`
> ` >= y(p+2x-3g_P)`.                                     `(CHAN-P)`

Together with `u_bar>=k_P` and the local slack floors `(6.4)/(6.5)`, `(CHAN-P)` retains the geometry that is lost when all pair slack is replaced by total `C0`.

---

## 10. Residual feedback

The pair-local witness floor also feeds directly into the exact rooted residual ledger. From

> `Z=u(p-lambda)+2q+E_U`,                                 `(10.1)`

and `(6.3)`, put

> `D_P^rig:=k_P(a-1)-u(p-lambda)`.                        `(10.2)`

Let `E0` be the applicable U-slack floor from Theorem 6.2 (using the local `u_bar` form where available). The same integer minimization used in the preserved rigid theorem gives

> `q+E_U >= E0+ceil([D_P^rig-E0]_+/2)`.                  `(10.3)`

Hence, from

> `f=(p-lambda)(p+u)+q+E_U-delta`,                        `(10.4)`

a rigid one-code survivor forces

> `f >= (p-lambda)(p+u)`
> `     +E0+ceil([D_P^rig-E0]_+/2)-delta`.                `(10.5)`

For an above-threshold candidate one may replace `delta` by `D_M-1`. This is the requested feedback from surviving rigid geometry into the rooted residual defect rather than another disconnected scalar estimate.

---

## 11. Finite diagnostic

The companion arithmetic diagnostic scans `3<=p<=18`, `1<=u<=18` over the same coarse above-threshold parameterization used by the previous rigid checker.

It records:

- `106,368` one-code `(p,u,lambda,x)` states passing the old population condition;
- the exact `Psi_p(x)<=C0` scorecard floor alone rejects `8,322` of those in the `g0>=1` regime;
- when the gamma floor and local U-slack floor share the **same** global scorecard `L_A+E_U<=C0`, `16,967` old-population states have no admissible `g_P` even before `(ONE-P)` or `(CHAN-P)` is used;
- adding the coarse `CROWD` ceiling raises this to `17,002`;
- a deliberately generous total-score version of `(ONE-P)` adds no further exclusions at this stage;
- the channel-separated `(CHAN-P)` adds a further `149`, giving `17,151` exclusions in this bounded diagnostic.

These numbers are **diagnostic only**. They show where the structural gain lies: the useful new obstruction is the gamma/U resource competition and, secondarily, channel separation. Collapsing the exact pair bill to total `C0` remains too lossy, so the next work should retain local `L_Y,E_bar,u_bar,S_P` rather than stack further global scalar relaxations.

---

## 12. Negative control and trust boundary

`X_3` has `u=0`, `A` independent and no nontrivial rigid complete A-cut at its canonical root. The present mechanism is therefore inactive and does not suppress the mandatory `12/32` exception.

Trust boundary:

- Lemmas 3.1, 4.1 and 5.1 are direct consequences of complementary-pair membership, matched-foot gamma localization and the rigid singleton-head property.
- Theorems 6.1--6.2 repeat the already-audited rigid witness count with the sharper pair-local matched bound.
- Theorem 7.1 adds two disjoint scorecard floors (`L_A` from gamma collision, `E_U` from U witnesses); no independence beyond the identity `S=L_A+E_U` is assumed.
- `(ONE-P)` uses the exact preserved `Ccap_P`, with the now-proved `h_P=0`.
- `(CHAN-P)` uses the directed weighted A/U capacity before code-radius relaxation.
- The finite scan is audit support, not graph realizability proof.
- No eventual theorem is claimed.
