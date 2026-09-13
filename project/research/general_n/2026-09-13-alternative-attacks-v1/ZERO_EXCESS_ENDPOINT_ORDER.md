# Zero-excess endpoint order-statistic lemma

13 September 2026. **Candidate general lemma inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note extracts the source-availability mechanism used in the state-519 continuation into a selection-free statement about scalar margins. It strengthens the trivial `C_i>=x_i` treatment of zero-excess labels.

**Correction preserved 13 September 2026.** An earlier wording said that the second-smallest eligible endpoint load `L_(2)` was universally at least 2. That is false: two eligible sources with `(q,p)=(1,0)` would give `L_(2)=1`. The state-519 verifier never relied on that statement and was conservative there. The correct combined lower bound for a zero-excess demand-two label is `C_i>=max(2,L_(2))`, as recorded below.

## Setup

Use the canonical bridge notation. For a positive-demand label `i`, write

```text
e_i=x_i-s_i>=0,
C_i=R_i+x_i=d_i+e_i.
```

At every selected incidence `ui`, the selected-excess lemma gives

```text
p_u-rho_u+1 <= e_i,                                  (1)
```

and endpoint load gives

```text
q_u+p_u <= C_i.                                       (2)
```

Selected-edge forcing also gives

```text
s_i<=rho_u.                                           (3)
```

Independently, by definition,

```text
C_i=R_i+x_i>=x_i.                                     (4)
```

## 1. Exact-demand source availability

Suppose label `i` has demand `d=s_i` and zero excess:

```text
e_i=0,
x_i=d.
```

Then every one of its `d` distinct selected sources satisfies, by (1) and (3),

```text
rho_u>=d,
p_u<=rho_u-1,
q_u>0.                                                (5)
```

Define the exact-demand eligible source set

```text
A_d={u in B : rho_u>=d, q_u>0, p_u<=rho_u-1}.         (6)
```

If a zero-excess demand-`d` label exists, necessarily

```text
|A_d|>=d.                                             (7)
```

Thus (7) is already a useful selection-free availability condition.

## 2. Endpoint-load order statistic

For `u in A_d`, put

```text
L_u=q_u+p_u.
```

Order these values increasingly:

```text
L_(1) <= L_(2) <= ... .                               (8)
```

The label selects `d` distinct sources from `A_d`. By (2), `C_i` is at least the largest endpoint load among those selected sources. The smallest possible value of that maximum over all `d`-subsets is the `d`-th order statistic. Therefore every zero-excess demand-`d` label satisfies

```text
C_i >= L_(d).                                         (9)
```

Combining this with the independent bound (4), and using `x_i=d`, gives the sharpened form

```text
C_i >= max(d,L_(d)).                                  (10)
```

If `|A_d|<d`, the label is impossible instead.

This uses no fixed selected geometry: it is a necessary consequence of the scalar source margins `(rho,q,p)`.

## 3. Baseline-three consequence for demand two

The refined baseline-three identity is

```text
sum_i x_i C_i
 =3(r+Q)+sum_i(x_i-3)C_i.                             (11)
```

For a zero-excess demand-two label,

```text
s_i=2, e_i=0, x_i=2,
```

so its correction is exactly

```text
-C_i.
```

Let

```text
z_0=#{i:s_i=2,e_i=0}
```

and, when `z_0>0`, define

```text
mu_2=max(2,L_(2)).                                    (12)
```

Equation (7) guarantees that `L_(2)` exists. Every zero-excess demand-two label then obeys

```text
C_i>=mu_2.
```

Hence the universal `-2 z_0` correction can be strengthened to

```text
-z_0 mu_2.                                            (13)
```

In particular, if `P_+` is any valid upper bound on all positive baseline-three corrections, then

```text
T + z_0 mu_2 - P_+ <= 3(r+Q)                         (14)
```

is necessary, where

```text
T=sum_u q_u(q_u+p_u).
```

The state-382 refinement used only the independent universal fact `C_i>=2` for a zero-excess demand-two label, giving `2z_0`. Equation (14) additionally retains the eligible-source endpoint order statistic when it is larger.

## 4. State 519 interpretation

State 519 has

```text
s=2,3^14,
rho=1^6,3^12.
```

In each of the three coarse exceptional low-excess profiles found at `E=6,8,9`, the unique demand-two label has `e=0`. Thus it needs two distinct `rho=3` selected sources with

```text
p_u<=2.
```

For any fixed q-vector and incoming allocation, `L_(2)` is the second-smallest `q_u+p_u` among active `rho=3` sources with `p_u<=2`, and `mu_2=max(2,L_(2))`.

The dedicated state-519 replay enumerates a pair of eligible sources and minimizes the incoming `sum q_u p_u` conditional on that pair. Its implementation uses the pair endpoint maximum directly without additionally replacing values below 2 by 2; that is a **weaker** relaxation than (14), so its positive gaps remain valid. In particular, the state-519 closure does not depend on the corrected normalization in (12).

## 5. Generalisation potential

The same lemma applies whenever exact-demand labels occur:

- (7) gives a low-p source-count condition for any demand `d`;
- (10) gives an endpoint lower bound by a source-load order statistic plus the trivial `C_i>=d` bound;
- for baseline three, demand-two zero-excess labels gain directly through the negative coefficient;
- with multiple zero-excess demand-two labels, every one individually satisfies `C_i>=mu_2`, so the safe aggregate contribution is `-z_0 mu_2` even if different labels reuse the same eligible sources.

A stronger relaxation can optimize `mu_2` jointly with the incoming ledger across the full adjacent low-demand family. Competition between labels for source slots may strengthen this further, but is not needed for (14).

## Trust boundary

This lemma depends only on canonical selected-edge forcing, selected-excess, endpoint load and the trivial `C_i>=x_i` identity. It does not assume graph-level switching and does not fix the identities of selected quasi-edge representatives. External checking of the canonical bridge and this derivation remains open.
