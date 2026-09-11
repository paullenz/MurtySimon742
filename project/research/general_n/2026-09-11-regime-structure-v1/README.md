# Adjacent RX-Hall regime structure: t=1,2,3

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural diagnostics inside the preserved RX-Hall 3-D model, with the first t=3 regime now reduced to a hand certificate. Not a general-N theorem. Independent mathematical review remains open.**

## Current headline

The adjacent exact laboratories require respectively 2, 3 and 4 scalar templates within their fixed-potential architectures:

- `n=30,t=1`: 7 hard profiles, exactly 2 templates;
- `n=29,t=2`: 902 regenerated profiles, exactly 3 templates;
- `n=29,t=3`: 94 regenerated profiles, exactly 4 templates.

A new symbolic milestone has now been reached at `t=3`: the complete `(h_res,J)=(4,14)` **A1 regime** no longer depends logically on the old 236,885-state histogram reduction. Its support and positive template gap are derived by hand from charging, zero slack, scalar cutoff and Hall inequalities; exact enumeration remains only as a falsification/audit layer. See:

- [`N29_T3_A1_COMPLETE_HAND_REDUCTION.md`](N29_T3_A1_COMPLETE_HAND_REDUCTION.md)
- [`N29_T3_A1_COMPLETE_HAND_CHECK.json`](N29_T3_A1_COMPLETE_HAND_CHECK.json)
- [`N29_T3_A1_D1_2_HAND_ELIMINATION.md`](N29_T3_A1_D1_2_HAND_ELIMINATION.md)

The hand route is now

```text
(h_res,J)=(4,14)
 -> charging gives D1 in {0,2,4}
 -> D1=4 impossible by mass
 -> D1=2 impossible by scalar-cutoff + largest-eight Hall
 -> D1=0 forces L=6 and support
      s in {2,3,4}, rho in {1,3,4,5,6}, rho1=9
 -> exact three-slack identity
 -> gap_A1 >= 1.
```

This is the first current `t=3` scalar regime converted from a finite profile certificate into an essentially transparent symbolic proof. The next symbolic targets are the adjacent A530 cells `(h_res,J)=(4,16)` and `(4,18)`.

## Non-circular regime conclusion

The earlier low-dimensional regime work has been subjected to a **non-circular exact validity-mask audit**. The corrected conclusion has two parts that must be kept separate.

### 1. `(h_res,J)` does NOT determine the complete template geometry

Let

```text
J = 2 z_2-D_1,
z_2=#{u:rho_u>=2},
D_1=#{i:s_i=1}.
```

If `M(P)` denotes the complete set of preserved templates having strictly positive exact gap on profile `P`, then `(h_res,J)` does **not** determine `M(P)`. At `t=3` there are eight distinct exact validity masks, and profiles with identical `(h_res,J)` can have different masks.

More strongly:

- profiles 1 and 2 have the **same entire residual sequence** `rho=(1^9,3^3,4^4)` but different exact masks;
- profiles 3 and 5 have the **same entire demand sequence** `s=(2,3^5,4^6)` but different exact masks.

Thus the detailed overlap geometry is genuinely joint in `(s,rho)`. A source-only or demand-only summary cannot reconstruct it.

### 2. `(h_res,J)` DOES give an exact sufficient finite regime partition

A proof does not need to reconstruct every template that happens to work. It only needs one template that works throughout each regime.

The non-circular audit recomputes **every template gap first**, using exact `fractions.Fraction` arithmetic and no chosen assignment labels, and then asks whether each feature cell has a nonempty common-template intersection.

That weaker and mathematically relevant test succeeds:

- `t=1`: `J` alone suffices;
- `t=2`: `J` alone suffices;
- `t=3`: `J` alone fails, but `(h_res,J)` suffices;
- consequently every occupied `(h_res,J)` cell across all three laboratories has at least one template with positive exact gap on **every** profile in the cell.

What is **not** claimed is that `(h_res,J)` is intrinsic, minimal, or determines all certificate overlap.

Exact checker:

```text
adjacent_t123_validity_mask_audit_exact.py
```

Successful non-circular common-template replay:

```text
run id: 34592723477
```

## Exact finite assignment rules

### t=1

On the seven `n=30,t=1` hard profiles:

```text
J in {14,16} -> A
otherwise    -> B
```

There are five occupied `J` cells and every one has a nonempty common-template intersection.

### t=2

On all 902 regenerated `n=29,t=2` profiles:

```text
J=12       -> T0
J odd      -> T1
otherwise  -> T2
```

There are twelve occupied `J` cells and every one has a nonempty common-template intersection.

The complete exact mask census is

```text
T0                 1
T1                20
T2                19
T0+T1             40
T1+T2            129
T0+T1+T2         693
```

