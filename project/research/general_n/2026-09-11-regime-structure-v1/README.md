# adjacent RX-Hall regime structure: t=1,2,3

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural diagnostics inside the already-preserved RX-Hall 3-D model. Not a general-N theorem. Independent mathematical review remains open.**

## Current headline

The adjacent exact laboratories require respectively 2, 3 and 4 scalar templates:

- `n=30,t=1`: 7 hard profiles, 2 exact templates;
- `n=29,t=2`: 902 regenerated profiles, 3 exact templates;
- `n=29,t=3`: 94 regenerated profiles, 4 exact templates.

The first attempted cross-laboratory compression by

```text
(h_res,L)
```

has now been exactly **falsified in all three laboratories**. Here `h_res` is the ordinary h-index of the residual degrees and `L` is the scalar supplement-cap cutoff from `SUPPLEMENT_CAP_THRESHOLD_LEMMA.md`.

A smaller replacement works on all three finite laboratories:

```text
(h_res,J),
J = 2 z_2 - D_1,
z_2 = #{u:rho_u>=2},
D_1 = #{i:s_i=1}.
```

Since all three current laboratories have `b=16` residual sources, this is equivalent to

```text
(h_res,G),
G = 2 rho_1 + nu_1,
rho_1=#{u:rho_u=1},
nu_1=#{i:s_i=1},
G=2b-J.
```

Every occupied `(h_res,G)` cell has one canonical valid exact-template assignment at `t=1,2,3`.

This is a finite assignment-compression result, **not** a theorem that `(h_res,J)` determines the complete overlap/coverage mask of all templates. Exact red-team checks show substantial template overlap within many `(h_res,G)` cells.

Full note:

```text
N29_T23_HL_COMPRESSION_FALSIFICATION.md
```

Replay:

```text
n29_t23_hL_compression_scan.py
```

Successful CI:

```text
run id:      34590110191
artifact id: 10195264884
artifact:    adjacent-t123-hL-compression
SHA-256:     7e2a50a7ec23e00e8479fe4dba7fbeb0e8422ffd6fc436960af06335b844e7a1
```

## t=2 unit-demand regime result

Let

```text
nu1(s) = #{ i : s_i = 1 }.
```

For the complete regenerated `n=29,Delta=16,t=2` RX-Hall frontier of 902 profiles, the three exact rational scalar templates admit the exact deterministic assignment

```text
nu1 = 0  -> T2   825 profiles
nu1 = 1  -> T1    76 profiles
nu1 = 2  -> T0     1 profile
```

No other value of `nu1` occurs on this frontier. Every assigned template has strictly positive exact `fractions.Fraction` certificate gap.

The exact incompatibility triangle proving that two scalar templates do not suffice consists of profiles `0`, `3`, and `77`:

| profile | demand id | `nu1` | unique-template role |
|---:|---:|---:|---|
| 0 | 45 | 2 | T0-only |
| 3 | 70 | 1 | T1-only |
| 77 | 154 | 0 | T2-only |

All three nevertheless share

```text
(h_res,L)=(4,6),
```

which is the cleanest falsification of the original two-index idea.

## t=2 exact overlap census

Writing a template-coverage mask in `(T0,T1,T2)` order:

```text
001   19
010   20
011  129
100    1
110   40
111  693
```

There are 40 profiles covered by exactly one template, 169 by exactly two, and 693 by all three. The deterministic regime assignment deliberately chooses one valid template even where others also work.

## Supplement-cap scalar cutoff

For an arbitrary demand count `a`, let

```text
C_u = min(a-rho_u, #{i:s_i<=rho_u}),
Z_u = rho_u+C_u,
L   = max{k>=1 : #{u:Z_u>=k-1}>=k+1}.
```

The monotone supplement-cap refinement has the exact closed form

```text
q*_u=min(C_u,L).
```

Thus the original vector fixed-point operation is carried by one integer cutoff. This structural lemma is independent of the `n=29` numerical certificate and is why the same `L` is legitimate in the `n=30,t=1` comparison after substituting its own value of `a`.

## Adjacent exact finite assignment rules

The new two-scalar view gives the following exact finite rules.

### t=1

On the seven `n=30,t=1` hard profiles, `G` alone separates the preserved assignment:

```text
G in {16,18} -> A
G in {13,15,17} -> B
```

### t=2

On all 902 profiles:

```text
G=20    -> T0
G odd   -> T1
otherwise -> T2
```

### t=3

On all 94 profiles:

```text
h_res=5              -> A38
h_res=4 and G<=16    -> A530
h_res=4 and G=18     -> A1
h_res=4 and G=19     -> A0
```

At `t=3`, `G` alone is not enough: `G=14,16` occur in both `A38` and `A530`, and the ordinary residual h-index supplies the missing distinction.

Chronologically `G=2rho_1+nu_1` was found from the `t=2,3` collision analysis before the `n=30,t=1` laboratory was inspected, so the `t=1` success is a genuine finite holdout check.

## Important boundary of the compression

The key `(h_res,J)` determines the **canonical valid-template assignment**, not the complete set of templates that happen to work on a profile.

Exact coverage-mask red-team counts within `(h_res,G)` cells are:

```text
t=1: 1 mixed coverage-mask cell, 3/7 profiles involved
t=2: 13 mixed coverage-mask cells, 879/902 profiles involved
t=3: 6 mixed coverage-mask cells, 93/94 profiles involved
```

So the next proof target should be “one fixed template works throughout each parameterized regime”, not “the two scalars reconstruct the entire certificate geometry”.

## Reproducibility

Original t=2 regime diagnostic:

```text
n29_t2_regime_structure_scan.py
.github/workflows/general-rx-hall-n29-t2-regime-structure.yml
```

Supplement cutoff replay:

```text
n29_t2_supplement_threshold_replay.py
SUPPLEMENT_CAP_THRESHOLD_LEMMA.md
```

Adjacent t=1,2,3 compression replay:

```text
n29_t23_hL_compression_scan.py
.github/workflows/general-rx-hall-n29-t23-hL-compression.yml
```

## Current next target

Feature hunting should stop here unless the present structure fails a fresh-domain test. The priority is now:

1. treat `J=2z_2-D_1` as the natural low-threshold ledger statistic rather than the raw encoding `G`;
2. derive regime-wise inequalities from `(h_res,J)` and the cumulative source/demand tails;
3. determine whether the coefficient 2 has a combinatorial origin in residual activity/Hall supply;
4. hostile-test the same pair on a genuinely fresh exact frontier not used in discovery;
5. if it survives, seek a parameterized statement that one fixed rational template works on each regime;
6. keep the graph-to-profile/RX-Hall bridge and 3-D potential lemma as the principal independent-review trust boundary.
