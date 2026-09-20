# Residual-one low-k escape family and k=2 mixing dichotomy

Date: 2026-09-20

Status: **same-session candidate structural/diagnostic package**, conditional on the rigid one-code residual-one interface and the hostile-replayed hub/private-orientation package. The first part independently hostile-replays the preceding orientation-covering theorem. The parameter family below is **not a graph construction**. Finite computation is diagnostic only. `X_3` and the zero-positive actual-D2C rigid complete-cut caveat remain binding.

## 1. Hostile replay of the orientation-covering theorem

Use the notation of `ONE_CODE_R1_ORIENTATION_COVERING.md`. For an escape vertex `w in E=U\W_s`, write

- `A_w={h in K: wh in E(G)}`;
- `B_w={h in K: wz_h in E(G)}`;
- `S_w={i in J1: wq_i in E(G)}`;
- `T_w={i in J1: wh_i in E(G)}`.

The two forcing statements survive direct replay from the singleton equations:

1. if `h in A_w` and `i in S_w`, reverse orientation would make `w` a second common neighbour of `q_i` and `h`, so `(h,i)` is forced F;
2. if `h in B_w` and `i in T_w`, forward orientation would make `w` a second common neighbour of `z_h` and `h_i`, so `(h,i)` is forced R.

A cell cannot be both orientations. Hence

> `(A_w cap B_w) x (S_w cap T_w)=empty`.                 `(LK-RECT)`

The physical counting also survives. If `A_w cap B_w=empty`, at least `k` of the `2k` pairs from `w` to `K union W_s` are absent. If `S_w cap T_w=empty`, at least `|J1|` pairs from `w` to the distinct matched vertices `{q_i,h_i:i in J1}` are absent. These pairs are all in the degree universe of the exact U-slack identity and are disjoint from each other.

For the radius-two part, if `w` sees any `q_i`, `i in J2`, predecessor `(OM-BAD0)` makes `w` anticomplete to K and costs `k` missing pairs. Otherwise all `|J2|` such `q_i` are absent, disjoint from the J1 pairs. Thus the predecessor conclusion is recovered without importing its scalar proof:

> `epsilon_w >= min(k,p-1)` for every escape `w`,         `(LK-ESC)`
>
> `E_E >= (c-1)min(k,p-1)`.                              `(LK-RES)`

No overlap defect was found in `(OC-RECT)--(OC-RES)` at the stated conditional scope.

## 2. Full OC-score optimization exposes a new exact low-k ray

The strengthened score floor does not close the whole residual-one domain. There is a particularly simple exact scaling family.

For every integer `t>=4`, set

- `c=p=t`;
- `y=t-1`, hence `g0=1`;
- `lambda=p-y+c-1=t`;
- `k=2`;
- `u=k+c-1=t+1`;
- `x=k+p-1=t+1`;
- `m=p-1=t-1`, so the residual dimension is exactly one.

The beta map `f:K->K\{h}` is then forced to be the transposition on the two K-heads, so

> `s_f=2`.                                                `(LK-SF)`

The order is

> `n=4p+2u-lambda=5t+2`.                                 `(LK-N)`

Thus the family is genuinely unbounded at the parameter level.

### Exact score quantities

For `s_f=2`, the exact predecessor terms are

`L0(2)=floor(5t/2)+2`,

`T(2)=2t+2`.

For `t>=4`, `L0(2)>T(2)`. The used-witness and escape-reservoir bills are

`k(p+k-2)=2t`,

`(c-1)min(k,p-1)=2t-2`.

Hence `(OC-SCORE)` requires only

> `floor(13t/2) <= C0`.                                  `(LK-SCORE-LB)`

The exact ceiling is

> `C0=floor((3t^2+10t-4)/2)`.                            `(LK-C0)`

The right side is quadratic while the strengthened physical floor is linear. The inequality holds for every `t>=4` and its margin grows.

### Exact rooted gate

The predecessor rooted gate has left side

`k(x+y-1)+T(2)=6t`.

Because `p=lambda=t`, its right side is

`(t-1)(t+2)+C0=t^2+t-2+C0`.

Thus the rooted margin is

> `t^2-5t-2+C0`,                                         `(LK-ROOT-M)`

which is positive already at `t=4` and grows thereafter.

Therefore the new ray survives both the full strengthened residual-one score gate and the exact predecessor rooted-Q gate. This is a method diagnostic, not realizability evidence.

## 3. Audit-mandated exact pair-local gates also remain open on the ray

Take the natural minimal pair count

`g_P=m=t-1`,

