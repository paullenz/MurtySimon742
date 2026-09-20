# One-code rigid cut — residual-one hub criticality

Date: 2026-09-20

Status: **same-session structural theorem package**, conditional on the rigid one-code near-equality interface, the private-coordinate normal form/exhaustion theorem, and the independently hostile-replayed raw same-code / rooted B-edge criticality mechanisms. It does not assert that the rigid interface is graph-realizable. The bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control.

This note continues the exact residual-dimension-one (`r=1`) frontier. Its main point is that the unique residual coordinate creates a literal rooted hub. Raw criticality of the hub spokes forces considerably more geometry than the scalar `r=1` profile records.

## 1. Setup

Fix a minimum-U source `s in Y=A_d`. Write

- `K` for its `k` U-certified heads;
- `H={h_i:i in I}` for its `m=p-1` matched-covered heads;
- `R={j}` for the unique residual coordinate;
- `d_U=c-1`, so `k=u-c+1`;
- `C=d xor e_j`.

Private-coordinate exhaustion gives

> `c(h)=C` for every `h in K`,
>
> `supp(c(h_i) xor d)` is `{i}` or `{i,j}` for `i in I`.

Thus `A_C=K`: no matched-covered head has code `C`, and `Y=A_d`.

For every `h in K`, let `z_h in U_bar(d)` be the selected U-witness for the crossing edge `s h`. Then

> `N(s) cap N(z_h)={h}`,
>
> `N(z_h) cap A_X={h}`.                                  `(RH-1)`

The `z_h` are distinct for the fixed source because the selected crossing heads are distinct physical singleton heads.

For each coordinate `ell`, write `q_ell` for the tight matched endpoint selected by `bar d`, i.e. the endpoint opposite the one selected by `d`.

## 2. A dead end worth preserving: the head-witness edge recycles its original certificate

The edge `h z_h` is itself critical, but applying edge criticality directly to it creates no new obligation. Indeed the already-selected pair `(s,z_h)` has

`N(s) cap N(z_h)={h}`.

After deleting `h z_h`, that unique length-two route from `s` to `z_h` disappears. Thus the original crossing certificate simultaneously certifies the head-witness edge.

> **HEAD-WITNESS RECYCLING OBSTRUCTION.** Directly reapplying criticality to `h z_h` does not advance the `r=1` branch. `(RH-REC)`

The correct object is instead the rooted matched edge through the unique residual coordinate.

## 3. The residual coordinate is a common physical hub

At coordinate `j`, both `C=d xor e_j` and `bar d` select `q_j`. Therefore for every `h in K`,

> `h q_j in E`, `z_h q_j in E`, and `h z_h in E`.         `(RH-HUB)`

So `q_j` is joined to all of `K` and all of `W_s={z_h:h in K}`, and each pair `(h,z_h)` completes a triangle through the same matched hub `q_j`.

This is a literal physical configuration, not a code-counting relaxation.

## 4. Hub-spoke criticality is forced into one beta orientation

Fix `h in K` and its witness `z=z_h`. The edge `z q_j` lies inside the rooted neighbourhood `B=N(v)`, so raw rooted B-edge criticality supplies one of the two standard singleton orientations.

### Reverse orientation is impossible

Suppose the source were `q_j`, the singleton head `z`, and the A-witness `a`. Then `a` must be adjacent to `z` and nonadjacent to `q_j`.

- If `a in A_X`, `(RH-1)` forces `a=h`, but `h q_j in E` by `(RH-HUB)`, contradicting the required source-witness nonedge.
- If `a in Y`, then `h` is adjacent to both `q_j` and `a` because `A_X--Y` is complete. Hence `h` is a second common neighbour of `q_j,a`, distinct from the prescribed head `z`.

So the reverse orientation cannot occur.

### The forward witness has code exactly C

Hence `z q_j` must be beta-oriented from source `z`: there is `a in A` with

> `N(z) cap N(a)={q_j}`,                                  `(RH-BETA)`

and `za` is the critical nonedge.

A Y-vertex cannot contain the head `q_j`, because every Y-code is `d`. Thus `a in A_X`.

Now `z` has code `bar d`, so it is adjacent to `q_i` for every private coordinate `i in I`. To keep `(RH-BETA)` singleton, `a` must avoid every such `q_i`; therefore `a_i=d_i` for all `i in I`. At coordinate `j`, `a` must contain the head `q_j`, so `a_j!=d_j`. Since `I=[p]\{j}`,

> `c(a)=d xor e_j=C`.

