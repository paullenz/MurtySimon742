# Exact threshold-capacity lemma used by the n=29 bridge

9 September 2026. Candidate mathematics; same-assistant rederivation, not external review.

**11 September 2026 audit correction.** A fresh cross-order red-team found that an intermediate sentence in the earlier text had the algebraic difference in the final comparison written in the wrong order. The correct identity is that `h*z_h+C(z_h-h,2)` minus the right side of (1) equals `(q-j)(q-j-1)/2 >= 0`. This is exactly the direction needed to deduce (2), so the final threshold-capacity inequality and every downstream numerical test remain unchanged. The supplement step immediately below has also been expanded to expose its two cases explicitly.

This file expands the threshold step that was too compressed in the first standalone bridge draft.

Let

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|.
```

For each label `i in I_h`, choose `s_i` actual selected incidences. By the source-demand inequality, every chosen source has `rho_u>=s_i>=h`, so every chosen incidence has source in `Z_h`.

Call a selected incidence **heavy** when its label lies in `I_h`. Let `ell_u` be the number of actual heavy selections with source `u`. Then

```text
W_h <= sum_{u in Z_h} ell_u,
```

because the chosen demand incidences are a subset of all actual heavy selections.

A source outside `Z_h` has `rho_u<=h-1`, and the source-demand inequality implies it cannot select a heavy label as one of the incidences used to satisfy that label's demand.

Now let

```text
J={u in Z_h: ell_u>h},
j=|J|.
```

Fix `u in J` and a heavy selected edge `ui->w`. For every other heavy selected label `j` at source `u`, the pair `{u,j}` must dominate `w`; since `uw` is missing, this forces the cross-edge `jw` in `H`. There are `ell_u-1>=h` such distinct labels `j`.

We claim that the supplement `w` lies in `Z_h`. There are two cases. If none of those `ell_u-1` forced edges `jw` is selected from source `w`, then all of them are residual and therefore `rho_w>=ell_u-1>=h`. If at least one forced edge `jw` is selected, then its label `j` is heavy, so `s_j>=h`; applying the source-demand implication `s_j<=rho_w` to that selected incidence gives `rho_w>=h`. Thus in every case `w in Z_h`.

Consequently every heavy arc from a source in `J` uses an unordered `B`-pair entirely inside `Z_h` and incident with `J`.

Selected orientations are injective on unordered `B`-pairs. Therefore the total number of heavy arcs contributed by sources in `J` is at most the number of unordered pairs of `Z_h` incident with `J`:

```text
j(z_h-j)+C(j,2)=j*z_h-j(j+1)/2.
```

Each source in `Z_h\J` contributes at most `h` heavy selections by definition of `J`. Hence

```text
W_h
 <= (z_h-j)h + j*z_h - j(j+1)/2.          (1)
```

If `W_h>0`, then some label has demand at least `h`, so it requires at least `h` distinct sources in `Z_h`; therefore `z_h>=h`.

Put

```text
q=z_h-h.
```

The difference between

```text
h*z_h+C(q,2)
```

and the right side of (1) is

```text
(q-j)(q-j-1)/2,
```

which is nonnegative for every integer `q-j`. Hence the right side of (1) is at most `h*z_h+C(z_h-h,2)`, and therefore

```text
W_h <= h*z_h + C(z_h-h,2).
```

Multiplying by two and simplifying gives

```text
2W_h <= z_h^2-z_h+h(h+1).                 (2)
```

This is the exact threshold-capacity inequality used in `minimal_prepare.py`.

Two further consequences used by the finite screen are immediate:

1. If `H0=max_i s_i>0`, then a label of demand `H0` needs `H0` distinct sources with residual degree at least `H0`, hence `z_H0>=H0`.
2. If residual activity gives every source baseline degree at least one and `r<=rmax`, then for `h>=2`

```text
r >= b+z_h(h-1),
```

so

```text
z_h <= floor((rmax-b)/(h-1)).
```

The lemma is a necessary capacity bound only; no sufficiency is claimed.
