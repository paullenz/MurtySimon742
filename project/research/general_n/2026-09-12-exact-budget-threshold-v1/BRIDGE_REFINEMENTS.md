# Exact budgets and tight heavy-label thresholds

12 September 2026. Research direction: Paul Lenz. Development and internal
audit: ChatGPT/Geeps. **Candidate universal bridge consequences; external review OPEN.**

All notation and graph implications come from the
[canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
These refinements require no solver and have no fixed-order restriction.

## 1. Exact demand-deficit identity

Write `r=sum_u rho_u=sum_i R_i`, `S=sum_i s_i`, and
`s_i=max(0,d_i-R_i)`. The exact degree ledger gives `sum_i d_i=2(r+t)`.
For a positive-demand label, `d_i-R_i=s_i`. For a zero-demand label,
`d_i-R_i=-(R_i-d_i)`, with `R_i-d_i>=0`. Consequently

`S-r-2t = sum_{i:s_i=0}(R_i-d_i)`.                         (1)

In particular:

- With no zero-demand labels, **r=S-2t exactly**.
- With exactly one zero-demand label, put `E=S-r-2t`. Its state must obey
  **d=R-E**, with `E>=0`; the other labels obey `d=R+s`.

This sharpens the conservative budget `r<=S-2t`. Retaining extra states in
earlier frontier expansions was safe; those expansions did not assert that
every retained state could realize the exact ledger. Formula (1) explains
their immediate removal and the correct treatment of a single zero demand.
With multiple zero demands, E is shared among them: do not impose the entire
deficit on each label.

## 2. Tight heavy-label subset lemma

Assume `t>0`, fix an integer `h>=2`, and put

`I={i:s_i>=h}`, `W=sum_{i in I}s_i`,

`Z={u:rho_u>=h}`, `z=|Z|`, `C_h(z)=[z(z-1)+h(h+1)]/2`.

If `W>0` and **W=C_h(z)**, then necessarily

`W-h(h+1) <= sum_{u in Z}(rho_u-1)`.                       (2)

Unlike the earlier total-demand lemma, this statement permits labels below
h, including zero demands. An immediate weaker consequence is

`b+2t <= h(h+1)+(S-W)`.                                   (3)

### Proof

Count **actual selected incidences whose labels lie in I**. Let `ell_u` be
their number from u. Every such source lies in Z. The canonical threshold
proof, with `J={u in Z:ell_u>h}` and `j=|J|`, gives

`W <= sum_Z ell_u <= (z-j)h+jz-j(j+1)/2 <= C_h(z)=W`.

Every inequality is therefore equality. Each heavy label has `x_i=s_i`,
because all of its selected incidences were counted and their total is W.
Every source in `Z\J` has `ell_u=h`; each source in J has `ell_u>h`.
Thus every source in Z has at least one selected **heavy** label.
The exact last slack is `(z-h-j)(z-h-j-1)/2`; hence the feasible j values
are `z-h` and `z-h-1`.

For any u in Z, choose a selected heavy label i. Its demand is positive,
and `x_i=s_i`, so endpoint load and source-degree forcing imply

`q_u+p_u <= R_i+x_i=d_i <= rho_u+q_u-1`.

Therefore `p_u<=rho_u-1`. Notice that q_u counts *all* selected incidences:
we have not assumed `q_u=ell_u`, nor excluded light-label incidences at u.

The threshold proof also sends every heavy selected arc from J back into Z.
These distinct arcs give

`sum_Z p_u >= sum_J ell_u = W-(z-j)h >= W-h(h+1)`.

Combining the incoming lower bound with `p_u<=rho_u-1` proves (2).
Residual activity on all b sources gives `sum_Z(rho_u-1)<=r-b`.
Using `W=S-(S-W)>=r+2t-(S-W)` proves (3). QED.

When every demand is at least h, W=S and (3) recovers the earlier lemma.
The essential generalization is the use of heavy outdegrees ell_u throughout
the capacity equality, while retaining total q_u in the endpoint calculation.

## 3. Exact-budget potential envelopes

Let `F(s,d,h)` be nondecreasing in its first two arguments and nonincreasing
in h. On a selected incidence ui the bridge gives

`s_i<=rho_u`, `d_i<=rho_u+q_u-1`, `R_i+x_i>=q_u+p_u`.

Therefore

`sum_i x_i F(s_i,d_i,R_i+x_i)`
`<= sum_u q_u F(rho_u,rho_u+q_u-1,q_u+p_u)`.                (4)

For `j>=1`, supplement forcing gives

`T_j=sum_{q_u>=j+1}q_u-sum_{rho_u+q_u>=j}p_u<=0`.          (5)

Indeed, each arc counted in the first sum enters a source eligible for the
second; distinct arcs are counted in that source's incoming degree p_u.

Choose arbitrary real multipliers lambda, c, mu and nonnegative tau_j.
Suppose every admissible label and source option satisfies

`ell_s <= lambda R+c x+x F(s,d,R+x)`,

`sigma_rho <= mu(q-p)-c q+sum_j tau_j`
`*[q 1(q>=j+1)-p 1(rho+q>=j)]-q F(rho,rho+q-1,q+p)`.

Summing and using the **exact** balances `sum R=r`, `sum x=sum q=sum p`,
together with (4) and (5), gives

`sum_i ell_{s_i}+sum_u sigma_{rho_u} <= lambda r`.          (6)

A strict reverse inequality excludes the state. All three balance
multipliers may have either sign. This use of free lambda relies on the
exact residual balance, unlike an envelope based only on `sum R<=r`.

Safe local domains include `s=max(0,d-R)`, `0<=d<=dmax`, `x>=s`,
`R+x<=b`, `x<=#{u:rho_u>=s}`, and the source bounds

`0<=q<=min(a-rho,#{i:s_i<=rho})`,

`0<=p<=min(rho+b-a-1,b-1-q)`.

Equation (1) supplies the specialized d values when there is at most one
zero demand. The N34 implementation uses this specialization only after
checking that hypothesis. Any nonnegative combination of indicators
`[d>=D,h<=H]`, `[s>=K,h<=H]`, and `[d-h>=L]` is an admissible F.

## Application and audit boundary

At `(a,b,t)=(15,18,2)`, (1) excludes 463 conservative positive-demand states.
The earlier total-demand lemma then excludes 148. After the original fixed
potential stage, (2) excludes another 51 states, including 11 zero-demand
states. Exact-budget envelopes supply 191 further integer certificates.
See the [N34 proof and ledger](../../n34/2026-09-12-m290-v1/README.md).

These are general graph implications, while complete finite coverage at N34
is proof-critical arithmetic. The separately structured integer verifier is
same-assistant internal verification. External mathematical review, novelty
assessment and external reproduction remain OPEN.