Thus `a in A_C=K`. Write one such witness as `a_h`.

Because `za_h` is the critical nonedge while `zh` is an edge,

> `a_h in K\{h}`.                                         `(RH-A1)`

Moreover, if `h a_h` were an edge, then `h` would be a second common neighbour of `z,a_h` in `(RH-BETA)`. Hence

> `h a_h notin E`.                                        `(RH-A2)`

Finally, every vertex of Y is adjacent to `a_h`. Therefore any Y-neighbour of `z` would also be a second common neighbour in `(RH-BETA)`. Consequently

> **`N_Y(z_h)=empty` for every `h in K`.**                 `(RH-Y0)`

Combining `(RH-1)` and `(RH-Y0)`, every selected `r=1` U-witness has exactly one A-neighbour:

> **`N_A(z_h)={h}`.**                                     `(RH-AEXACT)`

In particular `k>=2` whenever the `r=1` branch has a U-certified head.

## 5. The selected witness set is anticomplete to the entire bar-d U-class

The earlier hostile replay proved only `G[W]` independent for the global used-witness union; it deliberately did not claim anticompleteness from a used witness to an unused same-code U-vertex because the valid same-code edge orientation might choose the unused endpoint as source.

The new hub theorem removes exactly that gap for the fixed `r=1` minimum-source set `W_s`.

Take `z in W_s` and any `z' in U_bar(d)`. Suppose `zz' in E`.

Apply the independently repaired same-code U--U theorem. Its A-witness has complementary code `d`, hence lies in `Y`.

- If the valid source orientation chooses `z`, the predecessor hostile-replay argument applies: the unique X-head `h(z)` is adjacent to both `z` and every Y-witness, giving an illicit extra common neighbour.
- If the valid source orientation chooses `z'`, then the singleton head is `z`. The Y-witness must therefore be adjacent to `z`, contradicting `(RH-Y0)`.

Hence

> **`E(W_s,U_bar(d))=empty`.**                             `(RH-Ubar0)`

This is stronger than `G[W_s]` independent, but only at the present `r=1` scope where `(RH-Y0)` has been proved.

## 6. U-certified heads are anticomplete to all matched-covered heads

Fix `h in K` and `h_i in H`, with private coordinate `i in I`. By the private-coordinate normal form, `q_i` has the unique X-neighbour `h_i`. Since `z_h` has code `bar d`, `z_h q_i` is an edge in the rooted B-layer.

Suppose `h h_i in E`. Apply rooted B-edge criticality to `z_h q_i`.

### Forward orientation `z_h -> q_i`

The A-witness must contain `q_i`. No Y-vertex contains `q_i`, and `h_i` is its unique X-neighbour, so the witness must be `h_i`. But then `h` is adjacent to both `z_h` and `h_i`, giving a second common neighbour besides `q_i`.

### Reverse orientation `q_i -> z_h`

The A-witness must be adjacent to `z_h`. By `(RH-AEXACT)` it must be `h`. But then `h_i` is adjacent to both `q_i` and `h`, giving a second common neighbour besides `z_h`.

Both orientations fail. Therefore

> **`E(K,H)=empty`.**                                     `(RH-KH0)`

This is a strong physical decomposition of the internal X-layer in residual dimension one:

> `G[A_X]=G[K] dotcup G[H]` with no cross edges.           `(RH-XSPLIT)`

## 7. The hub beta certificates force a missing-edge matching budget inside K

For every `h in K`, `(RH-A1)--(RH-A2)` supply at least one different vertex `a_h in K` nonadjacent to h. Therefore the complement of `G[K]` has minimum degree at least one. Consequently

> `e(bar G[K])>=ceil(k/2)`,
>
> **`e(K)<=binom(k,2)-ceil(k/2)`.**                       `(RH-KMISS)`

Independently, the existing residual-one complement localization gives `A_bar(C)=empty` and `|U_bar(C)|<=c-1`, hence

> `e(K)<=k(c-1)`.                                         `(RH-KCAP)`

Thus the safe combined upper bound is

> **`2e(K)<=min{ k(k-1)-2ceil(k/2), 2k(c-1) }`.**         `(RH-KBEST)`

The map `h -> a_h` need not be injective: selected P2 is uniqueness for one physical `(source,coordinate)` obligation, and here the physical sources `z_h` are all different while the coordinate is always j. Likewise P1 forbids one fixed A-witness from reusing one unmatched source across *different* coordinates; it does not forbid many sources at the same coordinate from using the same A-witness. Therefore P1/P2 alone do **not** give a constant bound on k. This is an important method obstruction to the naive “one residual coordinate implies O(1) witnesses” hope.

