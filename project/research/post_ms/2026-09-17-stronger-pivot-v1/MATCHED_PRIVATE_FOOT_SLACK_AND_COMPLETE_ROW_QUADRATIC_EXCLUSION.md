# Matched private-foot slack transfer and complete-row quadratic exclusion

18 September 2026. Research directed by Paul Lenz; derivation and finite regression by ChatGPT/Geeps.

**Status: internal candidate structural theorems; not externally reviewed.** This note continues `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`, `GLOBAL_SLACK_DEFECT_CRITERION.md`, `COMPLETE_ROW_CLIQUE_PRIVATE_FEET.md`, and `COMPLETE_ROW_GLOBAL_NORMAL_FORM.md`.

The point of this unit is to do the A-side pricing that the previous handoff identified as the highest-value next step. The key observation is that a private foot for a critical edge whose **target lies in a tight fibre** inherits degree slack from the target's tight mate. In the complete-row normal form, the mandatory singleton/co-singleton support amplifies this from one unit per private foot to one unit per matched-clique edge certified by that foot.

Throughout, fix a maximum-degree root `v`, tight pairs

`P_i={q_i,q_i'}`, `i=1,...,p`,

unmatched set `U`, `u=|U|`, and

`b=2p+u`, `lambda=2b-n`.

Every vertex of `A union U` chooses exactly one endpoint from each tight pair.

---

## 1. Matched-target private-foot slack transfer

Let `s,t in P` be adjacent matched-core vertices in distinct tight fibres. Let `t'` be the tight mate of `t`. Suppose an A-vertex `h` certifies criticality of the edge `st` from source `s` toward target `t`, so

`h~s`, `h not~t`,

and

`N(h) intersect N(t)={s}`.                                      `(PF1)`

Because every `z in A union U` chooses exactly one endpoint of the tight pair `{t,t'}`, condition `(PF1)` implies

`z~h  ==>  z~t'`

for every `z in (A union U)\{h}`. Also `h~t'`, because `h not~t` and `h` chooses one endpoint of the fibre. Therefore

> `N(h) intersect (A union U) subseteq (N(t') intersect (A union U))\{h}`.   `(PF2)`

Now compare degrees. The A-vertex `h` has exactly `p` neighbours in `P`, while `t'` has the root `v` plus exactly `p-1` neighbours in the other tight fibres. Hence

`d(h)=p+|N(h) intersect (A union U)|`,

`d(t')=p+|N(t') intersect (A union U)|`.

Using `(PF2)`,

`d(h)<=d(t')-1`.

Equivalently:

> **MATCHED-TARGET PRIVATE-FOOT SLACK TRANSFER.**
>
> `epsilon_h >= epsilon_t' + 1`.                               `(PF3)`

In particular every such A-private foot has strictly positive maximum-degree slack.

This lemma is not special to the zero signing or to a complete unmatched row. It is valid anywhere the partial Boolean tight-pair normal form applies.

---

## 2. Critical clique edges can be grouped by private foot

Now enter the complete-row global normal form from `COMPLETE_ROW_GLOBAL_NORMAL_FORM.md`. After switching,

`G[P]=Q dotcup Q' = K_p dotcup K_p`,

where

`Q={q_1,...,q_p}`, `Q'={q_1',...,q_p'}`.

The matched orientation-code graph is also two `K_p` components. Consequently A realises at least

- `p-1` singleton code classes `{i}`;
- `p-1` co-singleton code classes `[p]\{i}`.

Take every physical edge of the clique `Q`. By D2C criticality and the rooted clique-private-foot theorem, choose one valid orientation of that edge and one A-private foot certifying it. A single private foot may certify several outgoing edges from the same clique source. Group the chosen oriented edges by the actual foot used.

For a Q-foot `h` private to source `q_i`, let

`T(h) subseteq [p]\{i}`

be the set of target coordinates of the chosen Q-edges certified by `h`, and put

`t(h)=|T(h)|`.

Its Boolean code is the co-singleton

`c(h)=[p]\{i}`.