so 862/902 profiles admit more than one template. The regime rule chooses one sufficient template; it does not pretend the cover is disjoint.

### t=3

On all 94 regenerated `n=29,t=3` profiles:

```text
h_res=5              -> A38
h_res=4, J=13        -> A0
h_res=4, J=14        -> A1
h_res=4, otherwise   -> A530
```

The seven occupied `(h_res,J)` cells are

```text
(4,13)   1 profile    common {A0}
(4,14)  11 profiles   common {A1}
(4,16)   7 profiles   common {A530}
(4,18)   2 profiles   common {A530}
(5,16)  42 profiles   common {A1,A38}
(5,18)  24 profiles   common {A38}
(5,20)   7 profiles   common {A38}
```

`J` alone is insufficient at `t=3`: the `J=16` and `J=18` cells contain both `h_res=4` and `h_res=5` profiles with no common template across the merged cell.

The complete exact `t=3` mask census is

```text
A0                         1
A1                         1
A38                        3
A530                       2
A1+A38                    18
A1+A530                    1
A1+A38+A530               57
A0+A1+A38+A530            11
```

## Exact template counts remain intact

The audit correction and A1 symbolic compression do not affect the exact minimum template counts:

- `t=1`: two explicit templates suffice, and an exact incompatibility certificate shows one cannot;
- `t=2`: three explicit templates suffice, and profiles `0,3,77` form an exact pairwise-incompatible triangle;
- `t=3`: four explicit templates suffice, and profiles `0,1,38,30` form an exact pairwise-incompatible clique.

Hence the finite sequence

```text
minimum template count: 2, 3, 4 for t=1,2,3
```

is still exact inside the three fixed-potential laboratories. It remains a suggestive `t+1` pattern, **not a theorem for general t**.

## Exact mask collisions: what `(h,J)` does not know

The first `t=3` `(h,J)` mask collision is profiles 1 and 2. Both have

```text
h_res=4, J=14, rho1=9, z2=7, r=34, D1=0,
rho=(1^9,3^3,4^4),
```

but

```text
profile 1: s=(2^2,3^4,4^6), mask={A1}
profile 2: s=(2,3^6,4^5),   mask={A1,A38,A530}.
```

Conversely, profiles 3 and 5 have the same `s=(2,3^5,4^6)` but different `rho` and different masks. These witnesses prove that any attempt to reconstruct the complete validity geometry must retain genuinely joint information.

Exact witness checker:

```text
n29_t3_hJ_collision_exact.py
```

Successful replay:

```text
run id:      34592115266
artifact id: 10196050417
```

## Joint HC3 capacity diagnostic

The natural graph-derived interaction statistic is the pointwise source cap

```text
qcap(rho)=min(a-rho, #{i:s_i<=rho}),
```

which is precisely the cap used by the exact certificate checker and comes from RX1/HC3 compatibility.

An exact `t=3` scan shows:

- `qcap` summaries materially reduce ambiguity;
- `(s histogram, qcap histogram)` leaves only **one** mixed validity-mask cell involving 3 profiles;
- the full state `(s histogram, multiset(rho,qcap(rho)))` determines the exact fixed-template gaps, as it must from the envelope formula;
- but on this 94-profile frontier that full state has 94 occupied cells, so it is a faithful representation rather than a useful compression theorem.

Checker:

```text
n29_t3_joint_capacity_structure_exact.py
```

Successful replay:

```text
run id:      34592346835
artifact id: 10196135538
```

This confirms that joint Hall compatibility is the right language for the **fine** geometry, while `(h_res,J)` remains enough for the **coarse sufficient regime cover**.

## Current next target

The programme now has a sharper division of labour:

1. **A530 symbolic compression:** repeat the A1 strategy for `(h_res,J)=(4,16)` and `(4,18)`, looking first for hand support restrictions and then for a positive slack decomposition of the A530 gap.
2. **Parameterisation:** identify which A1/A530 coefficients and thresholds can be expressed in `(a,b,t,h,J)` rather than the fixed values `(12,16,3,4,J)`.
3. **Fresh-frontier falsification:** once a candidate parameter rule exists, attack it on new exact frontiers (e.g. n=31/n=32) before claiming any infinite-family consequence.
4. **Universal trust boundary:** continue independent red-team of the graph-to-profile/RX-Hall bridge and the 3-D monotone-potential lemma.

The working hypothesis remains deliberately narrow:

> **Finite fact:** in the current `t=1,2,3` laboratories, a low-dimensional `(h_res,J)` partition selects one exact template per regime, while the number of templates is exactly `t+1`.
>
> **General-N question:** can that sufficient regime-wise structure, rather than the full overlap geometry, be proved symbolically and parameterised in `(n,t)`?

No affirmative general-N claim is made yet.
