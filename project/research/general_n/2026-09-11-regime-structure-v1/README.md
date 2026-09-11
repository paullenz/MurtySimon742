# Adjacent RX-Hall regime structure: t=1,2,3

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: exact finite structural diagnostics inside the preserved RX-Hall 3-D model. Not a general-N theorem. Independent mathematical review remains open.**

## Current headline — corrected after non-circular audit

The adjacent exact laboratories still require respectively 2, 3 and 4 scalar templates within their fixed-potential architectures:

- `n=30,t=1`: 7 hard profiles, exactly 2 templates;
- `n=29,t=2`: 902 regenerated profiles, exactly 3 templates;
- `n=29,t=3`: 94 regenerated profiles, exactly 4 templates.

Those exact template-count statements remain intact.

However, the attempted low-dimensional explanation by `(h_res,J)` has **not** survived a stronger audit.

Earlier exploratory scripts compressed a *chosen valid-template assignment* using

```text
J = 2 z_2-D_1,
z_2=#{u:rho_u>=2},
D_1=#{i:s_i=1}.
```

The `t=2` assignment labels were themselves defined from `D1`, and the `t=3` assignment labels were themselves defined from the previously found count tree containing the `rho1<=8` split. Re-classifying those labels with the same statistics is therefore not independent structural evidence.

This circularity is recorded explicitly in

```text
ASSIGNMENT_CLASSIFIER_AUDIT_CORRECTION.md
```

The correct independent target is the **complete exact validity mask**

```text
M(P)={T : exact_gap_T(P)>0}
```

under every preserved template. On `n=29,t=3`, all four gaps have now been recomputed with exact `fractions.Fraction` arithmetic for all 94 regenerated profiles before any feature classification is attempted.

## Exact t=3 validity-mask result

There are **8 distinct exact validity masks** among the 94 profiles:

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

The following candidate keys all fail to determine this mask:

```text
h_res
D1
rho1
J
(h_res,J)
(h_res,D1)
(h_res,D1,rho1)
(h_res,D1,D5,rho1)
(h_res,D1,D5,1[2z2>=b])
```

No tested integer threshold `rho1<=k` appended to `(h_res,D1,D5)` makes the mask pure. No subset of the tested primitive family `(h_res,D1,D5,rho1)` is sufficient.

Thus the previous special emphasis on coefficient `2` in `J` and on the half-source threshold `z2=b/2` is withdrawn as structural evidence. They remain useful encodings of one successful finite assignment rule only.

Exact checker:

```text
n29_t3_template_mask_structure_exact.py
```

Successful CI:

```text
run id:      34591935362
artifact id: 10195981323
artifact:    adjacent-t123-regime-key-redteam
```

## Smallest exact (h,J) collision

The first validity-mask collision already occurs at profiles 1 and 2. They have the same

```text
h_res = 4
J     = 14
rho1  = 9
z2    = 7
r     = 34
D1    = 0
D5    = 0
S     = 40
```

and the same full residual sequence

```text
rho = (1^9,3^3,4^4).
```

But their demand profiles differ:

```text
profile 1: s = (2^2,3^4,4^6)
profile 2: s = (2^1,3^6,4^5)
```

and their exact template-validity masks are

```text
profile 1: {A1}
profile 2: {A1,A38,A530}.
```

The exact gaps are:

```text
profile 1:
  A0   = -3049/81
  A1   = 1
  A38  = -2547/154
  A530 = -21493/1440

profile 2:
  A0   = -1598/81
  A1   = 159/5
  A38  = 4229/385
  A530 = 3151/288
```

So even the **entire residual sequence** does not determine the regime geometry.

## The converse collision: the demand side alone also fails

Profiles 3 and 5 have the identical full demand sequence

```text
s=(2,3^5,4^6),
```

but different residual profiles and different masks:

```text
profile 3 rho = (1^9,3^3,4^3,5)
mask = {A1,A38,A530}

profile 5 rho = (1^8,2,3^3,4^4)
mask = {A530}.
```

Therefore neither the full source marginal `rho` nor the full demand marginal `s` determines the exact template-validity mask.

This is the main structural conclusion of the audit:

> **The finite t=3 certificate geometry is genuinely joint in `(s,rho)`; a one-sided scalar or marginal classifier is insufficient.**

Exact collision checker:

```text
n29_t3_hJ_collision_exact.py
```

Successful CI:

```text
run id:      34592115266
artifact id: 10196050417
artifact:    adjacent-t123-regime-key-redteam
```

## What remains valid from the earlier assignment work

The old deterministic count trees are still correct *sufficient assignment rules*: every profile assigned by those trees receives a template with strictly positive exact gap. They remain useful compact replays of the finite cover.

What they do **not** establish is that their branch statistics are intrinsic, minimal, or likely to parameterize a universal theorem.

Likewise, the exact template-count minima remain separately established:

- `t=1`: two templates suffice, and an exact incompatibility certificate shows one cannot;
- `t=2`: three templates suffice, and profiles `0,3,77` form an exact pairwise-incompatible triangle;
- `t=3`: four templates suffice, and profiles `0,1,38,30` form an exact pairwise-incompatible clique.

The suggestive numerical sequence `2,3,4` therefore remains an observation about minimum template counts in three finite fixed-potential laboratories. It is **not currently backed by a valid low-dimensional `t+1` regime classifier**.

## Relation to the original (h,L) falsification

The original `(h_res,L)` compression is still exactly falsified. The later `(h_res,J)` assignment compression remains a compact way to encode chosen valid assignments, but the independent mask audit shows it does not capture the underlying overlap geometry.

Historical files are retained for reproducibility:

```text
N29_T23_HL_COMPRESSION_FALSIFICATION.md
n29_t23_hL_compression_scan.py
adjacent_t123_regime_key_redteam.py
```

The last of these should be read only as an assignment-rule compression/replay; see `ASSIGNMENT_CLASSIFIER_AUDIT_CORRECTION.md`.

## Current next target

The priority is now different from the pre-audit plan:

1. **Stop searching for source-only scalar classifiers.** The exact same-`rho` collision falsifies that route.
2. **Stop searching for demand-only classifiers.** The exact same-`s` collision falsifies that route.
3. Mine genuinely **joint** statistics of `(s,rho)` suggested by the RX1/Hall compatibility relation `s<=rho`, for example cumulative compatibility counts or Ferrers/majorization deficits.
4. Test whether a very small family of joint threshold statistics determines the exact validity masks, beginning with the explicit collisions above rather than with the easy bulk profiles.
5. Independently red-team the graph-to-profile/RX-Hall bridge and the 3-D monotone potential lemma; these remain the universal mathematical trust boundary.
6. Only if a joint statistic survives fresh finite laboratories should it be promoted into a parameterized regime lemma.

The natural next experiment is therefore to compare profiles by the joint threshold matrix

```text
C_{k,l}=#{(u,i): rho_u>=k and s_i<=l}
```

or, more economically, the Ferrers compatibility profile induced by `s_i<=rho_u`, and determine the smallest joint summary that separates the exact collision witnesses while retaining symbolic meaning.