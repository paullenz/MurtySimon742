# Selected-witness Hall cuts for the endpoint/orientation bridge

17 September 2026. Research directed by Paul Lenz; derivation and audit by ChatGPT/Geeps.

**Status: candidate general lemma inside the canonical selected/residual bridge; not promoted; external mathematical review open.** This is a step beyond the excess-aware one-source envelope: it restores the fact that the same selected label cannot independently witness arbitrarily many active B-sources, because label `i` has only `x_i` selected incidences in total.

## 1. Setup inherited from the current bridge

For each B-source `u`, retain residual degree `rho_u` and oriented missing-pair loads `p_u,q_u`, with

    sum_u p_u = sum_u q_u = Q.

For each A-label `i`, retain positive demand `s_i`, selected count `x_i`, selected excess

    e_i=x_i-s_i>=0,

residual column count `R_i`, and endpoint mass

    C_i=R_i+x_i.

The current bridge already supplies the following facts on every selected incidence `ui`:

    s_i <= rho_u,
    e_i >= max(0,p_u-rho_u+1),
    p_u+q_u <= C_i,
    p_u+q_u <= b-1.

It also supplies the crucial implication

    q_u>0  =>  u has at least one selected incidence.

Finally, label `i` has exactly `x_i` selected incidences over all B-sources.

## 2. Capacitated witness Hall theorem

Fix a candidate vector `(p,q,rho)`. Call `u` **active** when `q_u>0`. For an active source define its admissible witness labels

    N(u)={i:
          s_i<=rho_u,
          e_i>=max(0,p_u-rho_u+1),
          C_i>=p_u+q_u}.

(The common pair cap `p_u+q_u<=b-1` must also hold, but it does not depend on `i`.)

In an actual bridge realization, choose one actual selected incidence from each active source. If the chosen incidence at `u` uses label `i`, then `i in N(u)` by the inherited bridge facts. Since label `i` occurs on only `x_i` selected incidences, it can be chosen for at most `x_i` active sources.

Therefore the active sources admit a capacitated matching into the labels, with label capacities `x_i`. Equivalently, the following Hall family is necessary:

> For every subset `S` of active sources,
>
>     |S| <= sum_{i in N(S)} x_i,
>
> where `N(S)=union_{u in S} N(u)`.

This is just Hall's theorem after replacing label `i` by `x_i` clones. The point is not the matching theorem itself; the point is that the current local source envelope deliberately forgot this global reuse budget.

The result is strictly stronger than checking `q_u<=A_u(p_u)` source by source. The one-source envelope asks only whether `N(u)` is nonempty and how much `q` its best label permits. The Hall family remembers that a single good label has finite selected-incidence multiplicity.

## 3. Cheap nested corollaries

The full Hall family need not be enumerated in order to obtain useful cuts.

### Demand-threshold activity cut

For an integer `d`, let

    U_d={u:q_u>0 and rho_u<=d}.

Every witness of a source in `U_d` has `s_i<=d`. Hence

    |U_d| <= X_d := sum_{i:s_i<=d} x_i.                 (1)

This is especially relevant for mixed demand levels: if only a few selected incidences belong to low-demand labels, only that many low-residual sources may carry positive outgoing orientation load.

### Endpoint/excess threshold cut

Let

    g_u=max(0,p_u-rho_u+1).

For integers `d,w,e>=0`, define

    U(d,w,e)={u:q_u>0, rho_u<=d,
                p_u+q_u>=w, g_u>=e}.

Any witness label for such a source must satisfy simultaneously

    s_i<=d, C_i>=w, e_i>=e.

Therefore

    |U(d,w,e)|
      <= sum_{i:s_i<=d, C_i>=w, e_i>=e} x_i.           (2)

This is a compact three-threshold projection of the full witness Hall system.

### Layered outgoing-load cut

Taking `e=0` and using `p_u+q_u>=q_u`, for every `d,j>=1`,

    #{u:rho_u<=d and q_u>=j}
      <= sum_{i:s_i<=d, C_i>=j} x_i.                   (3)

By layer cake,

    sum_{u:rho_u<=d} q_u
      = sum_{j>=1} #{u:rho_u<=d and q_u>=j}
      <= sum_{j>=1} min(n_d, X_{d,j}),                 (4)

