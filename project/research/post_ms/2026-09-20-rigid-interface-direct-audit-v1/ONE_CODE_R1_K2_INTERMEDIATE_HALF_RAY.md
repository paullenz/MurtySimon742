# Residual-one k=2: explicit intermediate half-ray after the high-Y endpoint closure

Date: 2026-09-20

Status: **same-session corrected method diagnostic / exact parameter ray**, conditional on the residual-one `k=2,J2=empty` interface and the hostile-replayed off-ray capacity package. This is **not a graph construction**. A same-session draft incorrectly set `B0=empty`; that is impossible because the two selected complementary witnesses lie in `B0`. The corrected minimal physical assignment is `|B0|=2`. All conclusions below use that correction.

## 1. Exact ray and mandatory B0 floor

For every integer `t>=4`, set

- `p=2t`,
- `c=t`,
- `y=t`, hence `g0=p-y=t`,
- `lambda=c+p-y-1=2t-1`,
- `u=c+1=t+1`,
- `x=p+1=2t+1`,
- `k=2`,
- `m=p-1=2t-1`,
- residual dimension `r=1`.

The two selected U-witnesses `W_s` have code `bar d` and exactly one A_X-neighbour, their selected K-head. In particular they have no H-neighbour, so

> **`W_s subseteq B0={w in U_bar(d):d_H(w)=0}`.**        `(HR-BMIN)`

Hence `b=|B0|>=2`. The cheapest exact assignment is therefore

> **`b=2`, with `B0=W_s`.**                               `(HR-B2)`

Put `D=U\B0`; then `|D|=t-1`. The cross-edge count

`C=e(B0,D)`

is not set to zero; only

`0<=C<=2(t-1)`.

Thus the normalized parameters remain

`theta=y/p=1/2`, `kappa=c/p=1/2`,

while

`eta=b/p=1/t ->0`, `q=C/p^2->0`.

So the same normalized intermediate point survives, but the literal finite geometry contains the mandatory two selected B0 witnesses.

## 2. Exact score ceiling

The exact score ceiling is

`C0=(lambda+2)(p+u)+p-A_lambda`.

Here `lambda=2t-1` is odd and

`A_lambda=floor(lambda^2/2)+lambda+5=2t^2+4`.

Therefore

> **`C0=4t^2+7t-3`.**                                   `(HR-C0)`

## 3. Corrected physical score floor still leaves a quadratic margin

The general Y--U capacity theorem gives

`Z_YU>=max{by, |D|(y-1)}`.

With `b=2`, `|D|=t-1`, `y=t`, the second arm dominates for `t>=4`:

> **`Z_YU >= (t-1)^2`.**                                 `(HR-ZY)`

The two selected B0 witnesses are Y-anticomplete and each has exactly one X-neighbour. Therefore each contributes

`(x-1)+y=2t+t=3t`

located A--U holes, for `6t` holes in total. Every D vertex lies in the outside escape reservoir and global H/Y polarization contributes at least

`min{|H|,y-1}=t-1`

holes. These vertex blocks are disjoint, so

> **`Z >= 6t+(t-1)^2=t^2+4t+1`.**                       `(HR-Z)`

B0 is independent. Every D source has oriented U--U source capacity at most two, hence

`e(U)<=C+2|D|<=4(t-1)`.                                  `(HR-UE)`

Since `p-lambda=1`, the exact rooted identity gives

`E_U=Z-u(p-lambda)-2e(U)`,

and therefore

> **`E_U >= t^2-5t+8`.**                                 `(HR-E)`

Because `e(Y)=0`,

`L_Y=Z_YU-y`,

so

> **`L_Y >= t^2-3t+1`.**                                 `(HR-LY)`

Consequently

> **`E_U+L_A >= 2t^2-8t+9`.**                            `(HR-SCORE-LB)`

This is still far below `C0=4t^2+7t-3`; the leading score-floor coefficient is `2` in t^2 versus ceiling coefficient `4`.

Thus the intermediate half-ray remains a genuine aggregate-method escape after correcting the impossible `b=0` assignment.

## 4. Rooted-Q feedback remains open

The residual-one rooted-Q necessary inequality is

`2(x+y-1)+phi(p-1)`
` <= u(p-lambda)+2(c-1)u-(c-1)c+C0`.

The left side is

`6t+(2t-1)(2t-2)=4t^2+2`,

while the right side is

`(t+1)+(t^2+t-2)+C0=5t^2+9t-4`.

Hence the rooted margin is

> **`t^2+9t-6>0`.**                                      `(HR-ROOT)`

The normalized rooted restriction is likewise satisfied with margin:

`1 < kappa theta+S0 = 5/4`.

## 5. Audit-mandated exact pair-local scalar gates

Take

`g_P=m=2t-1`,

so

`k_P=x-g_P=2`.

The selected complementary used-witness pair contributes the safe pair-located slack floor

`S_P>=k(p+k-2)=2p=4t`.

For the hostile lower-capacity test set `S_P=4t`. Then

`D0=5p+5u-3lambda-2=9t+6`.

The exact capacity is

`Ccap_P=R_code(S_P)[g_P+2S_P/(lambda+1)]`,

with

`R_code(s)=floor((D0+sqrt(D0^2+12s))/3)`.

Since the square root is at least D0,

`R_code(4t)>=6t+4`,

and

`g_P+2S_P/(lambda+1)=(2t-1)+8t/(2t)=2t+3`.

Therefore

> **`Ccap_P >= (6t+4)(2t+3)=12t^2+26t+12`.**             `(HR-CCAP)`

The crossing demand is only

`2xy=4t^2+2t`,

and purified `(ONE-P)` asks only

`y(p+x+k_P)=4t^2+3t`.

Both have large positive margin. Finally

`3y-D0=-6t-6<0`,

so scalar `(CROWD)` is zero.

Hence all three audit-mandated aggregate pair-local scalar gates remain open on this corrected ray.

## 6. Corrected literal geometry

The correction changes the pointwise interpretation but not the asymptotic sparsity:

1. `B0=W_s` in the minimal assignment, so exactly two mandatory selected witnesses are H/Y-anticomplete;
2. `e(Y)=0`;
3. every Y--U edge is triangular;
4. high-Y vertices in D must reverse-certify through one of the two B0 witnesses, hence
   `e(Y,D)<=yb+|D|=3t-1`;
5. therefore `e(Y,U)=O(p)` even though an individual D vertex may have Y-degree larger than one;
6. `e(U)<=4t-4=O(p)` by B0 independence plus D-source capacity.

Thus the correct physical normal form is not “every U vertex has Y-degree at most one”. It is:

> **Y is independent, Y--U is globally sparse, U is globally sparse, and only two physical B0 vertices provide all high-Y reverse-certificate capacity.** `(HR-PHYS)`

That is an even more concentrated witness bottleneck and should be retained explicitly.

## 7. Next raw-criticality target

Do not re-optimize the aggregate pair scalars; they have quadratic margin. Attack the sparse Y/U system through the H layer.

In particular:

- keep the two selected B0 witnesses explicit rather than replacing them by normalized eta=0;
- retain the endpoint-indexed U-code classes that certify H--H edges;
- exploit that all but O(p) H--U edges are triangular (companion H--U triangle-scope lemma);
- orient that triangular bulk and test whether two B0 witnesses can supply the required reverse-certificate load without creating additional H/Y/U hole rectangles.

Upstream caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`; `X_3` remains mandatory.