# Residual-one k=2 compressed half barrier — additive refinement

Date: 2026-09-20

Status: **same-session accounting refinement and correction** to `ONE_CODE_R1_K2_COMPRESSED_GLOBAL_HALF_BARRIER.md`, under the same conditional `k=2`, `J2=empty`, compressed normal form. No finite scan is used.

The predecessor half-barrier theorem is correct. Its provisional equality classification was too permissive because it compared two lower bounds by a maximum even where substantial pieces live in disjoint currencies and can be added. Retaining that additivity leaves only one coefficient-`1/2` endpoint: asymptotically pure compressed F0.

## 1. Reuse the compressed P block

Let

- R be K-heavy, density `alpha`;
- D be W_s-free non-K-heavy, density `delta`;
- T=F1 union W-heavy, density `vartheta`;
- M be mixed, density `mu`;

with

`alpha+delta+vartheta+mu=1`.

Under the compressed normal form, all but `o(p)` vertices of D form the proper-support q_j-nonneighbour set P. The predecessor complement-capacity theorem gives

`M_U(P,E)/p^2 >= delta-delta^2/2-o(1)`.                 `(AR-P)`

The K-heavy Y-capacity theorem gives

`Z_Y(R)/p^2 >= alpha(1-delta)-o(1)`.                    `(AR-RY)`

These two blocks are disjoint.

## 2. T and M costs are additive to the P/Y blocks

The predecessor T bill is

- `Z_Y(T)>=vartheta(p-1)`;
- `M_U(R,T)>=alpha*vartheta*p^2-o(p^2)`.

Neither overlaps `(AR-P)` or `(AR-RY)`:

- Y--T and Y--R have different U endpoints;
- R--T pairs have no P endpoint.

Hence T contributes an additional asymptotic coefficient

`vartheta(1+alpha)`.                                     `(AR-T)`

For M, the mixing theorem gives `epsilon_w>=p+1`, so

`E_U(M)/p^2 >= mu-o(1)`.                                 `(AR-M0)`

This is a different term of `D_phys=E_U+Z_X+Z_Y+M_U`, so it adds to both `(AR-P)` and `(AR-RY)` even when the same graph nonedge helps create the slack.

Moreover every mixed vertex touches W_s and therefore has code different from `bar d`. Complement capacity gives at most two neighbours in P. The missing P-neighbours are disjoint from the two K/W_s holes and the `p-1` matched-fibre holes used in the original proof of `epsilon_w>=p+1`. Thus

`epsilon_w >= p+|P|-1`,

so in fact

> `E_U(M)/p^2 >= mu(1+delta)-o(1)`.                     `(AR-M)`

## 3. Direct additive compressed bound

Adding the four disjoint currencies/blocks `(AR-P)`, `(AR-RY)`, `(AR-T)`, `(AR-M)` gives

> `liminf D_phys/p^2 >= F(alpha,delta,vartheta,mu)`,
>
> `F = delta-delta^2/2 + alpha(1-delta)`
> `    + vartheta(1+alpha) + mu(1+delta)`.               `(AR-F)`

For fixed alpha,delta, the residual mass

`r0=1-alpha-delta=vartheta+mu`

should be placed in the cheaper of T and M. Therefore

`F >= delta-delta^2/2 + alpha(1-delta)`
`     +(1-alpha-delta)(1+min(alpha,delta))`.             `(AR-MIN)`

## 4. Exact minimization

### Case A: `alpha<=delta`

The residual mass is cheapest in T. Then

`F >= 1+alpha-alpha^2-2alpha*delta-delta^2/2`.           `(AR-A)`

For fixed delta this is concave in alpha, so the minimum over

`0<=alpha<=min(delta,1-delta)`

occurs at an endpoint.

- At `alpha=0`, `F=1-delta^2/2>=1/2`, with equality only at `delta=1`.
- If `delta<=1/2`, the other endpoint is `alpha=delta`, giving
  `F=1+delta-(7/2)delta^2>=5/8`.
- If `delta>=1/2`, the other endpoint is `alpha=1-delta`, giving
  `F=1-delta+delta^2/2=1/2+(1-delta)^2/2>=1/2`, again with equality only at `delta=1`.

### Case B: `delta<=alpha`

The residual mass is cheapest in M. Then

`F >= 1+delta-2alpha*delta-(3/2)delta^2`.                 `(AR-B)`

For fixed delta this decreases with alpha, so the minimum occurs at `alpha=1-delta`. Feasibility of `delta<=alpha` gives `delta<=1/2`, and

`F >= 1-delta+delta^2/2`
`   = 1/2+(1-delta)^2/2`
`   >=5/8`.

Therefore

> **`liminf D_phys/p^2 >= 1/2`**                         `(AR-HALF)`

and the only way to attain coefficient `1/2` in the compressed relaxation is

> **`alpha=0`, `delta=1`, `vartheta=mu=0`.**             `(AR-EQ)`

Equality in the K-heavy Y-cap step is vacuous because R is absent; the class identity says the entire escape reservoir is asymptotically D. To attain the compressed P premise with no positive-density non-F0 repair complication, the live equality endpoint is therefore asymptotically pure F0.

## 5. Correction to the predecessor equality statement

`ONE_CODE_R1_K2_COMPRESSED_GLOBAL_HALF_BARRIER.md` correctly proved the coefficient-`1/2` barrier, but its Section 6 statement that an `R:M=1:1` endpoint remains at equality is **superseded**.

At `delta=0`, `alpha=mu=1/2`, the K-heavy Y-hole block already contributes `1/2`, while mixed slack contributes another `1/2` in the separate `E_U` currency. Thus that endpoint costs at least coefficient one in `D_phys`, not one half.

The only coefficient-`1/2` compressed endpoint left is pure F0.

## 6. Pure-F0 equality normal form

At the remaining endpoint:

- `E=F0` up to `o(p)` vertices;
- almost every escape misses q_j;
- almost every escape has proper, asymptotically sparse private support;
- P is independent, so `M_U(E)=binom{|E|}{2}-o(p^2)` already supplies the entire half-quadratic leading term;
- any additional quadratic `E_U`, `Z_X`, or `Z_Y` would push the coefficient strictly above `1/2`.

For an exact F0 vertex t the preserved sector identity is

`alpha_H(t)+beta_Y(t)+gamma_E(t)=p-4+epsilon_t`.

In the pure independent endpoint `gamma_E(t)=p-2+o(p)`, hence

`alpha_H(t)+beta_Y(t)=epsilon_t-2+o(p)`.

Thus coefficient-`1/2` equality forces, on average,

- `epsilon_t=2+o(p)`;
- `alpha_H(t)+beta_Y(t)=o(p)`.

So the next literal object is an almost-independent U-reservoir whose vertices are simultaneously almost complete to H and Y while being K-free, W_s-free, q_j-nonneighbours and sparse-support. This is far more rigid than the previous R/F0/M optimizer.

## 7. Next attack

Do not continue broad coefficient algebra. Hostile-replay `(AR-F)` and then attack the pure-F0 equality normal form directly:

1. classify A--U criticality for an F0--Y edge under near-completeness to H and Y;
2. classify F0--H edges and test whether the same sparse-support vertex can be simultaneously H-complete and Y-complete without creating extra common neighbours;
3. use any forced H/Y holes or additional U-slack in the exact weighted rooted ledger;
4. retain the zero-positive rigid-fixture caveat and do not interpret the half barrier as a graph-realizability theorem.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`.