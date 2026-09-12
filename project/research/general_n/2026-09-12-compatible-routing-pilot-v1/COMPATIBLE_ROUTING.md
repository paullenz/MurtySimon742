# Selected-degree eligibility and compatible heavy routing

12 September 2026. Candidate general graph inequalities. Internal checks pass;
external mathematical review and novelty assessment remain OPEN.

Use the [canonical selected/residual bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
For a selected arc u->v, it gives

    rho_v + q_v >= q_u - 1.

This implication and the ordinary transport tails below already appear in
the preserved RX-Hall machinery. This study tests their combination with
heavy-load routing; it does not claim to discover that implication anew.

Fix h>=1, let H_u be the actual number of selected incidences from u to labels
of demand at least h, and put

    Z={u:rho_u>=h}, z=|Z|, J={u:H_u>h}, j=|J|,
    e_u=1[u in J], F_u=e_u H_u, O_u=q_u-F_u,
    m_u=1[u in Z] min(p_u,j-e_u), E_k={u:rho_u+q_u>=k}.

F counts heavy arcs from high senders; O counts all other selected arcs.
These are disjoint classes and exhaust the selected arcs. Every F arc ends
in Z. At a destination v there can be at most one such arc from each member
of J other than v, so its F-indegree is at most m_v.

## 1. Eligibility tails and a mixed cut

Every selected arc with q_u>k ends in E_k. Therefore

    A_k = sum_u q_u 1[q_u>k] - sum_{u in E_k} p_u <= 0.       (1)

For forced heavy arcs this strengthens to

    B_k = sum_u F_u 1[q_u>k] - sum_{u in E_k} m_u <= 0.       (2)

For any nonnegative integer cutoffs k and ell, the following is necessary:

    C_(k,ell) = sum_u O_u 1[q_u>k] + sum_u F_u 1[q_u>ell]
               - sum_{u in E_k} p_u
               - sum_{u in E_ell minus E_k} m_u <= 0.        (3)

Proof: the chosen O arcs end in E_k; the chosen F arcs end in Z intersect
E_ell. At a destination in E_k their combined indegree is at most p. Outside
E_k only the chosen F arcs can arrive, and their indegree is at most m.
Summing these disjoint destination contributions gives (3). This proof
counts actual arcs and uses neither a solver nor a fractional realization.

If ell>=k, E_ell is contained in E_k and (3) is implied by (1): the selected
traffic is then a subset of all arcs from q>k. The potentially stronger mixed
cuts have ell<k. Under rho+q<=a, cutoffs 0..a+1 include the full and empty
eligibility sets. No sufficiency for a routing or graph is asserted.

## 2. Retaining q in the load argument

Let T>=h, f(L)=max(0,T-max(h,L)),

    W=sum_{s_i>=h} s_i, G=sum_{s_i>=h} max(T,s_i), r=sum rho_u.

The [heavy-label load argument](../2026-09-12-heavy-load-family-v1/HEAVY_LOAD_FAMILY.md)
gives hR_i+hx_i+x_i f(R_i+x_i)>=h max(T,s_i).
Endpoint load R_i+x_i>=q_u+p_u, together with the decreasing f, gives

    hG <= hr + sum_u L_u,
    L_u = H_u (h+f(q_u+p_u)).                               (4)

This retains the total selected degree q; replacing it by H would weaken
the bound. Also

    sum H_u >= W, sum(q_u-p_u)=0,
    sum F_u <= K_j=j(z-j)+j(j-1)/2,
    sum(F_u-m_u)<=0.                                        (5)

The pair bound uses one orientation per missing unordered pair. The receiving
bound retains destinations with H=0, including destinations outside J.

## 3. A parameterized envelope

Choose nonnegative rational weights w, eta, mu, lambda, alpha_k, beta_k and
gamma_(k,ell), with finite support, and an arbitrary rational nu. Write a_k(u),
b_k(u), c_(k,ell)(u) for the individual summands in (1), (2), (3). Define

    V_u = w L_u + eta H_u - mu F_u - lambda(F_u-m_u)
          - sum alpha_k a_k(u) - sum beta_k b_k(u)
          - sum gamma_(k,ell) c_(k,ell)(u) - nu(q_u-p_u).

Equations (1)-(5) imply

    w h G <= w h r + sum V_u + mu K_j - eta W.               (6)

For each residual degree rho, bound V locally over integer source options:

    q+rho<=a, q+p<=b-1, 0<=p<=rho+b-a-1,
    0<=H<=min(q, #{i:h<=s_i<=rho}),
    0<=q-H<=#{i:s_i<h and s_i<=rho}.

All q,p,H are nonnegative. Positive surplus supplies rho>=1 in the present
application. The cut and load lemmas themselves only need their stated bridge
hypotheses. Zero-demand labels contribute to the light-label eligibility
count and require no assertion that their label degree equals their residual.

Let V_rho(0) and V_rho(1) be the maxima with e=0 and e=1, respectively. Since
exactly j sources have e=1, let M_j be the sum of the e=0 maxima plus the j
largest available differences V_rho(1)-V_rho(0), with multiplicities. Then

    w h G <= w h r + M_j + mu K_j - eta W.                  (7)

Any actual j must satisfy (7). A state is excluded only when every possible
j fails, possibly using the existing source-capacity rule for some j values.
w=0 is allowed: such a certificate rules out the source/transport data even
without using the load inequality. A nonempty class must have an allowed
local option; an empty required class is separately impossible.

This is a general hand implication with arbitrary parameters, not an assertion
of a new all-order density theorem. The finite local maxima in an application
may still require exact arithmetic. Normalization multipliers and artificial
LP variable-bound rows are absent from (7).

## 4. What the pilot establishes

For the catalogue-free baseline comparison, weaken f(q+p) to f(H+p), omit
q and the transport constraints, and use the preceding heavy-only local
domains. Monotonicity of f justifies that weakening; sources outside Z then
have zero cost and can be omitted from the maxima.

All 321 successful integer witnesses from the bounded pilot were converted
to (7) or this explicitly stated baseline weakening, with positive integer gaps.
A separately structured verifier checks
their local maxima and uses per-source cardinality dynamic programming instead
of the extraction program's sorting. A [compact example](COMPACT_EXAMPLE.md)
proves the needed source maxima by hand.

The tested mixed cuts add no whole-state exclusions beyond the separate tails.
Their validity is proved above, but this pilot establishes no additional
whole-state benefit from them. The useful measured gain is retaining
selected-degree destination eligibility in the heavy-load argument.
