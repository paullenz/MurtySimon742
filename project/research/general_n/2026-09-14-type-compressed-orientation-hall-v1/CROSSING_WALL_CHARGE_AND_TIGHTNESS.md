# Crossing-wall charge, double tightness, and selected-demand desert

14 September 2026. **Candidate exact structural package inside the canonical target-Hall framework. External mathematical review and novelty assessment remain OPEN.**

This note sharpens the Murty-specific attack on the q-stratified crossing statistic

```text
C_q(M+)=sum_{q,m} min(H^S_{q,m},L^O_{q,m}).
```

It records four consequences of a positive crossing:

1. every crossing unit charges injectively to both selected slack and exterior over-saturation;
2. the selected endpoint is deletion-neutral and the exterior endpoint has an exactly tight positive-slack neighborhood;
3. equality of the pre-diagonal incoming count creates an exact selected-demand desert between the crossing endpoints;
4. in the live post-pair cap, every crossing is witnessed by a residual-cap, selected-excess-cap, or potential-degree-cap threshold crossing.

The results do **not** prove `C_q=0`. The preserved positive-crossing counterexample remains valid and is used below as a hostile check.

## 1. Setup

Let `M+` be the union of all labelled minimum Hall witnesses, hence the unique maximal labelled minimizer. For every target `w` write

```text
q_w,
c_w=q_w+rho_w,
P_w,
y_w=d^+_{M+}(w),

s_w=(P_w-y_w)_+,
z_w=(y_w-P_w)_+.
```

Thus `s_w` is positive receiver slack and `z_w` is receiver over-saturation.

Before diagonal deletion put

```text
m_w=#{u in M+ : q_u<=c_w+1 and q_w<=c_u}.
```

For a block

```text
B_{q,m}={w:q_w=q,m_w=m},
```

recall

```text
H^S_{q,m}=#{w in B_{q,m}: w in M+, P_w>=m},
L^O_{q,m}=#{w in B_{q,m}: w notin M+, P_w<=m-1},
c_{q,m}=min(H^S_{q,m},L^O_{q,m}).
```

Then

```text
C_q(M+)=sum_{q,m} c_{q,m}.
```

## 2. Elementary two-sided charge

Inside one crossing block, every selected high endpoint `y` has

```text
y_y=m-1,
P_y>=m,
```

and therefore

```text
s_y=P_y-y_y>=1.                                      (1)
```

Every unselected low endpoint `x` has

```text
y_x=m,
P_x<=m-1,
```

and therefore

```text
z_x=y_x-P_x>=1.                                      (2)
```

Choose `c_{q,m}` distinct selected high endpoints and `c_{q,m}` distinct unselected low endpoints in each block. Different `(q,m)` blocks are disjoint, so these choices are globally disjoint.

Hence:

> **Two-sided crossing charge.**
>
> ```text
> C_q(M+)
> <= sum_{w in M+} s_w,                               (3)
>
> C_q(M+)
> <= sum_{w notin M+} z_w.                            (4)
> ```
>
> In particular
>
> ```text
> 2 C_q(M+)
> <= sum_{w in M+} s_w
>    +sum_{w notin M+} z_w.                           (5)
> ```

This is purely combinatorial and does not use swap rigidity.

## 3. Residual-budget weighted charge

In the positive-surplus Murty regime, the coupled residual-slack budget gives, at residual-slack level one,

```text
sum_{w:s_w>=1} max(0,y_w+a-b+1) <= r-b.              (6)
```

For a selected crossing endpoint in block `(q,m)`, `y_w=m-1`, so its contribution to the left side of (6) is

```text
max(0,m+a-b).                                         (7)
```

Using the distinct selected endpoints chosen in Section 2 gives:

> **Weighted crossing charge.**
>
> ```text
> sum_{q,m} c_{q,m} max(0,m+a-b)
> <= r-b.                                              (8)
> ```

Thus crossings above the threshold `m>b-a` spend residual-excess budget immediately. Any surviving positive crossing must either pay this cost or live in the low-`m` region where (8) is weak.

The basic target cap also gives, for every crossing block,

```text
m<=b-1-q,                                             (9)
```

because the selected endpoint has `P_y>=m` and `P_y<=b-1-q`.

## 4. Double-tightness lemma

Fix one crossing pair `x,y` with

```text
q_x=q_y=q,
c_x<c_y,
x notin M+,
y in M+,
m_x=m_y=m,
P_x<m<=P_y.                                           (10)
```

Let

```text
Z={w:y_w<P_w}                                         (11)
```

be the strict positive-slack target set, and let `N^+(u)` denote the directed-compatible target neighborhood of source `u`.

Because `x` lies outside the union of all minimizers, `M+ union {x}` is not a minimum Hall witness. Integrality therefore gives

```text
F(M+ union {x}) >= F(M+)+1.                           (12)
```

