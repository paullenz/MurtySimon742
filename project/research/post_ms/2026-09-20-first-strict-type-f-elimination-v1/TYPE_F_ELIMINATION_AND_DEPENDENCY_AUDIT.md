# First-strict funnel: complete Type-F elimination and dependency audit

Date: 2026-09-20

Status: **upstream internal correction / structural strengthening**. This note catches an omitted matched-neighbour check in the Type-F arm of the preserved first-strict dichotomy. The dichotomy statement itself remains correct as a local orientation classification, but its Type-F alternative is globally unrealizable once the full tight code is reinserted.

This finding supersedes `TYPE_F_SUPPORT_GAP_AND_M2_EVENTUAL_CLOSURE.md` within the same session: the earlier support-gap lemma was correct but unnecessarily weak.

## 1. Binding audit boundary

The 20 September daily adversarial audit remains binding. In particular, the raw meaning of a tight code has now been independently re-derived in `SAME_CODE_RAW_CRITICALITY_AUDIT.md`: every coded vertex selects one matched endpoint in each of the p tight fibres, and code agreement in a coordinate gives a literal common matched neighbour.

The present argument uses only that audited code semantics, outside-code complementation and the already-preserved first-strict funnel relation. It uses no finite scan, pair capacity, source-tuple counting or downstream m=1/m=2 theorem.

## 2. Exact Type-F data

Let `x in X\{a_0}` be a Type-F buffer neighbour with outside witness `z`.

The first-strict theorem gives:

1. `I_x={i}` for one coordinate `i in S_0`;
2. `c(z)=bar c(x)`;
3. `za_0` is a nonedge;
4. the forward funnel orientation is the literal singleton

   `N(z) cap N(a_0)={q_i}`.                             `(F-FUNNEL)`

Because x agrees with d **only** at i, the complementary code z differs from d **only** at i. Thus

> `S_z={i}`.                                             `(Z-SUPPORT)`

Because `a_0` has code neither `d` nor `bar d`, both `S_0` and

> `I_0=[p]\S_0`

are nonempty.

## 3. The omitted extra matched common neighbour

Choose any coordinate `j in I_0`. Since `i in S_0`, necessarily `j!=i`.

At j:

- `a_0` agrees with d, because `j in I_0`;
- z also agrees with d, because `S_z={i}` and `j!=i`.

Therefore z and `a_0` are both adjacent to the same d-selected tight matched endpoint in fibre j.

That matched endpoint is a common neighbour of z and `a_0` distinct from `q_i`. Hence

`|N(z) cap N(a_0)|>=2`,

contradicting `(F-FUNNEL)`.

Therefore:

> **Type F is impossible throughout the first-strict unloaded branch.** `(NO-F)`

The proof is valid for every admissible p; admissibility itself already forces `p>=2` because both `S_0` and `I_0` are nonempty.

## 4. Corrected first-strict normal form

Every buffer neighbour is therefore Type R. For every `x in X'=X\{a_0}`:

- `empty != I_x subseteq I_0`;
- `S_0 subseteq S_x`;
- `xa_0` is a nonedge;
- every valid outside witness z for bx is adjacent to `a_0`;
- for each `i in I_x`,
  `N(q_i) cap N(a_0)={z}`.

Thus `a_0` is isolated from all of `X'`:

> `d_X(a_0)=0`.                                         `(A0-X0)`

Group X' by tight code C. The fixed-foot identity at any `i in I_C` makes the physical outside witness **graph-fixed for the whole code class**. Conversely every physical vertex of `U_o` certifies at least one buffer edge by the raw reverse-fan theorem. Different X-codes have different complementary witness codes.

Hence:

> each X'-code class has exactly one physical eligible outside witness;
>
> every physical outside vertex is one of those class witnesses;
>
> `omega=|U_o|=h`, where h is the number of distinct X'-codes;
>
> the maximal representative number is `m=h=omega`.     `(R-CLASS-BIJECTION)`

