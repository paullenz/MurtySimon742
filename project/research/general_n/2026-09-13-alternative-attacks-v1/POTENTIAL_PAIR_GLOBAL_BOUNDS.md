# Global bounds from potential-pair capacity

13 September 2026. **Candidate general consequences inside the canonical selected/residual bridge. External mathematical review and novelty assessment remain OPEN.**

This note records the selection-independent global inequalities obtained by summing [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md). They are weaker than the full pointwise capacity test used in the finite frontier scan, but expose a plausible all-order mechanism: high selected load requires a sufficiently large reservoir of vertices whose `(q,c)` coordinates are compatible with being missing neighbours.

## 1. Setup

For `u in B`, write

```text
q_u = selected outdegree,
p_u = selected indegree,
rho_u = residual A-cross degree,
c_u = q_u+rho_u,
Q = sum_u q_u = sum_u p_u.
```

Let

```text
J=overline{H[B]}
```

be the actual missing graph and `K_D` the potential-pair graph from [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md). Then

```text
J subseteq K_D,                                       (1)
d_J(u)=q_u+p_u.                                       (2)
```

## 2. Global potential-edge bound

Summing (2),

```text
sum_u d_J(u)=sum_u(q_u+p_u)=2Q.                       (3)
```

Since `J subseteq K_D`,

```text
2Q <= sum_u d_KD(u)=2|E(K_D)|,                        (4)
```

or equivalently

```text
Q <= |E(K_D)|.                                        (5)
```

Thus the selected missing-edge count can never exceed the number of unordered pairs that survive the directed endpoint compatibility test.

This looks tautological after `K_D` has been defined, but its value is that `K_D` is determined only by the scalar source coordinates `(q_u,c_u)`, not by the unknown missing graph itself.

## 3. Threshold-reservoir form

Define

```text
H(r)=#{w:c_w>=r},
L(r)=#{w:q_w<=r}.                                     (6)
```

The pointwise threshold consequence of potential-pair capacity is

```text
d_KD(u)
 <= min(H(q_u-1),L(c_u+1))-1.                         (7)
```

Combining (4) and (7):

> **Global threshold-reservoir inequality.** Every legal branch satisfies
>
> ```text
> 2Q
> <= sum_u [min(H(q_u-1),L(c_u+1))-1].                (8)
> ```

Dropping the `L` term gives the simpler one-sided consequence

```text
2Q <= sum_u [H(q_u-1)-1].                             (9)
```

Dually,

```text
2Q <= sum_u [L(c_u+1)-1].                             (10)
```

The two-sided minimum in (8) is generally stronger than either marginal inequality.

## 4. Exact type-count form

Group vertices by type

```text
T=(q,c)
```

with multiplicity `m_T`. For types `T=(q,c)` and `T'=(q',c')`, define

```text
A(T,T')=1
```

when

```text
c'>=q-1,
q'<=c+1,
```

except on the simultaneous boundary

```text
c'=q-1,
q'=c+1,                                               (11)
```

where `A(T,T')=0`.

Then the exact potential degree of a vertex of type `T` is

```text
d_KD(T)=sum_T' m_T' A(T,T') - 1,                     (12)
```

where the `-1` removes the vertex itself. Consequently

```text
2Q <= sum_T m_T d_KD(T).                              (13)
```

The right side is a quadratic integer form in the type multiplicities. This is the representation used by the independent type-count frontier audit.

## 5. High-load scarcity

The simplest structural content of (9) is worth isolating. A source with selected outdegree `q` can have missing degree only into the reservoir

```text
{w:c_w>=q-1}.                                         (14)
```

Therefore

```text
p_u+q_u <= H(q_u-1)-1.                               (15)
```

If many sources have large `q_u`, then each of them requires a large high-`c` reservoir. But `c_u=q_u+rho_u<=a`, so a large `c` value consumes the same finite cross-neighbourhood budget that also supports selected demand. This is the prospective all-order tension:

```text
many large q
  -> many vertices need large c-reservoirs
  -> many c values must be large
  -> rho/q budget becomes concentrated
  -> selected-demand and incoming-capacity constraints tighten.       (16)
```

This is analogous in spirit to the earlier residual h-index argument, but the threshold variable now comes from **potential missing neighbours** rather than only residual activity.

## 6. Layer-cake form of the one-sided bound

Because `H(r)` is decreasing,

```text
sum_u H(q_u-1)
 = sum_{u,w} 1[c_w>=q_u-1]
 = #{(u,w): q_u<=c_w+1}.                              (17)
```

Hence (9) is exactly

```text
2Q+b
 <= #{(u,w): q_u<=c_w+1}.                             (18)
```

Equivalently, the number of ordered incompatible source-target pairs

```text
I_1=#{(u,w):q_u>=c_w+2}                               (19)
```

must satisfy

```text
I_1 <= b^2-b-2Q.                                      (20)
```

The two-dimensional theorem further removes ordered pairs with `q_w>=c_u+2` and the mutual boundary cases. Thus a dense missing graph forces the `(q,c)` cloud to have relatively few inversions of the form `q_u>=c_w+2`.

This order-theoretic viewpoint may be more amenable to a symbolic extremal argument than explicit orientation flow.

## 7. Coupling to incoming caps

The global edge bound (8) uses only `J subseteq K_D`. The finite closures are stronger because each vertex also has an incoming allowance

```text
P_u=min(
  rho_u+b-a-1,
  b-1-q_u,
  d_KD(u)-q_u,
  total-excess source cap when applicable
).                                                    (21)
```

and therefore

```text
Q<=sum_u P_u.                                         (22)
```

Equation (22) can be viewed as a weighted strengthening of (4): potential neighbours are not merely counted globally; each source must retain enough of its potential degree after its own outgoing load `q_u` has already consumed part of it.

## 8. Research direction

The next symbolic targets suggested by (8)-(20) are:

1. minimize the compatible-pair count for fixed `sum q`, `sum rho` and `q+rho<=a`;
2. characterize extremal `(q,c)` type distributions for the quadratic form (13);
3. combine high-load scarcity (15) with total-excess source caps to eliminate whole parameter regions without enumerating q profiles;
4. determine whether the inversion bound (20) admits a rearrangement/majorization extremum in which q is oppositely sorted to c;
5. couple the resulting scalar inequality to the existing `7/12` maximum-degree theorem to push the unresolved degree window downward.

No such stronger all-order theorem is claimed here yet.

## Trust boundary

All displayed inequalities are elementary consequences of `J subseteq K_D` and the potential-pair theorem. Their Murty-Simon application therefore inherits the canonical bridge trust boundary. These are necessary conditions only; satisfying them does not imply graph feasibility or prove the unrestricted conjecture.
