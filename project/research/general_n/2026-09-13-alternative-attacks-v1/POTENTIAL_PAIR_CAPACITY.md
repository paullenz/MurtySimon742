# Potential-pair capacity theorem

13 September 2026. **Candidate general theorem inside the canonical selected/residual bridge. External mathematical review and novelty assessment remain OPEN.**

This note isolates the mechanism that closed N34 scalar states 13518 and 13519. It is strictly cheaper than orienting the missing graph or solving a Hall flow: the directed selected-edge constraints first define an **undirected potential-pair graph**, and the actual missing graph must be a subgraph of it.

## 1. Setup

For `u in B` write

```text
q_u   = selected missing-B edges oriented out of u,
p_u   = selected missing-B edges oriented into u,
rho_u = residual A-cross degree,
c_u   = q_u+rho_u.
```

Let

```text
J=overline{H[B]}.
```

Every edge of `J` receives exactly one selected orientation, and therefore

```text
d_J(u)=q_u+p_u.                                       (1)
```

The directed compatibility theorem says that an actual selected orientation

```text
u -> w
```

requires

```text
q_u<=c_w+1,
q_w<=c_u.                                             (2)
```

## 2. Exact potential-pair criterion

Define the directed relation

```text
D(u,w)
 iff u!=w,
     q_u<=c_w+1,
     q_w<=c_u.                                        (3)
```

An unordered pair `{u,w}` can be missing only if at least one orientation is legal:

```text
D(u,w) or D(w,u).                                     (4)
```

The disjunction has an exact symmetric form.

> **Potential-pair criterion.** For distinct `u,w`, condition (4) holds if and only if
>
> ```text
> c_w>=q_u-1,
> q_w<=c_u+1,                                         (5)
> ```
>
> and it is **not** simultaneously true that
>
> ```text
> c_w=q_u-1,
> q_w=c_u+1.                                          (6)
> ```

### Proof

If `D(u,w)` holds then `q_u<=c_w+1`, giving the first inequality in (5), and `q_w<=c_u`, which is stronger than the second. If `D(w,u)` holds, the same two weak inequalities follow with the second strengthened instead.

Conversely suppose (5) holds. If `q_w<=c_u`, then `D(u,w)` holds. Otherwise the integer inequality in (5) forces `q_w=c_u+1`. If also `q_u<=c_w`, then `D(w,u)` holds. The only remaining possibility is `q_u=c_w+1` and `q_w=c_u+1`, exactly the simultaneous boundary (6), in which neither orientation is legal. QED.

## 3. Closed-form potential degree

Let `K_D` be the graph on `B` whose edges are exactly the potential missing pairs (4). Since `rho_u>=1` in the live positive-surplus branches,

```text
c_u>=q_u+1,
```

so `u` itself always satisfies the two weak inequalities in (5). Therefore the degree of `u` in `K_D` is exactly

```text
d_KD(u)
 = #{w : c_w>=q_u-1 and q_w<=c_u+1}
   - 1
   - #{w!=u : c_w=q_u-1 and q_w=c_u+1}.              (7)
```

The `-1` deletes `w=u`; the final term deletes the forbidden mutual-boundary pairs.

A weaker but sometimes convenient one-dimensional consequence is

```text
d_KD(u)
 <= min(
      #{w:c_w>=q_u-1},
      #{w:q_w<=c_u+1}
    ) - 1.                                            (8)
```

## 4. Missing-degree capacity

Every actual missing pair belongs to `K_D`, hence

```text
J subseteq K_D.                                       (9)
```

Combining (1) and (9):

```text
q_u+p_u=d_J(u)<=d_KD(u),                             (10)
```

so

```text
p_u<=d_KD(u)-q_u.                                    (11)
```

This is the **potential-pair capacity theorem**.

It is orientation-independent. No choice of directions, selected labels, or Hall flow can create a missing neighbour outside `K_D`.

## 5. Combined incoming capacity

The canonical bridge also gives

```text
p_u<=rho_u+b-a-1,                                    (12)
p_u<=b-1-q_u.                                        (13)
```

At fixed total excess `E`, [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md) supplies an additional bound. If every label has positive demand and `q_u>0`,

