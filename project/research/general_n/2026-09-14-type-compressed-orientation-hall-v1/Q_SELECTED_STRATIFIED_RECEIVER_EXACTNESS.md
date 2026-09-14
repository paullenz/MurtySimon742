# Exact q-selected receiver stratification

14 September 2026. **Candidate exact structural theorem for the post-pair orientation-Hall target cap. External mathematical review and novelty assessment remain OPEN.**

The global receiver-layer relaxation loses target identity and retains 99.6% of target-Hall failures in the frozen pilot. The loss disappears after retaining only two pieces of target information:

```text
q_w,
epsilon_w = 1_{w belongs to the selected Hall source set S}.          (1)
```

Within each `(q,epsilon)` stratum, the actual post-pair target capacity and incoming compatible-source count are co-monotone in `c=q+rho`. Consequently the layer/comonotone formula is exact inside every stratum.

## 1. Directed and potential compatibility

Write

```text
c_i=q_i+rho_i.                                           (2)
```

The directed target compatibility relation is

```text
D(u,w) iff u!=w,
            q_u<=c_w+1,
            q_w<=c_u.                                   (3)
```

The potential missing-pair graph `K_D` joins distinct `i,j` when at least one orientation is numerically possible:

```text
{i,j} in E(K_D) iff D(i,j) or D(j,i).                   (4)
```

Let `d_K(i)` be its degree.

## 2. Potential-degree monotonicity at fixed q

Take two vertices `x,y` with

```text
q_x=q_y=q,
c_x<=c_y.                                               (5)
```

For any third vertex `v`, if `{x,v}` is a potential pair then `{y,v}` is also a potential pair. Indeed either

```text
q<=c_v+1 and q_v<=c_x,                                  (6)
```

which remains true after replacing `c_x` by the larger `c_y`, or

```text
q_v<=c_x+1 and q<=c_v,                                  (7)
```

which again remains true for `c_y`.

Moreover `{x,y}` itself is a potential pair because `c_x,c_y>=q`. Hence the neighbor injection that replaces `y` by `x` on the mutual edge gives

> **Fixed-q potential-degree monotonicity.**
>
> ```text
> q_x=q_y, c_x<=c_y  =>  d_K(x)<=d_K(y).                (8)
> ```

## 3. Monotonicity of the post-pair target cap

The current exact relational scanner uses the target cap

```text
P_i = min(
  rho_i+b-a-1,
  b-1-q_i,
  rho_i+lambda(q_i,E,z),
  d_K(i)-q_i
),                                                       (9)
```

where the third entry is present only in the positive-q branch in which the selected-excess cap applies, and `lambda(q,E,z)` is independent of the vertex once `q,E,z` are fixed. Concretely the implementation is

```text
k*=min(z,min(q,E)),
if q>k*: lambda=floor((E-k*)/(q-k*))-1.                 (10)
```

At fixed `q`, increasing `c` is the same as increasing `rho`. The first and third terms of (9) are nondecreasing in `rho`, the second is constant, and the fourth is nondecreasing by (8). The minimum of nondecreasing functions is nondecreasing. Thus:

> **Fixed-q target-cap monotonicity.**
>
> ```text
> q_x=q_y, c_x<=c_y  =>  P_x<=P_y.                     (11)
> ```

This statement concerns the post-pair cap actually used by the current target-Hall model. It does not claim monotonicity for an arbitrary externally supplied capacity assignment.

## 4. Incoming-count monotonicity after fixing self-selection status

Fix an arbitrary source set `S`. Before deleting the forbidden diagonal, define

```text
m_w(S)=#{u in S:
          q_u<=c_w+1,
          q_w<=c_u},                                    (12)
```

where the numerical test is allowed to count `u=w`.

For `q_x=q_y` and `c_x<=c_y`, every selected source counted by `m_x` is also counted by `m_y`, so

```text
m_x(S)<=m_y(S).                                         (13)
```

The actual incoming count is

```text
y_w(S)=m_w(S)-epsilon_w,
epsilon_w=1_{w in S}.                                   (14)
```

Therefore, if in addition

```text
epsilon_x=epsilon_y,                                    (15)
```

then

> **Fixed-(q,epsilon) incoming monotonicity.**
>
> ```text
> c_x<=c_y  =>  y_x(S)<=y_y(S).                        (16)
> ```

The split by `epsilon` is exactly what removes the one-unit self-deletion obstruction that remains in a q-only stratification.

## 5. Exact stratified layer theorem

Partition target copies into the strata

```text
G_{q,epsilon}
 = {w:q_w=q, 1_{w in S}=epsilon}.                       (17)
```

Within each nonempty stratum, order target copies by increasing `c`. By (11) and (16), both sequences

```text
P_w,
y_w(S)                                                  (18)
```

are nondecreasing in that same order.

For each stratum and integer `k>=1`, define

```text
alpha_{q,epsilon,k}
 = #{w in G_{q,epsilon}:P_w>=k},

beta_{q,epsilon,k}
 = #{w in G_{q,epsilon}:y_w(S)>=k}.                     (19)
```

Because both threshold sets are suffixes of the same c-order, their intersection has size exactly the smaller suffix:

```text
#{w in G_{q,epsilon}:P_w>=k and y_w>=k}
 = min(alpha_{q,epsilon,k},beta_{q,epsilon,k}).          (20)
```

Using the layer-cake identity gives:

> **Exact q-selected receiver stratification theorem.** For every source set `S` in the current post-pair target-cap model,
>
> ```text
> H(S)=sum_w min(P_w,y_w(S))
>     =sum_{q,epsilon}\sum_{k>=1}
>        min(alpha_{q,epsilon,k},beta_{q,epsilon,k}).    (21)
> ```

Thus the full target-by-target receiving capacity is recovered exactly from one-dimensional layer counts in at most two strata per q-value.

## 6. Type-compressed form

For a complete-type Hall cut, `epsilon` is constant on every `(q,c,P)` type class. Hence (21) can be computed directly from the type table without labelled targets.

For the canonical maximal minimum witness `M+`, the selected bit is determined by its sharp-hardness staircase. The exact deficient Hall inequality therefore becomes an exact **q-stratified layer inequality** rather than a general target max-flow cut.

This is a stronger compression than the global receiver-layer bound:

```text
global layers                 : one P/y marginal pair,
q-only strata                 : retains q but not self-selection,
(q,selected)-strata           : exact for the post-pair cap.          (22)
```

## 7. General-theory target

The remaining problem is no longer target correlation. It is to control, for the canonical staircase, the stratum layer counts

```text
alpha_{q,epsilon,k},
beta_{q,epsilon,k}.                                    (23)
```

The alpha layers inherit explicit Murty bounds from `P>=k`. The beta layers count targets of fixed q and selected status whose intervals meet at least k selected source intervals. At fixed q this is a one-dimensional threshold condition in `c=q+rho`.

This offers a plausible symbolic route:

```text
canonical source staircase
 -> q-selected target strata
 -> monotone rho/c threshold counts
 -> exact Hall capacity.                               (24)
```

## 8. Trust boundary

The theorem is exact for the target capacities defined by the current post-pair relational model. Its Murty-Simon application inherits the canonical graph-to-constraint bridge and the validity of all cap terms entering (9). It does not assert graph realizability from target-flow feasibility and does not prove the unrestricted conjecture.
