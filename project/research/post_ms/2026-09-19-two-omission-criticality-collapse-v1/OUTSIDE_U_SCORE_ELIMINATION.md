# Eliminate outside-U corrections into a sharp full-support score surcharge

Date: 2026-09-19

Status: internal structural corollary in the rigid one-code `z=1`, `h=0`, full-support branch. This note continues `OUTSIDE_U_EXACT_BALANCE.md` and uses no new selected-witness premise.

## 1. Starting point

The forced omitted-nonedge theorem and exact outside-U degree sum give

> `S >= B+M+E_o+max{phi(g), L0+H_Y}`,                     `(1.1)`

where

> `L0=y(p-g+1)`,                                           `(1.2)`

and

> `H_X+H_Y+M`
> ` =u_o(p+k+1-lambda)+2Q_o+E_o`.                         `(1.3)`

Here

- `H_X` and `H_Y` are X--`U_o` and Y--`U_o` nonedges;
- `M` is the number of missing `U_- -- U_o` edges;
- `Q_o=e(G[U_o])`;
- `E_o` is total slack on `U_o`;
- `u_o=u-k-1`;
- `x=g+k`;
- `B=(k+1)(p+k-1)`.

The only crude bound used below is the physical capacity

> `H_X<=x u_o`.                                            `(1.4)`

The point is to eliminate `H_X,H_Y,M,E_o` without replacing the local geometry by total score `C0`.

## 2. Structural unit I — an outside correction must spill beyond X

Subtract `(1.4)` from `(1.3)`. Since `x=g+k`,

`p+k+1-lambda-x=p-g+1-lambda`.

Therefore

> `H_Y+M`
> ` >= u_o(p-g+1-lambda)+2Q_o+E_o`.                       `(2.1)`

In particular, with

> `R_o=[u_o(p-g+1-lambda)+2Q_o]_+`,                       `(2.2)`

we have the safe physical spill bound

> `H_Y+M>=R_o`.                                            `(2.3)`

Thus once all possible X--`U_o` holes have been used, any remaining outside degree deficit must appear either as a Y-hole or as a missing `U_- -- U_o` edge. Internal outside edges cost two further incidences each before slack is even counted.

## 3. Structural unit II — exact minimization of where the spill lands

Write

`A0=phi(g)`.

For fixed nonnegative `H_Y,M` with `H_Y+M>=R_o`, the part of `(1.1)` depending on their split is

> `M+max{A0,L0+H_Y}`.                                      `(3.1)`

The minimum of `(3.1)` is exact:

### Lemma 3.1

> `min_{h,m>=0, h+m>=R} [m+max{A,L+h}]`
> ` =max{A,L+R}`.                                          `(3.2)`

### Proof

It is enough to take `h+m=R` because both terms are monotone. Put `m=R-h`, `0<=h<=R`.

If `A<=L+h`, the expression is `R+L`. If `A>L+h`, it is `R-h+A`, minimized by taking h as large as the regime permits. If `A<=L+R`, the two regimes meet at value `L+R`; if `A>L+R`, the best choice is `h=R`, giving A. Thus the minimum is `max{A,L+R}`. `square`

This tiny optimization is useful because a Y-hole and a missing U-edge look different in the graph but have exactly interchangeable unit price until the gamma floor dominates.

## 4. Structural unit III — outside-aware score theorem

Dropping the manifestly nonnegative `E_o` in `(1.1)`, using `(2.3)` and Lemma 3.1 gives:

### Theorem 4.1 — exact-Q_o outside spill score floor

> `S`
> ` >= B+max{phi(g),`
> `          y(p-g+1)`
> `          +[u_o(p-g+1-lambda)+2Q_o]_+}`.               `(4.1)`

This retains the genuine internal outside-edge variable `Q_o` but eliminates all artificial correction-placement variables.

Since `Q_o>=0`, a parameter-only corollary is

> `S`
> ` >= B+max{phi(g),`
> `          y(p-g+1)`
> `          +u_o[p-g+1-lambda]_+}`.                      `(4.2)`

This strictly strengthens the first forced-omitted-nonedge floor whenever

`u_o>0` and `lambda<p-g+1`

unless the gamma collision term already dominates.

## 5. Structural unit IV — internal outside edges are never free

Equation `(4.1)` makes a useful stability statement explicit.

If

> `u_o(p-g+1-lambda)+2Q_o>=0`,

then every additional internal edge of `G[U_o]` increases the non-gamma branch of the score lower bound by **two units**, until the gamma term `phi(g)` becomes dominant.

Therefore any near-score-minimal full-support survivor is driven toward an independent outside-unmatched layer. This is not assumed as a theorem of realizability; it is the exact price of choosing `Q_o>0` inside the current branch.

## 6. Structural unit V — useful low-imbalance specialization

When

> `lambda<=p-g+1`,                                        `(6.1)`

formula `(4.2)` becomes

> `S`
> ` >= B+max{phi(g),`
> `          y(p-g+1)+u_o(p-g+1-lambda)}`.                `(6.2)`

At exact root balance `lambda=0`,

> `S`
> ` >= B+max{phi(g),(y+u_o)(p-g+1)}`.                     `(6.3)`

Thus at balance, outside unmatched vertices and outside A-sources contribute to the same linear deficit coefficient `p-g+1`; moving vertices from Y into `U_o` does not make that part of the bill disappear.

This is a cleaner structural picture than the predecessor free-correction ledger.

## 7. Diagnostic impact

A bounded arithmetic replay on the same coarse grid used by the preceding one-code checkers (`3<=p<=18`, `1<=u<=18`, all admissible nonnegative `lambda`, `3<=x<a`) gives:

- forced-omitted-nonedge base-score survivors: 59,500;
- survivors after the parameter-only outside spill floor `(4.2)`: 59,028;
- additional abstract parameter states rejected by the new spill theorem: 472.

These are parameter states, **not D2C graph counts**. The diagnostic merely confirms that `(4.2)` is a genuine strengthening and that its active region is primarily low root imbalance with nonempty `U_o`.

## 8. Trust boundary and next use

The theorem uses only:

1. the exact outside-U degree identity;
2. the physical bound `H_X<=x u_o`;
3. the already-proved forced omitted nonedges;
4. the existing gamma floor `phi(g)`.

No source-tuple theorem, finite graph scan or witness injectivity is used.

For the next step, retain `(4.1)` rather than `(4.2)` whenever `Q_o` is also constrained by another part of the rooted ledger. The most promising remaining question is whether the exact pair-local crossing bill `2xy<=Ccap_P` can be combined with this spill floor before replacing `S_P` by total S. A global `S_P<=C0` relaxation has already proved too generous and should not be repeated as the main attack.
