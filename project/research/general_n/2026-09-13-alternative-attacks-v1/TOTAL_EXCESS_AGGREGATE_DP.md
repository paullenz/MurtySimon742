# Aggregate total-excess source-capacity DP

13 September 2026. **Candidate general projection inside the canonical selected/residual bridge. External mathematical review remains OPEN.**

This note turns [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md) into a polynomial state-level screen. It does not enumerate complete `q`-vectors. Instead it computes the least incoming-capacity penalty compatible with a required total selected degree `Q=S+E`.

## 1. Universal incoming budget

Put

```text
D=b-a-1,
R=sum_u rho_u.
```

The canonical incoming inequality gives

```text
p_u<=rho_u+D.                                         (1)
```

Hence before using any source degree information,

```text
sum_u p_u <= U:=R+bD.                                (2)
```

But

```text
sum_u p_u=sum_u q_u=Q.                               (3)
```

## 2. Source-degree dependent cap

For a candidate source degree `q` at a vertex of residual degree `rho`, combine:

```text
p<=rho+D,                                             (4)
p<=b-1-q.                                             (5)
```

For `q>0`, let

```text
z=#{i:s_i=0},
k*=min(z,q,E).                                        (6)
```

If `q>k*`, [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md) adds

```text
p<=rho+floor((E-k*)/(q-k*))-1.                       (7)
```

If `q<=k*`, no additional total-excess cap is asserted.

Let

```text
P_E(rho,q)                                             (8)
```

be the minimum of the applicable right sides (4),(5),(7). If it is negative, that source-degree choice is impossible.

Relative to the universal allowance `rho+D`, define the nonnegative penalty

```text
r_E(rho,q)=(rho+D)-P_E(rho,q).                        (9)
```

For `q=0`, only (4)-(5) are used.

Then every legal branch satisfies

```text
Q=sum p
 <= U-sum_u r_E(rho_u,q_u).                          (10)
```

Equivalently,

```text
sum_u r_E(rho_u,q_u) <= U-Q.                         (11)
```

## 3. Source-degree range

Every source degree also satisfies

```text
q_u<=a-rho_u.                                         (12)
```

Selected-edge demand compatibility supplies the further selection-free bound

```text
q_u<=#{i:s_i<=rho_u}.                                 (13)
```

Thus define

```text
qmax(rho)=min(a-rho, #{i:s_i<=rho}).                  (14)
```

No individual selected geometry is fixed by (14).

## 4. Nested base-demand prefix constraints

Order sources by nondecreasing `rho`. After all source classes with residual degree at most `R0` have been processed, every label with

```text
s_i>R0                                                 (15)
```

must place all of its base `s_i` incidences on the unprocessed higher-rho sources. Therefore the already-used source degree is at most

```text
Q - H(R0),
H(R0)=sum_{i:s_i>R0}s_i.                              (16)
```

These are nested exact necessary constraints and can be imposed during the dynamic programme.

## 5. Dynamic programme

For fixed excess `E`, put

```text
Q=S+E.                                                 (17)
```

Process source classes in nondecreasing `rho`. Let

```text
dp[j]
```

be the minimum total penalty (9) among processed sources whose selected degrees sum to `j`. Transition each source through

```text
q=0,...,qmax(rho)                                     (18)
```

using cost `r_E(rho,q)`, discarding impossible `q` choices and enforcing (16) at each completed rho class.

Let

```text
Rmin(E)=dp[Q].                                         (19)
```

If `Q` is unreachable, set `Rmin(E)=+infinity`.

Then every legal branch necessarily satisfies

```text
Rmin(E) <= U-Q.                                       (20)
```

Thus

> **Aggregate total-excess exclusion.** If `Rmin(E)>U-Q`, the entire excess layer `E` is impossible, without enumerating complete source profiles.

If this happens for every admissible `E`, the scalar state is excluded under the retained canonical conditions.

## 6. Admissible excess range

A safe finite upper range is supplied by

```text
Q<=sum_u qmax(rho_u),                                 (21)
Q<=U,                                                  (22)
Q<=binom(b,2),                                        (23)
```

because selected missing edges are distinct unordered `B`-pairs. Therefore it is enough for this DP screen to check

```text
S<=Q<=min(sum qmax,U,binom(b,2)).                     (24)
```

A stronger scanner may replace (24) by any independently justified incoming or incidence bound.

## 7. What the DP retains and discards

Retained exactly at this level:

- total selected degree `Q=S+E`;
- residual-degree multiset `rho`;
- source degree bounds `q+rho<=a`;
- demand-compatible source degree count (13);
- nested base-demand placement (16);
- simple missing-degree cap `p+q<=b-1`;
- universal incoming cap;
- total-excess source cap.

Discarded at this level:

- the directed source-target compatibility relation;
- unordered-pair competition;
- exact selected-incidence Hall cuts beyond the nested base-demand prefixes;
- individual excess profiles;
- graph-level shared-residual geometry.

Therefore survival is only triage. Failure, however, is a valid integer certificate under the stated structural hypotheses.

## 8. Certificate

For an excluded excess layer record

```text
E,Q,U,U-Q,
qmax by rho class,
Rmin(E),
```

and the final DP table or its hash. All arithmetic is integral and independently replayable.

## Trust boundary

The DP is elementary finite optimisation once the canonical incoming/simple bounds, selected-edge demand compatibility and total-excess source cap are accepted. Its Murty-Simon application inherits the trust boundary of those lemmas. External mathematical review and independent computational reproduction remain open.
