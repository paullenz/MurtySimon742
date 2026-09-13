# Excess-budget orientation cost

13 September 2026. **Candidate general projection inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note couples the selected-excess inequality to the missing-edge orientation globally. The previous [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md) constrains each source separately. Summing over the entire selected-incidence system yields an additional weighted budget condition, and the orientation side of that condition is naturally a min-cost flow.

The clean theorem below is stated first for an **all-positive-demand** branch. A zero-demand correction requires separate accounting of incidences that do not satisfy the selected-excess inequality and is not silently assumed here.

## 1. Setup

For every selected label `i`, write

```text
x_i=s_i+e_i,
e_i>=0,
E=sum_i e_i.
```

For every source `u in B`, write

```text
q_u = selected outdegree,
p_u = selected indegree,
rho_u = residual A-cross degree.
```

Assume throughout Sections 1-7 that

```text
s_i>0 for every label i.                              (1)
```

For each source define

```text
L_u=max(0,p_u-rho_u+1).                               (2)
```

The selected-excess incidence inequality gives, on every selected incidence `u-i`,

```text
L_u<=e_i.                                             (3)
```

## 2. Global weighted excess inequality

Source `u` has exactly `q_u` selected incidences. Summing (3) over all selected source-label incidences gives

```text
sum_u q_u L_u
 <= sum_i x_i e_i.                                    (4)
```

Indeed label `i` occurs on exactly `x_i` selected incidences, so its excess `e_i` is counted exactly `x_i` times on the right.

Substituting `x_i=s_i+e_i`:

```text
sum_u q_u max(0,p_u-rho_u+1)
 <= sum_i (s_i+e_i)e_i.                               (5)
```

This is a global coupling between the orientation indegrees `p` and the excess distribution `e`.

## 3. Selection-free upper envelope for the excess side

Selected-edge forcing gives

```text
s_i<=rho_u                                             (6)
```

on every selected incidence. Therefore label `i` can use at most

```text
h_i=#{u:rho_u>=s_i}                                   (7)
```

sources. Since its selected degree is `x_i=s_i+e_i`, every legal branch has

```text
0<=e_i<=h_i-s_i.                                      (8)
```

If some `h_i<s_i`, the scalar state is already impossible.

For fixed total excess `E`, define the exact integer envelope

```text
M_s,rho(E)
 = max sum_i (s_i+e_i)e_i                             (9)
```

subject to

```text
sum_i e_i=E,
0<=e_i<=h_i-s_i,
e_i integer.                                          (10)
```

This is a small finite knapsack/dynamic programme depending only on `(s,rho,E)`. Every legal branch satisfies

```text
sum_u q_u max(0,p_u-rho_u+1)
 <= M_s,rho(E).                                       (11)
```

No selected geometry or individual excess profile is fixed in (11).

### Why the exact label cap matters

The weaker bound `e_i<=b-s_i` is always true, but (8) is usually sharper: a demand-`s_i` label can only be selected by sources whose residual degree reaches `s_i`. Thus the same demand-compatibility structure used by the selected-incidence Hall theorem also caps how much excess a label can carry.

## 4. Incoming orientation as a convex cost

For fixed `q,rho`, define the target cost

```text
f_u(p)=q_u max(0,p-rho_u+1).                          (12)
```

The first

```text
rho_u-1                                                (13)
```

incoming units at target `u` are free. Every further incoming unit increases `f_u` by exactly

```text
q_u.                                                   (14)
```

Therefore (11) says that the actual orientation must have total target cost at most `M_s,rho(E)`.

Let `P_u` be any valid upper bound on `p_u`, for example the minimum of

```text
b-1-q_u,
rho_u+b-a-1,
d_KD(u)-q_u,
the total-excess source cap.                          (15)
```

## 5. Cheap scalar allocation bound

Ignore source-target compatibility and ask only whether `Q=sum q=sum p` incoming units can be placed into target capacities `P_u` cheaply enough.

Target `u` supplies

```text
min(P_u,max(0,rho_u-1))                               (16)
```

zero-cost slots, followed by `P_u` minus that number of slots of unit cost `q_u`.

