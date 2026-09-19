# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph `X_3` is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_COMMON_BUFFER_ORIENTATION_REPAIR_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `c884e045fe9d757ec2c0d8f4ea245bcba7b72dc6`

LAST VERIFIED RESULT: `The previous matched-only classification of the minimal r=0 common-buffer edge b--x contained a raw criticality orientation error and is withdrawn. The corrected theorem says at most g reverse orientations exist, so at least k=x-g edges use the other orientation; each such certificate is either a matched foot with gamma=c(x) or an outside unmatched witness z in U_o with c(z)=bar c(x) and z anticomplete to Y. In the zero-buffer case g=p, the matched option is impossible and all k forced certificates are outside-U. Outside reuse forces H_Y>=ym and yields a repaired score/residual floor.`

UNPRESERVED WORK: `None. The invalidated statement, replacement theorem, arithmetic checker, audit scope and next frontier are preserved in project/research/post_ms/2026-09-19-common-buffer-criticality-repair-v1/.`

DEFERRED ADMIN: `Do not churn CI or reviewer packaging during this mathematics run. README remains lower-frequency and should be refreshed at the next daily audit/reviewer milestone if this repair survives the next attack.`

NEXT ACTION: `Stay on z=1 common-buffer. First attack the zero-buffer g=p subbranch with the new forced outside-U load, retaining the local pair score S_P and intersecting SP-LOCAL with exact Ccap_P, exact crossing traffic, ONE-P and CROWD. Feed any surviving local geometry through QE-CB into the rooted residual ledger. Then treat p-g>0 via the matched-cap/outside-hole dichotomy and only afterwards return to r>0. Do not move to z=2 or resurrect the invalid matched-only demand unless a separately proved restriction removes the outside-U channel.`

## Audit reconciliation

Before forward mathematics this run, `CURRENT_STATE.md`, `README.md`, recent commits, the 19 September daily adversarial/red-team audit/handoff, the source-premise repair, the finite source-tuple trust boundary and the independent actual-D2C Hall/pair-capacity regression were reread.

There is no departure from the audit priority order:

1. distinct physical-source identity and selected `(source,coordinate)` uniqueness remain independently repaired at the raw/selected interface;
2. the finite source-tuple theorem is not promoted as unconditional graph-level closure;
3. the independent actual-D2C regression remains mandatory, includes `X_3`, and still records zero graph/formula mismatches;
4. there is still no positive actual-graph fixture realizing the rigid complete Hall cut with `x>=3`, so the one-code results remain conditional hand structural implications;
5. exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain load-bearing and are not replaced by a coarse total-score collapse;
6. the four-exception gate remains subordinate; the closed mixed `{4,5}` ladder stays closed; first-proof priority on Erdos #742 stays inactive.

The new repair is itself an audit-driven departure from the *previous handoff*, not from the daily audit: the handoff proposed a gamma/code attack because it assumed a matched-only criticality localization. The raw orientation check invalidated that premise, so continuing the code-only line would have violated the user's instruction not to build downstream theory on a weakened premise.

## Mandatory negative control

`X_3` remains explicit and untouched: `n=12`, `m=32>M(12)=31`, diameter two, every edge critical, canonical root `a=3,b=8,p=4,u=0`, `Q=12`, `r=f=delta=0`. All common-buffer statements below require a nonempty unmatched-U mechanism (`k+1<=u`) and therefore do not exclude `X_3`.

## Scope of the invalidation

The affected file is

`project/research/post_ms/2026-09-19-common-buffer-criticality-v1/ANTICOMPLETE_BUFFER_X_EDGE_TRICHOTOMY.md`.

Its old Orientation I required simultaneously

`x z in E`, `b z notin E`, `N(x) cap N(z)={b}`,

which is impossible because `b z` is a nonedge. Therefore its matched-only Orientation-I localization and the consequent unconditional `>=k` gamma-aligned matched-foot demand are **withdrawn**.

The following predecessor results survive this check:

- `UNLOADED_COMMON_BUFFER_SOURCE_EDGE_DICHOTOMY.md`, including source--buffer triangle-freeness for `r>0`, the rectangular Y-hole product, the buffer/Y slack formulas and the common-buffer score floor;
- `check_z1_criticality_collapse.py`, because it does not use the faulty follow-on;
- the full-support `OMITTED_PAIR_NONEDGE_FORCING.md` theorem `nu=y`; a hostile reread found its two criticality orientations correctly paired with their singleton heads;
- the source-premise repair, graph-level regression, exact pair capacity, `(ONE-P)` and `(CROWD)`.

## Corrected minimal r=0 common-buffer theorem

Retain the unloaded common-buffer equality geometry:

- `X--Y` complete, `x=|X|>=3`, `y=|Y|>0`;
- all Y-sources have code d, `A_{bar d}=emptyset`;
- `g=g_P`, `k=x-g>0`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- `r=d_Y(b)=0`;
- `epsilon_b=p-g`, so b is complete to X and `U_o`.

Every `b x` edge lies in a triangle. The two correct criticality orientations are:

`(A)` `b z in E`, `x z notin E`, `N(x) cap N(z)={b}`;

`(B)` `x z in E`, `b z notin E`, `N(b) cap N(z)={x}`.

Orientation B still has only matched witnesses with `gamma(z)=bar d`, and each matched foot has at most one singleton X-head. Hence at most g buffer--X edges can use B, so at least

> `k=x-g`

edges use A.

Corrected Orientation A has exactly two surviving locations:

1. matched B, with `gamma(z)=c(x)`;
2. `z in U_o`, with `c(z)=bar c(x)` and z anticomplete to all of Y.

Thus choose k forced-A edges and split their X-sources into matched and outside sets of sizes `q_M,ell`:

