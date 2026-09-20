# Second-strict scope repair and complete large-head mixed `y=1` closure

Date: 2026-09-20

Status: **same-session internal repair and structural closure**, conditional on the audited rigid one-code/common-buffer interface. This note corrects a scope drift in the recent `y=1` scalar diagnostics. It does not repair the independent zero-positive-rigid-cut fixture gap. `X_3` remains the mandatory negative control and is outside this unmatched branch.

## 1. Audit reconciliation

The binding daily audit remains `project/research/post_ms/2026-09-20-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Before forward work the live `CURRENT_STATE.md`, root `README.md`, latest commit chain through `6efd74e15e3bf2b3ebff5ab619962575405543d0`, and the daily audit were reread.

The requested hostile check of `EXCEPTIONAL_FZ_CROSS_CLASS_CLOSURE.md` was carried out location by location. No missing witness channel was found:

- for a hypothetical D--E outside edge, any A-witness agreeing with the source code creates a tight matched common neighbour, so the forward orientation really is forced to C-code and the reverse orientation to H-code;
- the only C-coded A candidates are `a_0` and the radius-one C-heads; `a_0` is adjacent to every ordinary Type-R outside source, while a C-head shares the buffer `b` with every ordinary outside source;
- the unique H-coded candidate is `h`; if it were adjacent to the D-head in the reverse orientation, that D-head would be a second common neighbour in the already fixed singleton `N(w_E) cap N(h)={b}`.

Thus the D--E closure survives this hostile replay. The important new finding lies one level earlier: the recent scalar diagnostic accidentally enlarged the mathematical domain.

## 2. Scope repair: `t_0=p-g>=1` never disappeared

The positive-buffer common-buffer branch was introduced with

> `t_0:=p-g>=1`.

This is explicit in `BUFFER_ROOTED_MATCHED_EDGE_COLLAPSE.md` and retained verbatim in `BUFFER_FIRST_STRICT_LAYER.md`. `FIRST_STRICT_COMPLETE_CLOSURE.md` closes the first-strict equality layer **inside that same branch** and raises the unloaded floor to

`epsilon_b>=p-g+2`.

`SECOND_STRICT_INITIAL_REDUCTION.md` is explicitly the exact-equality follow-on to that theorem. Nothing in the transition opens a new `p-g<=0` branch. Therefore every exact second-strict descendant still satisfies

> **`t_0=p-g>=1`.**                                      `(SCOPE)`

Equivalently

> `g<=p-1`.

This is also consistent with the meaning of `epsilon_b` as degree slack from the maximum-degree root: in the exact second-strict layer `epsilon_b=t_0+2>=3`.

The recent `check_y1_physical_bills.py` instead scanned the much larger range

`1<=g<x`

without imposing `(SCOPE)`. Its 2,821 / 2,840 / 691 / 2,276 survivor counts therefore included rows that are not members of the branch being proved.

The error is diagnostic scope, not a failure of the case-specific structural lemmas.

## 3. The claimed exceptional-Fz unbounded family is out of scope

`EXCEPTIONAL_FZ_K1_SCALING.md` set `k=1`, hence `g=x-1`, and then introduced a second parameter (called `t` there) by

`omega=x-p+t`.

To avoid collision with the inherited branch variable, call that new parameter `tau`.

Under the actual second-strict scope,

`t_0=p-g=p-x+1>=1`,

so

> `x<=p`.

Therefore the sentence in the scaling note asserting that, for fixed `(p,tau)`, sufficiently large `x` survives is outside the branch: `x` cannot grow past fixed `p` at all.

More strongly, the exact rooted inequalities below kill the entire large-head `y=1` branch, including any scaling in which `p` grows with `x`.

Accordingly `EXCEPTIONAL_FZ_K1_SCALING.md` is retained as a useful record of what the *scope-relaxed* scalar system does, but its “genuine unbounded family” is **superseded as evidence about the exact second-strict branch**.

## 4. Scope-correct parameterization

In the large-head mixed `y=1` classification retain

- `p>=2`, `x>=5`;
- `k=x-g>=1`;
- `t_0=p-g>=1`;
- `omega=|U_o|>=2` (and `omega>=3` in exceptional Fz).

Then

> `x=p+k-t_0`,                                           `(X)`
>
> `u=k+1+omega`,                                         `(U)`
>
> `lambda=p+t_0+omega-1`.                                `(LAM)`

Put

> `s=p+k=x+t_0`.

Since `x>=5` and `t_0>=1`,

> `s>=t_0+5>=6`.                                         `(S)`

Let `eps in {0,1}` be the parity remainder in

`floor((n-1)^2/4)=((n-1)^2-eps)/4`.

For each of the four large-head `y=1` geometries, let `B` be exactly the rooted margin used in `check_y1_physical_bills.py`:

`B=R_max-r_low`.

A realizable row requires `B>=0`.

The key point is that after `(SCOPE)` is restored, `B` is already strictly negative in every case. No pair-capacity relaxation or score-margin argument is needed.

## 5. R and no-exception Fz are impossible

For both R and Fz0, direct substitution of `(X)--(LAM)` into the existing rooted ceiling gives

> `2B = eps -2k^2-2kp+2kt_0+2k omega+2k`
> `     -p^2+6p-t_0^2-2t_0 omega-omega^2+4omega-8`.       `(B-R)`

As a real quadratic in `omega`, its unconstrained maximum occurs at

`omega=k-t_0+2`.

Therefore every allowed integer `omega` satisfies

`2B <= eps-k^2-2kp+6k-p^2+6p-4t_0-4`

`    = eps-s^2+6s-4t_0-4`.

Because `s>=t_0+5` and `-s^2+6s` is decreasing for `s>=3`,

`2B <= eps-(t_0+5)^2+6(t_0+5)-4t_0-4`

`    = eps-t_0^2-8t_0+1`

`    <= -7`.

Thus

> **R and no-exception Fz have `B<0` and are impossible.** `(R/FZ0-EMPTY)`

This is a pure rooted-ledger contradiction.

## 6. Fx is impossible

Let

`c=ceil((x+p-2)/x)>=1`.

The exact Fx rooted margin is

> `2B = -2c+eps-2k^2-2kp+2kt_0+2k omega+2k`
> `     -p^2+4p-t_0^2-2t_0 omega-omega^2+2omega+2`.       `(B-FX)`

Its real maximum in `omega` occurs at `omega=k-t_0+1`, giving

`2B <= -2c+eps-s^2+4s-2t_0+3`.

Using `s>=t_0+5`, `c>=1`, `eps<=1`,

`2B <= -2+1-(t_0+5)^2+4(t_0+5)-2t_0+3`

`    = -t_0^2-8t_0-3`

`    <= -12`.

Hence

> **Fx is impossible.**                                  `(FX-EMPTY)`

## 7. Exceptional Fz is impossible

For exceptional Fz the strengthened physical bills `G[U_o]=empty`, `epsilon_{z_0}>=p+k+omega-2`, and `r>=x+2` give

> `2B = eps-2k^2-2kp+2kt_0+2k omega`
> `     -p^2+6p-t_0^2-2t_0 omega-omega^2+4omega-10`.      `(B-FZ1)`

The unconstrained real maximum is again at `omega=k-t_0+2`:

`2B <= eps-k^2-2kp+4k-p^2+6p-4t_0-6`

`    = eps-s^2+4k+6p-4t_0-6`.

Since `k>=1`, `p<=s-1`, so

`4k+6p=4s+2p<=6s-2`.

Therefore

`2B <= eps-s^2+6s-4t_0-8`

`    <= eps-(t_0+5)^2+6(t_0+5)-4t_0-8`

`    = eps-t_0^2-8t_0-3`

`    <= -11`.

Thus

> **exceptional Fz is impossible.**                      `(FZ1-EMPTY)`

The D--E cross-class closure remains correct, but after the scope repair it is no longer needed for an asymptotic optimization: the rooted margin is already negative everywhere in the legitimate branch.

## 8. Complete large-head mixed `y=1` closure

`SECOND_STRICT_MIXED_Y1_CLASSIFICATION.md` exhausts the large-head mixed `y=1` geometry into R, Fx, Fz0, and exceptional Fz.

Sections 5--7 eliminate all four. Hence:

> **LARGE-HEAD MIXED `y=1` CLOSURE.**
>
> In the exact second-strict mixed-hole branch, under the inherited positive-buffer condition `p-g>=1`, there is no configuration with `p>=2`, `x>=5`, `y=1`. `(Y1-LARGE-EMPTY)`

Together with the previously derived mixed `y>=2` closure, the only mixed-hole remnants are the explicit small-head tails `x=3,4` (plus any separately tracked degenerate `p` boundary already outside the large-head classification).

## 9. Independent diagnostic replay

A new scope-correct checker preserves the old formulas but restricts the loop to

`1<=g<=min(x-1,p-1)`.

On the same advertised box

- `2<=p<=20`;
- `5<=x<=30`;
- `2<=omega<=24`;

it tests

- 97,980 scoped rows in each of R, Fz0 and Fx;
- 93,720 scoped rows in exceptional Fz (`omega>=3`),

and finds

> **zero necessary-condition survivors in all four cases.**

The largest rooted margin in the box is already negative:

- R: `B_max=-4`;
- Fz0: `B_max=-4`;
- Fx: `B_max=-6`;
- exceptional Fz: `B_max=-6`.

The finite replay is not the proof; it is an independent check of the analytic inequalities above.

## 10. Dependency impact and next move

The following recent evidence is now superseded **for the exact second-strict branch**:

- the 2,821 / 2,840 / 691 / 2,276 `y=1` survivor counts from the scope-relaxed checker;
- the claim that exceptional Fz has a genuine unbounded `k=1` scalar family.

The structural R/Fx/Fz classification, the hostile Fz edge exclusions, and the physical-bill lemmas remain useful conditional mathematics; their scalar survivor interpretation was the part that drifted out of scope.

The correct second-strict frontier is now:

1. mixed-hole `y>=2`: internally closed by the existing analytic package;
2. mixed-hole `y=1,x>=5`: closed above by the inherited-scope rooted contradiction;
3. mixed-hole `y=1,x=3,4`: explicit small-head tails still open;
4. two-X-hole `(2,0)`: the large `y>=2,x>=4` core-saturated two-foot branch remains structurally live, together with its small/`y=1` boundary cases.

Because the large-head `y=1` branch is now closed before pair capacity is needed, the next high-value structural work moves to the two-X-hole certificate-incidence geometry and to the small-head mixed tails. Exact pair-local `Ccap_P/(ONE-P)/(CROWD)` remains mandatory if invoked later; it is not needed to justify `(Y1-LARGE-EMPTY)`.