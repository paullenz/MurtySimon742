# Maximal m=2, p>=3, x>=4: exact Hall/residual closure

Date: 2026-09-20

Status: **internal candidate structural theorem**, conditional on the independently audited first-strict unique-hole setup, the maximal raw-eligibility matching normalization, the corrected m=2 F/R normal form in `M2_BULK_BLOCK_SCOPE_CORRECTION.md`, and the raw same-code theorem already re-derived in `SAME_CODE_RAW_CRITICALITY_AUDIT.md`. This note independently rechecks the raw-edge collapse before using it. It does not alter the zero-positive-fixture caveat for the rigid complete-cut interface.

## 1. Audit reconciliation and scope

The 20 September daily adversarial audit remains binding. In particular:

- P1/P2 retain their repaired physical / selected-representative meanings;
- `X_3` remains the mandatory hostile control;
- exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` remain load-bearing wherever pair capacity is used;
- bounded actual-D2C regression still contains no positive rigid complete Hall-cut fixture with `x>=3`;
- finite scans are diagnostics only.

The predecessor proved, for maximal `m=2`, `p>=3`, `x>=4`, that the two X'-code classes have the corrected complementary F/R normal form

`|S_0|=1`, `I_F=S_0`, `I_R=I_0`.

The previous raw-edge note treated `omega=|U_o|>2`. Sections 2--5 below first independently audit its edge exclusions, then show that the same physical collapse extends to the remaining `omega=2` case, and finally use the exact Hall identity rather than another scalar approximation.

Write

- `A=X dotcup Y`, `|X|=x`, `|Y|=y>0`, `X--Y` complete;
- `x=g+k`, `k>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`;
- `omega=|U_o|=u-k-1>=2`;
- `C_R` for the radius-one code differing from `d` on the singleton `S_0={s}`;
- `C_F=bar C_R`.

Thus `a_0` and the R-heads have code `C_R`, while every F-head has code `C_F`.

## 2. Independent hostile replay of the raw-edge collapse

For `omega>2`, the matching-one component with multiple F-witnesses has a unique F-head `f`; write its witness star `Z_F=U_o\{z_R}`. Rechecking every witness location gives the same predecessor conclusions:

1. `Z_F--R_X` is empty. A same-code `C_R--C_R` edge would require a complementary witness. The only A-side complementary head is `f`, but every eligibility edge gives `N(z) cap N(f)={b}`; `z_R` gives the fixed `N(r) cap N(z_R)={b}`.
2. `z_R--Z_F` is empty. A U--U orientation must use an A-witness; the only possible code classes reduce to the same fixed eligibility pairs above.
3. `z_R` misses every F-head. A same-code `C_F--C_F` certificate again reduces to a fixed eligibility pair or to two X-vertices sharing the nonempty set `Y`.
4. every F-witness is A-anticomplete.
5. every F--R edge is impossible. In each orientation, a matched witness has an extra fixed common neighbour (`b` or `Y`); X-witnesses share `Y`; `z_R` and the F-witnesses miss the required head; a common-core witness shares a tight matched endpoint with the source.
6. same-code R--R edges then have no complementary witness, so `G[R_X]` is empty.
7. `a_0` misses every F-head by the same two-orientation exhaustion: matched witnesses have `z_R`, `b` or `Y` as an extra common neighbour; outside witnesses miss the head; core witnesses share a fixed tight endpoint.

Hence `G[X]` is edgeless and `G[U_o]` is edgeless for `omega>2`.

### The `omega=2` extension

Now `U_o={z_F,z_R}`. The F-class need not be a singleton head, but every F-head has the same sole physical witness `z_F`, while every R-head has the sole R-witness `z_R`.

The seven exclusions above do not use F-head uniqueness once `z_F` is fixed:

- `z_F--R_X` is excluded exactly as in item 1;
- `z_Rz_F` is excluded because every possible F-head has the fixed singleton pair `N(f) cap N(z_F)={b}`;
- `z_R` misses **every** F-head by the item-3 argument;
- `z_F` is A-anticomplete;
- the F--R exhaustion applies head-by-head;
- then both the R-class and the F-class are internally independent by the same-code theorem, because their only complementary physical witnesses miss all heads of the opposite class;
- `a_0` misses every F-head by the item-7 exhaustion.

Type R already gives `a_0--R_X` empty. Therefore the same graph-level conclusion holds:

> **For every `omega>=2`, `G[X]` and `G[U_o]` are edgeless.**       `(M2-XUO-EMPTY)`

Moreover the only X--`U_o` edge is `a_0z_R`: `N_A(z_R)={a_0}` and every F-witness is A-anticomplete.

## 3. Exact X--U incidence and exact X-slack

The preserved common-core theorem gives every vertex of `W_0` exactly one X-neighbour, so `e(X,W_0)=k`. The buffer has exactly the first-strict adjacency pattern `e(X,{b})=x-1`. By `(M2-XUO-EMPTY)`,

`e(X,U_o)=1`.

Hence

> `e(X,U)=k+x`,
>
> `Z_X=e_bar(X,U)=xu-(x+k)=k(x-1)+x omega`.             `(ZX-EXACT)`

Because `G[X]` is empty and `X--Y` is complete, every X-vertex has A-degree `y`. Summing the rooted slack identity over X gives

> `L_X=x(p+u-y)-e(X,U)`
>
> `   =x(p+k+omega-y)-k`.                               `(LX-EXACT)`

Equivalently, the exact Hall-density identity for the complete X--Y cut,

`2e(X)=x(p-y)-L_X+Z_X`,

reduces at `e(X)=0` to exactly the same formula. This is the previously unused consequence of the raw-edge collapse.

The reverse-fan theorem gives the exact physical Y-price

> `L_Y=y(p-g+1+omega)`.                                 `(LY-EXACT)`

## 4. Sharpened local rooted-slot floor

The code geometry also gives a sharper local Hamming bill than the predecessor diagnostic used.

- `x-1` X-vertices have code `C_R`, at Hamming distance one from `d`; each contributes at least one unused rooted slot.
- every F-head has code `C_F`, at Hamming distance `p-1` from `d`. In the `omega>2` branch there is one F-head, and in `omega=2` there may be more. For a universally weakest bound, retain only one such head. It contributes at least `p-1` slots.
- each `y in Y` sees all x X-vertices. Its total Hamming load is at least `(x-1)+(p-1)=x+p-2`, so for `p>=3` the local slot theorem gives at least two slots per Y-vertex.

Thus every survivor obeys

> `r >= x+p-2+2y`.                                      `(R-LOW)`

When `omega=2` has more than one F-head this bound is conservative, so the closure below remains valid.

## 5. Physical U-score and triangle ceilings

The raw collapse gives, for every `omega>=2`,

> `E_{U_o} >= omega^2+(p-1)omega-1`.                    `(UO-SCORE)`

For `omega=2` this is `2p+1`; for `omega>2` it is the predecessor bill.

The independent sets `U_-` and `U_o`, together with the preserved `k-1` core-separation holes, give

> `q <= Q:=binom(u,2)-binom(k+1,2)-binom(omega,2)-(k-1)`
>
> `      =k omega-k+omega+1`.                            `(Q-M2)`

The exact common-core plus weakest forced-hole bill is

> `E_core >= k(p+k-1)+(k-1)=k(p+k)-1`,

and the first-strict buffer pays `epsilon_b=p-g+1`.

Therefore the global score cap `L_A+E_U<=C_0` implies the necessary score inequality

> `L_X+L_Y+[k(p+k)-1]+(p-g+1)`
> `   +[omega^2+(p-1)omega-1] <= C_0`.                  `(SCORE-M2)`

No pair-local score has been substituted into total score here; `(SCORE-M2)` uses only disjoint physical lower bounds.

The rooted residual identity and `E_U<=C_0-L_X-L_Y` give

> `r <= (p-lambda)(p+u)+Q+C_0-L_X-L_Y`.                 `(R-UP)`

## 6. Analytic contradiction for `omega>=3`

It is useful to remove the floor in `C_0` only in the weakening direction. Put

`H=floor((lambda+1)^2/4)`.

Then

> `2H >= lambda(lambda+2)/2`.                            `(H-FLOOR)`

Set

`tau=p-y>=1`,
`X0=x-4>=0`, `K0=k-1>=0`, `W0=omega-3>=0`, `Y0=y-1>=0`.

Substitute `(LX-EXACT)`, `(LY-EXACT)` and `u=k+1+omega` into `(SCORE-M2)`, multiply by two, and weaken with `(H-FLOOR)`. A necessary condition is

> `F:=4tau-Q0 >=0`,                                     `(F-SCORE)`

where

> `Q0=23+(K0-W0)^2+(X0-Y0)^2`
> `      +2(K0+W0)(X0+Y0)+2K0+8W0+12X0`.              `(Q0)`

Hence `Q0>=23`, so the integer `tau>=6`, and also

> `X0 <= (4tau-23)/12`.                                 `(X0-CAP)`

Now combine `(R-UP)` with `(R-LOW)`, multiply by two and again weaken with `(H-FLOOR)`. A necessary condition is `R>=0`, where

> `R= -K0^2-2K0 tau-2K0Y0-2K0`
> `   -2tau^2-2tau W0+2tau X0-2tau Y0`
> `   -W0^2-2W0Y0-4W0`
> `   -X0^2+4X0Y0-4X0-Y0^2+4Y0-5`.                    `(R-POLY)`

Drop the nonpositive K0/W0 terms. By `(X0-CAP)`,

`4X0-2tau+4 <= -(2tau+11)/3 <0`,

so the entire Y0-dependent contribution is nonpositive. Thus

`R <= -2tau^2+2tau X0-X0^2-4X0-5`.

The right side is increasing in X0 throughout the allowed interval, because `(4tau-23)/12 < tau-2`. Evaluating at the endpoint gives

> `R <= -(208tau^2+560tau+145)/144 <0`,

contradicting the necessary `R>=0`.

Therefore:

> **No maximal `m=2`, `p>=3`, `x>=4`, `omega>=3` first-strict graph exists.** `(M2-OMEGA3-CLOSED)`

This is an analytic contradiction, not a bounded scan and not a use of pair capacity.

## 7. Analytic contradiction for `omega=2`

Repeat the same weakened score/residual calculation with

`X0=x-4`, `K0=k-1`, `Y0=y-1`, `tau=p-y`.

The score condition becomes

> `4tau >= Q2`,                                         `(F2-SCORE)`
>
> `Q2=15+K0^2+2K0(X0+Y0+2)`
> `      +(Y0-X0-1)^2+8X0`.                            `(Q2)`

Thus `tau>=4` and

> `X0 <= (4tau-15)/8`.                                  `(X02-CAP)`

The weakened residual condition is `R2>=0`, where

> `R2= -K0^2-2K0tau-2K0Y0-2K0`
> `    -2tau^2+2tau X0-2tau Y0+2tau`
> `    -X0^2+4X0Y0-4X0-Y0^2+6Y0-2`.                  `(R2-POLY)`

Dropping the K0 terms and using `(X02-CAP)`,

`4X0-2tau+6 <= -3/2 <0`,

so the Y0 contribution is nonpositive. Hence

`R2 <= -2tau^2+2tau X0+2tau-X0^2-4X0-2`.

This is increasing in X0 on the allowed interval. At `X0=(4tau-15)/8`,

> `R2 <= -(80tau^2+120tau-127)/64 <0` for `tau>=4`,

again a contradiction.

Therefore:

> **No maximal `m=2`, `p>=3`, `x>=4`, `omega=2` first-strict graph exists.** `(M2-OMEGA2-CLOSED)`

Since maximal `m=2` requires `omega>=2`, Sections 6 and 7 give the complete large-X closure:

> **For maximal `m=2`, `p>=3`, every first-strict survivor has `x=3`.** `(M2-LARGEX-CLOSED)`

## 8. Trust boundary and next branch

The closure is entirely hand-derived once the raw-edge exclusions and audited upstream identities are accepted. The exact pair-local `Ccap_P/(ONE-P)/(CROWD)` machinery is not weakened or replaced; it simply is not needed for this particular contradiction.

The next live maximal-m=2 branch is therefore `p>=3, x=3`. Here `X'` has two singleton heads, so the bulk-block argument no longer forces complementary F/R blocks. The correct next task is to classify the two singleton code blocks and their physical witness stars directly. The separate `p<=2` remainder should remain behind that classification unless it becomes load-bearing.
