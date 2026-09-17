# E=3 partition reduction: two of the three excess shapes are impossible

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate bridge-level continuation; not promoted; external mathematical review remains open.** This note continues the mixed `{4,5}` near-Turán scope at `(a,b,t)=(20,23,2)` after the small-excess theorem `E>=3` and the full selected-incidence Hall theorem.

## 1. Step-back

At total selected excess

    E=sum_i e_i=3,

there are only three partitions of the excess:

    (3), (2,1), (1,1,1).

The aggregate `E=3` obstruction showed that it is not enough to reuse the weighted endpoint/excess ledgers blindly. Before invoking full Hall, however, two of the three partitions can be removed by sharpening the existing small-excess argument only at the point where it actually changes: how many distinct selected labels can support a source with positive excess requirement.

The conclusion of this note is:

> In the mixed `{4,5}`, `h>=5`, `(20,23,2)` scope, the excess partitions `(1,1,1)` and `(2,1)` are impossible. Hence any surviving `E=3` bridge must have a **unique label of excess three**.

Thus the full `E=3` problem reduces to the single partition `(3)`.

## 2. Inherited notation

Let `k` be the number of demand-five labels. As before,

    r=76+k,
    Q=83+k,
    sum_u p_u=sum_u q_u=Q.

For a source `u`, put

    g_u=max(0,p_u-rho_u+1).

Every selected incidence `ui` satisfies

    e_i>=g_u.

Selected labels at one source are distinct. The local source inequality from the small-excess proof is

    10p_u+15q_u-q_u(p_u+q_u)
      <= 10rho_u+20+delta_k [rho_u=4],                 (1)

where

    delta_k=6  for 0<=k<=14,
    delta_15=5,
    delta_16=2,
    delta_k=0  for 17<=k<=20.

At `E<=2`, (1) was already proved. We first check exactly when it remains valid at `E=3`.

## 3. The local source inequality survives for partitions (1,1,1) and (2,1)

### Partition (1,1,1)

There are exactly three labels with positive excess, each of excess one. Therefore, at any source with `q_u>0`,

- if `g_u=0`, there is no new restriction;
- if `g_u=1`, at most three distinct selected labels are available, so `q_u<=3`;
- if `g_u>=2`, no selected label is eligible, so `q_u=0`.

Hence the only new active states beyond the zero-excess range have

    p_u=rho_u, q_u<=3.

For `rho_u>=4`, direct substitution gives

    10rho+15q-q(rho+q)
      =10rho+q(15-rho-q)
      <=10rho+20

for `q=1,2,3`. Thus (1) remains valid.

### Partition (2,1)

Now one label has excess two and one label has excess one. Thus

- `g=1` permits at most two distinct selected labels, so `q<=2`;
- `g=2` permits at most one selected label, so `q<=1`;
- `g>=3` permits none.

The only new active states are therefore

    p=rho,   q<=2,
    p=rho+1, q<=1.

These are exactly the states already checked in the `E<=2` proof, and for every active source `rho>=4` they satisfy (1) strictly or weakly. Hence (1) again survives unchanged.

So for either partition, summing (1) gives the same source lower bound as before with `E=3`:

    sum_u q_u(p_u+q_u)
      >= L_0(k)+75,                                    (2)

where

    L_0(k)=780+15k-delta_k floor((33+k)/3).

## 4. Partition-specific label ceilings

The small-excess note proved that, relative to the zero-excess label ceiling `U_0(k)`, the excess contribution satisfies

    Delta <= 24E + sum_i e_i^2.                         (3)

Here `E=3`.

For partition `(1,1,1)`,

    sum e_i^2=3,

so

    label side <= U_0(k)+75.                            (4)

For partition `(2,1)`,

    sum e_i^2=5,

so

    label side <= U_0(k)+77.                            (5)

Recall the exact zero-excess gap

    G(k)=L_0(k)-U_0(k),

with `G(k)>0` for every `k`, and the unique minimum `G(12)=2`.

## 5. Partition (1,1,1) is impossible

By (2) and (4), every such bridge would require

    U_0(k)+75 >= L_0(k)+75,

or `G(k)<=0`, contradicting `G(k)>0` for all `k=0,...,20`.

Therefore partition `(1,1,1)` is impossible.

## 6. Partition (2,1) is impossible except for one arithmetic equality case

By (2) and (5), feasibility requires

    G(k)-2 <=0.

Since `G(k)>=2`, this is impossible for every `k` except the sole equality case

    k=12, G(12)=2.

It remains only to close `(k,E)=(12,3)` with excess partition `(2,1)`.

At `k=12`,

    r=88,
    Q=95,
    c_4<=15.

Equality between the source lower bound and label upper bound would force equality in every intervening estimate. In particular `c_4=15`, and equality in the residual-mass bound forces

    rho=(5^5,4^15,1^3).                                (6)

Equality in the summed local source inequality (1) would also require every source to be locally tight.

For the partition `(2,1)` the locally tight states have the same incoming-load ceiling relevant here as in the preceding boundary argument:

- at `rho=1`, tightness forces `p<=3`;
- at `rho=4`, every tight state has `p<=3`;
- at `rho=5`, every tight state has `p<=7`.

Therefore (6) would imply

    sum_u p_u
      <= 3*3 + 15*3 + 5*7
      =89,

whereas the exact orientation ledger requires

    sum_u p_u=Q=95.

So equality is impossible; the source lower bound is in fact strictly larger than the label upper bound. This closes the final `(2,1)` case.

## 7. What remains: only partition (3)

The same local inequality (1) does **not** survive unchanged for partition `(3)`. With one label of excess three, the state

    p=rho+2, q=1, g=3

is now legal at the excess level. For example at `rho=5`,

    10p+15q-q(p+q)
      =77,

while the right side of (1) is only `70`.

This is not a failure of the canonical bridge; it identifies the exact remaining mechanism. Every such `g=3` source must use the **same unique excess-three label**, and full selected-incidence eligibility additionally requires that label to satisfy

    s_*<=rho_u,
    C_*>=p_u+q_u=rho_u+3.

Thus the remaining `(3)` case is intrinsically a **single-column row-packing / endpoint-tail problem**. Aggregate support coefficients alone deliberately forget the information needed to close it.

## 8. Bounded conclusion and next target

> **E=3 partition reduction.** In the canonical bridge at `(a,b,t)=(20,23,2)`, with all twenty demands in `{4,5}` and at least five residual sources of degree at least five, an `E=3` profile can survive only if its entire selected excess is concentrated on one label:
>
>     (e_i)^+ = (3).

The partitions `(1,1,1)` and `(2,1)` are impossible.

This is a bridge-level reduction, not a Murty-Simon proof and not a promoted catalogue theorem.

The next high-value task is now sharply defined: close or realize the unique-excess-three partition using the exact column degree `x_*=s_*+3`, the endpoint mass `C_*`, and the row-packing/Hall restrictions on every source with `g_u>0`, especially the `g=3` sources that are the only reason the old source support inequality can fail.
