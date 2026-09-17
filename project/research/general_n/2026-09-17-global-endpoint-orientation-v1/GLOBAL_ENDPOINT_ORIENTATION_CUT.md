# Global endpoint-orientation coupling cut

17 September 2026. Research directed by Paul Lenz; derivation and audit by ChatGPT/Geeps.

**Status: candidate general lemma inside the canonical selected/residual bridge; not promoted, external mathematical review open.** The abstract summation argument below is elementary once the previously recorded bridge facts are granted. Its purpose is to retain one piece of information lost by the scalar/heavy-load relaxations: the same margins `q_u,p_u` participate simultaneously in selected-label endpoint load and in the missing-pair orientation ledger.

## 1. Setup

Work in an all-positive-demand branch of the canonical selected/residual bridge. For each source `u in B` retain

```text
q_u   = selected missing-B edges oriented out of u,
p_u   = selected missing-B edges oriented into u,
rho_u = residual A-cross degree.
```

For each selected label `i` retain demand `s_i>0` and endpoint mass

```text
C_i=R_i+x_i.
```

The established bridge facts used here are:

1. exact orientation ledger

```text
sum_u q_u=sum_u p_u=:Q;                               (1)
```

2. if `q_u>0`, the exact selected-incidence system gives at least one selected incidence `ui`;
3. selected-edge forcing on every such incidence gives

```text
s_i<=rho_u;                                            (2)
```

4. endpoint load on every such incidence gives

```text
q_u+p_u<=C_i;                                          (3)
```

5. the canonical incoming caps give

```text
p_u<=b-1-q_u,
p_u<=rho_u+b-a-1.                                     (4)
```

Only the second cap in (4), together with the trivial `p_u<=b-1` when `q_u=0`, is needed for the basic cut.

## 2. Source endpoint ceiling

For each source define the largest endpoint mass of a demand-compatible label

```text
M_u=max { C_i : 0<s_i<=rho_u },                       (5)
```

with `M_u=-infinity` if the set is empty.

Also define the inactive incoming ceiling

```text
P_u^0=min(b-1, rho_u+b-a-1).                          (6)
```

A legal branch must have `P_u^0>=0` whenever `q_u=0`; otherwise (4) already contradicts `p_u>=0`.

Now put

```text
B_u = P_u^0                         if M_u=-infinity,
B_u = max(P_u^0,M_u)                otherwise.         (7)
```

Then every legal source satisfies

```text
p_u+q_u<=B_u.                                          (8)
```

Indeed:

- if `q_u=0`, (6) gives `p_u+q_u=p_u<=P_u^0<=B_u`;
- if `q_u>0`, some selected incidence `ui` exists. By (2), its label occurs in the maximum (5), and by endpoint load (3),

```text
p_u+q_u<=C_i<=M_u<=B_u.
```

This is the point where the selected-incidence and orientation systems are coupled rather than optimized independently.

## 3. Global endpoint-orientation cut

Summing (8) and using (1) gives the necessary inequality

```text
2Q = sum_u(p_u+q_u)
   <= sum_u B_u.                                      (9)
```

> **Global endpoint-orientation cut.** In every legal all-positive-demand canonical branch,
>
> ```text
> 2Q <= sum_{u in B} max(P_u^0,M_u),                  (10)
> ```
>
> interpreting a source with no demand-compatible selected label as contributing only `P_u^0`.

This is deliberately a cheap projection. It does not use selected excess, pair uniqueness, the two-dimensional orientation Hall relation, or competition between labels. Any of those can only strengthen the branch test.

The value of (10) is that it cannot be recovered by separately maximizing selected-incidence capacity and incoming-orientation capacity: the same `q_u` decides which side of the source bound is active, and the identity `sum q=sum p` converts the pointwise endpoint ceiling into a global factor-two demand.

## 4. The 17 September scalar staircase obstruction is killed

Apply the cut to the abstract scalar witness recorded in `../2026-09-17-staircase-scalar-obstruction-v1/`:

```text
a=20,
b=23,
rho=(5^5,4^11,1^7),
s_i=4 for all 20 labels,
x_i=4 for all 20 labels,
R=(4^16,3^4).
```

Hence

```text
C=(8^16,7^4),
Q=sum_i x_i=80,
b-a-1=2.
```

For a source with `rho=5` or `rho=4`, all twenty demand-four labels are demand-compatible and therefore

```text
M_u=8.
```

The inactive incoming ceilings are

```text
rho=5: P_u^0=min(22,7)=7,
rho=4: P_u^0=min(22,6)=6,
rho=1: P_u^0=min(22,3)=3.
```

A `rho=1` source has no demand-compatible label, so its contribution is only 3. Therefore

```text
sum_u B_u
 =5*8+11*8+7*3
 =149.                                                (11)
```

But

```text
2Q=160>149.                                           (12)
```

Thus the scalar witness **cannot extend even to the coupled canonical selected-incidence/orientation margins**. The gap is eleven units.

This does not prove that every scalar profile outside the exact block is impossible. It shows something more targeted and strategically useful: the explicit witness that defeated the staircase/heavy-load scalar system disappears as soon as one restores the most elementary common-margin endpoint coupling.

## 5. Relation to the existing flow theorems

The selected-incidence Hall theorem and orientation-flow Hall theorem are individually exact for their respective relaxations, but checking them independently can still forget that the same source has the same `q_u` and `p_u` in both systems. Inequality (10) is a low-cost common-margin cut before either system is independently maximized.

It should therefore be placed computationally before the more expensive Hall replays:

```text
source endpoint ceiling (10)
 -> pair-degree / orientation prefix screens
 -> pair-choice Hall
 -> target-capacity Hall
 -> selected-incidence Hall
 -> branch-specific joint geometry.
```

A stronger next version can replace `M_u` by an excess-aware endpoint ceiling: selected excess restricts the labels available to a source according to `p_u-rho_u+1`. That makes the ceiling depend on the incoming load itself and may yield a nonlinear but still finite source envelope.

## 6. What is and is not established

Established inside the stated bridge hypotheses:

- the pointwise common-margin ceiling (8);
- the summed cut (10);
- exact arithmetic exclusion (11)-(12) of the previously recorded scalar obstruction.

Not established here:

- that (10) alone forces an exact square block;
- that a branch satisfying (10) extends to a graph;
- any new canonical survivor count;
- external validation of the canonical selected/residual bridge facts on which the Murty-Simon application rests.

## 7. Strategic consequence

The last unit showed that more scalar staircase algebra could not close scope. This unit shows that the obstruction is not robust to even a simple non-decoupled endpoint/orientation cut. That is evidence that the correct next route is **joint common-margin structure**, not abandonment of the structural programme and not another round of scalar threshold summation.

The next high-value question is whether the excess-aware refinement of (10), possibly combined with endpoint-class packing, forces either an exact block or a much narrower family of non-square profiles. If it does not, the surviving profile should be preserved as the next stronger obstruction before adding full Hall geometry.

## Trust boundary

The summation proof is elementary. Its Murty-Simon interpretation depends on the existing canonical selected/residual bridge, specifically exact selected-incidence row degrees, selected-edge forcing, endpoint load, the missing-pair orientation ledger and the canonical incoming cap. Those dependencies remain subject to external review. No theorem about the original conjecture is promoted by this note.
