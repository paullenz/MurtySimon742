# Closed local maxima for a compatible-routing potential

Candidate general lemma, 12 September 2026. External review and novelty OPEN.
This extends the preceding [cutoff-2 analytic reduction](../2026-09-12-compatible-routing-catalogue-v1/FIXED_POTENTIAL.md).

## 1. Potential and source domain

Assume the canonical positive-surplus bridge, a>=2, b>=a, rho>=1 and h>=2.
Fix any integer eligibility cutoff k>=0 and an actual heavy-sender count j.
Let H count heavy selected incidences, q all selected incidences, p supplement
indegree and e=1[H>h]. Put

    f(L)=(4h-max(h,L))_+,
    V=H(h+f(q+p))+H-2eH+2 1[rho>=h] min(p,j-e)
      -4q 1[q>k]+4p 1[rho+q>=k].                         (1)

These are fixed weights: load 1, heavy demand 1, heavy receiving 2, ordinary
eligibility tail 4. The [general compatible-routing implication](../2026-09-12-compatible-routing-pilot-v1/COMPATIBLE_ROUTING.md)
gives

    h(G-r)+W <= sum V,
    W=sum_(s_i>=h) s_i, G=sum_(s_i>=h) max(4h,s_i), r=sum rho. (2)

For a source of residual rho, let u be its count of eligible heavy labels
and v its count of eligible light labels. The local integer domain is

    0<=H<=u, H<=q<=H+v, q+rho<=a,
    0<=p<=rho+b-a-1, q+p<=b-1.

The low sender class has H<=h; the high class H>h and requires j>=1.
The domain is a necessary-condition relaxation, not a routing realization.

## 2. Two selected-degree branches suffice

Fix H,p. Away from the destination-indicator jump at q=k-rho, the potential
is nonincreasing with q: f decreases, and -4q 1[q>k] is nonincreasing.
Consequently an exact local maximum is attained in one of two branches:

    q=H, or q=D=k-rho with D>=H, when locally feasible.    (3)

To justify completeness, split the allowed q interval below and at/above D.
Its smallest allowed q below D is H. If an allowed q reaches D while H<D,
then D is also allowed: lowering q preserves q+rho<=a, q+p<=b-1 and
q-H<=v. If H>=D, the whole allowed interval is nonincreasing and q=H
suffices. Repeating a point when H=D is harmless. This argument includes
zero-demand labels in v and needs no special label-degree convention.

## 3. The q=H branch has finitely many quadratic pieces

Write C=min(a-rho,u), R=rho+b-a-1, B=b-1 and J=j-e. Fix a sender class,
whose H interval is [0,min(C,h)] or [h+1,C]. Empty classes are omitted.
Then p lies in [0,min(R,B-H)]. For each fixed H, the potential is piecewise
affine in p, with breakpoints h-H, 4h-H and J. Thus the exact p maximum
occurs on one of these six affine branches, whenever feasible:

    p=0, p=R, p=J, p=B-H, p=h-H, p=4h-H.                  (4)

The two branches R and B-H split the upper endpoint min(R,B-H).
Each branch p=c+dH has d=0 or -1. Its feasible H domain is an integer
interval, obtained by intersecting the sender class with 0<=p<=R and H+p<=B.

Partition that interval where any formula changes:

- the source penalty changes at the first integer H=k+1;
- destination eligibility changes at the first integer H=D;
- for d=0 the ramp changes at H=h-c+1 and H=4h-c;
- for d=-1 the receiving minimum changes at H=c-J.

The other ramp/receiving expression is constant along the respective branch.
These are integer boundaries. There are at most five pieces for each of the
three constant-p branches and four pieces for each of the three slope-minus-one
branches: at most 27 pieces in total per sender class.

On a piece, (1) has the form

    A H^2 + Q H + K, with A in {0,-1}.                    (5)

Indeed the only quadratic contribution is H f(H+p). In the middle ramp
region it contributes -(1+d)H^2; outside it the expression is affine.
The indicator values and the branch of min(p,J) are fixed on each piece.

For an integer interval [L,U], an affine expression attains its maximum at
an endpoint. For -H^2+QH+K, complete the square: the maximizing integers
are among floor(Q/2) and ceil(Q/2), each clipped to [L,U]. Checking
floor(Q/2) and floor(Q/2)+1 is equivalent and harmless when Q is even.
Use mathematical floor for negative Q. Hence at most two candidate values
per piece suffice, without enumerating its H values.

## 4. The q=D branch is simpler

This branch exists only if 0<=D<=a-rho. Intersect the sender-class H interval
with [D-v,D]; also require P=min(R,B-D)>=0. If nonempty, p lies in [0,P],
independently of H. Since rho>=1, D=k-rho<k, so the source penalty vanishes
and the destination indicator is one. At fixed p, the coefficient of H is

    h+f(D+p)+1-2e >= h-1 > 0.                            (6)

Thus choose the largest allowed H. The remaining p maximum occurs at

    {0,P} union ({h-D,4h-D,J} intersect [0,P]),             (7)

at most five values. This recovers the earlier residual-one correction as
a special case when k=2, rho=1 and H=0.

## 5. Closed formula and global envelope

Define V_rho(e) as the maximum of the explicit values from (5) on the
partitioned branches (4), together with (7). At most

    27*2+5 = 59 candidate values                         (8)

are needed per source residual and sender class, regardless of graph order
or degree magnitudes. All expressions and interval endpoints are explicit
integer formulas in a,b,rho,h,k,j and the eligible-label counts u,v.
This is a closed, constant-size formula with case distinctions, not a single
polynomial or a proof that all source maxima can occur together.

Let M_(h,k,j) be the sum of all low-class maxima plus the j largest available
high-minus-low differences with source multiplicities. Then

    h(G-r)+W <= M_(h,k,j)                                (9)

is necessary for the actual j. Source-capacity exclusions can dispose of
other j values. Different j cases may use different k values; each k gives a
valid inequality. Every possible j must fail before a state is excluded.

The derivation preserves the exact local relaxation. Any additional reach
over the old cutoff-2 potential must come from changing k, not from the closed
evaluation itself. The hand proof supplies the general claim; the accompanying
finite checks challenge its algebra, boundaries, rounding and applications.
