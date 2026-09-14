# Murty q-tail Hall conjecture

14 September 2026. **Research conjecture / proof target. NOT a promoted theorem.**

The q-layer threshold normal form suggests a much stronger simplification on the actual Murty post-pair cap domain than is true for an arbitrary directed Hall instance.

For an integer `t>=1`, define the complete high-demand source tail

```text
S_t={u:q_u>=t}.                                         (1)
```

Let

```text
F(S)=H(S)-D(S)
```

be the exact directed target-Hall margin using the current post-pair target capacities `P`.

The candidate statement is:

> **Murty q-tail Hall conjecture.** For the target capacities produced by the current post-pair Murty cap formula,
>
> ```text
> min_{S subseteq B} F(S)
> = min_{t>=1} F(S_t),                                  (2)
> ```
>
> with the empty set included on the right as margin zero.

Equivalently, if the target-flow Hall relaxation fails at all, then it fails on a high-`q` tail.

If proved, this would replace arbitrary source-set min-cut / max-flow by a one-parameter family of explicit histogram cuts.

## 1. Exact tail margin

For a target `w`, the incoming count from `S_t` is

```text
y_w(t)
 = #{u != w :
       t<=q_u<=c_w+1,
       q_w<=c_u}.                                      (3)
```

Define the source rectangle count

```text
R(t,x;q)
 = #{u:t<=q_u<=x and c_u>=q}.                          (4)
```

Then

```text
y_w(t)
 = R(t,c_w+1;q_w) - 1_{q_w>=t}.                        (5)
```

Therefore the candidate exact minimum would be obtained from

```text
F_t
 = sum_w min(P_w,
             R(t,c_w+1;q_w)-1_{q_w>=t})
   - sum_{u:q_u>=t}q_u.                                (6)
```

No max flow remains in (6).

## 2. Frozen 812-profile result

The detailed frozen artifact from GitHub Actions run `34850187436` contains the 812 exact target-Hall failures missed by the global receiver-layer rearrangement.

Direct evaluation of every high-`q` tail on those frozen type profiles gives

```text
812 difficult profiles tested,
812 profiles with a deficient high-q tail,
0 misses.                                              (7)
```

The first deficient tail threshold is distributed as

```text
t=2 : 426
t=3 : 191
t=4 : 195.                                             (8)
```

The maximum-deficiency tail uses

```text
t=2 : 220
t=3 : 170
t=4 : 422.                                             (9)
```

Thus the entire difficult q-stratified residue is already witnessed by the one-parameter tail family.

This is stronger than the earlier observation that the canonical maximal witnesses on the 812 residue are q-homogeneous thresholds.

## 3. Exhaustive small-domain support for the CURRENT cap formula

The current target cap is

```text
P_u=min(
  rho_u+b-a-1,
  b-1-q_u,
  rho_u+lambda(q_u,E,z)  [when applicable],
  d_K(u)-q_u
).                                                      (10)
```

Here `c=q+rho`, `rho>=1`, `q+rho<=a`, and `d_K` is the exact potential-pair degree.

Independent exhaustive enumeration over `(q,rho,E,z)` with the cap (10) found no discrepancy between the exact Hall minimum and the best high-q tail.

Frozen completed blocks include:

```text
(a,b)=(2,3):       90 cap profiles,
(a,b)=(2,4):      351 cap profiles,
(a,b)=(3,4):   12,258 cap profiles,
(a,b)=(3,5):    3,320 multiset cap profiles,
(a,b)=(4,5):   42,836 multiset cap profiles,
(a,b)=(4,6):  145,729 multiset cap profiles.            (11)
```

The `(4,6)` block alone contains `10,980` profiles with negative exact Hall minimum. Every one has a high-q tail attaining the same minimum.

The multiset enumeration covers every `(q,rho)` margin pattern up to permutation and every tested admissible `E,z` value in the stated small universe.

## 4. Broad random red-team

Additional deterministic random tests over the current cap formula have varied

