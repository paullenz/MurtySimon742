# n=29, t=2 support minimisation — 10 September 2026

Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact finite-model checkpoint inside the candidate RX-Hall / BC framework. It is not an unrestricted Murty–Simon theorem and remains conditional on the universal graph-to-demand / BC compatibility bridge. Independent mathematical review remains open.

## 1. Starting point

The 10 September all-902 compression first established exact common potentials on the three consecutive BC `d` layers `D={1,2,3}` and `D={2,3,4}`, then showed that the three diagonal steps `J0,J1,J2` can be reduced to exactly the useful pair `J0+J2` within either three-layer family. See `N29_T2_THREE_LAYER_EXACT_2026-09-10.md`.

For `D={2,3,4}`, the first exact `J0+J2` certificate had 18 nonzero global generators: 16 rectangles plus the two diagonal thresholds.

## 2. Exact 16-generator descendant

Single-generator ablation showed that deleting `B(3,5)` caused both `B(3,5)` and the tiny `B(3,2)` term to disappear after refitting. Workflow `General RX-Hall n29 t2 c02 234 drop exact`, run **34457523167**, then exactified and independently replayed this descendant over all 902 profiles.

The exact 16-generator support is

```text
D=2: V={11,12,13,14}
D=3: V={0,4,7,8,10,12}
D=4: V={2,3,6,9}
diagonal: K={14,16}  <=>  c={2,0}
```

The accepted exact point has denominator scale `10^6`, homogeneous-row maximum LHS `0`, zero row/bound violations, and worst profile margin numerator `-1,999,907` against the required `-1,000,000`. The separate standard-library replay passes all 902 profiles.

Artifact `10144214581`; archive digest `sha256:3e89b8381a685e3c354633215aabc7743a77cdb559f68616754528010e17dbc9`.
Exact JSON SHA256 `3e5113e26a9c5600df64f322daf715f76fac6b37b2bc5ec8e24c71761aef2109`.
Replay JSON SHA256 `cf37e0af74e88ddb918edddcb35d9410a962667051a4631208bf881c1cfc9dd5`.

Several exact repeated weights appear in this certificate, notably

```text
B(3,7)=B(3,8)=B(4,9)=1,588,056,
B(2,11)=B(3,10)=2,117,408 = (4/3)*1,588,056.
```

These repetitions motivated a separate small-integer probe; they are suggestive structure, not by themselves a theorem.

## 3. From 16 to 14 generators

A complete single-rectangle deletion scan of the exact-16 support found only four deletions that could be refitted at all:

```text
B(2,12), B(3,12), B(4,2), B(4,3).
```

The other ten rectangle deletions were infeasible in the same common-potential model.

The best descendant came from deleting `B(3,12)`: the refitted solution simultaneously set `B(4,2)=0`, leaving **12 rectangles + J2 + J0 = 14 global generators**.

The support is

```text
D=2: V={11,12,13,14}
D=3: V={0,4,7,8,10}
D=4: V={3,6,9}
diagonal: K={14,16}  <=>  c={2,0}
```

Equivalently, in the original `h=b-v` threshold coordinate with `b=16`,

```text
D=2: h <= {5,4,3,2}
D=3: h <= {16,12,9,8,6}
D=4: h <= {13,10,7}
plus h-d <= 2 and h-d <= 0.
```

The `D`-layers are exactly `{t,t+1,t+2}` and the diagonal slacks are `{0,t}` for this `t=2` frontier. That is a promising parameter-level pattern; the remaining `V/h` breakpoints are not yet explained parametrically.

## 4. Exact support-14 replay

Workflow `General RX-Hall n29 t2 c02 support14 exact`, run **34458406442**, exactified this 14-generator support and then replayed it with the generic standard-library checker that imports neither SciPy/NumPy nor the LP builder/exactifier.

Results:

