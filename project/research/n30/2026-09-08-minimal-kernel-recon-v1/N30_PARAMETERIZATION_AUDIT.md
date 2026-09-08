# n=30 parameterization audit: from the standalone bridge to (a,b)=(13,16)

8 September 2026. Research direction: Paul Lenz. Mathematical development and internal audit: ChatGPT/Geeps.

**Status: same-assistant candidate audit, not independent review.** This note checks that the graph-theoretic bridge isolated for the n=29, Delta=16 calculation is genuinely parameteric in `a=deg_H(v)` and `b=|B|`, and records every numerical specialization used for n=30. It does not by itself prove the n=30 result.

## 1. Scope

Let `G` be a 30-vertex diameter-two edge-critical graph with

`Delta(G)=16`

and `m in {225,226}`. Put `H=\bar G`, choose a minimum-degree vertex `v` in `H`, and set

`A=N_H(v)`, `B=V(H)\N_H[v]`.

Then

`a=|A|=30-1-16=13`,

`b=|B|=16`.

With

`t=m-b(30-b)=m-16*14`,

we have

- `m=226 -> t=2`;
- `m=225 -> t=1`.

Both scopes have `t>0`, so the residual-activity lemma applies.

## 2. Quasi-edge construction is unchanged

For a missing unordered pair `uw` in `H[B]`, inserting `uw` corresponds to deleting the critical G-edge `uw`. The enlarged complement acquires an adjacent total-dominating pair. It cannot be `{u,w}`, since both B-vertices miss `v`. Thus, after interchanging `u,w` if necessary, there is an old cross-edge `ui` with `i in A` and

`N_H(u) union N_H(i)=V(H)\{w}`.

Choose one such `ui->w` for every missing B-pair. The B-source and unique exception recover the missing pair, so distinct missing B-pairs choose distinct selected cross-edges and each unordered B-pair receives at most one chosen orientation.

Nothing in this argument uses `a=12`; only the partition by a minimum-complement-degree vertex is used.

## 3. Exact ledger

With `C=H[A]`, `F=\bar C` on `A`, residual row degrees `rho_u`, residual column degrees `R_i`, actual selected column degrees `x_i`, and

`r=sum rho=sum R`,

counting H gives for all `a,b`:

`e(F)=r+t`,

`sum_i d_i=2(r+t)`.

Minimum H-degree gives

`x_i>=s_i=max(0,d_i-R_i)`

and hence

`S=sum_i s_i>=r+2t`.

For n=30 this is unchanged except that there are 13 labels rather than 12.

## 4. Pointwise forcing and the changed constants

For every selected `ui->w`, the same neighbourhood argument gives

`d_i<=rho_u+R_i`,

`d_i<=rho_u+rho_w`,

`d_i<=rho_u+q_u-1`,

`rho_w+q_w>=q_u-1`,

`R_i+x_i>=q_u+p_u`.

The first inequality implies the source-demand rule

`s_i<=rho_u`

for every selected source of label `i`.

The cross-neighbour count becomes

`q_u+rho_u<=a=13`.

The exact missing-degree identity is still

`q_u+p_u = missing degree of u in H[B]`.

Since

`deg_H(u)=rho_u+b-1-p_u >= a`,

we obtain the general supplement bound

`p_u<=rho_u+b-a-1`.

For `(a,b)=(13,16)` this is

`p_u<=rho_u+2`.

Also

`q_u+p_u<=b-1=15`.

These are exactly the source-type bounds encoded in `n30_threshold_model.py`.

## 5. Residual activity

The proof that `t>0` forces every `rho_u>=1` is parameteric.

Assume `rho_u=0`, put `U=N_A(u)` and `T=A\U`. There are no F-edges between U and T. Every F-edge inside U produces two distinct residual cross-edges using the distinct supplements of selected edges at `u`. Every F-edge inside T produces a distinct residual cross-edge with A-endpoint in T. The families are disjoint. Hence

`r>=2e(F[U])+e(F[T])>=e(F)=r+t`,

contradicting `t>0`.

Therefore for both n=30 dense scopes

`rho_u>=1` for all 16 B-sources and `r>=16`.

## 6. Charging specialization

The parameteric charging theorem is

`r-b >= sum_i s_i(s_i-1)/(a-s_i)`

and therefore

`sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t`.

At n=30, Delta=16:

`sum_{i=1}^{13} s_i(14-2s_i)/(13-s_i) >= 16+2t`.

Thus the right side is

- `20` at m=226;
- `18` at m=225.

No n=29 constant is retained.

## 7. Isolated-C exclusion and dmax

The parameteric isolated-C proof gives, if `C=H[A]` has an isolated vertex,

`b<=a-1-t`.

At `(a,b)=(13,16)` this would require

- `16<=10` for `t=2`;
- `16<=11` for `t=1`.

Both are impossible. Hence

`delta(C)>=1`.

Therefore

`d_i<=a-2=11`,

and by the handshake lemma

`e(C)>=ceil(a/2)=7`.