```text
b,
b-a,
positive rho profiles,
q with q+rho<=a,
E across the full range 0..Q,
zero-demand correction z,
potential-pair degree caps.                             (12)
```

No tail-minimum discrepancy has been found.

One dedicated equality run tested `28,138` valid current-cap profiles and obtained

```text
exact min F = min_t F(S_t)
```

in all `28,138` cases.

A separate wide-excess detection run tested `114,746` valid profiles; `1,564` had negative exact Hall minimum and all `1,564` had a deficient high-q tail.

These random totals are reconnaissance and are not combined into a formal exhaustive count because the runs use overlapping parameter ranges.

## 5. Crucial hostile counterexample outside the current cap formula

The tail statement is false for arbitrary fixed-q-monotone target capacities, even under several other Murty-looking pointwise restrictions.

Take `a=4`, `b=7` and seven labelled copies with `(q,c,P)`

```text
(0,2,2),
(1,2,1),
(3,4,3),
(3,4,3),
(1,2,1),
(3,4,3),
(2,3,0).                                               (13)
```

Here `rho=c-q>=1`, `c<=a`, and the listed capacities respect:

```text
P<=rho+b-a-1,
P<=b-1-q,
P<=d_K-q.                                              (14)
```

They are also fixed-q monotone.

Nevertheless the exact Hall minimum is `-1`, attained for a non-tail set containing the three `q=3` copies and the two `q=1` copies while excluding the `q=2` copy. Every high-q tail has margin at least zero.

Thus neither directed compatibility, positive residual activity, fixed-q monotonicity, nor the residual/simple/potential-pair caps alone imply (2).

The deterministic current cap (10), especially its selected-excess structure and the way all cap terms are combined, is genuinely part of the conjecture.

This counterexample is a standing red-team obligation: any proposed proof that does not use hypotheses distinguishing (10) from (13) is incomplete.

## 6. Relation to earlier results

The old one-sided orientation threshold inequality is the coarse capacity projection of a high-q tail. For `S_t`, sources cannot reach targets with `c<t-1`, giving

```text
sum_{u:q_u>=t}q_u
 <= sum_{w:c_w>=t-1}P_w                               (15)
```

as a safe but weaker condition.

The exact tail cut (6) also retains:

```text
q_w<=c_u,
unit source-target edges,
diagonal deletion,
competition among high-q sources.                      (16)
```

On the frozen 812 residue, the coarse rectangle/capacity-only form detects `794/812`, while the exact high-q tail detects `812/812`.

Thus the missing 18 cases require genuine directed target competition even though the witness family remains one-dimensional.

## 7. Why this would matter

If (2) is proved, then the current all-order target-Hall problem becomes:

```text
for every admissible q,rho,E,z profile,
find t such that F_t<0.                                (17)
```

Each `F_t` is the explicit histogram expression (6). The source-set search, canonical staircase, crossing statistic and target max-flow would disappear from the proof-critical layer.

The remaining work would be to combine (6) with:

```text
q+rho<=a,
sum q=S+E,
residual budget,
selected-excess budget,
potential-pair capacity,
source-demand forcing.                                 (18)
```

This is materially closer to a scalar all-order contradiction.

## 8. Immediate proof target

A direct universal exchange lemma based only on `q_x>q_y` is false away from Hall minimizers, even for current-cap profiles. Therefore the proof, if true, must use either:

1. minimum-witness tightness;
2. an uncrossing/compression argument acting on several q-levels at once; or
3. a structural property of the deterministic cap function (10), not merely neighborhood nesting.

The most promising route is to choose a Hall minimizer with lexicographically maximal selected `q`-multiset and prove that any inversion `y in S`, `x notin S`, `q_x>q_y` can be neutralized at minimum value using the cap-specific slack constraints.

## Trust boundary

Equation (2) is **not proved**. The 812-profile result and the finite enumerations are computational evidence only. The arbitrary-cap counterexample is preserved specifically to prevent accidental promotion of a false general Hall statement.