For every target `j in T(h)`, private-foot criticality implies that `h` is nonadjacent to every vertex of `A union U` whose `j`-th code bit is zero. Thus every A/U-neighbour of `h` has bit one on **all** coordinates of `T(h)`.

Let

`H_j^1={z in A union U:c_j(z)=1}`,

`H_T^1=intersect_{j in T} H_j^1`.

Then

`N(h) intersect (A union U) subseteq H_T^1\{h}`.                `(PF4)`

For every coordinate `j`, degree accounting at `q_j'` gives

`|H_j^1|=p+u-epsilon_{q_j'}`.                                  `(PF5)`

---

## 3. Sphere amplification: one unit of slack per certified clique edge

We now use the mandatory singleton/co-singleton support, not raw nonneighbour counting.

### Q-side

Suppose first that `t=t(h)>=2`. Since at most one singleton code is absent from A-support, choose a target

`j_0 in T(h)`

for which the singleton code `{j_0}` is realised in A.

The singleton `{j_0}` lies in `H_{j_0}^1` but outside `H_T^1`.

For each other target `k in T(h)\{j_0}`, the co-singleton `[p]\{k}` also lies in `H_{j_0}^1` but outside `H_T^1`. At most one co-singleton code is absent from A-support, so at least `t-2` of these additional exclusions are realised.

Therefore

`|H_{j_0}^1\H_T^1|>=t-1`,

and by `(PF5)`

`|H_T^1|<=p+u-epsilon_{q_{j_0}'}-(t-1)`.                       `(PF6)`

Using `(PF4)`,

`d(h)<=p+|H_T^1|-1`,

so

> `epsilon_h>=t+epsilon_{q_{j_0}'}>=t`.                         `(PF7)`

For `t=1`, `(PF7)` follows directly from `(PF3)`.

Thus every Q-private foot pays at least the number of chosen Q-edges assigned to it.

### Q'-side

The argument is symmetric. A Q'-private foot has singleton code `{i}`. If it certifies a target set `T` of size at least two, choose `j_0 in T` whose **co-singleton** code is realised. That co-singleton, together with all but at most one of the singleton codes for the remaining targets, gives `t-1` distinct exclusions from the all-zero target intersection. Hence again

> `epsilon_h>=t(h)`                                               `(PF8)`

for every Q'-private foot.

We record the structural statement:

> **EDGE-BY-EDGE CLIQUE SLACK THEOREM.** In the complete-row global normal form with `p>=3`, if a private A-foot certifies `t` selected critical edges from one source of `Q` or `Q'`, then its maximum-degree slack is at least `t`.

The key point is that witness reuse is **not free**: reusing one foot on several clique edges increases the same foot's degree deficit by at least the number of edges reused.

---

## 4. Quadratic A-side slack from the two matched cliques

Every edge of `Q=K_p` is assigned to exactly one chosen critical orientation and one private foot. Therefore, summing `(PF7)` over the distinct Q-feet,

`sum_{h in H_Q} epsilon_h >= sum_h t(h)=binom(p,2)`.             `(Q1)`

Similarly

`sum_{g in H_Q'} epsilon_g >= binom(p,2)`.                      `(Q2)`

For `p>=3`, Q-feet have co-singleton codes while Q'-feet have singleton codes, so the two foot populations are disjoint.

Consequently:

> **COMPLETE-ROW QUADRATIC A-SLACK THEOREM.**
>
> `L_A >= p(p-1)`.                                               `(QAS)`

This replaces the previous merely linear private-foot floor `L_A>=2p-2` in the complete-row branch.

The theorem is a hand consequence of D2C criticality, the tight-pair Boolean normal form, and the exact two-clique orientation support. It is not a finite-scan extrapolation.

---

## 5. Direct second-extremal consequence

Recall the exact global slack criterion. Put

`c_lambda = ceil(lambda(lambda+2)/2)`.

In the near-full normal form,

`T=p(lambda+1)+E_U+L_A`,

and

`m<=M(n)` iff

`E_U+L_A >= S_req`,

where

> `S_req = p lambda + 3p + u lambda + 2u - c_lambda - 2`.        `(GS-C)`