Adding `x` increases receiver capacity by exactly one on every target in `N^+(x) cap Z` and increases source demand by `q`. Hence

```text
|N^+(x) cap Z| >= q+1.                                (13)
```

Now delete the selected source `y`. Let

```text
T={w:y_w<=P_w}.                                       (14)
```

A target in `N^+(y)` loses one unit of capped receiver capacity exactly when it lies in `T`. Since `M+` is already minimum,

```text
F(M+\{y})-F(M+)
 =q-|N^+(y) cap T|
 >=0,                                                 (15)
```

so

```text
|N^+(y) cap T|<=q.                                    (16)
```

The crossing gives `y in Z`, and `D(x,y)` holds. For every third target `w`, source-neighborhood containment gives

```text
D(x,w) => D(y,w).                                     (17)
```

Therefore

```text
(N^+(x) cap Z)\{y}
 subseteq N^+(y) cap T.                               (18)
```

Combining (13), (16) and (18) forces equality throughout:

> **Crossing double tightness.**
>
> ```text
> |N^+(x) cap Z|=q+1,                                 (19)
>
> |N^+(y) cap T|=q,                                   (20)
>
> N^+(y) cap T=(N^+(x) cap Z)\{y}.                   (21)
> ```

Consequently

```text
F(M+\{y})=F(M+).                                      (22)
```

So **every selected endpoint of a positive crossing is individually removable while preserving the minimum Hall margin**.

Moreover every target reached by `y` outside the `q` shared targets in (21) is strictly over-saturated:

```text
w in N^+(y)\[(N^+(x) cap Z)\{y}]
 => y_w>=P_w+1.                                       (23)
```

This strictly strengthens the earlier equal-q swap wall. In particular, the target `x` and every target reached by `y` but not by `x` are over-saturated.

### Immediate residual consequence

The `q+1` targets in `N^+(x) cap Z` all have positive slack. One is `y`, with `y_y=m-1`; each of the other `q` targets receives at least the selected incidence from `y`, so has `y_w>=1`. Therefore (6) also implies the per-crossing necessary inequality

```text
max(0,m+a-b)
 + q max(0,a-b+2)
 <= r-b.                                              (24)
```

This is strongest when `b-a` is small; in the current high-Delta frontier the first term is usually the more relevant one.

## 5. Equal-m selected-demand desert

For fixed target demand `q`, the pre-diagonal incoming count is

```text
m(c)
 =#{u in M+ : c_u>=q and q_u<=c+1}.                   (25)
```

For the crossing pair, `m(c_x)=m(c_y)`. Hence no selected source can enter the rectangle opened by increasing the target cross degree from `c_x` to `c_y`.

Because `q_u>=c_x+2>q` in that rectangle, the condition `c_u>=q` is automatic. Therefore:

> **Selected-demand desert.**
>
> ```text
> #{u in M+ : c_x+2<=q_u<=c_y+1}=0.                  (26)
> ```

Equivalently, every source copy with demand in

```text
[c_x+2,c_y+1]                                         (27)
```

is exterior to `M+`.

This is an exact consequence of equal preincoming count; no Hall inequality is used beyond the definition of `M+`.

## 6. Exact potential-degree jump across a crossing

In the live positive-surplus source universe, the closed-form potential degree is

```text
d_K(u)
 = #{w:c_w>=q_u-1 and q_w<=c_u+1}-1
```

(the mutual-boundary correction is empty here because `c_w>=q_w+1`).

For `x,y` with the same `q` and `c_x<c_y`, the first threshold is identical and the only new potential neighbors are precisely the copies whose demand enters through the second threshold. Hence

```text
d_K(y)-d_K(x)
 = #{w:c_x+2<=q_w<=c_y+1}.                            (28)
```

Combining with the selected-demand desert (26):

> **Exterior degree-jump identity.**
>
> ```text
> d_K(y)-d_K(x)
> = #{w notin M+ : c_x+2<=q_w<=c_y+1}.                (29)
> ```

Thus every increase in potential degree across an equal-`m` crossing is supplied entirely by exterior vertices.

## 7. Cap-deficit trichotomy

The current post-pair target cap is

```text
P_w=min(
  rho_w+b-a-1,
  b-1-q_w,
  rho_w+lambda(q_w,E,z0),        [when applicable],
  d_K(w)-q_w
).                                                       (30)
```

Here `z0` denotes the zero-demand correction parameter used in the selected-excess cap; it is unrelated to the over-saturation variable `z_w` of Section 1.

For a crossing pair, `P_y>=m`. Hence **every** active cap term at `y` is at least `m`. In particular

```text
b-1-q>=m,                                             (31)
```

so the constant cap cannot explain `P_x<m`.

Therefore at least one of the following must hold at `x`:

### R. Residual-cap witness

