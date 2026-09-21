# Session handoff — independent #742 strip attack, focused session 1

## Material progress

1. **Strict threshold improvement.**  The profile scalar certificate sharpens
   from `5/64` to `121/1569`.  Exact degree assembly gives a tradeoff ladder,
   including `Delta>=88n/151` for `n>=149` and the near-scalar-ceiling
   `Delta>=39n/67` for `n>=4681`.  These are candidate results conditional on
   the inherited graph-to-profile spine and preserved `7/12` candidate.
2. **First obstruction isolated.**  The scalar ceiling was independently
   rederived and then strengthened into an exact rational plateau at demand
   height `1/4`, `b/a=139/100`.  It sits above the Turan-side surplus and
   survives threshold capacity, full selected-incidence Hall, pair orientation,
   pair uniqueness, and simultaneous disjoint selected/residual incidence
   graphicality.
3. **Graph-realizability rigidity.**  Physical selected-source identity gives
   the signature union theorem
   `|union_{i in N_F(j)} X_i|<=C_j` and a global second-moment/codegree
   inequality.  In the plateau band this forces average co-selected-pair
   F-codegree `>0.2484a-0.997`; asymptotically more than 21.7% of selected pair
   occurrences, representing at least `0.00351a^2` distinct pairs, have
   F-codegree at least `a/5`.
4. **Trust-boundary replay.**  The shared graph-to-demand and
   threshold-capacity spine was independently rederived.  No blocker was
   found; the delicate supplement step is valid only through an explicit
   residual-or-selected dichotomy.

All results are internal candidate mathematics.  Exact checkers are green;
external mathematical review remains open.

## Exact next move

Attack the positive-density high-codegree cluster from raw criticality.  For a
co-selected pair `(i,k)` with `c_F(i,k)>=a/5`, retain the common physical
source `u`, its supplement pairs, and the containment

```text
N_F(i) union N_F(k) subset N_u=S_u disjoint-union R_u.
```

Derive either:

1. an injection charging such pairs/common neighbours to distinct physical
   source--supplement obligations; or
2. a bounded cluster/blow-up classification for the selected signatures.

The target quantitative contradiction is to upper-bound the number of
distinct co-selected pairs with F-codegree at least `a/5` below
`(0.00351-o(1))a^2`.  Do not return to scalar minorant optimization: `39/67`
is already within about `2.4e-5` of the scalar ceiling, and the rational
plateau proves that Hall/profile marginals alone cannot reach `1/2`.