where `n_d=#{u:rho_u<=d}` and

    X_{d,j}=sum_{i:s_i<=d,C_i>=j}x_i.

Thus low-residual outgoing load is controlled by the *multiplicity* of compatible selected labels, not merely by the largest endpoint mass among them.

## 4. Strictness example against the one-source envelope

The following bridge-level profile is intentionally small and explicit. It satisfies the scalar ledger, separate selected/residual incidence margins, all displayed local endpoint/excess conditions, the incoming caps, and the excess-aware one-source envelope. It fails only when the globally shared selected-witness budget is restored.

Take

    a=10, b=20, t=0, Q=29.

Labels:

- one low label `L0` with `s=x=2`, `R=4`, `C=6`;
- nine high labels `L1,...,L9` with `s=x=3`;
- for `L1,L2`, take `R=2`, `C=5`;
- for `L3,...,L9`, take `R=3`, `C=6`.

Hence

    sum s=sum x=29,
    sum R=29,
    e_i=0 for every label.

Sources:

    rho=(3^5,2^7,0^8).

Thus `sum rho=29=sum R`, and the exact demand/residual ledger has `sum s=sum rho+2t=29`.

Choose orientation loads as follows.

- On the seven `rho=2` sources take `p=1` and

      q=(5,4,4,4,4,4,4),

  whose outgoing total is 29.
- On the five `rho=3` sources take `p=2,q=0`.
- On two `rho=0` sources take `p=6,q=0`; all other zero-residual sources have `p=q=0`.

Then `sum p=29=sum q`. The inactive incoming caps are

    p_u <= rho_u+b-a-1=rho_u+9,

and are respected. For every active `rho=2` source, the low label is locally admissible: `s=2<=rho`, zero excess allows `p=1`, and `p+q<=6=C_0`. Hence the exact one-source envelope has `q_u<=A_u(p_u)` at every source. In particular all support-function cuts derived solely from those local envelopes are compatible with this displayed `(p,q)` point.

The selected margins themselves are realizable without using the forbidden implication: connect each of the nine high labels to three of the five `rho=3` sources (27 selected incidences in total), and connect `L0` to two of the seven `rho=2` sources. The checker gives an explicit incidence matrix. Residual margins are simultaneously realizable on pairs disjoint from those selected incidences, with row degrees `(3^5,2^7,0^8)` and columns `(4,2,2,3^7)`; again the checker supplies an explicit matrix. Every selected edge in those matrices satisfies the displayed demand, excess and endpoint-load inequalities.

But all seven `rho=2` sources have `q>0`. Their only demand-compatible label is `L0`, whose selected capacity is `x_0=2`. The demand-threshold Hall cut (1) with `d=2` therefore says

    7 <= 2,

which is impossible. The Hall deficiency is 5.

So this profile demonstrates a genuine logical gap between the current one-source envelope and the shared selected-incidence structure: independent local feasibility can reuse the same low-demand label seven times even though only two selected incidences of that label exist.

## 5. Strategic consequence

The preceding uniform demand-four band was closed before this theorem because its low-demand selected capacity is enormous: twenty labels each have `x=4`. The new Hall family is therefore not aimed at re-proving that symmetric band. Its natural target is exactly the next scope frontier identified there: **mixed demand 4/5 profiles and positive selected excess**, where the supply of low-demand witness incidences can become scarce.

Accordingly, the next abstract census should not merely enumerate residual histograms and apply the source envelope. For every candidate `(p,q)` (or for a projected DP state), it should also impose at least the nested cuts (1)-(3), and ideally the full capacitated witness matching when the candidate set is small. This is a structural refinement, not another survivor-count scan.

## 6. Limits

This note does not prove exact-block coverage or the Murty-Simon conjecture. The Hall theorem is conditional on the currently inherited canonical bridge facts, whose independent mathematical review remains open. The strictness example is an abstract bridge profile designed to separate two relaxations; it is not an original graph realization or a counterexample. The theorem also does not yet use pair-choice Hall, target-capacity Hall, or diameter-two criticality, all of which remain available if mixed-demand profiles survive the selected-witness cuts.
