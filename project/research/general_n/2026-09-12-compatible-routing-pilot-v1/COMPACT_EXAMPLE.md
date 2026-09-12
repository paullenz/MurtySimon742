# A short eligibility-based exclusion

Candidate hand argument, 12 September 2026. External review remains OPEN.
This is N34 m=289 state 4665, selected in the frozen pilot. Its canonical
fixed-order proof already used an envelope; the purpose here is a simpler
general-mechanism explanation.

    a=15, b=18, t=1,
    s=(2^2,4^10,5^3), rho=(1^6,2,3,4^4,5^6).

At h=4 and T=16,

    r=57, W=55, G=208, z=10.

The ordinary heavy-pair bound is

    55 <= 4(10-j)+10j-j(j+1)/2.

For integer j=0..10 it permits only j=5 or j=6. For example its complete
upper-bound list is 40,45,49,52,54,55,55,54,52,49,45.

Use [the compatible-routing inequalities](COMPATIBLE_ROUTING.md) with the
load weight w=1, heavy-demand weight eta=1, receiving weight lambda=2,
ordinary eligibility-tail weight alpha_2=4, and all other weights zero.
For a source let e=1[H>4] and

    V = H(4+f(q+p)) + H - 2He
        + 2 1[rho>=4] min(p,j-e)
        - 4q 1[q>2] + 4p 1[rho+q>=2],
    f(L)=max(0,16-max(4,L)).

The load, heavy-demand, receiving and eligibility bounds imply

    sum V >= 4(G-r)+W = 659.                               (1)

The low-residual sources have very little useful receiving capacity:

- rho=1: no label has demand at most one, hence q=H=0 and V=0.
- rho=2 or 3: H=0 and q<=2; therefore V=4p<=4(rho+2), giving 16 and 20.

For rho=4 or 5, p<=rho+2<=7. All these sources satisfy rho+q>=2. At fixed
H,p, increasing q>=H can only decrease f(q+p) and the term -4q 1[q>2].
Thus it suffices to replace q by H to bound V from above.

If H=0,1,2,3,4, respective upper bounds are 40,53,64,61,64. To verify them,
use min(p,j)<=6, p<=7 and f(H+p)<=16-H-p in this range. For H=3 or 4 also
include the penalty -4H; for H=0,1,2 that penalty is zero. Consequently

    V<=64 whenever H<=4.                                   (2)

For H>=5 the expression becomes

    V <= -H + H(16-H-p)_+ + 2min(p,j-1)+4p.

When H+p<=16, this is

    H(15-H)+(4-H)p+2min(p,j-1).

For H=5, the p-dependent part is at most j-1<=5, giving V<=55.
For H=6 it is nonpositive, giving V<=54. For H>=7 it is again nonpositive,
and the integer quadratic H(15-H) is at most 56. When H+p>=16, the bound
is at most -5+2*5+4*7=33. Therefore

    V<=56 whenever H>4.                                    (3)

There are ten sources with rho>=4, of which exactly j have H>4. Combining
(2)-(3) with the six rho=1 sources and the two other sources gives

    sum V <= 16+20+64(10-j)+56j = 676-8j.

This is 636 for j=5 and 628 for j=6, both strictly below the required 659.
Thus the state is impossible under the bridge conditions.

The important eligibility fact is that a rho=1 source here has q=0, so its
destination score rho+q is one. It cannot receive an arc from any source with
q>=3. The ordinary transport cut at k=2 records this restriction. Counting
that destination's indegree without considering its eligibility loses the
information used in the contradiction.

The displayed source bounds are proved for their full stated domains; the
accompanying finite check is corroboration, not their proof. No graph at this
state is asserted to exist, and no new N34 theorem status is claimed.
