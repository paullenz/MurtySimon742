# Exact threshold-capacity lemma used by the n=29 bridge

9 September 2026. Candidate mathematics; same-assistant rederivation, not external review.

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

Fix `u in J`. For each heavy selected edge `ui->w`, the supplement `w` is adjacent in `H` to every other heavy selected label at source `u`. There are `ell_u-1>=h` such distinct labels, so `rho_w>=h` or, more generally, the source-demand/supplement count forces `w in Z_h`. Thus every heavy arc from a source in `J` uses an unordered `B`-pair entirely inside `Z_h` and incident with `J`.

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

The difference between the right side of (1) and

```text
h*z_h+C(q,2)
```

is

```text
(q-j)(q-j-1)/2,
```

which is nonnegative for every integer `q-j`. Therefore

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