Let `C_0(q,rho,P)` be the sum of the `Q` cheapest slots among all these target slots; if fewer than `Q` slots exist, set `C_0=+infinity`.

Every legal branch necessarily satisfies

```text
C_0(q,rho,P) <= M_s,rho(E).                           (17)
```

This is a particularly cheap all-excess screen. At `E=0`, the right side is zero and (17) reduces to the requirement that all incoming load fit within the exact-demand free capacities `p_u<=rho_u-1`.

## 6. Directed-compatible min-cost flow

Now retain the exact directed compatibility relation from [`ORIENTATION_FLOW_HALL.md`](ORIENTATION_FLOW_HALL.md):

```text
D(u,w)
 iff u!=w,
     q_u<=q_w+rho_w+1,
     q_w<=q_u+rho_u.                                  (18)
```

Construct the network

```text
source -> u_L       capacity q_u, cost 0,
u_L -> w_R        capacity 1, cost 0 when D(u,w),
w_R -> sink         free capacity from (16), cost 0,
w_R -> sink         remaining capacity, unit cost q_w.      (19)
```

Let `C_D(q,rho,P)` be the minimum cost of a value-`Q` flow, or `+infinity` if no such flow exists.

Every actual missing-edge orientation induces a value-`Q` flow in (19), and its flow cost is exactly

```text
sum_w q_w max(0,p_w-rho_w+1).                         (20)
```

Hence:

> **Excess-budget orientation theorem.** In an all-positive-demand branch, every legal scalar branch satisfies
>
> ```text
> C_D(q,rho,P) <= M_s,rho(E).                         (21)
> ```

Failure of (21) is a quantifier-correct exclusion of the `(E,q)` branch under the canonical bridge assumptions.

Because compatibility can only increase minimum cost relative to the free allocation,

```text
C_0 <= C_D.                                           (22)
```

Thus (17) is a cheap pre-screen and (21) is the stronger exact directed-flow relaxation.

## 7. Proof certificates

The excess envelope `M_s,rho(E)` can be certified by a finite DP table recording, after each label, the maximum value at every partial excess total.

The min-cost orientation side can be certified without floating arithmetic by recording an integral value-`Q` flow and its integer cost when feasible. For an exclusion, a dual min-cost-flow potential/cut certificate may be recorded, or the verifier can replay the small integer network exactly.

No floating-point solver status or timeout is proof.

## 8. Relation to the per-source total-excess cap

The per-source cap follows by applying (3) only to the `q_u` incidences at one source and bounding their selected excess by total `E`. The weighted inequality (4) instead sums **all** source incidences and correctly accounts for the fact that one label's excess can support at most `x_i` selected incidences.

Consequently the two conditions are complementary:

```text
per-source total-excess cap
    -> local target capacities P_u,
weighted excess-budget flow
    -> global budget on how many costly incoming slots may be used.   (23)
```

Both should be applied before fixing an individual excess profile.

## 9. Zero-demand boundary

If `s_i=0`, the selected-excess inequality (3) has not been established for that selected incidence. Such labels cannot simply be included in the left-hand summation.

A safe future extension can introduce

```text
z_u = number of zero-demand selected incidences at source u,
```

so the left side becomes

```text
sum_u (q_u-z_u)L_u,                                   (24)
```

while zero-demand selected incidences consume excess because `x_i=e_i>0`. This creates a small additional allocation problem. Until that correction is explicitly proved and implemented, theorem (21) is used only when all `s_i>0`.

## 10. Research significance

This projection reconnects three pieces that were previously being used separately:

1. selected-excess on source-label incidences;
2. source/target capacity of the missing-edge orientation;
3. demand-compatible limits on label selected degree.

It is still a relaxation: it does not force the orientation edge `u->w` and the selected label chosen at `u` to share the full graph geometry. But it is no longer a product of two independent feasibility checks; both sides compete for the same finite total excess budget.

## Trust boundary

The derivation is elementary once the canonical selected-excess inequality, selected-incidence degree ledger, and directed orientation compatibility lemma are accepted. Its Murty-Simon application inherits the trust boundary of those structural statements. Passing (21) is not graph feasibility and does not prove the unrestricted conjecture. External mathematical review and independent reproduction remain open.
