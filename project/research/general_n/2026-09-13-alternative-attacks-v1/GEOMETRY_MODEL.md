# Geometry-quantified modelling route

13 September 2026. **Research model and hand-extraction programme. Solver statuses are exploratory unless replaced by exact certificates or hand proofs.**

## 1. Quantifier correction

The recent shared-budget continuation fixes one selected-incidence family `S_u` and then asks whether residual budgets, incoming loads and pair deficits can coexist. It excludes 4,487 of 4,584 stored patterns, but a rejected stored pattern does not exclude its scalar state because alternative selected geometries may exist.

The natural correction is to put the selected geometry **inside** the feasibility problem.

For a fixed scalar/margin input, introduce binary variables

```text
y_(u,i)=1  iff source u selects label i.
```

Then enforce the row and column margins, eligibility, incoming-load accounting and the strongest hand consequences simultaneously. This treats all selected-set arrangements with those margins at once.

## 2. Exact-demand interval core

When `x=s`, the new interval consequence in `SELECTION_FREE.md` is especially simple. Let

```text
q_u=sum_i y_(u,i),
C_i=R_i+x_i=d_i.
```

For every selected incidence:

```text
q_u+p_u <= C_i <= rho_u+q_u-1.            (2.1)
```

Together with

```text
sum_u p_u = Q,
sum_i C_i = r+Q,
sum_u y_(u,i)=s_i,
sum_i y_(u,i)=q_u,
s_i<=rho_u whenever y_(u,i)=1,
```

this forms an integer margin/interval realization problem. It is already strictly stronger than checking one stored geometry.

For `x>s`, use the general selected-excess inequality

```text
p_u-rho_u+1 <= x_i-s_i                    (2.2)
```

on every selected positive-demand incidence, together with its summed form. This makes the cost of moving away from exact demand explicit rather than treating extra selected degree as free slack.

## 3. Exploratory state-227 pilot

A first in-session integer model was built for N34 state 227. A broad formulation that also attempted simultaneous selected/residual placement reached the runtime limit without an incumbent. **No mathematical conclusion is drawn from that timeout.**

A reduced fixed-margin formulation then held the saved row margins `q` and `x=s` but allowed every eligible selected-incidence matrix. A numerical integer solver reported infeasibility. That status is also not accepted as proof.

The useful outcome was extraction of a short exact case argument. `MARGIN_CLASS_EXAMPLE.md` proves by hand that **every** selected geometry with those fixed margins is impossible. `verify_margin_example.py` replays only the finite arithmetic of that proof and does not trust an optimizer.

Thus the modelling route has already upgraded one result from

```text
one stored selected pattern is impossible
```

to

```text
one entire (q,x) selected-geometry fibre is impossible.
```

It is still not a whole scalar-state exclusion because alternative `q` and `x>s` choices remain.

## 4. Planned all-geometry hierarchy

The next models should be nested so that every negative result has a clear meaning:

### G1. Fixed q, fixed x, all selected sets

Use row/column margins plus (2.1)/(2.2). This is the level now hand-closed for state 227's saved margin class.

### G2. Variable q, fixed x=s

Allow row margins to vary while retaining exact demand. Active/inactive source status changes the incoming capacity, so it must be modelled explicitly. Any numerical exclusion must be converted to an exact dual/counting argument before it changes project status.

### G3. Variable q and x>=s

Introduce selected-degree excess `e_i=x_i-s_i`. Use (2.2), the summed excess-load inequality, total selected/incoming balance, and source/label capacities. The aim is to prove that escaping an exact-demand obstruction consumes more excess than the canonical ledger permits.

### G4. Add shared residual and pair structure

Only after the selected-geometry layer is controlled should the existing shared residual-budget, pair-deficit and exact compatible-destination machinery be added. This avoids paying the combinatorial cost of residual realization on geometries already impossible at the margin level.

## 5. Certificate strategy

The intended use of optimization is discovery, not acceptance.

- If a linear relaxation is infeasible, extract an exact rational dual and simplify it to a hand inequality.
- If an integer model is infeasible, search for a small branch/counting proof, a Hall obstruction, or a proof-producing finite certificate with an independent checker.
- If a model is feasible, preserve the witness and use it to falsify proposed strengthenings.
- Timeouts and solver noncompletion remain explicitly negative evidence only.

The state-227 proof is the desired pattern: computation suggests the obstruction; the repository retains a short human-checkable argument that no longer depends on the solver status.
