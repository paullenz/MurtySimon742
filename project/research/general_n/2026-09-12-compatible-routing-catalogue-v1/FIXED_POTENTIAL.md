# The recurring potential: an exact analytic reduction

12 September 2026. Candidate bridge consequence; external review and novelty
OPEN. This reduction was derived after the frozen catalogue replay. It adds
no templates or excluded states to that experiment.

The same primitive weights used in the preceding compact hand example suffice
for 707 of the 990 catalogue exclusions at their recorded winning thresholds.
They are load=1, heavy demand=1, heavy receiving=2, ordinary eligibility at
cutoff 2=4. They work at h=4 and h=5 in the present data. Their validity as a
potential is already proved in the [general compatible-routing lemma](../2026-09-12-compatible-routing-pilot-v1/COMPATIBLE_ROUTING.md).
The result below simplifies its exact local maxima for arbitrary h>=2.

## Hypotheses and inequality

Use the canonical positive-surplus bridge with a>=2, b>=2, delta=b-a>=0,
and every source residual rho>=1. Fix h>=2 and an actual high-sender count j.
Let H count selected incidences to labels with s>=h, q count all selected
incidences, p be supplement indegree, and e=1[H>h]. Put

    f(L)=(4h-max(h,L))_+,
    m=1[rho>=h] min(p,j-e),
    V=H(h+f(q+p))+H-2eH+2m
      -4q 1[q>2]+4p 1[rho+q>=2].

Only options compatible with the chosen j are allowed; in particular j=0
forbids e=1. With W=sum_(s>=h) s, G=sum_(s>=h) max(4h,s) and r=sum rho,
the load, demand, receiving and ordinary transport inequalities imply

    h(G-r)+W <= sum V.                                    (1)

These weights are fixed; no optimization or solver is used in (1).

## 1. Eliminate q exactly from each local maximum

For rho>=2, the destination indicator in V is always one. At fixed H,p,
the dependence on q is through the decreasing f(q+p) and the nonincreasing
function -4q 1[q>2]. Therefore V is nonincreasing as q increases above H.
Moreover q=H is itself an allowed local option whenever

    0<=H<=C_rho=min(a-rho, #{i:h<=s_i<=rho}),
    0<=p<=P_rho(H)=min(rho+delta-1,b-1-H).

Indeed it uses no light labels and satisfies both selected-degree bounds.
Thus the exact local maximum in either sender class is attained at q=H.
It is the maximum of

    Phi(H,p)=H(h+f(H+p))+H-2eH
             +2 1[rho>=h] min(p,j-e)
             -4H 1[H>2]+4p.                               (2)

This is an assertion about a local maximum in the necessary-condition
relaxation. It does not replace the actual q by H in a graph or assert that
local maximizers can coexist in a graph.

For rho=1, H=0 because h>=2. If no label has s<=1, then q=0 and V=0.
Otherwise q=1 is locally available. For q=1 or 2 the value is 4p; for q>=3
it is 4p-4q. The cap p<=min(delta,b-1-q) cannot increase with q. Hence
the exact residual-one maximum is

    B_1 = 0                              if #{i:s_i<=1}=0,
          4 min(delta,b-2)               otherwise.       (3)

The q=0 option gives zero, and delta>=0 makes (3) nonnegative. These sources
are always in the low-sender class. Zero-demand labels are included in the
eligibility count; no equality of their label degree and residual is used.

## 2. Eliminate the full p enumeration

For fixed H, the expression (2) is piecewise affine in p. Its only possible
interior breakpoints are

    p=h-H, p=4h-H, p=j-e.

Therefore its exact maximum over integer p in [0,P_rho(H)] occurs among

    {0, P_rho(H)} union
    ({h-H,4h-H,j-e} intersect [0,P_rho(H)]).                (4)

All breakpoints are integers. Between adjacent breakpoints an affine
function attains its maximum at an endpoint, including the constant case.
If rho<h, the j-e breakpoint is harmlessly redundant. Thus at most five
p values need checking for each H, independently of the size of b.

Compute low and high maxima using (2)-(4) with H<=h and H>h respectively;
use (3) for rho=1. Sum the low maxima and add the j largest available
high-minus-low differences with source multiplicities. Denote the result M_j.
Then the fixed potential yields the necessary condition

    h(G-r)+W <= M_j.                                      (5)

Every actual j must satisfy (5). Whole-state exclusion still requires
covering every possible j, using the existing source-capacity rule where
applicable. The local maxima are a relaxation and give no routing sufficiency.

## What was learned

The recurring eligibility potential admits exact maxima without enumerating
q and with at most five p candidates per H. It exposes the loss at residual-one
destinations directly: if no demand is at most one, their local contribution
is zero even when an indegree cap alone would permit a positive value.
The penalty on sources with H>2 remains visible in (2).

The [reduction checker](check_fixed_potential.py) compares these analytic
maxima with every recorded full-model gap for this template, including failed
attempts. The hand argument above establishes the parameterized reduction;
the finite comparison corroborates it on the stated pool. The 707 applications
still use exact maxima and complete j coverage; they are not 707 separately
written hand proofs or a new density theorem.

This suggests a focused next mathematical target: find a closed bound for the
remaining H maximum, then test which hypotheses make that bound sharp enough
on the 4,584 combined survivors. Actual arc allocation and fuller label-degree
compatibility remain absent from the relaxation.