so `k_P=x-g_P=2=k`. The two selected used witnesses lie in the complementary `U_bar d` class, so the safe pair-located slack already satisfies

`S_P>=k(p+k-2)=2t`.

For a lower-capacity hostile test set `S_P=2t`. The exact pair parameter is

> `D0=5p+5u-3lambda-2=7t+3`.                             `(LK-D0)`

The preserved exact capacity uses

`R_code(S_P)=floor((D0+sqrt(D0^2+12S_P))/3)`.

Since the square root is at least `D0`,

`R_code(2t)>=floor(2D0/3)>=4t+2`.

Also

`g_P+2S_P/(lambda+1)`
`=t-1+4t/(t+1)`
`=t+3-4/(t+1)`
`>t+2` for `t>=4`.

Consequently

> `Ccap_P>(4t+2)(t+2)=4t^2+10t+4`.                      `(LK-CCAP)`

The crossing demand is only

`2xy=2(t+1)(t-1)=2t^2-2`,

so exact `Ccap_P` has large positive margin.

Purified `(ONE-P)` has right side

`y(p+x+k_P)=(t-1)(2t+3)=2t^2+t-3`,

which is also strictly below the same lower bound `(LK-CCAP)` even with `L_Y=0`.

Finally the scalar `(CROWD)` floor is zero because

`3y-D0=3(t-1)-(7t+3)=-4t-6<0`.

Thus all three audit-mandated aggregate pair-local scalar gates remain open on this low-k ray. This conclusion is deliberately limited: it does not test every physical distribution constraint behind the pair quantities.

## 4. k=2 forces a beta cross-hole normal form

Write `K={a,b}`. Because `f` has no fixed point,

`f(a)=b`, `f(b)=a`.

The two beta singleton equations are therefore

`N(z_a) cap N(b)={q_j}`,

`N(z_b) cap N(a)={q_j}`.                                 `(LK-BETA)`

For every escape vertex `w`, these imply the two cross exclusions

> `w a` and `w z_b` cannot both be edges;
>
> `w b` and `w z_a` cannot both be edges.                `(LK-CROSS)`

Hence every escape vertex already misses at least two of its four possible pairs to

`{a,b,z_a,z_b}`.                                         `(LK-2HOLE)`

More sharply, if `w` has at least one K-neighbour and at least one W_s-neighbour, `(LK-CROSS)` forces those neighbours to have the same head index. Therefore

> `A_w != empty` and `B_w != empty` imply `A_w cap B_w != empty`. `(LK-MIX0)`

This is special to the two-head endpoint and is stronger than the generic rectangle statement.

## 5. Mixed K/W escape vertices are very expensive

Assume `w` is mixed, i.e. it has a neighbour in K and a neighbour in W_s. By `(LK-MIX0)`, `A_w cap B_w` is nonempty, so `(LK-RECT)` forces

`S_w cap T_w=empty`.

Therefore w misses at least `|J1|` distinct radius-one fibre pairs.

A mixed w cannot be J2-bad: `(OM-BAD0)` would make it anticomplete to K, contradicting mixedness. Hence w misses every `q_i`, `i in J2`, adding `|J2|` further distinct pairs.

Finally `(LK-2HOLE)` contributes two missing K/W pairs, disjoint from all matched-fibre pairs. Since `|J1|+|J2|=p-1`,

> **if an escape vertex touches both K and W_s, then**
> **`epsilon_w >= p+1`.**                                `(LK-MIX)`

Equivalently, every escape vertex with slack `<p+1` is one-sided:

> **either `N(w) cap K=empty` or `N(w) cap W_s=empty`.**  `(LK-ONESIDE)`

This is the main structural consequence of the new low-k analysis. The scalar floor `epsilon_w>=2` hides a much sharper fact: cheap escape vertices cannot simultaneously serve the K-head degree demand and the used-witness degree demand.

## 6. Strategic consequence

The full residual-one obstruction has moved. The previous high-k `y=1` ray is finite after orientation covering, but the exact low-k/high-y family above remains unbounded even after the strengthened score/rooted gates and the audit-mandated aggregate pair-local gates.

The next attack should therefore retain the **one-sided escape partition** supplied by `(LK-ONESIDE)` instead of immediately summing escape slack. A successful closure would show that maximum-degree requirements force many escape vertices to serve both K and W_s, triggering the `p+1` price, or else that separating the escape reservoir into K-serving and W-serving sides creates enough located holes in the rooted residual/triangle ledger to contradict near equality.

The dominant global caveat remains unchanged: bounded graph-level regression still has zero positive actual-D2C rigid complete Hall-cut fixtures with `x>=3`.