The distinct agreement blocks `I_C` are pairwise disjoint nonempty subsets of `I_0`. Therefore

> `m=omega=h <= |I_0|=p-|S_0| <= p-1`.                 `(M<=P-1)`

This is a graph-level coordinate bound, not a selected-incidence capacity estimate.

## 5. Dependency audit: what becomes vacuous or superseded

The following same-day branches all assumed at least one realizable Type-F head and are therefore no longer live realizability branches:

- the Type-F side of `FIRST_STRICT_FUNNEL_RESERVOIR.md`;
- the all-F one-witness polarization and every later maximal-m1 all-F calculation;
- the complementary F/R maximal-m2 normal form and all F/R reservoir / raw-edge descendants;
- `M2_FR_RESERVOIR.md`;
- `M2_FR_RAW_EDGE_COLLAPSE.md`;
- `M2_FR_EXACT_HALL_CLOSURE.md`;
- the p=2 F/R and all-F analyses in `M2_P2_REMAINDER.md`;
- `TYPE_F_SUPPORT_GAP_AND_M2_EVENTUAL_CLOSURE.md` except for its historical role in exposing the stronger contradiction.

Their conditional algebra need not be deleted; it is preserved as mathematics on an empty parent hypothesis. They must not be cited as the reason those branches close once `(NO-F)` is independently audited.

The following remain structurally relevant:

- the unique-hole first-strict setup itself;
- all Type-R fixed-foot consequences;
- disjoint agreement blocks for distinct R-code classes;
- raw reverse-fan coverage of every physical outside vertex;
- exact physical Y-price from `Y--U=empty`;
- pair-local `Ccap_P/(ONE-P)/(CROWD)`;
- the raw same-code theorem and ordered `(source,witness)` injectivity;
- the graph-level `X_3` negative control and zero-positive-rigid-cut caveat.

## 6. Immediate consequences for m=1 and m=2

For `m=1`, `(R-CLASS-BIJECTION)` gives one R-code class and one physical witness. The previously preserved all-R one-witness raw-criticality closure therefore closes maximal m=1 directly; no all-F arm exists.

For `m=2`, there are exactly two R-code classes with two disjoint nonempty blocks in `I_0` and exactly two physical outside witnesses. In particular `p>=3`; the p=2 branch is impossible because `|I_0|=1` cannot contain two disjoint nonempty blocks.

The earlier maximal-m2 large-X corrected bulk argument can now be read more strongly: any conclusion forcing an F/R split is simply a contradiction with `(NO-F)`. Thus large-X m=2 is empty upstream, while the only possible m=2 tail has two singleton R-code classes (`x=3`).

The independently derived bounded-tail inequalities in `M2_X3_BOUNDED_TAIL.md` remain safe as necessary conditions for this x=3 tail and give `p<=8`; here `omega=m=2` exactly, so in fact

`u=k+3<=6`, `y<=p-1<=7`,

and

> `n=1+(3+y)+(2p+u) <=33`.                              `(M2-N33)`

Therefore maximal m=2 is an order-at-most-33 phenomenon under the corrected all-R-only first-strict structure.

## 7. Highest-value corrected frontier

The live unbounded first-strict branch is now much cleaner:

- **all buffer neighbours are Type R**;
- `m=omega=h` is simultaneously the maximal witness number, physical outside-reservoir size and number of X'-code classes;
- `m<=p-1`;
- the m distinct agreement blocks are disjoint nonempty subsets of `I_0`;
- each block/class has one graph-fixed complementary outside witness;
- `a_0` is isolated from X'.

The next structural question is no longer an F/R case split. It is whether a code class can contain more than one X'-head. If bulk R-classes can be excluded from raw matched-edge criticality, then `x-1=m=omega`; that would reduce the entire unbounded first-strict problem to a disjoint-block / one-head-per-block geometry and make the rooted residual ledger substantially more explicit.

That bulk-R exclusion is the highest-value next hand target.