```text
rho_x+b-a-1 < m.                                      (32)
```

Since the same cap at `y` is at least `m`,

```text
rho_y-rho_x
 >= m-(rho_x+b-a-1).                                  (33)
```

### E. Selected-excess-cap witness

When that cap is active,

```text
rho_x+lambda < m,                                     (34)
```

and therefore

```text
rho_y-rho_x
 >= m-(rho_x+lambda).                                 (35)
```

### K. Potential-degree-cap witness

```text
d_K(x)-q < m.                                         (36)
```

Since `d_K(y)-q>=m`, (29) gives

```text
#{w notin M+ : c_x+2<=q_w<=c_y+1}
 >= m-(d_K(x)-q).                                     (37)
```

Thus the potential-degree mode cannot create a crossing without paying for it in a concrete band of exterior high-demand vertices.

Because `P_x` is the minimum of the active cap terms, every positive crossing has at least one witness mode R, E or K. Multiple modes may hold simultaneously.

## 8. Relation to the original crossing wall

The earlier swap-rigidity theorem says that every third target satisfying

```text
D(y,w)=1,
D(x,w)=0
```

is over-saturated, and in the positive-surplus regime this includes all targets with

```text
c_x<q_w<=c_y.                                         (38)
```

Equation (23) is stronger: it says that **all** `y`-neighbors outside the exactly `q` shared non-over-saturated targets are over-saturated. The interval wall is only the most visible subfamily.

Combining (26) and (38) gives an additional useful statement:

```text
c_x+2<=q_w<=c_y
 => w notin M+
    and y_w>=P_w+1.                                   (39)
```

So all populated interior levels of a crossing wall are simultaneously exterior as sources and over-saturated as targets.

## 9. Hostile counterexample check

For the preserved five-copy counterexample

```text
A      q=0 c=4 P=4 selected,
C      q=0 c=2 P=2 unselected,
B1-B3  q=3 c=4 P=1 selected,
```

we have `m=4`, `C_q=1`,

```text
s_A=1,
z_C=2,
```

so (3)-(5) hold strictly.

Here `x=C`, `y=A`, `q=0`. The strict slack set reachable from `C` is exactly `{A}`, so

```text
|N^+(C) cap Z|=1=q+1.
```

Deleting `A` gives the other known minimum witness

```text
{B1,B2,B3},
```

confirming (22). The interval `c_x+2<=q_u<=c_y+1` is `[4,5]`, which contains no copies, so the selected-demand desert and degree-jump identity are also satisfied. The crossing is instead witnessed by the residual cap, so this hostile example is not accidentally excluded by the trichotomy.

This is exactly the intended red-team behaviour: the new lemmas constrain a positive crossing but do not smuggle in a false abstract `C_q=0` theorem.

## 10. Frozen-pilot evidence

GitHub Actions run `34859094097` completed successfully on the deterministic 15-state frozen pilot. Its artifact

```text
artifact id:     10356424619
artifact digest: sha256:b91c48268fb6b2b3c6545b28ced230d4ab8ad71b371b49205af1b6166c2a63f4
```

reports

```text
profiles tested:              201,493,148
target-Hall failure profiles:     205,919
global-layer detected:            205,107
global-layer false negatives:         812
q-stratified detected:            205,919
q-stratified false negatives:           0
zero-crossing profiles:           205,919
positive-crossing profiles:             0
crossing sum:                           0
maximum crossing:                       0
```

Thus `C_q=0` holds on **all 205,919** target-Hall failures in the frozen pilot, not only on the previously isolated 812 global-layer false negatives. This remains reconnaissance evidence, not a theorem.

## 11. Next analytic target

The crossing problem is now split into three concrete modes:

```text
R: residual-cap threshold crossing,
E: selected-excess-cap threshold crossing,
K: potential-degree threshold crossing supplied by exterior high-q mass.
```

The recommended next step is to derive Murty-wide impossibility or aggregate budget bounds separately for R/E/K, using:

- weighted residual charge (8) for high-`m` R/E crossings;
- exact selected-excess budget for E;
- exterior degree-jump identity (29), positive-slack incidence pressure, and low-c/high-q potential-pair obstruction for K;
- the double-tightness equations (19)-(23) in every mode.

This is materially narrower than attempting an abstract Hall exactness theorem.

## 12. Trust boundary

Sections 2 and 4 are exact consequences of the crossing definition, labelled Hall minimality/maximality, integrality, and directed source-neighborhood containment. Section 3 additionally uses the previously derived coupled residual-slack budget. Sections 5-7 use the live canonical/post-pair source universe and cap formula; the exact potential-degree jump uses positive-surplus residual activity as in the current frontier.

The package does not assert graph realizability, does not promote any new whole-state exclusion, and does not prove the unrestricted Murty-Simon conjecture. External mathematical review and genuinely independent reproduction remain open.
