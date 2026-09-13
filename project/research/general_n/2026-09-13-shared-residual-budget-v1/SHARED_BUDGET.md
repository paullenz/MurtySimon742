# Shared residual budgets and a balance-or-concentration alternative

13 September 2026. **Candidate general hand arguments. External mathematical
review and novelty assessment remain OPEN.** The finite application below
concerns fixed selected sets, not whole scalar states or graphs.

## 1. Canonical data and shared residual degrees

Use the [canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
For a B-source u, write S_u for its selected A-labels, q_u=|S_u|,
rho_u for its residual degree and p_u for its incoming selected-pair count.
For a label i, write x_i for its selected degree and R_i for its residual
degree. Put Q=sum q_u=sum x_i and r=sum rho_u=sum R_i. The bridge gives

```text
sum_u p_u = Q,
0 <= p_u <= h_u := min(rho_u+b-a-1, b-1-q_u),
p_u <= R_i+x_i-q_u                 for every i in S_u.       (1)
```

The same R_i occurs in every source inequality using i. Maximizing each
source independently discards this common budget.

In particular, R_i>=L_i, where

```text
L_i = max({0} union {q_u-x_i : i in S_u}).                    (2)
```

Also R_i<=b-x_i, because residual and selected cross-edges are disjoint.
Further upper bounds follow when C=H[A] has no isolated vertex. The bridge
proves this under t>0 and b>a-1-t; then d_i<=a-2. Use the **actual canonical
demands** s_i=max(0,d_i-R_i), not an arbitrarily trimmed demand vector.
Writing E=sum s_i-r-2t gives

```text
E = sum_(s_i=0) (R_i-d_i) >= 0.
```

Indeed sum d_i=2(r+t), and positive demands satisfy d_i=R_i+s_i.
Consequently valid upper bounds are

```text
U_i = min(b-x_i, a-2-s_i)         if s_i>0,
U_i = min(b-x_i, a-2+E)           if s_i=0.                   (3)
```

The zero-demand formula deliberately allows R_i>d_i. Replacing it by
R_i<=a-2 without checking E would be unjustified. The source definitions
in the frozen N34/N35 pool use actual demands, so (3) applies to that pool.
The general results below accept any correctly justified L,U; they do not
depend on (3) specifically.

## 2. Elementary weighted endpoint bound

Choose nonnegative rational weights alpha_(u,i) on selected incidences and
beta_u on sources, with

```text
beta_u + sum_(i in S_u) alpha_(u,i) >= 1  for every u.
```

Put lambda_i=sum_(u:i in S_u) alpha_(u,i). Multiplying (1), using p_u>=0,
and summing gives

```text
Q <= sum_u beta_u h_u
     + sum_(u,i) alpha_(u,i)(x_i-q_u)
     + sum_i lambda_i R_i.                                  (4)
```

For any prices v_i, define the shared-budget support function

```text
B(v) = max { sum_i v_i z_i : L_i<=z_i<=U_i, sum_i z_i=r }.   (5)
```

It is exactly computed by starting at z=L and assigning the remaining
r-sum L units to labels in descending price order, up to their upper
bounds. To prove optimality, move a unit from a lower-priced unsaturated
label to a higher-priced label whenever possible; this never reduces the
objective. Integer bounds and total give an integer maximizing vector,
so the same maximum holds for the continuous box relaxation.

Thus the right side of (4) is at most its first two terms plus B(lambda).
A strict failure is a directly checkable fixed-selected-pattern obstruction.
No numerical optimization status is needed to accept that certificate.

## 3. A short balanced-cover consequence

Let M be the number of sources with q_u>0 and c the number of labels with
x_i>0. Assume Q>0. Put H0=sum_(q_u=0) h_u.

Suppose the selected incidence family admits nonnegative weights alpha with

```text
sum_(i in S_u) alpha_(u,i) = 1     for each active source u,
sum_u alpha_(u,i) = M/c            for each used label i.    (6)
```

This means each active source distributes one unit among its selected
labels and all used labels receive equal total weight. Apply (4) with
beta=0 on active sources and beta=1 on empty sources. Since
sum_(active u) q_u=Q and sum_(used i) x_i=Q, the result is

```text
Q <= H0 - Q + (M/c)(Q + sum_(used i) R_i)
  <= H0 - Q + (M/c)(Q+r).
```

Therefore every such realization must satisfy the general inequality

```text
(2c-M)Q <= c H0 + M r.                                    (7)
```

This conclusion uses only endpoint load, incoming capacity and a balanced
cover of the actual selected incidences. It does not require the pair
lemma, finite-order enumeration, positive surplus or the upper bounds (3).
It remains conditional on the selected-incidence structure (6).

### If balance fails, a concentrated label set exists

There is an exact alternative to (6): some set I of used labels contains
all the selected labels of more than (M/c)|I| active sources.

To see this, construct an integer flow network. Give each active source
capacity c from a new starting vertex; connect it to its selected labels
with capacity cM+1; give each used label capacity M to a new terminal
vertex. Total required flow is cM. A full flow, divided by c, gives (6).
If no full flow exists, the vertices reachable by residual augmenting
paths determine a cut. No source-to-label edge can cross a deficient cut,
because its capacity exceeds cM. Hence if T is its reachable source set
and I its reachable label set, every S_u for u in T lies inside I and

```text
c(M-|T|)+M|I| < cM,
```

so c|T|>M|I|. Conversely such a family cannot satisfy (6), by counting the
mass it must send into I. The augmenting-path proof also gives integer
certificates of either outcome.

Combining this with (7): **if (2c-M)Q>cH0+Mr, every viable selected geometry
must have such a concentration witness.** This is an all-order structural
alternative, not an unconditional density theorem.

## 4. Pair deficits with shared residual budgets

For fixed S use [PAIR_OVERLAP.md](../2026-09-13-constraint-respecting-cross-v1/PAIR_OVERLAP.md):

```text
M_ij = max({q_u-1 : i,j in S_u} union {0}),
c_ij = number of sources selecting both i and j,
D_ij = max(0,M_ij-c_ij).
```

For nonnegative pair weights w_ij, let f_u^w(R) be the weighted number of
positive-deficit pairs contained in S_u union R that are not entirely
selected at u. An actual residual placement satisfies

```text
sum_(i<j) w_ij D_ij <= sum_u f_u^w(R_u).                    (8)
```

Choose arbitrary nonnegative selected-incidence weights alpha, arbitrary
prices v_i and an arbitrary rational incoming multiplier mu. Define

```text
A_u = sum_(i in S_u) alpha_(u,i),
lambda_i = sum_u alpha_(u,i),
K = sum_(u,i) alpha_(u,i)(x_i-q_u),
J = sum_u h_u max(0,mu-A_u),
C_u = max_(R subset A\S_u, |R|=rho_u)
        [f_u^w(R) + sum_(i in R)(lambda_i-v_i)].
```

Then every actual realization satisfies the candidate general inequality

```text
sum_(i<j) w_ij D_ij + mu Q <= sum_u C_u + B(v) + K + J.     (9)
```

Proof: weighted endpoint load gives sum A_u p_u<=sum lambda_i R_i+K.
Also sum A_u p_u>=mu Q-J, since 0<=p_u<=h_u and sum p_u=Q.
Add (8), subtract sum v_i R_i inside the source sums, bound each actual
row by C_u, and bound the remaining price sum by B(v). This proves (9).
No assumption of independence between sources is made. Taking separate
maxima is an upper relaxation, compensated here by a shared label budget.

When w=0 the bound is a residual-placement/endpoint control. Nonzero w
retains pair identities. With alpha=0, mu=0 and v=0 it reduces to weighted
local residual cover, including the earlier unweighted bound.

For fixed finite input, rational weights plus exact enumeration of the
local maxima give a certificate. Discovery uses linear optimization;
acceptance recomputes (9) exactly, without trusting solver feasibility,
infeasibility, status or dual tolerances.

## 5. Limits of the application

All finite tests in this checkpoint hold the selected geometry fixed to
the previous 4,584 saved witnesses after their recorded pair repairs.
They allow p to vary. The original saved p vectors were scalar transport
witnesses and fail shared endpoint accounting; fixing them would be an
unfairly strong comparison.

A rejected geometry can belong to a scalar state with another viable
geometry. Even a passing rational configuration witness is only a convex
mixture of residual rows: it does not select one simultaneous integer
placement, route all obligations, realize H[A] or construct a D2C graph.
No whole-state exclusion or change to the N34/N35 fixed-order ledgers is
claimed. External review and novelty remain open.