```text
profiles:                         902
finite inequalities:             334,159
variables:                        20,551
global nonzero generators:       14
scale:                            1,000,000
boost:                            2
homogeneous-row max LHS:          0
worst margin numerator:           -1,999,876
required margin numerator:        -1,000,000
row violations:                   0
bound violations:                 0
independent replay:               PASS
variable-order hash:              PASS
```

Artifact `10144542448`; archive digest `sha256:2575898ec2748465122546efb86dfd65725f9c62255c5cc0dd421da0d5f4b26e`.
Exact JSON SHA256 `851492ce86578198774c9f26f01d1102dc9035ad01ef114b640339b637baf45d`.
Replay JSON SHA256 `b80a60474df1e47e7c391a24c2d771486a971859f244e6b04f2515e44fc4521a`.

The 14 exact global generator numerators are

```text
B(2,11)   6,569,730
B(2,12)   7,443,376
B(2,13)  17,353,143
B(2,14)   4,858,018

B(3,0)   27,264,267
B(3,4)    4,985,326
B(3,7)    4,927,298
B(3,8)    4,927,298
B(3,10)   6,569,730

B(4,3)    3,172,445
B(4,6)    3,557,316
B(4,9)    4,927,298

J2         9,135,500
J0         8,642,565
```

Again there are exact repetitions:

```text
B(3,7)=B(3,8)=B(4,9),
B(2,11)=B(3,10) approximately (4/3) times that common unit
```

(the last relation differs by only rounding at the accepted integer scale; no exact rational identity is claimed for the support-14 point).

## 5. Deletion-minimality inside this language

Workflow `General RX-Hall n29 t2 c02 support14 drop`, run **34458457734**, removed each of the 12 rectangles one at a time while keeping all other support-14 generators available and refitting every profile-specific envelope coefficient.

Every one of the 12 deletion models is infeasible:

```text
D=2: V=11,12,13,14       all indispensable under single deletion
D=3: V=0,4,7,8,10        all indispensable under single deletion
D=4: V=3,6,9              all indispensable under single deletion
```

The two diagonal steps are also indispensable at the broader architecture level: `J0` alone was already known to fail all 902 even with the unrestricted rectangle dictionary, while `J1+J2` fails with that unrestricted dictionary, hence `J2` alone cannot suffice either.

Therefore the 14-generator support is **deletion-minimal in the current rectangle + diagonal-step language**. This is deliberately weaker than claiming global support-cardinality optimality: a different 13-generator support using substitute rectangle locations has not been ruled out.

## 6. Small-integer diagnostic

For the earlier exact-16 support, componentwise-rounded fixed-integer global potentials were tested after normalising by the repeated unit `1,588,056`.

Multipliers `1,2,3,4,6` are infeasible. Multipliers `8` and `12` are feasible numerically. In particular, multiplier 8 gives the compact integer global weights

```text
D=2:  (V11,V12,V13,V14) = (11,12,28,8)
D=3:  (V0,V4,V7,V8,V10,V12) = (41,8,8,8,11,5)
D=4:  (V2,V3,V6,V9) = (5,5,6,8)
J2=15, J0=14.
```

This is useful evidence that the common potential need not intrinsically use large or delicate decimal weights. These fixed-integer probes are still floating feasibility diagnostics until their profile-specific coefficients are exactified/replayed, and the support-14 route remains preferable because it uses fewer generators.

## 7. Next mathematical target

The computational pruning phase has now produced a stable object suitable for symbolic work:

```text
12 rectangle Hall steps on D={t,t+1,t+2}
+ 2 cumulative slack steps c={0,t}
= 14 deletion-minimal generators at n=29,t=2.
```

Next priority:

1. rewrite the 12 rectangle generators as three monotone one-dimensional step functions in the `h` coordinate;
2. combine them with the exact `DST_0` and `DST_t` inequalities;
3. derive closed upper/lower envelopes for the resulting label/source potential using the demand, source/supplement transport and selected-incidence identities;
4. search for a parameter explanation of the remaining `h` breakpoints rather than fitting another numerical support;
5. use `n=30` and then `n=31` only as falsification laboratories once a symbolic rule is proposed.
