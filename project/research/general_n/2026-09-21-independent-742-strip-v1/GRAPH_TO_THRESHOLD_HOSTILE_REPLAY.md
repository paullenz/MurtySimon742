# Hostile replay of the shared graph-to-threshold spine

21 September 2026.

**Verdict:** no blocking flaw found in an independent line-by-line
rederivation of the load-bearing Sections 1--3 of the canonical profile proof.
This is same-project internal replay, not external verification.

## 1. Complement/quasi-edge construction

In the complement `H`, an adjacent total-dominating pair is exactly a
nonedge of `G` with no common G-neighbour.  Since `G` has diameter two, `H`
contains none.  Deleting a critical G-edge is insertion of a missing H-edge
and must create one.

For a missing pair `uw` inside `H[B]`, the new dominating pair must use one of
`u,w`; otherwise neither adjacency nor neighbourhood union changed.  It cannot
be `{u,w}` because both miss the minimum-degree root `v`.  Hence it is a
pre-existing cross-edge, say `ui`, with `i in A`, and its unique previously
undominated vertex is `w`.  Thus `ui->w` is recoverable from its source and
exception.  Distinct missing B-pairs cannot select the same cross-edge.

## 2. Exact ledger

Selected cross-edges plus existing `H[B]` edges account for every unordered
B-pair exactly once.  With all other cross-edges residual,

```text
e(F)=r+t,
sum d_i=2(r+t),
sum R_i=r.
```

For `i in A`,

```text
deg_H(i)=a-d_i+R_i+x_i >= delta(H)=a,
```

so `x_i>=d_i-R_i`, hence `x_i>=s_i`.  Also

```text
S=sum max(0,d_i-R_i) >= sum(d_i-R_i)=r+2t.
```

No residual-activity assumption is used here.

## 3. Source-demand injection

Fix `ui->w`.  Every `j in N_F(i)` is missed by `i`, so `u` must neighbour
`j` in H.  If `uj` is residual, charge it to the source residual degree.  If
it is selected with supplement `w_j`, then `w_j` differs across selected
labels and differs from `w`.  The original quasi-edge `ui` must dominate
`w_j`, while `u` misses `w_j`, hence `iw_j` is an H-edge.  Both `i` and
`w_j` miss `j`, so `iw_j` cannot itself be selected (a selected cross-edge's
unique exception is in B); it is residual at label `i`.

This injects every uncharged F-neighbour into a distinct residual edge at
`i`, proving

```text
d_i<=rho_u+R_i,
s_i<=rho_u
```

for every selected incidence.

## 4. The delicate supplement step in threshold capacity

An apparent gap must be handled explicitly.  If source `u` has many selected
heavy labels, the supplement `w` of one selection neighbours every other
selected heavy label.  Those `w`--label edges need not all be residual.

Nevertheless `w` is heavy-residual:

- if at least `h` of those edges are residual, then `rho_w>=h` directly;
- if one is selected at a heavy label `j`, the already-proved source-demand
  inequality gives `rho_w>=s_j>=h`.

Thus every supplement of a source with more than `h` heavy selections belongs
to `Z_h`.  This two-case argument is essential; silently calling all such
edges residual would be false.

The source itself also lies in `Z_h` because it selects a heavy label.  The
selected source--supplement pairs are distinct unordered pairs in `Z_h`.
For `j` high-load sources their number is at most

```text
j(z_h-j)+binom(j,2).
```

All other `z_h-j` sources have at most `h` heavy selections.  Therefore

```text
W_h <= (z_h-j)h+jz_h-j(j+1)/2
    <= hz_h+binom(z_h-h,2),
```

because the exact gap is

```text
binom((z_h-h)-j,2),
```

nonnegative for every integer argument.  This is equivalent to

```text
2W_h<=z_h^2-z_h+h(h+1).
```

## 5. Profile projection

A maximum-demand label needs `H0` distinct selected sources, so
`z_h>=H0>=h`; nested residual tails give `sum_h z_h<=r`.  For
`p=|I_h|/a`, Cauchy and threshold capacity yield

```text
[(1/a) sum sqrt(2as_i-h^2)]^2
 <= p z_h^2+p(1-p)h^2
 <= z_h^2.
```

The last gap is `(1-p)(z_h^2-p h^2)>=0`.  Summing over thresholds recovers
the canonical profile integral.  The indispensable hypothesis `z_h>=h` is
present and is not inferred from the quadratic capacity alone.

## 6. Trust conclusion

The replay found no flaw in the shared graph-to-demand, threshold-capacity or
Cauchy projection.  The most fragile point is the supplement step in Section
4; it is valid only by the residual-or-selected dichotomy plus the already
proved source-demand inequality.

This raises internal confidence in both the old `7/12` candidate and the new
threshold ladder, but does not change either to externally verified status.
The remaining forward obstruction is graph realizability of the plateau, now
compressed by selected-signature/codegree rigidity.