## 8. Stronger Hamming/slack floor in the near-rigid provenance

Assume now `p>=4`, so `|H|=p-1>=3`. The preserved near-rigid theorem `J_X<1` and the private-coordinate separation of H give

> `e(H)<p/4`.                                             `(RH-HSPARSE)`

The exact rigid X-degree identity is

> `2e_X=x g0-L_X+Z_X`,

while the selected U-witnesses give

> `Z_X>=k(x-1)`.

Using `(RH-XSPLIT)`, `(RH-HSPARSE)`, and `(RH-KBEST)`,

`2e_X < p/2 + min{ k(k-1)-2ceil(k/2), 2k(c-1) }`.

Hence

> **`L_X > x g0 - p/2 +`**
> **`max{ k(p-1)+2ceil(k/2), k(p+k-2c) }`.**              `(RH-LX)`

Here we used the exact `r=1` identity

> `x-k=m=p-1`.

The first term already improves the predecessor residual-one specialization by `2ceil(k/2)`; the second becomes stronger when the complement-code capacity `k(c-1)` beats the trivial density of K.

An exact integral form is

> `L_X >= floor( x g0-p/2+max{...} )+1`.                  `(RH-LXINT)`

The hostile-replayed physical witness theorem simultaneously gives

> `E_U>=E_{W_s}>=k(p+k-2)`.                               `(RH-EW)`

Since `L_X` is A-slack and `E_{W_s}` is U-slack, these are non-overlapping and may be added in the global score ceiling.

## 9. Rooted-Q feedback also strengthens

The same fixed-source witness set is independent, so with `d_U=c-1`,

> `q<= (c-1)u-c(c-1)/2`.                                 `(RH-Q)`

The exact rooted identity and score ceiling therefore imply the residual-one necessary inequality

> **`k(x+y-1)+L_X^{min}`**
> **`<=u(p-lambda)+2(c-1)u-c(c-1)+C0`,**                  `(RH-QF)`

where `L_X^{min}` is the integer floor in `(RH-LXINT)`. This replaces the much weaker `phi(p-1)` term in the predecessor residual-one rooted-Q inequality whenever `(RH-LX)` dominates it.

## 10. Stress test on the exact post-exhaustion escape ray

For the preserved family

`c=p=2t`, `y=1`, `g0=2t-1`, `lambda=4t-2`, `u=x=3t`,

`k=t+1`, `d_U=2t-1`, `r=1`,

the first term in `(RH-LX)` gives

> **`L_X>=8t^2-3t+2ceil((t+1)/2)`.**                      `(RH-RAY-LX)`

Together with

`E_W>=3t^2+2t-1`,

the total physical score floor is

> `E_W+L_X>=11t^2-t-1+2ceil((t+1)/2)`.

The exact score ceiling is still

`C0=12t^2+6t-4`,

leaving margin

> `t^2+7t-3-2ceil((t+1)/2)>0` for every `t>=2`.

The strengthened rooted-Q inequality leaves margin

> `3t^2+8t-4-2ceil((t+1)/2)>0` for every `t>=2`.

So the new hub theorem materially tightens the branch but **does not close the unbounded r=1 parameter family by scalar score/rooted-Q aggregation alone**. This is the required stop/pivot diagnosis: another weak scalar inequality is not the next move.

## 11. Strategic conclusion

Residual dimension one is now a sharply constrained physical fan:

- the hub `q_j` is adjacent to all K-heads and their selected W-witnesses;
- `K--W_s` is exactly the selected head-witness matching on the X side because each witness has one X-neighbour;
- `W_s--Y` is empty;
- `W_s--U_bar(d)` is empty;
- `K--H` is empty;
- every hub spoke `z_h q_j` is beta-oriented through a non-neighbour `a_h in K\{h}`;
- the complement of `G[K]` has minimum degree at least one;
- P1/P2 by themselves do not bound k because all obligations use different physical sources at the same coordinate.

The next high-value structural attack is therefore the **beta-witness digraph on K**, `h -> a_h`, together with the singleton equations

`N(z_h) cap N(a_h)={q_j}`.

A useful theorem would price repeated use of one A-witness `a` by many different sources `z_h`, or show that directed cycles in the beta-witness digraph force additional U/A holes beyond `(RH-LX)`. Any such result attacks exactly the surviving physical freedom rather than adding another aggregate relaxation.