```text
p_u<=rho_u+floor(E/q_u)-1.                           (14)
```

With zero-demand labels, use the proved `k_*` correction from that note instead of (14).

Define `P_u(E,q,rho)` as the minimum of every applicable right-hand side (11)-(14). Then every legal branch satisfies

```text
P_u>=0 for every u,
Q=sum_u p_u=sum_u q_u<=sum_u P_u.                    (15)
```

Thus the integer deficit

```text
Def(E,q,rho)=sum_u P_u-Q                             (16)
```

must be nonnegative.

A negative value is a complete certificate excluding that source-degree profile. If every source-degree profile at every admissible `E` has negative deficit, the scalar state is excluded without orientation flow.

## 6. Selection-free source-degree universe

Every selected source-label incidence satisfies

```text
s_i<=rho_u,                                           (17)
```

and selected labels at a source are distinct. Together with `q_u+rho_u<=a`, every legal source degree obeys

```text
0<=q_u<=qmax(rho_u)
       :=min(a-rho_u, #{i:s_i<=rho_u}).               (18)
```

Consequently a deliberately enlarged but finite source-profile universe is

```text
q_u in [0,qmax(rho_u)],
sum_u q_u=S+E.                                        (19)
```

Enumerating (19) up to permutation of equal-`rho` vertices is enough for a quantifier-correct **pair-capacity exclusion**: every legal source profile is in this universe, but the universe does not assume that every enumerated profile has a legal selected-incidence realization.

Safe finite excess bounds include

```text
S+E<=sum_u qmax(rho_u),                              (20)
S+E<=sum_u rho_u+b(b-a-1),                           (21)
S+E<=binom(b,2).                                      (22)
```

## 7. Why this can be much stronger than aggregate capacity

The old incoming bounds (12)-(14) know only a vertex's own margins. Equation (11) imports the **distribution of all other `(q,c)` types** through (7).

In particular, a high-`q` source needs many potential missing neighbours with

```text
c_w>=q_u-1.                                           (23)
```

If the graph has a reservoir of low-`c` vertices, those vertices simply cannot support the missing degree needed by that high-load source. Conversely, a target with large `q_w` is unavailable to a source with small `c_u` because of the second inequality in (5).

This is the structural reason the theorem can close states that survive every aggregate total-capacity test.

## 8. Threshold corollaries

Define

```text
H(r)=#{w:c_w>=r},
L(r)=#{w:q_w<=r}.                                     (24)
```

Then (8) gives

```text
p_u+q_u
 <= min(H(q_u-1), L(c_u+1)) - 1,                     (25)
```

hence

```text
p_u
 <= min(H(q_u-1), L(c_u+1)) - 1 - q_u.               (26)
```

The first half alone gives the especially transparent high-load scarcity bound

```text
p_u+q_u<=H(q_u-1)-1.                                 (27)
```

These scalar threshold forms are weaker than exact (7) but may be better suited to symbolic all-order arguments.

## 9. Relation to orientation Hall flow

The logical hierarchy is

```text
directed orientation compatibility D
        =>
potential-pair graph K_D
        =>
pointwise missing-degree capacity (11)
        =>
aggregate incoming deficit test (15)
        =>
[if still needed] pair-choice Hall flow
        =>
[if still needed] target-capacity Hall flow.          (28)
```

The 13518/13519 closures stop at (15). This suggests that future frontier scans should apply potential-pair capacity before any max-flow computation.

## 10. Certificates

For a fixed `(E,q,rho)` profile, a compact exact certificate consists of

```text
q,
rho,
c=q+rho,
d_KD from (7),
all applicable incoming caps,
P,
sum P-Q.                                              (29)
```

All quantities are integers. No floating-point solver, timeout, or unsuccessful orientation search is involved.

## Trust boundary

The potential-pair criterion and degree calculation are elementary consequences of the directed compatibility conditions (2). Their Murty-Simon application inherits the trust boundary of the canonical graph-to-constraint bridge, especially the supplement-forcing and companion endpoint implications used to prove (2). Passing the pair-capacity test does not assert graph feasibility. External mathematical review and independent reproduction remain open.
