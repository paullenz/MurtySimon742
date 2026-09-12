# N35 candidate bound and equality classification

12 September 2026. Candidate theorem: every simple diameter-two edge-critical
graph G of order 35 has **e(G)<=306**, with equality exactly **K(17,18)**.
Internal proof assembly and exact replay are complete. External mathematical
review, novelty assessment and independent external reproduction remain OPEN.

## 1. Maximum-degree reduction

Write m=e(G), Delta=Delta(G), and consider m>=306. Since 35*17<2*306,
handshaking gives Delta>=18. The existing candidate structural results give:

| Maximum degree | Argument and conclusion |
|---|---|
| 18 | The [balanced-degree theorem](../../general_n/2026-09-12-balanced-degree-v1/BALANCED_DEGREE_THEOREM.md) gives m<=306, equality only K(17,18). |
| 19 | The sole new branch, treated below. |
| 20 | Here (a,b)=(14,20); the [a=14 high-b theorem](../../general_n/2026-09-12-a14-high-b-v1/A14_HIGH_B_SURPLUS_THEOREM.md) gives t=m-15b<=0, hence m<=300. |
| At least 21 | Since 21>=7*35/12, the [7/12 maximum-degree theorem](../../general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md) gives m<306. |

These dependencies are candidate graph theorems with their stated hypotheses;
none is inferred from the new finite computation. The 7/12 result is a logical
dependency of this N35 assembly. Fan's 1987 density theorem is not invoked.

## 2. The Delta=19 branch

Choose the canonical bridge, with `(a,b)=(15,19)` and benchmark
`b(a+1)=304`. Put t=m-304. At m>=306, t>=2. The
[fifteen-label tail theorem](../../general_n/2026-09-12-fifteen-label-tail-v1/FIFTEEN_LABEL_TAIL.md)
gives `19+2t<=Q<=26`, so t<=3. Only m=307 (t=3) and m=306 (t=2) remain.

The [canonical bridge](../../general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md)
supplies demands s_i=max(0,d_i-R_i), residual degrees rho_u, and selected
incidence counts x_i,q_u,p_u. Put S=sum s_i and r=sum rho_u. We use:

- all rho_u>=1, `sum_i R_i=r`, and `sum_i d_i=2(r+t)`;
- `E=S-r-2t=sum_{s_i=0}(R_i-d_i)>=0`;
- on a selected incidence u-i: `s_i<=rho_u`,
  `d_i<=rho_u+q_u-1`, and `R_i+x_i>=q_u+p_u`;
- `q_u+rho_u<=15`, `q_u+p_u<=18`, and `p_u<=rho_u+3`;
- `x_i>=s_i`, `R_i+x_i<=19`, and distinct selected source-label incidences.

Since `19>15-1-t`, an isolated vertex of C=H[A] is impossible. Hence
`d_i<=13`, and `r<=105-t-8`. In particular 0<=s_i<=13.

For h>=2 let W_h=sum_{s_i>=h}s_i and let gamma_h(W_h) be the least z>=h
with `2W_h<=z(z-1)+h(h+1)`, or zero when W_h=0. Actual residual tails satisfy
`#{u:rho_u>=h}>=gamma_h(W_h)`. Their monotone closure gives the minimum
residual multiset rho0. All possible residual multisets dominate rho0
coordinatewise and have sum at most S-2t.

## 3. Complete finite domain

The preserved [complete a=15 enumerator](../../n34/2026-09-12-frontier-v1/enumerate_frontier.cpp)
enumerates all 77,558,760 sorted 15-tuples in 0..14. Its committed
[FRONTIER.csv](../../n34/2026-09-12-frontier-v1/FRONTIER.csv) retains every
nonisolated-C profile with monotone score at least 20. This includes the
entire N35 domain: our thresholds are 25 and 23, and s_i<=13.
No N34-specific m or b assumption is used to discard a relevant CSV row.

`frontier.py` recomputes each score directly from its tails. It expands the
residual domain by recursive nondecreasing sequences above rho0 within the
total slack budget. Any sorted actual rho satisfying the tail lower bounds
dominates rho0; conversely, every such dominating tuple within the sum budget
is visited. The only further filter is the stated isolated-C residual bound.

| Edges | t | Demand profiles | Residual states | Positive-demand states | Zero-demand states |
|---|---:|---:|---:|---:|---:|
| 307 | 3 | 13 | 19 | 19 | 0 |
| 306 | 2 | 144 | 466 | 463 | 3 |

`audit_frontier.py` compares the exact state sets with the earlier breadth
expansion, using b=19 in a fresh imported module. Both implementations agree
on every state. They share the complete demand CSV, whose SHA-256 is pinned.

The three zero-demand states at t=2 are:

| s | rho | E | Exclusion |
|---|---|---:|---|
| (0,3^14) | (1^9,2,3^9) | 0 | Tight subset threshold |
| (0,3,4^13) | (1^8,3,4^10) | 0 | Fixed nine-term envelope |
| (0,4^14) | (1^8,4^11) | 0 | Fixed nine-term envelope |

Thus each zero label has d=R exactly. No free deficit allocation, guessed
zero-label residual count or positive-only formula is used.

## 4. Exclusion rules and exact acceptance

The [exact-budget and tight-subset refinements](../../general_n/2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md)
exclude positive-demand states unless S=r+2t, and exclude a tight heavy
subset when its incoming lower bound exceeds sum_Z(rho_u-1). The
[source-capped threshold lemma](../../general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md)
supplies the third hand rule. Both threshold formulas are recomputed in the
exact verifier rather than accepted from discovery labels.

The remaining states use the existing exact-budget monotone-potential lemma.
For a nonnegative combination F(s,d,L) of rectangle and diagonal indicators,
increasing in s,d and decreasing in L, selected incidences give

`sum_i x_i F(s_i,d_i,R_i+x_i) <= sum_u q_u F(rho_u,rho_u+q_u-1,q_u+p_u)`.

For each integer j from 1 to 15, supplement compatibility also gives
`T_j=sum_{q>=j+1}q-sum_{rho+q>=j}p<=0`.
Choose free multipliers lambda,c,mu and nonnegative tau_j. The saved local
lower bounds ell_s and sig_rho satisfy, for every allowed integer label or
source state,

`ell_s <= lambda R+c x+x F(s,d,R+x)`,

`sig_rho <= mu(q-p)-c q+sum_j tau_j T_j(local)-q F(rho,rho+q-1,q+p)`.

Summing, the potential transport, `sum x=sum q=sum p`, and `sum R=r` imply

`sum_i ell_(s_i)+sum_u sig_(rho_u) <= lambda r`.

Each certificate proves the strict reverse inequality. The local label
domain uses d=R+s when s>0, and d=R-E when s=0; 0<=d<=13,
`s<=x<=min(19-R,#{u:rho_u>=s})`. Source states use
`0<=q<=min(15-rho,#{i:s_i<=rho})` and
`0<=p<=min(rho+3,18-q)`. These are conservative graph domains.

The fixed nine- and thirteen-term potentials are explicitly specified in
`envelopes.py` and independently in `exact_checks.py`. Their old load cutoffs
remain the same graph-level integers, which is valid at b=19; they are not
silently shifted. The adaptive basis covers BC degree thresholds 1..13 and
loads 0..19, SH demand thresholds 1..14 and loads 0..19, and diagonal
thresholds -19..14. Every weight and tau is nonnegative. Free balance
multipliers are not incorrectly restricted in sign.

SciPy proposes coefficients. Integer rounding and one-sided envelope repair
produce candidate certificates, after which every local inequality, bound,
coefficient domain and strict gap is checked with integers. `verify.py`,
`exact_checks.py` and `frontier.py` import no numerical package or discovery
program. A solver status alone never excludes a state.

## 5. Complete disjoint ledger

| Exclusion | m=307 | m=306 | Total |
|---|---:|---:|---:|
| Positive-demand exact degree mass | 2 | 110 | 112 |
| Tight subset threshold | 6 | 93 | 99 |
| Source-capped threshold | 1 | 16 | 17 |
| Fixed nine-term exact envelope | 9 | 151 | 160 |
| Fixed thirteen-term exact envelope | 0 | 3 | 3 |
| Adaptive exact envelope | 1 | 93 | 94 |
| **Total** | **19** | **466** | **485** |
| **Unresolved** | **0** | **0** | **0** |

There are **228 hand/accounting exclusions and 257 exact envelopes**.
The replay checks **92,701 local integer inequalities** (2,588 at m=307,
90,113 at m=306). Every state is covered exactly once. The least negative
accepted gap numerator is -9,552; every saved gap is strictly negative.

## 6. Conclusion and trust boundary

No Delta=19 graph can have m>=306. The degree reduction therefore proves
the candidate bound m<=306 and restricts equality to Delta=18, where the
balanced-degree theorem forces K(17,18). Conversely, K(17,18) has 306 edges,
diameter two, and deleting any edge makes its endpoints have distance three.
It is therefore diameter-two edge-critical and realizes equality.

The full 485-state exclusion is proof-critical finite arithmetic. The new
N34 hand theorem with p<=4 is **not used** here: the generic N35 bound on a
rho=2 source is p<=5. The whole-count N34 model audit is also not a dependency.
Specialist review should prioritize the shared bridge, supplement routing,
exact-budget identity, and completeness of the finite reduction. Separate
internal implementations and clean replay do not establish external acceptance
or an unrestricted all-order solution.
