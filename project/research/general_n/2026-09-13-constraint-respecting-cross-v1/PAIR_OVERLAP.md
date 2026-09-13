# Pair-overlap projection from co-singleton traces

13 September 2026. **Candidate general hand lemmas.** External mathematical review and novelty assessment remain OPEN. This note continues the co-singleton trace argument from `CONTAINMENT_SPILL.md`. It derives necessary conditions for a fixed selected-set family; it does not exclude a whole scalar state unless every admissible selected-set family is covered.

## 1. Pair trace

Use the canonical notation

```text
S_u = selected A-labels at B-source u,
R_u = residual A-labels at u,
N_u = S_u union R_u,
q_u = |S_u|,
rho_u = |R_u|.
```

For each selected incidence `(u,i)`, let `w_i` be its actual B-side exception. Exact compatibility gives

```text
S_u \ N_(w_i) = {i},
S_(w_i) subset N_u,
```

and the `w_i` are distinct as `i` varies in `S_u`.

Fix a pair `{i,j} subset S_u`. Source `u` itself contains both labels, and every exception `w_h` with `h in S_u\{i,j}` also contains both. Hence the B-side common cross-degree

```text
d_ij := |{v in B : {i,j} subset N_v}|
```

satisfies

```text
d_ij >= q_u-1.                                      (1)
```

Define

```text
M_ij = max({q_u-1 : {i,j} subset S_u} union {0}).
```

Then every realization satisfies `d_ij>=M_ij`.

Summing over pairs gives the global pair moment

```text
sum_{i<j} M_ij <= sum_v binom(q_v+rho_v,2).          (2)
```

This is exactly the `k=2` member of the co-singleton moment hierarchy.

## 2. Separate what selected-selected pairs already supply

For a fixed selected-set family define

```text
c_ij = |{v in B : {i,j} subset S_v}|.
```

Those `c_ij` rows already contribute to `d_ij` without using residual labels. Therefore the remaining pair demand is

```text
D_ij = max(0, M_ij-c_ij).                             (3)
```

Every one of these remaining units must occur in a row where at least one of `i,j` is residual.

A coarse consequence is

```text
sum_{i<j} D_ij
    <= sum_v [q_v rho_v + binom(rho_v,2)].             (4)
```

The right side is exactly the number of unordered label-pair slots in the rows that use at least one residual incidence. This refines (2) whenever selected-selected pair occurrences are concentrated on the wrong label pairs.

## 3. Deficit graph and exact local residual-cover bound

Equation (4) still treats every residual-involving pair slot as equally useful. Exact pair labels give a stronger bound.

Form the **deficit graph** `F` on the A-labels:

```text
E(F) = {{i,j}: D_ij>0},
```

with edge demand `D_ij`.

For a source `v`, suppose its residual set were `R subset A\S_v` with `|R|=rho_v`. The row `N_v=S_v union R` can contribute at most one unit to each deficit edge, and it contributes only to deficit edges contained in `N_v` that are not already entirely selected at `v`. Define

```text
f_v(R)
  = |{{i,j} in E(F): {i,j} subset S_v union R,
                       {i,j} not subset S_v}|.
```

Let

```text
C_v(F,S_v,rho_v)
  = max_{R subset A\S_v, |R|=rho_v} f_v(R).           (5)
```

Then every actual residual realization satisfies the **local residual-cover inequality**

```text
sum_{i<j} D_ij
    <= sum_v C_v(F,S_v,rho_v).                         (6)
```

### Proof

For a deficit edge `{i,j}`, at least `D_ij` rows beyond the `c_ij` selected-selected rows must contain both labels, by (1)-(3). Every such extra row has at least one endpoint residual, so it is counted by `f_v(R_v)` for the actual residual set of that row. Summing these required units over deficit edges gives

```text
sum D_ij <= sum_v f_v(R_v).
```

For each row `f_v(R_v)<=C_v` by definition, proving (6).

No independence assumption between rows is used. Because the maxima in (5) are taken separately, (6) is deliberately generous: shared residual-label-degree constraints and exact destination assignments can only make realization harder.

Equivalently, if `e_F(X,Y)` denotes deficit edges across two disjoint label sets and `e_F(R)` those inside `R`, then

```text
C_v = max_{|R|=rho_v, R cap S_v=empty}
          [e_F(S_v,R)+e_F(R)].                         (7)
```

For the current `a=15` frontier this maximum is tiny enough to enumerate exactly, but (6) is a general combinatorial statement independent of those orders.

## 4. Relation between the three pair tests

For every fixed selected pattern,

```text
local residual-cover capacity
    <= total residual-involving pair capacity.
```

Thus (6) implies the coarse residual-deficit test (4), which in turn refines the raw total pair moment (2) after the actual selected-selected pair distribution is retained.

The improvement is conceptual as well as numerical: (6) knows **which pair deficits** remain and asks whether each source's limited residual set could cover enough of those particular edges.

## 5. Current finite reconnaissance and its scope

The complete scalar spill study supplies an exact-demand selected pattern for each of the 4,584 combined survivors. Applying (2) to those particular stored patterns initially rejects 23 of them. However, a deterministic degree-preserving two-source/two-label switch, preserving every `q_u`, every label degree `x_i=s_i`, source eligibility, transport data and spill data, repairs all 23 in at most three greedy switches. Therefore the global pair moment (2) adds **zero whole-state exclusions** on this witness study.

The local residual-cover test (6) is stronger on the repaired patterns. It rejects a nontrivial set of those particular selected realizations, sometimes by many units. These are **pattern exclusions only**. Degree-preserving search has already repaired several apparently difficult examples without changing the scalar profile; e.g. bounded searches found pair/local-cover passing realizations for N34 state 11236 and N35 state 430, while another difficult case reached a one-unit deficit.

Consequently no whole-state exclusion is claimed here. The exact counts for a frozen deterministic replay are generated by `check_pair_overlap.py`; search-assisted repairs beyond its frozen rule are preserved separately when promoted.

## 6. Why this is useful even if the current states can be repaired

The scalar spill study proved that every current survivor can hide inside some selected-degree vector. The pair deficit graph exposes the next missing information:

- **which labels are repeatedly selected together**;
- which of those pairs have already received selected-selected coverage;
- which precise pair deficits residual slots must realize;
- how much of that deficit graph each source can cover with only `rho_v` residual labels.

This is qualitatively closer to exact cross-neighbourhood realization than another scalar multiplier inequality. If all current states can still be repaired, the failed patterns and repairs reveal which pair designs are favoured. If some state cannot, (6) supplies a short checkable obstruction that does not depend on MILP infeasibility.

## 7. Next refinement

The natural follow-ups are:

1. quantify (6) over the admissible selected-set geometry of the most difficult states rather than a single stored witness;
2. incorporate residual-label degree budgets shared across rows, which (6) currently discards by maximizing each row independently;
3. if needed, repeat the same construction for triples: `M_T=max(q_u-2)` for `|T|=3`, subtract selected-only occurrences and bound how many positive-deficit triples each residual row can cover;
4. connect a surviving residual placement to the exact fixed-neighbourhood Hall routing criterion.

Any solver search used to discover a stronger cut remains exploratory until the resulting obstruction is independently checkable.