Since

`e(C)+r=C(a,2)-t`,

we obtain the safe row-total bounds

- `r<=78-2-7=69` at m=226;
- `r<=78-1-7=70` at m=225.

These are the only new row-total tightenings used by `n30_prepare.py`.

## 8. Threshold capacity is unchanged

For `h>=1`, define

`I_h={i:s_i>=h}`, `W_h=sum_{i in I_h}s_i`,

`Z_h={u:rho_u>=h}`, `z_h=|Z_h|`.

Exactly the same source/supplement argument gives

`2W_h <= z_h^2-z_h+h(h+1)`.

The proof uses only:

1. source demand `s_i<=rho_u` on every selected incidence;
2. distinct selected sources for one label;
3. one selected orientation per unordered B-pair;
4. supplement confinement to `Z_h` for a source carrying more than h heavy selected labels.

None depends on `a=12` or n=29.

This theorem is used twice in the n=30 pipeline:

- at demand preparation, with an optimistic upper bound on `z_h` inferred from `r_max`;
- after a concrete residual row is known, with its exact value `z_h=|{u:rho_u>=h}|`.

The second application is strictly stronger and is what reduces the clean residual frontiers from 35,530 to 9 rows at m=226 and from 150,896 to 272 rows at m=225.

## 9. Source-capacity Hall dual is unchanged

For a sorted largest-demand k-prefix with total `D_k`, a source of residual degree `j` has at most

`A_{k,j}=min(a-j, # eligible top-k labels with demand <=j)`

selected incidences into that prefix.

At n=30, `a=13`; the proof and exact dual combination are otherwise unchanged. `n30_prepare.py` uses rationally checked dual weights both to reject impossible demand profiles and, when no contradiction is obtained, to raise the certified lower bound on `r`.

Using a valid dual lower bound to increase `r_min` cannot discard a graph: every graph source-count vector satisfies the primal Hall system from which the bound is derived.

## 10. Residual-row scanner is unchanged except for dimensions

The scanner uses length-16 rows with entries `1<=rho_u<=13`. Its initial cap is

`c_u=min(13-rho_u, # {i:s_i<=rho_u})`.

Largest-demand-prefix Hall is necessary. The supplement-cap refinement remains monotone: if current caps dominate actual selected degrees, every actual supplement required for source degree q also satisfies the weaker supporter condition using current caps; therefore the refined value remains an upper bound on actual q.

No n=29-specific `a=12` or hidden `b=16` assumption remains beyond the explicit n=30 constants.

## 11. Fresh corrected cumulative-threshold model

`n30_threshold_model.py` is a new source file specialised directly to `a=13,b=16`; it does not import the historical n=29 threshold builders.

The empirical graph embedding has the same normalization as corrected n=29 v2:

- `Y`: fraction within an equal-demand label group;
- `T`: fraction of the **whole demand group** with a fixed `(d,R)` option and `x>=h`;
- `W`: fraction within an equal-rho source group;
- `P`: density among ordered distinct source/target pairs;
- `Z`: density among source-label pairs.

The two dimensionally critical incidence identities are

`sum_g n_g Z = q W` per source type,

and

`sum_k n_k Z = sum_h T_h` per label option.

There is no extra label-group multiplicity on the right of the second identity.

The nested selected-slot capacity is

`E[x 1{x>=h}] = (h-1)T_h + sum_{j=h}^U T_j`.

The source-type bounds are the n=30 values

`q<=13-rho`,

`p<=rho+2`,

`q+p<=15`.

The label degree bound is

`d<=11`.

The same-rho-group ordered-pair capacity is deliberately relaxed to `<=1`; an actual graph satisfies the stronger density bound `<=1/2`. This can create false LP survivors but cannot create a false exclusion.

Thus every actual graph surviving the preceding necessary cuts still maps to a feasible point of the n=30 LP.

## 12. Exact Farkas semantics

The n=30 model uses the same proof event as corrected n=29 v2 but in a fresh implementation. HiGHS may propose an infeasibility ray. A row is counted as excluded only after integer multipliers are reconstructed and checked directly:

- inequality multipliers nonnegative;
- equality multipliers signed integers;
- combined coefficient of every nonnegative primal variable nonnegative;
- combined right-hand side strictly negative.

A feasible nonnegative primal point would then give a nonnegative combined left side bounded by a negative number, impossible.

## 13. Audit conclusion

No n=29-specific graph lemma was needed to pass from `(a,b)=(12,16)` to `(13,16)`. The changes are exactly:

- 13 A-labels rather than 12;
- `q+rho<=13`;
- `p<=rho+2` rather than `rho+3`;
- `dmax=11` rather than 10;
- charging denominator 13 rather than 12;
- `t=2` or 1 rather than 3 or 2.

The proof-critical finite path for n=30 Delta=16 is therefore a genuine parameterization of the standalone bridge, not a new bespoke graph model.

**Independent mathematical review remains OPEN.** A failure of any universal graph lemma overrides every successful finite replay.