> `q_M+ell=k`.                                             `(MO1)`

No injectivity is asserted.

## Aligned-code capacity and forced outside load

For `lambda>=0` and an above-threshold candidate, use the preserved aligned-code cap

`w_c=2n_c+t_c<=R_code(C0)`,

where

`D0=5p+5u-3lambda-2`,

`R_code(C0)=floor((D0+sqrt(D0^2+12C0))/3)`.

Put

> `R_A=floor(R_code(C0)/2)`.

Then every A-code class has size at most `R_A`.

Matched Orientation-A feet for X-sources cannot lie in the g fibres whose gamma pair is `{d,bar d}`. The remaining `p-g` fibres expose at most `2(p-g)` usable gamma codes. Hence

> `q_M<=2(p-g)R_A`,

and therefore

> `ell >= ell_0=[k-2(p-g)R_A]_+`.                         `(OUT-FORCE)`

If `epsilon_b=0`, then `g=p`, so the matched capacity is zero and

> `ell=k=x-p`.                                             `(ZERO-OUT)`

This is the key reversal of the invalid handoff: **zero buffer slack forces outside-U certificates, not matched gamma-aligned certificates.**

## Outside-witness holes and score

Let W be the set of distinct outside witnesses chosen for the ell sources, `m=|W|`, and let `t_z` be the reuse load of z. A fixed z can serve only one X-code class, so `t_z<=R_A`, giving

> `m>=ceil(ell/R_A)`                                       `(REUSE)`

when `ell>0`.

Each z is anticomplete to Y, hence

> `H_Y>=ym`.                                               `(HY)`

It is also nonadjacent to its `t_z` served X-sources, and its U-slack satisfies

> `epsilon_z>=[p-x+t_z]_+`.

Thus

> `E_W>= [ell-(x-p)m]_+`.                                 `(EW)`

For `r=0` the Y-slack identity is exact:

> `L_Y=y(p-g+1)+H_Y`,

so

> `L_Y>=y(p-g+1+m)`.                                      `(LYM)`

With `E_core=k(p+k-2)`, the repaired score floor is

> `S>=E_core+(p-g)+E_W+max{phi(g),y(p-g+1+m)}`.          `(S-REPAIR)`

The one-code pair itself satisfies the sharper local floor

> `S_P>=E_core+(p-g)+y(p-g+1+m)`.                         `(SP-LOCAL)`

This is the quantity to intersect next with exact pair-local capacity rather than replacing it by total C0.

## Rooted residual feedback

Physical A--U nonedges obey

> `Z>=k(a-1)+y+ym+ell`.                                   `(Z-REPAIR)`

The terms are: `k(x-1)` X-holes from the common core, `y(k+1)` Y-holes to core plus buffer, `ym` Y-holes to the outside witnesses, and ell chosen X--outside witness nonedges.

Using

`Z=u(p-lambda)+2q+E_U`

and

`E_U>=E0:=E_core+(p-g)+E_W`,

put

`D_CB=k(a-1)+y+ym+ell-u(p-lambda)`.

Then

> `q+E_U>=E0+ceil([D_CB-E0]_+/2)`.                       `(QE-CB)`

Together with

`f=(p-lambda)(p+u)+q+E_U-delta`,

this feeds the repaired common-buffer geometry directly into the residual defect ledger.

At zero buffer slack (`g=p`, `ell=k`) the nonedge floor simplifies to

> `Z>=ka+y(1+m)`.                                         `(Z-ZERO)`

## Diagnostic audit

Companion checker:

`project/research/post_ms/2026-09-19-common-buffer-criticality-repair-v1/check_common_buffer_x_edge_repair.py`.

It audits the convex outside-witness slack inequality and replays the same coarse integer parameter box as the predecessor. It records:

- 16,065 exhaustive small convex-reuse checks, minimum margin zero, failures zero;
- 345,219 abstract r=0 equality `(p,u,lambda,x,g)` branches passing the predecessor scalar floor;
- 17,174 with positive forced outside load under `(OUT-FORCE)`;
- in this box, all 17,174 are exactly the zero-buffer `g=p` cases;
- 113 zero-buffer abstract branches rejected by the repaired Y-hole score floor;
- 17,061 zero-buffer abstract branches remain.

These are diagnostic parameter-branch counts, not D2C graph counts.

## Preserved full-support comparator

The full-support `z=1,h=0` branch remains the more expensive comparator. Raw criticality still forces every omitted source--`U_-` pair to be a nonedge (`nu=y`), and its corrected rooted-triangle baseline remains

`Q=p(p-1)+pu+e(G[U])`.

No claim from the current repair weakens that branch.

## Immediate research frontier

The highest-value next theorem is now narrower than the invalid handoff suggested:

1. **Zero-buffer first.** With `g=p`, all k forced Orientation-A certificates are outside-U. Use their forced local pair slack `(SP-LOCAL)` and residual floor `(QE-CB)`.
2. **Exact pair intersection.** Keep `S_P` live and impose `2xy<=Ccap_P`, exact `Ccap_P=R_code(S_P)[g+2S_P/(lambda+1)]`, `(ONE-P)` and `(CROWD)` simultaneously. Do not substitute total C0 until the local feasibility interval has been exhausted.
3. **Then `p-g>0`.** Use `q_M<=2(p-g)R_A` and the outside-hole surcharge together. Do not assume distinct matched feet.
4. **Then `r>0`.** The source--buffer triangle-free/rectangular-hole theorem is still valid and can be attacked after the corrected r=0 equality branch.
5. Do not move to `z=2` while these minimal `z=1` geometries remain live.
<!-- CURRENT-STATUS:END -->
