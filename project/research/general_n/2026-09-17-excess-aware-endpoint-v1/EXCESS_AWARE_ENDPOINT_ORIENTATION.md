# Excess-aware endpoint-orientation support cuts

17 September 2026. Research directed by Paul Lenz; derivation and audit by ChatGPT/Geeps.

**Status: candidate general lemma inside the canonical selected/residual bridge; not promoted; external mathematical review open.** This strengthens the preceding global endpoint-orientation cut by retaining the established selected-excess restriction instead of maximizing over all demand-compatible labels independently of the incoming load.

## 1. Setup

Work in the all-positive-demand canonical branch used by the preceding common-margin theorem. For every source `u in B` retain outgoing and incoming missing-pair orientation loads `q_u,p_u`, residual degree `rho_u`, and

    sum_u q_u = sum_u p_u =: Q.                         (1)

For every A-label i retain selected count x_i, demand s_i>0, residual column count R_i, endpoint mass

    C_i=R_i+x_i,

and selected excess

    e_i=x_i-s_i>=0.

The inherited bridge facts used here are:

- if q_u>0 then some selected incidence ui exists;
- on every selected incidence, `s_i<=rho_u`;
- endpoint load gives `p_u+q_u<=C_i`;
- incoming orientation caps give `p_u+q_u<=b-1` and `p_u<=rho_u+b-a-1`;
- the established selected-excess condition gives

    e_i >= max(0,p_u-rho_u+1)                          (2)

  whenever ui is selected.

The last condition is the information omitted by the preceding `M_u=max C_i` projection.

## 2. Exact local source envelope

Put

    P_u^0=min(b-1,rho_u+b-a-1).

For an integer incoming load `0<=p<=P_u^0`, define

    A_u(p)=max q

where the maximum is over q=0 and all integers q>=1 for which there exists a label i satisfying

    0<s_i<=rho_u,
    e_i>=max(0,p-rho_u+1),
    p+q<=C_i,
    p+q<=b-1.                                           (3)

Equivalently,

    A_u(p)=max( {0} union
      { min(C_i-p,b-1-p) : i satisfies the first two conditions } ),

with negative candidates discarded.

Every legal source therefore satisfies

    q_u <= A_u(p_u).                                    (4)

Consequently the exact source-envelope projection gives the necessary condition

    Q <= Phi(Q):=
         max { sum_u A_u(p_u) :
               0<=p_u<=P_u^0 integers,
               sum_u p_u=Q }.                          (5)

This is a one-dimensional dynamic programme in the incoming total, not a graph search and not a relaxation over independently chosen incoming and outgoing maxima.

## 3. Weighted support-function family

For nonnegative integer weights alpha,beta, define

    H_u(alpha,beta)=
      max_{0<=p<=P_u^0} [ alpha A_u(p)+beta p ].         (6)

Then (1) and (4) imply the whole family of necessary cuts

    (alpha+beta)Q <= sum_u H_u(alpha,beta).             (7)

The preceding global endpoint ceiling is a coarser member of this philosophy: it bounds p+q without allowing the admissible label set to shrink with p. Equation (7) can be strictly stronger because a high incoming load may require selected excess that the largest endpoint-mass label does not possess.

The exact DP (5) dominates every single support-function cut, while a small integer pair `(alpha,beta)` can often give a short hand certificate.

## 4. Strictness example: a non-square abstract profile

The refinement is genuinely stronger than the previous `2Q<=sum B_u` cut. Consider

    a=20, b=23, t=2, Q=80,
    rho=(5^7,4^8,2,1^7).

Take twenty labels with

    s_i=x_i=4,
    e_i=0,

and residual column counts

    R=(5,4^14,3^5).

Then

    C=(9,8^14,7^5),
    sum rho=sum R=76,
    r+2t=76+4=80=sum s.

The residual h-index is 5, with seven sources at or above five, while there are no demand-five labels. Thus this is deliberately non-square.

Basic degree compatibility is not the obstruction: `(9,8^14,7^5)` is graphical, and the residual bipartite margins `rho` and `R` satisfy Gale-Ryser.

### Previous common-margin cut passes exactly

For rho=5 or 4 the largest demand-compatible endpoint mass is 9. The inactive incoming ceilings are 7,6,4,3 for rho=5,4,2,1 respectively. Hence the preceding pointwise bounds are

    B=9 on the seven rho-5 sources,
    B=9 on the eight rho-4 sources,
    B=4 on the rho-2 source,
    B=3 on the seven rho-1 sources.

Therefore

    sum B_u = 7*9+8*9+4+7*3 = 160 = 2Q.                (8)

So the previous global endpoint-orientation cut does not reject this profile.

### Excess-aware cut rejects it

Because every label has e=0, (2) says an active source must satisfy `p<=rho-1`. Use the weighted cut `(alpha,beta)=(2,3)`.

For rho=5, an active source has `p<=4` and `q<=9-p`, so

    2q+3p <= 18+p <=22.

If inactive, `p<=7`, giving at most 21. Thus H_5=22.

For rho=4, active `p<=3` gives at most 21; inactive `p<=6` gives at most 18. Thus H_4=21.

The rho-2 and rho-1 sources have no demand-compatible label, so their maxima are purely incoming:

    H_2=3*4=12,
    H_1=3*3=9.

Summing,

    sum H_u
      =7*22+8*21+12+7*9
      =397.                                             (9)

But (7) requires

    5Q=400 <=397,

which is impossible. Thus this profile passes the preceding basic common-margin cut at equality but fails the excess-aware refinement.

The exact DP is stronger still: at total incoming load 80 it allows at most 78 outgoing units. The weighted hand cut already certifies impossibility, since `2 sum q + 3*80 <=397` forces `sum q<=78`.

## 5. Audit and limits

`check_excess_aware_endpoint_orientation.py` independently reconstructs the source curves, the previous basic cut, the `(2,3)` support cut, the exact incoming-total DP, Erdős-Gallai for the F-degree sequence and Gale-Ryser for the residual bipartite margins. A separately written C++ checker reproduces the key common-margin and DP totals.

The strict profile is an abstract bridge-level profile, not an original diameter-two edge-critical graph and not a Murty-Simon counterexample. Its purpose is to establish that the excess-aware cut adds real information beyond the previously published common-margin inequality.

The theorem itself is general inside the stated canonical bridge assumptions. It does not show that (5) alone forces an exact square block, and it does not replace pair uniqueness, target-capacity Hall, selected-incidence Hall or graph criticality.

## 6. Next target

The next useful step is no longer to ask whether excess helps: it does, strictly. Instead search the abstract non-square frontier **after** (5). Preserve the smallest profile that satisfies the staircase/heavy-load system, the basic common-margin cut and the full excess-aware source envelope. If no such profile survives in a justified parameter band, extract a hand inequality from the active support-function weights before invoking the more expensive Hall systems.