If `m>M(n)`, the parity gap in the exact criterion gives the stronger upper bound

> `E_U+L_A <= S_req-2`.                                         `(GS-A)`

Since `E_U>=0` and `(QAS)` gives `L_A>=p(p-1)`, an above-threshold complete-row configuration is impossible whenever

`p(p-1)>=S_req-1`.

After rearrangement:

> **COMPLETE-ROW QUADRATIC EXCLUSION REGION.**
>
> If
>
> `(lambda+2)u <= p^2-(lambda+4)p+c_lambda+3`,                   `(QER)`
>
> then a near-full D2C graph containing a complete unmatched row satisfies
>
> `m<=M(n)`.

Thus any hypothetical above-`M(n)` complete-row configuration must lie outside the quadratic region `(QER)`.

Important near-balanced specialisations are:

- `lambda=-1`: above threshold requires
  `u >= p^2-3p+4`;
- `lambda=0`: above threshold requires
  `2u >= p^2-4p+4`;
- `lambda=1`: above threshold requires
  `3u >= p^2-5p+6`.

Equivalently, complete rows are excluded whenever

- `lambda=-1` and `u<=p^2-3p+3`;
- `lambda=0` and `2u<=p^2-4p+3`;
- `lambda=1` and `3u<=p^2-5p+5`.

For every fixed `lambda`, this eliminates every complete-row family with `u=O(p)` once `p` is sufficiently large. More generally it prices the cheap one-code row on the exact defect scale, not merely at support level.

---

## 6. Boundary information in the hardest lambda=-1 layer

At `lambda=-1`, `(QAS)` and the exact above-threshold inequality give

`m>M(n) ==> E_U+p(p-1) <= 2p+u-4`.                              `(B1)`

Hence

> `m>M(n) ==> E_U <= u-p^2+3p-4`.                               `(B2)`

In particular the right side must be nonnegative, recovering

`u>=p^2-3p+4`.

This is much stronger than the previous universal unmatched floor `E_U>=ceil(u/4)` whenever the tight matching is genuinely near-full. It says that the complete-row escape, if it exists at all, is pushed out of the linear-unmatched regime into a **quadratically large unmatched set**.

This is the principal structural gain of the unit.

---

## 7. Exact regression

Companion checker:

`check_matched_private_foot_slack_and_complete_row_quadratic_exclusion.py`.

It performs two independent finite checks.

1. For every `p=3,...,10`, every possible omitted singleton support class, every possible omitted co-singleton support class, every source coordinate, and every nonempty target subset, it verifies the support-exclusion count used in `(PF6)` on both Q and Q' sides.

   Total target/support configurations checked: `1,941,976`.

   Minimum support-exclusion margin: `0`.

   Failures: `0`.

2. For `3<=p<=100`, `1<=u<=200`, and every `-1<=lambda<=min(u+1,20)`, it verifies that `(QER)` is algebraically equivalent to the direct integer condition `p(p-1)>=S_req-1`.

   Arithmetic configurations checked: `414,442`.

   Failures: `0`.

These checks audit the finite combinatorial bookkeeping and integer rearrangement only. They do not replace the hand D2C/private-foot argument.

---

## 8. Strategic consequence

The previous live target was to convert explicit complete-row/private-foot populations into `L_A`. This note does so sharply:

`complete row  ==>  L_A>=p(p-1)`.

Accordingly, the complete-row one-code escape is no longer a serious near-full obstruction when the unmatched set is linear (or otherwise below the quadratic boundary) in the number of tight pairs.

The remaining cheap row `K_{p-1} dotcup K_1` still enters the complementary U--U antipode/fan machinery rather than this theorem. The next high-value step is therefore to seek an analogous **edge-by-edge A-slack payment for fan/private-hole or clique-plus-isolate rows**, or else use `(QER)` as the complete-row side of a dichotomy showing that every sufficiently near-full unmatched configuration is expensive.

The published 2024 `n=12,m=32` graph is untouched: it lies in the full-tight `u=0,p=4,r=0` branch and contains no unmatched complete row.

No all-order second-extremal theorem is claimed.
